from tkinter import *
from tkinter import messagebox

# This function is called when the user clicks on the button. This functions --
# gives the program a chance to read in the entered values
def submit_click():
    if (name_entry.get() == '') or ((reading.get() == 0) and (sports.get() == 0) and (chess.get() == 0) and (stamp_collecting.get() == 0) and (walking.get() == 0)):
        messagebox.showerror('Error', 'Please Enter Name and Atleast One Hobby')
        return

    hobbies_text = ""
    if reading.get() == 1: hobbies_text += ("Reading, ")
    if sports.get() == 1: hobbies_text += ("Sports, ")
    if chess.get() == 1: hobbies_text += ("Chess, ")
    if stamp_collecting.get() == 1: hobbies_text += ("Stamp Collecting, ")
    if walking.get() == 1: hobbies_text += ("Walking, ")

    if gender.get() == 0: gender_txt = "Male"
    else:gender_txt = "Female"

    output_text_thing = f"Questionaire Values\nName : {name_entry.get()}\nAge : {age.get()}\nGender : {gender_txt}\nHobbies : {hobbies_text[:-2]}"
    output_text.delete(END)
    output_text.insert(END, output_text_thing)


def save_click():
    user_data = []
    try:
        f = open("tkinter_4_activity_2.txt", "r")
        lines = f.readlines()
        for x in lines:
            user_data.append(x.split(split_var))
        f.close()

    except:
        pass
    
    name_temp = str(name_entry.get()); walking_temp = str(walking.get()); age_temp = str(age.get()); 
    sports_temp = str(sports.get()); reading_temp = str(reading.get()); chess_temp = str(chess.get()); 
    stamp_collecting_temp = str(stamp_collecting.get()); gender_temp = str(gender.get())

    temp_save_file = [name_temp, age_temp, walking_temp, sports_temp, reading_temp, chess_temp, stamp_collecting_temp, gender_temp]
    user_data.append(temp_save_file)
    
    temp_save_file = []
    for i in user_data:
        temp_save_file_var = ''
        for x in i:
            temp_save_file_var += (x + split_var)
        temp_save_file_var = temp_save_file_var[:-(len(split_var))]
        temp_save_file.append(temp_save_file_var)

    f = open("tkinter_4_activity_2.txt", "w")
    f.writelines(temp_save_file)
    f.close()


def load_click():
    user_data = []
    try:
        f = open("tkinter_4_activity_2.txt", "r")
        lines = f.readlines()
        for x in lines:
            user_data.append(x.split(split_var))
        f.close()

        name_entry.delete(0, END)
        name_entry.insert(0, str(user_data[round_val][0]))
        walking.set(int(user_data[round_val][2]))
        age.set(int(user_data[round_val][1]))
        reading.set(user_data[round_val][4])
        sports.set(int(user_data[round_val][3]))
        chess.set(int(user_data[round_val][5]))
        stamp_collecting.set(int(user_data[round_val][6]))
        gender.set(int(user_data[round_val][7]))
        output_text.delete(0.0, END)
        output_text.insert(END, "Saved files have been loaded in.")

    except:
        output_text.delete(0.0, END)
        output_text.insert(END, "No saved files found.")


def dict_cycle():
    global round_val
    
    try:
        load_click()
    except:
        output_text.delete(0.0, END)
        output_text.insert(END, "No saved files found.")

    round_val += 1
    if round_val == len(user_data):
        round_val = 0


def recall_click():
    user_data = []
    try:
        f = open("tkinter_5", "r")
        lines = f.readlines()
        for x in lines:
            user_data.append(x.split(split_var))
        f.close()

    except:
        messagebox.showerror('Error', 'save file not found')
        return


    if (name_entry.get() == '') or ((reading.get() == 0) and (sports.get() == 0) and (chess.get() == 0) and (stamp_collecting.get() == 0) and (walking.get() == 0)):
        messagebox.showerror('Error', 'Please Enter Name and Atleast One Hobby')
        return

    name_temp = str(name_entry.get()); walking_temp = str(walking.get()); age_temp = str(age.get()); 
    sports_temp = str(sports.get()); reading_temp = str(reading.get()); chess_temp = str(chess.get()); 
    stamp_collecting_temp = str(stamp_collecting.get()); gender_temp = str(gender.get())

    temp_save_file = [name_temp, age_temp, walking_temp, sports_temp, reading_temp, chess_temp, stamp_collecting_temp, gender_temp]

    load_click()    
    accum = 0
    for i in user_data:
        if i == temp_save_file:
            accum += 1
    output_text.delete(0.0, END)
    output_text.insert(END, f"{accum} instances recalled")


user_data = []
round_val = 0
split_var = '  |  '

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
recall = IntVar()

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
Button(wd, text = 'RECALL', command = recall_click).pack()

# This runs the GUI and acts as a garbage collector for all interactions
wd.mainloop()
