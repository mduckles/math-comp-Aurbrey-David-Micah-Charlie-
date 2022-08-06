import numpy as np
import matplotlib.pyplot as plt
import time
import math
import statistics
#Importing any modules we may need

class SlingShot():
    '''The class of our slingshot object. Contains the models for calculating our mass'''
    def __init__(self, Spring, Size, Angle):
        '''Spring is the spring constant of the Elastic part. Size is the length of the elastic. Angle is the angle of release'''
        self.Spring = Spring 
        self.Size = Size
        self.Angle = Angle
    
    def VelocityLaunch(self, mass):
        '''A model for calculating the velocity of the object based on the calculations done on paper'''
        Vel = (((99**0.5)**0.5) * (4.477**0.5) * (self.Spring**0.5) * self.Size)/ (mass**0.5)
        return Vel

    def MassOfVel(self, TargetVel):
        '''Rearranged value of the previous model that we can plug in the escape velocity'''
        return (99**0.5) * 4.4775 * self.Spring * (self.Size**2) / TargetVel**2



escapeVel = 11200
# The escape velocity in m/s
size = 828/((99**0.5)/2)
# The length of the elastic band
BigSlingshot = SlingShot(81.75 * size/0.24, size, 70)
# Imputting the information into the object
Mass = BigSlingshot.MassOfVel(escapeVel)
# Calculating the mass based on the escape velocity
print(f'The mass of our object is {Mass} when the length of the elastic slingshot is {round(size, 3)}, when fired stright up ')

'''70 Degree Launch'''

size70deg = 828/((99**0.5)/2 * math.sin(math.radians(70)))
# The maximum length of the elastic band when pulled at a 70 degree angle
BigAngledSlingshot = SlingShot(81.75 * size70deg/0.24, size70deg, 70)
# Imputting the new information into the object
Mass70deg = BigAngledSlingshot.MassOfVel(escapeVel)
# Calculating the mass of the object when fired at 70 degrees from our model
print(f'The mass of our object is {Mass70deg} when the length of the elastic slingshot is {round(size70deg, 3)}, when fired at an angle of 70 degrees')
