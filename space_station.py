import card

class SpaceStation:
    # name and ID correspond to the player who is building the SpaceStation
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.cards = []
        #self.scores = [0,0,0,0,0]
        self.scores = []
        self.scores.append([0,0,0,0,0])
        self.budget = []
        self.budget.append(1000)

    def getName(self):
        return self.name
 
    def getID(self):
        return self.ID
 
    def getCards(self):
        return self.cards
 
    def getScores(self, r):
        return ("["+str(self.scores[r][0])+" "+str(self.scores[r][1])+" "+str(self.scores[r][2])+" "+str(self.scores[r][3])+" "+str(self.scores[r][4])+"]")
        #return self.scores
        
    def getBudget(self, r):
    	return self.budget[r]
 
    # adds a card to the list of won cards and increases the scores of the
    # categories that appear on the card
    def addCard(self, card):
        l = len(self.scores)-1
        self.cards.append(card)
        a=self.scores[l][0]
        b=self.scores[l][1]
        c=self.scores[l][2]
        d=self.scores[l][3]
        e=self.scores[l][4]
        self.scores.append([a,b,c,d,e])
        for i in range(0,5):
            self.scores[l+1][i] += card.getValue(i)
    
    def addBudget(self, budget):
    	self.budget.append(budget)
        
    def passround(self):
        l = len(self.scores)-1
        a=self.scores[l][0]
        b=self.scores[l][1]
        c=self.scores[l][2]
        d=self.scores[l][3]
        e=self.scores[l][4]
        self.scores.append([a,b,c,d,e])
        b = self.budget[len(self.budget)-1]
        self.budget.append(b)
 
##    def __repr__(self):
##        return(self.name + "'s Space Station: [" +
##               str(self.scores[0]) + ", " +
##               str(self.scores[1]) + ", " +
##               str(self.scores[2]) + ", " +
##               str(self.scores[3]) + ", " +
##               str(self.scores[4]) + "]")
