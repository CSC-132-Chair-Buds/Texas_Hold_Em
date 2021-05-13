# Texas_Hold_Em
Card Game for Final Project in CSC 132-004 at Louisiana Tech

Number of Group Members: 3

Description of Project:
    
  Essentially we are making the Texas Hold 'Em variation of Poker to the best of our abilities by coding it all by ourselves. Note this code
  is coded 100 percent in python. The three of us each have a Raspberry Pi with an LCD touchscreen, and we used this to run our poker game code.
  Since there are only three of us, we hardcoded the program to only play with 3 players ever in an entire game of poker. So, when one player quits
  the entire game of poker by quiting or running out of money, then the game will break and will have to be restarted manually. Our game runs its
  "main code" on one raspberry pi where it will do all the calculations of the game and then sends the required info to the other two rapberry pi
  touchscreens for display purposes. This way everyone can see what is happening for them, but the game is really only happening on one computer.
  The way we sent the information of the other raspberry pi players to the other raspberry pi's were by utilizing UDP socket programming (networking).
  For our project we had to have a nice enclosure for our game to sit in, so we created a nice hexagonal foam board case for all three of the rapberry
  pi's to be in. This case was hexagonal so players couldn't see eachother's screens and we used foam board because it was nice and inexpensive for our
  purposes. The last thing we implemented were GPIO buttons for input from the players of our game. We had four buttons for "make bet"/"call", for "fold",
  for "raise bet", and for "lower bet". We simply got arcade like buttons that had a positive lead and a negative lead, then we connected the positive
  lead into a breadboard GPIO pin and the negative lead into ground. With this simple circuit we created, our breadboard GPIO pins tell us whether
  or not you pressed one of the buttons.

Overview of Code:

    1.) The Class Heirarchy of Object-Oriented Programming of Objects used in poker (i.e. table to play upon, cards to use, players,  etc.)
    2.) The GUI (graphical user interface) using pygame
    3.) The Logic of the game (i.e. how betting rounds work or comparing hands to declare a winner)
    4.) The UDP (user datagram packeges) socket code

