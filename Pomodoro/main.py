import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    # timer text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title label "Timer"
    timer_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 50), highlightthickness=0, bg=YELLOW)
    # reset check marks
    c=tick_label.config(text='')
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work Time", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count-1)
    else:
        start_timer()
        marks = ""
        # add check marks for every successful work sessions
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        tick_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
# create window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# create label for timer
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), highlightthickness=0, bg=YELLOW)
timer_label.grid(column=1, row=0)
# create canvas `highlightthickness` is used to remove the border of padding
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# pass file path of image to photo image and store in variable
tomato_img = PhotoImage(file="tomato.png")
# create image in canvas
canvas.create_image(100, 112, image=tomato_img)
# add text to the canvas
timer_text = canvas.create_text(107, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# create start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# create tick mark
tick_label = Label(fg=GREEN, highlightthickness=0, bg=YELLOW)
tick_label.grid(column=1, row=3)

# create reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)








window.mainloop()
