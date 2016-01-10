import bidding_agent
import user_interface
import card
import random
import string
import os
import inspect
import importlib
import signal
from contextlib import contextmanager

class auctionSimulator:

    # Finds all classes in a directory that are subclasses of BiddingAgent
    def get_agents(directory = "."):
        modules = [file_name[:-3] for file_name in os.listdir(directory) if file_name.endswith('.py')]
        agents = []
        #add cheat detection
        for module_name in modules:
            module = __import__(module_name)
            for name, agent in inspect.getmembers(module, inspect.isclass):
                if agent not in agents and issubclass(agent, bidding_agent.BiddingAgent):
                    if agent != bidding_agent.BiddingAgent:
                    agents.append(agent)
    return agent_classes

    # Creates the BiddingAgent classes
    def make_agents(agents, cards, budget):
    agentClasses = [None]*len(agents)
    for i in range(len(agents)):
        with time_limit(5, i, "__init__"):
            agentClasses[i] = agents[i](cards, i, len(agents), budget)
    return agentClasses

    # For each round:
    # Generate the cards for a round of bidding (Can be random numbers and names)
    def generate_cards(num, round_number):
    cards = []
    for i in range(num):
        name = "".join(random.choice(string.ascii_letters) for i in range(10))
        cards.append(card.Card(name, random.randint(0, 8), random.randint(0, 8),
                          random.randint(0, 8), random.randint(0, 8),
                          random.randint(0, 8)))
    return cards


# Finds all classes in a directory that are subclasses of BiddingAgent
# Creates the BiddingAgent classes

# For each round:
# Generate the cards for a round of bidding (Can be random numbers and names)
# Call getBid for each BiddingAgent
# Call seeResults for each BiddingAgent after winner has been declared
# Calculate each BiddingAgent's scores
