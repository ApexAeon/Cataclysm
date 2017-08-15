import pygame, sys
from pygame.locals import *
from common import DISPLAYSURF
from common import FONT
import json
import time
import math
import sound
import pygame.mixer

pygame.mixer.init()

gs = {
    'isJumping':False,
    'jumpHeight':0,
    'isMovingUp':False,
    'isMovingDown':False,
    'isMovingLeft':False,
    'isMovingRight':False,
    'char':'../assets/sprites/player/player.png',
    'x':25,
    'y':0 ,
    'z':12,
    'lvl':'c01a',
    'realX':0,
    'realY':0,
    'facing':'left',
    'speed':0.5,
    'isAlive':True,
    'bullets':[],
    'isMoving':False,
    'velocity':{'north':0, 'south':0, 'east':0, 'west':0, 'up':0, 'down':0}
}

res = {}

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

def getGamestate(): # Will be used for saving.
    return gs
def setGamestate(gsin): # Will be used for loading.
    gs = gsin

def calcX(x, y, z):
    return ((x * 2 - z * 2) + 0.25 * (x-z)) * 4
def calcY(x, y, z):
    return ((x + z - y) + 0.25 * (x+z)) * 4
def start():
    res['charLeft'] = pygame.image.load(gs['char'])
    res['charRight'] = pygame.transform.flip(res['charLeft'], True, False)
    res['bullet'] = pygame.image.load('../assets/sprites/bullet/bullet.png')
    res['hitbox'] = pygame.image.load('../assets/sprites/player/hitbox.png')
    res['lvl'] = pygame.image.load('../maps/' + gs['lvl'] + '/visual.png')
    res['walls'] = pygame.image.load('../maps/' + gs['lvl'] + '/walls.png')
    chardisplay = res['charLeft']
    entities = json.loads(open('../maps/' + gs['lvl'] + '/entities.json').read())
    lvlmask = pygame.mask.from_surface(res['walls'])
    hitmask = pygame.mask.from_surface(res['hitbox'])
    dat = json.loads(open('../maps/' + gs['lvl'] + '/dat.json').read())
    sound.play(dat['sounds'])
    bulletIsExisting = False
    res['stepsounds'] = pygame.mixer.Sound('../assets/sounds/player/step.wav')
#
# Main Game Loop
#
    while True:
        sound.ping()
        if not gs['isAlive']:
            return 'DIE'
        gs['realX'] = calcX(gs['x'], gs['y'], gs['z'])
        gs['realY'] = calcY(gs['x'], gs['y'], gs['z'])

        timeStart = time.process_time() # Used to facilitate timing and FPS, see bottom of loop for more info.

        DISPLAYSURF.blit(res['lvl'], (0,0))
        DISPLAYSURF.blit(chardisplay,(math.floor(gs['realX']),math.floor(gs['realY'])))

        for obj in entities: # Tick through every entity in the lvl
            if obj['type'] == 'door':
                if tickDoor(obj) == 'CHANGELVL':
                    return 'CHANGELVL'
            if obj['type'] == 'kill':
                tickKill(obj)
        
        if bulletIsExisting:
            DISPLAYSURF.blit(res['bullet'],(bx,by))
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

#
# Event Processing
#
        for event in pygame.event.get():
            if event.type is QUIT:
               pygame.quit()
               sys.exit()
            if event.type is KEYDOWN and event.key is K_ESCAPE:
                return 'PAUSE'
            
            if event.type is KEYDOWN and event.key is K_w:
                gs['isMovingUp'] = True
                gs['facing'] = 'up'               
                gs['isMoving'] = True
            if event.type is KEYDOWN and event.key is K_a:
                gs['isMovingLeft'] = True
                chardisplay = res['charLeft']
                gs['facing'] = 'left'                
                gs['isMoving'] = True
            if event.type is KEYDOWN and event.key is K_s:
                gs['isMovingDown'] = True
                gs['facing'] = 'down'               
                gs['isMoving'] = True
            if event.type is KEYDOWN and event.key is K_d:
                gs['isMovingRight'] = True
                chardisplay = res['charRight']
                gs['facing'] = 'right'
                gs['isMoving'] = True
                
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
#
# Collision Detection and Movement
#
        if gs['isMovingUp'] and     lvlmask.overlap_area( hitmask , ( math.floor(calcX(gs['x'],0,gs['z']-1*gs['speed'])) , math.floor(calcY(gs['x'],0,gs['z']-1*gs['speed'])) ) ) is 0:
            gs['z'] = gs['z'] - 1*gs['speed']
        if gs['isMovingLeft'] and   lvlmask.overlap_area( hitmask , ( math.floor(calcX(gs['x']-1*gs['speed'],0,gs['z'])) , math.floor(calcY(gs['x']-1*gs['speed'],0,gs['z'])) ) ) is 0:
            gs['x'] = gs['x'] - 1*gs['speed'] 
        if gs['isMovingDown'] and   lvlmask.overlap_area( hitmask , ( math.floor(calcX(gs['x'],0,gs['z']+1*gs['speed'])) , math.floor(calcY(gs['x'],0,gs['z']+1*gs['speed'])) ) ) is 0:
            gs['z'] = gs['z'] + 1*gs['speed'] 
        if gs['isMovingRight'] and  lvlmask.overlap_area( hitmask , ( math.floor(calcX(gs['x']+1*gs['speed'],0,gs['z'])) , math.floor(calcY(gs['x']+1*gs['speed'],0,gs['z'])) ) ) is 0:
            gs['x'] = gs['x'] + 1*gs['speed']
#
# Jumping
#
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
#
# Debug Coordinates
#
        DISPLAYSURF.blit(FONT.render('X: ' + str(gs['x']) + ' Y: ' + str(gs['y']) + ' Z: ' + str(gs['z']), True, (0, 128, 255), (0, 0, 0)), (25,25)) # Display current player position for dev use.

        
        
        while True: # Delays time and makes sure a certain amount has passed since the last tick. Prevents crazy FPS and weird timing.
            if time.process_time() - timeStart > 0.03: #0.03
                pygame.display.update()
                break

     
            

    
    
    
