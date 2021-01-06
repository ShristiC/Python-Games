"""
Plays the game of BlackJack
"""

import Objects as obj 
deck = None
player = None
dealer = None

def __initialize_variables__():
    global deck, player, dealer
    
    deck = obj.Deck()
    deck.shuffle()

    player = obj.Player(input("What is the player's name? "))
    player.add_bet(int(input(f"How much would {player.name} like to bet on the game?\nThe default is $2, max is $500: ")))

    dealer = obj.Dealer()
    dealer.add_bet(player.bet)

def __deal_initial_cards__():
    global deck, player, dealer
    for i in range(2):
        player.add_cards(deck.deal_one())
        dealer.add_cards(deck.deal_one())
    dealer.hand[-1].faceup = False

    print("Dealer's hand ---------")
    dealer.print_hand()
    if(dealer.hand[0].rank == 'Ace'):
        print(f"current total: {dealer.hand[0].value[1]}")
    else:
        print(f"current total: {dealer.hand[0].value}")


    print("Player's hand ----------")
    player.print_hand()

def __player_game__():
    global deck, player, dealer
    bust = False
    game_on = True
    while not bust and game_on:
        total = player.calculate_total()
        if total == 21:
            print(f"Game over! {player.name} wins! Dealer pays {player.bet * 1.5} to {player.name}")
            game_on = False
            break
        elif total < 21:
            response = input("Would you like to Hit? Y or N ")
            if response == "Y":
                # Hit
                player.add_cards(deck.deal_one())
                player.print_hand()
                continue
            else:
                # Stay
                print(f"{player.name} decided to stay so now it is the dealer's play\n")
                game_on = False
                break
        else:
            print("BUSTED! player lost and the dealer has won!")
            bust = True
            break

    return bust

def __dealer_game__():
    global deck, dealer, player

    print("Now the dealer will keep hitting cards until its total is greater than player or is busted!")

    dealer.hand[-1].faceup = True
    game_on = True

    while game_on:
        dealer.print_hand()
        total = dealer.calculate_total()
        if total > player.total and total < 21 or total == 21:
            print(f"Dealer won! {player.name} loses all money")
            game_on = False
        elif total > 21:
            print(f"DEALER IS BUSTED! {player.name} wins {dealer.bet}. GAME OVER!")
            game_on = False
        else:
            # continue to hit
            dealer.add_cards(deck.deal_one())
            continue



if __name__ == "__main__":
    print("----------------------------------------------------------------------------------")
    print("This is a game of Blackjack where the computer is the dealer, and the user is the player.\n" +
    "The game is setup such that currently only 1 player plays. In this simplified game \n" +
    "the only actions available are Hit and Stay. An ace is treated as 1 or 11 by the player \n"+
    "and as 11 by the Dealer.\n\nWith the formalities out of the way, let's play!!")
    print("----------------------------------------------------------------------------------")

    __initialize_variables__()
    __deal_initial_cards__()
    bust = __player_game__()
    if not bust:
        __dealer_game__()