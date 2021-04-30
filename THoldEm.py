# we will have the overarching classes here
from random import randint
from time import *

class Card:
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
                if j == 0:
                    suitIn = 'clubs'
                if j == 1:
                    suitIn = 'spades'
                if j == 2:
                    suitIn = 'diamonds'
                if j == 3:
                    suitIn = 'hearts'
                newDeck.append(Card(i, suitIn, "IMAGE FILE LOCATION"))

        # we have an ordered deck stored as newDeck we still need to shuffle it
        # imagine taking a card out of an ordered deck randomly, and simply laying that randomly chosen card
        # at the top of the new 'shuffled' deck; of course you will be removing that card from the ordered deck as you do
        # and boom shuffled deck of cards at the end of the iterations.

        for i in range(52):
            randomIndice = randint(0,(len(newDeck))-1)
            self.deck.append(newDeck[randomIndice])
            del newDeck[randomIndice]





INCREMENT = 10
STARTING_BET = 10

Table1 = Table()
Table1.shuffle()
print (Table1.deck)




