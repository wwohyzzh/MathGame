from random import randint, choice

operation = ("+", "-", "*", "//")

state = {"monsterhealth": 0, "score": 0, "combo": 0, "maxcombo": 0, "mistake": 0}

def true():
    state["monsterhealth"] -= 5
    state["score"] += 1
    state["combo"] += 1

def false():
    state["monsterhealth"] += 10
    state["combo"] = 0
    state["mistake"] += 1

# keep the highest combo value reached
def max_combo():
    if state["combo"] > state["maxcombo"]:
        state["maxcombo"] = state["combo"]

def new_game_state():
    state["monsterhealth"] = 0
    state["score"] = 0
    state["combo"] = 0
    state["maxcombo"] = 0
    state["mistake"] = 0

# choose difficulty
def difficulty(select=None):
    if select is None:
        return None
    try:
        select = int(select)
    except ValueError:
        return None
    if select == 1:
        state["monsterhealth"] = 50
        maxnum = 50
    elif select == 2:
        state["monsterhealth"] = 100
        maxnum = 100
    elif select == 3:
        state["monsterhealth"] = 300
        maxnum = 250
    else:
        return None
    return maxnum

# generating random questions
def generate_question(maxnum=None):
    if maxnum is None:
        return None, None, None
    try:
        maxnum = int(maxnum)     
        op = choice(operation)
        num1 = randint(0, maxnum)
        num2 = randint(0, maxnum)
        return num1, op, num2
    except ValueError:
        return None, None, None

# calculating the random question generated
def calculate_question(num1=None, op=None, num2=None):
    if num1 is None or op is None or num2 is None:
        return None
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        return None
    try:  
        if op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        elif op == "*":
            return num1 * num2
        elif op == "//":
            return num1 // num2
    except ZeroDivisionError:
        return None

# checking the response from the user
def check_reply(result=None, reply=None):
    if result is None or reply is None:
        return None
    try:
        result = int(result)
        reply = int(reply)
    except ValueError:
        return None
    if result == reply:
        true()
        max_combo()
        return True
    else:
        false()
        return False

# checking if the game has been won  
def check_win(health=None):
    if health is None:
        return None
    try:
        health = int(health)
    except ValueError:
        return None
    if health > 0:
        return False
    elif health <= 0:
        new_game_state()
        return True
