import pandas as pd



dataset=pd.read_csv("nato_phonetic_alphabet.csv")




nato_dict = {row.letter: row.code for (index, row) in dataset.iterrows()}


def generate_phonetic():
    names = str(input("Please enter your name sir ?"))
    names.upper()
    try:
        nato_list = [nato_dict[letter] for letter in names]
    except KeyError:
        print("Only letters are allowed sir ")
    else:
        print(nato_list)

generate_phonetic()

