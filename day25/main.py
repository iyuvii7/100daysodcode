# with open(file='weather_data.csv', mode='r') as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data['temp'])

# temp_list = data['temp'].to_list()
# to find the avg using python '.sum()' function
# sum_of_temp = sum(temp_list)
# avg_of_temp = sum_of_temp / len(temp_list)
# print(avg_of_temp)

# we can also find the avg which is mean of temp using pandas .mean() function
# print(data['temp'].mean())

# for max value
# print(data['temp'].max())

# get data in row
# print(data[data.day == 'Monday'])

# get data in row where temp is max
# print(data[data.temp == data.temp.max()])

# get the monday temp and convert it to fahrenheit
# monday = data[data.day == 'Monday']
# print(monday.temp[0])
# monday_temp_in_F = monday.temp[0] * 9/5 + 32
# print(monday_temp_in_F)

# create a dataframe from scratch
# data_dict = {
#     'Student name': ['ABC', 'DEF', 'GHI'],
#     'Student score': [90, 50, 90]
# }
# df = pandas.DataFrame(data_dict)
# print(df)

import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data.columns)

squirrel_colors = data["Primary Fur Color"].dropna().unique()
# print(squirrel_colors)
color_count =[]
for color in squirrel_colors:
    color_count.append(len(data[data["Primary Fur Color"] == color]))
# gray_count = len(data[data['Primary Fur Color'] == 'Gray'])
# cinnamon_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
# black_count = len(data[data['Primary Fur Color'] == 'Black'])

data_dict ={
    "Fur color": squirrel_colors,
    "Count": color_count
}
# now convert this dict to dataframe
df = pd.DataFrame(data_dict)
df.to_csv("Squirrel_count")

# for color in list_of_fur_color:




