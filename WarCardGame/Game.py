"""
This will be the Main War Game Logic

How to Play:
1. There are two players and a deck
2. Shuffle the deck and split it evenly among the two players
3. Draw a card from each of the player decks and start comparing the ranks
4. Player with higher rank card wins all of the cards
5. If there is a tie, keep drawing until there is a round won by the player
6. Game is over when one player has all the cards

"""

import Deck as d
import Card as c
import Player as p

deck = None
p1 = None
p2 = None

def variable_initialization():
     # global variable initialization
    global deck, p1, p2
    p1 = p.Player("Bob")
    p2 = p.Player("Alice")
    deck = d.Deck()
    deck.shuffle()

def deal_cards():
    global deck, p1, p2
    # split the cards
    for i in range(26):
        p1.add_cards(deck.deal_one())
        p2.add_cards(deck.deal_one())

    # print(len(p1.all_cards))
    # print(len(p2.all_cards))

def play_game():
    # start playing the game
    # this code did not work because checking for null errors instead of checking length -- gives a safer comparison check
    global deck, p1, p2

    cards = []
    while True:
        c1 = p1.remove_one()
        c2 = p2.remove_one()

        if c1 == None and c2 == None:
            print("Game Over! There is no winner, its a tie")
            break
        elif c1 == None:
            print(f"Game Over! The winner is {p2.name}")
            break
        elif c2 == None:
            print(f"Game Over! The winner is {p1.name}")
            break

        cards.append(c1)
        cards.append(c2)
        for card in cards: print(card)
        if c1.value == c2.value:
            print("neither won the round")
            continue
        elif c1.value > c2.value:
            p1.add_cards(cards)
            print("player 1 won the round")
        else:
            p2.add_cards(cards)
            print("player 2 won the round")

        cards = []

def play_game_udemy():
    global p1, p2

    game_on = True

    round_num = 0

    while game_on:
        round_num += 1
        print(f"Round: {round_num}")

        if len(p1.all_cards) == 0:
            print('Player one, out of cards! Player 2 wins!')
            game_on = False
            break
        if len(p2.all_cards) == 0:
            print('Player two, out of cards! Player 1 wins!')
            game_on = False
            break

        # Start a New Round
        p1_cards = []
        p1_cards.append(p1.remove_one())
        p2_cards = []
        p2_cards.append(p2.remove_one())

        # player must draw 5 cards during war

        at_war = True

        while at_war:
            c1 = p1_cards[-1]
            c2 = p2_cards[-1]
            if c1.value < c2.value:
                p1.add_cards(p2_cards)
                p1.add_cards(p1_cards)
                at_war = False
            elif c1.value > c2.value:
                p2.add_cards(p1_cards)
                p2.add_cards(p2_cards)
                at_war = False
            else:
                # check if players have enough cards
                len_one = len(p1.all_cards)
                len_two = len(p2.all_cards)

                if  len_one >= 5 and len_two >= 5:
                    for i in range(5):
                        p1_cards.append(p1.remove_one())
                        p2_cards.append(p2.remove_one())
                elif len_one < 5:
                    at_war = False
                    game_on = False
                    print("Player 1 does not have enough cards! Player 2 wins!")
                else:
                    at_war = False
                    game_on = False
                    print("Player 2 does not have enough cards! Player 1 wins!")



if __name__ == "__main__":
    ''' Starts the game and has the initial setup ''' 

    variable_initialization()   

    deal_cards()

    # play_game()
    play_game_udemy()
    






