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
        
        self.main_obj = ColorSphere(app, pos=(-6, 10, 0), rot=(0, 0, 0), specularity=0.5, metalness=0, color=(0.8, 0.2, 0.2))
        self.main_obj.down_vel = 0
        self.main_obj.side_vel = 0.03
        self.objs.append(self.main_obj)
        add(self.main_obj)

        self.main_obj = ColorPlane(app, pos=(0, 0, 0), rot=(0, 0, 0), uni_scale=5, color=(0.4, 0.4, 0.4), specularity=0.1, metalness=0)
        add(self.main_obj)
            
    
    # SISTEM ANIMASI (MASIH BETA)
    def update(self):
        for o in self.objs:
            
            if o.side_vel > 0:
                o.side_vel -= self.app.time * 0.00005
            
            collider = o.scale[1] * o.uni_scale
            if o.pos[1] > collider :
                o.down_vel += self.app.time * 0.001
                o.prev_vel = o.down_vel
                
                o.pos = glm.vec3(o.pos[0] + o.side_vel , o.pos[1] - (self.app.time * o.down_vel) , o.pos[2])
                o.rot = glm.vec3(o.rot[0] , o.rot[1], o.rot[2] - o.side_vel)
                
                o.update()
                print("Fall")
            
            if o.pos[1] < collider and (o.down_vel/2) > 0.005:
                o.down_vel = -(o.prev_vel/2)
                o.pos = glm.vec3(o.pos[0], o.pos[1] - (self.app.delta_time * o.down_vel) , o.pos[2])
                o.update()
                print("Hit")
                