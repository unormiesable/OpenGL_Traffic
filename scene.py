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
        
        Plane = ColorPlane(app, uni_scale=5, specularity=0, pos=(0, 0, 0))
        self.app.physics.add_physics('plane.urdf', Plane.pos, (0, 0, 0))
        add(Plane)
        
        self.Cube_001 = ColorCube(app, pos=(0, 5, 0), specularity=1.0, metalness=0)
        self.Cube_001_phy = self.app.physics.add_physics('cube.urdf', self.Cube_001.pos, (0, 0, 0))
        add(self.Cube_001)
        
                
    # SISTEM ANIMASI (MASIH BETA)
    def update(self):
        for o in self.objects:
            if hasattr(o, 'anim') or hasattr(o, 'physics'):
                o.anim.animate()
    
        print(self.app.physics.get_pos(self.Cube_001_phy))
        self.Cube_001.pos = (self.app.physics.get_pos(self.Cube_001_phy))
        
        self.Cube_001.animate()