import imgui
import pygame as pg
from imgui.integrations.opengl import ProgrammablePipelineRenderer


class UI:
    def __init__(self, engine):
        self.engine = engine
        imgui.create_context()
        self.renderer = ProgrammablePipelineRenderer()
        imgui.get_io().ini_file_name = None 

    def process_input(self):
        io = imgui.get_io()
        io.mouse_down[0] = pg.mouse.get_pressed()[0]
        io.mouse_down[1] = pg.mouse.get_pressed()[2]
        io.mouse_down[2] = pg.mouse.get_pressed()[1]
        io.mouse_pos = pg.mouse.get_pos()

    def render(self):
        self.engine.ctx.viewport = (0, 0, *self.engine.WIN_SIZE)

        io = imgui.get_io()
        io.display_size = self.engine.WIN_SIZE

        imgui.new_frame()
        imgui.set_next_window_position(0, 0)
        imgui.set_next_window_size(300, 150)
        imgui.begin("GUI TESTING")
        imgui.text("HELLO WORLD")
        imgui.text("FPS: {:.2f}".format(self.engine.clock.get_fps()))
        imgui.end()
        

        imgui.render()
        self.renderer.render(imgui.get_draw_data())
