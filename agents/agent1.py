import biddingAgent

class agent1(biddingAgent.biddingAgent):
    def __init__(self, cards, ID, players, budget):
        self.ID=ID
        self.budget = budget

    def getName(self):
        return "A"

    def getColor(self):
        return "yellow"

    def getBid(self, card, index):
        return 5000

    def seeResults(self, card, winner, price, bids):
        if winner == self.ID:
            self.budget -= price
            
    def getBudget(self):
    	return self.budget
    
