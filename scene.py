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
        
        Plane = ColorPlane(app, uni_scale=5, specularity=0)
        Plane.anim = Animation(app, Plane)
        
        Plane.anim.add_keyframe(rot=Plane.rot, time=2, interpolation='ease_in_out')
        Plane.anim.add_keyframe(rot=(0, 720, 0), time=5, interpolation='ease_in_out')
        Plane.anim.add_keyframe(rot=(0, 360, 0), time=10, interpolation='ease_in_out')
        
        add(Plane)
        
        self.Cube = ColorCube(app, pos=(0, 1, 0), specularity=1.0, metalness=0)        
        add(self.Cube)
        
                
    # SISTEM ANIMASI (MASIH BETA)
    def update(self):
        for o in self.objects:
            if hasattr(o, 'anim'):
                o.anim.animate()
        
        self.Cube.pos = glm.vec3(0, 2 + (math.sin(self.app.time * 4))/2, 0)
        self.Cube.animate()