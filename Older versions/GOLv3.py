import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np
import math
import random


def checkSurrondingsOn(row,col,numRows,numCols,matrix):
    if row < 0 or row >= numRows: 
        return 0
    if col < 0  or col >= numCols: 
        return 0
    if matrix[row][col]:
        return 1
    else :
        return 0

def conway(matrix,numRows,numCols):

    newMatrix = np.zeros((numRows,numCols))

    for row in range(0,numRows):
        for col in range(0,numCols):
            liveCells = 0
            liveCells += checkSurrondingsOn(row-1,col-1,numRows,numCols,matrix)
            liveCells += checkSurrondingsOn(row-1,col  ,numRows,numCols,matrix)
            liveCells += checkSurrondingsOn(row-1,col+1,numRows,numCols,matrix)

            liveCells += checkSurrondingsOn(row,col-1,numRows,numCols,matrix)
            liveCells += checkSurrondingsOn(row,col+1,numRows,numCols,matrix)

            liveCells += checkSurrondingsOn(row+1,col-1,numRows,numCols,matrix)
            liveCells += checkSurrondingsOn(row+1,col  ,numRows,numCols,matrix)
            liveCells += checkSurrondingsOn(row+1,col+1,numRows,numCols,matrix)

            
            if (liveCells == 2 or liveCells == 3) and matrix[row][col]:
                newMatrix[row][col] = True 

            if liveCells == 3 and not matrix[row][col] :
                newMatrix[row][col] = True 

            #newMatrix[row][col] = bool(random.getrandbits(1))

    return newMatrix

def tile (gridPosX, gridPosY, tileSize) :
    glBegin(GL_QUADS)
    
    BottomLeftX = tileSize * gridPosX
    BottomLeftY = tileSize * gridPosY
    
    aux1 = BottomLeftX+tileSize
    aux2 = BottomLeftY+tileSize 

    glVertex3f(BottomLeftX          , BottomLeftY           , 0.0) # bottom left
    glVertex3f(aux1 , BottomLeftY           , 0.0) # bottom right
    glVertex3f(aux1 , aux2  , 0.0) # top right 
    glVertex3f(BottomLeftX          , aux2  , 0.0) # top left

    glEnd()

def grid(matrix,numRows,numCols,tileSize):

    gridSize = 10
    gridSizeH = numCols*tileSize
    gridSizeV = numRows*tileSize

    # print("Grid Size H: " + str(gridSizeH))
    # print("Grid Size Y: " + str(gridSizeV))

    # glBegin(GL_LINES)

    # # Left line 
    # glColor3f(1, 1, 1)
    # glVertex3fv(( 0, 0, 0))
    # glVertex3fv(( 0, gridSizeV, 0))
    # # Top Line
    # glVertex3fv(( 0, gridSizeV, 0))
    # glVertex3fv(( gridSizeH, gridSizeV, 0))
    # # Right Line
    # glVertex3fv(( gridSizeH, gridSizeV, 0))
    # glVertex3fv(( gridSizeH, 0, 0))
    # # Bottom Line
    # glVertex3fv(( 0, 0, 0))
    # glVertex3fv(( gridSizeH, 0, 0))

    # glColor3f(0.15, 0.15, 0.15)


    # for i in range(1,gridColNum) :
    #     glVertex3fv(( tileSize*i, 0, 0))
    #     glVertex3fv(( tileSize*i, gridSizeV, 0))

    # for i in range(1,gridRowNum) :
    #     glVertex3fv(( 0, tileSize*i, 0))
    #     glVertex3fv(( gridSizeH, tileSize*i, 0))

    # glEnd()

    glColor3f(1, 1, 1)
    for row in range(0,numRows):
        for col in range(0,numCols):
            if matrix[row][col]:
                tile(col,numRows-row-1,tileSize)

def randomMatrix(numRows,numCols):
    matrix = np.zeros((numRows,numCols))

    for row in range(0,numRows):
        for col in range(0,numCols):
            matrix[row][col] = bool(random.getrandbits(1))
    
    return matrix

def main():

    numRows = 130
    numCols = 130
    numElem = numRows * numCols
    matrix = randomMatrix(numRows,numCols)

    tickTime = 0

    print("Versão: " + str(glGetString(GL_VERSION)))
    pygame.init()
    display = (1400,900)

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

    gluPerspective(45, (display[0]/display[1]), 0.1, 500.0)
    glClearColor(0.1,0.1,0.1,0.1)
    glTranslatef(((numCols*tileSize)/(-2)), ((numRows*tileSize)/(-2)),-7)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        grid(matrix,numRows,numCols,tileSize)
        pygame.display.flip()
        pygame.time.wait(tickTime)

        # if np.count_nonzero(matrix) == 0 :
        #     matrix = randomMatrix()
        #     grid(matrix,tileSize)
        #     pygame.display.flip()
        #     pygame.time.wait(tickTime)
            

        matrix = conway(matrix,numRows,numCols)

main()