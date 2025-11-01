import random
import time

# Gets the answer from the user
def userinput(op):
    global reply
    while True:
        try:
            reply = int(input(f"\033[4;33m{num1} {op} {num2}:\033[0m "))
            break
        except ValueError:
            print("Just Enter Numbers!")

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

def true(state):
    state["monsterhealth"] -= 5
    state["score"] += 1
    state["combo"] += 1

def false(state):
    state["monsterhealth"] += 10
    state["combo"] = 0

# Record maximum combo value
def combos(state):
    if state["combo"] > state["maxcombo"]:
        state["maxcombo"] = state["combo"]

state = {"monsterhealth": 100, "score": 0, "combo": 0, "maxcombo": 0}

operation = ("+", "-", "*", "//")

# Loop
while True:

    num1 = random.randint(0, 100)
    num2 = random.randint(1, 100)
    
    op = random.choice(operation)
    
    # Problem result
    result = number(num1, num2, op)
    userinput(op)

    # Comparing results and answers
    if result == reply:
        true(state)
        combos(state)
        print("\033[1;32mTrue! :)\033[0m")
        print(f"\33[31mMonster Health:\033[0m {state["monsterhealth"]}")
        print(f"\033[32mScore:\033[0m {state['score']} \033[34mCombo:\033[0m {state["combo"]}")
    else:
        false(state)
        print("\033[1;31mFalse! :(\033[0m")
        print(f"\33[31mMonster Health:\033[0m {state["monsterhealth"]}")
        print(f"\033[32mScore:\033[0m {state["score"]} \033[31mCombo:\033[0m {state["combo"]}")

    # The game ends when the monster dies
    if state["monsterhealth"] == 0:
        print("\033[1;32;40mYOU WIN! :)\033[0m")
        combos(state)
        print(f"\033[32mScore:\033[0m {state["score"]} \033[34mMax Combo:\033[0m {state["maxcombo"]}")
        print("Thank you for playing!")
        time.sleep(5)
        break

# Good Luck!