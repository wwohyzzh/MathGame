import random
import time

# Function to get user's input for a given operation
def userinput(opp):
    global reply
    while True:
        try:
            # Ask the user to solve the math problem
            reply = int(input(f"{num1} {opp} {num2}: "))
            break
        except ValueError:
            # Handle invalid input
            print("Just Enter Numbers!")

# List of possible math operations
operation = ("+", "-", "*", "/")

# Initial health of the monster
monsterhealth = 100

# Tolerance for division answers (because of decimals)
tolerance = 0.5

# Game Loop
while True:

    # Generate two random numbers
    num1 = random.randint(0, 100)
    num2 = random.randint(1, 100)
    
    # Randomly choose an operation
    op = random.choice(operation)

    # Calculate the correct result based on the operation
    if op == "+":
        userinput("+")
        result = int(num1) + int(num2)
    elif op == "-":
        userinput("-")
        result = int(num1) - int(num2)
    elif op == "*":
        userinput("*")
        result = int(num1) * int(num2)
    elif op == "/":
        # For division, allow float input
        result = num1 / num2
        while True:
            try:
                divisionreply = float(input(f"{num1} / {num2}: "))
                break
            except ValueError:
                print("Just Enter Numbers!")
    
    # Check user's answer and update monster's health
    if op == "/":
         # Check if user's answer is within tolerance
        if abs(result - divisionreply) <= tolerance:
            monsterhealth -= 5
            print("True! :)")
            print(f"Monster Health: {monsterhealth}")
        else:
            monsterhealth += 10
            print("False! :(")
            print(f"Monster Health: {monsterhealth}")
    else:
        # Check answer for +, -, * operations
        if result == reply:
            monsterhealth -= 5
            print("True! :)")
            print(f"Monster Health: {monsterhealth}")
        else:
            monsterhealth += 10
            print("False! :(")
            print(f"Monster Health: {monsterhealth}")
    
    # Check if monster is defeated
    if monsterhealth == 0:
        print("YOU WIN! :)")
        print("Thank you for playing!")
        time.sleep(5)
        break

# Good Luck!