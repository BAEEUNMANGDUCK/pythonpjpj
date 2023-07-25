
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

import pandas as pd


df = pd.read_csv('nato_phonetic_alphabet.csv')

alphas = {row.letter : row.code for (index, row) in df.iterrows()}

print(alphas)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

input_word = input("Enter a word: ").upper()

nato_alphabet = [ alphas[alpha] for alpha in input_word ]

print(nato_alphabet)