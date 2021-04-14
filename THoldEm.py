# we will have the overarching classes here

class Card:
    def __init__(self, number, suit = " ", image = " "):

        self.number = number
        self.suit = suit
        self.image = image

class Player:
    def __init__(self, bet=0, purse = 1000):
        self.current_Bet = bet
        self.hand = []
        self.purse = purse


    def win(self):
        pass

    def clear_Hand(self):
        self.hand = []

    def make_Bet(self):
        pass
    def make_Small_Blind(self):
        pass
    def make_Big_Blind(self):
        pass
    def fold(self):
        pass
    def change_Bet(self):
        pass

class Table:
    def __init__(self, deck=[], pot = 0, hand = []):
        self.hand = hand
        self.deck = deck
        self.pot = pot

    def wipe_Clean(self):
        pass




