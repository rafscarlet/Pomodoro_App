from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
# Palette from https://colorhunt.co
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK_TEXT = "✓"
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    top_label.config(text="Timer", fg=GREEN)
    bot_label.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_secs=WORK_MIN*60
    short_break_secs = SHORT_BREAK_MIN *60
    long_break_secs = LONG_BREAK_MIN *60
    # # Test
    # work_secs = 5
    # short_break_secs = 5
    # long_break_secs = 5

    # If 8th rep do long break
    if reps % 8 == 0:
        count_down(long_break_secs)
        top_label.config(text='Break', fg=RED)

    # If 2/4/6th rep do short break
    elif reps % 2 == 0:
        count_down(short_break_secs)
        top_label.config(text='Break', fg=PINK)

    # If 1/3/5/7th rep do work
    else:
        count_down(work_secs)
        top_label.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    # Convert the count from seconds to minutes & seconds
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f'0{count_min}'
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')

    if count > 0:
        # Use count_down function with argument count-1 AFTER 1000 ms (milliseconds) = 1 sec
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()
        mark = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += TICK_TEXT
        bot_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App🍅")
window.config(padx=100, pady=50, bg=YELLOW)

# Labels
top_label = Label(text="Timer", fg=GREEN, font=(
    FONT_NAME, 40, "bold"), bg=YELLOW)
top_label.grid(row=0, column=1)


bot_label = Label(fg=GREEN, font=(FONT_NAME, 15, "bold"), bg=YELLOW)
bot_label.grid(row=3, column=1)

# Buttons
start_button = Button(text='Start', font=(
    FONT_NAME, 10, "normal"), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', font=(FONT_NAME, 10, "normal"), command=timer_reset)
reset_button.grid(row=2, column=2)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)  # center of canvas
timer_text = canvas.create_text(
    100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


window.mainloop()
