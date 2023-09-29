from tkinter import *

flash_dict = {"Irrational Number" : "**A number which cannot be expressed as a fraction, $\frac{a}{b}$ where both $a$ and $b$ are integers**, *see [[Turning Decimals into fractions]]*", "Rational Number" : "**Not irrational**"}


def button_one_click():
    text = flash_dict["Irrational Number"]
    output_text.delete(0.0, END)
    output_text.insert(END, text)

def button_two_click():
    text = flash_dict["Rational Number"]
    output_text.delete(0.0, END)
    output_text.insert(END, text)

window = Tk()
window.title('Flashcard test')

button_one = Button(window, text="Irrational Number", width=10, command=button_one_click)
button_one.grid(row=1, column=0, sticky=W)

button_two = Button(window, text="Rational Number", width=10, command=button_two_click)
button_two.grid(row=2, column=0, sticky=W)

output_text = Text(window, height=30, width=100, wrap=WORD, background="black")
output_text.grid(row=1, column=1, sticky=W)

window.mainloop()  