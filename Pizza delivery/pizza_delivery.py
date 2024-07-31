print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0
# For size of the pizza
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
else:
    bill += 25
# For pepperoni
if add_pepperoni =="y":
    if size == "s":
        bill += 2
    else:
        bill += 3
# for extra cheese
if extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}.")

