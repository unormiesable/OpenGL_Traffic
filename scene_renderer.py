import moderngl as mgl

# LOGIKA RENDERING YANG DIGUNAKAN
class SceneRenderer:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.mesh = app.mesh
        self.scene = app.scene
        
        self.depth_texture = self.mesh.texture.textures['depth_texture']
        self.depth_fbo = self.ctx.framebuffer(depth_attachment=self.depth_texture)
        
        self.create_post_fbo()

    def render_shadow(self):
        self.depth_fbo.clear()
        self.depth_fbo.use()
        for obj in self.scene.objects:
            obj.render_shadow()

    def main_render(self, skybox=False):
        self.ctx.clear(1.0, 0.0, 1.0)
        for obj in self.scene.objects:
            obj.render()
        if skybox:
            self.scene.skybox.render()


    def create_post_fbo(self):
        w, h = self.app.WIN_SIZE
        self.post_texture = self.ctx.texture((w, h), 4)
        self.post_depth = self.ctx.depth_renderbuffer((w, h))
        self.post_fbo = self.ctx.framebuffer(color_attachments=[self.post_texture], depth_attachment=self.post_depth)
        
        
    def post_process(self):
        self.app.ctx.screen.use()
        self.ctx.viewport = (0, 0, self.app.WIN_SIZE[0]*2, self.app.WIN_SIZE[1]*2)
        self.post_texture.use(location=0)
        self.app.mesh.vao.vaos['fullscreen_quad'].render(mgl.TRIANGLE_STRIP)


    def render(self, lighting=True, skybox=False):
        self.lighting = lighting

        if self.lighting:
            self.render_shadow()

        self.post_fbo.use()

        self.main_render(skybox=skybox)
        self.scene.update()

        self.post_process()



    def destroy(self):
        self.depth_fbo.release()

