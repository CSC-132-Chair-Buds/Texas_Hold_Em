import socket
import pygame
from time import sleep
pygame.init()

surface1 = pygame.display.set_mode((800,450))

# function to recieve messages from client
# takes the five parameters needed to update
# the gui
def UDP_server(round_Counter, main_Player, T1, other_Player1, other_Player2):
    host = "127.0.0.1"
    port = 65432

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = [round_Counter, main_Player, T1, other_Player1, other_Player2]
    newData = []
    for msg in data:
        if(msg == int):
            msg = 'i' + str(msg)
            newData.append(msg)
        else:
            msg = 's' + str(msg)
            newData.append(msg)
        sock.sendto(bytes(msg, "utf-8"), (host, port))
    
    
# function to send a message of str or int to the server
def UDP_client():
    host = "127.0.0.1"
    port = 65432

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind((host, port))    
    data, addr = sock.recvfrom(1024)
    data = data[1:-1]
    data = data.decode("utf-8")
    data = data.split(", ")
    print(data)
    
    return data

def UDP_client2():
    host = "127.0.0.1"
    port = 65432

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind((host, port))    
    data, addr = sock.recvfrom(1024)
    data = data.decode("utf-8")
    
    return data

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
        #determine player turn
        if(main_Char_Turn == True):
            textPlayer_Turn = style2.render("It's Your Turn.", True, (0,0,0))
            surface1.blit(textPlayer_Turn, (320,0))
        elif(other_Char1_Turn == True):
            textPlayer_Turn = style2.render("It's Player Two's Turn.", True, (0,0,0))
            surface1.blit(textPlayer_Turn, (280,0))
        else:
            textPlayer_Turn = style2.render("It's Player Three's Turn.", True, (0,0,0))
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
        #determine player turn
        if(main_Char_Turn == True):
            textPlayer_Turn = style2.render("It's Your Turn.", True, (0,0,0))
            surface1.blit(textPlayer_Turn, (320,0))
        elif(other_Char1_Turn == True):
            textPlayer_Turn = style2.render("It's Player Two's Turn.", True, (0,0,0))
            surface1.blit(textPlayer_Turn, (280,0))
        else:
            textPlayer_Turn = style2.render("It's Player Three's Turn.", True, (0,0,0))
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
        #determine player turn
        if(main_Char_Turn == True):
            textPlayer_Turn = style2.render("It's Your Turn.", True, (0,0,0))
            surface1.blit(textPlayer_Turn, (320,0))
        elif(other_Char1_Turn == True):
            textPlayer_Turn = style2.render("It's Player Two's Turn.", True, (0,0,0))
            surface1.blit(textPlayer_Turn, (280,0))
        else:
            textPlayer_Turn = style2.render("It's Player Three's Turn.", True, (0,0,0))
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
        #determine player turn
        if(main_Char_Turn == True):
            textPlayer_Turn = style2.render("It's Your Turn.", True, (0,0,0))
            surface1.blit(textPlayer_Turn, (320,0))
        elif(other_Char1_Turn == True):
            textPlayer_Turn = style2.render("It's Player Two's Turn.", True, (0,0,0))
            surface1.blit(textPlayer_Turn, (280,0))
        else:
            textPlayer_Turn = style2.render("It's Player Three's Turn.", True, (0,0,0))
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
        # determine winner
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
            textWin = style2.render("It's a Tie.", True, (0,0,0))
            surface1.blit(textWin, (340,0))

    # update screen
    pygame.display.flip()
    sleep(0.5)

# funtion to determine card image
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


def determineBool(Bool):
    if(Bool == "False"):
        Bool = False
    elif(Bool == "True"):
        Bool = True
    return Bool

# assign card back
Card_back = pygame.transform.scale(pygame.image.load("Deck of Cards (PNG)/PNG/gray_back.png"), (90,90))

Entire_Game = True

while(Entire_Game):
    # get table hand from server pi
    data = UDP_client()
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
    other_Char1_hand0_image = determineImage(num, suit)
    num = int(data[12])
    suit = data[13]
    other_Char1_hand1_image = determineImage(num, suit)

    # get main player 2 hands from server pi
    num = int(data[14])
    suit = data[15]
    main_Char_hand0_image = determineImage(num, suit)
    num = int(data[16])
    suit = data[17]
    main_Char_hand1_image = determineImage(num, suit)

    # get other player 3 hands from server pi
    num = int(data[18])
    suit = data[19]
    other_Char2_hand0_image = determineImage(num, suit)
    num = int(data[20])
    suit = data[21]
    other_Char2_hand1_image = determineImage(num, suit)


    game = True

    while(game):
        data = UDP_client()
        round_Counter = int(data[0])
        other_Char1_current_Bet = int(data[1])
        other_Char1_purse = int(data[2])
        T1_pot = int(data[3])
        main_Char_current_Bet = int(data[4])
        main_Char_purse = int(data[5])
        other_Char2_current_Bet = int(data[6])
        other_Char2_purse = int(data[7])

        other_Char1_Turn = determineBool(data[9])
        main_Char_Turn = determineBool(data[11])
        other_Char2_Turn = determineBool(data[13])

        other_Char1_Win = determineBool(data[10])
        main_Char_Win = determineBool(data[12])
        other_Char2_Win = determineBool(data[14])
        
        updateScreen(round_Counter, main_Char_hand0_image, main_Char_hand1_image, main_Char_current_Bet, main_Char_purse, T1_hand0_image, T1_hand1_image, T1_hand2_image, T1_hand3_image, T1_hand4_image, T1_pot, other_Char1_hand0_image, other_Char1_hand1_image, other_Char1_current_Bet, other_Char1_purse, other_Char2_hand0_image, other_Char2_hand1_image, other_Char2_current_Bet, other_Char2_purse, main_Char_Turn, main_Char_Win, other_Char1_Turn, other_Char1_Win, other_Char2_Turn, other_Char2_Win)

        game = bool(int(data[8]))
        print(game)
        
