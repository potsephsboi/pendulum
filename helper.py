import numpy as np
import pygame 
import time

WIDTH = 600
HEIGHT = 400
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

AXLE_POINT = pygame.Rect(292, 92, 16, 16)
RADIUS = 200

OSC_POINT_x0 = AXLE_POINT.x + RADIUS
OSC_POINT_y0 = AXLE_POINT.y
OSC_POINT = pygame.Rect(OSC_POINT_x0, OSC_POINT_y0, 16, 16)

### θ(t) calculation ###

g = 9.8
L = 2
m = 0.5
theta0 = np.pi / 2
thetad0 = 0

def theta(t):
    th = theta0
    thd = thetad0
    dt = 0.01
    for _ in np.arange(0, t, dt):
        thdd = -m*thd - (g/L)*np.sin(th)
        th += thd*dt
        thd += thdd*dt
    return th

### θ(t) calculation ###


def update_osc_point(runtime):
    th = theta(runtime)
    OSC_POINT.x = AXLE_POINT.x + RADIUS * np.sin(th)
    OSC_POINT.y = AXLE_POINT.y + RADIUS * np.cos(th)