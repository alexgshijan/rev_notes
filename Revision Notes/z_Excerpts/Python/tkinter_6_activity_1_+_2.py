from tkinter import *
from tkinter import messagebox

def save_click():
    user_data = []
    try:
        f = open(filename_txt, "r") #Tries to read in any existing data
        lines = f.readlines()
        for x in lines:
            user_data.append(x.split(split_var))
        f.close()

    except:
        pass
    #Add data from the entry boxes to the data variable
    temp_var = ([PlumberID_var.get(), firstname_var.get(), surname_var.get(), gassafe_var.get(), 
    hourlyrate_var.get(), callout_var.get(), years_var.get(), experience_var.get()])

    if (temp_var[0] == "") : messagebox.showerror('Error', 'Enter a Plumber ID'); return
    if (len(temp_var[1]) > 50) : messagebox.showerror('Error', 'Name is too long'); return
    if () :
        pass

    user_data.append(temp_var)

    temp_save_file = []
    for i in user_data: #Formats the data variable to be saved as txt
        temp_save_file_var = ''
        for x in i:
            temp_save_file_var += (x + split_var)
        temp_save_file_var = temp_save_file_var[:-(len(split_var))]
        temp_save_file.append(temp_save_file_var)

    f = open(filename_txt, "w") #Saves the formatted data variable 
    f.writelines(temp_save_file)
    f.close()


def count_click():
    try:
        f = open(filename_txt, "r")
        lines = f.readlines()
        for x in lines:
            user_data.append(x.split(split_var))
        f.close()

    except:
        messagebox.showerror('Error', 'No Data Saved')
        user_data = []

    temp_save_file = [PlumberID_var.get(), firstname_var.get(), surname_var.get(), gassafe_var.get(), 
    hourlyrate_var.get(), callout_var.get(), years_var.get(), experience_var.get()]

    accum = 0 #See if there are any exact matches in the data
    for i in user_data:
        if i == temp_save_file:
            accum += 1
    output_text.delete(0.0, END)
    output_text.insert(END, f"{accum} matches recalled")


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

Label(text="Experience").pack()
experience_var = Entry()
experience_var.pack()

Button(text = 'SAVE', command = save_click).pack()
Button(text = 'COUNT', command = count_click).pack()

win.mainloop()