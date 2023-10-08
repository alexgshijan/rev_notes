from tkinter import *

# Function to perform the dictionary search
def search_dictionary():
    key = entry.get()  # Get the user input from the Entry widget
    result = my_dictionary.get(key, "Key not found")
    output_text.delete(1.0, END)  # Clear previous output
    output_text.insert(END, result)

#Function to add new values to dictionary
def add_dictionary():
	inp_value = entry.get() #Get user inp
	key, value = inp_value.split(":")#Split into two variables, value and key by use of colon

	key = key.strip() #remove whitespace
	value = value.strip()
	my_dictionary[key] = value#append to dictionary

	output_text.delete(0.0, END)#clear previous output
	output_text.insert(END, "NEW ENTRY ADDED")


# Dictionary
my_dictionary = {"a": "1", "b": "2", "c": "3"}

# Create the main window
window = Tk()
window.title("Dictionary Search")

# Label and Entry for user input
input_label = Label(window, text="Enter a key:")
input_label.pack()

entry = Entry(window)
entry.pack(fill = "both", expand = True)
#Button to trigger the search
search_button = Button(window, text="Search", command=search_dictionary)
search_button.pack(fill = "both", expand = True)

add_button = Button(window, text="ADD NEW (split by ':')", command=add_dictionary)
add_button.pack(fill = "both", expand = True)
# Output area using a Text widget
output_text = Text(window, background = "Light Blue", height=2, width=30)
output_text.pack(fill = "both", expand = True)

# Run the Tkinter main loop
window.mainloop()

