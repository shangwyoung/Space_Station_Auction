
#Nick's card generator

import card
import random

def genCard():

    name = "name"
    stats = [0,0,0,0,0]

    x = random.randint(1,10)
    y = random.randint(0, 10-x)
    indices = random.sample([0, 1, 2, 3, 4], 2)
    stats[indices[0]] = x
    stats[indices[1]] = y

    card1 = card.Card(name,stats)
    return card1

def buildDeck(size):
    deck = []
    for i in range(0, size):
        deck.append(genCard())

    return deck

def main():

    size = 40
    deck = buildDeck(size)

    for i in range(0, size):
        print(deck[i])

    print(deck[0].getValue(1))
    print(deck[1].getName())
    print(deck[39].getStats())
    

main()
