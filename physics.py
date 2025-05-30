import pybullet as p
import pybullet_data

from pyglm import glm

class Physics:
    def __init__(self):
        self.client = p.connect(p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.81)
        
    def add_physics(self, urdf, basepos, baserot, scale=2):
        return p.loadURDF(urdf, basePosition=(basepos[0], basepos[2], basepos[1]),
                          baseOrientation=p.getQuaternionFromEuler(baserot),
                          globalScaling=scale)
    
    def get_pos(self, object):
        res = p.getBasePositionAndOrientation(object)
        pos = glm.vec3(res[0][0], res[0][2], res[0][1])
        return pos
    
    def get_rot(self, object):
        res = p.getBasePositionAndOrientation(object)
        rot = glm.vec3(res[1][0], res[1][2], res[1][1])
        return rot
    
    def get_status(self, object):
        res = p.getBasePositionAndOrientation(object)
        pos = glm.vec3(res[0][0], res[0][2], res[0][1])
        rot = glm.vec3(res[1][0], res[1][2], res[1][1])
        return pos, rot
    
    def stepSimulation(self):
        p.stepSimulation()
        
    def disconnect(self):
        p.disconnect()