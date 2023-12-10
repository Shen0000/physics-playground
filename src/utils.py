from objects import *
import math
# physics constants

FUDGE = 25 # fudge factor to make animations more realistic
G_0 = 9.80665

# Environment variables
LOSS = 0.1 # collisions will lose x% momentum

# physics functions

def calculate_position(ball, dt):
    # ball.set_vx(ball.get_vx0() + time * ball.get_ax())
    #ball.set_vy(ball.get_vy0() + time * ball.get_ay())
    # ball.set_x(ball.get_x0() + ball.get_vx0() * time + ball.get_ax() * time * time / 2)
    # ball.set_y(ball.get_y0() + ball.get_vy0() * time + ball.get_ay() * time * time / 2)
    ball.set_vy(ball.get_vy() + dt * ball.get_ay())
    ball.set_y(ball.get_y() + ball.get_vy() * dt + ball.get_ay() * dt * dt / 2)
    ball.set_vx(ball.get_vx() + dt * ball.get_ax())
    ball.set_x(ball.get_x() + ball.get_vx() * dt + ball.get_ax() * dt * dt / 2)
    return
    
def collision_handler(ball, height, width):
    if (ball.get_y() + ball.get_radius() >= height):
        ball.set_vy(-ball.get_vy() * (1-LOSS))
        ball.set_vx(ball.get_vx() * (1-LOSS))
        ball.set_y(height - ball.get_radius())
    if (ball.get_x() + ball.get_radius() >= width):
        ball.set_vy(ball.get_vy() * (1-LOSS))
        ball.set_vx(-ball.get_vx() * (1-LOSS))
        ball.set_x(width - ball.get_radius())
    if (ball.get_x() - ball.get_radius() <=0):
        ball.set_vy(ball.get_vy() * (1-LOSS))
        ball.set_vx(-ball.get_vx() * (1-LOSS))
        ball.set_x(ball.get_radius())
    return

def calculate_mechanical_energy(ball, height):
    return ball.get_mass() * ball.get_vy() * ball.get_vy() / 2 + (height - ball.get_y() - ball.get_radius()) * ball.get_mass() * G_0 * FUDGE

def check_collision(b, b2):
    return (b.get_x() - b2.get_x()) ** 2 + (b.get_y() - b2.get_y()) ** 2 <= (b.get_radius() + b2.get_radius()) ** 2

def ball_collision(b, b2):
    dx = b2.get_x() - b.get_x()
    dy = b2.get_y() - b.get_y()
    distance = (dx ** 2 + dy ** 2) ** (1/2)
    # Calculate the new velocities using the conservation of momentum and kinetic energy
    angle = math.atan2(dy, dx)
    m1 = b.get_mass()
    m2 = b2.get_mass()
    u1 = (b.get_vx() ** 2 + b.get_vy() ** 2) ** (1/2)
    u2 = (b2.get_vx() ** 2 + b2.get_vy() ** 2) ** (1/2)
    
    # Velocity components along the line of impact
    velocity_angle = math.atan2(b.get_vy(), b.get_vx())
    velocity_angle2 = math.atan2(b2.get_vy(), b2.get_vx())
    v1x = u1 * math.cos(velocity_angle - angle)
    v1y = u1 * math.sin(velocity_angle - angle)
    v2x = u2 * math.cos(velocity_angle2 - angle)
    v2y = u2 * math.sin(velocity_angle2 - angle)
    
    # New velocities after the collision
    v1x_prime = ((m1 - m2) * v1x + 2 * m2 * v2x) / (m1 + m2) * math.cos(angle) + u1 * math.sin(velocity_angle - angle) * math.cos(angle + math.pi/2)
    v2x_prime = ((m2 - m1) * v2x + 2 * m1 * v1x) / (m1 + m2) * math.cos(angle) + u2 * math.sin(velocity_angle2 - angle) * math.cos(angle + math.pi/2)
    v1y_prime = ((m1 - m2) * v1x + 2 * m2 * v2x) / (m1 + m2) * math.sin(angle) + u1 * math.sin(velocity_angle - angle) * math.sin(angle + math.pi/2)
    v2y_prime = ((m2 - m1) * v2x + 2 * m1 * v1x) / (m1 + m2) * math.sin(angle) + u2 * math.sin(velocity_angle2 - angle) * math.sin(angle + math.pi/2)
    
    # Convert the velocities back to the original coordinate system
    # v1x_prime = v1x_prime * math.cos(angle) + v1y * math.sin(angle)
    # v1y_prime = v1x_prime * -math.sin(angle) + v1y * math.cos(angle)
    # v2x_prime = v2x_prime * math.cos(angle) + v2y * math.sin(angle)
    # v2y_prime = v2x_prime * -math.sin(angle) + v2y * math.cos(angle)
    
    # Update the velocities of the circles
    # p1.velocity = Vector(v1x_prime, v1y_prime)
    # p2.velocity = Vector(v2x_prime, v2y_prime)
    b.set_vx(v1x_prime)
    b.set_vy(v1y_prime)
    b2.set_vx(v2x_prime)
    b2.set_vy(v2y_prime)
    # if (b2.y > b.y):
    #     b.set_y(b2.y - distance * math.cos(angle))
    #     b.set_x(b2.x - distance * math.sin(angle))