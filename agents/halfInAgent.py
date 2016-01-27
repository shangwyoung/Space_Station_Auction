import biddingAgent

class HalfInAgent(biddingAgent.biddingAgent):
    def __init__(self, cards, ID, players, budget):
        self.ID=ID
        self.budget = budget

    def getName(self):
        return "Half In"

    def getColor(self):
        return "#eceb7b"

    def getBid(self, card, index):
        return (self.budget)//2

    def seeResults(self, card, winner, price, bids):
        if winner == self.ID:
            self.budget -= price

    def getBudget(self):
        return self.budget
