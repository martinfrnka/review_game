import pygame

from script.helpers import load_assets, load_map
from script.tilemap import Tilemap
from script.camera import Camera2

class Editor:
    def __init__(self, width:int = 1280, height:int = 960, zoom = 2):
        pygame.init()
        self.screen_size = list((width, height))
        self.display_center = None
        pygame.display.set_caption('Review Editor' + str(self.screen_size))
        self.fullscreen = False
        self.timer = pygame.time.Clock()
        self.running = True

        self.camera_movement = [False, False, False, False]
        self.camera_desired_center_position = list((0,0))
        self.zoom_factor:float = zoom

        self.camera2:Camera2 = Camera2((self.screen_size), self.zoom_factor, 5)
        self.display = pygame.surface.Surface(self.camera2.get_display_size())

        self.screen = pygame.display.set_mode(self.screen_size, pygame.RESIZABLE)
        
        self.assets = load_assets()
        self.maps = load_map('0.json')
        
        self.change_resolution()
        self.tilemap = Tilemap(self.assets)
        
        print('Editor initialised!')
        
    def change_display_size(self):
        self.screen_size = self.screen.get_size()
        #camerazoom = self.camera.get_camera_zoom()
        self.display_center = ((self.screen_size[0]/2)/self.zoom_factor, (self.screen_size[1]/2)/self.zoom_factor)
        
        
        self.display = pygame.surface.Surface((int(self.screen_size[0]/self.zoom_factor), int(self.screen_size[1]/self.zoom_factor)))
        
        
        #self.camera = Camera2(self.camera_desired_center_position, self.display_center, self.zoom_factor)
        pygame.display.set_caption('Review Editor' + str(self.screen_size) +"; "+str(self.zoom_factor))
        
    def change_resolution(self):
        if self.fullscreen:
            print('go full')
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.screen_size)
        
        self.camera2.screen_size_changed((self.screen.get_width(), self.screen.get_height()))    

        self.change_display_size()

    def update_camera_desired_position(self, speed):
        self.camera_desired_center_position[0] += (self.camera_movement[3] - self.camera_movement[2])*speed
        self.camera_desired_center_position[1] += (self.camera_movement[1] - self.camera_movement[0])*speed



    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.timer.tick(60)
        
        pygame.quit()
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
            if event.type == pygame.VIDEORESIZE:
                self.change_resolution()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.camera_movement[0] = True
                if event.key == pygame.K_DOWN:
                    self.camera_movement[1] = True
                if event.key == pygame.K_LEFT:
                    self.camera_movement[2] = True
                if event.key == pygame.K_RIGHT:
                    self.camera_movement[3] = True
                if event.key == pygame.K_r:
                    self.screen_size = ((320,200))
                    self.change_resolution()
                if event.key == pygame.K_e:
                    self.screen_size = ((640, 480))
                    self.change_resolution()
                if event.key == pygame.K_f:
                    self.fullscreen = not self.fullscreen
                    self.change_resolution()
                if event.key == pygame.K_w:
                    self.zoom_factor +=1
                    if self.zoom_factor >10:
                        self.zoom_factor = 10
                    self.camera2.zoom_change(self.zoom_factor)
                if event.key == pygame.K_s:
                    self.zoom_factor -= 1
                    if self.zoom_factor <1:
                        self.zoom_factor = 1
                    self.camera2.zoom_change(self.zoom_factor)
                        
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.camera_movement[0] = False
                if event.key == pygame.K_DOWN:
                    self.camera_movement[1] = False
                if event.key == pygame.K_LEFT:
                    self.camera_movement[2] = False
                if event.key ==pygame.K_RIGHT:
                    self.camera_movement[3] = False
    
    def update(self):
        self.update_camera_desired_position(5)
        self.camera2.update(self.camera_movement, self.zoom_factor, 4)
        
        if self.display.get_size() != self.camera2.get_display_size():
            self.display = pygame.surface.Surface(self.camera2.get_display_size())
            
        
        self.tilemap.update()
    
    def draw(self):
        self.display.fill((0,200,200))
       
        self.tilemap.render(self.display, self.camera2.get_camera_offset())
                          
        self.screen.blit(pygame.transform.scale(self.display, (self.screen.width, self.screen.height)))
        pygame.display.flip()
        
    
Editor(800, 600, 2).run()