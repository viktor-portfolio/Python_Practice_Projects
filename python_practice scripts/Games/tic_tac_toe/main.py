board_pieces = ["-"] * 9
winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]
is_game_on = True
player_symbol = None

#CREATE BOARD
def create_board():
    n = 0
    coordinates_y = 1
    print("    " + '1' + "   " + '2' + "   " + '3' + "  ")
    print("  -------------")
    for _ in range(3):
        print(str(coordinates_y) + " | " + board_pieces[0 + n] + " | " + board_pieces[1 + n] + " | " + board_pieces[2 + n] + " |")
        print("  -------------")
        n += 3
        coordinates_y += 1

#USER SYMBOL CHECK
def user_choice_check():
    if user_choice == '1':
        user_symbol = "X"
        return user_symbol
    elif user_choice == '2':
        user_symbol = "O"
        return user_symbol
    else:
        print("Not a valid option")

#AI SYMBOL CHECK
def ai_choice_check(user_symbol):
    if user_symbol == 'X':
        ai_choice = 'O'
        return ai_choice
    else:
        ai_choice = 'X'
        return ai_choice

#PLAYER INPUT
def player_input(board):
    while True:
        user_input = input(
            "Please input the coordinates where you want to place your symbol(separated by a comma like this(row,column) and between 1 and 3 => (1,2): ").split(
            ',')
        try:
            if len(user_input) != 2:
                print("Invalid! Please use the correct format!")
                continue

            row = int(user_input[0])
            column = int(user_input[1])

            if row < 1 or row > 3 or column < 1 or column > 3:
                print("Coordinates given must be between 1 and 3. Try again!")
                continue

            coordinates = (row - 1) * 3 + (column -1)

            if board[coordinates] != "-":
                print("That spot is taken. Try again!")

            if 0 <= coordinates <= 8 and board[coordinates] == "-":
                board[coordinates] = player_symbol
                break
        except ValueError:
            print("Invalid input! Use the correct numbers and format. Try again!")
        except IndexError:
            print("Coordinates out of range! Use the correct format!")


#AI INPUT
def ai_input(board):
    priority_fields = [4, 0, 2, 6, 8, 1, 3, 5, 7]

    for combination in winning_combinations:
        fields = [board[field] for field in combination]
        if fields.count(ai_symbol) == 2 and fields.count("-") == 1:
            place_symbol = combination[fields.index("-")]
            board[place_symbol] = ai_symbol
            return

    for combination in winning_combinations:
        fields = [board[field] for field in combination]
        if fields.count(player_symbol) == 2 and fields.count("-") == 1:
            place_symbol = combination[fields.index("-")]
            board[place_symbol] = ai_symbol
            return

    for field in priority_fields:
        if board[field] == "-":
            board[field] = ai_symbol
            return


#WIN CONDITIONS VERSION 1.0
# def win_conditions(board,user,ai):
#     def horizontal():
#         global is_game_on
#         if board[0]==board[1]==board[2] and board[1] != "-" and board[1]==user:
#             print("The Player won the game")
#             is_game_on = False
#             create_board()
#         elif board[0]==board[1]==board[2] and board[1] != "-" and board[1]==ai:
#             print("The AI won the game")
#             is_game_on = False
#             create_board()
#
#         if board[3]==board[4]==board[5] and board[4] != "-" and board[4]==user:
#             print("The Player won the game")
#             is_game_on = False
#             create_board()
#         elif board[3]==board[4]==board[5] and board[4] != "-" and board[1]==ai:
#             print("The AI won the game")
#             is_game_on = False
#             create_board()
#
#         if board[6]==board[7]==board[8] and board[7] != "-" and board[7]==user:
#             print("The Player won the game")
#             is_game_on = False
#             create_board()
#         elif board[6]==board[7]==board[8] and board[7] != "-" and board[7]==ai:
#             print("The AI won the game")
#             is_game_on = False
#             create_board()
#
#     def vertical():
#         global is_game_on
#         if board[0]==board[3]==board[6] and board[3] != "-" and board[3]==user:
#             print("The Player won the game")
#             is_game_on = False
#             create_board()
#         elif board[0]==board[3]==board[6] and board[3] != "-" and board[3]==ai:
#             print("The AI won the game")
#             is_game_on = False
#             create_board()
#
#         if board[1]==board[4]==board[7] and board[4] != "-" and board[4]==user:
#             print("The Player won the game")
#             is_game_on = False
#             create_board()
#         elif board[1]==board[4]==board[7] and board[4] != "-" and board[4]==ai:
#             print("The AI won the game")
#             is_game_on = False
#             create_board()
#
#         if board[2]==board[5]==board[8] and board[5] != "-" and board[5]==user:
#             print("The Player won the game")
#             is_game_on = False
#             create_board()
#         elif board[2]==board[5]==board[8] and board[5] != "-" and board[5]==ai:
#             print("The AI won the game")
#             is_game_on = False
#             create_board()
#
#     def diagonal():
#         global is_game_on
#         if board[0]==board[4]==board[8] and board[4] != "-" and board[4]==user:
#             print("The Player won the game")
#             is_game_on = False
#             create_board()
#         elif board[0]==board[4]==board[8] and board[4] != "-" and board[4]==ai:
#             print("The AI won the game")
#             is_game_on = False
#             create_board()
#
#         if board[2]==board[4]==board[6] and board[4] != "-" and board[4]==user:
#             print("The Player won the game")
#             is_game_on = False
#             create_board()
#         elif board[2]==board[4]==board[6] and board[4] != "-" and board[4]==ai:
#             print("The AI won the game")
#             is_game_on = False
#             create_board()
#
#     def tie():
#         global is_game_on
#         if "-" not in board:
#             print("The Game Was a Tie!")
#             is_game_on = False
#             create_board()
#
#     horizontal()
#     vertical()
#     diagonal()
#     tie()

#WINNING CONDITIONS VERSION 2.0
def win_conditions(board, user):
    global is_game_on

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "-":
            winner = board[combo[0]]
            create_board()
            if winner == user:
                print("The Player won the game!")
            else:
                print("The AI won the game!")
            is_game_on = False
            return

    if "-" not in board:
        create_board()
        print("The Game Was a Tie!")
        is_game_on = False

#USER SYMBOL CHOICE
while True:
    user_choice = input("Press 1 for X symbol and press 2 for O symbol: ")
    if user_choice in ['1', '2']:
        break
    print("Invalid choice! Try again!")

player_symbol = user_choice_check()
print(f"Your symbol is {player_symbol}")

#AI SYMBOL
ai_symbol = ai_choice_check(player_symbol)
print(f"The AI symbol is {ai_symbol}")


#THE GAME
while is_game_on:
    create_board()

    player_input(board_pieces)
    win_conditions(board_pieces, player_symbol)
    if not is_game_on:
        break
    ai_input(board_pieces)
    win_conditions(board_pieces, player_symbol)


