import random

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def draw_one(a, b, c, d):
    glLineWidth(10)
    glBegin(GL_LINES)
    glVertex2f(a, b)
    glVertex2f(c, d)
    glEnd()

def draw_first_one():
    glColor3f(1.0, 0.0, 0.0)
    draw_one(50, 50, 50, 150)

def draw_second_one():
    glColor3f(1.0, 0.0, 1.0)
    draw_one(150, 50, 150, 150)

def draw_third_one():
    glColor3f(0.0, 0.0, 0.0)
    draw_one(250, 50, 250, 150)

def draw_fourth_one():
    glColor3f(0.0, 0.8, 0.1)
    draw_one(280, 50, 280, 150)

def draw_nine():
    glLineWidth(10)
    glColor3f(0.0, 1.0, 1.0)
    glBegin(GL_LINES)

    # square
    glVertex2f(80, 110)
    glVertex2f(120, 110)

    glVertex2f(120, 110)
    glVertex2f(120, 150)

    glVertex2f(120, 150)
    glVertex2f(80, 150)

    glVertex2f(80, 150)
    glVertex2f(80, 110)

    # stick
    glVertex2f(120, 50)
    glVertex2f(120, 110)
    glEnd()

def draw_zero():
    glLineWidth(10)
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_LINES)

    # square
    glVertex2f(180, 50)
    glVertex2f(220, 50)

    glVertex2f(220, 50)
    glVertex2f(220, 150)

    glVertex2f(220, 150)
    glVertex2f(180, 150)

    glVertex2f(180, 150)
    glVertex2f(180, 50)
    glEnd()

def draw_four():
    glLineWidth(10)
    glColor3f(1.0, 0.5, 0.0)
    glBegin(GL_LINES)

    # square
    glVertex2f(310, 110)
    glVertex2f(350, 110)

    glVertex2f(350, 110)
    glVertex2f(350, 150)

    # glVertex2f(350, 150)
    # glVertex2f(310, 150)

    glVertex2f(310, 150)
    glVertex2f(310, 110)

    # stick
    glVertex2f(350, 50)
    glVertex2f(350, 110)
    glEnd()

def draw_seven():
    glLineWidth(10)
    glColor3f(0.0, 0.5, 1.0)
    glBegin(GL_LINES)

    # horizontal stick
    glVertex2f(380, 150)
    glVertex2f(420, 150)

    # vertical stick
    glVertex2f(420, 150)
    glVertex2f(420, 50)
    glEnd()

def iterate():
    glViewport(0, 0, 1000, 600)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    # setting the bg color to white
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # glColor3f(0.5, 0.4, 1.0) #konokichur color set (RGB)
    #call the draw methods here

    draw_first_one()
    draw_nine()

    draw_second_one()
    draw_zero()

    draw_third_one()
    draw_fourth_one()

    draw_four()
    draw_seven()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 250) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()