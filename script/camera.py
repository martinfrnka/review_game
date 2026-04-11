
class Camera:
    def __init__(self, cam_pos, center_offset):
        self.offset = list(cam_pos)
        self.center_offset = list(center_offset)
        
    def update(self, focus_entity_pos = (0,0)):
        self.offset[0] -= (self.offset[0] - focus_entity_pos[0])/30
        self.offset[1] -= (self.offset[1] - focus_entity_pos[1])/30
        
    def get_camera_offset(self):
        return (self.offset[0] - self.center_offset[0], self.offset[1] - self.center_offset[1])
    
    