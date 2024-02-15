import random

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_knob():
    glColor3f(1.0, 0.5, 0.0)

    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(285, 125) #jekhane show korbe pixel
    glEnd()

def draw_triangle():
    glColor3f(0.0, 0.5, 1.0)

    glBegin(GL_TRIANGLES)
    glVertex2f(100, 350)
    glVertex2f(400, 350)
    glVertex2f(250, 500)
    glEnd()

def draw_square():
    glColor3f(1.0, 0.0, 1.0)

    glBegin(GL_LINES)
    glVertex(100, 50)
    glVertex(400, 50)

    glVertex(400, 50)
    glVertex(400, 350)

    glVertex(400, 350)
    glVertex(100, 350)

    glVertex(100, 350)
    glVertex(100, 50)
    glEnd()

def draw_window():
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 0.0)

    # window 1
    glVertex(120, 240)
    glVertex(180, 240)
    glVertex(180, 300)
    glVertex(120, 300)

    # window 2
    glVertex(320, 240)
    glVertex(380, 240)
    glVertex(380, 300)
    glVertex(320, 300)

    glColor3f(0.4, 0.9, 0.6)
    glEnd()

def draw_door():
    glColor3f(0.4, 0.9, 0.6)

    glBegin(GL_LINES)
    glVertex(210, 50)
    glVertex(290, 50)

    glVertex(290, 50)
    glVertex(290, 200)

    glVertex(290, 200)
    glVertex(210, 200)

    glVertex(210, 200)
    glVertex(210, 50)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    #konokichur color set (RGB)
    #call the draw methods here

    draw_triangle()
    draw_square()

    draw_window()
    draw_door()

    draw_knob()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()