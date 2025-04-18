from model import *
import glm


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        # skybox
        self.skybox = AdvancedSkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object
        
        # Testing Primitive
        add(Cube(app, pos=(0, 1, 0)))
        
        # Testing OBJ File
        add(Gate(app, pos=(0, 0, 0)))
