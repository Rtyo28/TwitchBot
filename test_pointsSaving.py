from StoreData import points

players = points()

players.readData('pointsFile')

print players.addUser('john', 0)
print players.addUser('James', 1000)
print players.addUser('RUKO', -420)

print players.returnPoints('RUKO')

players.changePoints('RUKO', -6969)

print players.returnPoints('RUKO')

players.changePoints('ayy', 5945)

print players.returnPoints('ayy')

players.saveData('pointsFile')