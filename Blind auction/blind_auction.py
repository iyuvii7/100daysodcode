import os
import platform

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
new_dict ={}

def highest_bid(bidding_record):
    highest_price = 0
    highest_bidder = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_price:
            highest_price = bid_amount
            highest_bidder = bidder
    print(f"Highest bid = {highest_price} by {highest_bidder}")
not_end_of_game = True
while not_end_of_game:
    name = input("Enter the name. ")
    bid_price = int(input("Enter the bid price. $"))
    new_dict[name] = bid_price
    any_other = input("Is there are other users who want to bid. Type 'yes' and 'no'.")
    if any_other == 'yes':
        clear_screen()
    else:
        not_end_of_game = False
        highest_bid(new_dict)
