import glm

# POINT LIGHT
class PointLight:
    def __init__(self, position=(0, 5, 0), color=(1, 1, 1), intensity=1.0, shadow_blur=1.0):
        self.position = glm.vec3(position[0] * shadow_blur, position[1] * shadow_blur, position[2] * shadow_blur)
        self.color = glm.vec3(color)
        
        self.direction = glm.vec3(0, 0, 0)
        self.shadow_blur = shadow_blur
        self.multiplier = intensity
        
        # INTENSITAS CAHAYA
        self.Ia = 0.3 * self.color * self.multiplier
        self.Id = 0.5 * self.color * self.multiplier
        self.Is = 1.0 * self.color * self.multiplier

        self.m_view_light = self.get_view_matrix()

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.direction, glm.vec3(0, 1, 0))
    