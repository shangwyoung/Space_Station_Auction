import tkinter as tk

class Auction_GUI():

    def __init__(self, canvas_height = 500, canvas_width = 700, scale = 20):
        # draw window
        self.root = tk.Tk()
        self.root.grid()
        # set up canvas
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.SCALE_FACTOR = scale
        self.w = tk.Canvas(self.root, bg = "white", 
                   width = self.canvas_width,
                   height = self.canvas_height)
        self.w.grid(columnspan=25, rowspan=10, sticky='W')
        
    def draw_map(self):
	# draw the map
        for x in range(25):
            for y in range(20):
                self.w.create_text((x * self.SCALE_FACTOR + 7.5, y * self.SCALE_FACTOR + 7.5), text= self.copy_L[x][y], font=('Courier New', -self.SCALE_FACTOR))

  
    def make_buttons(self):
        # Quit button
        self.quit_button = tk.Button(self.root, text='Quit', bg='indian red',
                                     width=4 , command=self.root.destroy)
        self.quit_button.grid(column=22, row=8)
        
        # Up button
        self.up_button = tk.Button(self.root, text='Start', bg='lightblue',
                                     width=4 , command=self.root.destroy)
        self.up_button.grid(column=22, row=7)
        
    def bind_key(self):
        # Add hotkeys for buttons.
        self.root.bind("q", lambda *args: exit())
        self.root.bind("Q", lambda *args: exit())
        
        
    def msg_box(self, s = "Welcome to Space Station Auction!"):
        # upper message box
        self.quote = s
        self.T = tk.Text(self.root, height=6, width=25)
        self.T.delete("1.0", tk.END)
        self.T.configure(state = 'normal')
        self.T.insert(tk.END, self.quote)
        self.T.configure(state = 'disabled')
        self.T.grid(column=22, row=1)
        
        
    def msg_box2(self, s = ""):
        # enter box for the user
        self.N = tk.Text(self.root, height=3, width=25)
        self.N.delete("1.0", tk.END)
        self.N.configure(state = 'normal')
        self.quote3 = ""
        self.N.insert(tk.END, self.quote3)
        self.N.configure(state = 'disabled')
        self.N.grid(column=22, row=2)
 