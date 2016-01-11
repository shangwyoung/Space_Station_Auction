from tkinter import *

master = Tk()
master.title("Space Station Auciton")
cardnames = """Puppy Cloning Center
Nuclear Power Plant
Oxygen Farm
Recreation Dome
Solar Observation Deck
Genetics Laboratory
"""

playernames = """Gary
Fred
Margo
Larry
Nick
Sharon
Lucy
Riley
Bob
Dave
Kelly
"""

left = Frame(master, bg="black")
left.pack(side=LEFT, fill=Y)

cardlbl = Message(left, text="MODULES", bd=5, bg="#666699",
                    relief=RAISED, width=100, fg="white")
cardlbl.pack(side=TOP, fill=X)

cards = Message(left, text = cardnames, bd = 5, bg="#ccccff", anchor =NW,
                  relief=RIDGE)
cards.pack(side=TOP, fill=BOTH, expand=1)


middle = Frame(master)
middle.pack(side=LEFT, fill=BOTH, expand=1)

picture = Canvas(middle, bg = "red")

img = PhotoImage(file="starry-sky-of-bretagne.gif")
picture.create_image(0,0, anchor=NW, image=img)

picture.pack(fill=BOTH, expand=1)

buttons = Frame(middle)
buttons.pack(side=BOTTOM, fill=X)

start = Button(buttons, text="START", bg="green")
step = Button(buttons, text="STOP", bg="yellow")
stop = Button(buttons, text="STOP", bg="red")
QUIT = Button(buttons, text="QUIT")

start.pack(side=LEFT, fill=X, expand=1)
step.pack(side=LEFT, fill=X, expand=1)
stop.pack(side=LEFT, fill=X, expand=1)
QUIT.pack(side=LEFT, fill=X, expand=1)


right = Frame(master, bg="black")
right.pack(side=RIGHT, fill=Y)

topplayer = Message(right, text="BIDDERS", bd=5, bg="#666699",
                    relief=RAISED, width=100, fg="white")
topplayer.pack(side=TOP, fill=X)

players = Message(right, text = playernames, bd = 5, bg="#ccccff", anchor =NW,
                  relief=RIDGE)
players.pack(side=TOP, fill=BOTH, expand=1)

mainloop()
