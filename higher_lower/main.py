import random
from game_data import data


# pick random name from the list of data
def generate_name():
    return random.choice(data)


# compare 2 chosen name followers and return the name which have more following

def more_followers(name_a, name_b):
    if name_a['follower_count'] > name_b['follower_count']:
        return 'a'
    else:
        return 'b'


# increase score if user right
def increase_score():
    global score
    score += 1
    return score


score = 0


def game():
    global score
    # pick a random name from list of dictionaries
    compare_a = generate_name()
    # print(compare_a)
    end_of_game = False
    while not end_of_game:
        against_b = generate_name()
        # print(against_b)
        if compare_a == against_b:
            against_b = generate_name()
        print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")
        # print the second name for the game
        print("Vs")
        print(f"Against B: {against_b['name']}, a {against_b['description']}, from {against_b['country']}.")
        # print(f"A followers {compare_a['follower_count']}")
        # print(f"B followers {against_b['follower_count']}")
        # to know the user input for who has more followers
        user_choice = input("Who has more followers? Type 'A' or 'B'.\n").lower()
        if more_followers(compare_a, against_b) == user_choice:
            print("You're right.")
            # to become an as user choice for next comparison if user were right
            if user_choice == 'b':
                compare_a = against_b
            score = increase_score()
            print(f"Your current score is {score}.")
        else:
            print("You're wrong.")
            print(f"Your final score is {score}.")
            end_of_game = True


game()
