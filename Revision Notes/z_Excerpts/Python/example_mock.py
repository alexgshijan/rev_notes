from tkinter import *
from tkinter import messagebox


def submit_click():
    try:
        int(id_var.get())
        if id_var.get() == "":
            messagebox.error('Entry Validation Failed', 'Client ID must not be empty')
            return
    except:
        messagebox.error('Entry Validation Failed', 'Client ID must be an integer')
        return
    if len(name_var.get()) > 50:
        messagebox.error('Entry Validation Failed', 'Name cannot be more than 50 characters')
        return

    if not ( 101 > age_var.get() > -1):
        messagebox.error('Entry Validation Failed', 'Age must be between 0 and 100')
        return

    user_data = [] 
    try: 
        f = open(filename_txt, "r") 
        lines = f.readlines() 
        for x in lines: 
            user_data.append(x.split(split_var)) 
        f.close()

    except:
        pass
    temp_var = [id_var.get(), name_var.get(), age_var.get(), swimming_var.get(), gym_var.get(),aerobics_var.get(),badminton_var.get(),squash_var.get()]


    user_data.append(temp_var) #If it passes all the validation, then add it to user_data

    temp_save_file = [] 
    for i in user_data: #Formats the data variable to be saved as txt
        temp_save_file_var = ''
        for x in i: #runs through all the variables in i within userdata
            temp_save_file_var += (x + split_var) 
        temp_save_file_var = temp_save_file_var[:-(len(split_var))] #removes the last split_var
        temp_save_file.append(temp_save_file_var) 

    f = open(filename_txt, "w") #Saves the formatted data variable 
    f.writelines(temp_save_file) #write the list line by line
    f.close()



    return

def search_click():
    try:
        fileObject = open(filename_txt, 'r')
    except:
        messagebox.showerror('File Operation Error', f'Could not find file {filename_txt}')



win = Tk()
filename_txt = 'customerdetails.txt'
split_var = '   |   '

Label(text='Fitness Leisure Centre', font=('arial', 20)).pack()

Label(text='Client ID').pack()
id_var = Entry()
id_var.pack()

Label(text='Customer Name').pack()
name_var = Entry()
name_var.pack()

Label(text='Customer Age').pack()
age_var = IntVar()
Spinbox(from_=0, to=100, textvariable=age_var).pack()

Label(text='Sports').pack()
swimming_var = IntVar()
gym_var = IntVar()
aerobics_var = IntVar()
badminton_var = IntVar()
squash_var = IntVar()
Checkbutton(text='Swimming', variable=swimming_var).pack()
Checkbutton(text='Gym', variable=gym_var).pack()
Checkbutton(text='Aerobics', variable=aerobics_var).pack()
Checkbutton(text='Badminton', variable=badminton_var).pack()
Checkbutton(text='Squash', variable=squash_var).pack()

Button(text='SUBMIT', command=submit_click).pack()
Button(text='SEARCH', command=search_click).pack()

win.mainloop()