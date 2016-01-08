class biddingAgent:

    def __init__(self): #what args do we need?
        pass

    # Give the name that will be displayed for your agent
    # @returns Your player name
    def getName(self):
        pass

    # Give the color of your agent name
    # @returns Your agent color
    def getColor(self):
        pass

    # 5 sec time limit
    # init will be called once per agent at the beginning of an auction
    # to provide the details of the contest and to allow time (limited)
    # for pre-processing. Note that agents must keep track of their own budget.
    # @param cards The list of all cards to be auctioned
    # @param ID Your agent's index
    # @param players The total number of players
    # @param budget Starting budget
    def init(self, cards, ID, players, budget):
        pass

    # Called for each auctioned card. Give your bid for the current card
    # @param card The next card (object) up for auction
    # @param index The index of the card in the auction
    # @returns An integer bid between 0 and your remaining budget
    def getBid(self, card, index):
        pass

    # Used by the system to inform your agent of the results of each auction
    # Record any useful information and update your budget if you won.
    # @param The now sold card
    # @param winner The bidding agent that won the card
    # @param price The price the winner paid for the card
    # @param bids A list of all bids made by all agents, ordered by agent IDs
    def seeResults(self, card, winner, price, bids):
        pass

    def __repr__(self):
        return self.__class__.__name__
    
