
from tkinter import *
from pygame import mixer

# ---------------------------- CONSTANTS ----------------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30

timer = None
mixer.init()

# ---------------------------- TIMER RESET --------------------------------------- # 

def reset_timer():
    if (timer):
        window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    check_mark_label.config(text="")
    canvas.itemconfig(timer_text, text=f"00:00")

# ---------------------------- TIMER MECHANISM ----------------------------------- # 

def bring_to_front():
    window.attributes('-topmost', True)
    window.attributes('-topmost', False)

def start_timer(round=0):
    round += 1

    if round % 8 == 0:
        check_mark_label.config(text="")
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60, round)
    elif round % 2 == 0:
        check_marks_count = (round // 2) % 4
        check_mark_label.config(text=CHECK_MARK * check_marks_count)
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60, round)
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60, round)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(time_in_seconds, round):

    minutes = time_in_seconds // 60
    remaining_seconds = time_in_seconds % 60

    if (minutes < 10): minutes = f"0{minutes}"
    if (remaining_seconds < 10): remaining_seconds = f"0{remaining_seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{remaining_seconds}")
    if (time_in_seconds == 3):
        mixer.Sound('countdown.wav').play()
        bring_to_front()
    if (time_in_seconds == 0):
        start_timer(round)
    else:
        global timer
        timer = window.after(1000, count_down, time_in_seconds - 1, round)

# ---------------------------- UI SETUP ------------------------------------------ #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", font=(FONT_NAME, 28, "bold"), fill="white")
canvas.grid(row=1, column=1)

timer_label = Label(
    text="Timer",
    font=(FONT_NAME, 45, "bold"),
    fg=GREEN, bg=YELLOW,
    highlightthickness=0
)

timer_label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark_label = Label(
    text="",
    font=(FONT_NAME, 35, "normal"),
    fg=GREEN,
    bg=YELLOW,
    highlightthickness=0
)
check_mark_label.grid(row=3, column=1)



window.mainloop()