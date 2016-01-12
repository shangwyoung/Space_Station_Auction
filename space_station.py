import card

class SpaceStation:
    # name and ID correspond to the player who is building the SpaceStation
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.cards = []
        self.scores = [0,0,0,0,0]
        self.rankScore = 0

    def getName(self):
        return self.name

    def getID(self):
        return self.ID

    def getCards(self):
        return self.cards

    def getValue(self, index):
        return self.scores[index]

    def getScores(self):
        return self.scores

    def getRank(self):
        return self.rankScore

    def incrementRankScore(self, amount):
        if amount > 0:
            self.rankScore += amount

    # adds a card to the list of won cards and increases the scores of the
    # categories that appear on the card
    def addCard(self, card):
        self.cards.append(card)
        for i in range(0,5):
            x = card.getValue(i)
            self.scores[i] += x

    def __repr__(self):
        return(self.name + "'s Space Station: [" +
                str(self.scores[0]) + ", " +
                str(self.scores[1]) + ", " +
                str(self.scores[2]) + ", " +
                str(self.scores[3]) + ", " +
                str(self.scores[4]) + "]")
