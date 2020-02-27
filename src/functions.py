from math import sqrt
from scipy.constants import k as K_B
from scipy.stats import maxwell
from essentials import Vector, Particle
from random import random
from database import WIDTH, HEIGHT

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



