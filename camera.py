import glm
import pygame as pg

# ATRIBUT KAMERA
FOV = 50
NEAR = 0.1
FAR = 100

Cam_Speed = 0.005
Mouse_Sens = 0.04


class Camera:
    def __init__(self, app, position=(-5, 1, 0), look_LR=0, look_UD=0):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        
        self.look_LR = look_LR
        self.look_UD = look_UD

        # VIEW MATRIX
        self.m_view = self.get_view_matrix()
        
        # PROJECTION MATRIX
        self.m_proj = self.get_projection_matrix()

    ## CAMERA CONTROLS ========================================================

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
        self.move()
        self.rotate()
        self.update_camera_vectors()
        self.m_view = self.get_view_matrix()

    def move(self):
        velocity = Cam_Speed * self.app.delta_time
        keys = pg.key.get_pressed()
        
        # SHIFT == RUN (Faster Aaah Movement)
        if keys[pg.K_LSHIFT] or keys[pg.K_RSHIFT]:
            velocity = 0.01 * self.app.delta_time
        else:
            velocity = 0.005 * self.app.delta_time
        
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

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)




















