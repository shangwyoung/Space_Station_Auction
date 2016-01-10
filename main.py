import Auction_GUI
import tkinter as tk

def main():
    # create a model for the game
    model = Auction_GUI.Auction_GUI()
    model.make_buttons()
    model.bind_key()
    model.msg_box()
    model.msg_box2()

    tk.mainloop()  
main()