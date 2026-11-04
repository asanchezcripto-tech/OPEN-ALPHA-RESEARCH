"""Read-only public-source inspection; stdlib only. Never imports inspected code.

Caches are local working material, excluded from the delivery archive and git.
Metadata records hashes/URLs, not a claim that remote software was executed.
"""
import concurrent.futures, hashlib, json, pathlib, re, sys, time, urllib.error, urllib.request
ROOT = pathlib.Path(__file__).resolve().parents[1]
CACHE = ROOT / '.working_cache' / 'infra'
CACHE.mkdir(parents=True, exist_ok=True)

def fetch(url, limit=1800000):
    key = hashlib.sha256(url.encode()).hexdigest()
    meta_path = CACHE / (key + '.json')
    body_path = CACHE / (key + '.txt')
    if meta_path.exists():
        meta = json.loads(meta_path.read_text(encoding='utf-8'))
        return meta, body_path.read_text(encoding='utf-8') if body_path.exists() else ''
    meta = {'url': url, 'accessed_at': '2026-11-04', 'status': None}
    body = ''
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'OpenAlpha-public-research/1.0'})
        with urllib.request.urlopen(req, timeout=25) as response:
            raw = response.read(limit + 1)
            meta.update(status=response.status, final_url=response.url, bytes=len(raw), truncated=len(raw)>limit,
                        sha256=hashlib.sha256(raw).hexdigest(), last_modified=response.headers.get('Last-Modified'))
            body = raw[:limit].decode('utf-8', errors='replace')
    except Exception as exc:
        meta['status'] = getattr(exc, 'code', 'error')
        meta['error'] = str(exc)[:250]
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
    if body:
        body_path.write_text(body, encoding='utf-8')
    return meta, body

def inspect_repo(item):
    url = item['url'].rstrip('/')
    meta, html = fetch(url)
    result = dict(item, fetch=meta)
    if meta['status'] != 200:
        return result
    result['current_oid'] = next(iter(re.findall(r'"currentOid":"([0-9a-f]{40})"', html)), None)
    result['default_branch'] = next(iter(re.findall(r'"defaultBranch":"([^"]+)"', html)), None)
    result['license_label'] = next(iter(re.findall(r'"spdxId":"([^"]+)"', html)), None)
    result['archived_notice'] = 'This repository was archived by the owner' in html
    result['fork_notice'] = next(iter(re.findall(r'forked from\s*<a[^>]*href="([^"]+)"', html)), None)
    result['paths'] = list(dict.fromkeys(re.findall(r'"path":"([^"\n]+)"', html)))[:100]
    result['relative_dates'] = list(dict.fromkeys(re.findall(r'datetime="([^"]+)"', html)))[:8]
    result['release_tags'] = list(dict.fromkeys(re.findall(r'/releases/tag/([^"<]+)', html)))[:3]
    repo = '/'.join(url.split('/')[-2:])
    sha = result['current_oid'] or result['default_branch']
    result['inspected_files'] = []
    if sha:
        candidates = [p for p in result['paths'] if '/' not in p and re.match(r'(?i)(readme|licen[cs]e|copying)(\.|$)', p)]
        for path in candidates[:4]:
            file_meta, content = fetch('https://raw.githubusercontent.com/' + repo + '/' + sha + '/' + path)
            result['inspected_files'].append(dict(file_meta, path=path))
    return result

if __name__ == '__main__':
    seeds = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'))
    dest = pathlib.Path(sys.argv[2])
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for row in pool.map(inspect_repo, seeds):
            results.append(row)
            dest.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
            print(row['id'], row['fetch']['status'], row.get('current_oid'), row.get('license_label'), flush=True)
