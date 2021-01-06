'''
Card Class : understands the card's suit, rank, and value
'''

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
    'Jack'  : 11,
    'Queen' : 12,
    'King'  : 13,
    'Ace'   : 14
}

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

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

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        self.faceup = True
    
    def __str__(self):
        return self.rank + " of " + self.suit

# def test_Card_class:
#     two_hearts = Card("Hearts", "Two")
#     print(two_hearts)

