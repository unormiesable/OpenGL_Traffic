from model import *
from comp_model import *
import glm
import random
import math

# SCENE (PENATAAN OBJEK OBJEK PADA SCENE)
class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        
        # LIST MOBIL
        self.cars0 = []
        self.cars1 = []
        
        # LIST ANTRIAN DI JALAN (UNTUK MENDAPATKAN POSISI MOBIL PALING BELAKANG)
        self.antrian0 = []
        self.antrian1 = []
        self.antrian2 = []
        self.antrian3 = []
        
        self.load()
        self.skybox = NextSkyBox(app)
        

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        # MAIN SCENE ==============================================================================
        # # JALAN
        add(ColorPlane(app, pos=(0, 0, 0),
                       scale=(20, 1, 2),
                       color=(0.1, 0.1, 0.1),
                       ))
        
        add(ColorPlane(app, pos=(0, 0, 0),
                       scale=(2, 1, 20),
                       color=(0.1, 0.1, 0.1),
                       ))
        
        # # GARIS JALAN
        add(ColorPlane(app, pos=(3, 0.01, 1), scale=(0.02, 1, 1), color=(0.6, 0.6, 0.6)))
        add(ColorPlane(app, pos=(11.5, 0.01, 0), scale=(8.5, 1, 0.02), color=(0.6, 0.6, 0.6)))

        add(ColorPlane(app, pos=(-3, 0.01, -1), scale=(0.02, 1, 1), color=(0.6, 0.6, 0.6)))
        add(ColorPlane(app, pos=(-11.5, 0.01, 0), scale=(8.5, 1, 0.02), color=(0.6, 0.6, 0.6)))

        add(ColorPlane(app, pos=(1, 0.01, -3), scale=(1, 1, 0.02), color=(0.6, 0.6, 0.6)))
        add(ColorPlane(app, pos=(-0, 0.01, -11.5), scale=(0.02, 1, 8.5), color=(0.6, 0.6, 0.6)))

        add(ColorPlane(app, pos=(-1, 0.01, 3), scale=(1, 1, 0.02), color=(0.6, 0.6, 0.6)))
        add(ColorPlane(app, pos=(-0, 0.01, 11.5), scale=(0.02, 1, 8.5), color=(0.6, 0.6, 0.6)))

        # # TROTOAR
        color_trotoar = (0.3, 0.3, 0.3)
        add(ColorCube(app, pos=(11, 0, 11),
                      scale=(9, 0.1, 9),
                      color=color_trotoar))
        
        add(ColorCube(app, pos=(-11, 0, 11),
                      scale=(9, 0.1, 9),
                      color=color_trotoar))
        
        add(ColorCube(app, pos=(-11, 0, -11),
                      scale=(9, 0.1, 9),
                      color=color_trotoar))
        
        add(ColorCube(app, pos=(11, 0, -11),
                      scale=(9, 0.1, 9),
                      color=color_trotoar))
        
        # # TAMAN
        add(ColorCube(app, pos=(11, 0.02, 11),
                      scale=(8, 0.1, 8),
                      color=(0.35, 0.25, 0.15)))
        
        # # POHON

        for x in range(16):
            for z in range(16):
                add(Tree(app, pos=((3.5 + random.uniform(0, 0.7)) + x * 0.9, 0.1, 4 + z * 0.9 + random.uniform(0, 1)),
                            uni_scale=0.3 * random.uniform(0.80, 1.2),
                            rot=(0, random.randint(0, 360), 0),
                            daun_color=(0.3 + random.uniform(-0.05, 0.05), 0.4 + random.uniform(-0.05, 0.05), 0.1 + random.uniform(-0.05, 0.05))))

        # # TRAFFIC LIGHTS
        self.lampu0 = Traffic_Light(app, pos=(-2.5, 0, -2.5), uni_scale=0.25, rot=(0, 0, 0))
        add(self.lampu0)

        self.lampu1 = Traffic_Light(app, pos=(2.5, 0, -2.5), uni_scale=0.25, rot=(0, -90, 0))
        add(self.lampu1)

        self.lampu2 = Traffic_Light(app, pos=(-2.5, 0, 2.5), uni_scale=0.25, rot=(0, 90, 0))
        add(self.lampu2)

        self.lampu3 = Traffic_Light(app, pos=(2.5, 0, 2.5), uni_scale=0.25, rot=(0, 180, 0))
        add(self.lampu3)


        # # BUILDINGS
        for x in range(6):
            add(Building(app, floor=int(random.uniform(4.0, 9.0)), uni_scale=0.6,
                        color=(random.uniform(0.1, 0.5), random.uniform(0.1, 0.5), random.uniform(0.1, 0.5) ), win_scale=0.9,
                        scale=(0.6, 1, 0.6),
                        pos=(-5 - x*2.5, 0.1, -5), top_color=(random.uniform(0.1, 0.5), random.uniform(0.1, 0.5), random.uniform(0.1, 0.5))))

            add(Building(app, floor=int(random.uniform(4.0, 9.0)), uni_scale=0.6,
                        color=(random.uniform(0.1, 0.5), random.uniform(0.1, 0.5), random.uniform(0.1, 0.5) ), win_scale=0.9,
                        scale=(0.6, 1, 0.6),
                        pos=(-5 - x*2.5, 0.1, 5), top_color=(random.uniform(0.1, 0.5), random.uniform(0.1, 0.5), random.uniform(0.1, 0.5))))

        # # PARKIRAN
        add(ColorPlane(app, pos=(-11, 0.11, -12), uni_scale=5, scale=(1.5, 1, 1),
                       color=(0.1, 0.1, 0.1)))
        
        add(ColorPlane(app, pos=(-11, 0.12, -12), uni_scale=5, scale=(1.5, 1, 0.01),
                       color=(0.5, 0.5, 0.0)))
        
        # # PARKING LINES
        for x in range(7):          
            add(ColorPlane(app, pos=(-5 -x*2, 0.12, -11.1), uni_scale=5, scale=(0.2, 1, 0.01),
                        color=(0.5, 0.5, 0.0),
                        rot=(0, 65, 0)))

            add(ColorPlane(app, pos=(-5 -x*2, 0.12, -12.9), uni_scale=5, scale=(0.2, 1, 0.01),
                        color=(0.5, 0.5, 0.0),
                        rot=(0, -65, 0)))
        
        # # PARKED CARS
        for x in range(random.randint(2, 6)):
            random1 = random.randint(0, 1)
            random2 = random.randint(0, 1)
            
            if random1 == 1:
                add(Fixed_Car(app, pos=(-6 -x*2, 0.1, -11), uni_scale=0.45,
                            rot=(0, 245, 0), color=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)),
                            sec_color=(random.uniform(0, 0.4), random.uniform(0, 0.4), random.uniform(0, 0.4)),
                            is_taxi=random.randint(0, 1), spoiler=random.randint(0, 1)))
            
            if random2 == 1:
                add(Fixed_Car(app, pos=(-6 -x*2, 0.1, -13), uni_scale=0.45,
                            rot=(0, -245, 0),color=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)),
                            sec_color=(random.uniform(0, 0.4), random.uniform(0, 0.4), random.uniform(0, 0.4)),
                            is_taxi=random.randint(0, 1), spoiler=random.randint(0, 1)))

        # # CARS
        for x in range(random.randint(3, 6)):
            car = Fixed_Car(app, pos=(-10 + x*3, 0, -1), uni_scale=0.45,
                        is_taxi=random.randint(0, 1), spoiler=random.randint(0, 1),
                        color=(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)),
                        sec_color=(random.uniform(0, 0.4), random.uniform(0, 0.4), random.uniform(0, 0.4)),
                        rot=(0, 180, 0), id=x)
            car.speed = 5
            add(car)
            self.cars0.append(car)
        
        
    # SISTEM ANIMASI (MASIH BETA)
    def update(self):

        # ANIMASI LAMPU (MASIH CARA KOBOY)
        def animate_lights(divider:int):
            if (int(self.app.time / divider) %4 == 0 ) : 
                self.lampu0.change_to_green()

                self.lampu1.change_to_red()
                self.lampu2.change_to_red()
                self.lampu3.change_to_red()
            
            elif (int(self.app.time / divider) %4 == 1 ) :
                self.lampu1.change_to_green()

                self.lampu0.change_to_red()
                self.lampu2.change_to_red()
                self.lampu3.change_to_red()

            elif (int(self.app.time / divider) %4 == 2 ) :
                self.lampu2.change_to_green()

                self.lampu0.change_to_red()
                self.lampu1.change_to_red()
                self.lampu3.change_to_red()
            
            elif (int(self.app.time / divider) %4 == 3 ) :
                self.lampu3.change_to_green()

                self.lampu0.change_to_red()
                self.lampu1.change_to_red()
                self.lampu2.change_to_red()


        # ANIMASI MOBIL MOBIL (INI JUGA SAMA CONTOH)
        def animate_cars():
            for car in self.cars0:
                car.pos[0] += car.speed * self.app.delta_time / 1000
                car.update()
                
                if car.pos[0] < -2.5 and car not in self.antrian0:
                    self.antrian0.append(car)
                    print("mobil ", car.id," masuk antrian 0")
                    
                if car.pos[0] > -2.5 and car in self.antrian0:
                    self.antrian0.remove(car)
                    print("mobil ", car.id," dihapus dari antrian 0")
                    
                if car.pos[0] > 18:
                    car.pos[0] = -18
                

                
        animate_cars()
        animate_lights(5)
