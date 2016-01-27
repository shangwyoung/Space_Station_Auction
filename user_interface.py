#User Interface class
#Sam Rossin
#fall 2015

#User interface class. Should be rewritten to make the UI happen, with the same methods
#Current functions are stubs.
#import auctionSimulator

class user_interface:
    #anything do initialize the UI should be here
    def __init__(self):
        self.agents = None
        self.winners = None
    
    #called when the agents are first listed by the auction simulator
    #passes a list of the names of the agents (in order of ID)
    #agents will always be referred to by ID after this, so we
    #can use this list for reference if we need names.
    #note that this only passes strings, as we should never need to access actual agent objects from the UI
    def on_game_started(self, agents):
        self.agents = agents
        self.winners = [0]*len(agents)
        
    #signifies the beginning of a round
    #cards is the list of cards for this round, in order they will be auctioned
    def on_round_started(self, rnd_number, cards):
        print("Starting round", rnd_number)
        
    #called when a card is auctioned off
    def on_auction_started(self, card):
        print("\nBidding on: ", card)
    
    #called when a bid is recieved from an agent
    def on_bid_received(self, card, agent_id, bid):
        print(self.agents[agent_id], "bid", bid)
    
    #called when a card is done being auctioned off
    def on_auction_finished(self, card, winner_id, price):
        print(self.agents[winner_id], " won", card.getName(), "at a price of", price)
    
    #called when a round has finished
    #scores is a list of the final score of each agent (in order of ID)
    #domiations is a list of tuples ids, where each tuple means the first agent dominated the second agent:
    #       that is [(1, 0), (2,1)] means agent 1 dominated agent 0, and agent 2 dominated agent 1
    #catagories is a list of the 5 individual catagory winners (again these are agent ids)
    #       in the order listed in auction_simulator.CATAGORIES
    def on_round_finished(self,scores, dominations, catagories):
        CATAGORIES = ["C1", "C2", "C3", "C4", "C5"]
        print("\nCalculating Scores:")
        for d in dominations:
            print("Agent", d[0], "dominated agent", d[1])
        for i in range(len(catagories)):
            print("Agent", catagories[i], "was best in", CATAGORIES[i])
            
        print("\nFinal Scores:")
        print(scores)
        
        maxx = 0
        max_index = -1
        for i in range(len(scores)):
            if scores[i] > maxx:
                maxx = scores[i]
                max_index = i
        self.winners[max_index]+=1
        print(self.agents)
            
        
    #called when someone submits an illegal bid. Currently does nothing, but might be useful
    #the reason parameter can currently be "type" which means the bid wasn't an int,
    #   or  "budget" which means they bid more than their remaining budget.
    #illegal bids are automatically set to 0 (so on_bid_received will be called immediatly after this
    #   with a value of 0)
    def on_illegal_bid_received(self, agent_id, reason):
        print(self.agents[agent_id], "made an illegal bid:", reason)
        
    #called when the game is finished
    #this function has no parameters, since all the information has already been
    #passed to the ui.
    #additionally, I don't know how we will want to agregate the scores between rounds,
    #   so when that it decided, it can be done here, or auction_simulater can be modified
    #   to do it, and then a parameter can be added to this function to pass the info
    def on_game_finished(self):
        print("\nThe game is over! The number of wins per agent was:")
        print(self.winners)
        print(self.agents)
        
        
    #called when a function runs for too long.
    #the parameter function can be "getBid", "seeResults", and "__init__"
    #note that the consequences for the offending player for they offenses are:
    #   "getBid" -- they bid 0
    #   "seeResults" -- no consequences: they just miss out on information potentially
    #   "__init__" -- disqualified for the round (they bid 0 for whole round)
    def on_function_timed_out(self, agent_id, function):
        print(self.agents[agent_id], "timed out on function", function)
