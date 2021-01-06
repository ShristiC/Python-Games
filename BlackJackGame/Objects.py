"""
Objects File which has the initial OOP code for Card, Deck, and Player

Card Class: designates the card's rank, suit, and value
Deck Class: designated a deck of cards
Player Class: defines how the Player operates 
"""

import random 

# Program Constants

# dictionary of card value pairs
values = {
    'Two'   : 2, 
    'Three' : 3,
    'Four'  : 4,
    'Five'  : 5,
    'Six'   : 6,
    'Seven' : 7,
    'Eight' : 8,
    'Nine'  : 9,
    'Ten'   : 10,
    'Jack'  : 10,
    'Queen' : 10,
    'King'  : 10,
    'Ace'   : [1,11]
}

# Has the card suit
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

# Orders the ranks of the cards
ranks = (
    'Two'  ,
    'Three',
    'Four' ,
    'Five' ,
    'Six'  ,
    'Seven',
    'Eight',
    'Nine' ,
    'Ten'  ,
    'Jack' ,
    'Queen',
    'King' ,
    'Ace'
)

# Defines the Cards in a Deck of Cards
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        self.faceup = True
 
    def __str__(self):
        return self.rank + " of " + self.suit

# Defines the Deck of Cards
class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        ''' intenral shuffling of the deck '''
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()

# Defines the Player Class
class Player:
    def __init__(self, name):
        self.name = name
        # default bet value of 2
        self.bet = 2
        self.hand = []
        self.total = 0

    def add_bet(self, bet):
        self.bet = bet

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # list of cards
            self.hand.extend(new_cards)
        else:
            # single card
            self.hand.append(new_cards)
    
    def calculate_total(self):
        # calculates the total of the current hand that the player has
        total_value = 0
        for card in self.hand:
            if(card.rank == 'Ace'):
                while True:
                    temp = int(input("Should this Ace be treated as a 1 or 11? "))
                    if temp != 1 or temp != 11:
                        print("Not a valid number, please try again")
                        continue
                    else:
                        total_value += temp
                        break

            else:
                total_value += card.value
        print(f"current total: {total_value}")
        self.total = total_value
        return total_value                    

    def print_hand(self):
        # prints the current hand that the player has
        for card in self.hand:
            print(card.rank, end=" ")
        print()
    
    def __str__(self):
        return f'Player {self.name} has {len(self.hand)} cards'

# Defines the Dealer Class
class Dealer:
    def __init__(self):
        self.player_bet = 2
        self.hand = []

    def add_bet(self, bet):
        self.bet = bet

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # list of cards
            self.hand.extend(new_cards)
        else:
            # single card
            self.hand.append(new_cards)
    
    def calculate_total(self):
        # calculates the current total of the hand the dealer has
        total_value = 0
        for card in self.hand:
            if(card.rank == 'Ace'):
                total_value += card.value[1]

            else:
                total_value += card.value
        print(f"current total: {total_value}")
        return total_value                    

    def print_hand(self):
        # prints the current hand of the dealer 
        for card in self.hand:
            if card.faceup:
                print(card.rank, end=" ")
            else:
                print("FACEDOWN", end=" ")
        print()
    
    def __str__(self):
        return f'Dealer has {len(self.hand)} cards'

