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
reps = 0 
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    reps = 0 



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # work_sec = 5
    # short_break_sec = 2
    # long_break_sec = 3
    reps +=1
    
    if reps % 2 != 0:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    else:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
        


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global timer
    count_min = count // 60
    count_sec = count % 60
    if len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps > 0 and reps % 2 == 0:
            check_label.config(text="✔"*(reps//2))
        start_timer() 






# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# canvas widget 여러 겹으로 쌓을 수 있음 

canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)



# Timer Label 

timer_label = Label(text="Timer",bg=YELLOW, highlightthickness=0 ,fg=GREEN, font=(FONT_NAME, 50, "bold"))
timer_label.grid(row=0, column=1)

# start button 

start_button = Button(text="Start",command=start_timer)
start_button.grid(row=2, column=0)

# reset button 

reset_button = Button(text="Reset",command=reset_timer)
reset_button.grid(row=2, column=2)

# check box label 

check_label = Label(bg=YELLOW, highlightthickness=0, fg=GREEN)
check_label.grid(row=3, column=1)

window.mainloop()