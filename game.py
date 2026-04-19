import pygame
from script.helpers import load_image, load_images, load_assets
from script.entities import Player
from script.tilemap import Tilemap
from script.camera import Camera
class Game:
    def __init__(self, width:int = 1280, height:int = 960, zoom = 2):
        pygame.init()
        self.screen_size = list((width, height))
        self.zoom_factor = zoom
        self.display_center = None
        pygame.display.set_caption('Review game')
        self.display:pygame.display.Surface = None
        self.fullscreen = False
        self.timer = pygame.time.Clock()
        self.running = True

        self.camera:Camera = None

        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        
        self.assets = load_assets()
        
        self.player = Player(self.assets['player'], (105,55), 3)

        self.change_resolution((width, height))
        self.tilemap = Tilemap(self.assets)
        print('Game initialised!')
        
    def change_display_size(self):
        self.screen_size = self.screen.get_size()
        self.display_center = ((self.screen_size[0]/2)/self.zoom_factor, (self.screen_size[1]/2)/self.zoom_factor)
        
        self.display = pygame.surface.Surface((int(self.screen_size[0]//self.zoom_factor), int(self.screen_size[1]/self.zoom_factor)))
        
        self.camera = Camera(self.player.get_center_pos(), self.display_center)
        
    def change_resolution(self, size):
        if not size:
            print('go full')
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(size, pygame.RESIZABLE)

        self.change_display_size()

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
                self.change_resolution((event.w, event.h))
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.movement[0] = True
                if event.key == pygame.K_DOWN:
                    self.player.movement[1] = True
                if event.key == pygame.K_LEFT:
                    self.player.movement[2] = True
                if event.key == pygame.K_RIGHT:
                    self.player.movement[3] = True
                if event.key == pygame.K_r:
                    self.change_resolution((320,240))
                if event.key == pygame.K_e:
                    self.change_resolution((640,480))
                if event.key == pygame.K_f:
                    self.fullscreen = not self.fullscreen
                    if self.fullscreen:
                        self.change_resolution(None)
                    else:
                        self.change_resolution((800,600))
                if event.key == pygame.K_w:
                    self.zoom_factor +=1
                    if self.zoom_factor >10:
                        self.zoom_factor = 10
                    self.change_display_size()
                if event.key == pygame.K_s:
                    self.zoom_factor -= 1
                    if self.zoom_factor <1:
                        self.zoom_factor = 1
                    self.change_display_size()
                        
                if event.key == pygame.K_SPACE:
                    self.player.jump = True
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.player.movement[0] = False
                if event.key == pygame.K_DOWN:
                    self.player.movement[1] = False
                if event.key == pygame.K_LEFT:
                    self.player.movement[2] = False
                if event.key == pygame.K_RIGHT:
                    self.player.movement[3] = False
    
    def update(self):
        self.player.update()
        self.camera.update(self.player.get_center_pos())
       
        self.tilemap.update()
    
    def draw(self):
        self.display.fill((0,200,200))
       
        self.tilemap.render(self.display, self.camera.get_camera_offset())
       
        self.player.render(self.display, self.camera.get_camera_offset())
                    
        self.screen.blit(pygame.transform.scale(self.display, (self.screen.width, self.screen.height)))
        pygame.display.flip()
        
    def resize():
        pass
    
Game(800, 600, 6).run()