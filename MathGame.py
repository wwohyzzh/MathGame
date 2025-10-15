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


operation = ("+", "-", "*", "/")

monsterhealth = 100

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
            print("True! :)")
            print(f"Monster Health: {monsterhealth}")
        else:
            monsterhealth += 10
            print("False! :(")
            print(f"Monster Health: {monsterhealth}")
    else:
        if result == reply:
            monsterhealth -= 5
            print("True! :)")
            print(f"Monster Health: {monsterhealth}")
        else:
            monsterhealth += 10
            print("False! :(")
            print(f"Monster Health: {monsterhealth}")

    # The game ends when the monster dies
    if monsterhealth == 0:
        print("YOU WIN! :)")
        print("Thank you for playing!")
        time.sleep(5)
        break

# Good Luck!