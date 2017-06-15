import pygame, sys
from pygame.locals import *
from common import DISPLAYSURF

gs = {'isJumping':'0','jumpHeight':'0','isMovingUp':'0','isMovingDown':'0','isMovingLeft':'0','isMovingRight':'0','char':'../assets/sprites/player/player.png', 'x':'0', 'y':'0' ,'z':'0', 'lvl':'../maps/c01a', 'realX':'300', 'realY':'300'}
pygame.font.init()
FONT = pygame.font.SysFont('Bauhaus 93 Regular', 40)


def getGamestate(): # Will be used for saving.
    return gs

def setGamestate(gsin): # Will be used for loading.
    gs = gsin

def start():
    facing = 'left'
    char = pygame.image.load(gs['char'])
    charflip = pygame.transform.flip(char, True, False)
    chardisplay = char
    lvl = pygame.image.load(gs['lvl'] + '/visual.png')
    charmask = pygame.mask.from_surface(char)
    lvlmask = pygame.mask.from_surface(pygame.image.load(gs['lvl'] + '/walls.png'))
    bullet = pygame.image.load('../assets/sprites/bullet/bullet.png')
    bx = 0
    by = 0
    bulletIsExisting = False
    hitbox = pygame.image.load('../assets/sprites/player/hitbox.png')
    hitmask = pygame.mask.from_surface(hitbox)
    while True: 
        DISPLAYSURF.blit(lvl, (0,0))
        DISPLAYSURF.blit(chardisplay,(int(gs['realX']),int(gs['realY'])))
        if bulletIsExisting:
            DISPLAYSURF.blit(bullet,(bx,by))
            if bulletFacing is 'left':
                bx = bx - 5
                by = by - 5
            if bulletFacing is 'right':
                bx = bx +5
                by = by +5
            if bulletFacing is 'up':
                bx = bx + 5
                by = by - 5
            if bulletFacing is 'down':
                bx = bx - 5
                by = by + 5
        for event in pygame.event.get():
            if event.type is QUIT:
               pygame.quit()
               sys.exit()
            if event.type is KEYDOWN and event.key is K_p:
                return 'PAUSE'
            
            if event.type is KEYDOWN and event.key is K_w:
                gs['isMovingUp'] = '1'
                facing = 'up'
            if event.type is KEYDOWN and event.key is K_a:
                gs['isMovingLeft'] = '1'
                chardisplay = char
                facing = 'left'
            if event.type is KEYDOWN and event.key is K_s:
                gs['isMovingDown'] = '1'
                facing = 'down'
            if event.type is KEYDOWN and event.key is K_d:
                gs['isMovingRight'] = '1'
                chardisplay = charflip
                facing = 'right'

            if event.type is KEYDOWN and event.key is K_q:
                gs['isJumping'] = '1'
                print("Jump!")
                
            if event.type is KEYUP and event.key is K_w:
                gs['isMovingUp'] = '0'
            if event.type is KEYUP and event.key is K_a:
                gs['isMovingLeft'] = '0'
            if event.type is KEYUP and event.key is K_s:
                gs['isMovingDown'] = '0'
            if event.type is KEYUP and event.key is K_d:
                gs['isMovingRight'] = '0'

            if event.type is KEYDOWN and event.key is K_e:
                bx = int(gs['realX'])+45
                by = int(gs['realY'])+25
                bulletIsExisting = True
                bulletFacing = facing

        if bool(int(gs['isMovingUp'])) and lvlmask.overlap_area(hitmask, (int(gs['realX'])+5, int(gs['realY'])-5)) is 0:
            gs['z'] = int ( gs['z'] ) - 5
            gs['realX'] = int(gs['realX']) + 5
            gs['realY'] = int(gs['realY']) - 5
        if bool(int(gs['isMovingLeft'])) and lvlmask.overlap_area(hitmask, (int(gs['realX'])-5, int(gs['realY'])-5)) is 0:
            gs['x'] = int ( gs['x'] ) - 5 
            gs['realX'] = int(gs['realX']) - 5
            gs['realY'] = int(gs['realY']) - 5
        if bool(int(gs['isMovingDown'])) and lvlmask.overlap_area(hitmask, (int(gs['realX'])-5, int(gs['realY'])+5)) is 0:
            gs['z'] = int ( gs['z'] ) + 5 
            gs['realX'] = int(gs['realX']) - 5
            gs['realY'] = int(gs['realY']) + 5
        if bool(int(gs['isMovingRight'])) and lvlmask.overlap_area(hitmask, (int(gs['realX'])+5, int(gs['realY'])+5)) is 0:
            gs['x'] = int ( gs['x'] ) + 5 
            gs['realX'] = int(gs['realX']) + 5
            gs['realY'] = int(gs['realY']) + 5

        if bool(int(gs['isJumping'])):
            print('Jumping!')
            if int(gs['jumpHeight']) is not 50:
                gs['y'] = str(int(gs['y']) + 5)
                gs['realY'] = str(int(gs['realY']) - 5)
                gs['jumpHeight'] = str(int(gs['jumpHeight']) + 5)
            if int(gs['jumpHeight']) is 50 and int(gs['y']) is not 0:
                gs['y'] = str(int(gs['y']) - 5)
                gs['realY'] = str(int(gs['realY']) + 5)
            if int(gs['jumpHeight']) is 50 and int(gs['y']) is 0:
                gs['jumpHeight'] = '0'
                gs['isJumping'] = '0'




    
            
        

        DISPLAYSURF.blit(FONT.render(str(gs['x']) + '_' + str(gs['z']), True, (0, 128, 255), (0, 0, 0)), (25,25))

        pygame.display.update()

     
            

    
    
    
