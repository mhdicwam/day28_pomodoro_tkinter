import tkinter
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.5
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.3
reps = 0
timer = None


# site for color : colorhunt.co  # program event driven
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    label_title.config(text="Timer")
    label_checkmark.config(text="")
    canvas.itemconfig(text_timer, text="00:00")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global btn_start
    # btn_start.configure(state=DISABLED)
    reps += 1
    print(reps)
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 8:
        count_down(long_break_sec)
        label_title.config(text="long Break Time", fg=RED)
    elif reps % 2 == 1:
        label_title.config(text="Work Time", fg=GREEN)
        count_down(work_sec)
    else:
        label_title.config(text="Break Time", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(text_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks = "✔"
        label_checkmark.config(text=marks)

    # --------------- UI SETUP ------------------------------- #


window = Tk()
window.title(" POMODOOOROOO TOM1TO POWER BITCH ")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)

text_timer = canvas.create_text(100, 132, text="00:00", fill="black", font=(FONT_NAME, 23, "bold"))
canvas.grid(column=1, row=1)

# Label
label_title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
label_title.grid(column=1, row=0)

# checkmark
label_checkmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
label_checkmark.grid(column=1, row=3)

# button
btn_rest = Button(text="Reset", command=reset_timer)
btn_rest.grid(column=2, row=2)

btn_start = Button(text="Start", command=start_timer)
btn_start.grid(column=0, row=2)
window.mainloop()
