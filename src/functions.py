from math import sqrt
from scipy.constants import k
from scipy.stats import maxwell
from essentials import vector, particle
from random import random
from database import height, width

def atomicMassToSI(mu):
     return (mu / 6.022e+26)

def generateParticles(n, mass, temperature):
    mkg = atomicMassToSI(mass)
    a = sqrt((k*T)/mkg)

    particles = map(lambda: return Particle(mass, temperature), range(n))

def randomizeParticles(particles, a):
    for i in range(len(particles)):
        speed = maxwell.rvs(scale=a)
        particles[i].velocity.randomizeWithScalar(speed)

        equalsPosition = True
        while(equalsPosition):
            
            equalsPosition = False
            particles[i].position.setCoords(random()*width, random()*height)

            for j in range(i):
                if(particles[i].distanceParticles(particles[j])):
                    equalsPosition = True
    


