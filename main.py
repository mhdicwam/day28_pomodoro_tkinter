from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# site for color : colorhunt.co  # program event driven
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    canvas.itemconfig(text_timer, text=count)
    window.after(1000, count_down, count - 1)


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

label_checkmark = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
label_checkmark.grid(column=1, row=3)

# button
btn_rest = Button(text="Reset")
btn_rest.grid(column=2, row=2)

btn_start = Button(text="Start", command=start_timer)
btn_start.grid(column=0, row=2)
window.mainloop()
