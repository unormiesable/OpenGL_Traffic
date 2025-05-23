from vao import VAO
from texture import Texture

# MESH DENGAN VAO DAN TEXTURE UNTUK MENAMPILKAN OBJEK
class Mesh:
    def __init__(self, app):
        self.app = app
        self.vao = VAO(app.ctx)
        self.texture = Texture(app)

    def destroy(self):
        self.vao.destroy()
        self.texture.destroy()