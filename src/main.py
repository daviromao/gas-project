import pygame
from pygame.locals import *
from database import elements
from utils import generateParticles, collideWall, checkCollision
from settings import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f'{PROJECT_NAME} - {ELEMENT} - {TEMPERATURE}K')

muElement = float(elements[ELEMENT])
particles = generateParticles(PARTICLES_NUMBER, muElement, TEMPERATURE)

clock = pygame.time.Clock()

while True:
    dt = clock.tick(144)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.fill(WHITE)

    for particle in particles: pygame.draw.circle(screen, BLUE, (int(particle.position.x), int(particle.position.y)), LENGHT_BALL)

    for i in range(len(particles)):
        particles[i].move(0.001 * dt)
        collideWall(particles[i])

    for i in range(len(particles)-2):
        for j in range(i+1,len(particles)):
            checkCollision(particles[i], particles[j], dt)


    pygame.display.update()
