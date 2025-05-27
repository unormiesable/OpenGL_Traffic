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
        
        Plane.anim.add_keyframe(rot=(0, 0, 0), time=0)
        Plane.anim.add_keyframe(rot=(0, 180, 0), time=2)
        
        add(Plane)
        
                
    # SISTEM ANIMASI (MASIH BETA)
    def update(self):
        for o in self.objects:
            if hasattr(o, 'anim'):
                o.anim.animate()
        
                