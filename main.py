from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 1
reps = 0
time_reset = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(time_reset)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checked_label.config("text")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps *= 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break)
        timer_label.config(text="Long Break 😍", fg=YELLOW)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Short Break 😊", fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="work", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global time_reset
        time_reset = window.after(1000, countdown, count - 1)

    else:
        start_timer()
        check = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            check += "✔️"
        checked_label.config(text=check)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodoro")
window.config(pady=100, padx=100, bg=GREEN)

def timer(a, b, c):
    print(a)
    print(b)
    print(c)
window.after(5000, timer,)

canvas = Canvas(width=280, height=224, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(130, 112, image=tomato_img)
timer_text = canvas.create_text(130, 130, text="00:00", fill="white", font=("Courier", 32, "bold"))
canvas.grid(column=1, row=1)


timer_label = Label(text="Timer", fg=RED, bg=GREEN, font=("Courier", 50, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checked_label = Label(fg=RED, bg=GREEN, font=("Arial", 20, "bold"))
checked_label.grid(column=1, row=3)




window.mainloop()