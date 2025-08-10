import pandas as pd

data = pd.read_csv("nato.csv")

# Exercise 1: Create a dictionary in this format: {"A": "Alfa", ...}
nato_alphabet = {row.letter.upper(): row.callsign.capitalize() for (index, row) in data.iterrows()}

# Exercise 2: Create a list of the phonetic code words
user_input = input("Enter the message: ").upper()
phonetic_code_words = [nato_alphabet[letter] for letter in user_input if letter in nato_alphabet.keys()]

print(phonetic_code_words)

