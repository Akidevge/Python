import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
df = pandas.read_csv(r"day 26\NATO-alphabet-start\nato_phonetic_alphabet.csv")
Nato = {row.letter: row.code for (index, row) in df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Say a word:")
# for letter in word:
#     print(letter)
wordList = [letter for letter in word]
print(f"wordlist:{wordList}")
phonetic = [key for word in wordList for (
    index, key) in Nato.items()if index == word.upper()]
# old method
# phonetic = []
# for word in wordList:
#     for (index, key) in Nato.items():
#         if index == word.upper():
#             phonetic.append(key)

print(phonetic)
