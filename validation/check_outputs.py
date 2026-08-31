"""Validate real native synthetic artifacts and archive safe copies for review."""
from pathlib import Path
import json,shutil
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
checks=[]
for mode in ['qa','scripted_sim','sampler_sim']:
 p=ROOT/'outputs'/mode/('qa_trace.csv' if mode=='qa' else 'sim_trace.csv');df=pd.read_csv(p)
 assert len(df)==10 and df.trial_id.nunique()==10 and df.item_id.nunique()==10
 assert set(df.bend_deg)=={15,30,45,60,75}
 for bend in [15,30,45,60,75]:assert set(df[df.bend_deg==bend].target_interval)=={1,2}
 for _,r in df.iterrows():
  chosen=1 if r.report_response=='f' else 2 if r.report_response=='j' else None
  assert bool(r.correct)==(chosen==r.target_interval)
  assert bool(r.missing_response)==(chosen is None)
  for name,duration in [('fixation',.5),('interval_one',1),('gap',1),('interval_two',1),('report',4),('intertrial',.3)]:assert abs(r[name+'_duration']-duration)<1e-8
  assert r.interval_one_asset.endswith('_signal.png')==(r.target_interval==1)
  assert r.interval_two_asset.endswith('_signal.png')==(r.target_interval==2)
 shutil.copy2(p,ROOT/f'validation/python_{mode}_synthetic.csv')
 checks.append(dict(mode=mode,status='PASS',rows=10,correct=int(df.correct.sum()),missing=int(df.missing_response.sum()),interval_one_flip_span_s=[float((df.gap_flip_time-df.interval_one_flip_time).min()),float((df.gap_flip_time-df.interval_one_flip_time).max())],interval_two_flip_span_s=[float((df.report_flip_time-df.interval_two_flip_time).min()),float((df.report_flip_time-df.interval_two_flip_time).max())]))
for name in ['qa_report.json','gate_report.json']:shutil.copy2(ROOT/'outputs/qa'/name,ROOT/'validation'/name)
(ROOT/'validation/native_output_check.json').write_text(json.dumps(dict(status='PASS',checks=checks,limitation='Synthetic responder output and software flip spans, not human data or photodiode timing'),indent=2))
print(json.dumps(checks,indent=2))
