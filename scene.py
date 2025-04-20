from model import *
import glm
import random

# SCENE (PENATAAN OBJEK OBJEK PADA SCENE)
class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        # skybox
        self.skybox = SkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object
        
        # TEST DENGAN PRIMITIVE OBJECT
        
        # TEXTURED
        # add(Cube(app, pos=(0, 1, 0), scale=(1, 1, 1)))
        # add(Plane(app, pos=(0, 0, 0), uni_scale= 5))
        
        # NO TEXTURED
        add(ColorPlane(app, pos=(0, 0, 0), color=(1.0, 1.0, 0.5), uni_scale= 10))
        # add(ColorCube(app, pos=(0, 2, 0), color=(1.0, 0.0, 0.0), scale=(1, 2, 1)))

        
        # TEST DENGAN FILE OBJ (PROTOTYPING)
        # add(Gate(app, pos=(0, 0, 0)))
        # add(Yellow_Car(app, pos=(0, 0, 0), uni_scale= 0.8))
        
        for i in range(10):
            add(ColorCube(app, pos=((i+1)-5, (i+1)/5, 0), color=(random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)), scale=(0.5, (i+1)/5, 1)))
