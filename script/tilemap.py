import pygame

class Tilemap:
    def __init__(self, assets):
        self.assets = assets    
    
    def update(self):
        pass
    
    def render(self, surface, offset):
        surface.fill((255,0,0), (80-offset[0],80-offset[1],10,10))
        
        x = 50
        for item in self.assets:
            y = 50
            if item == 'player':
                surface.blit(self.assets[item],(y-offset[0],x-offset[1]))
            else:
                for image in self.assets[item]:
                    surface.blit(self.assets[item][image], (y-offset[0],x-offset[1]))
                    y += 50
            x += 50
