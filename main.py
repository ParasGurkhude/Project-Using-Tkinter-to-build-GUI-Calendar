from tkinter import *
from tkcalendar import *

root = Tk()

def choice_date():
    present_date = display_cal.get_date()
    user_date =Label(text = present_date)
    user_date.pack(padx=5,pady=5)



display_cal = Calendar(root, stemode="day", date_pattern ="dd/mm/yy")
display_cal.pack(padx=20,pady=20)

open_cal = Button(root, text = "Select Date", command= choice_date)
open_cal.pack(padx=20,pady=20)

root.geometry('500x500')
root.title("GIU Calendar")
root.configure(bg = "sky blue")
root.mainloop()