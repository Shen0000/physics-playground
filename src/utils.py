from objects import *
# physics constants

FUDGE = 25 # fudge factor to make animations more realistic
G_0 = 9.80665

# physics functions

def calculate_position(ball, time, dt):
    ball.set_vx(ball.get_vx0() + time * ball.get_ax())
    #ball.set_vy(ball.get_vy0() + time * ball.get_ay())
    ball.set_vy(ball.get_vy() + dt * ball.get_ay())
    ball.set_x(ball.get_x0() + ball.get_vx0() * time + ball.get_ax() * time * time / 2)
    # ball.set_y(ball.get_y0() + ball.get_vy0() * time + ball.get_ay() * time * time / 2)
    ball.set_y(ball.get_y() + ball.get_vy() * dt + ball.get_ay() * dt * dt / 2)