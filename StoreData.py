class points:
    user = []
    points = []

    def addUser(self, user, points):
        try:
            index = self.getIndex(user)
        except:
            index = -1

        if index < 0:
            self.user.append(user)
            self.points.append(points)
            return 'User ' + user + ' added with ' + str(points) + ' base points.'
        else:
            return 'User ' + user + ' already exists, and has ' + str(self.points[index]) + ' points.'

    def getIndex(self, find):
        index = self.user.index(find)
        return index

    def changePoints(self, user, difference):
        try:
            index = self.getIndex(user)
        except:
            index = -1

        if index >= 0:
            self.points[index] += difference
        else:
            print 'User ' + user + ' not found while attempting to change user points.'

    def returnPoints(self, user):
        try:
            index = self.getIndex(user)
        except:
            index = -1

        if index >= 0:
            return 'User ' + user + ' has ' + str(self.points[index]) + ' points.'
        else:
            return 'User ' + user + ' not found while attempting find points.'

    def saveData(self, filename):
        fileout = open(filename, 'w+')
        fileout.write('Username\tPoints\n')
        for u in self.user:
            i = self.getIndex(u)
            fileout.write(u + '\t\t' + str(self.points[i]) + '\n')

    def readData(self, filename):
        with open(filename) as f:
            lines = f.readlines()
        skip = 0
        for l in lines:
            if skip == 0:
                skip = 1
            else:
                line = str.split(l)
                self.addUser(line[0], int(line[1]))
