# Imports tkinter as a native package, this makes programming using it way less --
# tedious but its important to note that had we not included the 'import *' all --
# tkinter based commands would have required as to include a 'package.'
from tkinter import *

# This function is called when the user clicks on the button. This functions --
# gives the program a chance to read in the entered values
def submit_click():
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


def load_click():
    try:
        f = open("tkinter_3_activity_2.txt", "r")
        user_data = (eval(f.read()))
        f.close()

        name_entry.delete(0, END)
        name_entry.insert(0, str(user_data[round_val]['name']))
        walking.set(int(user_data[round_val]['walking']))
        age.set(int(user_data[round_val]['age']))
        reading.set(user_data[round_val]['reading'])
        sports.set(int(user_data[round_val]['sports']))
        chess.set(int(user_data[round_val]['chess']))
        stamp_collecting.set(int(user_data[round_val]['stamp_collecting']))
        gender.set(int(user_data[round_val]['gender']))
        output_text.delete(0.0, END)
        output_text.insert(END, "Saved files have been loaded in.")
    except:
        output_text.delete(0.0, END)
        output_text.insert(END, "No saved files found.")


def save_click():
    name_temp = str(name_entry.get()); walking_temp = str(walking.get()); age_temp = str(age.get()); 
    sports_temp = str(sports.get()); reading_temp = str(reading.get()); chess_temp = str(chess.get()); 
    stamp_collecting_temp = str(stamp_collecting.get()); gender_temp = str(gender.get()); country_temp = str(country.get())

    temp_save_file = {'name':name_temp, 'walking':walking_temp, 'age':age_temp, 
    'sports':sports_temp, 'reading':reading_temp, 'chess':chess_temp, 
    'stamp_collecting':stamp_collecting_temp, 'gender':gender_temp}
    print(str(user_data))
    user_data.append(temp_save_file)
    print(str(user_data))
    
    f = open("tkinter_3_activity_2.txt", "w")
    f.write(str(user_data))
    f.close()


def dict_cycle():
    global round_val
    
    try:
        f = open("tkinter_3_activity_2.txt", "r")
        user_data = (eval(f.read()))
        f.close()
    except:
        output_text.delete(0.0, END)
        output_text.insert(END, "No saved files found.")

    round_val += 1
    if round_val == len(user_data):
        round_val = 0
    else:
        pass
    load_click()

user_data = []
round_val = 0

wd = Tk()
wd.title("Random Questionaire") # Sets the GUI's title

# This creates variables that the tkinter package can use.
walking = IntVar()
age = IntVar()
reading = IntVar()
sports = IntVar()
chess = IntVar()
stamp_collecting = IntVar()
gender = IntVar()

#This creates a label object, which is essentially a text widget
Label(text="Questionaire").pack() 

Label(text="Enter Your Name : ").pack()

# This cretes an entry object, which we can reference later and get the value
name_entry = Entry()
name_entry.pack()

Label(text="Select Your Age : ").pack()
# Spinboxes are essentially a slider widget
Spinbox(wd, textvariable = age, from_=0, to=100, width=5).pack()

Label(text="Select Your Gender : ").pack()
# Radiobuttons are essentially a single choice widget
Radiobutton(text = 'Male', variable = gender, value = 0).pack()
Radiobutton(text = 'Female', variable = gender, value = 1).pack()

Label(text="Select Your Hobbies : ").pack()
# Checkbuttons are essentially a multiple choice widgets
Checkbutton(text = 'Stamp Collecting', variable = stamp_collecting).pack()
Checkbutton(text = 'Chess', variable = chess).pack()
Checkbutton(text = 'Reading', variable = reading).pack()
Checkbutton(text = 'Sports', variable = sports).pack()
Checkbutton(text = 'Walking', variable = walking).pack()

# Summary Box, this is a text widget that can be updated while the code is running
output_text = Text()
output_text.pack()

# This creates a button object, when clicked it activates a function --
# We could also use lamda to add more functionality to the button click
Button(wd, text = 'SUBMIT', command = submit_click).pack()
Button(wd, text = 'SAVE', command = save_click).pack()
Button(wd, text = 'LOAD', command = load_click).pack()
Button(wd, text = 'NEXT', command = dict_cycle).pack()

# This runs the GUI and acts as a garbage collector for all interactions
wd.mainloop()

