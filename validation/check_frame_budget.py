"""Verify measured timeout behavior against the recorded framework frame budget."""
from pathlib import Path
import json
import pandas as pd
ROOT=Path(__file__).resolve().parents[1];rows=[];settings=[]
for mode in ['qa','scripted_sim','sampler_sim']:
 s=json.loads((ROOT/f'outputs/{mode}/settings.json').read_text());period=s['frame_time_seconds'];fps=s['win_fps']
 n=round(4/period);expected=(n-1)/fps
 settings.append(dict(mode=mode,frame_time_seconds=period,win_fps=fps,nominal_report_s=4,n_frames=n,expected_last_flip_s=expected))
 df=pd.read_csv(ROOT/f'outputs/{mode}'/('qa_trace.csv' if mode=='qa' else 'sim_trace.csv'))
 for _,r in df[df.missing_response].iterrows():
  close=float(r.report_close_time-r.report_onset_time);next_flip=float(r.intertrial_flip_time-r.report_flip_time)
  error=close-expected
  assert abs(error)<1/fps, (mode,error,1/fps)
  rows.append(dict(mode=mode,trial_id=int(r.trial_id),nominal_s=4,measured_close_s=close,next_intertrial_flip_s=next_flip,expected_close_s=expected,error_s=error,tolerance_s=1/fps))
(ROOT/'validation/native_frame_budget.json').write_text(json.dumps(dict(status='PASS',settings=settings,omissions=rows,scope='Frame-budget consistency, not exact nominal deadline. Default runtime rounds nominal/estimatedperiod then closes on lastflip (nframes-1intervals). Tolerance is one recorded displayframe, not an arbitrary widened deadline threshold.'),indent=2))
print(json.dumps(rows,indent=2))
