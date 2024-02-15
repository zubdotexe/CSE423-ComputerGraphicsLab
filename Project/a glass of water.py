import random

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

found_zone = None


def find_zone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    zone = None
    if abs(dx) >= abs(dy):
        if dx >= 0 and dy >= 0:
            zone = 0
        elif dx <= 0 and dy >= 0:
            zone = 3
        elif dx <= 0 and dy <= 0:
            zone = 4
        elif dx >= 0 and dy <= 0:
            zone = 7
    else:
        if dx >= 0 and dy >= 0:
            zone = 1
        elif dx <= 0 and dy >= 0:
            zone = 2
        elif dx <= 0 and dy <= 0:
            zone = 5
        else: # dx= > 0 and dy <= 0
            zone = 6

    return zone


def convert_zone(x1, y1, x2, y2):
    global found_zone
    found_zone = find_zone(x1, y1, x2, y2)
    # print(found_zone)

    if found_zone == 0:
        return x1, y1, x2, y2
    if found_zone == 1:
        a1 = y1
        b1 = x1
        a2 = y2
        b2 = x2
    elif found_zone == 2:
        a1 = y1
        b1 = -x1
        a2 = y2
        b2 = -x2
    elif found_zone == 3:
        a1 = -x1
        b1 = y1
        a2 = -x2
        b2 = y2
    elif found_zone == 4:
        a1 = -x1
        b1 = -y1
        a2 = -x2
        b2 = -y2
    elif found_zone == 5:
        a1 = -y1
        b1 = -x1
        a2 = -y2
        b2 = -x2
    elif found_zone == 6:
        a1 = -y1
        b1 = x1
        a2 = -y2
        b2 = x2
    else:
        a1 = x1
        b1 = -y1
        a2 = x2
        b2 = -y2

    return a1, b1, a2, b2


def convert_to_origin(x1, y1):
    if found_zone == 0:
        return x1, y1

    if found_zone == 1:
        a1 = y1
        b1 = x1
    elif found_zone == 2:
        a1 = -y1
        b1 = x1
    elif found_zone == 3:
        a1 = -x1
        b1 = y1
    elif found_zone == 4:
        a1 = -x1
        b1 = -y1
    elif found_zone == 5:
        a1 = -y1
        b1 = -x1
    elif found_zone == 6:
        a1 = y1
        b1 = -x1
    else:
        a1 = x1
        b1 = -y1

    return a1, b1


def mp_l(a1, b1, a2, b2):
    x1, y1, x2, y2 = convert_zone(a1, b1, a2, b2)
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    dNE = 2 * (dy - dx)
    dE = 2 * dy

    x = x1
    y = y1
    while x < x2:
        a, b = convert_to_origin(x, y)
        draw_points(a, b)
        if d <= 0:
            d = d + dE
            x += 1
            y += 0
            # print('d <= 0', d, x, y)
        else:
            d = d + dNE
            x += 1
            y += 1


def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()


def draw_glass():
    glColor3f(0.9, 0.9, 0.9)
    mp_l(400, 600, 400, 200)
    mp_l(400, 200, 600, 200)
    mp_l(600, 200, 600, 600)


def draw_water():
    glColor3f(0.4, 0.7, 0.9)
    for i in range(200+5, 400):
        mp_l(400+5, i, 600-4, i)    # as 600-4 is exclusive


def scale():
    v1 = np.array([[400+5],
                   [200+5],
                   [1]])

    v2 = np.array([[600-5],
                   [600-5],
                   [1]])

    sc = 0.9
    s = np.array([[1, 0, 0],
                  [0, sc, 0],
                  [0, 0, 1]])

    v11 = np.matmul(s, v1)
    v22 = np.matmul(s, v2)

    v22_int = int(v22[1][0])
    for i in range(200+5, v22_int):
        print(i)
        mp_l(400+5, i, 600-4, i) # 600-4 is exclusive

def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # glColor3f(0.4, 0.9, 0.6) #konokichur color set (RGB)
    #call the draw methods here
    draw_glass()
    draw_water()
    glutSwapBuffers()

    user_input = input()
    if user_input == '1':
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        iterate()

        draw_glass()
        draw_water()
        scale()
        glutSwapBuffers()
    # glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"A glass of water") #window name
glutDisplayFunc(showScreen)

glutMainLoop()