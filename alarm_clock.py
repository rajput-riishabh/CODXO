###############################################################  DIGITAL CLOCK  #########################################################################
"""
DIGITAL CLOCK : A fully functional digital clock embbeded with current time and date, 
                alarm system , stopwatch and timer.
                This clock will show a popup with your message and play a sound to alert you

"""
#E80087
## importing the required libraries
from tkinter.ttk import *                    #----------
from tkinter import *                        #  for gui   
from tkinter import ttk, messagebox          #----------
from time import strftime,gmtime             # to import real-time date and time 
from PIL import Image, ImageTk               # to import image and resize it
from pygame import mixer                     # to play the sound alert (play sound)
import threading                             # to keep keep the alarm activated in the background



## Initialize the mixer for sound
mixer.init()


## Function to update the clock and date
def update_clock():
    time_string = strftime("%I:%M:%S %p")
    
    time_label.config(text=time_string)
    alarm_time_label.config(text=time_string)
    stopwatch_time_label.config(text=time_string)
    timer_time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)
    
    clock.after(1000, update_clock)


## Function to create a custom popup with deactivate button
def show_alarm_popup(note):
    popup = Toplevel()
    popup.title("Alarm Alert")
    popup.geometry("300x200")
    
    msg = Label(popup, text=note, font=("Helvetica", 14))
    msg.pack(pady=20)
    
    deactivate_button = Button(popup, text="Deactivate", command=lambda: [deactivate_alarm(), popup.destroy()])
    deactivate_button.pack(pady=20)
    
    popup.mainloop()


## Alarm function to check and trigger alarm

def alarm():
    while status == "activated":
        current_time = strftime("%I:%M:%S %p")
        set_time = f"{hr_entry.get()}:{min_entry.get()}:{sec_entry.get()} {ampm_entry.get().upper()}"
        if current_time == set_time:
            mixer.music.load('alarm-clock-short-6402.mp3')
            mixer.music.play(loops=-1)
            show_alarm_popup(note2_entry.get())
            break


## Function to activate the alarm

def activate_alarm():
    global status
    status = "activated"
    t = threading.Thread(target=alarm)  # keep the alarm activated in background
    t.start()


## Function to deactivate the alarm

def deactivate_alarm():
    global status
    status = "deactivated"
    mixer.music.stop()
    hr_entry.delete(0, END)
    min_entry.delete(0, END)
    sec_entry.delete(0, END)
    ampm_entry.delete(0, END)
    note2_entry.delete(0, END)


## Function for Stopwatch

def update_stopwatch():
    if running:
        global counter
        counter += 1
        time_str = strftime('%H:%M:%S', gmtime(counter))
        stopwatch_label.config(text=time_str)
        stopwatch_frame.after(1000, update_stopwatch)

def start_stopwatch():
    global running
    if not running:
        running = True
        update_stopwatch()

def stop_stopwatch():
    global running
    running = False

def reset_stopwatch():
    global counter
    counter = 0
    stopwatch_label.config(text="00:00:00")


## Function for Timer

def update_timer():
    global timer_seconds
    if timer_seconds > 0:
        mins, secs = divmod(timer_seconds, 60)
        hours, mins = divmod(mins, 60)
        time_str = f"{hours:02}:{mins:02}:{secs:02}"
        timer_label.config(text=time_str)
        timer_seconds -= 1
        timer_frame.after(1000, update_timer)
    else:
        mixer.music.load('alarm-clock-short-6402.mp3')
        mixer.music.play()
        show_alarm_popup("Timer Ended!")

def start_timer():
    global timer_seconds
    timer_seconds = int(hours_entry.get()) * 3600 + int(minutes_entry.get()) * 60 + int(seconds_entry.get())
    update_timer()

def stop_timer():
    global timer_seconds
    timer_seconds = 0

def reset_timer():
    global timer_seconds
    timer_seconds = 0
    timer_label.config(text="00:00:00")
    hours_entry.delete(0, END)
    minutes_entry.delete(0, END)
    seconds_entry.delete(0, END)

    
## Main application window

clock = Tk()
clock.title("DIGITAL CLOCK")
clock.geometry("400x400")
clock.resizable(height=True, width=True)

frame_line = Frame(clock, width=500, height=5, bg="blue")
frame_line.pack()

clock_tabs = ttk.Notebook(clock)
clock_tabs.pack(expand=1, fill=BOTH)


# # Home tab for basic info like time, day, and date

home_frame = Frame(clock_tabs, width=480, height=580)
clock_tabs.add(home_frame, text="Time and Date")

time_title = LabelFrame(home_frame, text="Current Time: ")
time_title.pack()

time_label = Label(time_title, font=("Arial", 50), fg="#00FF00", bg="black")
time_label.pack()

frame_line = Frame(home_frame, width=500, height=5, bg="blue")
frame_line.pack()

date_day_title = LabelFrame(home_frame, text="Current Day and Date: ", bd=5)
date_day_title.pack(pady=10)

day_label = Label(date_day_title, font=("Ink Free", 25, "bold"))
day_label.pack()

date_label = Label(date_day_title, font=("Ink Free", 30))
date_label.pack()

frame_line = Frame(home_frame, width=500, height=5, bg="blue")
frame_line.pack()

frame_line = Frame(clock, width=500, height=5, bg="blue")
frame_line.pack()

note1_label = Label(home_frame, font=("Helvetica", 20), fg="#9793FF", justify="center", text="Hope you're having \n a great day!!")
note1_label.pack(pady=20)


# # Alarm tab to set the alarm

alarm_frame = Frame(clock_tabs, width=480, height=580)
clock_tabs.add(alarm_frame, text="Alarm Clock")

alarm_time_title = LabelFrame(alarm_frame, text="Current Time: ")
alarm_time_title.pack()

alarm_time_label = Label(alarm_time_title, font=("Arial", 50), fg="#00FF00", bg="black")
alarm_time_label.pack()

alarm_frame_line = Frame(alarm_frame, width=500, height=5, bg="#E80087")
alarm_frame_line.pack()


# # Image for the alarm

img = Image.open("icons8-alarm-clock-64.png")
img = img.resize((64, 64), Image.LANCZOS)
img = ImageTk.PhotoImage(img)

img_label = Label(alarm_frame, height=80, width=120, image=img, bg="white")
img_label.pack()

set_alarm_frame = Label(alarm_frame, text="Set The Alarm: ", font=("Arial", 12), fg='black')
set_alarm_frame.pack()

# # inputs for setting alarm time

hr_label = Label(alarm_frame, font=("Ink Free", 12, "bold"), text="Hours:")
hr_label.place(x=30, y=210)

hr_entry = Combobox(alarm_frame, font=("Helvetica", 12), width=2)
hr_entry["values"] = [f"{i:02}" for i in range(13)]
hr_entry.current(0)
hr_entry.place(x=40, y=240)

min_label = Label(alarm_frame, font=("Ink Free", 12, "bold"), text="Minutes:")
min_label.place(x=100, y=210)

min_entry = Combobox(alarm_frame, font=("Helvetica", 12), width=2)
min_entry["values"] = [f"{i:02}" for i in range(60)]
min_entry.current(0)
min_entry.place(x=120, y=240)

sec_label = Label(alarm_frame, font=("Ink Free", 12, "bold"), text="Seconds:")
sec_label.place(x=190, y=210)

sec_entry = Combobox(alarm_frame, font=("Helvetica", 12), width=2)
sec_entry["values"] = [f"{i:02}" for i in range(60)]
sec_entry.current(0)
sec_entry.place(x=200, y=240)

ampm_label = Label(alarm_frame, font=("Ink Free", 12, "bold"), text="AM/PM:")
ampm_label.place(x=280, y=210)

ampm_entry = Combobox(alarm_frame, font=("Helvetica", 12), width=3)
ampm_entry["values"] = ['AM', 'PM']
ampm_entry.current(0)
ampm_entry.place(x=290, y=240)

alarm_frame_line = Frame(alarm_frame, width=500, height=5, bg="#E80087")
alarm_frame_line.pack(pady=52)

note2_label = Label(alarm_frame, font=("Ink Free", 12, "bold"), text="Alarm message here:")
note2_label.place(x=10, y=272)

note2_entry = Entry(alarm_frame, font=("Helvetica", 10), width=50)
note2_entry.place(x=8, y=295)


activate_button = Button(alarm_frame, text="Activate", command=activate_alarm, width=20, bd=2)
activate_button.place(x=120, y=328)

# deactivate_button = Button(alarm_frame, text="Deactivate", command=deactivate_alarm, width=20, bd=2)
# deactivate_button.place(x=224, y=328)


# # Stopwatch tab for stopwatch functionality like start,stop and reset

stopwatch_frame = Frame(clock_tabs, width=480, height=580)
clock_tabs.add(stopwatch_frame, text="Stopwatch")

stopwatch_time_title = LabelFrame(stopwatch_frame, text="Current Time: ")
stopwatch_time_title.pack()

stopwatch_time_label = Label(stopwatch_time_title, font=("Arial", 50), fg="#00FF00", bg="black")
stopwatch_time_label.pack()

stopwatch_frame_line = Frame(stopwatch_frame, width=500, height=5, bg="blue")
stopwatch_frame_line.pack()

stopwatch_title = LabelFrame(stopwatch_frame, text="STOPWATCH: ", bd=5)
stopwatch_title.pack()

stopwatch_label = Label(stopwatch_title, font=("Arial", 40), fg="#00FF00", bg="black", text="00:00:00",width=20)
stopwatch_label.pack(pady=20)

stopwatch_frame_line = Frame(stopwatch_frame, width=500, height=5, bg="blue")
stopwatch_frame_line.pack()

start_button = Button(stopwatch_frame, text="Start", command=start_stopwatch, width=20, bd=2)
start_button.pack(pady=10)

stop_button = Button(stopwatch_frame, text="Stop", command=stop_stopwatch, width=20, bd=2)
stop_button.pack(pady=10)

reset_button = Button(stopwatch_frame, text="Reset", command=reset_stopwatch, width=20, bd=2)
reset_button.pack(pady=10)


# Timer tab for countdown functionality

timer_frame = Frame(clock_tabs, width=480, height=580)
clock_tabs.add(timer_frame, text="Timer")

timer_time_title = LabelFrame(timer_frame, text="Current Time: ")
timer_time_title.pack()

timer_time_label = Label(timer_time_title, font=("Arial", 50), fg="#00FF00", bg="black")
timer_time_label.pack()

timer_frame_line = Frame(timer_frame, width=500, height=5, bg="blue")
timer_frame_line.pack()

timer_title = LabelFrame(timer_frame, text="TIMER: ", bd=5)
timer_title.pack()

timer_label = Label(timer_title, font=("Arial", 30), fg="#00FF00", bg="black", text="00:00:00",width=20)
timer_label.pack(pady=20)

timer_frame_line = Frame(timer_frame, width=500, height=5, bg="blue")
timer_frame_line.pack()

hours_label = Label(timer_frame, font=("Ink Free", 12, "bold"), text="Hours:")
hours_label.place(x=50, y=232)

hours_entry = Entry(timer_frame, font=("Helvetica", 12), width=5)
hours_entry.place(x=50, y=255)

minutes_label = Label(timer_frame, font=("Ink Free", 12, "bold"), text="Minutes:")
minutes_label.place(x=140, y=232)

minutes_entry = Entry(timer_frame, font=("Helvetica", 12), width=5)
minutes_entry.place(x=140, y=255)

seconds_label = Label(timer_frame, font=("Ink Free", 12, "bold"), text="Seconds:")
seconds_label.place(x=230, y=232)

seconds_entry = Entry(timer_frame, font=("Helvetica", 12), width=5)
seconds_entry.place(x=230, y=255)

start_timer_button = Button(timer_frame, text="Start", command=start_timer, width=20, bd=2)
start_timer_button.place(x=30, y=285)

stop_timer_button = Button(timer_frame, text="Stop", command=stop_timer, width=20, bd=2)
stop_timer_button.place(x=200, y=285)

reset_timer_button = Button(timer_frame, text="Reset", command=reset_timer, width=20, bd=2)
reset_timer_button.place(x=120, y=320)




## Variables for Alarm
status = "deactivated"

## Variables for Stopwatch 
running = False
counter = 0

## Variables for Timer
timer_seconds = 0


## Start updating the clock
update_clock()

clock.mainloop()
