# Example file showing a circle moving on screen
import pygame
import math
from objects import *
from utils import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)
test_ball = GravityBall(10, screen.get_width() / 2, screen.get_height() / 4, 0, 0, 0, G_0*FUDGE)
# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("cyan2")
    time = pygame.time.get_ticks() / 1000
    text_surface = my_font.render(str(math.trunc(time)), False, (0, 0, 0))
    screen.blit(text_surface, (0,0))
    calculate_position(test_ball, time, dt)
    w, h = pygame.display.get_surface().get_size()
    if (test_ball.get_y() >= h):
        print("test")
        v_i = test_ball.get_vy()
        test_ball.set_vy(-v_i)
    pygame.draw.circle(screen, "red", pygame.Vector2(test_ball.get_x(), test_ball.get_y()), 40)

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
    dt = clock.tick(120) / 1000

pygame.quit()