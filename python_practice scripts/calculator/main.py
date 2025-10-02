from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculator_dict = {"+": add,
                   "-": subtract,
                   "*": multiply,
                   "/": divide,
                   }


def calculator():
    print(logo)
    should_continue = False
    user_input1 = float(input("Input your first number: "))

    while not should_continue:
        for symbol in calculator_dict:
            print(symbol)
        calculator_symbol = input("Choose your operation symbol: ")
        if calculator_symbol not in calculator_dict:
            print("Learn to type, restarting")
            calculator_symbol = input("Choose your operation symbol: ")

        user_input2 = float(input("Input your second number: "))

        result = calculator_dict[calculator_symbol](user_input1, user_input2)
        print(f"{user_input1} {calculator_symbol} {user_input2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or  type 'exit' to end the program: ").lower()

        if choice == 'y':
            user_input1 = result

        elif choice == 'exit':
            should_continue = True

        else:
            should_continue = True
            print("\n" * 20)
            calculator()

calculator()