import card

class SpaceStation:
    # name and ID correspond to the player who is building the SpaceStation
    def __init__(self, agent):
        self.agent = agent
        self.cards = []
        #self.scores = [0,0,0,0,0]
        self.scores = []
        self.scores.append([0,0,0,0,0])
        self.budget = [1000]
        self.rankScore = 0

    def getAgent(self):
        return self.agent
    
    def getName(self):
        return self.agent.getName()

    def getColor(self):
        return self.agent.getColor()

    def getCards(self):
        return self.cards
 
    def getScores(self, r):
        return self.scores[r]
        #return self.scores
        
    def getFinalScore(self):
    	return self.scores[len(self.scores)-1]
        
    def getBudget(self, r):
    	return self.budget[r]
    	
    def getRank(self):
        return self.rankScore

    def incrementRankScore(self, amount):
        if amount > 0:
            self.rankScore += amount
 
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
