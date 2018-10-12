"""
title: functions
"""
import math

def inputs():
    return input()

def convint(a):
    try:
        a = int(a)
        return a
    except ValueError:
        print("please enter a correct value ")
        return convint(inputs())



def scen1calc(a, b):
        time = ((b * 2) / 9.81) ** 0.5
        distance = time * a
        return distance

def scen2calc(a, b):
    speedh = (a * math.cos(math.radians(b)))
    speedv = (a * math.sin(math.radians(b)))
    timepeak = speedv / 9.81
    distance = timepeak * speedv * 2
    