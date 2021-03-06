import tkinter as tk
from tkinter import *
import math

root = tk.Tk()
root.title('Py Calculator')
root.resizable(width=False, height=False)

#Variáveis e Listas
inputs = " "
ops = ['×', '÷', '.', '*', '/', ' ', '**']

#Funções

def helpindex():
    root3 = tk.Tk()
    root3.title('Py Calculator')
    root3.resizable(width=False, height=False)

    text1 = Text(root3)
    text1.insert(INSERT, 'To be')
    text1.insert(END, " added...")
    text1.pack()

    root3.mainloop()

def insert(num):
    global inputs
    if inputs[-1] in ops and num in ops:
        pass
    else:
        visorinput['text'] += num
        if num == '×':
            inputs += '*'
        elif num == '÷':
            inputs += '/'
        else:
            inputs += num

def limpar():
    global inputs
    inputs = " "
    visorinput['text'] = ""
    visoroutput['text'] = ""

def delete():
    global inputs
    if inputs[-1] == " ":
        pass
    else:
        inputs = inputs[:-1]
        visorinput['text'] = visorinput['text'][:-1]

def resultado():
    visoroutput['text'] = ""
    global inputs
    visoroutput['text'] = eval(inputs)

def menu():
    root2 = tk.Tk()
    root2.title('More')
    root2.resizable(width=False, height=False)

    but0 = Button(root2, text='√', bd='0', font='Calibri 10 bold', height='3', width='16', command=lambda: insert('math.sqrt('))
    but0.grid(row=0, column=0)
    but0 = Button(root2, text='xⁿ', bd='0', font='Calibri 10 bold', height='3', width='16', command=lambda: insert('**'))
    but0.grid(row=0, column=1)

    root2.mainloop()

#Menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="More", command=menu)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=helpindex)
helpmenu.add_command(label="About...", command=helpindex)
menubar.add_cascade(label="Help", menu=helpmenu)

#Visor
visorinput = Label(root, text = '', bd = '0', bg = '#DADADA', font = 'Calibri 10 bold', height = '3', width = '36')
visorinput.grid(row = 0, column = 0, columnspan = 4,  sticky = 'e' + 'w')

visoroutput = Label(root, text = '', bd = '0', bg = '#DADADA', font = 'Calibri 12 bold', height = '3', width = '1')
visoroutput.grid(row = 1, column = 0, columnspan = 4,  sticky = 'e' + 'w')

#Botões de Operações
butresu = Button(root, text = '=', bd = '0', font = 'Calibri 10 bold', height = '3', width = '8', command = resultado)
butresu.grid(row = 6, column = 2)

butsoma = Button(root, text = '+', bd = '0', font = 'Calibri 10 bold', height = '3', width = '8', command = lambda:insert('+'))
butsoma.grid(row = 3, column = 3)

butsubt = Button(root, text = '-', bd = '0', font = 'Calibri 10 bold', height = '3', width = '8', command = lambda:insert('-'))
butsubt.grid(row = 4, column = 3)

butmult = Button(root, text = '×', bd = '0', font = 'Calibri 10 bold', height = '3', width = '8', command = lambda:insert('×'))
butmult.grid(row = 5, column = 3)

butdivs = Button(root, text = '÷', bd = '0', font = 'Calibri 10 bold', height = '3', width = '8', command = lambda:insert('÷'))
butdivs.grid(row = 6, column = 3)


#Botões de Número
but9 = Button(root, text = '9', bd = '0', font = 'Calibri 10 bold', height = '3', width = '8', command = lambda:insert('9'))
but9.grid(row = 3, column = 2)

but8 = Button(root, text = '8', bd = '0', font = 'Calibri 10 bold', height = '3', width = '8', command = lambda:insert('8'))
but8.grid(row = 3, column = 1)

but7 = Button(root, text = '7', bd = '0', font = 'Calibri 10 bold', height = '3', width = '8', command = lambda:insert('7'))
but7.grid(row = 3, column = 0)


but6 = Button(root, text = '6', bd = '0', font = 'Calibri 10 bold', height = '3', width = '8', command = lambda:insert('6'))
but6.grid(row = 4, column = 2)

but5 = Button(root, text = '5', bd = '0', font = 'Calibri 10 bold', height = '3', width = '8', command = lambda:insert('5'))
but5.grid(row = 4, column = 1)

but4 = Button(root, text = '4', bd = '0', font = 'Calibri 10 bold', height = '3', width = '8', command = lambda:insert('4'))
but4.grid(row = 4, column = 0)


but3 = Button(root, text = '3', bd = '0', font = 'Calibri 10 bold', height = '3', width = '8', command = lambda:insert('3'))
but3.grid(row = 5, column = 2)

but2 = Button(root, text = '2', bd = '0', font = 'Calibri 10 bold', height = '3', width = '8', command = lambda:insert('2'))
but2.grid(row = 5, column = 1)

but1 = Button(root, text = '1', bd = '0', font = 'Calibri 10 bold', height = '3', width = '8', command = lambda:insert('1'))
but1.grid(row = 5, column = 0)


but0 = Button(root, text = '0', bd = '0', font = 'Calibri 10 bold', height = '3', width = '8', command = lambda:insert('0'))
but0.grid(row = 6, column = 1)

#Outros Botões
butdot = Button(root, text = '.', bd = '0', font = 'Calibri 10 bold', height = '3', width = '8', command = lambda:insert('.'))
butdot.grid(row = 6, column = 0)

but9 = Button(root, text = ')', bd = '0', font = 'Calibri 10 bold', height = '3', width = '8', command = lambda:insert(')'))
but9.grid(row = 2, column = 3)

but9 = Button(root, text = '(', bd = '0', font = 'Calibri 10 bold', height = '3', width = '8', command = lambda:insert('('))
but9.grid(row = 2, column = 0)

butdel = Button(root, text = 'DEL',  bd = '0', font = 'Calibri 10 bold', height = '3', width = '8', command = delete)
butdel.grid(row = 2, column = 2, sticky = 'e' + 'w')

butlimp = Button(root, text = 'CLEAR', bd = '0', font = 'Calibri 10 bold', height = '3', width = '8', command = limpar)
butlimp.grid(row = 2, column = 1, sticky = 'e' + 'w')

root.config(menu=menubar)
root.mainloop()
