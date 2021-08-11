from tkinter import Label, Tk
import time
from datetime import datetime
#define title, window size, resize
app_window = Tk()
app_window.title("Digita Clock")
app_window.geometry("420x180")
app_window.resizable(1,1)
#define font type, size, background, foreground
text_font = ("Boulder", 70, 'bold')
background = "black"
foreground = "white"
border_width = 35

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)
#clock function
def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()



