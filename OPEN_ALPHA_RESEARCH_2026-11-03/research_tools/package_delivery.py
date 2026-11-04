"""Package only research artifacts and our own helpers; no network or publication."""
import datetime
import hashlib
import json
import pathlib
import re
import zipfile

ROOT=pathlib.Path(__file__).resolve().parents[1]
ARCHIVE=ROOT.parent/(ROOT.name+'.zip')
EXCLUDED={'.working_cache','__pycache__','.git'}
ALLOWED={'.md','.json','.csv','.py'}
manifest_path=ROOT/'FILE_MANIFEST.json'
qa=json.loads((ROOT/'inventories/quality_checks.json').read_text(encoding='utf-8'))
if qa['status']!='PASS':
    raise SystemExit('Refusing packaging: delivery integrity checks are not passing.')

files=[]
for path in sorted(ROOT.rglob('*')):
    if not path.is_file() or any(part in EXCLUDED for part in path.relative_to(ROOT).parts):
        continue
    if path==manifest_path or path.suffix=='.pyc':
        continue
    if path.name!='.gitignore' and path.suffix not in ALLOWED:
        raise SystemExit(f'Unexpected file type: {path.relative_to(ROOT)}')
    raw=path.read_bytes();content=raw.decode('utf-8')
    private_path=re.search(r'(?i)C:[/\\]Users[/\\][^\s/\\]+',content)
    secret=re.search(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\bgh[pousr]_[A-Za-z0-9]{30,}\b|\bhf_[A-Za-z0-9]{30,}\b',content)
    if private_path or secret:
        raise SystemExit(f'Potential private material: {path.relative_to(ROOT)}')
    if path.suffix=='.json':
        stack=[json.loads(content)]
        while stack:
            item=stack.pop()
            if isinstance(item,dict):
                for key,value in item.items():
                    if key in {'body','text','content','raw_text','source_code','readme_text','license_text'} and isinstance(value,str) and len(value)>400:
                        raise SystemExit(f'Possible fetched body in {path.relative_to(ROOT)}: {key}')
                    stack.append(value)
            elif isinstance(item,list):
                stack.extend(item)
    files.append(path)

manifest={
    'format_version':1,
    'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'scope':'Archivos incluidos en el ZIP; excluye este manifiesto de su propia lista de hashes.',
    'reference_date':'2026-11-03','source_observation_date':'2026-11-04',
    'excluded_directories':sorted(EXCLUDED),
    'included_types':['Notas propias Markdown','Inventarios CSV/JSON','Auxiliares Python propios','.gitignore'],
    'no_remote_publication':True,
    'file_count_excluding_manifest':len(files),
    'files':[dict(path=p.relative_to(ROOT).as_posix(),bytes=p.stat().st_size,
                  sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in files]
}
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
files.append(manifest_path)
with zipfile.ZipFile(ARCHIVE,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as archive:
    for path in files:
        archive.write(path,ROOT.name+'/'+path.relative_to(ROOT).as_posix())
with zipfile.ZipFile(ARCHIVE) as archive:
    bad=archive.testzip()
    if bad:
        raise SystemExit(f'Archive CRC failure: {bad}')
    for row in manifest['files']:
        data=archive.read(ROOT.name+'/'+row['path'])
        if hashlib.sha256(data).hexdigest()!=row['sha256']:
            raise SystemExit('Archive hash mismatch: '+row['path'])
    if len(archive.namelist())!=len(files):
        raise SystemExit('Archive file count mismatch.')
summary={'archive':ARCHIVE.name,'bytes':ARCHIVE.stat().st_size,
         'sha256':hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),
         'files_in_zip':len(files),'crc_and_manifest_hashes':'PASS'}
print(json.dumps(summary,ensure_ascii=False,indent=2))
