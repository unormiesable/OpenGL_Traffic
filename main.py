## IMPORT LIBRARY DAN MODULE
import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import Camera
from point_light import PointLight
from mesh import Mesh
from scene import Scene
from scene_renderer import SceneRenderer


# CLASS GRAPHIC ENGINE (MAIN CLASS)
class CGRAPHEngine:
    def __init__(self, win_size=(1280, 720)):
        
        pg.init()
        pg.display.set_caption("Grafika Komputer - Traffic Light Visualization (Alpha)")
        pg.display.set_icon(pg.image.load('images/traffic-light.png'))
        self.WIN_SIZE = win_size
        
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)

        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        self.ctx = mgl.create_context(require=330)
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0

        self.shadow_res = 8192
        
        self.light = PointLight(position=(-10, 10, 10), color=(1, 1, 1),intensity=1.0, shadow_blur=4.5)
        self.camera = Camera(self)
        self.mesh = Mesh(self)
        self.scene = Scene(self)
        self.scene_renderer = SceneRenderer(self)
        self.background_color = (0.25, 0.35, 0.5)


    # HANDLER INPUT USER ===================================================================================
    def check_events(self):
        for event in pg.event.get():
            
            # ESCAPE -> QUIT
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                self.scene_renderer.destroy()
                pg.quit()
                sys.exit()
            
            # TAB -> GANTI MODE KAMERA
            if event.type == pg.KEYDOWN:
                s_time = pg.time.get_ticks()

                if event.key == pg.K_TAB:
                    self.camera.use_orbit = not self.camera.use_orbit
                    self.camera.set_default()

                # SPAWNER MOBIL & REMOVE MOBIL (REMOVE BELUM)
                if s_time - self.scene.last_spawn_time >= self.scene.spawn_cooldown:
                    if event.key == pg.K_1:
                        if self.scene.cars0.__len__() > 6:
                            print("LANE 1 PENUH")
                        self.scene.spawn_car(0)
                        self.scene.last_spawn_time = s_time
                        
                    elif event.key == pg.K_2:
                        if self.scene.cars1.__len__() > 6:
                            print("LANE 2 PENUH")
                        self.scene.spawn_car(1)
                        self.scene.last_spawn_time = s_time
                        
                    elif event.key == pg.K_3:
                        if self.scene.cars0.__len__() > 6:
                            print("LANE 3 PENUH")
                        self.scene.spawn_car(2)
                        self.scene.last_spawn_time = s_time
                        
                    elif event.key == pg.K_4:
                        if self.scene.cars0.__len__() > 6:
                            print("LANE 4 PENUH")
                        self.scene.spawn_car(3)
                        self.scene.last_spawn_time = s_time
                        
                    elif event.key == pg.K_6:
                        self.scene.remove_car(0)
                        if self.scene.cars0.__len__() <= 4:
                            print("SETIAP LANE MINIMAL 4 MOBIL")
                    
                    elif event.key == pg.K_7:
                        self.scene.remove_car(1)
                        if self.scene.cars1.__len__() <= 4:
                            print("SETIAP LANE MINIMAL 4 MOBIL")
                    
                    elif event.key == pg.K_8:
                        self.scene.remove_car(2)
                        if self.scene.cars2.__len__() <= 4:
                            print("SETIAP LANE MINIMAL 4 MOBIL")
                    
                    elif event.key == pg.K_9:
                        self.scene.remove_car(3)
                        if self.scene.cars3.__len__() <= 4:
                            print("SETIAP LANE MINIMAL 4 MOBIL")
                    
                else:
                    # CUMA DEBUG 
                    print("HANYA DAPAT SPAWN/DESTROY MOBIL SETIAP ", self.scene.spawn_cooldown // 1000, " DETIK SEKALI")

            
            # ` -> TOGGLE MOUSE (KAYA DI GAME)
            if event.type == pg.KEYDOWN and event.key == pg.K_BACKQUOTE:
                is_visible = not pg.mouse.get_visible()
                pg.mouse.set_visible(is_visible)
                if is_visible:
                    pg.event.set_grab(False)
                else:
                    pg.event.set_grab(True)
                    
                    
            # SCROLL -> RADIUS ORBIT
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.camera.use_orbit:
                    
                    ## SCROLL ATAS 
                    if event.button == 4:
                        self.camera.orbit_radius -= 1
                        
                    ## SCROLL BAWAH
                    elif event.button == 5:
                        self.camera.orbit_radius += 1

                    # BATAS RADIUS
                    self.camera.orbit_radius = max(1.0, min(self.camera.orbit_radius, 100.0))
                
                
    # RENDER SCENE -> SCENE RENDERER
    def render(self):
        self.ctx.clear(color=(self.background_color))
        self.scene_renderer.render(lighting = 1, skybox = 1)
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(60)

if __name__ == '__main__':
    print("\033c")
    app = CGRAPHEngine()
    app.run()
