from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SECONDS_IN_HOUR = 60
reps = 0
timer = None

def start_app():
    global reps
    reps += 1
    work_seconds = WORK_MIN * SECONDS_IN_HOUR
    short_break_seconds = SHORT_BREAK_MIN * SECONDS_IN_HOUR
    long_break_seconds = LONG_BREAK_MIN * SECONDS_IN_HOUR


    if reps % 8 == 0:
        count_down(long_break_seconds)
        timer_title_label.config(text="Long Break", fg=RED)
    elif reps % 2 ==0:
        count_down(short_break_seconds)
        timer_title_label.config(text="Short Break", fg= PINK)
    else:
        count_down(work_seconds)
        timer_title_label.config(text="Work Time", fg=GREEN)

    start_button.config(state="disabled")

def reset_app():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_title_label.config(text="Timer")
    mark_label.config(text="")
    global reps
    reps = 0

    start_button.config(state="normal")

def count_down(counter):
    counter_minute = math.floor(counter / SECONDS_IN_HOUR)
    counter_second = counter % SECONDS_IN_HOUR
    if counter_second < 10:
        counter_second = f"0{counter_second}"


    canvas.itemconfig(timer_text, text=f"{counter_minute}:{counter_second}")
    if counter > 0:
        global timer
        timer = window.after(1000, count_down, counter - 1)
    else:
        start_app()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        mark_label.config(text = mark)


# _________________________________ UI _________________________________ #
window = Tk()
window.title("Time Manager App")
window.config(padx=100,pady=50,bg=YELLOW)


timer_title_label = Label(text="Timer",bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
timer_title_label.grid(column=1,row=0)

mark_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20))
mark_label.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
background_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=background_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_app)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_app)
reset_button.grid(column=2,row=2)














window.mainloop()