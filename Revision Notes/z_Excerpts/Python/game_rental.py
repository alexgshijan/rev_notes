from tkinter import *

def WinTrigger(menuOption):
    try:global win;win.destroy()
    except:pass

    temp_win = Tk()
    if menuOption == 'customer':
        temp_win.title("Rental Service - Customer Side")
        Buttons

    if menuOption == 'manager':
        temp_win.title("Rental Service - Manager Side")

    if menuOption == 'managerLogin':
        temp_win.title("Rental Service - Manager Side - Login")
        username = StringVar()
        password = StringVar()
        Label(text="Username :").pack()
        Entry(textvariable=username).pack()
        Label(text="Password :").pack()
        Entry(textvariable=password).pack()
        Button(text='SUBMIT', command=lambda:login(username,password))

    if menuOption == 'main':
        temp_win.title("Rental Servicee")
        Button(text = 'Customer Side System', width = 15, height = 1, command = lambda:WinTrigger('customer')).grid(row = 0, column = 0)
        Button(text = 'Manager Side System', width = 15, height = 1, command = lambda:WinTrigger('managerLogin')).grid(row = 0, column = 1)
    return temp_win

def login(username, password):
    if 
    pass

win = WinTrigger('main')
win.mainloop()


