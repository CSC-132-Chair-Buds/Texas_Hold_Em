from itertools import combinations

import numpy as np
import pandas as pd


class Card:

    def __init__(self, number, suit = " ", image = " " ):

        self.number = number
        self.suit = suit
        # all cards start with their face 'showing' will need to use self.set_Back to flip the card over to its back
        self.image = image
        self.face = image
        self.deck = []

    # random magic string function for testing purposes
    def __str__(self):
        return "{} of {}".format(self.number, self.suit)

    def __repr__(self):
        return "{} of {}".format(self.number, self.suit)

    def shuffle(self):

        # Build the deck; nested for loops to generate one of each card
        newDeck = []

        # run through the integers assosciated with each card and integer assosciated with each suit,
        # generate a card for each one and append it to the newDeck list which is ordered, we need to shuffle it still
        for i in range(2, 15):
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
            randomIndice = randint(0, (len(newDeck)) - 1)
            self.deck.append(newDeck[randomIndice])
            del newDeck[randomIndice]


class Player:

    def __init__(self,name, bet=0, purse = 1000, fold=False, win=False, round_Bet=0, handstrength=0):
        # bet is an integer corresponding to the bet value yet to be 'placed'
        # purse is an integer corresponding to the players money left in their pocket
        # fold is a boolean starting at "NO" for player not wanting to fold
        # win is also a boolean starting at "NO" for the player has not yet won, will be changed later in the game class
        self.current_Bet = bet
        self.hand = []
        self.purse = purse
        self.fold = fold
        self.win = win
        self.round_Bet = round_Bet
        self.name = name
        self.handstrength = handstrength



    def __str__(self):
        return self.name



    def win(self):
        pass

    # clears player hand after a game has been won or they have folded
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
    def makefold(self):
        self.fold = True

P1 = Player('P1')
P2 = Player('P2')
P3 = Player('P3')
#player 4 serving as table hand
Table = Player('Table')
P1.hand = [Card(10, 'spades'), Card (9, 'spades')]
P2.hand = [Card(7, 'clubs'), Card (6,'hearts')]
P3.hand = [Card(11, 'clubs'), Card (8,'clubs')]
Table.hand = [Card(13, 'spades'), Card(11, 'spades'), Card(7, 'clubs'), Card(12, 'spades'), Card(7, 'clubs')]
allCards=P1.hand+Table.hand



def compareHands():
    # set up the hand judging algorithim for each of the players in the round still

    P_List1 = [P1, P2, P3]
    P_List = []
    # remove players from the list if they've folded this round; RESET IT FOR NEXT ROUND
    for player in P_List1:
        if (player.fold==False):
            P_List.append(player)

    # yeah you get it iterate for each player still left
    for player in P_List:
        # create a list for each player of the table hand (5 cards) and their pocket cards (2 cards)
        # then create a unique list for each one containing the integer values for each card and the suits
        all_Cards = player.hand + Table.hand
        values = []
        suits = []
        hand_Values = []
        pair_Counter = 0


        #instantiate the hand comparisons to false until the algorithim runs for each player
        pair = False
        two_Pair = False
        TOK = False
        straight = False
        flush = False
        full_House = False
        FOK = False
        straight_Flush = False
        royal_Flush = False

        # set the values and suits of each card available to each player to seperate lists for ease
        for card in all_Cards:
            values.append(card.number)
            suits.append(card.suit)
        # not sure if this is needed anymore but dont wanna break it
        valuesNsuits = list(zip(values, suits))
        values.sort()


        # simply add the value of the highcard to the players count; if no other hands are 'gleaned'
        # then this single number represents the strength of their hand based on the highcard
        player.handstrength += max(values)

        #RECOGNIZE THAT THE LIST ASSESSMENT WILL 'BING' TWICE BECAUSE ITLL RECOGNIZE A PAIR TWICE IN THE LIST AS IT STEPS THROUGH
        # BECAUSE ITS CHECKING FOR DUPLICATES ON EACH ENTRY
        # iterate through each card integer value in the hand
        for value in values:
            # TEST FOR DIFFERENT HAND POSSIBILITIES IN ASCENDING VALUE (KINDA); we've already taken care of high card
            #PAIR TEST
            # if theres a duplicate of an integer than theres a pair
            if values.count(value)==2:
                pair_Counter += 1
                pair = True


            # TWO PAIR TEST; PIGGYBACK OFF OF PAIR TEST PINGING TWICE
            # if the previous loop binged 4 times this means there was two sets of pairs
            if pair_Counter == 4:
                two_Pair = True



            # THREE OF A KIND TEST
            # if theres a triplet of an integer value of a card then three of a kind (TOK; not the Tik variety)
            if values.count(value)==3:
                TOK = True

            # FOUR OF A KIND TEST
            # put this up here (not the next highest ranking hand) just to make use of the for loop thats already here
            # next highest ranking hand is actually straight
            # same logic; a quadruplet of integer value then a four of a kind (FOK)
            if values.count(value)==4:
                FOK = True

        # STRAIGHT TEST ( 5 cards in ascending consecutive order)
        # dedent because you dont need to do this for every single card in someones hand... Lot of wasted power
        # creates all possible combinations of 5 cards out of the seven on the table in a tuple
        # then compares the hardcoded list of tuples that equal a poker 'straight' to that list of tuples
        # if any of them return true then the player has a straight possible

        comb = list(combinations(values, 5))
        straights = [(2, 3, 4, 5, 6), (3, 4, 5, 6, 7), (4, 5, 6, 7, 8), (5, 6, 7, 8, 9), (6, 7, 8, 9, 10),
                     (7, 8, 9, 10, 11), (8, 9, 10, 11, 12), (9, 10, 11, 12, 13), (10, 11, 12, 13, 14)]

        # if a group denoted in the hardcoded list of possible straights is found in the possible hand combinations
        # available to a player then they have a straight

        for group in straights:
            if group in comb:
                straight = True
                straight_Set = sorted(group)
                # denote which set corresponded with a straight for later


        # FLUSH TEST (5 cards with the same suit)
        # simply run through each suit in the combined player/table hand and see if theres five of the same suit
        for suit in suits:
            if suits.count(suit)>=5:
                flush = True

        # FULL HOUSE TEST (a pair and a TOK)
        # simply piggy back off of our previous determinations; if they're both true for a player then they have a full house
        if ((TOK == True) and (pair==True)):
            full_House = True


        # STRAIGHT FLUSH TEST;
        if straight == True:
            #LIST COMPREHENSION DOES SOMETHING :)))
            # create a new list of tuples; adding the (value, suit) pair for each card responsible for the straight
            ComboStraight = [item for item in valuesNsuits for i in straight_Set if item[0]==i]

            # create counter for loop; shoutout brians' logic for betting round;
            # if the suit of each card responsible for the straight is the same suit as the first
            # and this comparison makes it all the way through the list then we have a straight flush
            n=0
            for i in range(len(ComboStraight)):
                if ComboStraight[0][1]==ComboStraight[i][1]:
                    n+=1
            # if the counter has made it to or past five then the cards responsible for the straight
            # all have the same suit. Duplicates can happen here based on integer comparison despite it not being the card
            # 'used' in the straight; so as long as it is at or above five we're good
            if n>=5:
                straight_Flush = True

        # ROYAL FLUSH TEST:
        # once again piggy back to get a chunk of code out of the way:
        # if theres a straight flush and the cards are the 5 highest; a royal flush has happened
        if ((straight_Flush == True) and (sorted(straight_Set)==[10,11,12,13,14])):
            royal_Flush = True

        # Lets do an elif tree to denote the strongest 'hand' they had which would be what you would call out
        # at the end of the poker hand; elif makes it to where the first read line that is true will be the
        # only one ran through; so putting the conditionals in descending order gives us the highest strength hand
        if (royal_Flush== True):
            player.handstrength += 1000
        elif (straight_Flush == True):
            player.handstrength += 900
        elif (FOK == True):
            player.handstrength += 800
        elif (full_House == True):
            player.handstrength += 700
        elif (flush == True):
            player.handstrength += 600
        elif (straight == True):
            player.handstrength += 500
        elif (TOK == True):
            player.handstrength += 400
        elif (two_Pair == True):
            player.handstrength += 300
        elif (pair == True):
            player.handstrength += 200


    # now lets simply compare their handstrengths to see who the winners are; give them the pot
    # and set the pot back equal to zero
    if ((P1.handstrength > P2.handstrength) and (P1.handstrength > P3.handstrength)):
        P1.purse += Table.pot
        Table.pot = 0
        print ("Player 1 is the winner")
    elif ((P2.handstrength > P1.handstrength) and (P2.handstrength > P3.handstrength)):
        P2.purse += Table.pot
        Table.pot = 0
        print ("Player 2 is the winner")
    elif ((P3.handstrength > P2.handstrength) and (P3.handstrength > P2.handstrength)):
        print ("Player 3 is the winner")
        P3.purse += Table.pot
        Table.pot = 0

    print(P3.handstrength)
    print (P1.handstrength)

compareHands()


