from random import randint, choice
from time import sleep

# Helper function to reduce duplicate print statements
def display_game_state(message, correct_answer=None, combo_color=34):
    print(f"\n{message}")
    
    if correct_answer is not None:
        print(f"Correct answer: {correct_answer}\n")
    
    monsterhealth = f"\33[31mMonster Health:\033[0m {state['monsterhealth']}"
    score = f"\033[32mScore:\033[0m {state['score']}"
    combo = f"\033[{combo_color}mCombo:\033[0m {state['combo']}"
    
    print(monsterhealth)
    print(f"{score} {combo}\n")

# Difficulty selection screen
def difficulty():
    while True:
        try:
            print("Select Difficulty:\n\033[31m1 Hard\033[0m \033[33m2 Medium\033[0m \033[32m3 Easy\033[0m")
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
                print("Just select 1, 2 and 3\n")
        except ValueError:
            print("\nJust select 1, 2 and 3\n")
    return maxnum

# Gets the answer from the user
def userinput():
    while True:
        try:
            reply = int(input(f"\033[4;33m{num1} {op} {num2}:\033[0m "))
            break
        except ValueError:
            print("Just Enter Numbers!")
    return reply

# Doing math operations
def number(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "//":
        try:
            return num1 // num2
        except ZeroDivisionError:
            return None

def true():
    state["monsterhealth"] -= 5
    state["score"] += 1
    state["combo"] += 1

def false():
    state["monsterhealth"] += 10
    state["combo"] = 0
    state["mistake"] += 1

# Record maximum combo value
def combos():
    if state["combo"] > state["maxcombo"]:
        state["maxcombo"] = state["combo"]

state = {"monsterhealth": 0, "score": 0, "combo": 0, "maxcombo": 0, "mistake": 0}

operation = ("+", "-", "*", "//")

maxnum = difficulty()

# Loop
while True:

    num1 = randint(0, maxnum)
    num2 = randint(0, maxnum)

    op = choice(operation)
    
    # Problem result
    result = number(num1, num2, op)
    
    if result is None:
        continue
    
    reply = userinput()

    # Comparing results and answers
    if result == reply:
        true()
        combos()
        display_game_state("\033[32mTrue! :)\033[0m")
    else:
        false()
        display_game_state("\033[31mFalse! :(\033[0m", correct_answer=result, combo_color=31)

    # The game ends when the monster dies
    if state["monsterhealth"] == 0:
        combos()
        print(f"\n\n\033[1;32;40mYOU WIN! :)\033[0m\n"
              f"\033[32mScore:\033[0m {state['score']} "
              f"\033[34mMax Combo:\033[0m {state['maxcombo']} "
              f"\033[31mMistakes made:\033[0m {state['mistake']}\n"
              f"Thank you for playing!")
        sleep(5)
        break

# Good Luck!