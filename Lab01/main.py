from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


# def draw_lines():
#     glLineWidth(5) #pixel size. by default 1 thake
#     glBegin(GL_LINES)
#     glVertex2f(250, 250) #jekhane show korbe pixel
#     glVertex2f(350, 250)
#     glEnd()

# def draw_triangles():
#     glLineWidth(5) #pixel size. by default 1 thake
#     glBegin(GL_LINES)
#     # ab line
#     glVertex2f(250, 250) #jekhane show korbe pixel
#     glVertex2f(350, 250)
#
#     # bc line
#     glVertex2f(350, 250)
#     glVertex2f(350, 350)
#
#     # ca line
#     glVertex2f(350, 350)
#     glVertex2f(250, 250)
#     glEnd()

# def draw_triangles():
#     glLineWidth(5) #pixel size. by default 1 thake
#     glBegin(GL_TRIANGLES)

#     glVertex2f(250, 250) #jekhane show korbe pixel
#     glVertex2f(350, 250)
#     glVertex2f(350, 350)
#     glEnd()

def draw_quads():
    glLineWidth(5) #pixel size. by default 1 thake
    glBegin(GL_QUADS)

    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(250, 250) #jekhane show korbe pixel

    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(350, 250)

    glColor3f(0.2, 0.5, 0.3)
    glVertex2f(350, 350)

    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(250, 350)

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
    glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    #call the draw methods here
    # draw_lines()
    draw_quads()
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)

glutMainLoop()