import tkinter as tk
from python_scripts.accessory_bars.bottombar import BottomBar
from python_scripts.accessory_bars.sidebars import SideBars
from python_scripts.accessory_bars.topbar import TopBar

"""Main page class handles the creation and maintenance of the main page """
class MainPage():
    __slots__ = ("main_window", "bottom_bar", "side_bar", "top_bar")
    def __init__(self):
        self.main_window = tk.Tk()
        self.bottom_bar = None
        self.side_bar = None
        self.top_bar = None
    
    # constructs the main page
    def construct_main_page(self)->None:
        self.main_window['bg'] = "#FFFFFF" #colour white background
        self.main_window.geometry("1300x750+0+0")
        self.main_window.title("Gotify")


        # constructing the side bar
        self.side_bar = SideBars(self.main_window, 1300, 750)
        self.side_bar.construct_side_frame(30)
        self.side_bar.populate_side_bar()


        # constructing the bottom bar
        self.bottom_bar = BottomBar(self.main_window, 1300, 750)
        self.bottom_bar.constructing_bottom_frame(27, 3)

        # constructing the top bar
        self.top_bar = TopBar(self.main_window, 1300, 750)
        self.top_bar.construct_top_frame()

    def draw_main_page(self):
        self.main_window.mainloop()
    
    