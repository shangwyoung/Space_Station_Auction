import card
import random



def genCard(prefCount,placeCount,suffCount):
    #passed line counts
    def findWord(file):
        F= open(file, "r")
        if file== "prefixes.txt":
            length= prefCount
        if file== "places.txt":
            length= placeCount
        if file== "suffixes.txt":
            length= suffCount
        num= random.randint(0, length)
        for i, line in enumerate(F):
            if i==num:
                return line.strip()
    pref= findWord("prefixes.txt")
    place=findWord("places.txt")
    suff=findWord("suffixes.txt")
    name= (pref+" "+place+" "+suff)
    # generates name
    stats = [0,0,0,0,0]

    x = random.randint(1,10)
    y = random.randint(0, 10-x)
    indices = random.sample([0, 1, 2, 3, 4], 2)
    stats[indices[0]] = x
    stats[indices[1]] = y

    card1 = card.Card(name,stats)
    return card1

def buildDeck(size):
    def lineCount(file):
        i=0
        with open(file, "r") as F:
            for i, l in enumerate(F):
                pass
            return i
    # returns the number of lines-1
    prefCount= lineCount("prefixes.txt")
    placeCount= lineCount("places.txt")
    suffCount= lineCount("suffixes.txt")
    # determines the linecounts here so each file neads to to be gone through only once per deck
    deck = []
    for i in range(0, size):
        deck.append(genCard(prefCount,placeCount,suffCount))

    return deck
