import numpy as np
import moderngl as mgl
import pywavefront

# CLASS VBO (MENYIMPAN DATA VERTEX, INDEX, DAN ATRIBUT)
class VBO:
    def __init__(self, ctx):
        self.vbos = {}
        
        # OBJEK DENGAN TEXTURE
        self.vbos['cube'] = CubeVBO(ctx)
        self.vbos['plane'] = PlaneVBO(ctx)
        
        # OBJEK TANPA TEXTURE
        self.vbos['color_cube'] = ColorCubeVBO(ctx)
        self.vbos['color_plane'] = ColorPlaneVBO(ctx)
        self.vbos['color_cylinder'] = ColorCylinderVBO(ctx)
        self.vbos['color_cone'] = ColorConeVBO(ctx)
        
        # OBJEK DENGAN OBJ FILE
        self.vbos['gate'] = GateVBO(ctx)
        self.vbos['yellow_car'] = Yellow_CarVBO(ctx)
        
        # SKYBOX (TIDAK DIGUNAKAN UNTUK SAAT INI)
        self.vbos['skybox'] = SkyBoxVBO(ctx)
        self.vbos['skybox_next'] = NextSkyBoxVBO(ctx)

    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]


class BaseVBO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = self.get_vbo()
        self.format: str = None
        self.attribs: list = None

    def get_vertex_data(self):
        pass

    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    def destroy(self):
        self.vbo.release()


class PlaneVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        positions = [
            (-1, 0, -1), (1, 0, -1), (1, 0, 1), (-1, 0, 1)
        ]
        indices = [(0, 2, 1), (0, 3, 2)] 
        normals = [(0, 1, 0)] * 6 
        tex_coords = [(0, 0), (1, 0), (1, 1), (0, 1)]

        def get_data(verts, inds):
            return np.array([verts[i] for tri in inds for i in tri], dtype='f4')

        pos_data = get_data(positions, indices)
        norm_data = np.array(normals, dtype='f4')
        tex_data = get_data(tex_coords, indices)

        return np.hstack([tex_data, norm_data, pos_data])


class CubeVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vertex_data(self):
        vertices = [(-1, -1, 1), ( 1, -1,  1), (1,  1,  1), (-1, 1,  1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), ( 1, 1, -1)]

        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]
        vertex_data = self.get_data(vertices, indices)

        tex_coord_vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
        tex_coord_indices = [(0, 2, 3), (0, 1, 2),
                             (0, 2, 3), (0, 1, 2),
                             (0, 1, 2), (2, 3, 0),
                             (2, 3, 0), (2, 0, 1),
                             (0, 2, 3), (0, 1, 2),
                             (3, 1, 2), (3, 0, 1),]
        tex_coord_data = self.get_data(tex_coord_vertices, tex_coord_indices)

        normals = [( 0, 0, 1) * 6,
                   ( 1, 0, 0) * 6,
                   ( 0, 0,-1) * 6,
                   (-1, 0, 0) * 6,
                   ( 0, 1, 0) * 6,
                   ( 0,-1, 0) * 6,]
        normals = np.array(normals, dtype='f4').reshape(36, 3)

        vertex_data = np.hstack([normals, vertex_data])
        vertex_data = np.hstack([tex_coord_data, vertex_data])
        return vertex_data
    
    
class GateVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/gate/gate.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data

class Yellow_CarVBO(BaseVBO):
    def __init__(self, app):
        super().__init__(app)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    def get_vertex_data(self):
        objs = pywavefront.Wavefront('objects/yellow_car/yellow_car.obj', cache=True, parse=True)
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        vertex_data = np.array(vertex_data, dtype='f4')
        return vertex_data


class SkyBoxVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '3f'
        self.attribs = ['in_position']

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vertex_data(self):
        vertices = [(-1, -1, 1), ( 1, -1,  1), (1,  1,  1), (-1, 1,  1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), ( 1, 1, -1)]

        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]
        vertex_data = self.get_data(vertices, indices)
        vertex_data = np.flip(vertex_data, 1).copy(order='C')
        return vertex_data


class NextSkyBoxVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '3f'
        self.attribs = ['in_position']

    def get_vertex_data(self):
        z = 0.9999
        vertices = [(-1, -1, z), (3, -1, z), (-1, 3, z)]
        vertex_data = np.array(vertices, dtype='f4')
        return vertex_data


# COLOR CLASS (NO TEXTURE OBJECT)

class ColorPlaneVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '3f 3f'
        self.attribs = ['in_normal', 'in_position']

    def get_vertex_data(self):
        positions = [
            (-1, 0, -1), (1, 0, -1), (1, 0, 1), (-1, 0, 1)
        ]
        
        indices = [(0, 2, 1), (0, 3, 2)]
        normals = [(0, 1, 0)] * 6

        def get_data(verts, inds):
            return np.array([verts[i] for tri in inds for i in tri], dtype='f4')

        pos_data = get_data(positions, indices)
        norm_data = np.array(normals, dtype='f4')

        return np.hstack([norm_data, pos_data])


class ColorCubeVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '3f 3f'
        self.attribs = ['in_normal', 'in_position']

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vertex_data(self):
        vertices = [(-1, -1, 1), ( 1, -1,  1), (1,  1,  1), (-1, 1,  1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), ( 1, 1, -1)]

        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]

        vertex_data = self.get_data(vertices, indices)

        normals = [( 0, 0, 1)] * 6 +  \
                  [( 1, 0, 0)] * 6 +  \
                  [( 0, 0,-1)] * 6 +  \
                  [(-1, 0, 0)] * 6 +  \
                  [( 0, 1, 0)] * 6 +  \
                  [( 0,-1, 0)] * 6

        normals = np.array(normals, dtype='f4')

        vertex_data = vertex_data.reshape(-1, 3)
        vertex_data = np.hstack([normals, vertex_data])
        return vertex_data


class ColorConeVBO(BaseVBO):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '3f 3f'
        self.attribs = ['in_normal', 'in_position']

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vertex_data(self):
        height = 2.0
        radius = 1.0
        segments = 32
        
        steps = 2 * np.pi / segments
        base_center = (0, -height / 2, 0)
        apex = (0, height / 2, 0)

        vertices = [base_center]
        for i in range(segments):
            angle = i * steps
            x = radius * np.cos(angle)
            z = radius * np.sin(angle)
            vertices.append((x, -height / 2, z))
        vertices.append(apex)

        base_indices = [(0, i + 1, ((i + 1) % segments) + 1) for i in range(segments)]

        apex_index = len(vertices) - 1
        side_indices = [(apex_index, ((i + 1) % segments) + 1, i + 1) for i in range(segments)]

        indices = base_indices + side_indices
        vertex_data = self.get_data(vertices, indices)
        vertex_data = vertex_data.reshape(-1, 3)

        normals = []

        for x in range(len(base_indices) * 3):
            normals.append((0, -1, 0))

        for i in range(segments):
            p1 = np.array(vertices[i + 1])
            p2 = np.array(vertices[((i + 1) % segments) + 1])
            apex_pos = np.array(vertices[apex_index])
            edge1 = p1 - apex_pos
            edge2 = p2 - apex_pos
            normal = np.cross(edge1, edge2)
            normal = normal / np.linalg.norm(normal)
            for x in range(3):
                normals.append(tuple(normal))

        normals = np.array(normals, dtype='f4')

        vertex_data = np.hstack([normals, vertex_data])
        return vertex_data


class ColorCylinderVBO(BaseVBO):
    
    # REFS
    # https://www.songho.ca/opengl/gl_cylinder.html
    # https://community.khronos.org/t/creating-cylinder/57116
    
    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '3f 3f'
        self.attribs = ['in_normal', 'in_position']

    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    def get_vertex_data(self):
        # BELUM SIAP BUAT DIUBAH 
        height = 2.0
        radius = 1.0
        segments = 32

        steps = 2 * np.pi / segments

        tutup_bawah = (0, -height / 2, 0)
        tutup_atas = (0, height / 2, 0)

        vertices = [tutup_bawah, tutup_atas]

        vert_bawah = len(vertices)
        for i in range(segments):
            angle = i * steps
            x = radius * np.cos(angle)
            z = radius * np.sin(angle)
            vertices.append((x, -height / 2, z))

        vert_atas = len(vertices)
        for i in range(segments):
            angle = i * steps
            x = radius * np.cos(angle)
            z = radius * np.sin(angle)
            vertices.append((x, height / 2, z))

        bawah_tengah = 0
        atas_tengah = 1

        indices = []
        
        for i in range(segments):
            p1 = vert_bawah + i
            p2 = vert_bawah + (i + 1) % segments
            indices.append((bawah_tengah, p1, p2))

        for i in range(segments):
            p1 = vert_atas + i
            p2 = vert_atas + (i + 1) % segments
            indices.append((atas_tengah, p2, p1))
            
        for i in range(segments):
            bawah = vert_bawah + i
            bawah_next = vert_bawah + (i + 1) % segments
            atas = vert_atas + i
            atas_next = vert_atas + (i + 1) % segments
            
            # WAIT KEKNYA KEBALIK??? (FIXED)
            indices.append((bawah, atas_next, bawah_next))
            indices.append((bawah, atas, atas_next))

        vertex_data = self.get_data(vertices, indices)
        normals = []

        for tri_indices in indices:
            if tri_indices[0] == bawah_tengah:
                for _ in range(3):
                    normals.append((0, -1, 0))
            elif tri_indices[0] == atas_tengah:
                 for _ in range(3):
                     normals.append((0, 1, 0))
            else:
                for vert_id in tri_indices:
                    v = np.array(vertices[vert_id])
                    normal = np.array([v[0], 0.0, v[2]])                        
                    normals.append(tuple(normal))

        normals = np.array(normals, dtype='f4')
        vertex_data = np.hstack([normals, vertex_data])
        return vertex_data