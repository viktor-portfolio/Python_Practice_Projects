import random
import hangman_words
from hangman_art import logo,stages

print(logo)

chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
lives = 6
game_over = False
correct_letters = []

word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)


while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guess this {guess} letter")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    print(f"You guessed {guess}, that's not in the word. You lose a life.")

    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************")
            print(f"The correct word was {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
