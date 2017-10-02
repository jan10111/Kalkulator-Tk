import Tkinter
import tkMessageBox

def kalkulator():
    number_x = int(numberImput.get())
    number_y = int(numberImputt.get())
    op = str(operation.get())
    output = int()

    if op == "+":
        output += number_x + number_y
    elif op == "-":
        output += number_x - number_y
    elif op == "*":
        output += number_x * number_y
    elif op == "/":
        output += number_x / number_y

    tkMessageBox.showinfo(window, output)
    """s tkMessageBox znam izpisat output, ne znam pa ga v originalnem windowu...mas kaksen nasvet?"""



window = Tkinter.Tk()

description = Tkinter.Label(window, text="This is LaMe calculator.\n"
                                         "Please enter a number, select operation\n"
                                         "and then enter another number.")
description.pack()

numberImput = Tkinter.Entry(window)
numberImput.pack()

operation = Tkinter.Entry(window)
operation.pack()

numberImputt = Tkinter.Entry(window)
numberImputt.pack()

submit = Tkinter.Button(window, text="calculate", command=kalkulator)
submit.pack()

outputText = Tkinter.Text(window)
outputText.pack()

window.mainloop()