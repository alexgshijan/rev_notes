# Only works in Python 3 (Created in 3.4.2)
# tkinter comes as part of the standard install - messagebox has to be imported explicitly

#. . . means missing or incomplete code

from tkinter import *
from tkinter import messagebox

def saveClient() :
    ClientIDSave = ClientIDVar.get()
    ClientIDSave = ClientIDSave.ljust(50)
    
    TitleSave=TitleVar.get()
    TitleSave = TitleSave.ljust(50)
    
    FirstnameSave = FirstnameVar.get()
    FirstnameSave = FirstnameSave.ljust(50)
    
    SurnameSave = SurnameVar.get()
    SurnameSave = SurnameSave.ljust(50)
    
    AddressSave = AddressVar.get()
    AddressSave = AddressSave.ljust(50)
    

    
    fileObject = open("clients.txt","a")
    fileObject.write(ClientIDSave + TitleSave + FirstnameSave + SurnameSave + AddressSave + "\n")
    fileObject.close()
    
    return

def countClient() :
    ClientCount=0
    CountNeeded=0

    ClientIDSave = ClientIDVar.get()
    
    TitleSave=TitleVar.get()
    
    FirstnameSave = FirstnameVar.get()
    
    SurnameSave = SurnameVar.get()
    
    AddressSave = AddressVar.get()
    
    
    
    if not ClientIDSave == "" :
        CountNeeded +=1
    if not TitleSave == "" :
        CountNeeded +=1
    if not FirstnameSave == "" :
        CountNeeded +=1
    if not SurnameSave == "" :
        CountNeeded +=1
    if not AddressSave == "" :
        CountNeeded +=1
    

    if CountNeeded == 0 :
        messagebox.showerror("Error","Please enter something to count!")
        return
    try:
        fileObject=open("savefile.txt","r")
        print()
        
    except IOError:
        messagebox.showerror("Error","No file to read")

    else:
        while True:
            CountGot=0
            recordVar=fileObject.readline()
            if recordVar=="":
                fileObject.close()
                break
         
            if ClientIDSave in recordVar[0:50] and not ClientIDSave=="" :
                CountGot +=1
            if TitleSave in recordVar[50:100] and not TitleSave=="" :
                CountGot +=1
            if FirstnameSave in recordVar[100:150] and not FirstnameSave=="":
                CountGot +=1
            if SurnameSave in recordVar[150:200] and not SurnameSave =="":
                CountGot +=1
            if AddressSave in recordVar[200:250] and not AddressSave=="":
                CountGot +=1
          
            if CountGot == CountNeeded:
                ClientCount += 1
                
        messagebox.showinfo("Found: ",str(ClientCount))    
    
    return

def searchClient() :
    ClientCount=0
    CountNeeded=0

    ClientIDSave = ClientIDVar.get()
    
    TitleSave=TitleVar.get()
    
    FirstnameSave = FirstnameVar.get()
    
    SurnameSave = SurnameVar.get()
    
    AddressSave = AddressVar.get()
    
    
    
    if not ClientIDSave == "" :
        CountNeeded +=1
    if not TitleSave == "" :
        CountNeeded +=1
    if not FirstnameSave == "" :
        CountNeeded +=1
    if not SurnameSave == "" :
        CountNeeded +=1
    if not AddressSave == "" :
        CountNeeded +=1
    

    if CountNeeded == 0 :
        messagebox.showerror("Error","Please enter something to count!")
        return
    try:
        fileObject=open("savefile.txt","r")
        print()
        
    except IOError:
        messagebox.showerror("Error","No file to read")

    else:
        while True:
            CountGot=0
            recordVar=fileObject.readline()
            if recordVar=="":
                fileObject.close()
                break
         
            if ClientIDSave in recordVar[0:50] and not ClientIDSave=="" :
                CountGot +=1
            if TitleSave in recordVar[50:100] and not TitleSave=="" :
                CountGot +=1
            if FirstnameSave in recordVar[100:150] and not FirstnameSave=="":
                CountGot +=1
            if SurnameSave in recordVar[150:200] and not SurnameSave =="":
                CountGot +=1
            if AddressSave in recordVar[200:250] and not AddressSave=="":
                CountGot +=1
          
            if CountGot == CountNeeded:
                ClientCount += 1
                outString = recordVar[0:50] + "\n" + recordVar[50:100]+"\n" + recordVar[100:150]
                messagebox.showinfo ("Found: ", outString)
                
        messagebox.showinfo("Found: ",str(ClientCount))    
    
    return



def makeWindow():


    
    global ClientIDVar, TitleVar, FirstnameVar, SurnameVar, AddressVar

    #Create a window/form
    win = Tk()
    
    frame1=Frame(win)
    frame1.pack()

    Label(frame1, text="Clients", font=("Helvetica 12 bold")).grid(row=0, column=0)
    
    Label(frame1, text="ClientID").grid(row=1, column=0, sticky=W)
    ClientIDVar=StringVar()
    ClientID= Entry(frame1, textvariable=ClientIDVar)
    ClientID.grid(row=1,column=1,sticky=W)

    Label(frame1, text="Title").grid(row=2, column=0, sticky=W)
    TitleVar=StringVar()
    Title= Entry(frame1, textvariable=TitleVar)
    Title.grid(row=2,column=1,sticky=W)

    Label(frame1, text="Firstname").grid(row=3, column=0, sticky=W)
    FirstnameVar=StringVar()
    Firstname= Entry(frame1, textvariable=FirstnameVar)
    Firstname.grid(row=3,column=1,sticky=W)
    
    Label(frame1, text="Surname").grid(row=4, column=0, sticky=W)
    SurnameVar=StringVar()
    Surname= Entry(frame1, textvariable=SurnameVar)
    Surname.grid(row=4,column=1,sticky=W)
    
    Label(frame1, text="Address").grid(row=5, column=0, sticky=W)
    AddressVar=StringVar()
    Address= Entry(frame1, textvariable=AddressVar)
    Address.grid(row=5,column=1,sticky=W)
    
   
  

    frame2 = Frame(win)
    frame2.pack()
    b1= Button(frame2, text=" Save ", command=saveClient)
    b2= Button(frame2, text=" Count ", command=countClient)
    b1.pack(side=LEFT); b2.pack(side=LEFT)
    
    return win


#this is the main program!
win = makeWindow()
win.mainloop()
