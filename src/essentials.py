from math import cos, sin, radians
from random import random

class Vector:
    def __init__(self, x=0, y=0, module=0):
        self.x = float(x)
        self.y = float(y)
        self.module = module
    
    def setCoords(self, x, y):
        self.x = x
        self.y = y

    def manhattanDistance(self, vetor):  
        return abs(self.x - vetor.x) + abs(self.y - vetor.y)

class Velocity(Vector):
    def __init__(self, x=0, y=0, module=0):
        super(x, y, module)
    
    def randomizeWithSpeed(self, speed):
        angle = radians(random()*360)
        self.x = cos(angle)*speed
        self.y = sin(angle)*speed

class Particle:
    def __init__(self, mass, temperature, position=(0, 0), velocity=(0, 0), radius = 1):
        self.mass = mass
        self.temperature = temperature
        self.position = Vector(position[0], position[1])
        self.velocity = Vector(velocity[0], velocity[1])
        self.radius = radius
    
    def distanceParticles(self, other):
        return self.position.manhattanDistance(other.position) < self.radius
    
