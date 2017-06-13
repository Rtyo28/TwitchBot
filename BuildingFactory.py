class Residence:

# A residence next to another residence increases production by 5

    def __init__(self):
        self.cost = 50
        self.production = 10
        self.type = 'gold'

    def setProduction(self, north, south, east, west):
        self.production = 10
        if north == 'residence':
            self.production += 5
        if south == 'residence':
            self.production += 5
        if east == 'residence':
            self.production += 5
        if west == 'residence':
            self.production += 5

class Farm:

# A farm next to river increases production by 5

    def __init__(self):
        self.cost = 10
        self.production = 10
        self.type = 'food'

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


class Lumbermill:

# A Lumbermill next to forest increases production by 5

    def __init__(self):
        self.cost = 50
        self.production = 10
        self.type = 'wood'

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

