# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
#
# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas as pd
data = pd.read_csv('nato_phonetic_alphabet.csv')
df = pd.DataFrame(data)
# print(df)
alphabet_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_word = input("Enter the word: ").upper()

# loop in input word and search that alphabet in alphabet_dict and make a list (simple)
phonetic_word = [alphabet_dict[item] for item in input_word]
print(phonetic_word)
