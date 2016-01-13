# This is very incomplete, but I hoped to at least outline some kind framework
# That we can build on. Have a look at critter_gui.py to see what I have been
# refering to.

from tkinter import *
import card

class AuctionGUI():

    def __init__(self, model, gui_functions, defaults, scale, num_bidders):
        self.model = model #is this the same as master?
        self.gui_functions = gui_functions #"secure all the gui functions"
        self.SCALE_FACTOR = scale #simpler way to deal with various screen sizes
        self.num_bidders = num_bidders #number of players
        self.is_running = False #keep track of whether the auction is running
        self.budget = 100.00 #starting budget
        self.initialize_graphics(1)# 1 is temporary...
        self.root.mainloop() #keep window open unti auction ends or its closed

    def initialize_graphics(self, defaults):
        # GUI Window
        self.root = Tk()
        self.root.title("Space Station Auction")
        self.root.minsize(width=800, height=600) #get from defaults perhaps?

        # Left Panel (card list)
        self.left = Frame(self.root)
        self.left.pack(side=LEFT, fill=Y)

        self.left_header = Message(self.left, text="MODULES", bd=5, bg="#666699",
                                  relief=RAISED, width=100, fg="white")
        self.left_header.pack(side=TOP, fill=X)

        self.cards = Message(self.left, text="temporary", bd=5, bg="#ccccff", anchor=NW,
                        relief=RIDGE)
        self.cards.pack(side=TOP, fill=BOTH, expand=1)

        # Middle Panel (card/graph display and buttons)...maybe buttons seperate?
        self.middle = Frame(self.root)
        self.middle.pack(side=LEFT, fill=BOTH, expand=1)

        self.canvas = Canvas(self.middle)
        self.background = PhotoImage(file='background.gif')
        self.canvas.create_image(0,0, anchor=NW, image=self.background)
        self.canvas.pack(fill=BOTH, expand=1)

        # Buttons
        self.play_pause_button = Button(self.middle, text="START", bg="green")
        self.next_button = Button(self.middle, text="NEXT", bg="yellow")
        self.quit_button = Button(self.middle, text="RESET", bg="red")
        self.info_button = Button(self.middle, text="?")

        self.play_pause_button.pack(side=LEFT, fill=X, expand=1)
        self.next_button.pack(side=LEFT, fill=X, expand=1)
        self.quit_button.pack(side=LEFT, fill=X, expand=1)
        self.info_button.pack(side=LEFT, fill=X, expand=1)

        # Right Panel (player list)
        self.right = Frame(self.root)
        self.right.pack(side=RIGHT, fill=Y)

        self.right_header = Message(self.right, text="BIDDERS", bd=5, bg="#666699", anchor=NW,
                                   relief=RAISED, width=100, fg="white")
        self.right_header.pack(side=TOP, fill=X)

        self.players = Message(self.right, text="temporary", bd=5, bg="#ccccff", anchor=NW,
                               relief=RIDGE)
        self.players.pack(side=TOP, fill=BOTH, expand=1)
                                   
    """
    def make_buttons(self):

    def bind_keys(self):

        # Key Bindings for different actions (when we have them)

        self.root.bind("<Escape>", lambda *args: exit())

    def play_pause(self):

        #stop or start the auction

    def next_card(self):
    """
    # not working. there is a special thing we need to do with the gui functions becuase once
    # it is initialized, it just stays in its own loop. There is a method to correct this
    # in the critter lab that I am trying to figure out. Feel free to try and implement
    # this if you see how it works.
    def draw_card(self, card):
        
        self.canvas.create_rectangle(15,15,320,420, fill="#00e5e6", outline="#19334d", width=5)
        self.canvas.create_rectangle(35,35,300,400, fill="#19334d")
        self.canvas.create_text(168,50, anchor=N, fill="#00e5e6", width=230,
                            text=card.getName(), font=("Helvetica", "26"),
                            justify=CENTER)

    """
    def draw_graph(self):

    def update_graph(self):

    def update_bidders(self):

    def update_cards(self):
    """

def main(): #for testing purposes
    gui = AuctionGUI(1,1,1,1,1)
    card1 = card.Card("Radiation Treatment Center", [1,5,0,0,0])
    gui.draw_card(card1) #testing draw_card

main()
