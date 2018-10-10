"""
title: functions
"""


def inputs():
    return input()

def convint(a):
    try:
        a = int(a)
    except ValueError:
        print("please enter a correct value ")
        return inputs()