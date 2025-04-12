import pandas as pd

from List_Comprehension import numbers

dataset=pd.read_csv("nato_phonetic_alphabet.csv")

names=str(input("Please enter your name sir ?"))

names.upper()

nato_dict = {row.letter: row.code for (index, row) in dataset.iterrows()}

nato_list = [nato_dict[letter] for letter in names]

print(nato_list)

