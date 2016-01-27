import biddingAgent

class AverageAgent(biddingAgent.biddingAgent):
    def __init__(self, cards, ID, players, budget):
        self.ID=ID
        self.budget = budget
        self.numRounds = 0
        self.totalBid = 0

    def getName(self):
        return "Average"

    def getColor(self):
        return "#7b26d9"

# Bids the average of all previous winning bids
    def getBid(self, card, index):
        if (self.numRounds == 0):
            return 0
        currBid = self.totalBid//self.numRounds
        return min(currBid, self.budget)

    def seeResults(self, card, winner, price, bids):
        if winner == self.ID:
            self.budget -= price
        self.totalBid += price
        self.numRounds += 1

    def getBudget(self):
        return self.budget
