import pygame

class Camera:
    def __init__(self, cam_pos, center_offset, initial_zoom):
        self.offset = list(cam_pos)
        self.center_offset = list(center_offset)
        self.zoom:float = initial_zoom
        
    def update(self, focus_entity_pos, zoom, speed):
        self.offset[0] -= (self.offset[0] - focus_entity_pos[0])*speed/30
        self.offset[1] -= (self.offset[1] - focus_entity_pos[1])*speed/30
        self.zoom += (self.zoom - zoom)*speed/3
        if self.zoom < 1:
            self.zoom = 1
        if self.zoom > 10:
            self.zoom = 10
        #print ('currentZoom ', self.zoom)
        
    def get_camera_offset(self):
        return (self.offset[0] - self.center_offset[0], self.offset[1] - self.center_offset[1])
    
    def get_camera_zoom(self):
        return self.zoom
    
    
class Camera2:
    def __init__(self, screen_size, camera_zoom_factor, camera_speed):
        self.zoom_factor = camera_zoom_factor
        self.current_zoom_factor = camera_zoom_factor
        self.speed = camera_speed
        self.screen_size = list(screen_size)
        self.display_size = list((screen_size[0]/camera_zoom_factor, screen_size[1]/camera_zoom_factor))
        self.display_center = list((self.display_size[0]//2, self.display_size[1]//2))
        self.center_offset = list((0,0))
        
        print('Camera2 initialised (display size/center/offset, zoom_factor, speed): ', self.display_size, self.display_center, self.center_offset, self.speed, self.zoom_factor)
    
    def get_display_size(self):
        return self.display_size
    
    def get_camera_offset(self):
        return (self.center_offset[0], self.center_offset[1])
    
    def get_camera_zoom_factor(self):
        return self.zoom_factor
    
    def screen_size_changed(self, screen_size):
        self.screen_size = list(screen_size)
        old_display_size = self.display_size
        old_display_center = self.display_center
        old_center_offset = self.center_offset
        self.display_size = list((int(screen_size[0]/self.current_zoom_factor), int(screen_size[1]/self.current_zoom_factor)))
        self.display_center = list((int(self.display_size[0]/2), int(self.display_size[1]/2)))
   
        #ofset je potreba prepocitat ze stare velikosti na novou....
        x_factor = old_display_size[0]/self.display_size[0]
        y_factor = old_display_size[1]/self.display_size[1]
        self.center_offset[0] = int(old_center_offset[0]/x_factor)
        self.center_offset[1] = int(old_center_offset[1]/y_factor)
        
        print('Camera2 updated (display size/center/offset, zoom_factor, speed): ', self.display_size, self.display_center, self.center_offset, self.speed, self.zoom_factor)
        
        

    def zoom_change(self, zoom):
        self.zoom_factor = zoom
    
    
    def update(self, movement, zoom, speed):
        self.center_offset[0] += (movement[3] - movement[2])*speed/30
        self.center_offset[1] += (movement[1] - movement[0])*speed/30
        
        #TODO: podmínku vymyslet tak, aby se skončilo, když display bude změněn o 1px (něco jako target_size)
        if self.zoom_factor != self.current_zoom_factor:
            if abs(self.current_zoom_factor - self.zoom_factor) > 0.001:
                self.current_zoom_factor += (self.zoom_factor - self.current_zoom_factor)/30
            else:
                self.current_zoom_factor = self.zoom_factor
            self.screen_size_changed(self.screen_size)
        
        print ('currentZoom; zoom_factor ', self.current_zoom_factor, self.zoom_factor)