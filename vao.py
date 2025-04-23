from vbo import VBO
from shader_program import ShaderProgram

# CLASS VAO (SETUP UNTUK POINTER KE VBO DAN SHADER PROGRAM)
class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # OBJEK TANPA TEXTURE ========================================================================
        # COLOR CUBE VAO
        self.vaos['color_cube'] = self.get_vao(
            program=self.program.programs['default_color'],
            vbo = self.vbo.vbos['color_cube'])

        # COLOR CUBE SHADOW VAO
        self.vaos['shadow_color_cube'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['color_cube'])
        
        # COLOR PLANE VAO
        self.vaos['color_plane'] = self.get_vao(
            program=self.program.programs['default_color'],
            vbo = self.vbo.vbos['color_plane'])

        # COLOR PLANE SHADOW VAO
        self.vaos['shadow_color_plane'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['color_plane'])
        
        # COLOR CYLINDER VAO
        self.vaos['color_cylinder'] = self.get_vao(
            program=self.program.programs['default_color'],
            vbo = self.vbo.vbos['color_cylinder'])

        # COLOR CYLINDER SHADOW VAO
        self.vaos['shadow_color_cylinder'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['color_cylinder'])
        
        # COLOR CONE VAO
        self.vaos['color_cone'] = self.get_vao(
            program=self.program.programs['default_color'],
            vbo = self.vbo.vbos['color_cone'])

        # COLOR CONE SHADOW VAO
        self.vaos['shadow_color_cone'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['color_cone'])
        
        
        # OBJEK DENGAN TEXTURE ========================================================================
        # PLANE VAO
        self.vaos['plane'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['plane'])

        # PLANE SHADOW VAO
        self.vaos['shadow_plane'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['plane'])

        
        # CUBE VAO
        self.vaos['cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['cube'])

        # CUBE SHADOW VAO
        self.vaos['shadow_cube'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo = self.vbo.vbos['cube'])
        
        # GATE VAO
        self.vaos['gate'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['gate'])

        # GATE SHADOW VAO
        self.vaos['shadow_gate'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['gate'])
        
        # YELLOW CAR VAO
        self.vaos['yellow_car'] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['yellow_car'])

        # YELLOW CAR SHADOW VAO
        self.vaos['shadow_yellow_car'] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos['yellow_car'])
        
        # SKYBOX VAO
        self.vaos['skybox'] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo=self.vbo.vbos['skybox'])

        # ADV SKYBOX VAO
        self.vaos['skybox_next'] = self.get_vao(
            program=self.program.programs['skybox_next'],
            vbo=self.vbo.vbos['skybox_next'])


    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()