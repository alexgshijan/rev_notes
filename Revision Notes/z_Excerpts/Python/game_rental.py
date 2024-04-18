from tkinter import *
from tkinter import messagebox

def WinTrigger(menuOption, fPass = True):
    try:global win;win.destroy()
    except:pass

    temp_win = Tk()
    if menuOption == 'customer':
        temp_win.title("Rental Service - Customer Side")
        Buttons

    elif menuOption == 'manager':
        temp_win.title("Rental Service - Manager Side")

    elif menuOption == 'managerLogin':
        if fPass != True:
            if (fPass[0].get() == 'username') and (fPass[1].get() == 'password'):
                temp_win = WinTrigger('manager')
            else:
                Label(text="ERROR : Incorrect Credentials").pack()
        else:
            temp_win.title("Rental Service - Manager Side - Login")
            username = StringVar()
            password = StringVar()
            Label(text="Username :").pack()
            Entry(textvariable=username).pack()
            Label(text="Password :").pack()
            Entry(textvariable=password).pack()
            Button(text='SUBMIT', command=lambda:WinTrigger('managerLogin', [username,password])).pack()

    elif menuOption == 'main':
        temp_win.title("Rental Service")
        Button(text = 'Customer Side System', width = 15, height = 1, command = lambda:WinTrigger('customer')).pack()
        Button(text = 'Manager Side System', width = 15, height = 1, command = lambda:WinTrigger('managerLogin')).pack()

    return temp_win

def rerun(window):
    try:win.destroy()
    except:pass
    window.mainloop()

rerun(WinTrigger('main'))


