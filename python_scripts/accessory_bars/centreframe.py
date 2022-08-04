import tkinter as tk
from databases.db_translator import Db_Translator

"""
Class to handle the construction of the centreframe / main housing frame of the application
CentreFrame has the responsibility to adapt and change to what buttons the user presses
"""
class CentreFrame ():
    __slots__ = ("centre_frame", "actions", "display_list")

    def __init__(self, window, screenheight:int, screenwidth:int):
        self.centre_frame = tk.Frame(master = window, width=(screenwidth - screenwidth/6), height=500,
        bg="#B2BEB5")
        
        self.actions = None

        self.display_list = list()
    
    # displaying the centre frame 
    def construct_centre_frame(self)->None:
        self.centre_frame.grid(row=2, column=2)
    
    # changing what will be displayed
    def change_centre_frame(self, given_action)->None:
        self.actions = given_action 
    
    # function to populate what is on the centre frame with a given action
    def populate_centre_frame(self)->None:
        if(self.actions == "home_clicked"): # have to populate with most clicked from DB
            db_object = Db_Translator("most_clicked.csv")
            self.display_list = db_object.content_list()
        
        elif(self.actions == "ls_clicked"):
            # incrementing the most_clicked csv file is a microprocess that needs to be triggered

            db_object = Db_Translator("liked_songs.csv") # creating an instance of the Db_Translator object to retrieve the liked_songs playlist
            self.display_list = db_object.content_list()
        
        elif(self.actions == "settings_clicked"):
            # displaying the settings links
            db_object = Db_Translator("settings_widgets.csv")
            self.display_list = db_object.content_list()


        

        for i in range(6):
            self.display_list[i].grid(row=2, column=3)
        

    

