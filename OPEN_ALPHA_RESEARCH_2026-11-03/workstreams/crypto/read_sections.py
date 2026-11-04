import json,pathlib,re,sys
p=pathlib.Path(__file__).parent/'inspection_code.json'
a=json.loads(p.read_text(encoding='utf8'))
repo,pattern=sys.argv[1:3]
limit=int(sys.argv[3]) if len(sys.argv)>3 else 12000
remaining=limit
for x in a:
 if x['repo']!=repo or x['status']!=200:continue
 if len(sys.argv)>4 and not re.search(sys.argv[4],x['path']):continue
 text=x['text'];lines=text.splitlines()
 hits=[i for i,l in enumerate(lines) if re.search(pattern,l,re.I)]
 if not hits:continue
 print('\nFILE '+x['path']+' '+x.get('commit',''))
 ranges=[]
 for i in hits:
  if ranges and i<ranges[-1][1]:continue
  ranges.append((max(0,i-2),min(len(lines),i+14)))
 for s,e in ranges:
  chunk='\n'.join(str(i+1)+': '+lines[i] for i in range(s,e))
  if len(chunk)>remaining:chunk=chunk[:remaining]
  print(chunk.encode('ascii','backslashreplace').decode())
  remaining-=len(chunk)
  if remaining<=0:break
 if remaining<=0:break
