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
        
        self.objs = []
        
        self.Cube_001 = ColorCube(app, pos=(0, 1, 0), rot=(0, 0, 0), color=(0.2, 0.8, 0.2))
        self.Cube_001.anim = Animation(self.Cube_001, app)
        self.objs.append(self.Cube_001)
        
        a = self.Cube_001.anim
        a.add_keyframe(pos=(0, 1, 0), rot=(0, 0, 0), scale=(1, 1, 1), time=3)
        a.add_keyframe(pos=(3, 1, 0), rot=(0, 180, 0), scale=(1, 1, 1), time=6)
        a.add_keyframe(pos=(-3, 1, 0), rot=(0, 360, 0), scale=(1, 1, 1), time=9)
        
        add(self.Cube_001)
        
        self.Plane_001 = ColorPlane(app, pos=(0, 0, 0), rot=(0, 0, 0), color=(0.3, 0.3, 0.5), uni_scale=5)
        self.objs.append(self.Plane_001)
        add(self.Plane_001)
                
    # SISTEM ANIMASI (MASIH BETA)
    def update(self):
        self.Cube_001.anim.animate()
        
                