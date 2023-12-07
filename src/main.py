# Example file showing a circle moving on screen
import pygame
import math
from objects import *
from utils import *

# pygame setup
pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)
# test_ball = GravityBall(10, 40, screen.get_width() / 2, screen.get_height() / 4, 0, 0, 0, G_0*FUDGE)
# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
test_sun = GravityBall(1e15, 40, screen.get_width() / 2, screen.get_height() / 2, 0, 0, 0, 0)
test_planet = GravityBall(1e5, 20, screen.get_width() / 2 + 100, screen.get_height() / 2, 0, 10, 0, 0)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("cyan2")
    time = pygame.time.get_ticks() / 1000
    # timer_text = my_font.render(str(math.trunc(time)), False, (0, 0, 0))
    # dt_text = my_font.render(str(math.trunc(dt)), False, (0, 0, 0))
    # mechanical_energy_text = my_font.render(str(round(calculate_mechanical_energy(test_ball, HEIGHT), 2)), False, (0, 0, 0))
    # screen.blit(timer_text, (0,0))
    # screen.blit(mechanical_energy_text, (0,50))
    # screen.blit(dt_text, (0,100))
    # calculate_position(test_ball, dt)
    # collision_handler(test_ball, HEIGHT)
    # pygame.draw.circle(screen, "red", pygame.Vector2(test_ball.get_x(), test_ball.get_y()), test_ball.get_radius())
    calculate_gravitational_force(test_sun, test_planet)
    calculate_position(test_sun, dt)
    calculate_position(test_planet, dt)
    planet_x_text = my_font.render(str(test_planet.get_x()), False, (0, 0, 0))
    screen.blit(planet_x_text, (0,0))
    planet_y_text = my_font.render(str(test_planet.get_y()), False, (0, 0, 0))
    screen.blit(planet_y_text, (0,50))
    pygame.draw.circle(screen, "orange", pygame.Vector2(test_sun.get_x(), test_sun.get_y()), test_sun.get_radius())
    pygame.draw.circle(screen, "blue", pygame.Vector2(test_planet.get_x(), test_planet.get_y()), test_planet.get_radius())

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