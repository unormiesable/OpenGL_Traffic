from model import *
import glm
import random
import math

# SCENE (PENATAAN OBJEK OBJEK PADA SCENE)
class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        
        # LIST MOBIL
        self.cars = []
        
        self.load()
        self.skybox = SkyBox(app)
        


    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object
        
        # JALAN
        add(ColorPlane(app, pos=(0, 0, 0), color=(0.1, 0.1, 0.1), scale=(2, 1, 1), uni_scale= 10))

        # GARIS JALAN
        for i in range(8):
            add(ColorCube(self.app, pos=(-16 + (i * 5), 0, 0), scale=(1, 0.05, 0.05)))
            
        # TROTOAR
        add(ColorCube(self.app, pos=(0, 0, 12), scale=(20, 0.1, 2), color=(0.3, 0.3, 0.3)))
        add(ColorCube(self.app, pos=(0, 0, -12), scale=(20, 0.1, 2), color=(0.3, 0.3, 0.3)))
    
        for i in range(4):
            car = Fixed_Car(app, pos=(-5 + (i * 6), 0, random.uniform(-8.0, 8.0)),
                            color=(random.uniform(0.0, 0.8), random.uniform(0.0, 0.8), random.uniform(0.0, 0.8)),
                            sec_color=(random.uniform(0.3, 0.8), random.uniform(0.3, 0.8), random.uniform(0.3, 0.8)),
                            uni_scale=0.7, spoiler=random.randint(0, 1), is_taxi=random.randint(0, 1))
            car.speed = 6
            add(car)
            self.cars.append(car)
        
        # TEST ADD POHON
        for i in range(20):
            add(Tree(app, pos=(-20 + (i * 2), -0.06, random.randint(-20, -15)), 
                     uni_scale=random.uniform(0.9, 1.1), 
                     rot=(0, random.randint(0, 360), 0)))
            
            add(Tree(app, pos=(-20 + (i * 2), -0.06, random.randint(15, 20)), 
                     uni_scale=random.uniform(0.9, 1.1), 
                     rot=(0, random.randint(0, 360), 0)))
            
        # ADD DASAR
        add(ColorPlane(app, pos=(0, -0.02, 0), uni_scale = 30, color=(0.39, 0.26, 0.13)))

        
    # SISTEM ANIMASI (MASIH BETA)
    def update(self):
                
        # ANIMASI MOBIL MOBIL
        def animate_cars():
            
            for car in self.cars:
                car.pos[0] -= car.speed * self.app.delta_time / 1000.0
                if car.pos[0] < -18:
                    car.pos[0] = 18
                    car.pos[2] = random.randint(-7, 7)
                    car.update_car_color(new_prime_color=(random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)),
                                        new_sec_color=(random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)))
                
                # ANIMASI BAN TIAP MOBIL
                car.ban_kiri_depan.rot[2] = self.app.time * 3
                car.ban_kiri_belakang.rot[2] = self.app.time * 3
                car.ban_kanan_depan.rot[2] = self.app.time * 3
                car.ban_kanan_belakang.rot[2] = self.app.time * 3
                
                car.update()
                
        animate_cars()
