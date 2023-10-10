from tkinter import *


def button_click():
    hobbies_text = ""
    if reading.get() == 1: hobbies_text += ("Reading, ")
    if sports.get() == 1: hobbies_text += ("Sports, ")
    if chess.get() == 1: hobbies_text += ("Chess, ")
    if stamp_collecting.get() == 1: hobbies_text += ("Stamp Collecting, ")
    if walking.get() == 1: hobbies_text += ("Walking, ")

    if gender.get() == 0: gender_txt = "Male"
    else:gender_txt = "Female"

    output_text_thing = f"Questionaire Values\nName : {name_entry.get()}\nAge : {age.get()}\nGender : {gender_txt}\nHobbies : {hobbies_text[:-2]}"
    output_text.delete(0.0, END)
    output_text.insert(END, output_text_thing)


wd = Tk()
wd.title("Random Questionaire")

name = IntVar()
walking = IntVar()
age = IntVar()
reading = IntVar()
sports = IntVar()
chess = IntVar()
stamp_collecting = IntVar()
gender = IntVar()
country = IntVar()

Label(text="Questionaire").pack()

Label(text="Enter Your Name : ").pack()
name_entry = Entry()
name_entry.pack()

Label(text="Select Your Age : ").pack()
Spinbox(wd, textvariable = age, from_=0, to=100, width=5).pack()

Label(text="Select Your Gender : ").pack()
Radiobutton(text = 'Male', variable = gender, value = 0).pack()
Radiobutton(text = 'Female', variable = gender, value = 1).pack()

Label(text="Select Your Hobbies : ").pack()
Checkbutton(text = 'Stamp Collecting', variable = stamp_collecting).pack()
Checkbutton(text = 'Chess', variable = chess).pack()
Checkbutton(text = 'Reading', variable = reading).pack()
Checkbutton(text = 'Sports', variable = sports).pack()
Checkbutton(text = 'Walking', variable = walking).pack()

# Summary Box
output_text = Text()
output_text.pack()

Button(wd, text = 'SUBMIT', command = button_click).pack()

wd.mainloop()