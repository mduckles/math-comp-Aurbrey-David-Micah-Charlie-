import numpy as np
import matplotlib.pyplot as plt
import time
import math
import statistics

def ElasticEnergy(k,dx):
    return (k*(dx)**2)/2

Payload_Weight = 1
class SlingShot():
    def __init__(self, Spring, Size, Angle):
        '''Spring is the spring constant of the Elastic part. Size is the length of the elastic. Angle is the angle of release'''
        self.Spring = Spring 
        self.Size = Size
        self.Angle = Angle

<<<<<<< HEAD
    def EnergyOutcome(self):
        '''Determines the ElasticPotential Energy of the slingshot at its maximum pulled distanc'''
=======
    def kineticOutcome(self):
        '''out puts the ElasticEnergy'''
>>>>>>> 2b85c80d80327e6fe7bbcfa39ae1435fd037df78
        maxPullConst = 3*(11*0.5) # Proportion between length of elastic and the distanc pulled. 
        DistancePulled = maxPullConst/self.Size
        return ElasticEnergy(self.Spring, DistancePulled)
    
<<<<<<< HEAD
    def ForceOutcome(self):
        '''Determines the Force of the object when it is pulled back in the slingshot'''
        return (2*(self.Spring * 4.5 * math.degrees(math.cos(math.asin(1/10)))))
=======

>>>>>>> 2b85c80d80327e6fe7bbcfa39ae1435fd037df78

Test1 = SlingShot(5, 10, 70)
print(Test1.kineticOutcome())
print(Test1.ForceCalc2())