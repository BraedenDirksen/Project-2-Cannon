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
        return round(distance, 2)

def scen2calc(a, b):
        speedh = (a * math.cos(math.radians(b)))
        speedv = (a * math.sin(math.radians(b)))
        heightpeak = (speedv ** 2) / 9.81
        timepeak = speedv / 9.81
        totaldist = round(speedh * timepeak * 2, 2)
        return totaldist

def scen3calc(a, b, c):
        speedh = (a * math.cos(math.radians(b)))
        speedv = (a * math.sin(math.radians(b)))
        heightpeak = (speedv ** 2) / (9.81 * 2)
        timepeak = speedv / 9.81
        totalheight = heightpeak + c
        timefall = ((totalheight * 2) / 9.81) ** 0.5
        totaltime = timefall + timepeak
        totaldist = round(speedh * totaltime, 2)
        return totaldist




