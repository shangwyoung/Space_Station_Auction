import biddingAgent

class agent1(biddingAgent.biddingAgent):
    def __init__(self, cards, ID, players, budget):
        self.ID=ID
        self.budget = budget

    def getName(self):
        return "All In"

    def getColor(self):
        return "#24ee93"

    def getBid(self, card, index):
        return self.budget

    def seeResults(self, card, winner, price, bids):
        if winner == self.ID:
            self.budget -= price
            
    def getBudget(self):
    	return self.budget
    
