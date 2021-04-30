# we will have the overarching classes here
from random import randint
import numpy as np
import pandas
import pygame
import time
import RPi.GPIO as GPIO

pygame.init()
surface1 = pygame.display.set_mode((1500, 800))
GPIO.setmode(GPIO.BCM)
round_Counter = 0

# P1 is just the player that we want to have being the 'main character'
def updateScreen(round_Counter, main_Char, T1, other_Char1, other_Char2):
    # make background green (using HEX for RGB values)
    surface1.fill((0x8FDA87))

    # put table pot, player's pot and bet on display
    style = pygame.font.Font(None, 40)
    textPBet = style.render("Your Current Bet $()".format(main_Char.current_Bet), True, 0x000000)
    textPPurse = style.render("Your Purse ${}".format(main_Char.purse), True, 0x000000)
    textTPot = style.render("Table pot ${}".format(T1.pot), True, 0x000000)
    surface1.blit(textPBet, (0, 680))
    surface1.blit(textPPurse, (0, 720))
    surface1.blit(textTPot, (0, 760))

    if (round_Counter < 2):
        # Table hand
        surface1.blit(Card.back, (400, 350))
        surface1.blit(Card.back, (560, 350))
        surface1.blit(Card.back, (720, 350))
        surface1.blit(Card.back, (880, 350))
        surface1.blit(Card.back, (1040, 350))

        # player's hands
        # player 1
        surface1.blit(main_Char.hand[0].image, (600, 700))
        surface1.blit(main_Char.hand[1].image, (760, 700))
        # player 2
        surface1.blit(Card.back, (0, 0))
        surface1.blit(Card.back, (160, 0))
        # player 3
        surface1.blit(Card.back, (1200, 0))
        surface1.blit(Card.back, (1360, 0))

    elif (round_Counter == 2):
        # Table hand (The Flop)
        surface1.blit(T1.hand[0].image, (400, 350))
        surface1.blit(T1.hand[1].image, (560, 350))
        surface1.blit(T1.hand[2].image, (720, 350))
        surface1.blit(Card.back, (880, 350))
        surface1.blit(Card.back, (1040, 350))

        # player's hands
        # player 1
        surface1.blit(main_Char.hand[0].image, (600, 700))
        surface1.blit(main_Char.hand[1].image, (760, 700))
        # player 2
        surface1.blit(Card.back, (0, 0))
        surface1.blit(Card.back, (160, 0))
        # player 3
        surface1.blit(Card.back, (1200, 0))
        surface1.blit(Card.back, (1360, 0))

    elif (round_Counter == 3):
        # Table hand (The Turn)
        surface1.blit(T1.hand[0].image, (400, 350))
        surface1.blit(T1.hand[1].image, (560, 350))
        surface1.blit(T1.hand[2].image, (720, 350))
        surface1.blit(T1.hand[3].image, (880, 350))
        surface1.blit(Card.back, (1040, 350))

        # player's hands
        # player 1
        surface1.blit(main_Char.hand[0].image, (600, 700))
        surface1.blit(main_Char.hand[1].image, (760, 700))
        # player 2
        surface1.blit(Card.back, (0, 0))
        surface1.blit(Card.back, (160, 0))
        # player 3
        surface1.blit(Card.back, (1200, 0))
        surface1.blit(Card.back, (1360, 0))

    elif (round_Counter == 4):
        # Table hand (The Turn)
        surface1.blit(T1.hand[0].image, (400, 350))
        surface1.blit(T1.hand[1].image, (560, 350))
        surface1.blit(T1.hand[2].image, (720, 350))
        surface1.blit(T1.hand[3].image, (880, 350))
        surface1.blit(T1.hand[4].image, (1040, 350))

        # player's hands
        # player 1
        surface1.blit(main_Char.hand[0].image, (600, 700))
        surface1.blit(main_Char.hand[1].image, (760, 700))
        # player 2
        surface1.blit(Card.back, (0, 0))
        surface1.blit(Card.back, (160, 0))
        # player 3
        surface1.blit(Card.back, (1200, 0))
        surface1.blit(Card.back, (1360, 0))

    elif (round_Counter == 5):
        # Table hand (Reveal all Cards)
        surface1.blit(T1.hand[0].image, (400, 350))
        surface1.blit(T1.hand[1].image, (560, 350))
        surface1.blit(T1.hand[2].image, (720, 350))
        surface1.blit(T1.hand[3].image, (880, 350))
        surface1.blit(T1.hand[4].image, (1040, 350))

        # player's hands
        # player 1
        surface1.blit(main_Char.hand[0].image, (600, 700))
        surface1.blit(main_Char.hand[1].image, (760, 700))
        # player 2
        surface1.blit(other_Char1.hand[0].image, (0, 0))
        surface1.blit(other_Char1.hand[1].image, (160, 0))
        # player 3
        surface1.blit(other_Char2.hand[0].image, (1200, 0))
        surface1.blit(other_Char2.hand[1].image, (1360, 0))

    # update screen
    pygame.display.flip()



class Card:
    back=pygame.transform.scale(pygame.image.load("gray_back.png"), (120,120))
    def __init__(self, number, suit = " ", image = " " ):

        self.number = number
        self.suit = suit
        # all cards start with their face 'showing' will need to use self.set_Back to flip the card over to its back
        self.image = image
        self.face = image

        # random magic string function for testing purposes
        def __str__(self):
            return "{} of {}".format(self.number, self.suit)

        # set the image of the card to the back of card image
        def set_Back(self):
            self.image = back

        def set_Face(self):
            self.image = self.face

class Player:

    def __init__(self, betpin, raisepin, lowerpin, foldpin, bet=0, purse = 1000, fold=False, win=False, round_Bet=0):
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
        self.betpin = betpin
        self.raisepin = raisepin
        self.lowerpin  = lowerpin
        self.foldpin = foldpin

        GPIO.setup(betpin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(raisepin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(lowerpin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        GPIO.setup(foldpin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)






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
    def fold(self):
        self.fold = 1


    def change_Bet(self, minimum_bet):
        self.current_Bet = minimum_bet
        if self == P1:
            otherChar1 = P2
            otherChar2 = P3

        if self == P2:
            otherChar1 = P1
            otherChar2 = P3

        if self == P3:
            otherChar1 = P1
            otherChar2 = P2


        #infinite while loop
        if (minimum_bet > self.purse):
            # DO SOME STUFF
            self.fold = True

        while (True):
            # if raise pin is pressed, increase that current bet by the increment (10)
            if (GPIO.input(self.raisepin) == GPIO.HIGH) and (self.current_Bet < self.purse):
                self.current_Bet += 10
                updateScreen(round_Counter, self, T1, otherChar1, otherChar2)

            # if the decrease button is pressed decrase the current bet by the increment
            if (GPIO.input(self.lowerpin) == GPIO.HIGH) and (self.current_Bet > minimum_bet):
                self.current_Bet -= 10
                updateScreen(round_Counter, self, T1, otherChar1, otherChar2)


            # if the fold pin has been pressed; make the player boolean responsible for declaring their fold status True
            if (GPIO.input(self.foldpin) == GPIO.HIGH):
                self.fold = True
                return

            # if the bet pin has been pressed
            if (GPIO.input(self.betpin) == GPIO.HIGH):
                return

            sleep(0.1)


class Table():
    def __init__(self, seat, deck=[], pot = 0, hand = []):
        self.hand = hand
        self.deck = deck
        self.pot = pot
        self.seat = seat

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
            for i in range(2, 15):
                for j in range(4):
                    if (i < 11):
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
                        fileLocation = "{}{}.png".format(str(i), s)
                    elif (i == 11):
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
                    elif (i == 12):
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
                    elif (i == 13):
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
                    elif (i == 14):
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
                    newDeck.append(Card(i, suitIn, pygame.transform.scale(
                        pygame.image.load("Deck of Cards (PNG)/PNG/{}".format(fileLocation)),
                        (150, 150))))  # may need to edit file location depending on which folder it is in

            # we have an ordered deck stored as newDeck we still need to shuffle it
            # imagine taking a card out of an ordered deck randomly, and simply laying that randomly chosen card
            # at the top of the new 'shuffled' deck; of course you will be removing that card from the ordered deck as you do
            # and boom shuffled deck of cards at the end of the iterations.

            for i in range(52):
                randomIndice = randint(0, (len(newDeck)) - 1)
                self.deck.append(newDeck[randomIndice])
                del newDeck[randomIndice]


class Game:
    # NEED TO TAKE MONEY OUT OF PLAYERS HANDS FOR BIG AND SMALL BLINDS BEFORE CARDS ARE DEALT
    # NEED TO FIGURE OUT HOW TO WAIT FOR A PLAYERS BUTTON PRESS; EITHER HAVE TO PRESS BET OR FOLD
    # WHILE LOOP STOPS IMMEDIATELY ONCE SOMEONE RAISES THE BET AND RE-ASKS PLAYER 1 FOR A BET
    def __init__(self):
        pass

    def startup(self):
        #generate the table and wipe it clean to avoid something stupid

        T1 = Table()
        T1.wipe_Clean()

        # shuffle the cards and generate the deck for the hand to be dealt
        T1.shuffle()

        # we need to instantiate the players for the Game; and sit them at the table
        # their purse is hardcoded at $1000
        P1 = Player(seat = 1)
        P2 = Player(seat = 2)
        P3 = Player(seat = 3)
        Players = [P1, P2, P3]

        # we need to assign blind bets for this game; will do so randomly
        #small blind given randomly then big blind given to the player to the right of him (or circle around to the other side)
        # random number chosen for the small blind
        small_Blind_Random = randint(0,2)
        Players[small_Blind_Random].make_Small_Blind()
        Players[small_Blind_Random].purse -= Players[small_Blind_Random].current_Bet
        T1.pot += Players[small_Blind_Random].current_Bet
        Players[small_Blind_Random].round_Bet += small_Blind



        # if the player chosen is player 3 then the big blind circles around to player 1 in the 0th index
        if (small_Blind_Random==2):
            Players[0].make_Big_Blind()
            Players[0].purse -= Players[0].current_Bet
            T1.pot += Players[0].current_Bet
            Players[0].round_Bet += big_Blind

        # if not; the big blind is given to the player on his right
        else:
            Players[(small_Blind_Random+1)].make_Big_Blind()
            Players[(small_Blind_Random + 1)].purse -= Players[(small_Blind_Random+1)].current_Bet
            T1.pot += Players[(small_Blind_Random+1)].current_Bet
            Players[small_Blind_Random + 1].round_Bet += big_Blind


    def roundOfBetting(self):
        P_List = [P1, P2, P3]
        P_List_Bets = [P1.round_Bet, P2.round_Bet, P3.round_Bet]
       # implement this next line if we want unlimited passes around the table before betting stopped and everyones called
       # if their last bet values are not the same that means someones bet and we need to keep betting
        while(1):
            i = 0
            while (i < len(P_List)):
                # WAIT FOR INPUT SOMEHOW
                # WAIT WAIT WAIT FOR INPUT

                P_List[i].change_Bet(max(P_List_Bets)-P_List[i].round_Bet)
                # IF THEY PRESS THE FOLD BUTTON FOR THEIR INPUT; REMOVE THEM FROM THE LIST AND LET THE SHOW GO ON
                if( P_List[i].fold == True):
                    del P_List[i]

                # STILL NEED TO FIGURE OUT HOW TO SEE IF THEY"RE BETTING THE APPROPRIATE AMOUNT; greater than or equal to the highest bet purse

                # this says if they've pressed the bet button; remove the money from their purse and add that ammount to the table and their round_Bet
                # update the List of round_bets so that we can determine whether or not they're betting the correct ammount

                # IF THE PLAYER HAS THROWN ENOUGH DOWN; ADD AND DELETE THE APPROPRIATE NUMBERS
                # AND UPDATE THE LIST OF THE ROUND BETS
                ##if ((PList[i].current_Bet + PList[i].round_Bet) >= max(P_List_Bets)):
                if( P_List[i].fold == False):
                    P_List[i].purse -= P_List[i].current_Bet
                    P_List[i].round_Bet += P_List[i].current_Bet
                    P_List_Bets = [P1.round_Bet, P2.round_Bet, P3.round_Bet]

                    T1.pot += P_List[i].current_Bet
                i += 1

            # NEW WHILE LOOP
            j = 0
            while (P_List[j].round_Bet == P_List[0].round_Bet):
                # if the while loop has ran the whole time meaning that each consectuive players roundBet is equal to the first players round bet
                # then the betting round is over
                if (j==(len(P_List)-1)):
                    # break out of the loop when the loop has ran through entirely, meaning all players left in the list have equal round bets
                    return
                j += 1


    def compareHands():
        # set up the hand judging algorithim for each of the players in the round still

        P_List1 = [P1, P2, P3]
        P_List = []
        # remove players from the list if they've folded this round; RESET IT FOR NEXT ROUND
        for player in P_List1:
            if (player.fold == False):
                P_List.append(player)

        # yeah you get it iterate for each player still left
        for player in P_List:
            # create a list for each player of the table hand (5 cards) and their pocket cards (2 cards)
            # then create a unique list for each one containing the integer values for each card and the suits
            all_Cards = player.hand + T1.hand
            values = []
            suits = []
            hand_Values = []
            pair_Counter = 0

            # instantiate the hand comparisons to false until the algorithim runs for each player
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

            # RECOGNIZE THAT THE LIST ASSESSMENT WILL 'BING' TWICE BECAUSE ITLL RECOGNIZE A PAIR TWICE IN THE LIST AS IT STEPS THROUGH
            # BECAUSE ITS CHECKING FOR DUPLICATES ON EACH ENTRY
            # iterate through each card integer value in the hand
            for value in values:
                # TEST FOR DIFFERENT HAND POSSIBILITIES IN ASCENDING VALUE (KINDA); we've already taken care of high card
                # PAIR TEST
                # if theres a duplicate of an integer than theres a pair
                if values.count(value) == 2:
                    pair_Number = value
                    pair_Counter += 1
                    pair = True

                # TWO PAIR TEST; PIGGYBACK OFF OF PAIR TEST PINGING TWICE
                # if the previous loop binged 4 times this means there was two sets of pairs
                if pair_Counter == 4:
                    two_Pair = True

                # THREE OF A KIND TEST
                # if theres a triplet of an integer value of a card then three of a kind (TOK; not the Tik variety)
                if values.count(value) == 3:
                    TOK = True

                # FOUR OF A KIND TEST
                # put this up here (not the next highest ranking hand) just to make use of the for loop thats already here
                # next highest ranking hand is actually straight
                # same logic; a quadruplet of integer value then a four of a kind (FOK)
                if values.count(value) == 4:
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
            flushCards = []
            for suit in suits:
                if suits.count(suit) >= 5:
                    flush = True
                    flushCards.append(suit)

            # FULL HOUSE TEST (a pair and a TOK)
            # simply piggy back off of our previous determinations; if they're both true for a player then they have a full house
            if ((TOK == True) and (pair == True)):
                full_House = True

            # STRAIGHT FLUSH TEST;
            if straight == True:
                # LIST COMPREHENSION DOES SOMETHING :)))
                # create a new list of tuples; adding the (value, suit) pair for each card responsible for the straight
                ComboStraight = [item for item in valuesNsuits for i in straight_Set if item[0] == i]

                # create counter for loop; shoutout brians' logic for betting round;
                # if the suit of each card responsible for the straight is the same suit as the first
                # and this comparison makes it all the way through the list then we have a straight flush
                n = 0
                for i in range(len(ComboStraight)):
                    if ComboStraight[0][1] == ComboStraight[i][1]:
                        n += 1
                # if the counter has made it to or past five then the cards responsible for the straight
                # all have the same suit. Duplicates can happen here based on integer comparison despite it not being the card
                # 'used' in the straight; so as long as it is at or above five we're good
                if n >= 5:
                    straight_Flush = True

            # ROYAL FLUSH TEST:
            # once again piggy back to get a chunk of code out of the way:
            # if theres a straight flush and the cards are the 5 highest; a royal flush has happened
            if ((straight_Flush == True) and (sorted(straight_Set) == [10, 11, 12, 13, 14])):
                royal_Flush = True

            # Lets do an elif tree to denote the strongest 'hand' they had which would be what you would call out
            # at the end of the poker hand; elif makes it to where the first read line that is true will be the
            # only one ran through; so putting the conditionals in descending order gives us the highest strength hand
            if (royal_Flush == True):
                player.handstrength += 1000000
            if (straight_Flush == True):
                player.handstrength += 9000
            if (FOK == True):
                player.handstrength += 800
                player.handstrength += (pair_Number * 4)
            if (full_House == True):
                player.handstrength += 7000
            if (flush == True):
                player.handstrength += 6000
                player.handstrength += (max(flushCards) * 5)
            if (straight == True):
                player.handstrength += 5000
                player.handstrength += (max(straight_Set))
            if (TOK == True):
                player.handstrength += 400
                player.handstrength += (pair_Number * 3)
            if (two_Pair == True):
                player.handstrength += 300
                player.handstrength += (pair_Number * 2)
            if (pair == True):
                player.handstrength += 200
                player.handstrength += pair_Number

        print(P1.handstrength)
        print(P2.handstrength)
        print(P3.handstrength)

        # now lets simply compare their handstrengths to see who the winners are; give them the pot
        # and set the pot back equal to zero
        if ((P1.handstrength > P2.handstrength) and (P1.handstrength > P3.handstrength)):
            P1.purse += T1.pot
            T1.pot = 0
            print("Player 1 is the winner")
            P1.win = True
        elif ((P2.handstrength > P1.handstrength) and (P2.handstrength > P3.handstrength)):
            P2.purse += T1.pot
            T1.pot = 0
            print("Player 2 is the winner")
            P2.win = True
        elif ((P3.handstrength > P2.handstrength) and (P3.handstrength > P2.handstrength)):
            print("Player 3 is the winner")
            P3.purse += T1.pot
            T1.pot = 0
            P3.win = True

        print(P3.handstrength)
        print(P1.handstrength)



    def play_Game():

        # shuffling the tables deck; this will allow this function ONLY to be looped for continuous rounds?*******
        T1.shuffle()

        # deal pocket cards to the players then deal the table its 5 cards for the game; these will be stored and
        # 'revealed' as the game progresses
        i=0
        for player in Players:
            player.hand.append(T1.deck[i])
            player.hand.append(T1.deck[i+1])
            i += 2
        for i in range (6,11):
            T1.hand.append(T1.deck[i])

        # CALL FIRST BETTING ROUND AFTER POCKET CARDS HAVE BEEN PLAYED; NO TABLE CARDS HAVE BEEN REVEALED
        # NEED TO FIGUREOUT IF PUT UPDATE SCREEN WITHIN ROUND OF BETTING TO HAVE SOME INFINITE LOOP THAT ALLOWS FOR
        # CONSTANT TEXT UPDATING AS PEOPLE ARE CLICKING BUTTONS?
        updateScreen(round_Counter)
        roundOfBetting()
        round_Counter += 1
        P1.round_Bet = 0
        P2.round_Bet = 0
        P3.round_Bet = 0


        # ok now lets do the flop then allow them to bet
        updateScreen(round_Counter)
        roundOfBetting()
        round_Counter += 1

        #ok now lets flip the fourth card over then allow a betting round
        updateScreen(round_Counter)
        roundOfBetting()
        round_Counter += 1

        # ok now lets flip the final card over and allow the final round of betting
        updateScreen(round_Counter)
        roundOfBetting()
        round_Counter += 1
        compareHands()

        # update the screen for the last time to show the players who won and with what hand
        updateScreen(round_Counter)
        for player in Players:
            if player.win == True:
                # DO SOME DISPLAY STUFF ?? PRINT ACROSS ALL BOARDS THAT PLAYER BLANK IS THE WINNER
                # PASS FOR NOW
                P1.round_Bet = 0
                P2.round_Bet = 0
                P3.round_Bet = 0

































INCREMENT = 10

small_Blind = 10
big_Blind = 20
Game1 = Game()
Game1.startup()

# beginning idea of how to loop through the game for several hands
while (P1.purse != 0) and (P2.purse != 0) (P3.purse != 0):
    Game1.play_Game()
    round_Counter = 0





