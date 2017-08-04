import pygame, sys
from pygame.locals import *
import json
import os
import os.path

pygame.init()
pygame.font.init()
DISPLAYSURF = pygame.display.set_mode((828, 640))
FONT = pygame.font.SysFont('Bauhaus 93 Regular', 40)
def write(strin, pos):
    DISPLAYSURF.blit(FONT.render(strin, True, (0, 128, 255)), pos)
gridunit = pygame.image.load("../src/assets/textures/grid/v3/grid.png")
currentX = 0
currentY = 0
for a in range(0, 640//gridunit.get_height()*gridunit.get_height(), gridunit.get_height()):
    currentY = a
    for b in range(0, 828//gridunit.get_width()*gridunit.get_width(), gridunit.get_width()):
        currentX = b
        DISPLAYSURF.blit(gridunit, (currentX, currentY))
pygame.display.update()
currentX = 0
currentY = 0
currentAsset = 0
placing = False
assets = []
for dirpath, dirnames, filenames in os.walk("..\\src\\assets\\textures"):
    for filename in [f for f in filenames if f.endswith(".png")]:
        assets.append(pygame.image.load(os.path.join(dirpath, filename)))
while True:
    if placing is False:
        dispcopy = DISPLAYSURF.copy()
        placing = True
    for event in pygame.event.get():
        if event.type is QUIT:
            pygame.quit()
            sys.exit()
        elif event.type is KEYDOWN:
            if event.key == K_w:
                currentY -= gridunit.get_height()//2
                currentX += gridunit.get_width()//2
                DISPLAYSURF.blit(dispcopy, (0, 0))
                DISPLAYSURF.blit(assets[currentAsset], (currentX, currentY))
            elif event.key == K_s:
                currentY += gridunit.get_height()//2
                currentX -= gridunit.get_width()//2
                DISPLAYSURF.blit(dispcopy, (0, 0))
                DISPLAYSURF.blit(assets[currentAsset], (currentX, currentY))
            elif event.key == K_a:
                currentY -= gridunit.get_height()//2
                currentX -= gridunit.get_width()//2
                DISPLAYSURF.blit(dispcopy, (0, 0))
                DISPLAYSURF.blit(assets[currentAsset], (currentX, currentY))
            elif event.key == K_d:
                currentY += gridunit.get_height()//2
                currentX += gridunit.get_width()//2
                DISPLAYSURF.blit(dispcopy, (0, 0))
                DISPLAYSURF.blit(assets[currentAsset], (currentX, currentY))

            elif event.key == K_e:
                currentAsset -= 1
                if currentAsset is -1:
                    currentAsset=len(assets)-1
                if currentAsset is len(assets):
                    currentAsset=0
                DISPLAYSURF.blit(dispcopy, (0, 0))
                DISPLAYSURF.blit(assets[currentAsset], (currentX, currentY))
            elif event.key == K_q:
                currentAsset += 1
                if currentAsset is -1:
                    currentAsset=len(assets)-1
                if currentAsset is len(assets):
                    currentAsset=0
                DISPLAYSURF.blit(dispcopy, (0, 0))
                DISPLAYSURF.blit(assets[currentAsset], (currentX, currentY))


            elif event.key == K_RETURN:
                DISPLAYSURF.blit(dispcopy, (0, 0))
                DISPLAYSURF.blit(assets[currentAsset], (currentX, currentY))
                placing = False
    pygame.display.update()
                


