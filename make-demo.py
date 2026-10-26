from pathlib import Path
import re, shutil
root=Path(__file__).resolve().parent
html=(root/'index.html').read_text(encoding='utf-8')
html,n=re.subn(r'(<script data-seed>)const SEED=.*?;</script>',r'\1const SEED=[];</script>',html,count=1,flags=re.S)
if n!=1:
    raise RuntimeError('Cannot locate seed data; no demo was written.')
html=html.replace("renal-insight-v1", "renal-insight-public-demo-v1")
html=html.replace('แผนกไตเทียม · โรงพยาบาลบ้านแพ้ว','ระบบสาธิต · ไม่มีข้อมูลผู้ป่วยเริ่มต้น')
out=root/'public-demo';out.mkdir(exist_ok=True)
(out/'index.html').write_text(html,encoding='utf-8')
for name in ('sw.js','.nojekyll'):
    shutil.copyfile(root/name,out/name)
print('Created public-demo with no embedded patient records. Do not import real patient data on a public/shared device.')
