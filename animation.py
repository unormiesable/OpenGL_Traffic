from pyglm import glm
import numpy as np

class Animation:
    def __init__(self, app, target_model):
        self.target_model = target_model
        self.app = app
        self.keyframes = []

    def add_keyframe(self, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1), time=0, interpolation='linear'):
        self.keyframes.append((pos, rot, scale, time, interpolation))

    def animate(self):
        if len(self.keyframes) < 2:
            if len(self.keyframes) == 1:
                key = self.keyframes[0]
                self._apply_keyframe(key)
            self.target_model.m_model = self.target_model.get_model_matrix()
            return

        self.keyframes.sort(key=lambda k: k[3])
        current_time = self.app.time

        prev_key = None
        next_key = None

        for i, key in enumerate(self.keyframes):
            if key[3] <= current_time:
                prev_key = key
            if key[3] >= current_time:
                next_key = key
                break

        if prev_key is None and next_key is None:
            self.target_model.m_model = self.target_model.get_model_matrix()
            return
        elif prev_key is None:
            self._apply_keyframe(self.keyframes[0])
        elif next_key is None:
            self._apply_keyframe(self.keyframes[-1])
        elif prev_key == next_key:
            self._apply_keyframe(prev_key)
        else:
            time_start = prev_key[3]
            time_end = next_key[3]
            duration = time_end - time_start

            if duration == 0:
                self._apply_keyframe(prev_key)
            else:
                t = (current_time - time_start) / duration
                interpolation_type = prev_key[4]

                if interpolation_type == 'linear':
                    t_mod = t
                elif interpolation_type == 'smoothstep':
                    t_mod = glm.smoothstep(0.0, 1.0, t)
                elif interpolation_type == 'ease_in_out':
                    t_mod = t * t * (3 - 2 * t)
                else:
                    t_mod = t 

                pos_start = glm.vec3(prev_key[0])
                pos_end = glm.vec3(next_key[0])
                self.target_model.pos = glm.mix(pos_start, pos_end, t_mod)

                rot_start = glm.vec3([glm.radians(a) for a in prev_key[1]])
                rot_end = glm.vec3([glm.radians(a) for a in next_key[1]])
                self.target_model.rot = glm.mix(rot_start, rot_end, t_mod)

                scale_start = glm.vec3(prev_key[2])
                scale_end = glm.vec3(next_key[2])
                scale_interp = glm.mix(scale_start, scale_end, t_mod)
                self.target_model.scale = glm.vec3(
                    scale_interp.x * self.target_model.uni_scale,
                    scale_interp.y * self.target_model.uni_scale,
                    scale_interp.z * self.target_model.uni_scale
                )
        self.target_model.animate()

    def _apply_keyframe(self, key):
        self.target_model.pos = glm.vec3(key[0])
        self.target_model.rot = glm.vec3([glm.radians(a) for a in key[1]])
        self.target_model.scale = glm.vec3(
            key[2][0] * self.target_model.uni_scale,
            key[2][1] * self.target_model.uni_scale,
            key[2][2] * self.target_model.uni_scale
        )
