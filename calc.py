from tkinter import *

root = Tk()

root.geometry('320x400')
root.resizable(width=False, height=False)
root['bg'] = 'black'

def delet():
    userInput.delete(len(userInput.get()) - 1, 'end')


def clear():
    userInput.delete(0, 'end')


def result():
    try:
        res = eval(userInput.get())
        userInput.delete(0, 'end')
        userInput.insert('end', res)
    except ZeroDivisionError:
        userInput.delete(0, 'end')
        userInput.insert('end', 'Неможна ділити на нуль')
    except NameError:
        userInput.delete(0, 'end')
        userInput.insert('end', 'Неможна вводити букви')
    except ValueError:
        pass


def main(item):
    if len(userInput.get()) > 22:
        userInput.config(font=('Arial', 14, 'bold'))
        if len(userInput.get()) > 27:
            userInput.config(font=('Arial', 12, 'bold'))
            if len(userInput.get()) > 27:
                userInput.config(font=('Arial', 10, 'bold'))
            if len(userInput.get()) > 35:
                userInput.delete(len(userInput.get()) - 1, 'end')

    userInput.insert('end', item)


userInput = Entry(bg='black', fg='white', font=('Arial', 18, 'bold'))
userInput.place(x=0, y=0, height=100, width=320)

Button(text='c', font=('Arial', 15, 'bold'), bg='black', fg='DarkOrange2', command=clear).place(x=0, y=100, width=80, height=60)
Button(text='🔙', font=('Arial', 15, 'bold'), bg='black', fg='DarkOrange2', command=delet).place(x=80, y=100, width=80, height=60)
Button(text='π', font=('Arial', 15, 'bold'), bg='black', fg='DarkOrange2', command=lambda: main('3.14')).place(x=160, y=100, width=80, height=60)
Button(text='÷', font=('Arial', 15, 'bold'), bg='black', fg='DarkOrange2', command=lambda: main('/')).place(x=240, y=100, width=80, height=60)

Button(text='7', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('7')).place(x=0, y=160, width=80, height=60)
Button(text='8', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('8')).place(x=80, y=160, width=80, height=60)
Button(text='9', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('9')).place(x=160, y=160, width=80, height=60)
Button(text='×', font=('Arial', 15, 'bold'), bg='black', fg='DarkOrange2', command=lambda: main('*')).place(x=240, y=160, width=80, height=60)

Button(text='4', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('4')).place(x=0, y=220, width=80, height=60)
Button(text='5', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('5')).place(x=80, y=220, width=80, height=60)
Button(text='6', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('6')).place(x=160, y=220, width=80, height=60)
Button(text='-', font=('Arial', 15, 'bold'), bg='black', fg='DarkOrange2', command=lambda: main('-')).place(x=240, y=220, width=80, height=60)

Button(text='1', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('1')).place(x=0, y=280, width=80, height=60)
Button(text='2', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('2')).place(x=80, y=280, width=80, height=60)
Button(text='3', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('3')).place(x=160, y=280, width=80, height=60)
Button(text='+', font=('Arial', 15, 'bold'), bg='black', fg='DarkOrange2', command=lambda: main('+')).place(x=240, y=280, width=80, height=60)

Button(text='e', font=('Arial', 15, 'bold'), bg='black', fg='DarkOrange2', command=lambda: main('2.71828')).place(x=0, y=340, width=80, height=60)
Button(text='0', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('0')).place(x=80, y=340, width=80, height=60)
Button(text='.', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('.')).place(x=160, y=340, width=80, height=60)
Button(text='=', font=('Arial', 15, 'bold'), bg='DarkOrange2', fg='white', command=result).place(x=240, y=340, width=80, height=60)


root.mainloop()