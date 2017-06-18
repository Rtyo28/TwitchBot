import numpy
import random
from TwitchBot.BuildingFactory import *

filename = 'land01.txt'
fileout = 'LandOutput.txt'

with open(filename) as f:
    lines = f.readlines()

map = numpy.array([['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0']])

wildTypes = ['forest', 'river', 'grassland']

outFile = open(fileout, "w")

for x in range(5):
    spaces = str.split(lines[x])
    for y in range(5):
        temp = spaces[y]
        if temp == 'R':
            map[x, y] = Residence().getName()
            outFile.write('R ')
        elif temp == 'F':
            map[x, y] = Farm().getName()
            outFile.write('F ')
        elif temp == 'L':
            map[x, y] = Lumbermill().getName()
            outFile.write('L ')
        else:
            temp2 = random.choice(wildTypes)
            print(temp2)
            map[x, y] = temp2
            outFile.write(map[x, y] + ' ')
    outFile.write('\n')

gold = 0
wood = 0
food = 0

for x in range(5):
    for y in range(5):
        if map[x, y] == 'R':
            if x < 1:
                north = 'null'
            else:
                north = map[x-1, y]

            if x > 3:
                south = 'null'
            else:
                south = map[x+1, y]

            if y < 1:
                west = 'null'
            else:
                west = map[x, y-1]

            if y > 3:
                east = 'null'
            else:
                east = map[x, y+1]

            amt, type = Residence.setProduction(Residence(), north, south, east, west)
            print(str(amt) + ' ' + type + '\n')
            gold += amt
print(gold)