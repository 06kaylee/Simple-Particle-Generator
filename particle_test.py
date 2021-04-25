import pygame, sys, random
from pygame.locals import *

# game setup
clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('Particle Generator')
screen = pygame.display.set_mode((500, 500), 0, 32)
 

 
# [location, velocity, timer]
particles = []
 

while True:
    # background
    screen.fill((0,0,0))

    mx, my = pygame.mouse.get_pos()
    
    particles.append([[mx, my], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 6)])
 
    for particle in particles:
        particle[0][0] += particle[1][0]    # adds random int for movement in the x direction
        particle[0][1] += particle[1][1]    # adds random int for movement in the y direction
        particle[2] -= 0.1      # subtract from the timer (how long the particle lasts)
        particle[1][1] += 0.1   # adding to the vertical velocity
        pygame.draw.circle(screen, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        # check if the timer ran out
        if particle[2] <= 0:
            particles.remove(particle)
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                

    pygame.display.update()
    clock.tick(60)