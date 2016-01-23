from tkinter import *
import card_generator
import card
import space_station
#import auctionSimulator

class AuctionGUI():
    
    def __init__(self, width, height):
        self.wide = width
        self.high = height
        self.bids = []
        self.winner = []
        self.stations = []
        self.round = 0
        self.price = []
        self.display = []
        #self.deck = card_generator.buildDeck(40)

    def initialize_graphics(self):

        # ROOT WINDOW
        self.root = Tk()
        self.root.title("Space Station Auction!")

        # *LEFT PANEL*
        self.left = Frame(self.root)
        self.left.pack(side=LEFT, fill=BOTH, expand=1)

        # bid result history
        self.bid_history = Frame(self.left)
        self.bid_history.pack(side=TOP, fill=X)

        self.S = Scrollbar(self.bid_history)
        self.T = Text(self.bid_history, height=4, bg="black", fg="green",
                      state=DISABLED)
        self.S.pack(side=RIGHT, fill=Y)
        self.T.pack(side=LEFT, fill=X, expand=1)
        self.S.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.S.set)

        # canvas for player info, graph, etc
        self.graph = Canvas(self.left, bg="black", scrollregion=[0,0,2592,1728])

        self.img = PhotoImage(file="background.gif")
        self.graph.create_image(0,0, anchor=NW, image=self.img)

        self.graph.pack(side=TOP, fill=BOTH, expand=1)

        self.graph_scroll = Scrollbar(self.left, orient=HORIZONTAL,
                command=self.graph.xview)
        self.graph_scroll.pack(side=TOP, fill=X)
        self.graph.config(xscrollcommand=self.graph_scroll.set)

        # buttons
        self.buttons = Frame(self.left, bg="grey", bd=5)
        self.buttons.pack(side=BOTTOM, fill=X)

        self.play_pause_button = Button(self.buttons, bg="#33ff33", text="PLAY",
                                        width=10, activebackground="green")
        self.step_button = Button(self.buttons, bg="#ffff33", text="STEP",
                                  width=10, command=self.step, activebackground="yellow")
        self.quit_button = Button(self.buttons, bg="#ff3333", text="QUIT",
                                  width=10, command=self.root.destroy, activebackground="red")
        self.info_button = Button(self.buttons, bg="grey", text="?",
                                  width=5, activebackground="#ff3333")

        self.play_pause_button.pack(side=LEFT)
        self.step_button.pack(side=LEFT, padx=20)
        self.quit_button.pack(side=LEFT)
        self.info_button.pack(side=RIGHT)

        # *RIGHT PANEL*
        self.right = Frame(self.root)
        self.right.pack(side=RIGHT, fill=Y)

        # current card
        self.current = Canvas(self.right, width =(self.wide+10),
                              height=(self.high+10), bg="black")
        self.current.pack(side=TOP)

        #card queue
        self.queue = Canvas(self.right, width=(self.wide+10), bg="black")
        self.queue.pack(side=TOP, fill=Y, expand=1)

    def step(self):
        self.draw_card()
        self.update_queue()
        self.update_info()

    # I think this method should probably take card as an arg instead of
    # searching the deck within the method, but we can discuss this
    def draw_card(self):
        if len(self.deck)>0:
            self.card = self.deck[0]
            """
            for rounded card later

            self.current.create_arc(5,5,17,17, start=90, extent=90, outline="white")
            self.current.create_arc(173,5,185,17, start=0, extent=90, style=ARC, outline="white")
            self.current.create_arc(173,178,185,195, start=270, extent=90, style=ARC, outline="white")
            self.current.create_arc(5,178,17,195, start=180, extent=90, style=ARC, outline="white")
            """
            self.current.create_rectangle(5,5,190,200, fill="#19334d", outline="#00e5e6", width=10)
            self.current.create_text(95,20, anchor=N, fill="#00e5e6", width =150,
                        text=self.card.getName(), font=("Helvetica", "16"),
                        justify=CENTER)
            self.current.create_text(95,150, anchor=N, fill="#00e5e6", width =150,
                        text="[" + str(self.card.getValue(0)) +
                   ", " + str(self.card.getValue(1)) +
                   ", " + str(self.card.getValue(2)) +
                   ", " + str(self.card.getValue(3)) +
                   ", " + str(self.card.getValue(4)) + "]", 
                        font=("Helvetica", "16"),
                        justify=CENTER)
            self.deck.remove(self.deck[0])

    def add_history(self, message):
        self.T.config(state=NORMAL)
        self.T.insert(END, "\n" + message)
        self.T.see(END)
        self.T.config(state=DISABLED)

    def update_queue(self):
        #first card in queue
        if len(self.deck)>0:
            
            card1=self.deck[0]
            self.queue.create_rectangle(5, 5, 190, 100, fill="#19334d", outline="#00e5e6", width=3)
            self.queue.create_text(95, 15, anchor=N, fill="#00e5e6", width = 150,
                        text="[NEXT 1] "+card1.getName(), font=("Helvetica", "13"),
                        justify=CENTER)
            self.queue.create_text(95,80, anchor=N, fill="#00e5e6", width =150,
                        text="[" + str(card1.getValue(0)) +
                   ", " + str(card1.getValue(1)) +
                   ", " + str(card1.getValue(2)) +
                   ", " + str(card1.getValue(3)) +
                   ", " + str(card1.getValue(4)) + "]", 
                        font=("Helvetica", "13"),
                        justify=CENTER)
        else:
            self.queue.create_rectangle(5, 5, 190, 100, fill="#000000", outline="#000000", width=3)
        #second card in queue
        if len(self.deck)>1:
            card2 = self.deck[1]
            self.queue.create_rectangle(5, 105, 190, 200, fill="#19334d", outline="#00e5e6", width=3)
            self.queue.create_text(95, 115, anchor=N, fill="#00e5e6", width = 150,
                        text="[NEXT 2] "+card2.getName(), font=("Helvetica", "13"),
                        justify=CENTER)
            self.queue.create_text(95,180, anchor=N, fill="#00e5e6", width =150,
                        text="[" + str(card2.getValue(0)) +
                   ", " + str(card2.getValue(1)) +
                   ", " + str(card2.getValue(2)) +
                   ", " + str(card2.getValue(3)) +
                   ", " + str(card2.getValue(4)) + "]", 
                        font=("Helvetica", "13"),
                        justify=CENTER)
        else:
            self.queue.create_rectangle(5, 105, 190, 200, fill="#000000", outline="#000000", width=3)

    def update_info(self):
        #delete current price and card
        if len(self.display)>0:
            for i in range (len(self.display)):
                self.graph.delete(self.display[i])
        if len(self.bids)>0:
            #update bidding price
            bids = self.bids[0]
            winner = self.winner[0]
            price = self.price[0]
            stations = self.stations[1]
            self.bids.remove(self.bids[0])
            self.winner.remove(self.winner[0])
            self.price.remove(self.price[0])
            self.stations.remove(self.stations[1])
            for i in range (len(bids)):
                self.display.append(self.graph.create_text(45+85*i, 110, anchor=N, fill="#00e5e6", width = 75,
                        text="$"+str(bids[i][1]), font=("Helvetica", "12"),
                        justify=CENTER))
            
            #give card to the winner   
            self.display.append(self.graph.create_rectangle(5+85*winner, 5, 85+85*winner, 60, fill="#19334d", outline="#00e5e6", width=3))
            self.display.append(self.graph.create_text(45+85*winner, 40, anchor=N, fill="#00e5e6", width = 75,
                        text="[" + str(self.card.getValue(0)) +
                       ", " + str(self.card.getValue(1)) +
                       ", " + str(self.card.getValue(2)) +
                       ", " + str(self.card.getValue(3)) +
                       ", " + str(self.card.getValue(4)) + "]", font=("Helvetica", "12"),
                        justify=CENTER))
            self.display.append(self.graph.create_text(45+85*winner, 20, anchor=N, fill="#00e5e6", width = 75,
                        text="$"+str(price), font=("Helvetica", "12"),
                        justify=CENTER))
            self.add_history("'"+stations[winner].getName()+"' won '"+self.card.getName()+"' for $"+str(price))

            #update total scores
            for i in range (len(stations)):
                self.display.append(self.graph.create_text(45+85*i, 240, anchor=N, fill="#00e5e6", width = 75,
                        text=stations[i].getScores(self.round), font=("Helvetica", "12"),
                        justify=CENTER))
                
            #update budgets
            for i in range (len(stations)):
                self.display.append(self.graph.create_text(45+85*i, 195, anchor=N, fill="#00e5e6", width = 75,
                        text="$"+str(stations[i].getBudget(self.round)), font=("Helvetica", "12"),
                        justify=CENTER))


            self.round += 1            
                       

    def add_stations(self, stations):
        if len(self.stations) == 0:
            self.stations.append(stations)
            #agent info
            self.graph.create_rectangle(5, 100, 85, 170, fill="#19334d", outline="#00e5e6", width=3)
            self.graph.create_text(45, 130, anchor=N, fill="#00e5e6", width = 75,
                            text=self.stations[0][0].getName(), font=("Helvetica", "12"),
                            justify=CENTER)
            self.graph.create_rectangle(90, 100, 170, 170, fill="#19334d", outline="#00e5e6", width=3)
            self.graph.create_text(130, 130, anchor=N, fill="#00e5e6", width = 75,
                            text=self.stations[0][1].getName(), font=("Helvetica", "12"),
                            justify=CENTER)
            self.graph.create_rectangle(175, 100, 255, 170, fill="#19334d", outline="#00e5e6", width=3)
            self.graph.create_text(215, 130, anchor=N, fill="#00e5e6", width = 75,
                            text=self.stations[0][2].getName(), font=("Helvetica", "12"),
                            justify=CENTER)
            self.graph.create_rectangle(260, 100, 340, 170, fill="#19334d", outline="#00e5e6", width=3)
            self.graph.create_text(300, 130, anchor=N, fill="#00e5e6", width = 75,
                            text=self.stations[0][3].getName(), font=("Helvetica", "12"),
                            justify=CENTER)
            #station info - unchanged
            self.graph.create_rectangle(5, 165, 85, 270, fill="#19334d", outline="#00e5e6", width=3)
            self.graph.create_text(45, 175, anchor=N, fill="#00e5e6", width = 75,
                            text="Budget: ", font=("Helvetica", "12"),
                            justify=CENTER)
            self.graph.create_text(45, 220, anchor=N, fill="#00e5e6", width = 75,
                            text="Total Scores: ", font=("Helvetica", "12"),
                            justify=CENTER)
            
            self.graph.create_rectangle(90, 165, 170, 270, fill="#19334d", outline="#00e5e6", width=3)
            self.graph.create_text(130, 175, anchor=N, fill="#00e5e6", width = 75,
                            text="Budget: ", font=("Helvetica", "12"),
                            justify=CENTER)
            self.graph.create_text(130, 220, anchor=N, fill="#00e5e6", width = 75,
                            text="Total Scores: ", font=("Helvetica", "12"),
                            justify=CENTER)
            
            self.graph.create_rectangle(175, 165, 255, 270, fill="#19334d", outline="#00e5e6", width=3)
            self.graph.create_text(215, 175, anchor=N, fill="#00e5e6", width = 75,
                            text="Budget: ", font=("Helvetica", "12"),
                            justify=CENTER)
            self.graph.create_text(215, 220, anchor=N, fill="#00e5e6", width = 75,
                            text="Total Scores: ", font=("Helvetica", "12"),
                            justify=CENTER)
            
            self.graph.create_rectangle(260, 165, 340, 270, fill="#19334d", outline="#00e5e6", width=3)
            self.graph.create_text(300, 175, anchor=N, fill="#00e5e6", width = 75,
                            text="Budget: ", font=("Helvetica", "12"),
                            justify=CENTER)
            self.graph.create_text(300, 220, anchor=N, fill="#00e5e6", width = 75,
                            text="Total Scores: ", font=("Helvetica", "12"),
                            justify=CENTER)
            #station info - to be changed
            
            
        else:
            self.stations.append(stations)

    #def update_info(self):
        

    def add_deck(self, deck):
        self.deck = deck

        
    def update_round(self, bids, winner, space_stations):
        self.bids.append(bids)
        self.winner.append(winner)
        self.stations.append(space_stations)

    def update_price(self, price):
        self.price.append(price)
        
"""
def main():
    gui = AuctionGUI(180, 190)
    gui.initialize_graphics()
    gui.add_stations(1)
    gui.add_history("player5 won 'Puppy Cloning Center' for $100")
    gui.add_history("There was a tie for best bid, but player2 won 'Defensive Weapons Array' for $85")
    gui.add_history("player2 won 'Emergency Escape Pod' for $95")
    gui.add_history("player7 won 'Oxygen Farm' for $300")
    gui.add_history("player0 won 'Interstellar Party Beacon' for $250")
    gui.root.mainloop()

main()"""
