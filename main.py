import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# Todo 1. Create a dictionary in format
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
# Todo 2. Create a list of the phonetic code words from a word that a user inputs


def generate_phonetic():
    word = input("Enter a word").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, keyword not found")
        generate_phonetic()
    else:
        print(output_list)