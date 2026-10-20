"""Copy imagegen outputs; inspect alpha and describe sprite regions without editing pixels."""
from pathlib import Path
import json
import shutil
import sys
sys.path.append(str(Path.home()/'.cache/codex-runtimes/codex-primary-runtime/dependencies/python/Lib/site-packages'))
import numpy as np
from PIL import Image
from scipy.ndimage import label, find_objects

ROOT=Path(__file__).resolve().parents[1]
GEN=Path.home()/'.codex/generated_images/01a1570d-a4b3-7dc2-b83c-1cfd9e910ad7'
files={
 'fachada-proxima.png':'exec-652d087c-4f02-43df-b187-939f7e3e1f1c.png',
 'lia-rig.png':'exec-2daa3e71-0f8b-41df-ad84-a8ad2c20d91b.png',
 'caio-rig.png':'exec-51592af6-2326-4278-8316-94ac605bdc3c.png',
 'motorista-rig.png':'exec-776de319-75ed-4db7-92fc-44c1b906c253.png',
 'rua-vazia-vertical.png':'exec-e935d05b-79b3-45fa-be99-f56ed96c3cc6.png',
 'rua-predio-vertical.png':'exec-259b7dae-0c0a-46ec-b6a2-a897c49d8178.png',
 'jantar-vertical.png':'exec-a0028e1b-000e-406d-803d-04ba9d19bb85.png',
 'cadeira.png':'exec-84b469ca-90a8-4500-8995-1f0ea2c67732.png',
 'onibus.png':'exec-6f83e8ce-9ea6-4e54-b8e2-326b4565639d.png',
 'sobreviventes.png':'exec-062bc4e1-9bd9-4e64-b08d-393e6050cbf7.png',
}
manifest={}
for dest,source in files.items():
    path=ROOT/'public/assets'/dest
    if not path.exists(): shutil.copy2(GEN/source,path)
    im=Image.open(path).convert('RGBA')
    a=np.asarray(im)[:,:,3]
    manifest[dest]={'file':dest,'generated_file':source,'width':im.width,'height':im.height,
                    'transparent':bool(np.min(a)==0),'mode':'built-in image_gen'}

rigs={}
for char in ['lia','caio','motorista']:
    path=ROOT/'public/assets'/f'{char}-rig.png'
    im=Image.open(path).convert('RGBA')
    a=np.asarray(im)[:,:,3]
    lab,num=label(a>160)
    sizes=np.bincount(lab.ravel()); sizes[0]=0
    biggest=sorted(range(1,num+1),key=lambda k:sizes[k],reverse=True)[:12]
    boxes=[]
    all_slices=find_objects(lab)
    for k in biggest:
        sl=all_slices[k-1]; y,x=sl
        boxes.append([max(0,x.start-3),max(0,y.start-3),min(im.width,x.stop+3)-max(0,x.start-3),min(im.height,y.stop+3)-max(0,y.start-3)])
    boxes.sort(key=lambda b:b[1]+b[3]/2)
    ordered=[]
    for row in range(4): ordered+=sorted(boxes[row*3:row*3+3],key=lambda b:b[0])
    keys=['head0','head1','head2','body','pack','knock','upperL','armL','upperR','armR','legL','legR'] if char=='lia' else ['head0','head1','head2','body','armL','armR','upperL','foreL','upperR','foreR','legL','legR']
    rigs[char]={'file':f'{char}-rig.png','width':im.width,'height':im.height,'parts':dict(zip(keys,ordered))}
    print(char,dict(zip(keys,ordered)))
for filename,key in [('cadeira.png','cadeira'),('onibus.png','onibus')]:
    im=Image.open(ROOT/'public/assets'/filename).convert('RGBA')
    mask=im.getchannel('A').point(lambda p:255 if p>180 else 0)
    b=mask.getbbox()
    rigs[key]={'file':filename,'width':im.width,'height':im.height,'parts':{'full':[b[0],b[1],b[2]-b[0],b[3]-b[1]]}}
im=Image.open(ROOT/'public/assets/sobreviventes.png').convert('RGBA')
rigs['extras']={'file':'sobreviventes.png','width':im.width,'height':im.height,'parts':{}}
for i in range(2):
    left=round(i*im.width/2); right=round((i+1)*im.width/2)
    b=im.getchannel('A').crop((left,0,right,im.height)).point(lambda p:255 if p>180 else 0).getbbox()
    rigs['extras']['parts'][f'person{i}']=[left+b[0],b[1],b[2]-b[0],b[3]-b[1]]
(ROOT/'src/rigs.json').write_text(json.dumps(rigs,indent=2),encoding='utf-8')
(ROOT/'docs/artes-manifesto.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print('Art assets copied and alpha verified; sprite metadata saved. Source pixels unchanged.')
