import random
import time

# Utility: Print colored text
def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

# Utility: Print error messages
def print_error(message):
    print_colored(message, "1;31")  # Bold red

# Utility: Print difficulty options
def print_difficulty_options():
    print("Select Difficulty:")
    print_colored("1 Hard", "31")
    print_colored("2 Medium", "33")
    print_colored("3 Easy", "32")

# Difficulty selection screen
def difficulty(state):
    global maxnum
    while True:
        try:
            print_difficulty_options()
            select = int(input("Select: "))
            print("")
            if select == 1:
                state["monsterhealth"] = 300
                maxnum = 250
                break
            elif select == 2:
                state["monsterhealth"] = 100
                maxnum = 100
                break
            elif select == 3:
                state["monsterhealth"] = 50
                maxnum = 50
                break
            else:
                print_error("Just select 1, 2 or 3\n")
        except ValueError:
            print_error("Just select 1, 2 or 3\n")

# Gets the answer from the user
def userinput(op):
    global reply
    while True:
        try:
            reply = int(input(f"\033[4;33m{num1} {op} {num2}:\033[0m "))
            break
        except ValueError:
            print_error("Just Enter Numbers!")

# Doing math operations
def number(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "//":
        return num1 // num2

# Correct answer logic
def true(state):
    state["monsterhealth"] -= 5
    state["score"] += 1
    state["combo"] += 1

# Incorrect answer logic
def false(state):
    state["monsterhealth"] += 10
    state["combo"] = 0
    state["mistake"] += 1

# Record maximum combo value
def combos(state):
    if state["combo"] > state["maxcombo"]:
        state["maxcombo"] = state["combo"]

# Print current game status
def print_status(state):
    print_colored("Monster Health:", "31")
    print(f"{state['monsterhealth']}")
    print_colored("Score:", "32")
    print(f"{state['score']} ", end="")
    print_colored("Combo:", "34")
    print(f"{state['combo']}\n")

# Print result of a round
def print_result(is_correct, result=None):
    if is_correct:
        print_colored("\nTrue! :)", "1;32")
    else:
        print_colored("\nFalse! :(", "1;31")
        print(f"Correct answer: {result}\n")

# Print final game summary
def print_summary(state):
    print_colored("\n\nYOU WIN! :)", "1;32;40")
    print_colored("Score:", "32")
    print(f"{state['score']} ", end="")
    print_colored("Max Combo:", "34")
    print(f"{state['maxcombo']} ", end="")
    print_colored("Mistakes made:", "31")
    print(f"{state['mistake']}")
    print("Thank you for playing!")

# Game state
state = {"monsterhealth": 0, "score": 0, "combo": 0}

# Main game loop
def main():
    global num1, num2
    state["mistake"] = 0
    state["maxcombo"] = 0

    difficulty(state)

    while state["monsterhealth"] > 0:
        op = random.choice(["+", "-", "*", "//"])
        num1 = random.randint(1, maxnum)
        num2 = random.randint(1, maxnum)

        if op == "//":
            num2 = random.randint(1, maxnum)  # Avoid division by zero

        correct = number(num1, num2, op)
        userinput(op)

        if reply == correct:
            true(state)
            print_result(True)
        else:
            false(state)
            print_result(False, correct)

        combos(state)
        print_status(state)
        time.sleep(0.5)

    print_summary(state)

if __name__ == "__main__":
    main()