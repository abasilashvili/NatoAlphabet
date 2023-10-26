import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
user_input = input("Type your name: ").upper()

nato_output = {i: nato_dict[i] for i in user_input}

print(nato_output)


