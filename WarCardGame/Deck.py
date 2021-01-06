'''
Instantiates a new deck - list of card objects
Shuffle a Deck through a method call
Deal cards from the Deck object
'''

import random
import Card as cd

class Deck:
    def __init__(self):
        ''' initializes the list through a deck of cards '''
        self.all_cards = []
        for suit in cd.suits:
            for rank in cd.ranks:
                # Create Card object
                created_card = cd.Card(suit, rank)
                self.all_cards.append(created_card)

    def print_deck(self):
        ''' prints the deck of cards '''
        for card in self.all_cards:
            print(card)

    def shuffle(self):
        ''' internal shuffling of the deck, does not return anything '''
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

# new_deck = Deck()
# # new_deck.print_deck()
# new_deck.shuffle()
# print(new_deck.deal_one())