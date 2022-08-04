# This is a second version of a spotify emulating application writting in Tkinter
This spotify emulater does not have direct access to a song database so I instead configured the application
to utilise Youtube's search. However, the main point of this emulater was to become confident with databases in python.
Considering that the application works I think it was successful. 

Regards,
    Gerald


# design steps
## 1 -> Design the main interface first and then worry about authentication
    - main design is going to be the current design utilised but it will be in white as this works better for mac
    - We will have a large empty space in the center that will be filled with relevant applets or perhaps albums if I construct a relational database
    - Originally there will be a liked songs, recent songs, and playlists buttons
    - we will have a collapsible windows / workspace on the left of the screen to house the common spotify functions
    - on the bottom we will have a space for the song name to be whenever a song may be playing

## 2 -> implementing agility and dynamic linking in the applet
    - I will be designing a dynamic system to manage player libraries or albums in the applet
        - to do this we will have a database created for usercontent_playlists which will be playlists
            - and usercontent_albums which will be their favourited albums
            - and then we will have liked songs

    - on the main page of the app we will have a dynamic page which changes with user requests
        - this main page has an action data member that will be changed anytime the user wants to do something like go to their liked songs
        - this will then change another function that will go to the database of liked songs and retrieve the songs and their hyperlinks, the hyperlinks are vital to being able to click on the song, as each song will act as a button in the applet 
            - because of this button type that they are they need to have a function accompanying them when they are shown on the page
                - initially there will be a 10 block limit to what is shown on the screen, unless they are songs in which case they can be more than 10