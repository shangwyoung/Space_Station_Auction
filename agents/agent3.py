import biddingAgent

class agent3(biddingAgent.biddingAgent):
    def __init__(self, cards, ID, players, budget):
        pass

    def getName(self):
        return "C"

    def getColor(self):
        return "green"

    def getBid(self, card, index):
        return 100

    def seeResults(self, card, winner, price, bids):
        print("agent3's result")
    
