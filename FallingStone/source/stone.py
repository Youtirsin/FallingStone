import pygame
from random import randint

class stone(pygame.sprite.Sprite):
    def __init__(self,zone):
        pygame.sprite.Sprite.__init__(self)
        words=pygame.font.SysFont('comicsansms',30).render('stone',True,(0,0,0),(255,255,255)).convert_alpha()
        self.zone=zone
        self.image=words
        self.rect=self.image.get_rect()
        self.rect.top=0
        self.rect.left=randint(0,zone[0]-self.rect.width)
        self.clock=pygame.time.get_ticks()
    def update(self):
        if self.clock<pygame.time.get_ticks()-1:
            self.rect.top+=1
            self.clock=pygame.time.get_ticks()
        if self.rect.top>=self.zone[1]:
            self.rect.top=0
            self.rect.left=randint(0,self.zone[0]-self.rect.width)
            