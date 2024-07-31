# list comprehension
# syntax
# new_list =[new_item for item in list if test]

# new list with squared value of numbers ( list )
# numbers = [1,2,3,4,5]
# square_list = [n**2 for n in numbers]
# print(square_list)

# dict comrehension
# syntax
# new_dict = {key_exp: value_exp for item in iterable if condition}

# creating a dict where keys are numbers and value is their square
# numbers=[1,2,3,4,5,6,7,8,9,10]
# new_dict = {n: n**2 for n in numbers}
# print(new_dict)

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# for (key,value) in weather_c.items():
#     print(key)

# loop through pandas dataframe
import pandas as pd

# Create the dictionaryS
student_data = {
    "name_of_student": [
        "Alice", "Bob", "Charlie", "David", "Eva",
        "Frank", "Grace", "Hannah", "Ian", "Jane"
    ],
    "marks_of_student": [
        85, 92, 78, 88, 76,
        95, 89, 84, 91, 77
    ]
}

df = pd.DataFrame(student_data)
for (index, row) in df.iterrows():
    print(row.marks_of_student)
