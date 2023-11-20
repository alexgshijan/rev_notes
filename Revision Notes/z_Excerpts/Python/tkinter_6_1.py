from tkinter import *
from tkinter import messagebox

def save_click():
    pass


def count_click():
    pass


win = Tk()
win.title("Tkinter 6 Activity 1")
GasSafe_var = IntVar()
user_data = []
round_val = 0
split_var = '  |  '
filename_txt = 'tkinter_6_activity_1.txt'

Label(text="Plumbers\n", font=('Comic Sans', 25)).pack()

Label(text="PlumberID").pack()
PlumberID_var = Entry()
PlumberID_var.pack()

Label(text="First Name").pack()
firstname_var = Entry()
firstname_var.pack()

Label(text="Surname").pack()
surname_var = Entry()
surname_var.pack()

Label(text="Gas Safe").pack()
Radiobutton(text="Yes", variable=gassafe_var, value= 1).pack()
Radiobutton(text="No", variable= gassafe_var, value= 0).pack()

Label(text="Hourly Rate").pack()
hourlyrate_var = Entry()
hourlyrate_var.pack()

Label(text="Call Out Price").pack()
callout_var = Entry()
callout_var.pack()

Label(text="Years Experience").pack()
years_var = Entry()
years_var.pack()

Label(text="Specialism").pack()
specialism_var = Entry()
specialism_var.pack()

Button(text = 'SAVE', command = save_click).pack()
Button(text = 'COUNT', command = count_click).pack()

win.mainloop()