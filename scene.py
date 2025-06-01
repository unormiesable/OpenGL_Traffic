from model import *
from comp_model import *
from animation import Animation
from pyglm import glm
import random
import math

import pybullet as p

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
        
        Plane = ColorPlane(app, uni_scale=30, specularity=1, pos=(0, 0, 0), color=(0.3, 0.5, 0.3))
        self.app.physics.add_physics_urdf('plane.urdf', Plane.pos, (0, 0, 0))
        add(Plane)
        

        for x in range(10):
            for y in range(10):
                for z in range(5):
                    self.Cube_001 = ColorCube(app, pos=(-5 + (x * 1.1), 2 + (y * 1.2), -2.5 + (z * 1.1)),
                                            rot=(random.randint(0, 360), random.randint(0, 360), random.randint(0, 360)),
                                            color=(0.8, 0.3, 0.3),
                                            uni_scale=0.5, scale=(1, 1, 1),
                                            specularity=1.0, metalness=0)
                    self.Cube_001_phy = self.app.physics.add_physics_geometry(geometry=p.GEOM_BOX,
                                                                half_extents=(self.Cube_001.scale[0], self.Cube_001.scale[2], self.Cube_001.scale[1]),
                                                                pos=self.Cube_001.pos,
                                                                rot=self.Cube_001.rot,
                                                                mass=1)
                    self.Cube_001.physics = self.Cube_001_phy
                    add(self.Cube_001)
        
                
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
            