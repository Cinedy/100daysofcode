# List comprehension = create a new list from a previous list : new list = [new_item for item in list]
# Keyword Method with iterrows() : {new_key:new_value for (index, row) in df.iterrows()}

#NATO ALPHABET PROJECT
import pandas


#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Only letters in the alphabet!")
        generate_phonetic()
    else: 
        print(output)

generate_phonetic()