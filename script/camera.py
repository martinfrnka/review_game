import pygame

    
class Camera:
    def __init__(self, screen_size, camera_zoom_factor, camera_speed):
        self.zoom_factor = camera_zoom_factor
        self.current_zoom_factor = camera_zoom_factor
        self.camera_speed = camera_speed
        self.screen_size = list(screen_size)
        self.display_size = list((screen_size[0]/camera_zoom_factor, screen_size[1]/camera_zoom_factor))
        self.display_center = list((self.display_size[0]//2, self.display_size[1]//2))
        self.center_offset = list((0,0))
        self.desired_center_offset = list((0,0))
        
        print('Camera initialised (display size/center/offset, zoom_factor, speed): ', self.display_size, self.display_center, self.center_offset, self.camera_speed, self.zoom_factor)
    
    def get_display_size(self):
        return self.display_size
    
    def get_camera_offset(self):
        return (self.center_offset[0], self.center_offset[1])
    
    def get_camera_zoom_factor(self):
        return self.zoom_factor
    
    def get_camera_speed(self):
        return self.camera_speed
    
    def screen_size_changed(self, screen_size):
        self.screen_size = list(screen_size)
        old_display_size = self.display_size
        old_center_offset = self.center_offset
        old_desired_center_offset = self.desired_center_offset
        
        self.display_size = list((int(screen_size[0]/self.current_zoom_factor), int(screen_size[1]/self.current_zoom_factor)))
        self.display_center = list((int(self.display_size[0]/2), int(self.display_size[1]/2)))
   
        #ofset je potreba prepocitat ze stare velikosti na novou....
        x_factor:float = old_display_size[0]/self.display_size[0]
        y_factor:float = old_display_size[1]/self.display_size[1]
        self.center_offset[0] = int(old_center_offset[0]/x_factor)
        self.center_offset[1] = int(old_center_offset[1]/y_factor)

        #TODO: doplnit update desired center offsetu, aby se kamera posunula na stejné místo i při změně velikosti obrazovky (nejen zoomu)
        self.desired_center_offset[0] = int(old_desired_center_offset[0]/x_factor)
        self.desired_center_offset[1] = int(old_desired_center_offset[1]/y_factor)

        # print('Camera updated (display size/center/offset, zoom_factor, speed): ', self.display_size, self.display_center, self.center_offset, self.camera_speed, self.zoom_factor)
        
    # def zoom_change(self, zoom):
    #     self.zoom_factor = zoom
        
    def camera_zoom_up(self):
        self.zoom_factor += 1
        if self.zoom_factor >10:
            self.zoom_factor = 10
    
    def camera_zoom_down(self):
        self.zoom_factor -= 1
        if self.zoom_factor < 1:
            self.zoom_factor = 1
            
    def speed_up(self):
        self.camera_speed += 1
        if self.camera_speed > 20:
            self.camera_speed = 20
    
    def speed_down(self):
        self.camera_speed -= 1
        if self.camera_speed < 1:
            self.camera_speed = 1

    def update(self, movement):
        #TODO: podmínku vymyslet tak, aby se skončilo, když display bude změněn o 1px (něco jako target_size)
        if self.zoom_factor != self.current_zoom_factor:
            if abs(self.current_zoom_factor - self.zoom_factor) > 0.001:
                self.current_zoom_factor += (self.zoom_factor - self.current_zoom_factor)/30
            else:
                self.current_zoom_factor = self.zoom_factor
            self.screen_size_changed(self.screen_size)
        
        #kam se má kamera pohnout?
        self.desired_center_offset[0] += (movement[3] - movement[2]) * self.camera_speed*self.current_zoom_factor
        self.desired_center_offset[1] += (movement[1] - movement[0]) * self.camera_speed*self.current_zoom_factor

        self.center_offset[0] -= (self.center_offset[0] - self.desired_center_offset[0])/30
        self.center_offset[1] -= (self.center_offset[1] - self.desired_center_offset[1])/30
        
        
        # print ('currentZoom; zoom_factor ', self.current_zoom_factor, self.zoom_factor)