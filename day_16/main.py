# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
# my_screen = Screen()
# my_screen.exitonclick()
from prettytable import PrettyTable
# import datetime

# date = datetime.date(2024,6,6)
# print(date)

# today = datetime.date.today()
# print(today.year)
# print(today.month)
# print(today.day)

# create time object
# time = datetime.time(20,20,20)
# print(time)
# dt = datetime.datetime(2050,9,15,9,50,50)
# print(dt)
#
# now = datetime.datetime.now()
# formate_date = now.strftime("%Y_%m_%d %H:%M:%S")
# print(formate_date)

# lambda function
# b = lambda a: 'positive' if a > 0 else 'negative'
# print(b(-7))

# 1. Write a  Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.
# Sample Output:
# a = lambda x: x + 15
# b = lambda x,y: x*y
# print(a(2))
# print(b(5,5))

# 2. Write a  Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75


# def func_comp(n):
#     return lambda x: x*n
#
# result = func_comp(15)
# print(f"The double of 15 = {result(2)}")
# print(f"The triple of 15 = {result(3)}")


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# doubled_numbers = map(lambda x: x%2==0, numbers)
# print(list(doubled_numbers))  # Output: [2, 4, 6, 8]

# Given a list of temperatures in Celsius, use the map() function to convert them to Fahrenheit. The formula to convert Celsius to Fahrenheit is:
# List of temperatures in Celsius
# celsius_temps = [0, 20, 37, 100]
# fahrenheit_temps = map(lambda x: x * 9 / 5 + 32, celsius_temps)
# print(list(fahrenheit_temps))

# Given a list of numbers, use the map() function to square each number.
# numbers = [1, 2, 3, 4, 5]
# square_numbers = map(lambda x: x**2, numbers)
# print(list(square_numbers))

# Given a list of strings, use the map() function to get the length of each string
# words = ["apple", "banana", "cherry"]
# length = map(lambda x: len(x), words)
# print(list(length))

from prettytable.colortable import ColorTable, Themes
table = ColorTable()
table. add_column('Pokemon name', ['Pikachu', 'Squirtel', 'charmander'])
table. add_column('Type', ['Electric', 'Water', 'Fire'])
table.align = 'c'
table.set_style = 'double_border'
print(table)