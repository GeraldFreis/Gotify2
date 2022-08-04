import tkinter as tk
import tkinter.font as font

class TopBar():
    def __init__(self, mainwindow, screenwidth:int, screenheight:int):
        self.top_bar = tk.Frame(master = mainwindow, width=(screenwidth - (screenwidth / 6)), height=100, bg="#FFFFFF")
        main_font = font.Font(family="Gothic Medium", size=35)
        self.name = tk.Label(master = mainwindow, text="Gerald for now", font=main_font)
    
    def construct_top_frame(self):
        self.top_bar.grid(row=0, column=3, columnspan=4, rowspan=4)
        self.name.grid(row = 0, column = 2)
    
