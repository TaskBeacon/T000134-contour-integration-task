"""Independent synthetic checks of materials, schedules, true trial orchestration and startup."""
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import hashlib,importlib,json,math,sys,os
import numpy as np
import yaml
from PIL import Image
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
os.chdir(ROOT)
from src.utils import make_schedule,decode,score,summarize

def angular(a,b):return abs((a-b+90)%180-90)
cfg=yaml.safe_load((ROOT/'config/config.yaml').read_text(encoding='utf8'))
manifest=json.loads((ROOT/'assets/manifest.json').read_text())
stats=[]
for pair in manifest['pairs']:
    pos=np.array(pair['positions']);s=np.array(pair['signal_orientations_deg']);n=np.array(pair['null_orientations_deg'])
    assert pos.shape==(256,2) and len(set(map(tuple,(pos//32).astype(int))))==256
    dist=np.linalg.norm(pos[:,None,:]-pos[None,:,:],axis=2);np.fill_diagonal(dist,np.inf)
    assert dist.min()>=18-1e-8
    assert np.array_equal(np.sort(s),np.sort(n)) and np.all(s!=n)
    vv=np.array(pair['backbone_vertices']);vec=np.diff(vv,axis=0)
    tangent=np.rad2deg(np.arctan2(vec[:,1],vec[:,0]))%180
    assert np.max(np.abs(pos[:12]-(vv[1:]+vv[:-1])/2))<1e-9
    assert all(angular(a,b)<1e-8 for a,b in zip(s[:12],tangent))
    nullaligned=[angular(a,b)<15 for a,b in zip(n[:12],tangent)]
    assert sum(nullaligned)<=3 and not any(all(nullaligned[i:i+3]) for i in range(10))
    features=[]
    for kind in ['signal','null']:
        data=(ROOT/pair[kind+'_file']).read_bytes();assert hashlib.sha256(data).hexdigest()==pair[kind+'_sha256']
        arr=np.array(Image.open(ROOT/pair[kind+'_file']));assert arr.shape==(512,512)
        features.append([float(arr.mean()),float(arr.std()),int(np.sum((arr==0)|(arr==255)))])
    stats.append(dict(item_id=pair['item_id'],min_spacing=float(dist.min()),null_planted_aligned=int(sum(nullaligned)),signal_features=features[0],null_features=features[1]))
assert len(stats)==100
# Independent scheduling balance across99participant seeds, unique items and alltarget cells.
for sid in range(101,200):
    settings=SimpleNamespace(**cfg['task'],subject_id=sid);plan=make_schedule(settings)
    assert len(plan)==len({decode(x)['item_id'] for x in plan})==100
    for beta in [15,30,45,60,75]:
        for interval in [1,2]:assert sum(decode(x)['bend_deg']==beta and decode(x)['target_interval']==interval for x in plan)==10
# Execute actual run_trial body with lightweight public API seam; no claim of actual GUI timing here.
module=importlib.import_module('src.run_trial')
class Unit:
    response=None
    calls=[]
    def __init__(self,phase,*a,**k):self.phase=phase;self.state={};self.calls.append([phase,[],None])
    def add_stim(self,*a):self.calls[-1][1].extend(a);return self
    def show(self,**kw):self.calls[-1][2]=kw['duration'];return self
    def capture_response(self,**kw):self.state={'response':self.response,'rt':.25 if self.response else None};return self.show(**kw)
    def get_state(self,key):return self.state.get(key)
    def to_dict(self,row):row.update({self.phase+'_'+k:v for k,v in self.state.items()});return self
settings=SimpleNamespace(**cfg['task'],**cfg['timing'],triggers=cfg['triggers']['map'],subject_id=134)
rows=[]
for target in [1,2]:
 for response in ['f','j',None]:
    Unit.response=response;Unit.calls=[]
    with patch.object(module,'StimUnit',Unit),patch.object(module,'set_trial_context'),patch.object(module,'next_trial_id',return_value=1):
        row=module.run_trial(None,None,settings,f'b15_00|{target}',SimpleNamespace(get=lambda x:x),None)
    assert [c[0] for c in Unit.calls]==['fixation','interval_one','gap','interval_two','report','intertrial']
    assert [c[2] for c in Unit.calls]==[.5,1,1,1,4,.3]
    assert Unit.calls[1][1]==[f'b15_00_{"signal" if target==1 else "null"}']
    assert Unit.calls[3][1]==[f'b15_00_{"signal" if target==2 else "null"}']
    assert row['correct']==(response==('f' if target==1 else 'j'))
    assert row['missing_response']==(response is None);rows.append(row)
summary=summarize(rows)['conditions'][0];assert summary['total']==6 and summary['valid']==4 and summary['missing']==2 and summary['accuracy_all']==2/6
# Audit normal human branch through real cfg/settings/seed setup; synthetic form and mocked GUI init only.
main=importlib.import_module('main')
class StopAtGUI(Exception):pass
with patch.object(main,'SubInfo') as form,patch.object(main,'initialize_triggers'),patch.object(main,'initialize_exp',side_effect=StopAtGUI):
 form.return_value.collect.return_value={'subject_id':134}
 try:main.run(SimpleNamespace(config_path=ROOT/'config/config.yaml',mode='human'))
 except StopAtGUI:pass
 else:raise AssertionError('Human path never reached GUI initializer')
result=dict(status='PASS',pairs=100,schedule_subjects=99,actual_run_trial_scenarios=6,human_startup='PASS to mocked GUI initializer with synthetic ID; does not validate actual dialog',material_statistics=stats)
(ROOT/'validation/native_semantics.json').write_text(json.dumps(result,indent=2),encoding='utf8')
# Exact parity oracle consumed by webtests.
oracle=dict(plans={str(sid):make_schedule(SimpleNamespace(**cfg['task'],subject_id=sid)) for sid in [101,134,999]},scores=[dict(target=t,response=r,result=score(r,.25,t)) for t in [1,2] for r in ['f','j',None]])
(ROOT/'validation/parity_oracle.json').write_text(json.dumps(oracle,indent=2),encoding='utf8')
print('PASS:100pairs;99balanced schedules;6actualrun_trialcases;normalhumanstartup seam')
