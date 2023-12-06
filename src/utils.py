from objects import *
# physics constants

FUDGE = 25 # fudge factor to make animations more realistic
G_0 = 9.80665

# Environment variables
LOSS = 0.5 # collisions will lose x% energy

# physics functions

def calculate_position(ball, dt):
    # ball.set_vx(ball.get_vx0() + time * ball.get_ax())
    #ball.set_vy(ball.get_vy0() + time * ball.get_ay())
    # ball.set_x(ball.get_x0() + ball.get_vx0() * time + ball.get_ax() * time * time / 2)
    # ball.set_y(ball.get_y0() + ball.get_vy0() * time + ball.get_ay() * time * time / 2)
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