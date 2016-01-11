
#Nick's card generator

import card
import random

class NickCardGenerator:
    def __init__(self, size, rnd):
        self.size = size
        self.stats = [0,0,0,0,0]
        self.name = rnd
        
    def getList(self):
        return self.stats
        
    def genCard(self):
        x = random.randint(1,10)
        y = random.randint(0, 10-x)
        indices = random.sample([0, 1, 2, 3, 4], 2)
        self.stats[indices[0]] = x
        self.stats[indices[1]] = y
        card1 = card.Card(self.name,self.stats)
        return card1

    def buildDeck(self):
        deck = []
        for i in range(0, self.size):
            deck.append(self.genCard())

        return deck

##    def main():
##
##        size = 40
##        deck = buildDeck(size)
##
##        for i in range(0, size):
##            print(deck[i])
##
##        print(deck[0].getValue(1))
##        print(deck[1].getName())
##        print(deck[39].getStats())
    
