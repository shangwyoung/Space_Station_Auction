import biddingAgent

class agent1(biddingAgent.biddingAgent):
    def __init__(self, cards, ID, players, budget):
        pass

    def getName(self):
        return "A"

    def getColor(self):
        return "red"

    def getBid(self, card, index):
        return 10

    def seeResults(self, card, winner, price, bids):
        print("agent1's result")
    
