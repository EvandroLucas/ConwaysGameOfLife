import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np
import math
import random


def checkSurrondingsOn(row,col,matrix):
    if row < 0 or row >= np.size(matrix,0): 
        return 0
    if col < 0  or col >= np.size(matrix,1): 
        return 0
    if matrix[row][col] == 1:
        return 1
    else :
        return 0

def conway(matrix):

    newMatrix = np.zeros((np.size(matrix,0),np.size(matrix,1)))

    for row in range(0,np.size(matrix,0)):
        for col in range(0,np.size(matrix,1)):
           #  print("row: " + str(row) + ", col: " + str(col))
            liveCells = 0
            liveCells += checkSurrondingsOn(row-1,col-1,matrix)
            liveCells += checkSurrondingsOn(row-1,col  ,matrix)
            liveCells += checkSurrondingsOn(row-1,col+1,matrix)

            liveCells += checkSurrondingsOn(row,col-1,matrix)
            liveCells += checkSurrondingsOn(row,col+1,matrix)

            liveCells += checkSurrondingsOn(row+1,col-1,matrix)
            liveCells += checkSurrondingsOn(row+1,col  ,matrix)
            liveCells += checkSurrondingsOn(row+1,col+1,matrix)

            
            if (liveCells == 2 or liveCells == 3) and matrix[row][col] == 1 :
                newMatrix[row][col] = 1 

            if liveCells == 3 and matrix[row][col] == 0 :
                newMatrix[row][col] = 1 
                

    return newMatrix

def tile (gridPosX, gridPosY, tileSize) :
    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    
    BottomLeftX = tileSize * gridPosX
    BottomLeftY = tileSize * gridPosY

    glVertex3f(BottomLeftX          , BottomLeftY           , 0.0) # bottom left
    glVertex3f(BottomLeftX+tileSize , BottomLeftY           , 0.0) # bottom right
    glVertex3f(BottomLeftX+tileSize , BottomLeftY+tileSize  , 0.0) # top right 
    glVertex3f(BottomLeftX          , BottomLeftY+tileSize  , 0.0) # top left

    glEnd()

def grid(matrix,tileSize):

    gridColNum = np.size(matrix,1)
    gridRowNum = np.size(matrix,0)
    gridSize = 10
    gridSizeH = gridColNum*tileSize
    gridSizeV = gridRowNum*tileSize

    # print("Grid Size H: " + str(gridSizeH))
    # print("Grid Size Y: " + str(gridSizeV))

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


    for i in range(1,gridColNum) :
        glVertex3fv(( tileSize*i, 0, 0))
        glVertex3fv(( tileSize*i, gridSizeV, 0))

    for i in range(1,gridRowNum) :
        glVertex3fv(( 0, tileSize*i, 0))
        glVertex3fv(( gridSizeH, tileSize*i, 0))

    glEnd()

    for row in range(0,gridRowNum):
        for col in range(0,gridColNum):
            if matrix[row][col] == 1:
                tile(col,gridRowNum-row-1,tileSize)

def randomMatrix():
    matrix = np.zeros((110,180))

    for row in range(0,np.size(matrix,0)):
        for col in range(0,np.size(matrix,1)):
            if bool(random.getrandbits(1)) :
                matrix[row][col] = 1
    return matrix

def main():


    matrix = randomMatrix()

    tickTime = 1

    print("Versão: " + str(glGetString(GL_VERSION)))
    pygame.init()
    display = (1200,800)

    tileSize = 0.05

    print ("Display: " + str(display))
    print ("TileSize: " + str(tileSize))
    print ("Matrix: " + str(np.size(matrix,0)) + " lines,"+str(np.size(matrix,1))+" cols," + str(np.size(matrix))+ " elements   " )
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL|HWSURFACE)

    gluPerspective(45, (display[0]/display[1]), 0.1, 500.0)
    glClearColor(0.1,0.1,0.1,0.1)
    glTranslatef(((np.size(matrix,1)*tileSize)/(-2)), ((np.size(matrix,0)*tileSize)/(-2)),-8)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        grid(matrix,tileSize)
        pygame.display.flip()
        pygame.time.wait(tickTime)

        # if np.count_nonzero(matrix) == 0 :
        #     matrix = randomMatrix()
        #     grid(matrix,tileSize)
        #     pygame.display.flip()
        #     pygame.time.wait(tickTime)
            

        matrix = conway(matrix)

main()