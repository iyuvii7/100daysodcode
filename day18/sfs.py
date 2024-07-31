import numpy as np

def monty_hall(switch):
    # All doors have a goat initially
    doors = np.array([0, 0, 0])

    # Randomly decide which door will have a car
    winner_index = np.random.randint(0, 3)

    # Place the car in the winner door
    doors[winner_index] = 1

    # Participant selects a door at random
    choice = np.random.randint(0, 3)

    # Get doors that can be opened (host cannot open the door chosen or the one with the car)
    openable_doors = [i for i in range(3) if i not in (winner_index, choice)]

    # Host opens one of the available doors at random
    door_to_open = np.random.choice(openable_doors)

    # Switch to the other available door (the one that is not the original choice or the opened one)
    if switch:
        choice = [i for i in range(3) if i not in (choice, door_to_open)][0]

    # Return 1 if you open a door with a car, 0 otherwise
    return doors[choice]

print(monty_hall(True))
