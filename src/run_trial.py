from psyflow import StimUnit,next_trial_id,set_trial_context
from .utils import decode,score

def run_trial(win,kb,settings,condition,stim_bank,trigger_runtime,block_id=None,block_idx=None):
    spec=decode(condition);trial_id=next_trial_id()
    row=dict(trial_id=trial_id,block_id=block_id,block_idx=block_idx,condition=condition,**spec,
             material_version=settings.material_version,diagnostic=settings.diagnostic,
             physical_calibration=False)
    def unit(phase,*stims,keys=(),duration=None):
        u=StimUnit(phase,win,kb,runtime=trigger_runtime).add_stim(*stims)
        set_trial_context(u,trial_id=trial_id,phase=phase,deadline_s=duration,valid_keys=list(keys),
                          block_id=block_id,condition_id=spec['bend_condition'],stim_id=spec['item_id'],task_factors=spec)
        return u
    unit('fixation',stim_bank.get('fixation'),duration=settings.fixation_duration).show(
        duration=settings.fixation_duration,onset_trigger=settings.triggers['fixation_onset']).to_dict(row)
    for interval,phase in [(1,'interval_one'),(2,'interval_two')]:
        kind='signal' if interval==spec['target_interval'] else 'null'
        unit(phase,stim_bank.get(spec['item_id']+'_'+kind),duration=settings.array_duration).show(
            duration=settings.array_duration,onset_trigger=settings.triggers[phase+'_onset']).to_dict(row)
        row[phase+'_asset']=f"assets/arrays/{spec['item_id']}_{kind}.png"
        if interval==1:
            unit('gap',duration=settings.gap_duration).show(duration=settings.gap_duration,onset_trigger=settings.triggers['gap_onset']).to_dict(row)
    report=unit('report',stim_bank.get('report_prompt'),keys=settings.report_keys,duration=settings.report_duration)
    report.capture_response(keys=settings.report_keys,duration=settings.report_duration,terminate_on_response=True,
        onset_trigger=settings.triggers['report_onset'],response_trigger={settings.first_key:settings.triggers['first_response'],settings.second_key:settings.triggers['second_response']},timeout_trigger=settings.triggers['omission']).to_dict(row)
    row.update(score(report.get_state('response'),report.get_state('rt'),spec['target_interval'],settings.first_key,settings.second_key))
    unit('intertrial',duration=settings.intertrial_duration).show(duration=settings.intertrial_duration,onset_trigger=settings.triggers['intertrial_onset']).to_dict(row)
    return row
