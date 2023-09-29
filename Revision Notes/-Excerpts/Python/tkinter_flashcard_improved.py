from tkinter import *


flash_dict = {"Irrational Number" : "asdsadsadas", 
"Rational Number" : "**Not irrational**",
"test" : "**test**"}

#This is the function that will be called when the button is clicked, it will take the --
# name of the button clicked and call aand pass it to the flash_dict dictionary, which --
# will print the definition to the output_text text box
def button_x(button_names):
    text = flash_dict[button_names]
    output_text.delete(0.0, END)
    output_text.insert(END, text)


window = Tk()
window.title('Flashcard test')

button_one = Button(window, text="Irrational Number", width=10, command=lambda:button_x("Irrational Number"))
button_one.grid(row=1, column=0, sticky=W)

button_two = Button(window, text="Rational Number", width=10, command=lambda:button_x("Rational Number"))
button_two.grid(row=2, column=0, sticky=W)

button_three = Button(window, text="test", width=10, command=lambda:button_x("test"))
button_three.grid(row=3, column=0, sticky=W)

output_text = Text(window, height=30, width=100, wrap=WORD, background="black")
output_text.grid(row=1, column=1, sticky=W)

window.mainloop()  