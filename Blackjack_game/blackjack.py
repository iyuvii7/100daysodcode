
import random
# function to withdraw random card from the list
def withdraw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    """withdraw the random card from the list and how much is needed"""
    return random.choice(cards)

# this will calculate the score from the list
def calculate_score(cards):
    """This will calculate the sum of the list values"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
        # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "you went over. You lose"
    if user_score == computer_score:
        return "draw"
    elif computer_score == 0:
        return "lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with blackjack"
    elif user_score > 21:
        return "You went over. You loose"
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose"


def play_game():
    # is user want to play or not
        # user cards list
        user_cards = []
        # computer cards list
        computer_cards = []
        is_game_over = False
        # user score variable
        user_score = 0
        # computer score variable
        computer_score = 0
        for _ in range(2):
            user_cards.append(withdraw_card())
            computer_cards.append(withdraw_card())
        while not is_game_over:
            user_score = calculate_score(user_cards)
            print(f"User cards: {user_cards}, and score: {user_score}")
            computer_score = calculate_score(computer_cards)
            print(f"Computer cards: {computer_cards}, and score: {computer_score}")
            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over = True
            else:
                want_to_play = input("Type 'y' to get another card, type 'n' to pass: ")
                if want_to_play == 'y':
                    user_cards.append(withdraw_card())
                else:
                    is_game_over = True
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(withdraw_card())
            computer_score = calculate_score(computer_cards)
        print(f"   Your final hand: {user_cards}, final score: {user_score}")
        print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare_score(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    # clear()
    play_game()