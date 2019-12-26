import sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,480))
screen_height = screen.get_height()
screen_width = screen.get_width()
clock = pygame.time.Clock()

class Mover(pygame.sprite.Sprite):
    def __init__(self):
        super(Mover, self).__init__()
        self.surf = pygame.Surface((50,50))
        self.surf.fill((0,255,0))
        self.rect = self.surf.get_rect()
        self.g = (0,1)
        self.speed = [2,0]
    def update(self):
        if self.rect.bottom >= screen_height:
            self.speed[1] = -abs(self.speed[1])
        else:
            for k in {0,1}: self.speed[k] += self.g[k]
        if self.rect.left < 0:
            self.speed[0] = abs(self.speed[0])
        elif self.rect.right > screen_width:
            self.speed[0] = -abs(self.speed[0])

        self.rect.move_ip(self.speed)

surf = pygame.Surface((50,50))
surf.fill((255,0,0))
mover1 = Mover()



running = True
while running:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            running = False
    clock.tick(60)
    screen.fill((0,0,0))
    screen.blit(surf,(100,100))
    mover1.update()
    screen.blit(mover1.surf, mover1.rect)
    pygame.display.flip()
pygame.quit()


