from tkinter import *
import card_generator
import card
import space_station
import time
#import auctionSimulator

class AuctionGUI():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.bids = []
        self.winner = []
        self.stations = []
        self.round = 0
        self.price = []
        self.display = []
        self.deck = card_generator.buildDeck(10) #for testing

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
        self.graph = Canvas(self.left, bg="black", scrollregion=[0,0,2592,1728], width=800, height=600)

        self.img = PhotoImage(file="background.ppm")
        self.graph.create_image(0,0, anchor=NW, image=self.img)

        self.graph.pack(side=TOP, fill=BOTH, expand=1)

        # scrollbar for main canvas... probably won't use
        """
        self.graph_scroll = Scrollbar(self.left, orient=HORIZONTAL,
                command=self.graph.xview)
        self.graph_scroll.pack(side=TOP, fill=X)
        self.graph.config(xscrollcommand=self.graph_scroll.set)
        """

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
        
        # bindings for [?] button
        self.legend_button.bind('<Enter>', self.legend)
        self.legend_button.bind('<Leave>', self.remove_legend)

        # *RIGHT PANEL*
        self.right = Frame(self.root)
        self.right.pack(side=RIGHT, fill=Y)

        # current card
        self.current = Canvas(self.right, width =(self.width),
                              height=(self.height), bg="black")
        self.current.pack(side=TOP)

        #card queue
        self.queue = Canvas(self.right, width=(self.width), bg="black")
        self.queue.pack(side=TOP, fill=Y, expand=1)
        
        # TESTING ONLY
        """
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
        """

    def step(self):
        self.advance_queue()
        self.update_info()
        

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

    # draws a card-like representation of a players space-station
    # this will require significant changes to bidding_agent and space_station
    # related to this, we need to discuss the changes to space_station
    def draw_station(self, station, index):
        self.root.update()
        width = self.graph.winfo_width()
        height = self.graph.winfo_height()

        #scale font size for name
        
        x = 22
        
        l = len(station.getName())
        if l > 4:
            x = int(20 - l/2)
            
        self.graph.create_rectangle(5+95*index,height-160,95*(index+1),height, fill="purple", outline="grey", width=2)
        self.graph.create_text(50+95*index,height-155, anchor=N, text="$"+str(station.getBudget(self.round)), font=("Helvetica", "22"))
        self.graph.create_text(50+95*index,height-22, anchor=CENTER, text=station.getName(), font=("Helvetica", str(x)), width=90)

        scores = station.getScores(self.round)

        if scores[0] > 0:
            self.graph.create_rectangle(9+95*index,height-40-(scores[0]*2),23+95*index,height-40, fill=self.colors[0], outline="#202060", width=2)
        if scores[1] > 0:
            self.graph.create_rectangle(26+95*index,height-40-(scores[1]*2),40+95*index,height-40, fill=self.colors[1], outline="#202060", width=2)
        if scores[2] > 0:
            self.graph.create_rectangle(43+95*index,height-40-(scores[2]*2),57+95*index,height-40, fill=self.colors[2], outline="#202060", width=2)
        if scores[3] > 0:
            self.graph.create_rectangle(60+95*index,height-40-(scores[3]*2),74+95*index,height-40, fill=self.colors[3], outline="#202060", width=2)
        if scores[4] > 0:
            self.graph.create_rectangle(77+95*index,height-40-(scores[4]*2),91+95*index,height-40, fill=self.colors[4], outline="#202060", width=2)

    def findhighest(self, bids):
        x=bids[0]
        highest=x[1]
        for i in bids:
            if i[1] > highest:
                highest = i[1]
        print(highest)
        return highest

    def scale(self, height, highest, bid):
        return (height-((bid/highest)*height))

    def makeBars(self, stations, bids):
        width = self.graph.winfo_width()
        height = self.graph.winfo_width() - 363
        players = len(bids)
        barwidth = 80 #width/(players)
        padding = 10 #barwidth/(players/2)
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
            Rx = (barwidth*(i-1)) + padding
            bar_height = self.scale(height, highest, bid)
            Lx = i*barwidth #barwidth*(i)
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
        

    def add_history(self, message):
        self.T.config(state=NORMAL)
        self.T.insert(END, "\n" + message)
        self.T.see(END)
        self.T.config(state=DISABLED)

    def advance_queue(self):
        if self.deck:
            self.card = self.deck[0]
            self.draw_card(self.card)
            self.deck.remove(self.deck[0])
            self.queue.delete(ALL)
            for i in range(0, len(self.deck)):
                self.draw_cardlet(self.deck[i], i)
                
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
            '''self.display.append(self.graph.create_rectangle(5+85*winner, 5, 85+85*winner, 60, fill="#19334d", outline="#00e5e6", width=3))
            self.display.append(self.graph.create_text(45+85*winner, 40, anchor=N, fill="#00e5e6", width = 75,
                        text="[" + str(self.card.getValue(0)) +
                       ", " + str(self.card.getValue(1)) +
                       ", " + str(self.card.getValue(2)) +
                       ", " + str(self.card.getValue(3)) +
                       ", " + str(self.card.getValue(4)) + "]", font=("Helvetica", "12"),
                        justify=CENTER))
            self.display.append(self.graph.create_text(45+85*winner, 20, anchor=N, fill="#00e5e6", width = 75,
                        text="$"+str(price), font=("Helvetica", "12"),
                        justify=CENTER))'''
            self.add_history("'"+stations[winner].getName()+"' won '"+self.card.getName()+"' for $"+str(price))

            '''#update total scores
            for i in range (len(stations)):
                self.display.append(self.graph.create_text(45+85*i, 240, anchor=N, fill="#00e5e6", width = 75,
                        text=stations[i].getScores(self.round), font=("Helvetica", "12"),
                        justify=CENTER))
                
            #update budgets
            for i in range (len(stations)):
                self.display.append(self.graph.create_text(45+85*i, 195, anchor=N, fill="#00e5e6", width = 75,
                        text="$"+str(stations[i].getBudget(self.round)), font=("Helvetica", "12"),
                        justify=CENTER))'''
            self.graph.create_image(0,0, anchor=NW, image=self.img)
            for i in range(0, len(stations)):
                self.draw_station(stations[i], i)

            self.makeBars(stations, bids) 


            self.round += 1            
                       

    def add_stations(self, stations):
        if len(self.stations) == 0:
            self.stations.append(stations)
            #agent info
            for i in range(0, len(stations)):
                self.draw_station(stations[i], i)
            """
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
            """
            
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


