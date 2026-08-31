from dataclasses import dataclass
from psyflow.sim.contracts import Action

@dataclass
class TaskSamplerResponder:
    rt_s:float=.15
    def start_session(self,session,rng):self.rng=rng
    def act(self,obs):
        keys=list(obs.valid_keys or [])
        if 'space' in keys:return Action(key='space',rt_s=self.rt_s)
        if keys:
            if self.rng.random()<.2:return Action(key=None,rt_s=None)
            return Action(key=self.rng.choice(keys),rt_s=self.rt_s)
        return Action(key=None,rt_s=None)
    def on_feedback(self,feedback):pass
    def end_session(self):pass
