# Imports tkinter as a native package, this makes programming using it way less --
# tedious but its important to note that had we not included the 'import *' all --
# tkinter based commands would have required as to include a 'package.'
from tkinter import *

# This will store the text inputted into the input when the button is clicked --
# within the variable 'text' and print it to console, it also prints the text --
# onto the text box within the GUI

def button_click():
    print(entry_one.get())
    output_text.delete(0.0, END)
    output_text.insert(END, f"You've just typed in : {entry_one.get()}")


window = Tk()
window.title('GUI test') # Sets the GUI's title

# This creaates a label object called label_one, labels are a text widget, column --
# and row act as coordinates for where the widget is placed
label_one = Label(window, text="Enter Something : ")
label_one.grid(row=0, column=0, sticky=W)

# This creates a Entry object called entry_one, Entry acts as an input method
entry_one = Entry(window, width=20, bg='light green')
entry_one.grid(row=1,column=0,sticky=E)

# This creates a button widget
button_one = Button(window, text="SUBMIT", width=5, command=button_click)
button_one.grid(row=2, column=0, sticky=W)

# Creates a text box widget, the text displayed can be changed during the program --
# is runnning
output_text = Text(window, height=30, width=10, wrap=WORD, background="yellow")
output_text.grid(row=3, column=0, columnspan=2, sticky=W)

# A garbage collector for all interactions to the GUI, this also runs the main --
# running loop pf GUI
window.mainloop()  
