from random import randint


def check_winners(player_points, dealer_points):
    if player_points > 21:
        print('You lost!')
        return True
    elif dealer_points > 21:
        print('You won!')
        return True
    elif player_points == dealer_points:
        print('It is a draw!')
        return True
    elif player_points == 21:
        print('You won!')
        return True
    elif player_points > dealer_points:
        print('You won!')
        return True
    elif player_points < dealer_points:
        print('You lost!')
        return True


def draw_card(deck_points):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    drawn_card = cards[randint(0, 12)]
    if drawn_card == 11:
        if deck_points + drawn_card > 21:
            drawn_card = 1
    return drawn_card


def Blakjack():
    while True:
        start = input("Do you want to start a game of Blakjack? y/n ")
        if start == 'y':
            rand_player_cards = []
            player_points = 0
            rand_player_cards.append(draw_card(player_points))
            rand_player_cards.append(draw_card(player_points))
            player_points = sum(rand_player_cards)
            print(f'You draw {player_points} points')
            rand_dealer_cards = []
            dealer_points = 0
            rand_dealer_cards.append(draw_card(dealer_points))
            rand_dealer_cards.append(draw_card(dealer_points))
            dealer_points = sum(rand_dealer_cards)
            while dealer_points < 17:
                rand_dealer_cards.append(draw_card(dealer_points))
                dealer_points = sum(rand_dealer_cards)
            print(f'Dealer drew {rand_player_cards[0]} and a mysterious card')

            while player_points < 21:
                continue_game = input(
                    'Do you want to draw an extra card? y/n ')
                if continue_game == 'y':
                    drawn_card = draw_card(player_points)
                    rand_player_cards.append(drawn_card)
                    print(f'You drawn {drawn_card}')
                    player_points = sum(rand_player_cards)
                    print(f'You draw {player_points} points')
                else:
                    break
            for card in rand_dealer_cards:
                print(f'Dealer drew {card}')
            print(f'Dealer has {dealer_points} ponts')
            print(f'You have {player_points} points')
            check_winners(player_points, dealer_points)
        else:
            print('See you soon!')
            break


Blakjack()
