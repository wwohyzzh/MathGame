import random
import time

# Gets the answer from the user
def userinput(op):
    global reply
    global divisionreply
    while True:
        if op == "/":
            try:
                divisionreply = float(input(f"{num1} {op} {num2}: "))
                break
            except ValueError:
                print("Just Enter Numbers!")
        else:
            try:
                reply = int(input(f"{num1} {op} {num2}: "))
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
            print("True! :)")
            print(f"Monster Health: {monsterhealth}")
            print(f"Score: {score} Combo: {combo}")
        else:
            monsterhealth += 10
            combo = 0
            print("False! :(")
            print(f"Monster Health: {monsterhealth}")
            print(f"Score: {score} Combo: {combo}")
    else:
        if result == reply:
            monsterhealth -= 5
            score += 1
            combo += 1
            combos()
            print("True! :)")
            print(f"Monster Health: {monsterhealth}")
            print(f"Score: {score} Combo: {combo}")
        else:
            monsterhealth += 10
            combo = 0
            print("False! :(")
            print(f"Monster Health: {monsterhealth}")
            print(f"Score: {score} Combo: {combo}")

    # The game ends when the monster dies
    if monsterhealth == 0:
        print("YOU WIN! :)")
        combos()
        print(f"Score: {score} Max Combo: {maxcombo}")
        print("Thank you for playing!")
        time.sleep(5)
        break

# Good Luck!