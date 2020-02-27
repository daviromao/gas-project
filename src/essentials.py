from math import cos, sin, radians, sqrt
from random import random
from database import LENGHT_BALL

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

    def __str__(self):
        return str((self.x, self.y))

class Velocity(Vector):
    def __init__(self, x=0, y=0, module=0):
        super().__init__(x, y, module)
    
    def randomizeWithSpeed(self, speed):
        angle = radians(random()*360)
        self.x = cos(angle)*speed
        self.y = sin(angle)*speed

class Particle:
    def __init__(self, mass, speed, position=(0, 0), velocity=(0, 0), radius = LENGHT_BALL):
        self.mass = mass
        self.position = Vector(position[0], position[1])
        self.velocity = Velocity(velocity[0], velocity[1])
        self.speed = speed
        self.radius = radius
    
    def move(self, dt):

        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

        return self

    def randomizeVelocity(self):
        self.velocity.randomizeWithSpeed(self.speed)

        return self

    def distanceParticles(self, other):
        return self.position.manhattanDistance(other.position) <= LENGHT_BALL*2
    
    def collisionParticles(self, other):
        dX = abs(self.position.x - other.position.x)
        dY = abs(self.position.y - other.position.y)
        d = sqrt(dX*dX + dY*dY)

        return d <= self.radius + other.radius
    def positionVals(self):
        return (self.position.x, self.position.y)

    def __str__(self):
        return str(self.position) + " " + str(self.velocity)