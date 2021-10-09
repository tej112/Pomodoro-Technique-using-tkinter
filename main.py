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
LONG_BREAK_MIN = 20
CHECK = '✅'
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    if reps != 0:
        window.after_cancel(timer)
    timer_label['text']='Timer'
    canvas.itemconfig(timer_text,text = '00:00')
    check_mark['text']=''
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    if reps > 0:
        window.after_cancel(timer)
        reps = 0
        

    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN *60

    if reps == 9:
        reps = 0

    if reps % 2 ==0:
        if reps == 8:
            count_down(long_break_sec)
            timer_label['text']='Long Break'
            reps = 0
        else:
            count_down(short_break_sec)
            timer_label['text']='Short Break'
    else:
        count_down(work_sec)
        timer_label['text']='Work'
        check_mark['text'] = '✅'* (math.floor(reps/2)+1)

    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text = f'{count_min}:{"0"+str(count_sec) if count_sec < 10 else count_sec }')
    if count > 0:
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100,pady=50,bg=YELLOW)

timer_label = Label(text="Timer", bg=YELLOW, fg='green', font=(FONT_NAME, 25,'bold'))
timer_label.grid(row=0,column=1)

canvas = Canvas(width = 200, height = 224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME,28,'bold'))
canvas.grid(row=1,column=1)

start_button = Button(text='Start',bg = 'blue',width = 15,font = ('',13,'bold'),command=start_timer).grid(row=2,column=0)
reset_button = Button(text='Reset',bg = 'red',width = 15,font = ('',13,'bold'),command=reset_timer).grid(row=2,column=2)
check_mark = Label(fg ='green')
check_mark.grid(row=3,column=1)
window.mainloop()