# LOGIKA RENDERING YANG DIGUNAKAN
class SceneRenderer:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.mesh = app.mesh
        self.scene = app.scene
        
        self.depth_texture = self.mesh.texture.textures['depth_texture']
        self.depth_fbo = self.ctx.framebuffer(depth_attachment=self.depth_texture)

    def render_shadow(self):
        self.depth_fbo.clear()
        self.depth_fbo.use()
        for obj in self.scene.objects:
            obj.render_shadow()

    def main_render(self, skybox=False):
        self.app.ctx.screen.use()
        for obj in self.scene.objects:
            obj.render()
        
        if skybox:
            self.scene.skybox.render()

    def render(self, lighting=True, skybox=False):
        self.lighting = lighting
        
        if self.lighting:
            self.render_shadow()
        
        self.main_render(skybox=skybox)

    def destroy(self):
        self.depth_fbo.release()

