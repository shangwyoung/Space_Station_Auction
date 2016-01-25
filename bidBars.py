# bidBars.py
# Figuring out the bars for the auction simulator visualization
# 1/17/16
# Sage Vouse

import time
from tkinter import *
#import card
#import BiddingAgent
#import AuctionSimulator
def findhighest(playerinfo):
    x=playerinfo[0]
    highest=x[0]
    for i in playerinfo:
        if i[0]>highest:
            highest=i[0]
    return highest

def scale(height,highest, bid):
    return (height-((bid/highest)*height))
        
master = Tk()
width= eval(input("width?: "))
height= 450
playerinfo=[(367, "medium orchid"),(0,"midnight blue"),(402,"sea green"),(20,"steel blue"),(70,"cadet blue"),(111,"gold"),(205,"navy"),(460,"plum"),(17,"deep sky blue"),(230,"dark slate gray"),(127,"VioletRed1"),(270,"misty rose"),(45,"hot pink"),(100,"DarkOrchid3")]
players= len(playerinfo)
barwidth= width/(players)
padding= barwidth/(players/2)
width=width+padding
w = Canvas(master, width= width, height= height)
w.pack()


Rx= padding # right corner x value
#Uy would be equal to the height; is agent-specific (is equivocal to bid)
Lx= barwidth # left corner x value
#lower corners' y value is unchanging and always set at full 



highest= findhighest(playerinfo)
for i in range(1,players+1):
    player_data=playerinfo[i-1]
    bid=player_data[0]
    color= player_data[1]
    Rx=(barwidth*(i-1))+padding
    bar_height= scale(height,highest, bid)
    Lx=barwidth*(i)
    start= height
    iterations=120
    if bar_height== height:
        time.sleep(0.1)
        w.create_rectangle(Rx,bar_height, Lx, height, fill=color, outline= color)
    else:
        w.create_rectangle(Rx, (height+bar_height), Lx, height*2, fill=color, outline= color)
        w.addtag_all("%d"%(i))
        for n in range(iterations):
            w.move("%d" %(i), 0, -(height/iterations))
            master.update()
 #           time.sleep(0.02)
        
        
        

    



mainloop()
