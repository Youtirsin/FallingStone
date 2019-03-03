import pygame

class record(pygame.sprite.Sprite):
    def __init__(self,be4Str,count,position):
        pygame.sprite.Sprite.__init__(self)
        self.count=count
        self.be4Str=be4Str
        self.msg=str(self.count)
        self.image=pygame.font.SysFont('comicsansms',30).render(self.be4Str+self.msg,True,(0,0,0),(255,255,255)).convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.left=position[0]
        self.rect.top=position[1]
    def update(self):
        if self.msg!=str(self.count):
            self.msg=str(self.count)
            self.image=pygame.font.SysFont('comicsansms',30).render(self.be4Str+self.msg,True,(0,0,0),(255,255,255)).convert_alpha()
            self.rect.width=self.image.get_rect().width