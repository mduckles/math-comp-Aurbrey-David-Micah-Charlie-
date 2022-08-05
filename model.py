import numpy as np
import matplotlib.pyplot as plt
import time
import statistics

def ElasticEnergy(k,dx):
    return (k*(dx)**2)/2

Payload_Weight = 1
class SlingShot():
    def __init__(self, Spring, Size, Angle):
        self.Spring = Spring 
        self.Size = Size
        self.Angle = Angle

    def kineticOutcome(self):
        return ElasticEnergy(self.Spring, self.Size)


