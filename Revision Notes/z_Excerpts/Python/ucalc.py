from tkinter import *

def text_bump(input_value):
    global output_string
    global screen
    output_string = str(input_value)
    screen.delete(END)
    screen.insert(END, output_string)
    
def equal_out():
    global output_string
    global screen
    equal_temp = eval(str(screen.get('0.0', END)))
    screen.delete('0.0', END)
    screen.insert(END, equal_temp)
    output_string = str(equal_temp)


def MS():
    calc_write = open('calculatorfile.txt', 'w')
    calc_write.write(str(eval(screen.get('0.0', END))))
    output_string = str(screen.get('0.0', END))
    calc_write.close()
    

def MR():
    try:
        calc_write = open('calculatorfile.txt', 'r')
        reading_value = calc_write.read()
        calc_write.close()
        screen.delete('0.0',END)
        screen.insert(END, reading_value)
        output_string = str(reading_value)   
        
    except:
        pass

def clear():
    screen.delete('0.0', END)
    output_string = ''

def undo():
    global output_string
    if output_string == '':
        return
    else:
        output_string = output_string[:-1]
        screen.delete('0.0', END)
        screen.insert(END, output_string)

win = Tk()
win.title  = 'our (better) calculator'
output_string = ''

#functions
Button(text = 'MS', width = 5, height = 1, command = MS).grid(row = 1, column = 0)
Button(text = 'MR', width = 5, height = 1, command = MR).grid(row = 1, column = 1)
Button(text = 'Clear', width = 5, height = 1, command = clear).grid(row = 1, column = 3)
Button(text = 'Undo', width = 5, height = 1, command = undo).grid(row = 1, column = 2)

#numbers
Button(text = '1', width = 5, height = 1, command = lambda:text_bump('1')).grid(row = 2,column = 0)
Button(text = '2', width = 5, height = 1, command = lambda:text_bump('2')).grid(row = 2,column = 1)
Button(text = '3', width = 5, height = 1, command = lambda:text_bump('3')).grid(row = 2,column = 2)
Button(text = '4', width = 5, height = 1, command = lambda:text_bump('4')).grid(row = 3,column = 0)
Button(text = '5', width = 5, height = 1, command = lambda:text_bump('5')).grid(row = 3,column = 1)
Button(text = '6', width = 5, height = 1, command = lambda:text_bump('6')).grid(row = 3,column = 2)
Button(text = '7', width = 5, height = 1, command = lambda:text_bump('7')).grid(row = 4,column = 0)
Button(text = '8', width = 5, height = 1, command = lambda:text_bump('8')).grid(row = 4,column = 1)
Button(text = '9', width = 5, height = 1, command = lambda:text_bump('9')).grid(row = 4,column = 2)
Button(text = '0', width = 5, height = 1, command = lambda:text_bump('0')).grid(row = 5,column = 1)

#operators
Button(text = '+', width = 5, height = 1, command = lambda:text_bump('+')).grid(row = 2, column = 3)
Button(text = '-', width = 5, height = 1, command = lambda:text_bump('-')).grid(row = 3, column = 3)
Button(text = '*', width = 5, height = 1, command = lambda:text_bump('*')).grid(row = 4, column = 3)
Button(text = '/', width = 5, height = 1, command = lambda:text_bump('/')).grid(row = 5, column = 3)
Button(text = '=', width = 5, height = 1, command = equal_out).grid(row = 5, column = 2)
Button(text = '.', width = 5, height = 1, command = lambda:text_bump('.')).grid(row = 5, column = 0)


screen = Text(width=15, height= 5)
screen.grid(row = 0, column = 0, columnspan = 4, sticky = 'EW')

win.mainloop()
