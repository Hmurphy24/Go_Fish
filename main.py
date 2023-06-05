import random

go_fish_match_dictionary = {'User Books': 0, 'Computer Books': 0}

go_fish_score_dictionary = {'Wins': 0, 'Losses': 0, 'Ties': 0, 'Games Played': 0}


def go_fish_rules():

    print()

    print('Welcome to Go Fish!')

    print()

    print('The deck will be shuffled a number of times specified by you and will be distributed between you and the computer.')
    print('Once you have four of the same card, you have a book!')
    print('When it\'s your turn, ask the computer if they have a card you want. If they don\'t then you draw from the deck.')
    print('The same applies when it is the computer\'s turn as well.')
    print('When asking for a card, type in either "Ace", "Jack", "Queen", "King", "2", "3", etc.')

    print()

    print('The end goal is to try to have more books than the computer!')
    print('Good luck!')
    print()


def go_fish_card_sorter():

    go_fish_entire_card_deck = []

    go_fish_cards_list_one = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    go_fish_cards_list_two = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    go_fish_cards_list_three = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    go_fish_cards_list_four = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    for card in go_fish_cards_list_one:

        go_fish_entire_card_deck.append(card)

    for card in go_fish_cards_list_two:

        go_fish_entire_card_deck.append(card)

    for card in go_fish_cards_list_three:

        go_fish_entire_card_deck.append(card)

    for card in go_fish_cards_list_four:

        go_fish_entire_card_deck.append(card)

    go_fish_times_shuffled = int(input('How many times do you want the deck to be shuffled? '))

    print('The deck will be shuffled {} time(s)!'.format(go_fish_times_shuffled))

    print()

    while go_fish_times_shuffled > 0:

        random.shuffle(go_fish_entire_card_deck)

        go_fish_times_shuffled -= 1

    go_fish_valid_requests = []

    for card in go_fish_cards_list_one:

        go_fish_valid_requests.append(card)

    for card in go_fish_cards_list_two:

        go_fish_valid_requests.append(card)

    for card in go_fish_cards_list_three:

        go_fish_valid_requests.append(card)

    for card in go_fish_cards_list_four:

        go_fish_valid_requests.append(card)

    return go_fish_entire_card_deck, go_fish_valid_requests


def go_fish_card_dealer(total_deck):

    go_fish_card_sort_counter = 0

    go_fish_remaining_deck = []

    go_fish_computer_deck = []

    go_fish_user_deck = []

    while go_fish_card_sort_counter < 7:

        go_fish_computer_deck.append(total_deck[0])

        total_deck.remove(total_deck[0])

        go_fish_user_deck.append(total_deck[0])

        total_deck.remove(total_deck[0])

        go_fish_card_sort_counter += 1

    for card in total_deck:

        go_fish_remaining_deck.append(card)

    return go_fish_remaining_deck, go_fish_computer_deck, go_fish_user_deck


def go_fish_gameplay(card_pile, computer_hand, user_hand, valid_requests):

    go_fish_computer_matches = []

    go_fish_user_matches = []

# Checking For Computer Matches

    for card in computer_hand:

        go_fish_matches_counter = computer_hand.count(card)

        if go_fish_matches_counter > 3:

            go_fish_computer_matches.append(card)

            go_fish_match_dictionary['Computer Books'] += 0.25

    for card in go_fish_computer_matches:

        if card in computer_hand:

            computer_hand.remove(card)

    for card in go_fish_computer_matches:

        if card in valid_requests:

            valid_requests.remove(card)

# Checking For User Matches

    for card in user_hand:

        go_fish_matches_counter = user_hand.count(card)

        if go_fish_matches_counter > 3:

            go_fish_user_matches.append(card)

            go_fish_match_dictionary['User Books'] += 0.25

    for card in go_fish_user_matches:

        if card in user_hand:

            user_hand.remove(card)

    for card in go_fish_user_matches:

        if card in valid_requests:

            valid_requests.remove(card)

# Main Game Loop

    print('Starting Hands:')

    print('User Hand:')

    print(user_hand)

    print()

    print('Books:')

    print('User Books:')

    print(go_fish_user_matches)

    print()

    print('Computer Books:')

    print(go_fish_computer_matches)

    print()

    while True:

        if (len(user_hand) == 0) and (len(computer_hand) == 0) and (len(card_pile) == 0):

            print('All of the cards have been booked!')

            break

# Getting The User's Card Request

        while True:

            if len(user_hand) == 0:

                print('You have no cards, so you draw!')

                print()

                user_hand.append(card_pile[0])

                card_pile.remove(card_pile[0])

                break

            else:

                go_fish_user_request = input('Which card(s) do you want to ask the computer for? ')

                print()

                if (go_fish_user_request.capitalize() in valid_requests) and (go_fish_user_request.capitalize() in computer_hand):

                    print('The computer had that card! It was added to your hand!')

                    print()

                    for card in computer_hand:

                        if card == go_fish_user_request.capitalize():

                            user_hand.append(card)

                    computer_hand = [i for i in computer_hand if i != go_fish_user_request.capitalize()]

                    if len(user_hand) == 0:

                        print('You are out of cards, so you draw a card!')

                        user_hand.append(card_pile[0])

                        card_pile.remove(card_pile[0])

                    break

                elif (go_fish_user_request.capitalize() in valid_requests) and (go_fish_user_request.capitalize() not in computer_hand):

                    print('Go Fish!')

                    print('You drew a card!')

                    print()

                    user_hand.append(card_pile[0])

                    card_pile.remove(card_pile[0])

                    break

                elif (go_fish_user_request.capitalize() in go_fish_user_matches) or (go_fish_user_request.capitalize() in go_fish_computer_matches):

                    print('This card already has it\'s book made!')

                else:

                    print('Please enter a valid card!')

                    print()

# Checking For User Matches

        for card in user_hand:

            go_fish_matches_counter = user_hand.count(card)

            if go_fish_matches_counter > 3:

                go_fish_user_matches.append(card)

                go_fish_match_dictionary['User Books'] += 0.25

        for card in go_fish_user_matches:

            if card in user_hand:

                user_hand.remove(card)

        for card in go_fish_user_matches:

            if card in valid_requests:

                valid_requests.remove(card)

        # Computer Turn

        print('Updated Hands:')

        print('User Hand:')

        print(user_hand)

        print()

        print('Books:')

        print('User Books:')

        print(go_fish_user_matches)

        print()

        print('Computer Books:')

        print(go_fish_computer_matches)

        print()

        if (len(user_hand) == 0) and (len(computer_hand) == 0) and (len(card_pile) == 0):

            print('All of the cards have been booked!')

            break

        if len(computer_hand) == 0:

            print('The computer has no cards in it\'s hand, so it draws a card!')

            print()

            computer_hand.append(card_pile[0])

            card_pile.remove(card_pile[0])

        else:

            go_fish_computer_turn = random.choice(computer_hand)

            print('The computer asked for a ' + go_fish_computer_turn + '!')

            print()

            if go_fish_computer_turn in user_hand:

                print('The computer took your card(s)!')

                print()

                for card in user_hand:

                    if card == go_fish_computer_turn:

                        computer_hand.append(card)

                user_hand = [i for i in user_hand if i != go_fish_computer_turn]

                if len(computer_hand) == 0:

                    print('The computer is out of cards, so it draws a card!')

                    computer_hand.append(card_pile[0])

                    card_pile.remove(card_pile[0])

            elif go_fish_computer_turn not in user_hand:

                print('The computer had to Go Fish!')

                print()

                computer_hand.append(card_pile[0])

                card_pile.remove(card_pile[0])

# Checking For Computer Matches

        for card in computer_hand:

            go_fish_matches_counter = computer_hand.count(card)

            if go_fish_matches_counter > 3:

                go_fish_computer_matches.append(card)

                go_fish_match_dictionary['Computer Books'] += 0.25

        for card in go_fish_computer_matches:

            if card in computer_hand:

                computer_hand.remove(card)

        for card in go_fish_computer_matches:

            if card in valid_requests:

                valid_requests.remove(card)

        print('Updated Hands:')

        print('User Hand:')

        print(user_hand)

        print()

        print('Books:')

        print('User Books:')

        print(go_fish_user_matches)

        print()

        print('Computer Books:')

        print(go_fish_computer_matches)

        print()

    print()

    print('Here\'s the end of game statistics:')

    print()

    print('Books:')

    print('User Books:')

    print(go_fish_user_matches)

    print()

    print('Computer Books:')

    print(go_fish_computer_matches)

    print()

    print(go_fish_match_dictionary)

    print()

    if len(go_fish_user_matches) > len(go_fish_computer_matches):

        print('You had more books! So you won the game!')

        print()

        go_fish_score_dictionary['Wins'] += 1

    elif len(go_fish_user_matches) < len(go_fish_computer_matches):

        print('You had less books than the computer, so you lost!')

        print()

        go_fish_score_dictionary['Losses'] += 1

    else:

        print('You had the same number of books as the computer, so it\'s a tie!')

        print()

        go_fish_score_dictionary['Ties'] += 1


def go_fish_replay():

    print('Here\'s the score:')

    print(go_fish_score_dictionary)

    while True:

        print()

        go_fish_replay_request = input('Would you like to play again/ ("Yes"/"No"): ')

        if go_fish_replay_request.upper() == 'YES':

            print('Okay! Let\'s go!')

            break

        elif go_fish_replay_request.upper() == 'NO':

            print('Okay, bye!')

            exit()

        else:

            print('Please type either "Yes" or "No"!')


go_fish_rules()

while True:

    go_fish_total_deck = go_fish_card_sorter()

    go_fish_gameplay_decks = go_fish_card_dealer(go_fish_total_deck[0])

    go_fish_gameplay(go_fish_gameplay_decks[0], go_fish_gameplay_decks[1], go_fish_gameplay_decks[2], go_fish_total_deck[1])

    go_fish_score_dictionary['Games Played'] += 1

    go_fish_replay()
