# student_dict = {
#     "student": ["Fahmi", "Abdul", "Aziz"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())

#TODO 1. Create a dictionary in this format:
phonetic_dictionary = {row.letter:row.code for (index, row) in data.iterrows()}
# print(phonetic_dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [phonetic_dictionary[letter] for letter in word]
print(output_list)

