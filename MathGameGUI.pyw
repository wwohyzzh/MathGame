import MathGameEngine as game
import tkinter as tk

# adjust difficulty
def diff_select(select):
    global maxnum
    
    if select == 1:
        maxnum = game.difficulty(1)
        diff_label.config(text="Easy", fg="green")
    elif select == 2:
        maxnum = game.difficulty(2)
        diff_label.config(text="Medium", fg="orange")
    elif select == 3:
        maxnum = game.difficulty(3)
        diff_label.config(text="Hard", fg="red")

    select_screen.withdraw()
    screen.deiconify()
    start()
    state()

# random question generation
def generate_quest():
    global result
    
    num1, op, num2 = game.generate_question(maxnum)
    quest_label.config(text=f"{num1} {op} {num2}", fg="black")
    result = game.calculate_question(num1, op, num2)
    enter_reply.delete(0, "end")
    new_quest_button.place_forget()

# updating values ​​with each response
def state():
    health_label.config(text=f"Monster Health: {game.state["monsterhealth"]}")
    score_label.config(text=f"Score: {game.state["score"]}")
    combo_label.config(text=f"Combo: {game.state["combo"]}")
    max_combo_label.config(text=f"Max Combo: {game.state["maxcombo"]}")
    mistake_label.config(text=f"Mistakes: {game.state["mistake"]}")

# checking the response from the user
def check_reply():
    reply = enter_reply.get()
    answer = game.check_reply(result, reply)
    
    if answer is True:
        quest_label.config(text="True!", fg="green")
        new_quest_button.place(x=55, y=85, anchor="center")
        combo_label.config(fg="green")
        state()
    elif answer is False:
        quest_label.config(text="False!", fg="red")
        new_quest_button.place(x=55, y=85, anchor="center")
        combo_label.config(fg="red")
        enter_reply.delete(0, "end")
        enter_reply.insert(0, f"Correct Answer: {result}")
        state()

    ## check win status
    win = game.check_win(game.state["monsterhealth"])

    if win is True:
        screen.withdraw()
        win_screen.deiconify()
    elif win is False:
        pass

# start the game
def start():
    generate_quest()
    while result is None:
        generate_quest()
        break

screen = tk.Tk()
screen.title("MathGame")
screen.geometry("250x250")
screen.config(bg="beige")
screen.resizable(False, False)
screen.withdraw()

frame1 = tk.Frame(screen, bd=3, relief="groove", bg="beige", width=200, height=110)
frame1.place(x=25, y=15)

quest_label = tk.Label(frame1, text="", bg="beige", font=("arial", 15, "bold"))
quest_label.place(x=100, y=25, anchor="center")

enter_reply = tk.Entry(frame1)
enter_reply.place(x=100, y=55, anchor="center")

check_button = tk.Button(frame1, text="Check", command=check_reply)
check_button.place(x=140, y=85, anchor="center")

new_quest_button = tk.Button(frame1, text="Next", command=start)

frame2 = tk.Frame(screen, bd=3, relief="groove", bg="beige", width=150, height=75)
frame2.place(x=100, y=185, anchor="center")

health_label = tk.Label(frame2, fg="red", bg="beige", text="")
health_label.place(x=5, y=0)

score_label = tk.Label(frame2, fg="blue", bg="beige", text="")
score_label.place(x=5, y=15)

combo_label = tk.Label(frame2, fg="green", bg="beige", text="")
combo_label.place(x=55, y=15)

max_combo_label = tk.Label(frame2, fg="orange", bg="beige", text="")
max_combo_label.place(x=5, y=30)

mistake_label = tk.Label(frame2, fg="red", bg="beige", text="")
mistake_label.place(x=5, y=45)

diff_label = tk.Label(frame2, bg="beige", text="")
diff_label.place(x=85, y=45)

select_screen = tk.Toplevel()
select_screen.title("Select Difficulty")
select_screen.geometry("275x100")
select_screen.config(bg="beige")
select_screen.resizable(False, False)

diff1 = tk.Button(select_screen, text="Easy", fg="green", command=lambda: diff_select(1))
diff1.place(x=40, y=30)

diff2 = tk.Button(select_screen, text="Medium", fg="orange", command=lambda: diff_select(2))
diff2.place(x=110, y=30)

diff3 = tk.Button(select_screen, text="Hard", fg="red", command=lambda: diff_select(3))
diff3.place(x=200, y=30)

win_screen = tk.Toplevel()
win_screen.title("Win!")
win_screen.geometry("300x150")
win_screen.config(bg="beige")
win_screen.resizable(False, False)
win_screen.withdraw()

new_game_button = tk.Button(win_screen, text="New Game", fg="blue", command=lambda:(win_screen.withdraw(), select_screen.deiconify()))
new_game_button.place(x=30, y=85)

exit_button = tk.Button(win_screen, text="Exit Game", fg="red", command=lambda: screen.destroy())
exit_button.place(x=200, y=85)

win_label = tk.Label(win_screen, text="You Win :)", fg="green", bg="beige", font=("arial", 25, "bold"))
win_label.place(x=150, y=30, anchor="center")

thanks_label = tk.Label(win_screen, text="Thank You For Playing!", bg="beige", fg="green", font=("arial", 10, "bold"))
thanks_label.place(x=150, y=60, anchor="center")

screen.mainloop()
select_screen.mainloop()
win_screen.mainloop()
