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
    
    # SISTEM ANIMASI (MASIH BETA)
    def update(self):
        pass