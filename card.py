class Card:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

    def getName(self):
        return self.name

    def getStats(self):
        return self.stats

    def getValue(self, index):
        return self.stats[index]

    def __repr__(self):
        return("[" + self.name +
               ", " + str(self.stats[0]) +
               ", " + str(self.stats[1]) +
               ", " + str(self.stats[2]) +
               ", " + str(self.stats[3]) +
               ", " + str(self.stats[4]) + "]")
