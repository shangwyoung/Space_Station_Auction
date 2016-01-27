import random
import biddingAgent

class ProportionalBiddingAgent(biddingAgent.biddingAgent):
    def __init__(self, cards, ID, players, budget):
        self.ID = ID
        self.budget = budget
        self.total = 0

        for card in cards:
            self.total += sum(card.getStats())

    def getName(self):
        return "Proportional"

    def getColor(self):
        return "#fe7329"

    # def init(self, cards, ID, players, budget):
    #    pass

    def getBid(self, card, index):
        cardVal = sum(card.getStats())
        return (self.budget*cardVal)//self.total

    def seeResults(self, card, winner, price, bids):
        self.total -= sum(card.getStats())
        if winner == self.ID:
            self.budget -= price
            
    def getBudget(self):
    	return self.budget

    def __repr__(self):
        return self.__class__.__name__
