import biddingAgent
import card
import card_generator
import space_station
import auction_gui
import sortSpaceStations

import user_interface
import random
import string
import os
import inspect
import importlib
import signal
from contextlib import contextmanager

# game constants
NUM_ROUNDS = 10
STARTING_BUDGET = 1000
CARDS_PER_AGENT = 5

# scoring constants
DOMINATE_POINTS = 1
HIGHEST_POINTS = 1

# this is useful for printing stuff
CATAGORIES = ["Science", "Ecology", "Culture", "Commerce", "Industry"]

#timeout exception: an exception for the purpose of cutting functions off
#if they run too long

##class TimeoutException(Exception): pass
##
###signal handler to handle sigalrm
##def signal_handler(signum, frame):
##    raise TimeoutException()
##
###fucntion to use to limit the time of other functions
###must be used in a with clause
##@contextmanager
##def time_limit(seconds, agent_id, function):
##    signal.setitimer(signal.ITIMER_REAL, seconds)
##    try:
##        yield
##    except TimeoutException:
##        UI.on_function_timed_out(agent_id, function)
##    finally:
##        signal.setitimer(signal.ITIMER_REAL, 0)


#finds all classes in the given directory that are subclasses
#of biddingAgent
def get_agent_classes(directory = "agents"):
    modules = [file_name[:-3] for file_name in os.listdir(directory) if file_name.endswith('.py')]
    agent_classes = []
    for module_name in modules:
        #module = __import__(module_name)
        module = importlib.import_module(directory + "." +  module_name)
        for name, agent in inspect.getmembers(module, inspect.isclass):
            if agent not in agent_classes and issubclass(agent, biddingAgent.biddingAgent):
                if agent != biddingAgent.biddingAgent:
                    agent_classes.append(agent)
    return agent_classes


#creates a bidding agent for each bidding agent class
#
#returns a list of these agents
#
#params: a list of classes, a list of cards, and a budget
#this id of an agent will be its position in the list
def make_bidding_agents(agent_classes, cards, budget):
    agents = [None]*len(agent_classes)     
    for i in range(len(agent_classes)):
        #with time_limit(5, i, "__init__"):
            agents[i] = agent_classes[i](cards, i, len(agent_classes), budget)
            print(agents[i].getName())
    return agents

#make space stations for each agent
def make_space_stations(agents):
    stations = [None]*len(agents)     
    for i in range(len(agents)):
        agent = agents[i]
        #name = agent.getName()
        #with time_limit(5, i, "__init__"):
        stations[i] = space_station.SpaceStation(agent)
        #print(stations[i].getName())
        #print(stations[i].getID())
    GUI.add_stations(stations)
    return stations

#params: the round number, the card being bid on
def get_bids(card, index, agents, budgets):
    UI.on_auction_started(card)
    bids = [];
    
    for i in range(len(agents)):
        bid = 0
        if agents[i]:
            #with time_limit(.1,i, "getBid"):
                bid = agents[i].getBid(card, index)
        
        if type(bid) != int:
            bid = 0
            UI.on_illegal_bid_received(i, "type")
        elif bid > budgets[i]:
            bid = 0
            UI.on_illegal_bid_received(i, "budget")
            
        UI.on_bid_received(card, i, bid)
        
        bids.append((i, bid))
    return bids
    

#gives out the results of a round of bids
#bids is a list of tuples, (id, bid)
def give_results(bids, agents, card, budgets):
    bids = sorted(bids, key = lambda x: x[1], reverse = True)
    winner = bids[0][0]
    price = bids[1][1]
    
    #keep track of budgets
    budgets[winner] -= price
    
    #sort by agent
    bids = sorted(bids, key = lambda x: x[0])
    formatted_bids = [x[1] for x in bids]
    for i in range(len(agents)):
        if agents[i]:
            #with time_limit(.1, i, "seeResults"):
                agents[i].seeResults(card, winner, price, formatted_bids)

    GUI.update_price(price)
    
    UI.on_auction_finished(card, winner, price)
    return winner

def sort_stations(stations):
    sorter = sortSpaceStations.SortSpaceStations()
    sortedstations = sorter.sort_stations(stations)
    return sortedstations
            
def main():
    print("hi")

    global GUI
    GUI = auction_gui.AuctionGUI(180, 190)
    GUI.initialize_graphics()
    #GUI.add_stations(1)
    #set signal handler so we can use SIGALRM to enforce time limits
    #signal.signal(signal.SIGALRM, signal_handler)
    
    #build UI. It is global because I got sick of passing it into every function
    global UI
    UI = user_interface.user_interface()
    
    #set up game
    agent_classes = get_agent_classes()
    
    UI.on_game_started([x.__name__ for x in agent_classes])
    num_agents = len(agent_classes)

    #set up card generator

    
    cards = card_generator.buildDeck(NUM_ROUNDS)
    GUI.add_deck(cards)

    
    
    #for rnd in range(NUM_ROUNDS):
        
        #set up round
        #cards = generate_cards(num_agents*CARDS_PER_AGENT, rnd)
        #cards = card_generator.buildDeck()
    UI.on_round_started(NUM_ROUNDS, cards)
    
    agents = make_bidding_agents(agent_classes, cards, STARTING_BUDGET);
    space_stations = make_space_stations(agents)
    #GUI.add_stations(space_stations)
    budgets = [STARTING_BUDGET for agent in agents]
    cards_won = {}
    
    #do bidding
    for i in range(len(cards)):
        bids = get_bids(cards[i], i, agents, budgets)
        winner = give_results(bids, agents, cards[i], budgets)
        
        for j in range (len(space_stations)):
            if j == winner:
                b = agents[j].getBudget()
                space_stations[j].addCard(cards[i])
                space_stations[j].addBudget(b)
            else:
                space_stations[j].passround()
            
        
        if winner in cards_won:
            cards_won[winner].append(cards[i])
        else:
            cards_won[winner] = [cards[i]]
        GUI.update_round(bids, winner, space_stations)
    
    
    #do scoring
    print("about to ssort")
    stations_copy = []
    for i in range (len(space_stations)):
        stations_copy.append(0)
    #for i in range (len(space_stations)):
        stations_copy[i] = space_stations[i]
    sortedstations = sort_stations(stations_copy)
    GUI.add_results(sortedstations)
    
 

    UI.on_game_finished()
    for i in range(num_agents):
        print(str(space_stations[i].getName())+": "+str(space_stations[i].getScores(NUM_ROUNDS)[0])
             +" "+str(space_stations[i].getScores(NUM_ROUNDS)[1])
             +" "+str(space_stations[i].getScores(NUM_ROUNDS)[2])
             +" "+str(space_stations[i].getScores(NUM_ROUNDS)[3])
             +" "+str(space_stations[i].getScores(NUM_ROUNDS)[4]))
        print(space_stations[i].getRank())
    #for i in range(num_agents):
        #print(str(space_stations[i].getName())+space_stations[i].getScores(NUM_ROUNDS))
    GUI.root.mainloop()

main()
    

#if __name__ == '__main__':
#    main()


# Finds all classes in a directory that are subclasses of BiddingAgent
# Creates the BiddingAgent classes

# For each round:
# Generate the cards for a round of bidding (Can be random numbers and names)
# Call getBid for each BiddingAgent
# Call seeResults for each BiddingAgent after winner has been declared
# Calculate each BiddingAgent's scores
