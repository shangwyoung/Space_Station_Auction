from tkinter import *

class Prompt:
    def __init__(self, master):
        frame = Frame(master)
        frame.config(bd=20)
        frame.pack()

        self.v = StringVar()

        self.deckTypes = [("Standard", 1), ("Random", 2), ("Mixed", 3)]

        def confirm():
            print(self.v.get())
            master.destroy()

        for txt, val in self.deckTypes:
            Radiobutton(frame,
                    text=txt,
                    indicatoron=0,
                    width=20,
                    padx=20,
                    variable=self.v,
                    command=confirm,
                    value=val).pack(anchor=N)

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.leave=Button(frame,
                text="QUIT", fg="red",
                command=frame.quit)
        self.leave.pack(side=LEFT)

        self.message = Button(frame,
                text="?", bg="purple", fg="black",
                command=self.display_message)
        self.message.pack(side=RIGHT)

        self.prompt = Message(frame, text="DONT PRESS THE PRETTY BUTTON")
        self.prompt.pack(side=BOTTOM)

    def display_message(self):
        print("You pressed the button didn't you?")

root = Tk()
promt = Prompt(root)
root.mainloop()

root2 = Tk()
app = App(root2)
root2.mainloop()
root2.destroy()
