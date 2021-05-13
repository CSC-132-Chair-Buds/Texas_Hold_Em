# import needed modules
import socket
import pygame
from time import sleep
# do not forget to initialize pygame
pygame.init()

# create display screen here and we use (800,450)
# so that it fits nicely along the raspberry pi
# LCD touchscreen
surface1 = pygame.display.set_mode((800,450))
 
# function to recieve data streams from MainPlayer_FINALFINAL.py
# the Main Player sends over a list as a string (i.e. "[0,1,2,...,n]")
# we decipher this string and turn it back into a list of data
def UDP_client():
    # host IP address that needs to change depending on current IPv4 IP address
    host = "127.0.0.1"
    # port that matches Second Player's Port in Main Player Code
    port = 65433

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    sock.bind((host, port))    
    
    # receive data from Main Player code
    data, addr = sock.recvfrom(1024)
    
    # We know the main player sent the data as a string of a list
    # so here we take off the brackets of the list from the string
    data = data[1:-1]
    data = data.decode("utf-8")
    
    # Use the split function to make this string of a list back into a list
    data = data.split(", ")
    print(data)
    
    # returns the list of data
    return data


# Function to update GUI for second player based off of the many data sent from the main player
# P1 is just the player that we want to have being the 'main character'
def updateScreen(round_Counter, main_Char_hand0_image, main_Char_hand1_image, main_Char_current_Bet, main_Char_purse, T1_hand0_image, T1_hand1_image, T1_hand2_image, T1_hand3_image, T1_hand4_image, T1_pot, other_Char1_hand0_image, other_Char1_hand1_image, other_Char1_current_Bet, other_Char1_purse, other_Char2_hand0_image, other_Char2_hand1_image, other_Char2_current_Bet, other_Char2_purse, main_Char_Turn, main_Char_Win, other_Char1_Turn, other_Char1_Win, other_Char2_Turn, other_Char2_Win):
    # make background green (using HEX for RGB values)
    surface1.fill((0x8FDA87))
    # put table pot, player's pot and bet on display
    style = pygame.font.Font(None, 20)
    style2 = pygame.font.Font(None, 40)
    textPBet = style.render("Your Current Bet ${}".format(main_Char_current_Bet), True, (0,0,0))
    textPPurse = style.render("Your Purse ${}".format(main_Char_purse), True, (0,0,0))
    textTPot = style.render("Table pot ${}".format(T1_pot), True, (0,0,0))
    textP2Bet = style.render("Player 2 Current Bet ${}".format(other_Char1_current_Bet), True, (0,0,0))
    textP2Purse = style.render("Player 2 Purse ${}".format(other_Char1_purse), True, (0,0,0))
    textP3Bet = style.render("Player 3 Current Bet ${}".format(other_Char2_current_Bet), True, (0,0,0))
    textP3Purse = style.render("Player 3 Purse ${}".format(other_Char2_purse), True, (0,0,0))
    surface1.blit(textPBet, (0, 360))
    surface1.blit(textPPurse, (0, 380))
    surface1.blit(textTPot, (0, 400))
    surface1.blit(textP2Bet,(0, 100))
    surface1.blit(textP2Purse,(0, 120))
    surface1.blit(textP3Bet, (610, 100))
    surface1.blit(textP3Purse, (610, 120))
    if (round_Counter < 2):
        # Table hand
        surface1.blit(Card_back, (140, 170))
        surface1.blit(Card_back, (240, 170))
        surface1.blit(Card_back, (340, 170))
        surface1.blit(Card_back, (440, 170))
        surface1.blit(Card_back, (540, 170))
        # player's hands
        # player 1
        surface1.blit(main_Char_hand0_image, (320, 350))
        surface1.blit(main_Char_hand1_image, (420, 350))
        # player 2
        surface1.blit(Card_back, (0, 0))
        surface1.blit(Card_back, (100, 0))
        # player 3
        surface1.blit(Card_back, (610, 0))
        surface1.blit(Card_back, (710, 0))
        # determine player turn and display it
        if(main_Char_Turn == True):
            textPlayer_Turn = style2.render("its Your Turn.", True, (0,0,0))
            surface1.blit(textPlayer_Turn, (320,0))
        elif(other_Char1_Turn == True):
            textPlayer_Turn = style2.render("its Player Two's Turn.", True, (0,0,0))
            surface1.blit(textPlayer_Turn, (280,0))
        else:
            textPlayer_Turn = style2.render("its Player Three's Turn.", True, (0,0,0))
            surface1.blit(textPlayer_Turn, (270,0))
    elif (round_Counter == 2):
        # Table hand (The Flop)
        surface1.blit(T1_hand0_image, (140, 170))
        surface1.blit(T1_hand1_image, (240, 170))
        surface1.blit(T1_hand2_image, (340, 170))
        surface1.blit(Card_back, (440, 170))
        surface1.blit(Card_back, (540, 170))
        # player's hands
        # player 1
        surface1.blit(main_Char_hand0_image, (320, 350))
        surface1.blit(main_Char_hand1_image, (420, 350))
        # player 2
        surface1.blit(Card_back, (0, 0))
        surface1.blit(Card_back, (100, 0))
        # player 3
        surface1.blit(Card_back, (610, 0))
        surface1.blit(Card_back, (710, 0))
        # determine player turn and display it
        if(main_Char_Turn == True):
            textPlayer_Turn = style2.render("its Your Turn.", True, (0,0,0))
            surface1.blit(textPlayer_Turn, (320,0))
        elif(other_Char1_Turn == True):
            textPlayer_Turn = style2.render("its Player Two's Turn.", True, (0,0,0))
            surface1.blit(textPlayer_Turn, (280,0))
        else:
            textPlayer_Turn = style2.render("its Player Three's Turn.", True, (0,0,0))
            surface1.blit(textPlayer_Turn, (270,0))
    elif (round_Counter == 3):
        # Table hand (The Turn)
        surface1.blit(T1_hand0_image, (140, 170))
        surface1.blit(T1_hand1_image, (240, 170))
        surface1.blit(T1_hand2_image, (340, 170))
        surface1.blit(T1_hand3_image, (440, 170))
        surface1.blit(Card_back, (540, 170))
        # player's hands
        # player 1
        surface1.blit(main_Char_hand0_image, (320, 350))
        surface1.blit(main_Char_hand1_image, (420, 350))
        # player 2
        surface1.blit(Card_back, (0, 0))
        surface1.blit(Card_back, (100, 0))
        # player 3
        surface1.blit(Card_back, (610, 0))
        surface1.blit(Card_back, (710, 0))
        # determine player turn and display it
        if(main_Char_Turn == True):
            textPlayer_Turn = style2.render("its Your Turn.", True, (0,0,0))
            surface1.blit(textPlayer_Turn, (320,0))
        elif(other_Char1_Turn == True):
            textPlayer_Turn = style2.render("its Player Two's Turn.", True, (0,0,0))
            surface1.blit(textPlayer_Turn, (280,0))
        else:
            textPlayer_Turn = style2.render("its Player Three's Turn.", True, (0,0,0))
            surface1.blit(textPlayer_Turn, (270,0))
    elif (round_Counter == 4):
        # Table hand (The Turn)
        surface1.blit(T1_hand0_image, (140, 170))
        surface1.blit(T1_hand1_image, (240, 170))
        surface1.blit(T1_hand2_image, (340, 170))
        surface1.blit(T1_hand3_image, (440, 170))
        surface1.blit(T1_hand4_image, (540, 170))
        # player's hands
        # player 1
        surface1.blit(main_Char_hand0_image, (320, 350))
        surface1.blit(main_Char_hand1_image, (420, 350))
        # player 2
        surface1.blit(Card_back, (0, 0))
        surface1.blit(Card_back, (100, 0))
        # player 3
        surface1.blit(Card_back, (610, 0))
        surface1.blit(Card_back, (710, 0))
        # determine player turn and display it
        if(main_Char_Turn == True):
            textPlayer_Turn = style2.render("its Your Turn.", True, (0,0,0))
            surface1.blit(textPlayer_Turn, (320,0))
        elif(other_Char1_Turn == True):
            textPlayer_Turn = style2.render("its Player Two's Turn.", True, (0,0,0))
            surface1.blit(textPlayer_Turn, (280,0))
        else:
            textPlayer_Turn = style2.render("its Player Three's Turn.", True, (0,0,0))
            surface1.blit(textPlayer_Turn, (270,0))
    elif (round_Counter == 5):
        # Table hand (Reveal all Cards)
        surface1.blit(T1_hand0_image, (140, 170))
        surface1.blit(T1_hand1_image, (240, 170))
        surface1.blit(T1_hand2_image, (340, 170))
        surface1.blit(T1_hand3_image, (440, 170))
        surface1.blit(T1_hand4_image, (540, 170))
        # player's hands
        # player 1
        surface1.blit(main_Char_hand0_image, (320, 350))
        surface1.blit(main_Char_hand1_image, (420, 350))
        # player 2
        surface1.blit(other_Char1_hand0_image, (0, 0))
        surface1.blit(other_Char1_hand1_image, (100, 0))
        # player 3
        surface1.blit(other_Char2_hand0_image, (610, 0))
        surface1.blit(other_Char2_hand1_image, (710, 0))
        # determine winner and display it
        if(main_Char_Win == True):
            textWin = style2.render("YOU WON!", True, (0,0,0))
            surface1.blit(textWin, (340,0))
        elif(other_Char1_Win == True):
            textWin = style2.render("Player Two Wins.", True, (0,0,0))
            surface1.blit(textWin, (310,0))
        elif(other_Char2_Win == True):
            textWin = style2.render("Player Three Wins.", True, (0,0,0))
            surface1.blit(textWin, (310,0))
        else:
            textWin = style2.render("Its a Tie.", True, (0,0,0))
            surface1.blit(textWin, (340,0))
    # update screen
    pygame.display.flip()
    sleep(0.5)

# funtion to determine card image from the data received from main player
def determineImage(num, suit):
    if(suit == "'clubs'"):
        suit = "C"
    elif(suit == "'spades'"):
        suit = "S"
    elif(suit == "'diamonds'"):
        suit = "D"
    elif(suit == "'hearts'"):
        suit = "H"

    print(num)
    print(suit)
    if(int(num) < 11):
        fileLocation = "{}{}.png".format(num, suit)
    elif(int(num) == 11):
        fileLocation = "J{}.png".format(suit)
    elif(int(num) == 12):
        fileLocation = "Q{}.png".format(suit)
    elif(int(num) == 13):
        fileLocation = "K{}.png".format(suit)
    elif(int(num) == 14):
        fileLocation = "A{}.png".format(suit)
        
     
    return (pygame.transform.scale(
                pygame.image.load("Deck of Cards (PNG)/PNG/{}".format(fileLocation)),
                (90, 90)))  # may need to edit file location depending on which folder it is in

# function used to convert stringed Boolean values sent
# from the main player back to Boolean values
def determineBool(Bool):
    if(Bool == "False"):
        Bool = False
    elif(Bool == "True"):
        Bool = True
    return Bool

# assign card back from card image files
Card_back = pygame.transform.scale(pygame.image.load("Deck of Cards (PNG)/PNG/gray_back.png"), (90,90))


Entire_Game = True

while(Entire_Game):
    # NOTE data from main player is sent in a very specific order
    # that is why we append specific indecies to certain variables
    data = UDP_client()
    
    # get table hand from server pi
    num = int(data[0])
    suit = data[1]
    T1_hand0_image = determineImage(num, suit)
    num = int(data[2])
    suit = data[3]
    T1_hand1_image = determineImage(num, suit)
    num = int(data[4])
    suit = data[5]
    T1_hand2_image = determineImage(num, suit)
    num = int(data[6])
    suit = data[7]
    T1_hand3_image = determineImage(num, suit)
    num = int(data[8])
    suit = data[9]
    T1_hand4_image = determineImage(num, suit)

    # get other Player 1 hands from server pi
    num = int(data[10])
    suit = data[11]
    other_Char2_hand0_image = determineImage(num, suit)
    num = int(data[12])
    suit = data[13]
    other_Char2_hand1_image = determineImage(num, suit)

    # get main player 2 hands from server pi
    num = int(data[14])
    suit = data[15]
    other_Char1_hand0_image = determineImage(num, suit)
    num = int(data[16])
    suit = data[17]
    other_Char1_hand1_image = determineImage(num, suit)

    # get other player 3 hands from server pi
    num = int(data[18])
    suit = data[19]
    main_Char_hand0_image = determineImage(num, suit)
    num = int(data[20])
    suit = data[21]
    main_Char_hand1_image = determineImage(num, suit)


    game = True

    while(game):
        # NOTE data from main player is sent in a very specific order
        # that is why we append specific indecies to certain variables
        data = UDP_client()
        round_Counter = int(data[0])
        other_Char2_current_Bet = int(data[1])
        other_Char2_purse = int(data[2])
        T1_pot = int(data[3])
        other_Char1_current_Bet = int(data[4])
        other_Char1_purse = int(data[5])
        main_Char_current_Bet = int(data[6])
        main_Char_purse = int(data[7])

        other_Char2_Turn = determineBool(data[9])
        other_Char1_Turn = determineBool(data[11])
        main_Char_Turn = determineBool(data[13])

        other_Char2_Win = determineBool(data[10])
        other_Char1_Win = determineBool(data[12])
        main_Char_Win = determineBool(data[14])
        
        # send all of this data to the GUI in order to update it accordingly for the second player's screen
        updateScreen(round_Counter, main_Char_hand0_image, main_Char_hand1_image, main_Char_current_Bet, main_Char_purse, T1_hand0_image, T1_hand1_image, T1_hand2_image, T1_hand3_image, T1_hand4_image, T1_pot, other_Char1_hand0_image, other_Char1_hand1_image, other_Char1_current_Bet, other_Char1_purse, other_Char2_hand0_image, other_Char2_hand1_image, other_Char2_current_Bet, other_Char2_purse, main_Char_Turn, main_Char_Win, other_Char1_Turn, other_Char1_Win, other_Char2_Turn, other_Char2_Win)
        
        # here we check if the round of everyone's current hands is still going on
        game = bool(int(data[8]))
        print(game)
        
