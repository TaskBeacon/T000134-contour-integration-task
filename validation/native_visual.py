"""GUI lease required. Ordinary human startup with synthetic form, actual PsychoPy window."""
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import json,os,sys
ROOT=Path(__file__).resolve().parents[1];os.chdir(ROOT);sys.path.insert(0,str(ROOT))
import main
from psyflow import StimBank,load_config
from psychopy import core
class Finished(Exception):pass
def capture(unit,**kwargs):
    # Draw actual runtime stimuli outside task implementation solely for screenshot inspection.
    for stim in unit.stimuli:stim.draw()
    unit.win.flip();core.wait(.15);unit.win.getMovieFrame(buffer='front');unit.win.saveMovieFrames(str(ROOT/'validation/native_instruction.png'))
    cfg=load_config(str(ROOT/'config/config.yaml'))
    bank=StimBank(unit.win,{k:cfg['stim_config'][k] for k in ['b15_00_signal','b15_00_null','b75_00_signal','report_prompt']}).preload_all()
    for name in ['b15_00_signal','b15_00_null','b75_00_signal','report_prompt']:
        bank.get(name).draw();unit.win.flip();core.wait(.15)
        unit.win.getMovieFrame(buffer='front');unit.win.saveMovieFrames(str(ROOT/f'validation/native_{name}.png'))
    (ROOT/'validation/native_human_startup.json').write_text(json.dumps(dict(status='PASS',mode='human',window_size=list(map(int,unit.win.size)),scope='Real initialization/StimBank/window; synthetic SubInfo return and intercepted first wait; no human identity or human performance data')))
    raise Finished()
with patch.object(main,'SubInfo') as form,patch.object(main.StimUnit,'wait_and_continue',capture):
 form.return_value.collect.return_value={'subject_id':134}
 try:main.run(SimpleNamespace(config_path=ROOT/'config/config.yaml',mode='human'))
 except Finished:print('PASS: actual human startup window and5screens captured with synthetic identity')
