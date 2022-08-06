from re import M
import numpy as np
import matplotlib.pyplot as plt
import time
import math
import statistics

def ElasticEnergy(k,dx):
    return (k*(dx)**2)/2


class SlingShot():
    def __init__(self, Spring, Size, Angle):
        '''Spring is the spring constant of the Elastic part. Size is the length of the elastic. Angle is the angle of release'''
        self.Spring = Spring 
        self.Size = Size
        self.Angle = Angle

    def EnergyOutcome(self):
        '''Determines the ElasticPotential Energy of the slingshot at its maximum pulled distanc'''
        maxPullConst = (99**0.5)/2 # Proportion between length of elastic and the distanc pulled. 
        DistancePulled = self.Size/maxPullConst
        return ElasticEnergy(self.Spring, DistancePulled)
    
    def ForceOutcome(self):
        '''Determines the Force of the object when it is pulled back in the slingshot'''
        return (2*(self.Spring * 4.5 * math.degrees(math.cos(math.asin(1/10)))))
    
    def VelocityLaunch(self, mass):
        '''Assuming velocity is linear '''
        Vel = (((99**0.5)**0.5) * (4.477**0.5) * (self.Spring**0.5) * self.Size)/ (mass**0.5)
        return Vel

    def MassOfVel(self, TargetVel):
        return (99**0.5) * 4.477 * self.Spring * (self.Size**2) / TargetVel**2



escapeVel = 11200
size = 828//((99**0.5)/2)
BigSlingshot = SlingShot(81.75 * size/0.24, size, 70)
Mass = BigSlingshot.MassOfVel(escapeVel)
print(f'The mass of our object is {Mass} when the length of the elastic slingshot is {size} ')
