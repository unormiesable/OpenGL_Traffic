import pybullet as p
import pybullet_data

from pyglm import glm

class Physics:
    def __init__(self):
        self.client = p.connect(p.DIRECT)
        self.timestep = 60
        
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.81)
        p.setTimeStep(1/self.timestep)
        
    def add_physics_urdf(self, urdf, basepos=(0, 0, 0), baserot=(0, 0, 0), scale=1):
        return p.loadURDF(urdf, basePosition=(basepos[0], basepos[2], basepos[1]),
                          baseOrientation=p.getQuaternionFromEuler((baserot[0], baserot[2], baserot[1])),
                          globalScaling=scale * 2)
    
    def add_physics_geometry(self, geometry=p.GEOM_BOX ,half_extents=(0.5, 0.5, 0.5), pos=(0, 0, 0), rot=(0, 0, 0), mass=1, scale=(1, 1, 1)):
        collision_shape = p.createCollisionShape(geometry, halfExtents=half_extents, meshScale=(scale[0], scale[2], scale[1]))
        visual_shape = p.createVisualShape(geometry, halfExtents=half_extents, rgbaColor=[1, 0, 0, 1], meshScale=(scale[0], scale[2], scale[1]))
        
        orientation = p.getQuaternionFromEuler((rot[0], rot[2], rot[1]))
        body = p.createMultiBody(baseMass=mass,
                                baseCollisionShapeIndex=collision_shape,
                                baseVisualShapeIndex=visual_shape,
                                basePosition=(pos[0], pos[2], pos[1]),
                                baseOrientation=orientation)
        return body
    
    def get_pos(self, object):
        res = p.getBasePositionAndOrientation(object)
        pos = glm.vec3(res[0][0], res[0][2], -res[0][1])
        return pos
    
    def get_rot(self, physics_object):
        res = p.getBasePositionAndOrientation(physics_object)
        quat = res[1]
        glm_quat = glm.quat(quat[3], quat[0], quat[2], -quat[1])
        
        return glm_quat
    
    def get_status(self, object):
        rot = self.get_rot(object)
        pos = self.get_pos(object)
        return pos, rot
    
    def stepSimulation(self):
        p.stepSimulation()
        
    def disconnect(self):
        p.disconnect()