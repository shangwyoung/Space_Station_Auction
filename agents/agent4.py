import biddingAgent

class agent4(biddingAgent.biddingAgent):
    def __init__(self, cards, ID, players, budget):
        pass

    def getName(self):
        return "D"

    def getColor(self):
        return "green"

    def getBid(self, card, index):
        return 5000

    def seeResults(self, card, winner, price, bids):
        print("agent4's result")
    
