import random
import biddingAgent

class RandomBiddingAgent(biddingAgent.biddingAgent):
    def __init__(self, cards, identification, budget, players):
        self.identification = identification
        self.budget = budget

    def getName(self):
        return "Random Bidding Agent"

    def getColor(self):
        return "Blue"

    def getBid(self, card, index):
        return random.randint(0, self.budget)

    def seeResults(card, winner, price, bids):
        if winner == self.identification:
            self.budget -= price
