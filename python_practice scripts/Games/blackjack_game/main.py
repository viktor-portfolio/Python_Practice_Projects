from art import logo
import random


def card_deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_on_random = random.choice(cards)
    return card_on_random

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_the_game():
    print(logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1
    program_close = False

    for card in range(2):
        user_cards.append(card_deal())
        computer_cards.append(card_deal())

    while not program_close:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
        print(f"Computers first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            program_close = True
        else:
            card_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")
            if card_or_pass == 'y':
                user_cards.append(card_deal())
            else:
                program_close = True

    while computer_score > 0 and computer_score < 17:
        computer_cards.append(card_deal())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score{user_score}")
    print(f"Computers final hand: {computer_cards}, final score {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_the_game()


