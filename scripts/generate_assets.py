"""Deterministic authored Gabor bank; no borrowed image material."""
from pathlib import Path
import hashlib,json,math,random
import numpy as np
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]

def axial(a,b): return abs((a-b+90)%180-90)

def intersect(a,b,c,d):
    def cross(p,q,r): return (q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
    return cross(a,b,c)*cross(a,b,d)<0 and cross(c,d,a)*cross(c,d,b)<0

def make_pair(beta,index,retry=0):
    rng=random.Random(1340000+beta*100+index+retry*10000000)
    for attempt in range(200000):
        phi=rng.uniform(0,2*math.pi)
        p=np.array([256+64*math.cos(phi),256+64*math.sin(phi)])
        angle=phi+math.pi+rng.choice([-1,1])*math.radians(beta)
        path=[];tangents=[];vertices=[p.tolist()]
        for _ in range(12):
            length=rng.uniform(24,40)
            q=p+length*np.array([math.cos(angle),math.sin(angle)])
            mid=(p+q)/2
            path.append(mid.tolist());tangents.append(math.degrees(angle)%180);vertices.append(q.tolist())
            p=q;angle+=math.radians(rng.choice([-1,1])*beta+rng.uniform(-10,10))
        cells=[(int(x//32),int(y//32)) for x,y in path]
        if len(set(cells))<12 or any(not(14<=x<=497 and 14<=y<=497) for x,y in path): continue
        if any(math.dist(path[i],path[j])<18 for i in range(12) for j in range(i)): continue
        if any(intersect(vertices[i],vertices[i+1],vertices[j],vertices[j+1]) for i in range(12) for j in range(i-1)): continue
        break
    else: raise RuntimeError('Cannot construct bounded nonintersecting path')
    positions=list(path);orientations=list(tangents)
    for cy in range(16):
        for cx in range(16):
            if (cx,cy) in cells: continue
            for _ in range(100000):
                candidate=[rng.uniform(max(14,cx*32),min(497,(cx+1)*32)),rng.uniform(max(14,cy*32),min(497,(cy+1)*32))]
                if all(math.dist(candidate,p)>=18 for p in positions):break
            else:
                if retry>=20: raise RuntimeError('Background packing failed after20 deterministic retries')
                return make_pair(beta,index,retry+1)
            positions.append(candidate);orientations.append(rng.uniform(0,180))
    for _ in range(10000):
        null=orientations.copy();rng.shuffle(null)
        aligned=[axial(null[i],tangents[i])<15 for i in range(12)]
        if sum(aligned)<=3 and not any(all(aligned[i:i+3]) for i in range(10)) and all(a!=b for a,b in zip(null,orientations)):break
    else:raise RuntimeError('Null permutation failed')
    return dict(item_id=f'b{beta}_{index:02d}',bend_deg=beta,index=index,seed=1340000+beta*100+index+retry*10000000,
                positions=positions,path_indices=list(range(12)),backbone_vertices=vertices,
                signal_orientations_deg=orientations,null_orientations_deg=null)

def render(pair,kind):
    canvas=np.zeros((512,512),dtype=np.float64)
    for (x,y),t in zip(pair['positions'],pair[kind+'_orientations_deg']):
        x0,x1=int(math.floor(x))-13,int(math.floor(x))+15
        y0,y1=int(math.floor(y))-13,int(math.floor(y))+15
        yy,xx=np.mgrid[y0:y1,x0:x1];dx=xx-x;dy=yy-y
        normal=math.radians(t+90)
        carrier=dx*math.cos(normal)+dy*math.sin(normal)
        patch=np.exp(-(dx*dx+dy*dy)/32)*np.cos(2*math.pi*carrier/8)
        canvas[y0:y1,x0:x1]+=patch
    # Same amplitude and rendering for every element/interval; clipping recorded in audit.
    arr=np.round(127.5+127.5*.95*canvas).clip(0,255).astype('uint8')
    return Image.fromarray(arr,'L')

def main():
    folder=ROOT/'assets/arrays';folder.mkdir(parents=True,exist_ok=True);pairs=[]
    for beta in [15,30,45,60,75]:
        for index in range(20):
            pair=make_pair(beta,index)
            for kind in ['signal','null']:
                path=folder/f'{pair["item_id"]}_{kind}.png';render(pair,kind).save(path)
                pair[kind+'_file']=path.relative_to(ROOT).as_posix()
                pair[kind+'_sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
            pairs.append(pair)
    (ROOT/'assets/manifest.json').write_text(json.dumps({'version':'gabor-paired-v1','pairs':pairs},separators=(',',':')),encoding='utf8')
    print(f'Generated {len(pairs)} unique paired arrays, 200 PNGs')

if __name__=='__main__':main()
