import pygame, sys
from pygame.locals import *
from common import DISPLAYSURF
from common import FONT
import json
import time
import math

gs = {
    'isJumping':False,
    'jumpHeight':0,
    'isMovingUp':False,
    'isMovingDown':False,
    'isMovingLeft':False,
    'isMovingRight':False,
    'char':'../assets/sprites/player/player.png',
    'x':96,
    'y':0 ,
    'z':65,
    'lvl':'c01a',
    'realX':0,
    'realY':0,
    'facing':'left',
    'speed':1,
    'isAlive':True
}

def tickDoor(obj): # For every door object in a level, this will run, with the specified parameters of each specific door.
    if gs['x'] >= obj['posdict']['x'] and gs['y'] >= obj['posdict']['y'] and gs['z'] >= obj['posdict']['z'] and gs['x'] <= obj['dposdict']['x'] and gs['y'] <= obj['dposdict']['y'] and gs['z'] <= obj['dposdict']['z']:
        # Take the player to the destination if they are within the boundaries of the door.
        gs['x'] = obj['exitposdict']['x']
        gs['y'] = obj['exitposdict']['y']
        gs['z'] = obj['exitposdict']['z']
        gs['realX'] = 200 + gs['x'] + gs['z']
        gs['realY'] = 200 + gs['x'] + gs['z'] + gs['y']
        gs['lvl'] = obj['exitlvl']
        gs['isMovingUp'] = False
        gs['isMovingDown'] = False
        gs['isMovingLeft'] = False
        gs['isMovingRight'] = False
        return 'CHANGELVL'
def tickKill(obj):
    if gs['x'] >= obj['posdict']['x'] and gs['y'] >= obj['posdict']['y'] and gs['z'] >= obj['posdict']['z'] and gs['x'] <= obj['dposdict']['x'] and gs['y'] <= obj['dposdict']['y'] and gs['z'] <= obj['dposdict']['z']:
        gs['isAlive'] = False
def tickLadder(obj):
    if gs['x'] >= obj['posdict']['x'] and gs['y'] >= obj['posdict']['y'] and gs['z'] >= obj['posdict']['z'] and gs['x'] <= obj['dposdict']['x'] and gs['y'] <= obj['dposdict']['y'] and gs['z'] <= obj['dposdict']['z']:
        print('You are supposedly on a ladder...')
def getGamestate(): # Will be used for saving.
    return gs

def setGamestate(gsin): # Will be used for loading.
    gs = gsin

def start():
    char = pygame.image.load(gs['char'])
    charflip = pygame.transform.flip(char, True, False)
    chardisplay = char
    lvl = pygame.image.load('../maps/' + gs['lvl'] + '/visual.png')
    entities = json.loads(open('../maps/' + gs['lvl'] + '/entities.json').read())
    charmask = pygame.mask.from_surface(char)
    lvlmask = pygame.mask.from_surface(pygame.image.load('../maps/' + gs['lvl'] + '/walls.png'))
    bullet = pygame.image.load('../assets/sprites/bullet/bullet.png')
    bx = 0
    by = 0
    bulletIsExisting = False
    hitmask = pygame.mask.from_surface(pygame.image.load('../assets/sprites/player/hitbox.png'))
    while True:
        if not gs['isAlive']:
            return 'DIE'
        gs['realX'] = math.floor(gs['x'] * 2 - gs['z'] * 2 + 0.25)
        gs['realY'] = math.floor(gs['x'] + gs['z'] - gs['y'] + 0.50)
        timeStart = time.process_time()
        DISPLAYSURF.blit(lvl, (0,0))
        DISPLAYSURF.blit(chardisplay,(gs['realX'],gs['realY']))

        for obj in entities: # Tick through every entity in the lvl
            if obj['type'] == 'door':
                if tickDoor(obj) == 'CHANGELVL':
                    return 'CHANGELVL'
            if obj['type'] == 'kill':
                tickKill(obj)
        
        if bulletIsExisting:
            DISPLAYSURF.blit(bullet,(bx,by))
            if gs['bulletDirection'] is 'left':
                bx = bx - 5
                by = by - 5
            if gs['bulletDirection'] is 'right':
                bx = bx + 5
                by = by + 5
            if gs['bulletDirection'] is 'up':
                bx = bx + 5
                by = by - 5
            if gs['bulletDirection'] is 'down':
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
                gs['facing'] = 'up'
            if event.type is KEYDOWN and event.key is K_a:
                gs['isMovingLeft'] = True
                chardisplay = char
                gs['facing'] = 'left'
            if event.type is KEYDOWN and event.key is K_s:
                gs['isMovingDown'] = True
                gs['facing'] = 'down'
            if event.type is KEYDOWN and event.key is K_d:
                gs['isMovingRight'] = True
                chardisplay = charflip
                gs['facing'] = 'right'
                
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
                gs['bulletDirection'] = gs['facing']

        if gs['isMovingUp'] and     lvlmask.overlap_area(hitmask, (math.floor(gs['x'] * 2 - (gs['z']-2*gs['speed']) * 2 + 0.25) , math.floor(gs['x'] + (gs['z']-2*gs['speed']) + 0.50))) is 0:
            gs['z'] = gs['z'] - 2*gs['speed']
        if gs['isMovingLeft'] and   lvlmask.overlap_area(hitmask, (math.floor((gs['x']-2*gs['speed']) * 2 - gs['z'] * 2 + 0.25) , math.floor((gs['x']-2*gs['speed']) + gs['z'] + 0.50))) is 0:
            gs['x'] = gs['x'] - 2*gs['speed'] 
        if gs['isMovingDown'] and   lvlmask.overlap_area(hitmask, (math.floor(gs['x'] * 2 - (gs['z']+2*gs['speed']) * 2 + 0.25) , math.floor(gs['x'] + (gs['z']+2*gs['speed']) + 0.50))) is 0:
            gs['z'] = gs['z'] + 2*gs['speed'] 
        if gs['isMovingRight'] and  lvlmask.overlap_area(hitmask, (math.floor((gs['x']+2*gs['speed']) * 2 - gs['z'] * 2 + 0.25) , math.floor((gs['x']+2*gs['speed']) + gs['z'] + 0.50))) is 0:
            gs['x'] = gs['x'] + 2*gs['speed']

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

        DISPLAYSURF.blit(FONT.render(str(gs['x']) + '_' + str(gs['y']) + '_' + str(gs['z']), True, (0, 128, 255), (0, 0, 0)), (25,25))
        while True:
            if time.process_time() - timeStart > 0.03:
                pygame.display.update()
                break

     
            

    
    
    
