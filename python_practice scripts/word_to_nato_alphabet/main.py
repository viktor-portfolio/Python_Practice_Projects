import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}
translate_on = True

while translate_on:
    user_input = input("Enter the word you want to get translated: ").upper()

    if user_input == "EXIT":
        translate_on = False
    else:
        try:
            translated_word = [nato_dict[letter] for letter in user_input]
        except KeyError:
            print("Sorry, only letters in the alphabet, please.")
        else:
            print(translated_word)

