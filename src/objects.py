# classes for the different objects in the simulation
from utils import *


class Ball():
    def __init__(self, mass=1):
        self.mass = mass
        
        
class GravityBall(Ball):
    def __init__(self, mass=1, radius=1, x0=0, y0=0, vx0=0, vy0=0, ax=0, ay=0):
        super().__init__()
        self.mass = mass
        self.radius = radius
        self.x0 = x0
        self.y0 = y0
        self.vx0 = vx0
        self.vy0 = vy0
        self.x = x0
        self.y = y0
        self.vx = vx0
        self.vy = vy0
        self.ax = ax
        self.ay = ay
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y
    def set_vx(self, vx):
        self.vx = vx
    def set_vy(self, vy):
        self.vy = vy
    def set_ax(self, ax):
        self.ax = ax
    def set_ay(self, ay):
        self.ay = ay
    def get_vx0(self):
        return self.vx0
    def get_vy0(self):
        return self.vy0
    def get_x0(self):
        return self.x0
    def get_y0(self):
        return self.y0
    def get_vx(self):
        return self.vx
    def get_vy(self):
        return self.vy
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_ax(self):
        return self.ax
    def get_ay(self):
        return self.ay
    def get_mass(self):
        return self.mass
    def get_radius(self):
        return self.radius