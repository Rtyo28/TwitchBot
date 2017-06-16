import numpy
import random
from TwitchBot.BuildingFactory import *

filename = 'land01.txt'
fileout = 'LandOutput.txt'

with open(filename) as f:
    lines = f.readlines()

i = 0
j = 0

map = numpy.array([0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0])

wildTypes = ['forest', 'river', 'grassland']

outFile = open(fileout, "w")

for x in range(5):
    spaces = str.split(lines[i])
    for y in range(5):
        temp = spaces[i]
        if temp == 'R':
            map[i, j] = Residence()
        elif temp == 'F':
            map[i, j] = Farm()
        elif temp == 'L':
            map[i, j] = Lumbermill()
        else:
            map[i, j] = random.choice(wildTypes)
        j += 1
    i += 1

