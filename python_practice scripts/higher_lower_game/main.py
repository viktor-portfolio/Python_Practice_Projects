import random
from art import logo, vs
from game_data import data

def formatting(account):
    acc_name = account["name"]
    acc_desc = account["description"]
    acc_country = account["country"]

    return f": {acc_name}, a {acc_desc} from {acc_country}"


def get_winner(follower_a, follower_b):
    if follower_a >= follower_b:
        return 'a'
    else:
        return 'b'



print(logo)

def higher_lower_game():
    user_score = 0
    game_over = False
    choice_b = random.choice(data)

    while not game_over:

        choice_a = choice_b
        choice_b = random.choice(data)

        if choice_a == choice_b:
            choice_b = random.choice(data)

        follower_count_a = choice_a["follower_count"]
        follower_count_b = choice_b["follower_count"]

        print(f"Compare A: {formatting(choice_a)}")
        print(f"\n{vs}\n")
        print(f"Compare B: {formatting(choice_b)}")

        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

        print("\n" * 20)
        print(logo)

        winner = get_winner(follower_count_a, follower_count_b)

        if user_choice == winner:
            user_score += 1
            print(f"You are right! Current score: {user_score}.")
        else:
            print(f"Sorry, that is wrong. Final score: {user_score}")
            game_over = True



higher_lower_game()