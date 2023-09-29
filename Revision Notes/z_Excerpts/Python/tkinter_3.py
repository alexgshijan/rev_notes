from tkinter import *

def button_click():

    output_text_thing = f"{v.get()}\n{check_conv(check_one.get())}\n{check_conv(check_two.get())}\n"
    output_text.delete(0.0, END)
    output_text.insert(END, output_text_thing)

def check_conv(var):
    if var == 0:
        return 'False'
    if var == 1:
        return 'True'
    else: (print("Crit Error w/ check_conv"))

wd = Tk()
wd.title('Tkinter w/ more windows')

v = IntVar()
spin = Spinbox(wd, textvariable = v, from_=0, to=100, width=5)
spin.pack()

check_one = IntVar()
checkbox_one = Checkbutton(wd, text = 'Check One', variable = check_one)
checkbox_one.pack()

check_two = IntVar()
checkbox_two = Checkbutton(wd, text = 'Check Two', variable = check_two)
checkbox_two.pack()



output_text = Text(wd, height=30, width=50, wrap=WORD)
output_text.pack()

submit_button = Button(wd, text = 'SUBMIT', command = button_click)
submit_button.pack()

wd.mainloop()