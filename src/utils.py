from math import sqrt
from scipy.constants import k as K_B
from scipy.stats import maxwell
from classes import Particle
from random import random
from settings import WIDTH, HEIGHT, LENGHT_BALL

def atomicMassToSI(mu):
     return (mu / 6.022e+26)

def generateParticles(n, atomicMass, temperature):
    mkg = atomicMassToSI(atomicMass)
    a = sqrt((K_B*temperature)/mkg)

    speeds = maxwell.rvs(scale=a, size=n)

    particles = list(map(lambda speed: Particle(mkg, speed), speeds))
    particles = list(map(lambda particle: particle.randomizeVelocity(), particles))

    for i in range(len(particles)):
        equalsPosition = True
        while(equalsPosition):
            equalsPosition = False
            particles[i].position.setCoords(random()*WIDTH, random()*HEIGHT)

            for j in range(i):
                if(particles[i].distanceParticles(particles[j])):
                    equalsPosition = True

    return particles

def collideWall(particle):
    if(particle.position.x + LENGHT_BALL > WIDTH):
        particle.position.x = WIDTH-LENGHT_BALL
        particle.velocity.x *= -1

    elif(particle.position.x - LENGHT_BALL < 0):
        particle.position.x = LENGHT_BALL
        particle.velocity.x *= -1

    elif(particle.position.y + LENGHT_BALL > HEIGHT):
        particle.position.y = HEIGHT-LENGHT_BALL
        particle.velocity.y *= -1

    elif(particle.position.y - LENGHT_BALL < 0):
        particle.position.y = LENGHT_BALL
        particle.velocity.y *= -1

def checkCollision(particle1, particle2, dt):
    if(particle1.position.manhattanDistance(particle2.position) <= 20):
        velocityAux = particle1.velocity
        particle1.velocity = particle2.velocity
        particle2.velocity = velocityAux

        particle1.move(0.002 * dt)
        particle2.move(0.002 * dt)