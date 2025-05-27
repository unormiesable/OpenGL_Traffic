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

        key_before = None
        key_after = None

        for i, key in enumerate(self.keyframes):
            if key[3] <= current_time:
                key_before = key
            if key[3] >= current_time:
                key_after = key
                break

        if key_before is None and key_after is None:
            self.target_model.m_model = self.target_model.get_model_matrix()
            return
        elif key_before is None:
            self._apply_keyframe(self.keyframes[0])
        elif key_after is None:
            self._apply_keyframe(self.keyframes[-1])
        elif key_before == key_after:
            self._apply_keyframe(key_before)
        else:
            time_start = key_before[3]
            time_end = key_after[3]
            duration = time_end - time_start

            if duration == 0:
                self._apply_keyframe(key_before)
            else:
                t = (current_time - time_start) / duration
                interpolation_type = key_before[4]

                if interpolation_type == 'linear':
                    t_mod = t
                elif interpolation_type == 'smoothstep':
                    t_mod = glm.smoothstep(0.0, 1.0, t)
                elif interpolation_type == 'ease_in_out':
                    t_mod = t * t * (3 - 2 * t)
                else:
                    t_mod = t 

                pos_start = glm.vec3(key_before[0])
                pos_end = glm.vec3(key_after[0])
                self.target_model.pos = glm.mix(pos_start, pos_end, t_mod)

                rot_start = glm.vec3([glm.radians(a) for a in key_before[1]])
                rot_end = glm.vec3([glm.radians(a) for a in key_after[1]])
                self.target_model.rot = glm.mix(rot_start, rot_end, t_mod)

                scale_start = glm.vec3(key_before[2])
                scale_end = glm.vec3(key_after[2])
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
