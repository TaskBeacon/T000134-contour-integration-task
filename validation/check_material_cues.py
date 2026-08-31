"""Independent nuisance-feature and accidental low-curvature chain screening.
This proxy is not a human contour detector and does not certify all shortcuts absent.
"""
from pathlib import Path
import json
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
m=json.loads((ROOT/'assets/manifest.json').read_text())
rows=[]
for p in m['pairs']:
 pos=np.array(p['positions']);delta=pos[None,:,:]-pos[:,None,:]
 distance=np.linalg.norm(delta,axis=2);chord=np.rad2deg(np.arctan2(delta[:,:,1],delta[:,:,0]))%180
 out={'item_id':p['item_id']}
 for kind in ['signal','null']:
  angles=np.array(p[kind+'_orientations_deg'])
  errors=np.abs((angles[:,None]-chord+90)%180-90)
  edges=(distance>=18)&(distance<=50)&(errors<=25)&(errors.T<=25)
  unseen=set(range(256));sizes=[]
  while unseen:
   start=unseen.pop();stack=[start];count=0
   while stack:
    v=stack.pop();count+=1
    nxt=set(np.flatnonzero(edges[v]))&unseen;unseen-=nxt;stack.extend(nxt)
   sizes.append(count)
  out[kind+'_largest_local_alignment_component']=max(sizes)
 rows.append(out)
s=json.loads((ROOT/'native_semantics.json').read_text()) if (ROOT/'native_semantics.json').exists() else json.loads((ROOT/'validation/native_semantics.json').read_text())
st=s['material_statistics']
result=dict(status='PASS',proxy_definition='undirected18..50px neighbor graph; each bar within25degrees of joining chord; component size is conservative upper bound on connected chain length',max_null_component=max(x['null_largest_local_alignment_component'] for x in rows),maximum_paired_mean_gray_difference=max(abs(x['signal_features'][0]-x['null_features'][0]) for x in st),maximum_paired_pixel_sd_difference=max(abs(x['signal_features'][1]-x['null_features'][1]) for x in st),maximum_clipped_pixels=max(max(x['signal_features'][2],x['null_features'][2]) for x in st),limitations='Proxy misses strongly bent paths and does not establish perceptual discriminability; no human pilot. Identical coordinates remove all density/spacing-only classifiers exactly; orientation multisets remove global histogram-only classifiers exactly. Pixel statistics remain numerically near-matched, not bit-exact.',rows=rows)
# Deliberately not a gate asserting the human task is valid from this proxy alone.
(ROOT/'validation/material_cues.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
