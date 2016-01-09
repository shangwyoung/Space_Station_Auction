from tkinter import *

master = Tk()

#left column for card queue
msg = "one\ntwo\nthree\nfour\nfive\nsix\nseven\neight\nnine\nten"
cards = Message(master, ,text=msg, bd=5, bg="purple", anchor=NW)
cards.pack(side=LEFT, fill=Y)

#card current card and graph
middle = Frame(master)
middle.pack(side=LEFT, fill=Y)

card = Canvas(middle, bg="red")
card.pack()

graph = Canvas(middle, bg="blue")
graph.pack()

#right column for bidders
players = Message(master, text=msg, bd=5, bg="green", anchor=NW)
players.pack(side=LEFT, fill=Y)

mainloop()
