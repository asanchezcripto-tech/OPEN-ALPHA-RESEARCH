"""Offline integrity checks of this research delivery; never runs external projects."""
import collections
import csv
import json
import pathlib
import re
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parents[1]
I = ROOT / 'inventories'
errors = []
checks = collections.Counter()
tables = {}

def check(condition, message, kind):
    checks[kind] += 1
    if not condition:
        errors.append(message)

for path in sorted(I.glob('*.json')):
    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data, list):
        continue
    tables[path.stem] = data
    ids = [r['id'] for r in data if 'id' in r]
    check(len(ids) == len(set(ids)), f'{path.name}: duplicate IDs', 'unique_ids')
    csvpath = path.with_suffix('.csv')
    check(csvpath.exists(), f'{csvpath.name}: missing', 'csv_json_parity')
    if csvpath.exists():
        with csvpath.open(encoding='utf-8-sig', newline='') as stream:
            rows = list(csv.DictReader(stream))
        check(len(rows) == len(data), f'{path.name}: row count differs from CSV', 'csv_json_parity')
        for n, (expected, actual) in enumerate(zip(data, rows), 1):
            for key, value in expected.items():
                serialized = (json.dumps(value, ensure_ascii=False)
                              if isinstance(value, (list, dict))
                              else '' if value is None else str(value))
                check(actual.get(key) == serialized,
                      f'{path.name}:{n}:{key}: CSV value differs', 'csv_json_values')

projects = {r['id']: r for r in tables['projects']}
sources = {r['id']: r for r in tables['sources']}
evidence = {r['id']: r for r in tables['evidence']}
all_ids = {r['id'] for table in tables.values() for r in table if 'id' in r}
limits = dict(utility=25, evidence=15, data=15, ease=12, license=10,
              maintenance=8, usability=8, differentiation=7)
allowed = {'REUTILIZACIÓN POTENCIALMENTE COMPATIBLE', 'COMPATIBLE CON OBLIGACIONES',
           'SOLO INVESTIGACIÓN / RESTRICCIONES', 'LICENCIA NO VERIFICADA',
           'NO RECOMENDADO PARA EL USO PREVISTO'}
for name, data in tables.items():
    for row in data:
        label = f"{name}/{row.get('id', '?')}"
        for sid in row.get('source_ids', []):
            check(sid in sources, f'{label}: missing source {sid}', 'source_references')
        for eid in row.get('evidence_ids', []):
            check(eid in evidence, f'{label}: missing evidence {eid}', 'evidence_references')
        for field in ['source_id', 'evidence_source_id']:
            if row.get(field):
                check(row[field] in sources, f'{label}: missing {field} {row[field]}', 'source_references')
        for cid in row.get('candidate_ids', []):
            check(cid in projects, f'{label}: missing candidate {cid}', 'candidate_references')
        if row.get('candidate_id'):
            check(row['candidate_id'] in projects, f"{label}: missing candidate_id {row['candidate_id']}", 'candidate_references')
        scores = row.get('scores')
        if isinstance(scores, dict):
            check(set(scores) == set(limits), f'{label}: score dimensions mismatch', 'scores')
            for key, value in scores.items():
                check(isinstance(value, (int, float)) and 0 <= value <= limits.get(key, -1),
                      f'{label}: invalid score {key}={value}', 'scores')
            if row.get('score_total') is not None:
                check(sum(scores.values()) == row['score_total'], f'{label}: score total differs', 'scores')
        if name == 'projects':
            check(row.get('license_status') in allowed, f'{label}: invalid license class', 'license_classes')
            check(row.get('tests_executed') is False, f'{label}: execution status not false', 'static_scope')
            check(row.get('verification_level') in {'V1', 'V2', 'V3', 'D0'}, f'{label}: bad level', 'verification_levels')
            if row.get('verification_level') == 'V3':
                check(bool(row.get('deep_review_path')), f'{label}: V3 has no review', 'deep_reviews')
            if row.get('verification_level') == 'D0':
                check(row.get('score_total') is None and row.get('verified_at') is None,
                      f'{label}: unverified row has score/date', 'verification_levels')
        for field in ['deep_review_path', 'blueprint_path']:
            if row.get(field):
                check((ROOT / row[field]).is_file(), f'{label}: missing {row[field]}', 'artifact_paths')

for row in tables['relations']:
    for field in ['from_id', 'to_id']:
        if row.get(field):
            check(row[field] in all_ids or bool(row.get(field.replace('_id', '_url')))
                  or bool(row.get('external_node')),
                  f"relations/{row['id']}: unresolved node {field}={row[field]}", 'graph_nodes')

required = ['README.md', 'RESEARCH_PROTOCOL.md', 'QUALITY_REVIEW.md',
            '00_EXECUTIVE_BRIEF.md', '01_SEARCH_COVERAGE.md', '02_PROJECT_CATALOG.md',
            '03_DEEP_TECHNICAL_REVIEWS/README.md', '04_ALGORITHMS_AND_METHODS.md',
            '05_MODELS_AND_DATASETS.md', '06_DATA_AND_INFRASTRUCTURE.md',
            '07_LICENSE_AND_RISK_MATRIX.md', '08_TECHNOLOGY_COMPARISONS.md',
            '09_HIDDEN_GEMS.md', '10_NOVEL_COMBINATIONS.md', '11_PRODUCT_OPPORTUNITIES.md',
            '12_TOP_FIVE_BLUEPRINTS/README.md', '13_RESEARCH_BACKLOG.md',
            '14_FINAL_STRATEGIC_VERDICT.md', 'inventories/stage_log.json', 'inventories/README.md']
for relative in required:
    check((ROOT / relative).is_file(), f'Missing required artifact {relative}', 'required_artifacts')

markdown_files = [p for p in ROOT.rglob('*.md') if '.working_cache' not in p.parts]
for path in markdown_files:
    text = path.read_text(encoding='utf-8')
    check('\ufffd' not in text, f'{path.relative_to(ROOT)}: replacement character', 'encoding')
    # URLs and inline code are not filesystem references. Check local Markdown links.
    for link in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', text):
        link = link.strip('<>')
        if re.match(r'[A-Za-z][A-Za-z0-9+.-]*:', link) or link.startswith('#'):
            continue
        target = urllib.parse.unquote(link.split('#', 1)[0])
        if target:
            check((path.parent / target).exists(),
                  f'{path.relative_to(ROOT)}: broken local link {link}', 'local_links')
    check(not re.search(r'\]\((?:None|null|undefined)\)', text),
          f'{path.relative_to(ROOT)}: null URL', 'local_links')

stats = json.loads((I / 'coverage_stats.json').read_text(encoding='utf-8'))
check(stats['catalog_resources'] == len(projects), 'Catalog statistic mismatch', 'counts')
check(stats['directly_verified'] == sum(p['verification_level'] != 'D0' for p in projects.values()),
      'Verified statistic mismatch', 'counts')
check(stats['verification_levels'] == dict(collections.Counter(p['verification_level'] for p in projects.values())),
      'Level statistic mismatch', 'counts')
check(stats['deep_reviews'] == len([p for p in projects.values() if p.get('deep_review_path')]),
      'Deep review statistic mismatch', 'counts')
check(15 <= len(tables.get('selected_components', [])) <= 25, 'Selection count outside target', 'counts')
check(len(tables['opportunities']) >= 12, 'Too few concepts', 'counts')
check(len([p for p in tables['opportunities'] if p.get('blueprint_path')]) == 5, 'Blueprint count differs', 'counts')

result = {'status': 'PASS' if not errors else 'FAIL', 'scope': 'Integridad de entrega, sin tests de terceros ni validación empírica.',
          'checked_at': '2026-11-04', 'checks': dict(checks), 'total_checks': sum(checks.values()),
          'errors': errors, 'external_urls_rechecked_in_this_pass': False,
          'markdown_files_checked': len(markdown_files)}
(I / 'quality_checks.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(1 if errors else 0)
