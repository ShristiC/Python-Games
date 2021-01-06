"""
Player class for the War Card Game

- holds a player's current list of cards
- player should be able to add / remove cards to their "hand"
- player can add single or multiple cards to their "hand"
- need to translate a deck of cards with top / bottom to Python list

"""

# pop(0) from the list --> taking the top card
# append(object) to the list --> adds a card to the bottom of the deck
# listA.extend(listB) -> appends listB to the end of listA

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        try:
            card = self.all_cards.pop(0)
        except:
            return None
        else:
            return card

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # list of cards
            self.all_cards.extend(new_cards)
        else:
            # single card
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


