import imgui
import pygame as pg
from imgui.integrations.opengl import ProgrammablePipelineRenderer


class GUI:
    def __init__(self, app):
        self.app = app
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
        self.app.ctx.viewport = (0, 0, *self.app.WIN_SIZE)

        io = imgui.get_io()
        io.display_size = self.app.WIN_SIZE

        imgui.new_frame()
        
        imgui.set_next_window_position(0, 0)
        imgui.set_next_window_size(300, 100)
        imgui.begin("SCENE PLAYER", flags=imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_COLLAPSE)
        
        button_text = "PAUSE" if self.app.playing else "PLAY"
        if imgui.button(button_text):
            self.app.toggle_play()
        
        imgui.same_line(spacing=10)
        
        if imgui.button("RESET"):
            self.app.reset()
            
        imgui.same_line(spacing=10)
            
        if imgui.button("RENDER"):
            self.app.toggle_render_view()

        imgui.same_line(spacing=10)
            
        if imgui.button("COLOR"):
            self.app.toggle_color()
        
        
        imgui.end()


        imgui.render()
        self.renderer.render(imgui.get_draw_data())
