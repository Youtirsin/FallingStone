import pygame

class bullet(pygame.sprite.Sprite):
    def __init__(self,master):
        pygame.sprite.Sprite.__init__(self)
        words=pygame.font.SysFont('comicsansms',30).render('bullet',True,(0,0,0),(255,255,255)).convert_alpha()
        self.image=words
        self.rect=self.image.get_rect()
        self.rect.center=master.rect.center
        self.clock=pygame.time.get_ticks()
    def hit(self):
        self.kill()
    def update(self):
        if self.clock<pygame.time.get_ticks()-1:
            self.rect.top-=1
            self.clock=pygame.time.get_ticks()
        if self.rect.top<=0:
            self.kill()
