from tkinter import *
import pickle

try: 
    glossary_dict = pickle.load( open( "tkinter_w_dictionary_savefile.p", "rb" ) )
except:
    glossary_dict = {"motherboard":"Connects all different parts of the computer together",
    "hdds and ssds" : "Secondary storage unit. All programs are installed here, all data is saved here",
    "psu" : "Distributes the correct amount of power to other parts of the computer (drop-down transformer)**}",
    "gpu" : "Provides processing for games, videos, movie editing etc.",
    "optical disc drive" : "Used for reading from/writing to CDs, DVDs and sometimes Bluray."}
    pickle.dump(glossary_dict, open( "tkinter_w_dictionary_savefile.p", "wb" ) )

addNewDef_text = "To add new term, enter the term name and press the 'ADD NEW' button"

button_pass = False
key_valiue_txt = "errpr"

def searchClick(): #defining searchClick function, searches for term in glossary_dict, w/ error handling
    temp_txt = f"Defintion of '{entry_one.get().upper()}' Not Found In Glossary"
    try:
        temp_txt = f"Defintion of {entry_one.get().upper()} : {glossary_dict[entry_one.get().lower()]}"
        output_text.delete(0.0, END)
        output_text.insert(END, temp_txt)
    except:
        output_text.delete(0.0, END)
        output_text.insert(END, temp_txt)

def clearClick(): #defining clearClick function, clears the GUI, displays defintion of terms in glossary
    def_txt = f"Glossary Contains the Terms : {list(glossary_dict.keys())}\n\n{addNewDef_text}"
    entry_one.delete(0, END)
    output_text.delete(0.0, END)
    output_text.insert(END, def_txt)

def addNewClick(): #defining addNewClick function, adds new term to glossary
    global key_value_txt
    global button_pass
    if entry_one.get == "": return
    if button_pass == True:
        glossary_dict[key_value_txt.lower()] = entry_one.get()
        button_pass = False
        entry_one.delete(0, END)
        output_text.delete(0.0, END)
        output_text.insert(END, "Defintion stored")
        pickle.dump(glossary_dict, open( "tkinter_w_dictionary_savefile.p", "wb" ) )
        return
    key_value_txt = f"{entry_one.get().lower()}"
    def_txt = f"Enter Defintion of {key_value_txt}. Click 'ADD NEW' once you are ready"

    entry_one.delete(0, END)
    output_text.delete(0.0, END)
    output_text.insert(END, def_txt)
    button_pass = True



window = Tk() 
window.title("Glossary Search, working w/ dictionaries")

label_one = Label(window, text="Enter Something : ")
label_one.grid(row=0, column=0, sticky=W)

entry_one = Entry(window, width=20, bg='light green')
entry_one.grid(row=1,column=0,sticky=E)

button_one = Button(window, text="SEARCH", width=5, command=searchClick)
button_one.grid(row=2, column=0, sticky=W)

button_one = Button(window, text="CLEAR", width=5, command=clearClick)
button_one.grid(row=2, column=1, sticky=W)

button_one = Button(window, text="ADD NEW", width=5, command=addNewClick)
button_one.grid(row=2, column=2, sticky=W)

output_text = Text(window, height=30, width=40, wrap=WORD, background="black")
output_text.grid(row=3, column=0, columnspan=4, sticky=W)

clearClick() #calling clearClick function, displays defintion of terms in glossary

window.mainloop()  