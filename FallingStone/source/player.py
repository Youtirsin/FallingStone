import pygame

class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        words=pygame.font.SysFont('comicsansms',30).render('player',True,(0,0,0),(255,255,255)).convert_alpha()
        self.image=words
        self.rect=self.image.get_rect()
        self.rect.center=pygame.mouse.get_pos()
        self.deadFlag=False
    def relive(self):
        self.deadFlag=False
        words=pygame.font.SysFont('comicsansms',30).render('player',True,(0,0,0),(255,255,255)).convert_alpha()
        self.image=words
    def update(self):
        if self.deadFlag==False:
            self.rect.center=pygame.mouse.get_pos()
        if self.deadFlag:
            words=pygame.font.SysFont('comicsansms',30).render('Dead player',True,(0,0,0),(255,255,255)).convert_alpha()
            self.image=words

