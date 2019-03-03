import pygame
from random import randint
from source.player import player
from source.bullet import bullet
from source.stone import stone
from source.record import record

screenWidth,screenHeight=700,700
pygame.init()
screen=pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('Falling Stone')

def UI():
    background=pygame.Surface(screen.get_size()).convert()
    background.fill(pygame.color.Color('white'))
    screen.blit(background,(0,0))
    words='press any key or mousekey to start,shoot or relive.'
    screen.blit(pygame.font.SysFont('comicsansms',30).render(words,True,(0,0,0),(255,255,255)).convert_alpha(),(0,screenHeight/2))
        
    while True:
        event=pygame.event.poll()
        if event.type==pygame.KEYDOWN or event.type==pygame.MOUSEBUTTONDOWN:
            return True
        pygame.display.update()
def gaming():
    background=pygame.Surface(screen.get_size()).convert()
    background.fill(pygame.color.Color('black'))
    screen.blit(background,(0,0))

    hW=player()
    hWGroup=pygame.sprite.Group(hW)

    bulletGroup=pygame.sprite.Group()
    bulletCount=record('bullet:',0,(0,0))
    bulletTick=0

    stGroup=pygame.sprite.Group(stone((screenWidth,screenHeight)))
    stoneCount=record('level:',1,(600,0))
    stoneCount.rect.left=screenWidth-stoneCount.rect.width
    stoneTick=0

    recordGroup=pygame.sprite.Group(bulletCount,stoneCount)
    
    while True:
        #ticks initialize
        if stoneTick==0:
            stoneTick=pygame.time.get_ticks()
        if bulletTick==0:
            bulletTick=pygame.time.get_ticks()

        #event handlers
        event=pygame.event.poll()
        if event.type==pygame.QUIT:
            pygame.quit()
        elif event.type==pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
            #gameStart=True
            if hW.deadFlag:
                stoneCount.count-=1
                hW.relive()
            else:
                if bulletCount.count>0:
                    bulletGroup.add(bullet(hW))
                    bulletCount.count-=1

        #collision check
        if pygame.sprite.spritecollide(hW,stGroup,True):
            hW.deadFlag=True
        for bu in bulletGroup.sprites():
            if pygame.sprite.spritecollide(bu,stGroup,True):
                bu.kill()
                stoneCount.count-=1
                    
        if hW.deadFlag==False:
            hWGroup.clear(screen,background)
            bulletGroup.clear(screen,background)
            stGroup.clear(screen,background)
            recordGroup.clear(screen,background)

            hWGroup.update()
            bulletGroup.update()
            stGroup.update()
            recordGroup.update()

            #ticks
            if stoneTick<=pygame.time.get_ticks()-5000:
                stGroup.add(stone((screenWidth,screenHeight)))
                stoneCount.count+=1
                stoneTick=pygame.time.get_ticks()
            if bulletTick<=pygame.time.get_ticks()-20000:
                bulletCount.count+=1
                bulletTick=pygame.time.get_ticks()

            stoneCount.rect.left=screenWidth-stoneCount.rect.width

            hWGroup.draw(screen)
            bulletGroup.draw(screen)
            stGroup.draw(screen)
            recordGroup.draw(screen)
        else:
            hWGroup.clear(screen,background)
            hWGroup.update()
            hWGroup.draw(screen)

                
        pygame.display.update()


if __name__=='__main__':
    if UI():
        gaming()