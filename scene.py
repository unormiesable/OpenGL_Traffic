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
        # add(ColorCylinder(app, pos=(0, 1, 0), color=(0.2, 0.2, 0.2), scale=(1, 1, 1), rot=(90, 0, 0)))
        
        
        # TEST DENGAN FILE OBJ (PROTOTYPING)
        # add(Gate(app, pos=(0, 0, 0)))
        # add(Yellow_Car(app, pos=(0, 0, 0), uni_scale= 0.8))
        
        # TESTING LOOP RANDOM COLOR
        # for i in range(10):
        #     add(ColorCube(app, pos=((i+1)-5, (i+1)/5, 0), color=(random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)), scale=(0.5, (i+1)/5, 1)))

        
        # TESTING BUAT MOBIL DARI PRIMITIF
        
        # BAN KIRI
        add(ColorCylinder(app, pos=(-2.0, 1, 1.8), color=(0.2, 0.2, 0.2), scale=(1, 0.3, 1), rot=(90, 0, 0)))
        add(ColorCylinder(app, pos=(-2.0, 1, 2.0), color=(1.0, 1.0, 1.0), scale=(1, 0.3, 1), rot=(90, 0, 0), uni_scale= 0.5))
        add(ColorCylinder(app, pos=(2.2, 1, 1.8), color=(0.2, 0.2, 0.2), scale=(1, 0.3, 1), rot=(90, 0, 0)))
        add(ColorCylinder(app, pos=(2.2, 1, 2.0), color=(1.0, 1.0, 1.0), scale=(1, 0.3, 1), rot=(90, 0, 0), uni_scale= 0.5))
        
        # BAN KANAN
        add(ColorCylinder(app, pos=(-2.0, 1, -1.8), color=(0.2, 0.2, 0.2), scale=(1, 0.3, 1), rot=(90, 0, 0)))
        add(ColorCylinder(app, pos=(-2.0, 1, -2.0), color=(1.0, 1.0, 1.0), scale=(1, 0.3, 1), rot=(90, 0, 0), uni_scale= 0.5))
        add(ColorCylinder(app, pos=(2.2, 1, -1.8), color=(0.2, 0.2, 0.2), scale=(1, 0.3, 1), rot=(90, 0, 0)))
        add(ColorCylinder(app, pos=(2.2, 1, -2.0), color=(1.0, 1.0, 1.0), scale=(1, 0.3, 1), rot=(90, 0, 0), uni_scale= 0.5))
        
        # BASE
        add(ColorCube(app, pos=(0.2, 2, 0), color=(1.0, 1.0, 0.0), scale=(3.4, 1, 1.6)))
        add(ColorCube(app, pos=(1, 3, 0), color=(1.0, 1.0, 0.0), scale=(0.7, 0.7, 1.5), rot=(0, 0, 45)))
        add(ColorCube(app, pos=(-1, 3, 0), color=(1.0, 1.0, 0.0), scale=(0.7, 0.7, 1.5), rot=(0, 0, 60)))
        add(ColorCube(app, pos=(-0.12, 3.3, 0), color=(1.0, 1.0, 0.0), scale=(1.12, 0.7, 1.5), rot=(0, 0, 0)))
        
        # WINDOW
        add(ColorCube(app, pos=(1.05, 3, 0), color=(0.8, 0.8, 1.0), scale=(0.7, 0.7, 1.3), rot=(0, 0, 45)))
        add(ColorCube(app, pos=(0.95, 3, 0), color=(0.8, 0.8, 1.0), scale=(0.7, 0.7, 1.52), rot=(0, 0, 45)))
        add(ColorCube(app, pos=(-1.05, 3, 0), color=(0.8, 0.8, 1.0), scale=(0.7, 0.7, 1.3), rot=(0, 0, 60)))
        add(ColorCube(app, pos=(-0.95, 3, 0), color=(0.8, 0.8, 1.0), scale=(0.7, 0.7, 1.52), rot=(0, 0, 60)))
        add(ColorCube(app, pos=(-0.12, 3.3, 0), color=(0.8, 0.8, 1.0), scale=(1.12, 0.64, 1.52), rot=(0, 0, 0)))