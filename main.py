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

from physics import Physics

import imgui
from imgui.integrations.opengl import ProgrammablePipelineRenderer



# CLASS GRAPHIC ENGINE (MAIN CLASS)
class SxvxnEngine:
    def __init__(self, win_size=(1600, 900)):
        
        pg.init()
        pg.display.set_caption("Sxvxn Engine - Testing")
        pg.display.set_icon(pg.image.load('images/7-engine.png'))
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
        self.ticks = 100
        
        self.physics = Physics()

        self.shadow_res = 8192
        self.light = PointLight(position=(-10, 10, 10), color=(1, 1, 1),intensity=1.0, shadow_blur=4.5)
        self.camera = Camera(self)
        self.mesh = Mesh(self)
        self.scene = Scene(self)
        self.scene_renderer = SceneRenderer(self)
        self.background_color = (0.25, 0.35, 0.5)

        imgui.create_context()
        self.imgui_renderer = ProgrammablePipelineRenderer()
        imgui.get_io().ini_file_name = None

        


    # HANDLER INPUT USER ===================================================================================
    def check_events(self):
        
        io = imgui.get_io()
        io.mouse_down[0] = pg.mouse.get_pressed()[0]  # Left click
        io.mouse_down[1] = pg.mouse.get_pressed()[2]  # Right click
        io.mouse_down[2] = pg.mouse.get_pressed()[1]  # Middle click

        mouse_x, mouse_y = pg.mouse.get_pos()
        io.mouse_pos = mouse_x, mouse_y

        for event in pg.event.get():
            
            # ESCAPE -> QUIT
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                self.scene_renderer.destroy()
                self.physics.disconnect()
                pg.quit()
                sys.exit()
            
            # TAB -> GANTI MODE KAMERA
            if event.type == pg.KEYDOWN:
                s_time = pg.time.get_ticks()

                if event.key == pg.K_TAB:
                    self.camera.use_orbit = not self.camera.use_orbit
                    self.camera.set_default()


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
        self.ctx.clear(color=self.background_color)
        self.scene_renderer.render(lighting=1, skybox=1, post=1)

        # IMGUI RENDER
        io = imgui.get_io()
        io.display_size = self.WIN_SIZE
        self.ctx.viewport = (0, 0, *self.WIN_SIZE)

        imgui.new_frame()
        imgui.set_next_window_position(0, 0)
        imgui.set_next_window_size(300, 150)
        imgui.begin("DEBUG INFO")
        imgui.text("FPS: {:.2f}".format(self.clock.get_fps()))
        imgui.end()
        imgui.render()
        self.imgui_renderer.render(imgui.get_draw_data())
        
        # SWAP BUFFER
        pg.display.flip()




    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.scene.update()
            
            self.physics.stepSimulation()
            
            self.render()
            self.delta_time = self.clock.tick(self.ticks)
            imgui.get_io().delta_time = self.delta_time / 1000.0

if __name__ == '__main__':
    print("\033c")
    app = SxvxnEngine()
    app.run()
