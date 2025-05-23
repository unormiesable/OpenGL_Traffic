# JEMBATAN PROGRAM UTAMA DENGAN PROGRAM SHADERS
class ShaderProgram:
    def __init__(self, ctx):
        self.ctx = ctx
        self.programs = {}
        
        self.programs['default_color'] = self.get_program('default_color')
        self.programs['rough_color'] = self.get_program('rough_color')

        self.programs['default_texture'] = self.get_program('default_texture')
        
        self.programs['skybox'] = self.get_program('skybox')
        self.programs['skybox_next'] = self.get_program('skybox_next')
        self.programs['shadow_map'] = self.get_program('shadow_map')

    # SETUP BUAT BACA SHADER (.frag, .vert)
    def get_program(self, shader_program_name):
        with open(f'shaders/{shader_program_name}.vert') as file:
            vertex_shader = file.read()

        with open(f'shaders/{shader_program_name}.frag') as file:
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program

    def destroy(self):
        [program.release() for program in self.programs.values()]
