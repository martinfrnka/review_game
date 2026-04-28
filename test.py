import pygame

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
changed = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                width -=20
                changed = True
            if event.key == pygame.K_RIGHT:
                width +=20
                changed = True
            if event.key == pygame.K_UP:
                height -=20
                changed = True
            if event.key == pygame.K_DOWN:
                height +=20
                changed = True
    if changed:
        screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        changed = False
    