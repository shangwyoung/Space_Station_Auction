from tkinter import *
import card_generator
import card
import space_station
<<<<<<< HEAD
=======
import time
#import auctionSimulator
>>>>>>> master

class AuctionGUI():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
<<<<<<< HEAD
        self.deck = card_generator.buildDeck(100)
=======
        self.bids = []
        self.winner = []
        self.stations = []
        self.round = 0
        self.price = []
        self.display = []
        self.deck = card_generator.buildDeck(10) #for testing

>>>>>>> master
        self.icons = [] #initialized below
        self.colors = ['cyan','#8cff1a','#ff66ff','yellow','#ff6666']
        #experimental
        self.borders =['','cyan','#00b1b3','#3333ff','#009933','purple','grey','','#8cff1a','','yellow','','red','','','magenta','','','','', 'orange']
<<<<<<< HEAD
=======
      
>>>>>>> master

    def initialize_graphics(self):

        # ROOT WINDOW
        self.root = Tk()
        self.root.title("Space Station Auction!")
<<<<<<< HEAD

=======
        
>>>>>>> master
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
<<<<<<< HEAD
        self.graph = Canvas(self.left, bg="black", scrollregion=[0,0,2592,1728])
=======
        self.graph = Canvas(self.left, bg="black", scrollregion=[0,0,2592,1728], width=800, height=600)
>>>>>>> master

        self.img = PhotoImage(file="background.ppm")
        self.graph.create_image(0,0, anchor=NW, image=self.img)

        self.graph.pack(side=TOP, fill=BOTH, expand=1)

<<<<<<< HEAD
        # graph scrollbar
        """
        self.graph_scroll = Scrollbar(self.left, orient=HORIZONTAL,
                command=self.graph.xview)
        self.graph_scroll.pack(side=TOP, fill=X)
        self.graph.config(xscrollcommand=self.graph_scroll.set)
        """

=======
>>>>>>> master
        # buttons
        self.buttons = Frame(self.left, bg="grey", bd=5)
        self.buttons.pack(side=BOTTOM, fill=X)

        self.play_pause_button = Button(self.buttons, bg="#33ff33", text="PLAY",
                                        width=10, activebackground="green")
        self.step_button = Button(self.buttons, bg="#ffff33", text="STEP",
                                  width=10, command=self.step, activebackground="yellow")
        self.quit_button = Button(self.buttons, bg="#ff3333", text="QUIT",
                                  width=10, command=self.root.destroy, activebackground="red")
        self.legend_button = Button(self.buttons, bg="grey", text="LEGEND",
                                  width=7, relief=GROOVE)

        self.play_pause_button.pack(side=LEFT)
        self.step_button.pack(side=LEFT, padx=20)
        self.quit_button.pack(side=LEFT)
        self.legend_button.pack(side=RIGHT)
<<<<<<< HEAD

=======
        
>>>>>>> master
        # bindings for [?] button
        self.legend_button.bind('<Enter>', self.legend)
        self.legend_button.bind('<Leave>', self.remove_legend)

        # *RIGHT PANEL*
<<<<<<< HEAD
        self.right = Frame(self.root, bd=0)
        self.right.pack(side=RIGHT, fill=Y)

        # current card
        self.current = Canvas(self.right, width =(self.width),
                              height=(self.height), bg="black", bd=0)
        self.current.pack(side=TOP)

        #card queue
        self.queue = Canvas(self.right, width=(self.width), bg="black", bd=0)
        self.queue.pack(side=TOP, fill=Y, expand=1)


        # TESTING ONLY
        self.station1 = space_station.SpaceStation("Super-Station", 12345)
        self.station1.addCard(self.deck[0])
        self.station1.addCard(self.deck[1])
        self.station1.addCard(self.deck[2])
        self.station1.addCard(self.deck[3])
        self.station1.addCard(self.deck[4])
        self.station1.addCard(self.deck[5])
        self.station1.addCard(self.deck[6])
        self.station1.addCard(self.deck[7])
        self.station1.addCard(self.deck[8])
        self.station1.addCard(self.deck[9])
        self.draw_station(self.station1, 0)
        self.draw_station(self.station1, 1)
        self.draw_station(self.station1, 2)
        self.draw_station(self.station1, 3)

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
=======
        self.right = Frame(self.root)
        self.right.pack(side=RIGHT, fill=Y)


        #card queue
        self.queue = Canvas(self.right, width=(self.width), bg="black", scrollregion=[0,0,self.width,(len(self.deck)-1)*70+self.height])
        self.S2 = Scrollbar(self.right, orient=VERTICAL)
        self.queue.pack(side=LEFT, fill=Y, expand=1)
        self.S2.pack(side=RIGHT, fill=Y)
        self.queue.config(yscrollcommand=self.S2.set)
        self.S2.config(command=self.queue.yview)

    def step(self):
        self.advance_queue()
        self.update_info()
        

     # I think this method should probably take card as an arg instead of
    # searching the deck within the method, but we can discuss this -NM
    def draw_card(self, card, index):
        # consider seperate method for this (duplicated in draw_cardlet) or a card method.
        num = 0
        icon1 = 0
        icon2 = 0
>>>>>>> master
        for i in range (0, len(card.getStats())):
            if card.getValue(i) > 0:
                num += 1
                if num == 1:
<<<<<<< HEAD
                    index1 = i
                else:
                    index2 = i
        self.create_rounded(self.current, 0,0,180,190, 30, 1, "#202060", self.borders[(index1+1)*(index2+1)])# old color is "#ffc34d"
        self.create_rounded(self.current, 10,10,170,180, 20, 0, "#202060", "#202060")
        self.current.create_text(90,20, anchor=N, fill=self.borders[(index1+1)*(index2+1)], width =150,
=======
                    icon1 = i
                else:
                    icon2 = i
        y = index*70
        self.create_rounded(self.queue, 0,y,180,y+190, 30, 1, "#202060", self.borders[(icon1+1)*(icon2+1)])# old color is "#ffc34d"
        self.create_rounded(self.queue, 10,y+10,170,y+180, 20, 0, "#202060", "#202060")
        self.queue.create_text(90,y+20, anchor=N, fill=self.borders[(icon1+1)*(icon2+1)], width =150,
>>>>>>> master
                                text=card.getName(), font=("Helvetica", "16"),
                                justify=CENTER)
        
        if num == 1:
<<<<<<< HEAD
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
=======
            self.queue.create_image(78,y+150, anchor=W, image=self.icons[icon1])
            self.queue.create_text(76, y+150, anchor=E, text=card.getValue(icon1),
                                     font=("Helvetica", "22"), fill=self.colors[icon1])
        else:
            self.queue.create_image(38,y+150, anchor=W, image=self.icons[icon1])
            self.queue.create_text(36,y+150, anchor=E, text=card.getValue(icon1),
                                     font=("Helvetica", "22"), fill=self.colors[icon1])
            self.queue.create_image(118,y+150, anchor=W, image=self.icons[icon2])
            self.queue.create_text(116,y+150, anchor=E, text=card.getValue(icon2),
                                     font=("Helvetica", "22"), fill=self.colors[icon2])
>>>>>>> master
                    

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

<<<<<<< HEAD
    # draws a black box over the cardlet at the given index
    def erase_cardlet(self, index):
        y = index*78
        self.queue.create_rectangle(0,y,190,70+y, 30, 0, "black", "black")

    # draws a card-like representation of a players space-station
    # this will require significant changes to bidding_agent and space_station
    def draw_station(self, station, index):
        self.root.update()
        width = self.graph.winfo_width()
        height = self.graph.winfo_height()
        self.graph.create_rectangle(5+95*index,height-160,95*(index+1),height-5, fill="purple", outline="grey", width=2)
        self.graph.create_text(50+95*index,height-155, anchor=N, text="$999", font=("Helvetica", "22"))
        self.graph.create_text(50+95*index,height-5, anchor=S, text="TEST", font=("Helvetica", "22")) #name will need to scale to size of name

        if station.getValue(0) > 0:
            self.graph.create_rectangle(9+95*index,height-40-(station.getValue(0)*2),23+95*index,height-40, fill=self.colors[0], outline="#202060", width=2)
        if station.getValue(1) > 0:
            self.graph.create_rectangle(26+95*index,height-40-(station.getValue(1)*2),40+95*index,height-40, fill=self.colors[1], outline="#202060", width=2)
        if station.getValue(2) > 0:
            self.graph.create_rectangle(43+95*index,height-40-(station.getValue(2)*2),57+95*index,height-40, fill=self.colors[2], outline="#202060", width=2)
        if station.getValue(3) > 0:
            self.graph.create_rectangle(60+95*index,height-40-(station.getValue(3)*2),74+95*index,height-40, fill=self.colors[3], outline="#202060", width=2)
        if station.getValue(4) > 0:
            self.graph.create_rectangle(77+95*index,height-40-(station.getValue(4)*2),91+95*index,height-40, fill=self.colors[4], outline="#202060", width=2)

    # adds a new line of text to the bid history window
=======
    # draws a card-like representation of a players space-station
    def draw_station(self, station, index, num_stations):
        self.root.update()
        width = self.graph.winfo_width()
        height = self.graph.winfo_height()

        barwidth= width/(num_stations)
        padding= barwidth/(num_stations/2)
        Lx=(barwidth*(index))+(padding/4)
        Rx=barwidth*(index+1)-(padding/4)
        cord=(padding+Lx/2)+(barwidth*(index-1)-(barwidth*(index-1))/2)+padding-(padding/6)
        
        
        scores = station.getScores(self.round)
        tinybar=barwidth/8
        barcord= Lx+tinybar
        outline= "navy"


        #scale font size for name
        x = 22
        
        l = len(station.getName())
        if l > 4:
            x = int(20 - l/2)

        y= int((barwidth*2)/height)

        self.graph.create_rectangle(Lx,height-160,Rx,height-5, fill="dark violet", outline="SlateBlue1", width=2)
        self.graph.create_text(cord,height-155, anchor=N, text="$"+str(station.getBudget(self.round)), font=("Helvetica", str(y)), fill= "SeaGreen1")
        self.graph.create_text(cord,height-35, anchor=N, text=station.getName(), font=("Helvetica", str(x)), width=90, fill="navy" )

        if scores[0] > 0:
            self.graph.create_rectangle(barcord, height-40-(scores[0]*2), barcord+tinybar, height-40, fill=self.colors[0], outline=outline, width=2)
        if scores[1] > 0:
            self.graph.create_rectangle(barcord+(tinybar), height-40-(scores[1]*2), barcord+(tinybar*2), height-40, fill=self.colors[1], outline=outline, width=2)
        if scores[2] > 0:
            self.graph.create_rectangle(barcord+(tinybar*2), height-40-(scores[2]*2), barcord+(tinybar*3), height-40, fill=self.colors[2], outline=outline, width=2)
        if scores[3] > 0:
            self.graph.create_rectangle(barcord+(tinybar*3), height-40-(scores[3]*2), barcord+(tinybar*4), height-40, fill=self.colors[3], outline=outline, width=2)
        if scores[4] > 0:
            self.graph.create_rectangle(barcord+(tinybar*4), height-40-(scores[4]*2), barcord+(tinybar*5), height-40, fill=self.colors[4], outline=outline, width=2)

    
##        self.graph.create_rectangle(5+95*index,height-160,95*(index+1),height-5, fill="purple", outline="grey", width=2)
##        self.graph.create_text(50+95*index,height-155, anchor=N, text="$"+str(station.getBudget(self.round)), font=("Helvetica", "22"))
##        self.graph.create_text(50+95*index,height-22, anchor=CENTER, text=station.getName(), font=("Helvetica", str(x)), width=90)
##
##        scores = station.getScores(self.round)
##
##        if scores[0] > 0:
##            self.graph.create_rectangle(9+95*index,height-40-(scores[0]*2),23+95*index,height-40, fill=self.colors[0], outline="#202060", width=2)
##        if scores[1] > 0:
##            self.graph.create_rectangle(26+95*index,height-40-(scores[1]*2),40+95*index,height-40, fill=self.colors[1], outline="#202060", width=2)
##        if scores[2] > 0:
##            self.graph.create_rectangle(43+95*index,height-40-(scores[2]*2),57+95*index,height-40, fill=self.colors[2], outline="#202060", width=2)
##        if scores[3] > 0:
##            self.graph.create_rectangle(60+95*index,height-40-(scores[3]*2),74+95*index,height-40, fill=self.colors[3], outline="#202060", width=2)
##        if scores[4] > 0:
##            self.graph.create_rectangle(77+95*index,height-40-(scores[4]*2),91+95*index,height-40, fill=self.colors[4], outline="#202060", width=2)

    def findhighest(self, bids):
        x=bids[0]
        highest=x[1]
        for i in bids:
            if i[1] > highest:
                highest = i[1]
        return highest

    def scale(self, height, highest, bid):
        return (height-((bid/highest)*height))

    # draws animated bars for each agents bid
    def makeBars(self, stations, bids):
        width = self.graph.winfo_width()
        height = self.graph.winfo_width() - 363
        players = len(bids)
        barwidth = width/(players)#85
        padding = barwidth/((players)/2)#15 
        width = width+padding

        Rx = padding # right corner x value
        #Uy would be equal to the height; is agent-specific (is equivocal to bid)
        Lx = barwidth # left corner x value
        #lower corners' y value is unchanging and always set at full 



        highest = self.findhighest(bids)
        for i in range(1,players+1):
            bar = 0 #init canvas object
            player_data=bids[i-1]
            bid = player_data[1]
            color = stations[i-1].getColor()
            Rx = 15 + (i-1)*95#(barwidth*(i-1)) + padding
            bar_height = self.scale(height, highest, bid)
            Lx = 85 + (i-1)*95
            start = height
            iterations = 120
            if bar_height == height:
                time.sleep(0.1)
                bar = self.graph.create_rectangle(Rx,bar_height, Lx, height, fill=color, outline=color)
            else:
                bar = self.graph.create_rectangle(Rx, height+bar_height, Lx, height*2, fill=color, outline=color)
                self.graph.addtag_all(bar)   
                for n in range(iterations):
                    self.graph.move(bar, 0, -(height/iterations))
                    self.root.update()
                    time.sleep(0.008)

    def draw_bars(self, stations, bids):
        width = self.graph.winfo_width()
        height = self.graph.winfo_height() - 162
        players = len(bids)
        highest = self.findhighest(bids)

        barwidth= (width/(players))
        padding= barwidth/((players)/2)

        for i in range(0,players):
            bar = 0
            player_data=bids[i]
            bid = player_data[1]
            color = stations[i].getColor()
            bar_size = ((bid/highest)*(height-10))

            Lx = barwidth*(i+1)-(padding/4)
            Ly = height
            Rx = (barwidth*(i))+(padding/4)
            Ry = height
            
            iterations = 105
            increment = bar_size/iterations
            bar = self.graph.create_rectangle(Rx+30,Ry,Lx-30,Ly, fill=color, width=0)
            for j in range(iterations):
                coords = self.graph.coords(bar)
                self.graph.coords(bar, coords[0], coords[1]-increment, coords[2], coords[3])
                self.root.update()
                if increment > 4:
                    if (j/iterations) > .8:
                       time.sleep(0.0194)
                    else:
                        time.sleep(0.015)
                elif increment > 2:
                    time.sleep(0.012) 
                elif increment > 1.5:
                    time.sleep(0.0097) 
                elif increment > 1:
                    time.sleep(0.009)
                elif increment > .47: 
                    time.sleep(0.0047)
                elif increment < .3:
                    time.sleep(0.0016)
                else:
                   time.sleep(0.002)
            if bar_size < 35:
                self.graph.create_text(((Lx-(barwidth/(2.55)))), height-bar_size-35, anchor=N, text="$" +str(bid), font=("Helvetica", "18", "bold"), fill="white")
            else:
                self.graph.create_text(((Lx-(barwidth/(2.55)))), height-bar_size, anchor=N, text="$" +str(bid), font=("Helvetica", "18", "bold"), fill="white")
            self.root.update()

    # displays a text message
>>>>>>> master
    def add_history(self, message):
        self.T.config(state=NORMAL)
        self.T.insert(END, "\n" + message)
        self.T.see(END)
        self.T.config(state=DISABLED)

<<<<<<< HEAD
    # draws the next card in the stack, removes it, and draws the remaining queue
    def advance_queue(self):
        if self.deck:
            card = self.deck[0]
            self.draw_card(card)
            self.deck.remove(self.deck[0])
            self.queue.delete(ALL)
            for i in range(0, len(self.deck)):
                self.draw_cardlet(self.deck[i], i)

=======
     # moves the cards up in the visual queue
    def advance_queue(self):
        self.queue.config(scrollregion=[0,0,self.width,(len(self.deck)-1)*70+self.height])
        if self.deck:
            self.queue.delete(ALL)
            for i in range(len(self.deck)-1, -1, -1):
                self.draw_card(self.deck[i], i)
            self.card = self.deck[0]
            self.deck.remove(self.deck[0])
                
>>>>>>> master
    # draws the legend which shows the icons for each of the 5 categories
    def legend(self, event):
        width = self.graph.winfo_width()
        height = self.graph.winfo_height()
        x1 = width-self.width+10
        y1 = height-self.height-5
        x2 = width-5
        y2 = height-5
        self.a = self.graph.create_rectangle(x1,y1,x2,y2, fill="#202060", outline="grey", width=5)
        self.b = self.graph.create_text((x2-100), y1+(self.height*(1/6)), text="Science", anchor=W, font=("Helvetica", "12", "bold"), fill=self.colors[0])
        self.c = self.graph.create_text((x2-100), y1+(self.height*(2/6)), text="Ecology", anchor=W, font=("Helvetica", "12", "bold"), fill=self.colors[1])
        self.d = self.graph.create_text((x2-100), y1+(self.height*(3/6)), text="Culture", anchor=W, font=("Helvetica", "12", "bold"), fill=self.colors[2])
        self.e = self.graph.create_text((x2-100), y1+(self.height*(4/6)), text="Commerce", anchor=W, font=("Helvetica", "12", "bold"), fill=self.colors[3])
        self.f = self.graph.create_text((x2-100), y1+(self.height*(5/6)), text="Industry", anchor=W, font=("Helvetica", "12", "bold"), fill=self.colors[4])

        self.g = self.graph.create_image((x2-150), y1+(self.height*(1/6)), image=self.icons[0], anchor=W)
        self.h = self.graph.create_image((x2-150), y1+(self.height*(2/6)), image=self.icons[1], anchor=W)
        self.i = self.graph.create_image((x2-150), y1+(self.height*(3/6)), image=self.icons[2], anchor=W)
        self.j = self.graph.create_image((x2-150), y1+(self.height*(4/6)), image=self.icons[3], anchor=W)
        self.k = self.graph.create_image((x2-150), y1+(self.height*(5/6)), image=self.icons[4], anchor=W)

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
<<<<<<< HEAD
        
        
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
=======
                
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
            
            #give card to the winner.
            # TODO mabye?
            
            self.graph.create_image(0,0, anchor=NW, image=self.img)
            for i in range(0, len(stations)):
                self.draw_station(stations[i], i, len(stations))

            self.draw_bars(stations, bids)

            self.add_history("'"+stations[winner].getName()+"' won '"+self.card.getName()+"' for $"+str(price))

            self.round += 1                        

    def add_stations(self, stations):
        if len(self.stations) == 0:
            self.stations.append(stations)
            #agent info
            for i in range(0, len(stations)):
                self.draw_station(stations[i], i, len(stations))
        else:
            self.stations.append(stations)

    def add_deck(self, deck):
        self.deck = deck

        
    def update_round(self, bids, winner, space_stations):
        self.bids.append(bids)
        self.winner.append(winner)
        self.stations.append(space_stations)

    def update_price(self, price):
        self.price.append(price)

>>>>>>> master
