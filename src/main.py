import pygame
from database import WIDTH, HEIGHT
from functions import generateParticles

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ideal Gas')

particles = generateParticles(30, 120, 298.15)

squares = list(map(lambda particle: pygame.Rect(particle.position.x, particle.position.y, 5, 5), particles))

clock = pygame.time.Clock()

while True:

    dt = clock.tick(100)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.fill(BLACK)

    for square in squares: pygame.draw.rect(screen, WHITE, square)
    for i in range(len(squares)):
        velocity_x = particles[i].velocity.x
        velocity_y = particles[i].velocity.y
        squares[i].move_ip(velocity_x* 0.001 * dt, velocity_y * 0.001 * dt)

    pygame.display.update()
