# Example file showing a circle moving on screen
import pygame
import math
import random
from objects import *
from utils import *


# pygame setup
pygame.init()
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
mode = 0 # code for the different modes: 0 is bouncing balls, 1 is gravity simulation
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)
test_ball = GravityBall(10, 40, screen.get_width() / 2, screen.get_height() / 4, 0, 0, 0, G_0*FUDGE)
# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
bouncing_balls = []
balls_colors = []

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse click position
            x, y = pygame.mouse.get_pos()
            collides = False
            for ball in bouncing_balls:
                if check_collision(ball, GravityBall(10, 40, x, y, 0, 0, 0, 0)):
                    collides = True
                    continue
            if (not collides):
                bouncing_balls.append(GravityBall(10, 40, x, y, random.randint(-100, 100), random.randint(-100, -50), 0, G_0*FUDGE))
                balls_colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                screen.fill("cyan2")  # Fill the screen with cyan2 color
                bouncing_balls.clear()
            

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("cyan2")
    # time = pygame.time.get_ticks() / 1000
    # timer_text = my_font.render(str(math.trunc(time)), False, (0, 0, 0))
    # dt_text = my_font.render(str(math.trunc(dt)), False, (0, 0, 0))
    # mechanical_energy_text = my_font.render(str(round(calculate_mechanical_energy(test_ball, HEIGHT), 2)), False, (0, 0, 0))
    # screen.blit(timer_text, (0,0))
    # screen.blit(mechanical_energy_text, (0,50))
    # screen.blit(dt_text, (0,100))
    # calculate_position(test_ball, dt)
    # collision_handler(test_ball, HEIGHT)
    # pygame.draw.circle(screen, "red", pygame.Vector2(test_ball.get_x(), test_ball.get_y()), test_ball.get_radius())
    if (mode == 0):
        for i in range(len(bouncing_balls)):
            ball = bouncing_balls[i]
            color = balls_colors[i]
            calculate_position(ball, 0.016)
            collision_handler(ball, HEIGHT, WIDTH)
            j = i - 1
            while (j >= 0):
                # if (ball.get_x() - bouncing_balls[j].get_x() > ball.get_radius() + bouncing_balls[j].get_radius()):
                #     break
                if (check_collision(ball, bouncing_balls[j])):
                    ball_collision(ball, bouncing_balls[j])
                j -= 1
                    
            pygame.draw.circle(screen, color, pygame.Vector2(ball.get_x(), ball.get_y()), ball.get_radius())
            pygame.draw.circle(screen, (0, 0, 0), (ball.get_x(), ball.get_y()), ball.get_radius() + 1, width=2)

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     player_pos.y -= 300 * dt
    # if keys[pygame.K_s]:
    #     player_pos.y += 300 * dt
    # if keys[pygame.K_a]:
    #     player_pos.x -= 300 * dt
    # if keys[pygame.K_d]:
    #     player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()