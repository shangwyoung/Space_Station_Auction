from tkinter import *
import card_generator
import card

class AuctionGUI():
    
    def __init__(self, width, height):
        self.wide = width
        self.high = height
        self.deck = card_generator.buildDeck(40)

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
        if self.deck[0]:
            card = self.deck[0]
            """
            for rounded card later

            self.current.create_arc(5,5,17,17, start=90, extent=90, outline="white")
            self.current.create_arc(173,5,185,17, start=0, extent=90, style=ARC, outline="white")
            self.current.create_arc(173,178,185,195, start=270, extent=90, style=ARC, outline="white")
            self.current.create_arc(5,178,17,195, start=180, extent=90, style=ARC, outline="white")
            """
            self.current.create_rectangle(5,5,190,200, fill="#19334d", outline="#00e5e6", width=10)
            self.current.create_text(95,20, anchor=N, fill="#00e5e6", width =150,
                        text=card.getName(), font=("Helvetica", "16"),
                        justify=CENTER)
            self.current.create_text(95,150, anchor=N, fill="#00e5e6", width =150,
                        text="[" + str(card.getValue(0)) +
                   ", " + str(card.getValue(1)) +
                   ", " + str(card.getValue(2)) +
                   ", " + str(card.getValue(3)) +
                   ", " + str(card.getValue(4)) + "]", 
                        font=("Helvetica", "16"),
                        justify=CENTER)
            self.deck.remove(self.deck[0])

    def add_history(self, message):
        self.T.config(state=NORMAL)
        self.T.insert(END, "\n" + message)
        self.T.see(END)
        self.T.config(state=DISABLED)

    def update_queue(self):
        pass

    def update_info(self):
        pass
        

def main():
    gui = AuctionGUI(180, 190)
    gui.initialize_graphics()
    gui.add_history("player5 won 'Puppy Cloning Center' for $100")
    gui.add_history("There was a tie for best bid, but player2 won 'Defensive Weapons Array' for $85")
    gui.add_history("player2 won 'Emergency Escape Pod' for $95")
    gui.add_history("player7 won 'Oxygen Farm' for $300")
    gui.add_history("player0 won 'Interstellar Party Beacon' for $250")
    gui.root.mainloop()

main()
