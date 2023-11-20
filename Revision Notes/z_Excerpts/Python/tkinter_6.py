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

    except: #If an error occured while trying to read the file, then just ignore
        pass
    #Add data from the entry boxes to the data variable
    temp_var = ([PlumberID_var.get(), firstname_var.get(), surname_var.get(), gassafe_var.get(), 
    hourlyrate_var.get(), callout_var.get(), years_var.get(), specialism_var.get()])

    if (temp_var[0] == "") : messagebox.showerror('Error', 'Enter a Plumber ID'); return #Make sure that Plumber ID isn't empty
    if (len(temp_var[1]) > 50) : messagebox.showerror('Error', 'First Name is too long'); return #Make sure the name doesn't exceed mac char limit of 50
    if (len(temp_var[2]) > 50) : messagebox.showerror('Error', 'Surame is too long'); return
    #No Validation for gassafe_var since input is already restricted
    try: 
        x =float(temp_var[4]) #Attempt to assign the variable as a float (error occurs if there are non number characters)
        if ((x < 0) or (x > 100)): messagebox.showerror('Error', 'Hourly rate must be between 0 and 100'); return #Range check
    except ValueError: messagebox.showerror('Error', 'Hourly rate must be a number'); return
    try: 
        x =float(temp_var[5])
        if ((x < 0) or (x > 200)): messagebox.showerror('Error', 'Callout rate must be between 0 and 200'); return
    except ValueError: messagebox.showerror('Error', 'Callout rate must be a number'); return
    try: 
        x =str(temp_var[6])
        if ((x < 0) or (x > 100)): messagebox.showerror('Error', 'Callout rate must be between 0 and 100'); return
    except ValueError: messagebox.showerror('Error', 'Years Experience must be a Number'); return
    if (len(temp_var[7]) > 100) : messagebox.showerror('Error', 'Specialism Name is too long'); return

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
        lines = f.readlines() #Stores the text file as a list of lines.
        for x in lines:
            user_data.append(x.split(split_var))
        f.close()

    except:
        messagebox.showerror('Error', 'No Data Saved')
        user_data = []

    temp_save_file = [PlumberID_var.get(), firstname_var.get(), surname_var.get(), gassafe_var.get(), 
    hourlyrate_var.get(), callout_var.get(), years_var.get(), specialism_var.get()]

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
split_var = '  |  ' #This will be used to split up variables in the text file
filename_txt = 'tkinter_6_activity_1.txt' #This is the file location of the save file

Label(text="Plumbers\n", font=('Comic Sans', 25)).pack()

Label(text="PlumberID").pack() #The 'Question' label
PlumberID_var = Entry() #Text entry box
PlumberID_var.pack() #Formater

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

Button(text = 'SAVE', command = save_click).pack() # Buttons call functions when clicked
Button(text = 'COUNT', command = count_click).pack()

win.mainloop() # Runs the window