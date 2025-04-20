import glm

# DIRECTIONAL LIGHT (MATAHARI SEBAGAI SOURCE LIGHT)
class Light:
    def __init__(self, position=(5, 10, 5), color=(1, 1, 1)):
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        
        self.direction = glm.vec3(0, 0, 0)
        self.multiplier = 1.2
        
        # INTENSITAS CAHAYA
        self.Ia = 0.3 * self.color * self.multiplier
        self.Id = 0.5 * self.color * self.multiplier
        self.Is = 1.0 * self.color * self.multiplier

        self.m_view_light = self.get_view_matrix()

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.direction, glm.vec3(0, 1, 0))