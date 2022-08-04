import tkinter as tk

"""
Class to handle the sidebars of the mainpage
    preconditions = mainwindow object created by the mainpage class    
"""
class SideBars():
    __slots__ = ("side_bar", "settings_button", "home_button", "liked_songs_button")
    
    def __init__(self, mainwindow, screenwidth:int, screenheight:int):
        self.side_bar = tk.Frame(master = mainwindow,
            background = "#FEFBEA",
            border = 1,
            width = screenwidth / 6,
            height = screenheight)
        
        self.settings_button = None
        self.home_button = None
        self.liked_songs_button = None
        
    # constructing the side frame object 
    def construct_side_frame(self, totalrows:int)->None:
        self.side_bar.grid(row = 1, column = 1, rowspan = totalrows, columnspan = 1)
    
    def populate_side_bar(self)->None:
        self.settings_button = tk.Button(master = self.side_bar, text="Settings",
        width = 10, height = 1,
        pady=10, border=0).grid(row = 1, column = 1)

        self.home_button = tk.Button(master = self.side_bar, text="Home",
        width = 10, height = 1,
        pady=10, border=0).grid(row = 2, column = 1)

        self.liked_songs_button = tk.Button(master = self.side_bar, text="Liked Songs",
        width = 10, height = 1,
        pady=10, border=0, borderwidth=2).grid(row = 3, column = 1)

    
