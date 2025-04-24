import pygame as pg
import moderngl as mgl
import glm

# TEXTURE YANG AKAN DIGUNAKAN PADA OBJEK
class Texture:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.textures = {}
        
        # TEXTURE ID (PADA PROJECT INI DINAMAI 'tex_id')
            
        self.textures[0] = self.get_texture(path='textures/crate.png')
        self.textures['white'] = self.get_texture(path='objects/gate/gate.jpg')
        self.textures['yellow_car'] = self.get_texture(path='objects/yellow_car/yellow_car.jpg')
        self.textures['skybox'] = self.get_texture_cube(dir_path='textures/skybox/', ext='png')
        self.textures['depth_texture'] = self.get_depth_texture()
    
    # DEPTH TEXTURE UNTUK BAYANGAN (KONTROL SHADOW MAP)
    def get_depth_texture(self):
        shadow_res = 4096
        depth_texture = self.ctx.depth_texture((shadow_res, shadow_res))
        depth_texture.repeat_x = False
        depth_texture.repeat_y = False
        return depth_texture

    # TEXTURE CUBE (DIGUNAKAN PADA CUBE DAN SKYBOX)
    def get_texture_cube(self, dir_path, ext='png'):
        faces = ['right', 'left', 'top', 'bottom'] + ['front', 'back'][::-1]

        textures = []
        for face in faces:
            texture = pg.image.load(dir_path + f'{face}.{ext}').convert()
            if face in ['right', 'left', 'front', 'back']:
                texture = pg.transform.flip(texture, flip_x=True, flip_y=False)
            else:
                texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
            textures.append(texture)

        size = textures[1].get_size()
        texture_cube = self.ctx.texture_cube(size=size, components=3, data=None)

        for i in range(6):
            texture_data = pg.image.tostring(textures[i], 'RGB')
            texture_cube.write(face=i, data=texture_data)

        return texture_cube

    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
    
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        texture.anisotropy = 16.0
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]