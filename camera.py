import glm
import pygame as pg

# ATRIBUT KAMERA
FOV = 60
NEAR = 0.1
FAR = 100

Cam_Speed = 0.02
Rotate_Speed = 1.0
Mouse_Sens = 0.04

# CLASS KAMERA
class Camera:
    def __init__(self, app, position=(-6, 4.5, 6), look_LR=-45, look_UD=-25):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        
        # KAMERA MODE FLY (WASD)
        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        
        self.look_LR = look_LR
        self.look_UD = look_UD

        # KAMERA MODE ORBIT
        self.use_orbit = False
        self.orbit_target = glm.vec3(0, 0, 0)
        self.orbit_radius = 10.0

        # VIEW MATRIX
        self.m_view = self.get_view_matrix()
        
        # PROJECTION MATRIX
        self.m_proj = self.get_projection_matrix()

    # KONTROL KAMERA ========================================================

    def rotate(self):
        rel_x, rel_y = pg.mouse.get_rel()
        self.look_LR += rel_x * Mouse_Sens
        self.look_UD -= rel_y * Mouse_Sens
        self.look_UD = max(-90, min(90, self.look_UD))

    def update_camera_vectors(self):
        look_LR, look_UD = glm.radians(self.look_LR), glm.radians(self.look_UD)

        self.forward.x = glm.cos(look_LR) * glm.cos(look_UD)
        self.forward.y = glm.sin(look_UD)
        self.forward.z = glm.sin(look_LR) * glm.cos(look_UD)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def update(self):
        if self.use_orbit:
            self.update_orbit()
        else:
            self.move()
            self.rotate()
            self.update_camera_vectors()
            self.m_view = self.get_view_matrix()


    def move(self):
        velocity = Cam_Speed * self.app.delta_time
        keys = pg.key.get_pressed()
        
        # SHIFT == RUN // CTRL == SLOW (FLY CAMERA SPEED CONTROL)
        if keys[pg.K_LSHIFT] or keys[pg.K_RSHIFT]:
            velocity = 0.05 * self.app.delta_time
        elif keys[pg.K_LCTRL] or keys[pg.K_RCTRL]:
            velocity = 0.01 * self.app.delta_time
        else:
            velocity = 0.02 * self.app.delta_time
        
        if keys[pg.K_w]:
            self.position += self.forward * velocity
        if keys[pg.K_s]:
            self.position -= self.forward * velocity
        if keys[pg.K_a]:
            self.position -= self.right * velocity
        if keys[pg.K_d]:
            self.position += self.right * velocity
        if keys[pg.K_q]:
            self.position += self.up * velocity
        if keys[pg.K_e]:
            self.position -= self.up * velocity

    def update_orbit(self):
        keys = pg.key.get_pressed()
        
        
        if keys[pg.K_LSHIFT] or keys[pg.K_RSHIFT]:
            Rotate_Speed = 0.1 * self.app.delta_time
        elif keys[pg.K_LCTRL] or keys[pg.K_RCTRL]:
            Rotate_Speed = 0.02 * self.app.delta_time
        else:
            Rotate_Speed = 0.05 * self.app.delta_time
        
        if keys[pg.K_LEFT]:
            self.look_LR += Rotate_Speed
        if keys[pg.K_RIGHT]:
            self.look_LR -= Rotate_Speed
        if keys[pg.K_UP]:
            self.look_UD += Rotate_Speed
        if keys[pg.K_DOWN]:
            self.look_UD -= Rotate_Speed

        rel_x, rel_y = pg.mouse.get_rel()
        self.look_LR += rel_x * Mouse_Sens
        self.look_UD -= rel_y * Mouse_Sens
        self.look_UD = max(-90, min(90, self.look_UD))

        theta = glm.radians(self.look_LR)
        phi = glm.radians(self.look_UD)

        x = self.orbit_radius * glm.cos(phi) * glm.cos(theta)
        y = self.orbit_radius * glm.sin(phi)
        z = self.orbit_radius * glm.cos(phi) * glm.sin(theta)

        self.position = self.orbit_target + glm.vec3(x, y, z)
        self.forward = glm.normalize(self.orbit_target - self.position)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))
        self.m_view = self.get_view_matrix()


    # RESET CAMERA
    def set_default(self):
        self.position = glm.vec3(-6, 4.5, 6)
        self.orbit_target = glm.vec3(0, 0, 0)
        self.orbit_radius = 10
        
        if self.use_orbit:
            self.look_LR = 135
            self.look_UD = 25
        else:
            self.look_LR = -45
            self.look_UD = -25

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)

