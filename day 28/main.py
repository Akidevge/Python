import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(fg=GREEN, text="Timer")
    check_mark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    if reps == 0 or reps % 2 == 0:
        count = WORK_MIN
        label.config(fg=GREEN, text="Work")
    elif reps % 7 == 0:
        count = LONG_BREAK_MIN
        label.config(fg=RED, text="L_Break")
    else:
        count = SHORT_BREAK_MIN
        label.config(fg=PINK, text="S_Break")
    count_down(count)
    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    min = int(count/60)
    sec = int(count % 60)
    if sec == 0:
        sec = "00"
    elif int(sec) < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work = math.floor(reps/2)
        for x in range(work):
            mark += "✓"
            check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
label.grid(column=1, row=0)
img = tkinter.PhotoImage(file=r"D:\Python\day 28\tomato.png")
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
count = 10
start_button = tkinter.Button(
    text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = tkinter.Button(
    text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)
check_mark = tkinter.Label(fg=GREEN, bg=YELLOW, highlightthickness=0)
check_mark.grid(column=1, row=3)
window.mainloop()
