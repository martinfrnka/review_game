import pygame

class PhysicsEntity:
    def __init__(self, image, position):
        self.pos = list(position)
        self.image = image
        self.movement = list([False, False, False, False])
        
    def update(self):
        pass
    
    def render(self, display, offset):
        #display.blit(self.image, (self.pos[0]-offset[0]+display.width//2, self.pos[1]-offset[1]+display.height//2))
        #display.blit(self.image, (display.width//2, display.height//2))
        display.blit(self.image, (self.pos[0]-offset[0], self.pos[1]-offset[1]))
        
    def get_pos(self):
        return (self.pos[0], self.pos[1])
        
        
class Player(PhysicsEntity):
    def __init__(self, image, position=(0, 0), speed=1):
        super().__init__(image, position)
        self.speed = speed
        self.jump = False
        
    def update(self):
        if self.jump:
            self.pos[1] -= 30
            self.jump = False
            
        self.pos[0] +=self.speed*(int(self.movement[3]-self.movement[2]))
        self.pos[1] +=self.speed*(int(self.movement[1]-self.movement[0]))

