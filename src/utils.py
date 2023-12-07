from objects import *
import math
# physics constants

FUDGE = 25 # fudge factor to make animations more realistic
G_0 = 9.80665 # acceleration due to gravity
G = 6.67e-11 # gravitation constant

# Environment variables
LOSS = 0.5 # collisions will lose x% energy

# physics functions

def calculate_position(ball, dt):
    # ball.set_vx(ball.get_vx0() + time * ball.get_ax())
    #ball.set_vy(ball.get_vy0() + time * ball.get_ay())
    # ball.set_x(ball.get_x0() + ball.get_vx0() * time + ball.get_ax() * time * time / 2)
    # ball.set_y(ball.get_y0() + ball.get_vy0() * time + ball.get_ay() * time * time / 2)
    ball.set_vx(ball.get_vx() + dt * ball.get_ax())
    ball.set_x(ball.get_x() + ball.get_vx() * dt + ball.get_ax() * dt * dt / 2)
    ball.set_vy(ball.get_vy() + dt * ball.get_ay())
    ball.set_y(ball.get_y() + ball.get_vy() * dt + ball.get_ay() * dt * dt / 2)
    return
    
def collision_handler(ball, height):
    if (ball.get_y() + ball.get_radius() >= height):
        ball.set_vy(-ball.get_vy() * (1-LOSS))
        ball.set_y(height-ball.get_radius())
    return

def calculate_mechanical_energy(ball, height):
    return ball.get_mass() * ball.get_vy() * ball.get_vy() / 2 + (height - ball.get_y() - ball.get_radius()) * ball.get_mass() * G_0 * FUDGE

def calculate_gravitational_force(ball, ball2):
    m1 = ball.get_mass()
    m2 = ball2.get_mass()
    x1 = ball.get_x()
    x2 = ball2.get_x()
    y1 = ball.get_y()
    y2 = ball2.get_y()
    f = G * m1 * m2 / ((x2 - x1)**2 + (y2 - y1)**2)  # magnitude of the gravitational force
    theta = math.atan2(y2 - y1, x2 - x1)  # angle between the line joining the two objects and the x-axis
    fx = f * math.cos(theta)  # x component of the gravitational force
    fy = f * math.sin(theta)  # y component of the gravitational force
    ax = fx / ball.get_mass()
    ay = fy / ball.get_mass()
    ax2 = fx / ball2.get_mass()
    ay2 = fy / ball2.get_mass()
    ball.set_ax(ax if x1 < x2 else -ax)
    ball.set_ay(ay if y1 < y2 else -ay)
    ball2.set_ax(ax2 if x2 < x1 else -ax2)
    ball2.set_ay(ay2 if y2 < y1 else -ay2)
    return
