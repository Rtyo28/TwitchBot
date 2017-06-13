class Units:

    def __init__(self):
        self.gold = 0
        self.wood = 0
        self.food = 0

    def changeGold(self, amount):
        self.gold += amount
        return self.gold

    def changeWood(self, amount):
        self.wood += amount
        return self.wood

    def changeFood(self, amount):
        self.food += amount
        return self.food

    def setTo(self, gold, wood, food):
        self.gold = gold
        self.wood = wood
        self.food = food
        return self.gold, self.wood, self.food

