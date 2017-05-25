import pygame, sys
from pygame.locals import *
from common import DISPLAYSURF

gs = {'isMovingUp':'0','isMovingDown':'0','isMovingLeft':'0','isMovingRight':'0','char':'../assets/sprites/player/player.png', 'x':'0', 'z':'0', 'lvl':'../maps/c01a', 'realX':'300', 'realY':'300'}


'''
class IsoSprite(pygame.sprite.Sprite):
    def __init__(self, cont, img):
        self.controller = cont
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
    def setPos(pos, key)
        if key is self.controller:
            self.x = pos[0]
            self.y = pos[1]

class Player():
    def __init__(self, sprite, name)
    def move():
        if gs['isMovingUp'] is '1':

        if gs['isMovingLeft'] is '1':

        if gs['isMovingDown'] is '1':

        if gs['isMovingRight'] is '1':
            
class RemotePlayer():

class AI():
'''

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

            
                
                
        if bool(int(gs['isMovingUp'])) and lvlmask.overlap_area(charmask, (int(gs['realX'])+5, int(gs['realY'])-5)) is 0:
            gs['z'] = int ( gs['z'] ) - 5
            gs['realX'] = int(gs['realX']) + 5
            gs['realY'] = int(gs['realY']) - 5
        if bool(int(gs['isMovingLeft'])) and lvlmask.overlap_area(charmask, (int(gs['realX'])-5, int(gs['realY'])-5)) is 0:
            gs['x'] = int ( gs['x'] ) - 5 
            gs['realX'] = int(gs['realX']) - 5
            gs['realY'] = int(gs['realY']) - 5
        if bool(int(gs['isMovingDown'])) and lvlmask.overlap_area(charmask, (int(gs['realX'])-5, int(gs['realY'])+5)) is 0:
            gs['z'] = int ( gs['z'] ) + 5 
            gs['realX'] = int(gs['realX']) - 5
            gs['realY'] = int(gs['realY']) + 5
        if bool(int(gs['isMovingRight'])) and lvlmask.overlap_area(charmask, (int(gs['realX'])+5, int(gs['realY'])+5)) is 0:
            gs['x'] = int ( gs['x'] ) + 5 
            gs['realX'] = int(gs['realX']) + 5
            gs['realY'] = int(gs['realY']) + 5

        '''
        if lvlmask.overlap_area(charmask, (int(gs['realX']), int(gs['realY']))) is not 0:
            gs['realX'] = 300
            gs['realY'] = 300
            gs['x'] = 0
            gs['z'] = 0
        '''   
        
                
        pygame.display.update()

     
            

    
    
    
