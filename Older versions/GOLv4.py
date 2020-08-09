import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np
import math
import random
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

    gridSize = 10
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
                # tile(col,numRows-row-1,tileSize)
                tile(row,col,tileSize)

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

    numRows = 120
    numCols = 120
    numElem = numRows * numCols
    matrix = randomMatrix(numRows,numCols)

    tickTime = 0

    print("Versão: " + str(glGetString(GL_VERSION)))
    pygame.init()
    display = (1000,800)

    tickTime = 10

    if numRows <= 90:
        tileSize = 0.06
        tickTime = 40
    elif numRows > 90 and numRows <= 120 :
        tileSize = 0.04
    elif numRows > 120 and numRows <= 150 :
        tileSize = 0.03
    elif numRows > 150 and numRows <= 200 :
        tileSize = 0.02
    else:
        tileSize = 0.01


    print ("Display: " + str(display))
    print ("TileSize: " + str(tileSize))
    print ("Matrix: " + str(numRows) + " lines,"+str(numCols)+" cols," + str(numElem)+ " elements   " )
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL|HWSURFACE)

    gluPerspective(45, (display[0]/display[1]), 0, 10)
    glClearColor(0.1,0.1,0.1,0.1)
    glTranslatef(((numCols*tileSize)/(-2)), ((numRows*tileSize)/(-2)),-7)


    paused = False

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

        glClear(GL_COLOR_BUFFER_BIT)


        matrix[0][0] = True
        matrix[numRows-1][numCols-1] = True
        grid(matrix,numRows,numCols,tileSize)


        pos = pygame.mouse.get_pos()
        print("mouse pos: " + str(pos))
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        print("mouse pressed: " + str(pressed1) +"," + str(pressed2) +"," + str(pressed3))

        truePos = [0,0]
        truePos[0] = math.floor((pos[0] - 167) * (numCols/(831-167)))
        truePos[1] = math.floor((pos[1] - 732) * (numRows/(69-732 )))
        print("True pos: " + str(truePos))
        redTile(truePos[0],truePos[1],tileSize)
        if pressed1 == 1 :
            matrix[truePos[0]][truePos[1]] = True
        elif pressed3 == 1 :
            matrix[truePos[0]][truePos[1]] = False

        matrix[0][0] = True
        matrix[numRows-1][numCols-1] = True


        pygame.display.flip()
        pygame.time.wait(tickTime)

        # if np.count_nonzero(matrix) == 0 :
        #     matrix = randomMatrix()
        #     grid(matrix,tileSize)
        #     pygame.display.flip()
        #     pygame.time.wait(tickTime)
            
        if not paused : 

            matrix = conway(matrix,numRows,numCols)
            matrix = radiation(matrix,numRows,numCols,0.0001)

        pygame.event.pump()
main()