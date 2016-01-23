from tkinter import *
import card_generator
import card

class AuctionGUI():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.deck = card_generator.buildDeck(100)
        self.icons = [] #initialized below
        self.colors = ['cyan','#8cff1a','#ff66ff','yellow','#ff6666']
        #experimental
        self.borders =['','cyan','#00b1b3','#3333ff','#009933','purple','grey','','#8cff1a','','yellow','','red','','','magenta','','','','', 'orange']

    def initialize_graphics(self):

        # ROOT WINDOW
        self.root = Tk()
        self.root.title("Space Station Auction!")

        # Icons!
        self.science = PhotoImage(file="science.gif")
        self.ecology = PhotoImage(file="ecology.gif")
        self.culture = PhotoImage(file="culture.gif")
        self.commerce = PhotoImage(file="commerce.gif")
        self.industry = PhotoImage(file="industry.gif")
        self.icons.append(self.science)
        self.icons.append(self.ecology)
        self.icons.append(self.culture)
        self.icons.append(self.commerce)
        self.icons.append(self.industry)

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

        self.img = PhotoImage(file="background.ppm")
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
                                  width=5, relief=GROOVE)

        self.play_pause_button.pack(side=LEFT)
        self.step_button.pack(side=LEFT, padx=20)
        self.quit_button.pack(side=LEFT)
        self.info_button.pack(side=RIGHT)

        # bindings for [?] button
        self.info_button.bind('<Enter>', self.legend)
        self.info_button.bind('<Leave>', self.remove_legend)

        # *RIGHT PANEL*
        self.right = Frame(self.root, bd=0)
        self.right.pack(side=RIGHT, fill=Y)

        # current card
        self.current = Canvas(self.right, width =(self.width),
                              height=(self.height), bg="black", bd=0)
        self.current.pack(side=TOP)

        #card queue
        self.queue = Canvas(self.right, width=(self.width), bg="black", bd=0)
        self.queue.pack(side=TOP, fill=Y, expand=1)

    def step(self):
        self.add_history(self.deck[0].getName() + " is now current. (TEST)")
        self.advance_queue()

    # I think this method should probably take card as an arg instead of
    # searching the deck within the method, but we can discuss this -NM
    def draw_card(self, card):
        # consider seperate method for this (duplicated in draw_cardlet) or a card method.
        num = 0
        index1 = 0
        index2 = 0
        for i in range (0, len(card.getStats())):
            if card.getValue(i) > 0:
                num += 1
                if num == 1:
                    index1 = i
                else:
                    index2 = i
        self.create_rounded(self.current, 0,0,180,190, 30, 1, "#202060", self.borders[(index1+1)*(index2+1)])# old color is "#ffc34d"
        self.create_rounded(self.current, 10,10,170,180, 20, 0, "#202060", "#202060")
        self.current.create_text(90,20, anchor=N, fill=self.borders[(index1+1)*(index2+1)], width =150,
                                text=card.getName(), font=("Helvetica", "16"),
                                justify=CENTER)
        
        if num == 1:
            self.current.create_image(78,150, anchor=W, image=self.icons[index1])
            self.current.create_text(76, 150, anchor=E, text=card.getValue(index1),
                                     font=("Helvetica", "22"), fill=self.colors[index1])
        else:
            self.current.create_image(38,150, anchor=W, image=self.icons[index1])
            self.current.create_text(36, 150, anchor=E, text=card.getValue(index1),
                                     font=("Helvetica", "22"), fill=self.colors[index1])
            self.current.create_image(118,150, anchor=W, image=self.icons[index2])
            self.current.create_text(116, 150, anchor=E, text=card.getValue(index2),
                                     font=("Helvetica", "22"), fill=self.colors[index2])
                    

    # draws a reduced version of a card which only has the symbols and colors
    def draw_cardlet(self, card, index):
        num = 0
        index1 = 0
        index2 = 0
        for i in range (0, len(card.getStats())):
            if card.getValue(i) > 0:
                num += 1
                if num == 1:
                    index1 = i
                else:
                    index2 = i
        y = index*78
        self.create_rounded(self.queue, 0,y,180,76+y, 30, 1, "#202060", self.borders[(index1+1)*(index2+1)])
        self.create_rounded(self.queue, 10,10+y,170,66+y, 20, 0, "#202060", "#202060")
        
        if num == 1:
            self.queue.create_image(78,38+y, anchor=W, image=self.icons[index1])
            self.queue.create_text(76, 38+y, anchor=E, text=card.getValue(index1),
                                     font=("Helvetica", "22"), fill=self.colors[index1])
        else:
            self.queue.create_image(38,38+y, anchor=W, image=self.icons[index1])
            self.queue.create_text(36, 38+y, anchor=E, text=card.getValue(index1),
                                     font=("Helvetica", "22"), fill=self.colors[index1])
            self.queue.create_image(118,38+y, anchor=W, image=self.icons[index2])
            self.queue.create_text(116, 38+y, anchor=E, text=card.getValue(index2),
                                     font=("Helvetica", "22"), fill=self.colors[index2])

    # draws a black box over the cardlet at the given index
    def erase_cardlet(self, index):
        y = index*78
        self.queue.create_rectangle(0,y,190,70+y, 30, 0, "black", "black")

    # adds a new line of text to the bid history window
    def add_history(self, message):
        self.T.config(state=NORMAL)
        self.T.insert(END, "\n" + message)
        self.T.see(END)
        self.T.config(state=DISABLED)

    # draws the next card in the stack, removes it, and draws the remaining queue
    def advance_queue(self):
        if self.deck:
            card = self.deck[0]
            self.draw_card(card)
            self.deck.remove(self.deck[0])
            self.queue.delete(ALL)
            for i in range(0, len(self.deck)):
                self.draw_cardlet(self.deck[i], i)

    def update_info(self):
        pass

    # draws the legend which shows the icons for each of the 5 categories
    def legend(self, event):
        width = self.graph.winfo_width()
        height = self.graph.winfo_height()
        x1 = width-self.width-5
        y1 = height-self.height-5
        x2 = width-5
        y2 = height-5
        self.a = self.graph.create_rectangle(x1,y1,x2,y2, fill="grey", width=5)
        self.b = self.graph.create_text((x2-100), y1+(self.height*(1/6)), text="Science", anchor=W, font=("Helvetica", "12", "bold"))
        self.c = self.graph.create_text((x2-100), y1+(self.height*(2/6)), text="Ecology", anchor=W, font=("Helvetica", "12", "bold"))
        self.d = self.graph.create_text((x2-100), y1+(self.height*(3/6)), text="Culture", anchor=W, font=("Helvetica", "12", "bold"))
        self.e = self.graph.create_text((x2-100), y1+(self.height*(4/6)), text="Commerce", anchor=W, font=("Helvetica", "12", "bold"))
        self.f = self.graph.create_text((x2-100), y1+(self.height*(5/6)), text="Industry", anchor=W, font=("Helvetica", "12", "bold"))

        self.g = self.graph.create_oval((x2-150), y1+(self.height*(1/6))-10, (x2-130), y1+(self.height*(1/6))+10, fill="blue")
        self.h = self.graph.create_oval((x2-150), y1+(self.height*(2/6))-10, (x2-130), y1+(self.height*(2/6))+10, fill="green")
        self.i = self.graph.create_oval((x2-150), y1+(self.height*(3/6))-10, (x2-130), y1+(self.height*(3/6))+10, fill="purple")
        self.j = self.graph.create_oval((x2-150), y1+(self.height*(4/6))-10, (x2-130), y1+(self.height*(4/6))+10, fill="yellow")
        self.k = self.graph.create_oval((x2-150), y1+(self.height*(5/6))-10, (x2-130), y1+(self.height*(5/6))+10, fill="red")

    # removes all the canvas objects that make up the legend
    def remove_legend(self, event):
        self.graph.delete(self.a,self.b,self.c,self.d,self.e,
                          self.f,self.g,self.h,self.i,self.j,
                          self.k)

    # draws a rounded rectangle. Format: (canvas, x1,y1,x2,y2, corner radius, border width, fill color)
    def create_rounded(self, canvas, x1, y1, x2, y2, r, w, o, f):
        canvas.create_arc(x1, y1, x1+r, y1+r, start=90, extent=90, style=PIESLICE, width=w, outline=o, fill=f)
        canvas.create_arc(x2-r, y1, x2, y1+r, start=0, extent=90, style=PIESLICE, width=w, outline=o, fill=f)
        canvas.create_arc(x1, y2-r, x1+r, y2, start=180, extent=90, style=PIESLICE, width=w, outline=o, fill=f)
        canvas.create_arc(x2-r, y2-r, x2, y2, start=270, extent=90, style=PIESLICE, width=w, outline=o, fill=f)
        
        canvas.create_line(x1+r/2, y1, x2-r/2, y1, width=w, fill=o)
        canvas.create_line(x1, y1+r/2, x1, y2-r/2, width=w, fill=o)
        canvas.create_line(x1+r/2, y2, x2-r/2, y2, width=w, fill=o)
        canvas.create_line(x2, y1+r/2, x2, y2-r/2, width=w, fill=o)

        canvas.create_rectangle(x1+r/2-w/2, y1+w/2, x2-r/2+w/2, y2-w/2, fill=f, width=0)
        canvas.create_rectangle(x1+w/2, y1+r/2-w/2, x2-w/2, y2-r/2+w/2, fill=f, width=0)
        
        
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
