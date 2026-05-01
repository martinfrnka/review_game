import pygame

from script.helpers import load_assets, load_map
from script.tilemap import Tilemap
from script.camera import Camera

class Editor:
    def __init__(self, width:int = 1280, height:int = 960, zoom = 2):
        self.current_tile = 0
        self.current_variant = 0
        
        pygame.init()
        self.screen_size = list((width, height))
        self.display_center = None
        pygame.display.set_caption('Review Editor' + str(self.screen_size))
        self.fullscreen = False
        self.timer = pygame.time.Clock()
        self.running = True

        self.camera_movement = [False, False, False, False]

        self.camera:Camera = Camera((self.screen_size), zoom, 2)
        self.display = pygame.surface.Surface(self.camera.get_display_size())

        self.screen: pygame.Surface = None        
        self.change_resolution()

        self.assets = load_assets()
        self.maps = load_map('0.json')        

        self.tilemap = Tilemap(self.assets)
        
        print('Editor initialised!')
                
    def change_resolution(self):
        if self.fullscreen:
            print('go full')
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.screen_size)
        
        self.camera.screen_size_changed((self.screen.get_width(), self.screen.get_height()))    
        pygame.display.set_caption('Review Editor' + str(self.screen_size) +"; "+str(self.camera.zoom_factor))

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.timer.tick(60)
        
        pygame.quit()
        
    def handle_events(self):
        for event in pygame.event.get():
            #quit when ESC is pressed or window is closed
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
            if event.type == pygame.VIDEORESIZE:
                self.change_resolution()
            
            #key is pressed
            if event.type == pygame.KEYDOWN:
                #movement of camera, arrows
                if event.key == pygame.K_UP:
                    self.camera_movement[0] = True
                if event.key == pygame.K_DOWN:
                    self.camera_movement[1] = True
                if event.key == pygame.K_LEFT:
                    self.camera_movement[2] = True
                if event.key == pygame.K_RIGHT:
                    self.camera_movement[3] = True
                
                #r,e,f - resolution change, w,s - zoom, q,a - speed of camera
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
                    self.camera.camera_zoom_up()
                if event.key == pygame.K_s:
                    self.camera.camera_zoom_down()
                if event.key == pygame.K_q:
                    self.camera.speed_up()
                if event.key == pygame.K_a:
                    self.camera.speed_down()
                        
            #release of keys
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
        
        self.camera.update(self.camera_movement)
        
        if self.display.get_size() != self.camera.get_display_size():
            self.display = pygame.surface.Surface(self.camera.get_display_size())
        
        self.tilemap.update()
    
    def draw(self):
        self.display.fill((0,200,200))
       
        self.tilemap.render(self.display, self.camera.get_camera_offset())
                          
        self.screen.blit(pygame.transform.scale(self.display, (self.screen.width, self.screen.height)))
        pygame.display.flip()
        
    
Editor(800, 600).run()