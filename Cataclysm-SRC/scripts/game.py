import pygame, sys
from pygame.locals import *
from common import DISPLAYSURF

gs = {'isJumping':False,'jumpHeight':0,'isMovingUp':False,'isMovingDown':False,'isMovingLeft':False,'isMovingRight':False,'char':'../assets/sprites/player/player.png', 'x':0, 'y':0 ,'z':0, 'lvl':'../maps/c01a', 'realX':300, 'realY':300}
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
        DISPLAYSURF.blit(chardisplay,(gs['realX'],gs['realY']))
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

            if event.type is KEYDOWN and event.key is K_ESCAPE:
                return 'PAUSE' 
            if event.type is KEYDOWN and event.key is K_w:
                gs['isMovingUp'] = True
                facing = 'up'
            if event.type is KEYDOWN and event.key is K_a:
                gs['isMovingLeft'] = True
                chardisplay = char
                facing = 'left'
            if event.type is KEYDOWN and event.key is K_s:
                gs['isMovingDown'] = True
                facing = 'down'
            if event.type is KEYDOWN and event.key is K_d:
                gs['isMovingRight'] = True
                chardisplay = charflip
                facing = 'right'
            if event.type is KEYDOWN and event.key is K_SPACE:
                gs['isJumping'] = True
                
            if event.type is KEYUP and event.key is K_w:
                gs['isMovingUp'] = False
            if event.type is KEYUP and event.key is K_a:
                gs['isMovingLeft'] = False
            if event.type is KEYUP and event.key is K_s:
                gs['isMovingDown'] = False
            if event.type is KEYUP and event.key is K_d:
                gs['isMovingRight'] = False

            if event.type is KEYDOWN and event.key is K_e:
                bx = gs['realX']+45
                by = gs['realY']+25
                bulletIsExisting = True
                bulletFacing = facing

        if gs['isMovingUp'] and lvlmask.overlap_area(hitmask, (gs['realX']+5, gs['realY']-5)) is 0:
            gs['z'] = gs['z'] - 5
            gs['realX'] = gs['realX'] + 5
            gs['realY'] = gs['realY'] - 5
        if gs['isMovingLeft'] and lvlmask.overlap_area(hitmask, (gs['realX']-5, gs['realY']-5)) is 0:
            gs['x'] = gs['x'] - 5 
            gs['realX'] = gs['realX'] - 5
            gs['realY'] = gs['realY'] - 5
        if gs['isMovingDown'] and lvlmask.overlap_area(hitmask, (gs['realX']-5, gs['realY']+5)) is 0:
            gs['z'] = gs['z'] + 5 
            gs['realX'] = gs['realX'] - 5
            gs['realY'] = gs['realY'] + 5
        if gs['isMovingRight'] and lvlmask.overlap_area(hitmask, (gs['realX']+5, gs['realY']+5)) is 0:
            gs['x'] = gs['x'] + 5 
            gs['realX'] = gs['realX'] + 5
            gs['realY'] = gs['realY'] + 5

        if gs['isJumping']:
            if gs['jumpHeight'] is not 50:
                gs['y'] = gs['y'] + 5
                gs['realY'] = gs['realY'] - 5
                gs['jumpHeight'] = gs['jumpHeight'] + 5
            if gs['jumpHeight'] is 50 and gs['y'] is not 0:
                gs['y'] = gs['y'] - 5
                gs['realY'] = gs['realY'] + 5
            if gs['jumpHeight'] is 50 and gs['y'] is 0:
                gs['jumpHeight'] = 0
                gs['isJumping'] = 0

        DISPLAYSURF.blit(FONT.render(str(gs['x']) + '_' + str(gs['z']), True, (0, 128, 255), (0, 0, 0)), (25,25))

        pygame.display.update()

     
            

    
    
    
