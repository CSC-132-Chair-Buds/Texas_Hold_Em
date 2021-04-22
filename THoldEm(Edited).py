# we will have the overarching classes here
from random import randint

# import time
from time import *

# Importing and initializing pygame for GUI purposes (Clay)
import pygame
pygame.init()

surface1= pygame.display.set_mode((1500,800))


class Card:
    # class variable of back of card
    back = pygame.transform.scale(pygame.image.load("Deck of Cards (PNG)/PNG/gray_back.png"),(150,150))
    
    def __init__(self, number, suit = " ", image = " "):

        self.number = number
        self.suit = suit
        self.image = image

    # random magic string function for testing purposes
    def __str__(self):
        return "{} of {}".format(self.number, self.suit)

class Player:

    def __init__(self, bet=0, purse = 1000, fold=0, win=0):
        # bet is an integer corresponding to the bet value yet to be 'placed'
        # purse is an integer corresponding to the players money left in their pocket
        # fold is a boolean starting at "NO" for player not wanting to fold
        # win is also a boolean starting at "NO" for the player has not yet won, will be changed later in the game class
        self.current_Bet = bet
        self.hand = []
        self.purse = purse
        self.fold = fold
        self.win = win



    def win(self):
        pass

    # clears player hand after a game has been won
    def clear_Hand(self):
        self.hand = []

    # removes the current Bet from the players remaining purse value
    # adds that current Bet to the value of the table's pot
    def make_Bet(self):
        self.purse-=self.current_Bet
        Table1.pot+=self.current_Bet
    def make_Small_Blind(self):
        self.current_Bet = small_Blind
    def make_Big_Blind(self):
        self.current_Bet = big_Blind
    def fold(self):
        self.fold = 1
    def change_Bet(self):
        # Raise Bet
        #GPIO FOR XX SPACE ==HIGH
        if (1==0):#GPIO FOR XX SPACE FOR RAISING BET == HIGH
            #raise the current bet for the player by the increment
            self.current_Bet+=INCREMENT

        # Lower Bet
        ## GPIO FOR XX SPACE == LOW
        if (1==0): #GPIO INPUT FOR XX SPACE FOR LOWERING BET ==HIGH
            # lower the current bet for the player by the hardcoded increment
            self.current_Bet-=INCREMENT



class Table():
    def __init__(self, deck=[], pot = 0, hand = []):
        self.hand = hand
        self.deck = deck
        self.pot = pot

    # 'reset' the table after a game has been won
    def wipe_Clean(self):
        self.hand = []
        self.deck = []
        self.pot = 0

    # create a new deck with randomized locations for each of the card instantiations
    # identical with pulling in all the cards from the table and shuffling them
    def shuffle(self):

        # Build the deck; nested for loops to generate one of each card
        newDeck = []

        # run through the integers assosciated with each card and integer assosciated with each suit,
        # generate a card for each one and append it to the newDeck list which is ordered, we need to shuffle it still
        for i in range(2,15):
            for j in range(4):
                if(i<11):
                    if j == 0:
                        suitIn = 'clubs'
                        s = "C"
                    if j == 1:
                        suitIn = 'spades'
                        s = "S"
                    if j == 2:
                        suitIn = 'diamonds'
                        s = "D"
                    if j == 3:
                        suitIn = 'hearts'
                        s = "H"
                    fileLocation = "{}{}.png".format(str(i),s)
                elif(i==11):
                    if j == 0:
                        suitIn = 'clubs'
                        s = "C"
                    if j == 1:
                        suitIn = 'spades'
                        s = "S"
                    if j == 2:
                        suitIn = 'diamonds'
                        s = "D"
                    if j == 3:
                        suitIn = 'hearts'
                        s = "H"
                    fileLocation = "J{}.png".format(s)
                elif(i==12):
                    if j == 0:
                        suitIn = 'clubs'
                        s = "C"
                    if j == 1:
                        suitIn = 'spades'
                        s = "S"
                    if j == 2:
                        suitIn = 'diamonds'
                        s = "D"
                    if j == 3:
                        suitIn = 'hearts'
                        s = "H"
                    fileLocation = "K{}.png".format(s)
                elif(i==13):
                    if j == 0:
                        suitIn = 'clubs'
                        s = "C"
                    if j == 1:
                        suitIn = 'spades'
                        s = "S"
                    if j == 2:
                        suitIn = 'diamonds'
                        s = "D"
                    if j == 3:
                        suitIn = 'hearts'
                        s = "H"
                    fileLocation = "Q{}.png".format(s)
                elif(i==14):
                    if j == 0:
                        suitIn = 'clubs'
                        s = "C"
                    if j == 1:
                        suitIn = 'spades'
                        s = "S"
                    if j == 2:
                        suitIn = 'diamonds'
                        s = "D"
                    if j == 3:
                        suitIn = 'hearts'
                        s = "H"
                    fileLocation = "A{}.png".format(s)
                # append an instance (the value, suit, and image (rescale image here and load it))
                                                                        # load image here                                                   # resize image here
                newDeck.append(Card(i, suitIn, pygame.transform.scale(pygame.image.load("Deck of Cards (PNG)/PNG/{}".format(fileLocation)),(150,150))))         #may need to edit file location depending on which folder it is in

        # we have an ordered deck stored as newDeck we still need to shuffle it
        # imagine taking a card out of an ordered deck randomly, and simply laying that randomly chosen card
        # at the top of the new 'shuffled' deck; of course you will be removing that card from the ordered deck as you do
        # and boom shuffled deck of cards at the end of the iterations.

        for i in range(52):
            randomIndice = randint(0,(len(newDeck))-1)
            self.deck.append(newDeck[randomIndice])
            del newDeck[randomIndice]

# function to easily adjust surface display
def updateScreen(roundCounter):
    # make background green (using HEX for RGB values)
    surface1.fill((0x8FDA87))

    if(roundCounter < 2):
        # Table hand
        surface1.blit(Card.back,(400,350))
        surface1.blit(Card.back,(560,350))
        surface1.blit(Card.back,(720,350))
        surface1.blit(Card.back,(880,350))
        surface1.blit(Card.back,(1040,350))

        # player's hands
        # player 1
        surface1.blit(Table1.deck[9].image,(600,700))
        surface1.blit(Table1.deck[50].image,(760,700))
        # player 2
        surface1.blit(Card.back,(0,0))
        surface1.blit(Card.back,(160,0))
        # player 3
        surface1.blit(Card.back,(1200,0))
        surface1.blit(Card.back,(1360,0))

    elif(roundCounter == 2):
        # Table hand (The Flop)
        surface1.blit(Table1.deck[0].image,(400,350))
        surface1.blit(Table1.deck[1].image,(560,350))
        surface1.blit(Table1.deck[12].image,(720,350))
        surface1.blit(Card.back,(880,350))
        surface1.blit(Card.back,(1040,350))

        # player's hands
        # player 1
        surface1.blit(Table1.deck[9].image,(600,700))
        surface1.blit(Table1.deck[50].image,(760,700))
        # player 2
        surface1.blit(Card.back,(0,0))
        surface1.blit(Card.back,(160,0))
        # player 3
        surface1.blit(Card.back,(1200,0))
        surface1.blit(Card.back,(1360,0))

    elif(roundCounter == 3):
        # Table hand (The Turn)
        surface1.blit(Table1.deck[0].image,(400,350))
        surface1.blit(Table1.deck[1].image,(560,350))
        surface1.blit(Table1.deck[12].image,(720,350))
        surface1.blit(Table1.deck[16].image,(880,350))
        surface1.blit(Card.back,(1040,350))

        # player's hands
        # player 1
        surface1.blit(Table1.deck[9].image,(600,700))
        surface1.blit(Table1.deck[50].image,(760,700))
        # player 2
        surface1.blit(Card.back,(0,0))
        surface1.blit(Card.back,(160,0))
        # player 3
        surface1.blit(Card.back,(1200,0))
        surface1.blit(Card.back,(1360,0))

    elif(roundCounter == 4):
        # Table hand (The Turn)
        surface1.blit(Table1.deck[0].image,(400,350))
        surface1.blit(Table1.deck[1].image,(560,350))
        surface1.blit(Table1.deck[12].image,(720,350))
        surface1.blit(Table1.deck[16].image,(880,350))
        surface1.blit(Table1.deck[45].image,(1040,350))

        # player's hands
        # player 1
        surface1.blit(Table1.deck[9].image,(600,700))
        surface1.blit(Table1.deck[50].image,(760,700))
        # player 2
        surface1.blit(Card.back,(0,0))
        surface1.blit(Card.back,(160,0))
        # player 3
        surface1.blit(Card.back,(1200,0))
        surface1.blit(Card.back,(1360,0))

    elif(roundCounter == 5):
        # Table hand (Reveal all Cards)
        surface1.blit(Table1.deck[0].image,(400,350))
        surface1.blit(Table1.deck[1].image,(560,350))
        surface1.blit(Table1.deck[12].image,(720,350))
        surface1.blit(Table1.deck[16].image,(880,350))
        surface1.blit(Table1.deck[45].image,(1040,350))

        # player's hands
        # player 1
        surface1.blit(Table1.deck[9].image,(600,700))
        surface1.blit(Table1.deck[50].image,(760,700))
        # player 2
        surface1.blit(Table1.deck[23].image,(0,0))
        surface1.blit(Table1.deck[10].image,(160,0))
        # player 3
        surface1.blit(Table1.deck[8].image,(1200,0))
        surface1.blit(Table1.deck[4].image,(1360,0))

    # update screen
    pygame.display.flip()


INCREMENT = 10
STARTING_BET = 10



Table1 = Table()
Table1.shuffle()

updateScreen(1)
sleep(5)
updateScreen(2)
sleep(5)
updateScreen(3)
sleep(5)
updateScreen(4)
sleep(5)
updateScreen(5)
