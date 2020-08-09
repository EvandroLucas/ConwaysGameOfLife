import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np
import math
import random
import sys
from random import randrange


def checkSurrondingsOn(row,col,numRows,numCols,matrix):
    if row < 0 or row >= numRows: 
        return 0
    if col < 0  or col >= numCols: 
        return 0
    if matrix[row][col]:
        return 1
    else :
        return 0

def radiation(matrix,numRows,numCols,rate):

    numElem = numRows*numCols
    particles = math.floor(rate * numElem)
    for i in range(0,particles):
        matrix[randrange(numRows)][randrange(numCols)] = True
    return matrix



def conway(matrix,numRows,numCols):

    newMatrix = np.full((numRows,numCols),False)

    for row in range(0,numRows):
        for col in range(0,numCols):
            liveCells = 0

            liveCells += checkSurrondingsOn(row-1,col-1,numRows,numCols,matrix)
            liveCells += checkSurrondingsOn(row-1,col  ,numRows,numCols,matrix)
            liveCells += checkSurrondingsOn(row-1,col+1,numRows,numCols,matrix)

            liveCells += checkSurrondingsOn(row,col-1,numRows,numCols,matrix)
            if liveCells < 4 : 
                liveCells += checkSurrondingsOn(row,col+1,numRows,numCols,matrix)
                if liveCells < 4 : 
                    liveCells += checkSurrondingsOn(row+1,col-1,numRows,numCols,matrix)
                    if liveCells < 4 : 
                        liveCells += checkSurrondingsOn(row+1,col  ,numRows,numCols,matrix)
                        if liveCells < 4 : 
                            liveCells += checkSurrondingsOn(row+1,col+1,numRows,numCols,matrix)

                            if (liveCells == 2 or liveCells == 3) and matrix[row][col]:
                                newMatrix[row][col] = True 
                            elif liveCells == 3 and not matrix[row][col] :
                                newMatrix[row][col] = True 

    return newMatrix


def tileFromMatrix(gridPosX,gridPosY,numRows,numCols,tileSize):
    tile(gridPosY,numRows-gridPosX-1,tileSize)

def tile (gridPosX, gridPosY, tileSize) :
    glBegin(GL_QUADS)
    
    BottomLeftX = tileSize * gridPosX
    BottomLeftY = tileSize * gridPosY
    
    aux1 = BottomLeftX+tileSize
    aux2 = BottomLeftY+tileSize 

    glVertex2f(BottomLeftX          , BottomLeftY           ) # bottom left
    glVertex2f(aux1 , BottomLeftY           ) # bottom right
    glVertex2f(aux1 , aux2  ) # top right 
    glVertex2f(BottomLeftX          , aux2  ) # top left

    glEnd()

def redTile(gridPosX, gridPosY, tileSize):
    glColor3f(1, 0, 0)
    tile(gridPosX, gridPosY, tileSize)

def grid(matrix,numRows,numCols,tileSize):

    gridSizeH = numCols*tileSize
    gridSizeV = numRows*tileSize

    glBegin(GL_LINES)

    # Left line 
    glColor3f(1, 1, 1)
    glVertex3fv(( 0, 0, 0))
    glVertex3fv(( 0, gridSizeV, 0))
    # Top Line
    glVertex3fv(( 0, gridSizeV, 0))
    glVertex3fv(( gridSizeH, gridSizeV, 0))
    # Right Line
    glVertex3fv(( gridSizeH, gridSizeV, 0))
    glVertex3fv(( gridSizeH, 0, 0))
    # Bottom Line
    glVertex3fv(( 0, 0, 0))
    glVertex3fv(( gridSizeH, 0, 0))

    glColor3f(0.15, 0.15, 0.15)


    for i in range(1,numCols) :
        glVertex3fv(( tileSize*i, 0, 0))
        glVertex3fv(( tileSize*i, gridSizeV, 0))

    for i in range(1,numRows) :
        glVertex3fv(( 0, tileSize*i, 0))
        glVertex3fv(( gridSizeH, tileSize*i, 0))

    glEnd()

    glColor3f(1, 1, 1)
    for row in range(0,numRows):
        for col in range(0,numCols):
            if matrix[row][col]:
                tileFromMatrix(row,col,numRows,numCols,tileSize)

def randomMatrix(numRows,numCols):
    matrix = np.zeros((numRows,numCols))

    for row in range(0,numRows):
        for col in range(0,numCols):
            matrix[row][col] = bool(random.getrandbits(1))
    
    return matrix


def waitForKey(key) : 

    while(True):
        pygame.time.wait(200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == key:
                    return

def main():

    if len(sys.argv) >= 2 :
        numRows = min(120,int(sys.argv[1]))
        numCols = min(120,int(sys.argv[2]))
    
    else:
        numRows = 60
        numCols = 60
    numElem = numRows * numCols
    #matrix = randomMatrix(numRows,numCols)
    matrix = np.zeros((numRows,numCols))

    tickTime = 0

    print("Versão: " + str(glGetString(GL_VERSION)))
    pygame.init()

    display = (800 ,800 )

    if (display[1] == 800):
        tileSizeFactor = 137.5

    if (display[1] == 600):
        tileSizeFactor = 104

    tickTime = 10


    if (numRows <= 20):
        tileSize = 0.2
        tickTime = 60
    if (20 < numRows <= 40):
        tileSize = 0.08
        tickTime = 40
    if (40 < numRows <= 90):
        tileSize = 0.06
        tickTime = 40
    if (90 < numRows <= 120) :
        tileSize = 0.04
    if (120 < numRows <= 150) :
        tileSize = 0.03
    if (150 < numRows <= 200) :
        tileSize = 0.02
    if (200 < numRows):
        tileSize = 0.01

    


    print ("Display: " + str(display))
    print ("TileSize: " + str(tileSize))
    print ("Matrix: " + str(numRows) + " lines,"+str(numCols)+" cols," + str(numElem)+ " elements   " )
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL|HWSURFACE)

    maxFov = 45
    fov = 45
    gluPerspective(fov, (display[0]/display[1]), 0, 10)
    glClearColor(0.1,0.1,0.1,0.1)
    translation = (((numCols*tileSize)/(-2)) , ((numRows*tileSize)/(-2)) , -7)
    glTranslatef(translation[0],translation[1],translation[2])
    # glTranslatef(0, 0,-7)


    paused = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if paused : 
                        print("Game Resumed")
                        paused = False
                    elif not paused:
                        print("Game Paused")
                        paused = True
                elif event.key == pygame.K_DOWN:
                    print("Down")
                elif event.key == pygame.K_DELETE:
                    print("Deleting")
                    matrix = np.zeros((numRows,numCols))
                elif event.key == pygame.K_r:
                    print("Random")
                    matrix = randomMatrix(numRows,numCols)

        glClear(GL_COLOR_BUFFER_BIT)

        matrix[0][0] = True
        matrix[-1][-1] = True

        grid(matrix,numRows,numCols,tileSize)


        pos = pygame.mouse.get_pos()
        #print("mouse pos: " + str(pos))
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        # print("mouse pressed: " + str(pressed1) +"," + str(pressed2) +"," + str(pressed3))

        tileSizeInPixels = tileSizeFactor * (tileSize)
        gridWidthInPixels = math.floor(tileSizeInPixels * numCols)
        gridHeightInPixels = math.floor(tileSizeInPixels * numRows)
        hDiff = (display[0] - gridWidthInPixels)
        vDiff = (display[1] - gridHeightInPixels)
        hMargin = hDiff/2
        vMargin = vDiff/2

        #print("hDiff /2 = " + str(hMargin))
        #print("vDiff /2 = " + str(vMargin))

        blPos = (hDiff/2            ,display[1]-vMargin)
        brPos = (display[0]-hMargin   ,display[1]-vMargin)
        tlPos = (hDiff/2            ,vDiff/2)
        trPos = (display[0]-hMargin   ,vDiff/2)

        #print("BL : " + str(blPos))
        #print("BR : " + str(brPos))
        #print("TL : " + str(tlPos))
        #print("TR : " + str(trPos))

        truePos = [0,0]
        truePos[0] = (pos[0] - blPos[0] ) / tileSizeInPixels
        truePos[1] = (pos[1] - blPos[1] ) / tileSizeInPixels
        truePos[0] = math.floor(truePos[0]) 
        truePos[1] = math.floor(truePos[1]*(-1))

        #print("True pos: " + str(truePos))
        redTile(truePos[0],truePos[1],tileSize)
        if (0 <= truePos[0] < numCols) and (0 <= truePos[1] < numRows) :
            if pressed1 == 1 :
                matrix[-truePos[1]-1][truePos[0]] = True
            elif pressed3 == 1 :
                matrix[-truePos[1]-1][truePos[0]] = False

        # redTile(0,0,tileSize)
        # redTile(numRows-1,numCols-1,tileSize)

        pygame.display.flip()
        pygame.time.wait(tickTime)

        # if np.count_nonzero(matrix) == 0 :
        #     matrix = randomMatrix()
        #     grid(matrix,tileSize)
        #     pygame.display.flip()
        #     pygame.time.wait(tickTime)
            
        if not paused : 

            matrix = conway(matrix,numRows,numCols)
            matrix = radiation(matrix,numRows,numCols,0.0000)

        pygame.event.pump()
main()
