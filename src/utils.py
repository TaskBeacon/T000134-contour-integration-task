"""Task-specific item/interval preplan and denominator-preserving outcomes."""
import random

def make_schedule(settings):
    sid=int(settings.subject_id)
    if not 101<=sid<=999: raise ValueError('subject_id must be101..999')
    n=int(settings.exemplars_per_bend)
    if n not in (2,20):raise ValueError('Expected diagnostic2 or full20 exemplars per bend')
    rng=random.Random(int(settings.overall_seed)+sid);labels=[]
    for condition in settings.conditions:
        beta=int(condition.split('_')[1]);intervals=[1,2]*(n//2);rng.shuffle(intervals)
        labels.extend(f'b{beta}_{i:02d}|{target}' for i,target in enumerate(intervals))
    rng.shuffle(labels)
    if len(labels)!=settings.total_trials:raise ValueError('Plan count does not match total_trials')
    return labels

def decode(label):
    item,interval=label.split('|');beta=int(item.split('_')[0][1:])
    return dict(item_id=item,bend_deg=beta,bend_condition=f'bend_{beta}',target_interval=int(interval))

def score(response,rt,target,first='f',second='j'):
    chosen=1 if response==first else 2 if response==second else None
    return dict(chosen_interval=chosen,correct=chosen==target,missing_response=chosen is None,
                response_rt_s=rt if chosen is not None else None)

def summarize(rows):
    result=[]
    for beta in [15,30,45,60,75]:
        rr=[r for r in rows if r['bend_deg']==beta];valid=[r for r in rr if not r['missing_response']]
        correct=sum(bool(r['correct']) for r in rr)
        result.append(dict(bend_deg=beta,total=len(rr),valid=len(valid),missing=len(rr)-len(valid),correct=correct,
                      accuracy_all=correct/len(rr) if rr else None,accuracy_valid=correct/len(valid) if valid else None))
    return dict(conditions=result,physical_calibration=False,human_pilot=False,threshold_estimated=False)
