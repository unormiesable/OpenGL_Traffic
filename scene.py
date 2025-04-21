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
        add(ColorPlane(app, pos=(0, 0, 0), color=(0.1, 0.1, 0.1), scale=(2, 1, 1), uni_scale= 10))
        # add(ColorCube(app, pos=(0, 2, 0), color=(1.0, 0.0, 0.0), scale=(1, 2, 1)))
        # add(ColorCylinder(app, pos=(0, 1, 0), color=(0.2, 0.2, 0.2), scale=(1, 1, 1), rot=(90, 0, 0)))
        
        # TEST DENGAN FILE OBJ (PROTOTYPING)
        # add(Gate(app, pos=(0, 0, 0)))
        # add(Yellow_Car(app, pos=(0, 0, 0), uni_scale= 0.8))
        
        # TESTING LOOP RANDOM COLOR
        # for i in range(10):
        #     add(ColorCube(app, pos=((i+1)-5, (i+1)/5, 0), color=(random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)), scale=(0.5, (i+1)/5, 1)))
    
        # GARIS JALAN
        for i in range(8):
            add(ColorCube(self.app, pos=(-16 + (i * 5), 0, 0), scale=(1, 0.05, 0.05)))
    
        # MOBIL MOBIL (TESTING CLASS MOBIL (MASIH PERLU DIPERBAIKI))
        # for i in range(5):
        #     car_position = (-16 + (i * 8) + random.uniform(0.0, 2.0), 0, random.randint(-7, 7))
        #     car_color = (random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0))
        #     Car(self.app, add ,position=car_position, color=car_color)
        
        for i in range(3):
            add(Fixed_Car(app, pos=(-10 + (i * 10), 0, random.randint(-7, 7)),
                          color=(random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0))
                          ))