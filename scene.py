from model import *
from comp_model import *
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
        
        self.main_obj = ColorCube(app, pos=(0, 2, 0), rot=(0, random.randint(0, 360), 0))
        self.objs.append(self.main_obj)
        add(self.main_obj)
        
        add(ColorPlane(app, pos=(0, 0, 0), color=(0.3, 0.5, 0.3), uni_scale=10, specularity=0.1))
            
    
    # SISTEM ANIMASI (MASIH BETA)
    def update(self):
        for o in self.objs:
            o.pos = glm.vec3(o.pos[0], 2 + math.sin( (self.app.time) * 2) * 0.8, o.pos[2])
            o.rot.y += 0.01
            o.update()

                