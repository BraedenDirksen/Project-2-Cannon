"""
title: functions
"""


def inputs():
    return input()

def convint(a):
    try:
        a = int(a)
        return a
    except ValueError:
        print("please enter a correct value ")
        return convint(a)