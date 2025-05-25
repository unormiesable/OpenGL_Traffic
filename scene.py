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
        
        # SPAWNER
        self.last_spawn_time = 0
        self.spawn_cooldown = 1000

        # WAKTU LAMPU
        self.wait_time = 2
        
        self.load()
        self.skybox = NextSkyBox(app)
        

    def add_object(self, obj):
        self.objects.append(obj)
        

    def load(self):
        app = self.app
        add = self.add_object
        
        add(ColorPlane(app, uni_scale = 5, pos=(0, 0, 0),
                       color=(0.6, 0.6, 0.8),
                       specularity=0.2, metalness=0))
        
        add(ColorCube(app, pos=(-1.5, 1, 0),
                      color=(0.8, 0.4, 0.4),
                      specularity=0.2, metalness=0))
        
        add(ColorCube(app, pos=(1.5, 1, 0),
                      color=(0.4, 0.8, 0.4),
                      specularity=0.2, metalness=1))
        
        
        # add(ColorCone(app, pos=(0, 1, 0),
        #               color=(0.8, 0.4, 0.4)))
        
        # add(ColorCylinder(app, pos=(0, 1, 0),
        #               color=(0.8, 0.4, 0.4)))
    
    # SISTEM ANIMASI (MASIH BETA)
    def update(self):
        pass