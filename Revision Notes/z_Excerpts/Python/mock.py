from tkinter import * #//
from tkinter import messagebox

def count():
    return

def submit():
    temp_save_var = f'{str(name_var.get())} + split_var + {str(gender.get())}'
    try:
        file_ = open(filename, 'a')
    except:
        file_ = open(filename, 'w')
    
    file_.write(temp_save_var + '\n')
    file_.close()
    return



win = Tk()
split_var = "  |  "
gender = IntVar()
age = IntVar()
filename = 'mock.txt'

Label(text='Alex and Co Questionaire', font=('ariel', 18)).pack()

Label(text='Enter Name').pack()
name_var = Entry()
name_var.pack()

Label(text='Select Gender').pack()
Radiobutton(text='Male', variable=gender, value=0).pack()
Radiobutton(text='Female', variable=gender, value=1).pack()

Label(text='Select Age').pack()
Spinbox(textvariable=age, from_ = 0, to = 101, width=10).pack()

Button(text='SUBMIT', command=submit).pack()
Button(text='COUNT', command=count).pack()

win.mainloop()