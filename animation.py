from pyglm import glm
import numpy as np

class Animation:
    def __init__(self, target_model, app):
        self.target_model = target_model
        self.app = app
        self.keyframes = []

    def add_keyframe(self, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1), time=0):
        self.keyframes.append((pos, rot, scale, time))

    def animate(self):
        if len(self.keyframes) < 2:
            if len(self.keyframes) == 1:
                key = self.keyframes[0]
                self.target_model.pos = key[0]
                self.target_model.rot = glm.vec3([glm.radians(a) for a in key[1]])
                self.target_model.scale = glm.vec3(key[2][0] * self.target_model.uni_scale, key[2][1] * self.target_model.uni_scale, key[2][2] * self.target_model.uni_scale)
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
            key = self.keyframes[0]
            self.target_model.pos = key[0]
            self.target_model.rot = glm.vec3([glm.radians(a) for a in key[1]])
            self.target_model.scale = glm.vec3(key[2][0] * self.target_model.uni_scale, key[2][1] * self.target_model.uni_scale, key[2][2] * self.target_model.uni_scale)
        elif key_after is None:
            key = self.keyframes[-1]
            self.target_model.pos = key[0]
            self.target_model.rot = glm.vec3([glm.radians(a) for a in key[1]])
            self.target_model.scale = glm.vec3(key[2][0] * self.target_model.uni_scale, key[2][1] * self.target_model.uni_scale, key[2][2] * self.target_model.uni_scale)
        elif key_before == key_after:
            key = key_before
            self.target_model.pos = key[0]
            self.target_model.rot = glm.vec3([glm.radians(a) for a in key[1]])
            self.target_model.scale = glm.vec3(key[2][0] * self.target_model.uni_scale, key[2][1] * self.target_model.uni_scale, key[2][2] * self.target_model.uni_scale)
        else:
            time_start = key_before[3]
            time_end = key_after[3]
            duration = time_end - time_start

            if duration == 0:
                self.target_model.pos = key_before[0]
                self.target_model.rot = glm.vec3([glm.radians(a) for a in key_before[1]])
                self.target_model.scale = glm.vec3(key_before[2][0] * self.target_model.uni_scale, key_before[2][1] * self.target_model.uni_scale, key_before[2][2] * self.target_model.uni_scale)
            else:
                t = (current_time - time_start) / duration
                self.target_model.pos = glm.mix(glm.vec3(key_before[0]), glm.vec3(key_after[0]), t)
                rot_before_rad = glm.vec3([glm.radians(a) for a in key_before[1]])
                rot_after_rad = glm.vec3([glm.radians(a) for a in key_after[1]])
                self.target_model.rot = glm.mix(rot_before_rad, rot_after_rad, t)

                scale_before_raw = glm.vec3(key_before[2])
                scale_after_raw = glm.vec3(key_after[2])
                interpolated_scale_raw = glm.mix(scale_before_raw, scale_after_raw, t)
                self.target_model.scale = glm.vec3(
                    interpolated_scale_raw.x * self.target_model.uni_scale,
                    interpolated_scale_raw.y * self.target_model.uni_scale,
                    interpolated_scale_raw.z * self.target_model.uni_scale
                )
        
        self.target_model.animate()