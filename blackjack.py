# import art

import random

#####################################################_Global Variables_#################################################

# cards to play with.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

########################################################_Functions_#####################################################


##function to deal a card
def deal_card(number_of_cards):
    return random.sample(cards, number_of_cards)


##function to ask user to play & test input is valid, and ask again if not
def get_yes_no():
    while True:
        response = input("Would you like to play a game of Blackjack? 'yes' or 'no': ").strip().lower()
        if response in ["yes", "no"]:
            return response
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


# Function to calculate the current total score
def calculate_score(hand):
    score = sum(hand)
    if score == 21 and len(hand) == 2:  # Blackjack condition
        return 0
    if 11 in hand and score > 21:
        hand[hand.index(11)] = 1  # Adjust ace from 11 to 1 if score is over 21
        score = sum(hand)
    return score


##function to ask for hit or pass
def hit_or_pass():
    while True:
        choice = input("Type 'y' to hit, type 'n' to pass: ").strip().lower()
        if choice in ["y", "n"]:
            return choice
        else:
            print("Invalid input. Please try again.")


# Function to determine the game outcome
def victory_loss(player_score, npc_score):
    if player_score == 0:
        return "Blackjack! You win!"
    elif npc_score == 0:
        return "Computer got Blackjack. You lose!"
    elif player_score > 21:
        return "You went over 21. You lose!"
    elif npc_score > 21:
        return "Computer went over 21. You win!"
    elif player_score > npc_score:
        return "You win!"
    elif npc_score > player_score:
        return "You lose!"
    else:
        return "It's a draw!"


####################################################_Code Start_########################################################


# call function and set initial variable
play_a_game = get_yes_no()

# Start game if user asks
while play_a_game == "yes":
    ### TODO print logo
    

    # print(art.logo)

    ##begin game
    player_hand = deal_card(2)
    npc_hand = deal_card(2)
    player_score = calculate_score(player_hand)
    npc_score = calculate_score(npc_hand)

    ##Report initial hands and player score
    print(f"Your first hand: {player_hand}, Your score: {player_score}")
    print(f"Computer's first card: {npc_hand[0]}")

    ##Player's turn
    while player_score != 0 and player_score < 21:
        hit = hit_or_pass()
        if hit == "y":
            player_hand.extend(deal_card(1))
            player_score = calculate_score(player_hand)
            npc_score = calculate_score(npc_hand)
            print(f"Your hand: {player_hand}, Your score: {player_score}")
            print(f"Computer's first card: {npc_hand[0]}")
            if player_score > 21:
                print("You went over, You lose!")
                break
        else:
            break

    # NPC's Turn
    if player_score <= 21:
        while npc_score < 17:
            npc_hand.extend(deal_card(1))
            npc_score = calculate_score(npc_hand)

        print(f"Computer's Final Hand: {npc_hand}, Computer's final score: {npc_score}")
        print(victory_loss(player_score, npc_score))

    # Ask player to play again
    play_a_game = get_yes_no()

