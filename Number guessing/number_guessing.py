import random

def difficulty(user_choice):
    """It will return total number of attempts user will have based on their difficulty choice"""
    if user_choice == 'easy':
        return 10
    elif user_choice == 'hard':
        return 5

def right_guess(user_number, computer_number):
    if user_number < computer_number:
        print("Too low.")
        print("Guess again.")
        return False
    elif user_number > computer_number:
        print("Too high.")
        print("Guess again.")
        return False
    elif user_number == computer_number:
        print(f"You've got it the answer was: {computer_number}")
        return True

not_end_of_game = True
while not_end_of_game:
    print("Welcome to the guessing game.")
    print("I'm thinking of a number between 1 and 100.")
    # generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    # print(random_number)
    choose_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choose_difficulty not in ['easy', 'hard']:
        print("Invalid input! Please choose either 'easy' or 'hard'.")
        continue
    number_of_attempts = difficulty(choose_difficulty)
    while number_of_attempts > 0:
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if not right_guess(user_number=guess, computer_number=random_number):
            number_of_attempts -= 1
        else:
            not_end_of_game = False
            break
    if number_of_attempts == 0:
        not_end_of_game = False
        print("You've run out of guesses. You lose.")
