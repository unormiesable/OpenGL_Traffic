from model import *
from comp_model import *
from animation import Animation
from pyglm import glm
import random
import math

# SCENE (PENATAAN OBJEK OBJEK PADA SCENE)
class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        
        self.load()
        self.skybox = NextSkyBox(app)
        

    def add_object(self, obj):
        self.objects.append(obj)
        

    def load(self):
        app = self.app
        add = self.add_object
        
        Plane = ColorPlane(app, uni_scale=15, specularity=1, pos=(0, 0, 0), color=(0.2, 0.2, 0.2))
        self.app.physics.add_physics('plane.urdf', Plane.pos, (0, 0, 0))
        add(Plane)
        

        # self.Cube_001 = ColorCube(app, pos=(0, 3, 0), rot=(0, 0, 0), color=(0.8, 0.3, 0.3), uni_scale=0.5,
        #                           specularity=1.0, metalness=0)
        # self.Cube_001_phy = self.app.physics.add_physics('cube.urdf', self.Cube_001.pos, self.Cube_001.rot, scale=0.5)
        # self.Cube_001.physics = self.Cube_001_phy
        # add(self.Cube_001)
        
        self.Cube_001 = ColorCube(app, pos=(0.5, 5, 0), rot=(0, 35, 20), color=(0.8, 0.3, 0.3), uni_scale=0.5,
                                  specularity=1.0, metalness=0)
        self.Cube_001_phy = self.app.physics.add_physics('cube.urdf', self.Cube_001.pos, self.Cube_001.rot, scale=0.5)
        self.Cube_001.physics = self.Cube_001_phy
        add(self.Cube_001)
        
        self.Cube_002 = ColorCube(app, pos=(0, 4, 0), rot=(0, 0, 0), uni_scale=0.5, color=(0.2, 0.4, 0.5),
                                  specularity=1.0, metalness=0)
        self.Cube_002_phy = self.app.physics.add_physics('cube.urdf', self.Cube_002.pos, self.Cube_002.rot, scale=0.5)
        self.Cube_002.physics = self.Cube_002_phy
        add(self.Cube_002)
        
        self.Cube_003 = ColorCube(app, pos=(-0.5, 7, 0.2), rot=(30, 25, 22), uni_scale=0.5, color=(0.4, 0.4, 0.2),
                                  specularity=1.0, metalness=0)
        self.Cube_003_phy = self.app.physics.add_physics('cube.urdf', self.Cube_003.pos, self.Cube_003.rot, scale=0.5)
        self.Cube_003.physics = self.Cube_003_phy
        add(self.Cube_003)
        
        self.Sphere_001 = ColorSphere(app, pos=(-0.5, 7, 0.2), rot=(0, 0, 0), uni_scale=0.5, color=(0.5, 0.2, 0.4),
                                  specularity=1.0, metalness=0)
        self.Sphere_001_phy = self.app.physics.add_physics('sphere2.urdf', self.Sphere_001.pos, self.Sphere_001.rot, scale=0.5)
        self.Sphere_001.physics = self.Sphere_001_phy
        add(self.Sphere_001)
        
        self.Sphere_002 = ColorSphere(app, pos=(0, 1.2, 0), rot=(0, 0, 0), uni_scale=0.5, color=(0.3, 0.3, 0.1),
                                  specularity=1.0, metalness=0)
        self.Sphere_002_phy = self.app.physics.add_physics('sphere2.urdf', self.Sphere_002.pos, self.Sphere_002.rot, scale=0.5)
        self.Sphere_002.physics = self.Sphere_002_phy
        add(self.Sphere_002)

        # add(ColorCube(app, pos=(0, 0, 0), color=(0, 0, 1), uni_scale=0.1, specularity=1.0, metalness=0))
        
                
    # SISTEM ANIMASI (MASIH BETA)
    def update(self):
        y = self.app.time
        
        for o in self.objects:
            if hasattr(o, 'anim'):
                o.anim.animate()
            
            if hasattr(o, 'physics'):
                o.pos = self.app.physics.get_pos(o.physics)
                rotation_quat = self.app.physics.get_rot(o.physics)
                o.update_quat(rotation_quat)
            