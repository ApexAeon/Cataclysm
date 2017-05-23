import pygame, sys
from pygame.locals import *
from common import DISPLAYSURF

gs = {'isMovingUp':'0','isMovingDown':'0','isMovingLeft':'0','isMovingRight':'0','char':'..\\assets\\sprites\\player\\player.png', 'x':'0', 'z':'0', 'lvl':'..\\maps\\c01a\\1.png', 'realX':'0', 'realY':'0'}
realX = 0
realY = 0

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
    char = pygame.image.load(gs['char'])
    charflip = pygame.transform.flip(char, True, False)
    chardisplay = char
    lvl = pygame.image.load(gs['lvl'])
    while True: 
        DISPLAYSURF.blit(lvl, (0,0))
        DISPLAYSURF.blit(chardisplay,(int(gs['realX']),int(gs['realY'])))
        for event in pygame.event.get():
            if event.type is QUIT:
               pygame.quit()
               sys.exit()
            if event.type is KEYDOWN and event.key is K_p:
                return 'PAUSE'
            
            if event.type is KEYDOWN and event.key is K_w:
                gs['isMovingUp'] = '1'
            if event.type is KEYDOWN and event.key is K_a:
                gs['isMovingLeft'] = '1'
                chardisplay = char
            if event.type is KEYDOWN and event.key is K_s:
                gs['isMovingDown'] = '1'
                
            if event.type is KEYDOWN and event.key is K_d:
                gs['isMovingRight'] = '1'
                chardisplay = charflip
                
            if event.type is KEYUP and event.key is K_w:
                gs['isMovingUp'] = '0'
            if event.type is KEYUP and event.key is K_a:
                gs['isMovingLeft'] = '0'
            if event.type is KEYUP and event.key is K_s:
                gs['isMovingDown'] = '0'
            if event.type is KEYUP and event.key is K_d:
                gs['isMovingRight'] = '0'
                
        if bool(int(gs['isMovingUp'])):
            gs['z'] = int ( gs['z'] ) - 5
            gs['realX'] = int(gs['realX']) + 5
            gs['realY'] = int(gs['realY']) - 5
        if bool(int(gs['isMovingLeft'])):
            gs['x'] = int ( gs['x'] ) - 5 
            gs['realX'] = int(gs['realX']) - 5
            gs['realY'] = int(gs['realY']) - 5
        if bool(int(gs['isMovingDown'])):
            gs['z'] = int ( gs['z'] ) + 5 
            gs['realX'] = int(gs['realX']) - 5
            gs['realY'] = int(gs['realY']) + 5
        if bool(int(gs['isMovingRight'])):
            gs['x'] = int ( gs['x'] ) + 5 
            gs['realX'] = int(gs['realX']) + 5
            gs['realY'] = int(gs['realY']) + 5
        
                
        pygame.display.update()

     
            

    
    
    
