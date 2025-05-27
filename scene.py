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
        
        Plane = ColorPlane(app, uni_scale=5)
        Plane.anim = Animation(Plane, app)
        
        Plane.anim.add_keyframe(rot=Plane.rot, time=0)
        Plane.anim.add_keyframe(rot=(0, 3600, 0), time=20)
        
        add(Plane)
        
        self.Cube = ColorCube(app, pos=(0, 1, 0))        
        add(self.Cube)
        
                
    # SISTEM ANIMASI (MASIH BETA)
    def update(self):
        for o in self.objects:
            if hasattr(o, 'anim'):
                o.anim.animate()
        
        self.Cube.pos = glm.vec3(0, 2 + (math.sin(self.app.time * 4))/2, 0)
        self.Cube.animate()