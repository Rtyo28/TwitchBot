class Residence:

# A residence next to another residence increases production by 5

    def __init__(self):
        self.cost = 50
        self.production = 10
        self.type = 'gold'
        self.name = 'Residence'

    def setProduction(self, north, south, east, west):
        self.production = 10
        if north == 'R':
            self.production += 5
        if south == 'R':
            self.production += 5
        if east == 'R':
            self.production += 5
        if west == 'R':
            self.production += 5
        return self.production, self.type

    def getName(self):
        return self.name

    def getProduction(self):
        return self.production

    def getCost(self):
        return self.cost

class Farm:

# A farm next to river increases production by 5

    def __init__(self):
        self.cost = 10
        self.production = 10
        self.type = 'food'
        self.name = 'Farm'

    def setProduction(self, north, south, east, west):
        self.production = 10
        if north == 'river':
            self.production += 5
        if south == 'river':
            self.production += 5
        if east == 'river':
            self.production += 5
        if west == 'river':
            self.production += 5
        return self.production, self.type

    def getName(self):
        return self.name

    def getProduction(self):
        return self.production

    def getCost(self):
        return self.cost

class Lumbermill:

# A Lumbermill next to forest increases production by 5

    def __init__(self):
        self.cost = 50
        self.production = 10
        self.type = 'wood'
        self.name = 'Lumbermill'

    def setProduction(self, north, south, east, west):
        self.production = 10
        if north == 'forest':
            self.production += 5
        if south == 'forest':
            self.production += 5
        if east == 'forest':
            self.production += 5
        if west == 'forest':
            self.production += 5
        return self.production, self.type

    def getName(self):
        return self.name

    def getProduction(self):
        return self.production

    def getCost(self):
        return self.cost

