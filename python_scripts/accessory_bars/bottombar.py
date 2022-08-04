import tkinter as tk
"""Class to handle the bottom bar on the screen
    preconditions = mainwindow to construct this class (mainwindow is required to be the window of a mainpage object)
"""
class BottomBar():
    __slots__ = ("bottom_frame", "song_name")

    def __init__(self, mainwindow, screenwidth:int, screenheight:int):
        self.bottom_frame = tk.Frame(master=mainwindow,
            background = "#FEFBEA",
            border = 1,
            width=1200,
            height=750//7)
        
        self.song_name = tk.Button(master=self.bottom_frame,
        text="No song yet, search and play to begin",
        fg = "#808080",
        bg = "#FEFBEA",
        border = 2)

    # creates a bottom bar frame onto the main window
    def constructing_bottom_frame(self, startingrow: int, startingcolumn: int)->None:
       self.bottom_frame.grid(row=startingrow, column=startingcolumn, rowspan=4, columnspan=2)

       self.song_name.grid(row=2, column=1, columnspan=1)
    

    # changing the song name 
    def changing_song(self, songname:str)->None:
        self.song_name['text'] = songname
