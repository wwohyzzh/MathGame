import random
import time

# Gets the answer from the user
def userinput(op):
    global reply
    global divisionreply
    while True:
        if op == "/":
            try:
                divisionreply = float(input(f"\033[4;33m{num1} {op} {num2}:\033[0m "))
                break
            except ValueError:
                print("Just Enter Numbers!")
        else:
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
    elif op == "/":
        return num1 / num2

def combos():
    global combo
    global maxcombo
    
    if combo > maxcombo:
        maxcombo = combo

operation = ("+", "-", "*", "/")

monsterhealth = 100

combo = 0

maxcombo = 0

score = 0

tolerance = 0.5

# Loop
while True:

    num1 = random.randint(0, 100)
    num2 = random.randint(1, 100)
    
    op = random.choice(operation)
    
    # Problem result
    result = number(num1, num2, op)
    userinput(op)

    # Comparing results and answers
    if op == "/":
        if abs(result - divisionreply) <= tolerance:
            monsterhealth -= 5
            score += 1
            combo += 1
            combos()
            print("\033[1;32mTrue! :)\033[0m")
            print(f"\33[31mMonster Health:\033[0m {monsterhealth}")
            print(f"\033[32mScore:\033[0m {score} \033[34mCombo:\033[0m {combo}")
        else:
            monsterhealth += 10
            combo = 0
            print("\033[1;31mFalse! :(\033[0m")
            print(f"\33[31mMonster Health:\033[0m {monsterhealth}")
            print(f"\033[32mScore:\033[0m {score} \033[31mCombo:\033[0m {combo}")
    else:
        if result == reply:
            monsterhealth -= 5
            score += 1
            combo += 1
            combos()
            print("\033[1;32mTrue! :)\033[0m")
            print(f"\33[31mMonster Health:\033[0m {monsterhealth}")
            print(f"\033[32mScore:\033[0m {score} \033[34mCombo:\033[0m {combo}")
        else:
            monsterhealth += 10
            combo = 0
            print("\033[1;31mFalse! :(\033[0m")
            print(f"\33[31mMonster Health:\033[0m {monsterhealth}")
            print(f"\033[32mScore:\033[0m {score} \033[31mCombo:\033[0m {combo}")

    # The game ends when the monster dies
    if monsterhealth == 0:
        print("\033[1;32;40mYOU WIN! :)\033[0m")
        combos()
        print(f"\033[32mScore:\033[0m {score} \033[34mMax Combo:\033[0m {maxcombo}")
        print("Thank you for playing!")
        time.sleep(5)
        break

# Good Luck!