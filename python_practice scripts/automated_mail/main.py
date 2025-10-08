with open("./Input/names.txt") as name_file:
    names = name_file.read().splitlines()

with open("./Input/starting_letter.txt") as letter_file:
    letter = letter_file.read()

for name in names:
    new_letter = letter.replace("[name]", name)
    with open(f"./Output/ReadyLetters/letter_to_{name}.txt", mode="w") as file:
        file.write(new_letter)


