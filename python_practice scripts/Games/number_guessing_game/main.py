
from art import logo
import random

EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5
SECRET_DIFFICULTY = 1

def random_number_generator():
    return random.randint(1, 100)

def set_difficulty(user_difficulty):
    if user_difficulty == 'easy':
        return EASY_DIFFICULTY
    elif user_difficulty == 'hard':
        return HARD_DIFFICULTY
    else:
        return SECRET_DIFFICULTY

def lives_manager(guess, winning_number, lives):
    if guess != winning_number:
        if guess < winning_number:
            print("Too low")
            return lives - 1
        elif guess > winning_number:
            print("Too high")
            return lives - 1

def number_guessing_game():
    program_close = False

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    user_lives = set_difficulty(difficulty)
    the_number = random_number_generator()

    while not program_close:
        print(f"You have {user_lives} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))

        user_lives = lives_manager(user_guess, the_number, user_lives)

        if user_guess == the_number:
            print("You have guessed correctly!")
            program_close = True

        if user_lives == 0:
            print("You ran out of attempts")
            print(f"The number was {the_number}")
            program_close = True
        elif user_guess != the_number:
            print("Guess again!")


number_guessing_game()




