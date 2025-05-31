import pybullet as p
import pybullet_data

from pyglm import glm

class Physics:
    def __init__(self):
        self.client = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.81 * 10)
        
    def add_physics(self, urdf, basepos=(0, 0, 0), baserot=(0, 0, 0), scale=1):
        return p.loadURDF(urdf, basePosition=(basepos[0], basepos[2], basepos[1]),
                          baseOrientation=p.getQuaternionFromEuler((baserot[0], baserot[2], baserot[1])),
                          globalScaling=scale * 2)
    
    def get_pos(self, object):
        res = p.getBasePositionAndOrientation(object)
        pos = glm.vec3(res[0][0], res[0][2], -res[0][1])
        return pos
    
    def get_rot(self, physics_object):
        res = p.getBasePositionAndOrientation(physics_object)
        rot = p.getEulerFromQuaternion(res[1])
        fixed_rot = glm.vec3(rot[0], rot[2], -rot[1])
        
        return fixed_rot
    
    def get_status(self, object):
        rot = self.get_rot(object)
        pos = self.get_pos(object)
        return pos, rot
    
    def stepSimulation(self):
        p.stepSimulation()
        
    def disconnect(self):
        p.disconnect()