import biddingAgent

class agent2(biddingAgent.biddingAgent):
    def __init__(self, cards, ID, players, budget):
        pass

    def getName(self):
        return "B"

    def getColor(self):
        return "green"

    def getBid(self, card, index):
        return 50

    def seeResults(self, card, winner, price, bids):
        print("agent2's result")
    
