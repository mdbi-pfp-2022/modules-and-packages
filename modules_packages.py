#%%

# use variable naming rules when creating
# new python modules
import greetings
# %%

import sys

for folder in sys.path:
    print(folder)

# %%

import joey
# %%
import time

num = 0

while num <= 500:
    print(num)
    num = num + 1
# %%
import math


def calculate_area(radius):
    return math.pi * radius ** 2


print(calculate_area(4))
print(calculate_area(2))
# %%

import greetings

greetings.greet_everybody()
# %%

from greetings import greet_everybody

greet_everybody()
# %%

# from greetings import greet_everybody
# from math import pi
# from json import load

import greetings

greetings.greet_everybody()
# %%

import greetings as g

g.greet_everybody()