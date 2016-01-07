class Card:
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

    def getName(self):
        return self.name

    def getStats(self):
        return self.stats

    def getValue(self, index):
        retun self.card[index]

    def __repr__(self):
        return("[" + self.card[0] +
               ", " + str(self.card[1]) +
               ", " + str(self.card[2]) +
               ", " + str(self.card[3]) +
               ", " + str(self.card[4]) +
               ", " + str(self.card[5]) + "]\n")
