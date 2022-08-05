import numpy as np
import matplotlib.pyplot as plt
import time
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

    def kineticOutcome(self):
        '''out puts the ElasticEnergy'''
        maxPullConst = 3*(11*0.5) # Proportion between length of elastic and the distanc pulled. 
        DistancePulled = maxPullConst/self.Size
        return ElasticEnergy(self.Spring, DistancePulled)
    


Test1 = SlingShot(5, 10, 70)
print(Test1.kineticOutcome())
