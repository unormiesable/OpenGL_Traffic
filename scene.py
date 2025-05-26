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
        
        self.main_obj = ColorCylinder(app, pos=(0, 1, 0), rot=(0, random.randint(0, 360), 0))
        self.objs.append(self.main_obj)
        add(self.main_obj)

        self.main_obj = ColorPlane(app, pos=(0, 0, 0), rot=(0, 0, 0), uni_scale=5)
        self.objs.append(self.main_obj)
        add(self.main_obj)
            
    
    # SISTEM ANIMASI (MASIH BETA)
    def update(self):
        pass
                