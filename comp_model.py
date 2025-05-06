import moderngl as mgl
import numpy as np
import glm
from model import *


# MODEL KOMPOSISI
# TES KUBUS DAN PLANE
class Cube_Plane:
    def __init__(self, app, pos=(0, 0, 0), rot=(0, 0, 0),
                 scale=(1, 1, 1), uni_scale=1, color=(1.0, 1.0, 1.0)):

        self.app = app
        self.pos = glm.vec3(pos)
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = glm.vec3(scale) * uni_scale
        self.color = glm.vec3(color)

        # BUAT OBJEK DARI PRIMITIF
        self.plane = ColorPlane(app, pos=(0, 0, 0), color=color, scale=(5, 5, 5))
        self.cube = ColorCube(app, pos=(0, 1, 0), color=color, scale=(1, 1, 1))

        self.update_model_matrices()

    def get_model_matrix(self, part):
        m_model = glm.mat4()

        # TRANSFORMASI PARENT
        m_model = glm.translate(m_model, self.pos)
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        m_model = glm.scale(m_model, self.scale)

        # TRANSFORMASI LOKAL
        m_model = glm.translate(m_model, glm.vec3(part.pos))
        m_model = glm.rotate(m_model, part.rot.z, glm.vec3(0, 0, 1))
        m_model = glm.rotate(m_model, part.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, part.rot.x, glm.vec3(1, 0, 0))
        m_model = glm.scale(m_model, glm.vec3(part.scale))

        return m_model

    def update_model_matrices(self):
        self.plane.m_model = self.get_model_matrix(self.plane)
        self.cube.m_model = self.get_model_matrix(self.cube)

    def update(self):
        self.update_model_matrices()

        self.plane.color = self.color
        self.cube.color = self.color

        self.plane.update()
        self.cube.update()

    def render(self):
        self.plane.render()
        self.cube.render()

    def render_shadow(self):
        self.plane.render_shadow()
        self.cube.render_shadow()
        

# MODEL MOBIL 
class Fixed_Car:
    def __init__(self, app, pos=(0, 0, 0), rot=(0, 0, 0),
                 scale=(1, 1, 1), uni_scale=1, color=(1.0, 1.0, 1.0),
                 win_color=(0.6, 0.6, 0.8), head_size=0.25, sec_color=(1.0, 1.0, 1.0), 
                 spoiler=True, is_taxi=False):

        self.app = app
        self.pos = glm.vec3(pos)
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = glm.vec3(scale) * uni_scale
        self.color = glm.vec3(color)
        self.uni_scale = uni_scale
        self.head_size = head_size
        self.sec_color = sec_color
        self.add_spoiler = spoiler
        self.is_taxi = is_taxi

        self.win_color = win_color
        
        # BUAT OBJEK DARI PRIMITIF
        # BODY
        self.body = ColorCube(app, pos=glm.vec3(0.0, 1.5, 0.0), color=color, scale=(3.0, 1.0, 1.5))
        self.roof = ColorCube(app, pos=(0.5, 2.6, 0.0), color=color, scale=(1, 1, 1.4))
        self.windf = ColorCube(app, pos=(self.roof.pos[0] - 1.0, 2.18, 0.0), color=color, scale=(1, 1, 1.4), rot=(0, 0, 45))
        self.windb = ColorCube(app, pos=(self.roof.pos[0] + 0.65, 2.24, 0.0), color=color, scale=(1, 1, 1.4), rot=(0, 0, 30))
        
        # BUMPER
        self.bumper = ColorCube(app, pos=(0.0, 0.74, 0.0), color=sec_color, scale=(3.1, 0.25, 1.6))
        
        # WIND MISC
        self.winmid = ColorCube(app, pos=(0.5, 2.6, 0.0), color=color, scale=(0.1, 1, self.roof.scale[2] + 0.005))
        
        
        # WINDOWS
        self.glassf = ColorCube(app, pos=(self.roof.pos[0] - 1.1, 2.3, 0.0), color=win_color, scale=(1, 1, self.roof.scale[2]), rot=(0, 0, 45), uni_scale=0.85)
        self.glassb = ColorCube(app, pos=(self.roof.pos[0] + 0.8, 2.3, 0.0), color=win_color, scale=(1, 1, self.roof.scale[2]), rot=(0, 0, 30), uni_scale=0.85)
        
        self.glassfs = ColorCube(app, pos=(self.roof.pos[0] - 1.0, 2.3, 0.0), color=win_color, scale=(1, 1, self.roof.scale[2] + 0.25), rot=(0, 0, 45), uni_scale=0.85)
        self.glassbs = ColorCube(app, pos=(self.roof.pos[0] + 0.65, 2.33, 0.0), color=win_color, scale=(1, 1, self.roof.scale[2] + 0.25), rot=(0, 0, 30), uni_scale=0.85)
        self.glassms = ColorCube(app, pos=(self.roof.pos[0] - 0.03, 2.65, 0.0), color=win_color, scale=(1.15, 1, self.roof.scale[2] + 0.25), rot=(0, 0, 0), uni_scale=0.85)
        
        # BAN KIRI
        self.ban_kiri_depan = ColorCylinder(app, pos=(-2, 0.9, 1.8), color=(0.2, 0.2, 0.2), rot=(90, 0, 0), scale=(1, 0.35, 1), uni_scale=0.9)
        self.ban_kiri_belakang = ColorCylinder(app, pos=(2, 1, 1.8), color=(0.2, 0.2, 0.2), rot=(90, 0, 0), scale=(1, 0.4, 1))
        
        # VELG KIRI
        self.velg_kiri_depan = ColorCylinder(app, pos=(-2, 0.9, 2.05), color=(0.8, 0.8, 0.8), rot=(90, 0, 0), scale=(1, 0.37, 1), uni_scale=0.35)
        self.velg_kiri_belakang = ColorCylinder(app, pos=(2, 1, 2.05), color=(0.8, 0.8, 0.8), rot=(90, 0, 0), scale=(1, 0.5, 1), uni_scale=0.4)

        # BAN KANAN
        self.ban_kanan_depan = ColorCylinder(app, pos=(-2, 0.9, -1.8), color=(0.2, 0.2, 0.2), rot=(90, 0, 0), scale=(1, 0.35, 1), uni_scale=0.9)
        self.ban_kanan_belakang = ColorCylinder(app, pos=(2, 1, -1.8), color=(0.2, 0.2, 0.2), rot=(90, 0, 0), scale=(1, 0.4, 1))
        
        # VELG KANAN
        self.velg_kanan_depan = ColorCylinder(app, pos=(-2, 0.9, -2.05), color=(0.8, 0.8, 0.8), rot=(90, 0, 0), scale=(1, 0.37, 1), uni_scale=0.35)
        self.velg_kanan_belakang = ColorCylinder(app, pos=(2, 1, -2.05), color=(0.8, 0.8, 0.8), rot=(90, 0, 0), scale=(1, 0.5, 1), uni_scale=0.4)
        
        # HEADLIGHT
        self.headlightl = ColorCylinder(app, rot=(0, 0, 90), scale=(self.head_size, 0.1, self.head_size), pos=(-3, 1.9, 1), color=win_color)
        self.headlightr = ColorCylinder(app, rot=(0, 0, 90), scale=(self.head_size, 0.1, self.head_size), pos=(-3, 1.9, -1), color=win_color)
        
        self.headlightl_out = ColorCylinder(app, color=(0.2, 0.2, 0.2), rot=(0, 0, 90), scale=(self.head_size + 0.1, 0.1, self.head_size + 0.1), pos=(-2.95, 1.9, 1))
        self.headlightr_out = ColorCylinder(app, color=(0.2, 0.2, 0.2), rot=(0, 0, 90), scale=(self.head_size + 0.1, 0.1, self.head_size + 0.1), pos=(-2.95, 1.9, -1))
        
        # BACKLIGHT
        self.backlightl = ColorCube(app, pos=(3, 2, 1), scale=(0.05, 0.15, 0.3), color=(0.8, 0.2, 0.2))
        self.backlightr = ColorCube(app, pos=(3, 2, -1), scale=(0.05, 0.15, 0.3), color=(0.8, 0.2, 0.2))
        
        # SPOILER
        self.spoiler = ColorCube(app, pos=(2.65, 3, 0), scale=(0.25, 0.05, 1.5), color=sec_color)
        self.spoiler_stand_kiri = ColorCube(app, pos=(2.65, 2.5, 0.8), scale=(0.07, 0.5, 0.07), color=sec_color)
        self.spoiler_stand_kanan = ColorCube(app, pos=(2.65, 2.5, -0.8), scale=(0.07, 0.5, 0.07), color=sec_color)
        
        # MODE TAXI
        self.mode_taxi = ColorCube(app, pos=(0.5, 3.7, 0), scale=(0.07, 0.3, 0.6), color=sec_color)
        
        self.update_model_matrices()
        

    def get_model_matrix(self, part):
        m_model = glm.mat4()

        # TRANSFORMASI PARENT
        m_model = glm.translate(m_model, self.pos)
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        m_model = glm.scale(m_model, self.scale * self.uni_scale)

        # TRANSFORMASI LOKAL
        m_model = glm.translate(m_model, glm.vec3(part.pos))
        m_model = glm.rotate(m_model, part.rot.z, glm.vec3(0, 0, 1))
        m_model = glm.rotate(m_model, part.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, part.rot.x, glm.vec3(1, 0, 0))
        m_model = glm.scale(m_model, glm.vec3(part.scale))

        return m_model

    # UPDATE MATRIX OBJEK (UPDATE TRANSFORMASI KESELURUHAN -> UNTUK TIAP PRIMITIF)
    def update_model_matrices(self):
        self.body.m_model = self.get_model_matrix(self.body)
        self.roof.m_model = self.get_model_matrix(self.roof)
        self.windf.m_model = self.get_model_matrix(self.windf)
        self.windb.m_model = self.get_model_matrix(self.windb)
        
        self.bumper.m_model = self.get_model_matrix(self.bumper)
        
        self.winmid.m_model = self.get_model_matrix(self.winmid)
        
        self.glassf.m_model = self.get_model_matrix(self.glassf)
        self.glassb.m_model = self.get_model_matrix(self.glassb)
        self.glassfs.m_model = self.get_model_matrix(self.glassfs)
        self.glassbs.m_model = self.get_model_matrix(self.glassbs)
        self.glassms.m_model = self.get_model_matrix(self.glassms)
        
        self.ban_kiri_depan.m_model = self.get_model_matrix(self.ban_kiri_depan)
        self.ban_kiri_belakang.m_model = self.get_model_matrix(self.ban_kiri_belakang)
        self.ban_kanan_depan.m_model = self.get_model_matrix(self.ban_kanan_depan)
        self.ban_kanan_belakang.m_model = self.get_model_matrix(self.ban_kanan_belakang)
        
        self.velg_kiri_depan.m_model = self.get_model_matrix(self.velg_kiri_depan)
        self.velg_kiri_belakang.m_model = self.get_model_matrix(self.velg_kiri_belakang)
        self.velg_kanan_depan.m_model = self.get_model_matrix(self.velg_kanan_depan)
        self.velg_kanan_belakang.m_model = self.get_model_matrix(self.velg_kanan_belakang)
        
        self.headlightl.m_model = self.get_model_matrix(self.headlightl)
        self.headlightr.m_model = self.get_model_matrix(self.headlightr)
        self.headlightl_out.m_model = self.get_model_matrix(self.headlightl_out)
        self.headlightr_out.m_model = self.get_model_matrix(self.headlightr_out)
        
        self.backlightl.m_model = self.get_model_matrix(self.backlightl)
        self.backlightr.m_model = self.get_model_matrix(self.backlightr)
        
        self.spoiler.m_model = self.get_model_matrix(self.spoiler)
        self.spoiler_stand_kiri.m_model = self.get_model_matrix(self.spoiler_stand_kiri)
        self.spoiler_stand_kanan.m_model = self.get_model_matrix(self.spoiler_stand_kanan)
        
        self.mode_taxi.m_model = self.get_model_matrix(self.mode_taxi)

    def update(self):
        self.update_model_matrices()

    def update_car_color(self, new_prime_color, new_sec_color):
        self.color = glm.vec3(new_prime_color)
        self.sec_color = glm.vec3(new_sec_color)
        
        self.body.color = self.color
        self.roof.color = self.color
        self.windf.color = self.color
        self.windb.color = self.color
        self.bumper.color = self.sec_color
        self.winmid.color = self.color
        self.spoiler.color = self.sec_color
        self.spoiler_stand_kiri.color = self.sec_color
        self.spoiler_stand_kanan.color = self.sec_color
        self.mode_taxi.color = self.sec_color
        
        self.update_model_matrices()

    def render(self):
        self.body.render()
        self.roof.render()
        self.windf.render()
        self.windb.render()
        
        self.bumper.render()
        
        self.winmid.render()
        
        self.glassf.render()
        self.glassb.render()
        self.glassfs.render()
        self.glassbs.render()
        self.glassms.render()
        
        self.ban_kiri_depan.render()
        self.ban_kiri_belakang.render()
        self.ban_kanan_depan.render()
        self.ban_kanan_belakang.render()
        
        self.velg_kiri_depan.render()
        self.velg_kiri_belakang.render()
        self.velg_kanan_depan.render()
        self.velg_kanan_belakang.render()
        
        self.headlightl.render()
        self.headlightr.render()
        self.headlightl_out.render()
        self.headlightr_out.render()
        
        self.backlightl.render()
        self.backlightr.render()
        
        if self.add_spoiler == True:
            self.spoiler.render()
            self.spoiler_stand_kiri.render()
            self.spoiler_stand_kanan.render()
        
        if self.is_taxi == True:
            self.mode_taxi.render()
            

    def render_shadow(self):
        self.body.render_shadow()
        self.roof.render_shadow()
        self.windf.render_shadow()
        self.windb.render_shadow()
        
        self.bumper.render_shadow()
        
        self.winmid.render_shadow()
        
        self.glassf.render_shadow()
        self.glassb.render_shadow()
        self.glassfs.render_shadow()
        self.glassbs.render_shadow()
        self.glassms.render_shadow()
        
        self.ban_kiri_depan.render_shadow()
        self.ban_kiri_belakang.render_shadow()
        self.ban_kanan_depan.render_shadow()
        self.ban_kanan_belakang.render_shadow()
        
        self.velg_kiri_depan.render_shadow()
        self.velg_kiri_belakang.render_shadow()
        self.velg_kanan_depan.render_shadow()
        self.velg_kanan_belakang.render_shadow()
        
        self.headlightl.render_shadow()
        self.headlightr.render_shadow()
        self.headlightl_out.render_shadow()
        self.headlightr_out.render_shadow()
        
        self.backlightl.render_shadow()
        self.backlightr.render_shadow()
        
        if self.add_spoiler == True:
            self.spoiler.render_shadow()
            self.spoiler_stand_kiri.render_shadow()
            self.spoiler_stand_kanan.render_shadow()

        if self.is_taxi == True:
            self.mode_taxi.render_shadow()
      
# MODEL POHON
class Tree:
    def __init__(self, app, pos=(0, 0, 0), rot=(0, 0, 0),
                 scale=(1, 1, 1), uni_scale=1, batang_color=(0.3, 0.2, 0.1), daun_color=(0.3, 0.4, 0.1), color=(1, 1, 1), uni_scale_batang=1, uni_scale_daun=1):

        self.app = app
        self.pos = glm.vec3(pos)
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = glm.vec3(scale) * uni_scale
        self.color = glm.vec3(color)

        # BUAT OBJEK DARI PRIMITIF
        self.batang = ColorCylinder(app, pos=(0, 1, 0), color=batang_color, scale=(0.2, 1, 0.2), uni_scale=uni_scale_batang)
        
        self.daun_bawah = ColorCone(app, pos=(0, 3, 0), color=daun_color, scale=(1.2, 1, 1.2), uni_scale=uni_scale_daun, rot=(5, 0, 2))
        self.daun_tengah = ColorCone(app, pos=(0, 4.2, 0), color=daun_color, scale=(1.1, 1, 1.1), uni_scale=uni_scale_daun, rot=(2, 0, 5))
        self.daun_atas = ColorCone(app, pos=(0, 5.3, 0), color=daun_color, scale=(0.95, 0.9, 0.95), uni_scale=uni_scale_daun, rot=(4, 0, 3))

        self.update_model_matrices()

    def get_model_matrix(self, part):
        m_model = glm.mat4()

        # TRANSFORMASI PARENT
        m_model = glm.translate(m_model, self.pos)
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        m_model = glm.scale(m_model, self.scale)

        # TRANSFORMASI LOKAL
        m_model = glm.translate(m_model, glm.vec3(part.pos))
        m_model = glm.rotate(m_model, part.rot.z, glm.vec3(0, 0, 1))
        m_model = glm.rotate(m_model, part.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, part.rot.x, glm.vec3(1, 0, 0))
        m_model = glm.scale(m_model, glm.vec3(part.scale))

        return m_model

    def update_model_matrices(self):
        self.batang.m_model = self.get_model_matrix(self.batang)
        
        self.daun_bawah.m_model = self.get_model_matrix(self.daun_bawah)
        self.daun_tengah.m_model = self.get_model_matrix(self.daun_tengah)
        self.daun_atas.m_model = self.get_model_matrix(self.daun_atas)

    def update(self):
        self.update_model_matrices()

        self.batang.color = self.color
        
        self.daun_bawah.color = self.color
        self.daun_tengah.color = self.color
        self.daun_atas.color = self.color

        self.batang.update()
        
        self.daun_bawah.update()
        self.daun_tengah.update()
        self.daun_atas.update()

    def render(self):
        self.batang.render()
        
        self.daun_bawah.render()
        self.daun_tengah.render()
        self.daun_atas.render()

    def render_shadow(self):
        self.batang.render_shadow()
        
        self.daun_bawah.render_shadow()
        self.daun_tengah.render_shadow()
        self.daun_atas.render_shadow()


# MODEL TRAFFIC LIGHT
class Traffic_Light:
    def __init__(self, app, pos=(0, 0, 0), rot=(0, 0, 0),
                 scale=(1, 1, 1), uni_scale=1, color=(1.0, 1.0, 1.0)):

        self.app = app
        self.pos = glm.vec3(pos)
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = glm.vec3(scale) * uni_scale
        self.color = glm.vec3(color)

        # BUAT OBJEK DARI PRIMITIF
        ## UTAMA
        self.tiang = ColorCylinder(app, pos=(0, 2, 0), color=(0.5, 0.5, 0.5), scale=(0.15, 2, 0.15),)
        self.box = ColorCube(app, pos=(0, 5, 0), uni_scale=0.4, scale=(1, 3, 1), color=(0.1, 0.1, 0.1))

        self.red_light = ColorCylinder(app, pos=(-0.05, 5.7, 0), rot=(0, 0, 90), scale=(0.3, 0.4, 0.3), color=(1, 0, 0))
        self.yellow_light = ColorCylinder(app, pos=(-0.05, 5, 0), rot=(0, 0, 90), scale=(0.3, 0.4, 0.3), color=(1, 1, 0))
        self.green_light = ColorCylinder(app, pos=(-0.05, 4.3, 0), rot=(0, 0, 90), scale=(0.3, 0.4, 0.3), color=(0, 1, 0))

        ## DETAIL

        self.update_model_matrices()

    def get_model_matrix(self, part):
        m_model = glm.mat4()

        # TRANSFORMASI PARENT
        m_model = glm.translate(m_model, self.pos)
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        m_model = glm.scale(m_model, self.scale)

        # TRANSFORMASI LOKAL
        m_model = glm.translate(m_model, glm.vec3(part.pos))
        m_model = glm.rotate(m_model, part.rot.z, glm.vec3(0, 0, 1))
        m_model = glm.rotate(m_model, part.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, part.rot.x, glm.vec3(1, 0, 0))
        m_model = glm.scale(m_model, glm.vec3(part.scale))

        return m_model

    def update_model_matrices(self):
        self.tiang.m_model = self.get_model_matrix(self.tiang)
        self.box.m_model = self.get_model_matrix(self.box)
        self.red_light.m_model = self.get_model_matrix(self.red_light)
        self.yellow_light.m_model = self.get_model_matrix(self.yellow_light)
        self.green_light.m_model = self.get_model_matrix(self.green_light)


    def update(self):
        self.update_model_matrices()


    # GANTI WARNA LAMPU MERAH
    def change_to_red(self):
        self.red_light.color = glm.vec3(1, 0, 0)
        self.yellow_light.color = glm.vec3(0.2, 0.2, 0)
        self.green_light.color = glm.vec3(0, 0.2, 0)

        self.red_light.update()
        self.green_light.update()
        self.yellow_light.update()

    # GANTI WARNA LAMPU KUNING
    def change_to_yellow(self):
        self.red_light.color = glm.vec3(0.2, 0, 0)
        self.yellow_light.color = glm.vec3(1, 1, 0)
        self.green_light.color = glm.vec3(0, 0.2, 0)

        self.red_light.update()
        self.green_light.update()
        self.yellow_light.update()

    # GANTI WARNA LAMPU IJO
    def change_to_green(self):
        self.red_light.color = glm.vec3(0.2, 0, 0)
        self.yellow_light.color = glm.vec3(0.2, 0.2, 0)
        self.green_light.color = glm.vec3(0, 1, 0)

        self.red_light.update()
        self.green_light.update()
        self.yellow_light.update()


    def render(self):
        self.tiang.render()
        self.box.render()
        self.red_light.render()
        self.yellow_light.render()
        self.green_light.render()

    def render_shadow(self):
        self.tiang.render_shadow()
        self.box.render_shadow()
        self.red_light.render_shadow()
        self.yellow_light.render_shadow()
        self.green_light.render_shadow()