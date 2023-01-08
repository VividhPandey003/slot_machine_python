import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    # if the user enters 1 then it goes from 0-0 if 2lines then 0-1 i.e index of lines (looping through every row)
    for line in range(lines):
        # we refer to first element in the column whatever might be the line number thus [0]
        symbol = columns[0][line]
        for column in columns:  # we loop through every single column and check for that symbol that occured in the first index
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break  # if symbols are not the same, go to the next line
            else:
                winnings += values[symbol]*bet
                winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        # "_" is used as an anonymous var in python.
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        # you put a [:] colon inside list parameters to copy a list= slice operator
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:  # maximum index we have is len(cols)-1
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("What would you like to deposit? ₹")
        if amount.isdigit():
            amount = int(amount)  # convert string to int
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on: (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)  # convert string to int
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines


def get_bet():
    while True:
        amount = input(
            "Enter the amount you want to bet on each line? ₹ ")
        if amount.isdigit():
            amount = int(amount)  # convert string to int
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ₹{MIN_BET} - ₹{MAX_BET}. ")
        else:
            print("Please enter a number.")
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(
                f"You have insufficient balance, Your current balance is ₹{balance}")
        else:
            break

    print(
        f"You are betting ₹{bet} on {lines} lines. Total bet is equal to ₹{total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)

    print(f"You won ₹{winnings}!!")
    # '*' is a splat/unpack operator
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You are left with ₹{balance}")


main()
