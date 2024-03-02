from tkinter import *
from math import sin, cos
root = Tk()

root.geometry('400x400')
root.resizable(width=False, height=False)
root['bg'] = 'black'
root.title('Калькулятор')

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
h = h / 2
w = w / 2
w = w - (w / 3.5)
h = h - (h / 2)

root.geometry(f'400x400+{int(w)}+{int(h)}')


def sinusCosinus(event):
    if event == 'sin':
        try:
            resSinus = sin(float(userInput.get()))
            userInput.delete(0, 'end')
            userInput.insert(0, str(resSinus))
        except ValueError:
            userInput.delete(0, 'end')
            userInput.insert('end', 'Помилка!!!!')
            root.after(1500, clear)
    if event == 'cos':
        try:
            resCosinus = cos(float(userInput.get()))
            userInput.delete(0, 'end')
            userInput.insert(0, str(resCosinus))
        except ValueError:
            userInput.delete(0, 'end')
            userInput.insert('end', 'Помилка!!!!')
            root.after(1500, clear)


def delet():
    userInput.delete(len(userInput.get()) - 1, 'end')


def clear():
    userInput.delete(0, 'end')


def leave():
    root.destroy()


def result():
    try:
        res = eval(userInput.get())
        userInput.delete(0, 'end')
        userInput.insert('end', res)
    except ZeroDivisionError:
        userInput.delete(0, 'end')
        userInput.insert('end', 'Неможна ділити на нуль')
        root.after(1500, clear)
    except NameError:
        userInput.delete(0, 'end')
        userInput.insert('end', 'Неможна вводити букви')
        root.after(1500, clear)
    except ValueError:
        userInput.delete(0, 'end')
        userInput.insert('end', 'Помилка!!!!')
        root.after(1500, clear)
    except SyntaxError:
        userInput.delete(0, 'end')
        userInput.insert('end', 'Помилка!!!!')
        root.after(1500, clear)


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
userInput.place(x=0, y=0, height=100, width=400)

Button(text='c', font=('Arial', 15, 'bold'), bg='black', fg='DarkOrange2', command=clear).place(x=0, y=100, width=80, height=60)
Button(text='🔙', font=('Arial', 15, 'bold'), bg='black', fg='DarkOrange2', command=delet).place(x=80, y=100, width=80, height=60)
Button(text='π', font=('Arial', 15, 'bold'), bg='black', fg='DarkOrange2', command=lambda: main('3.14')).place(x=160, y=100, width=80, height=60)
Button(text='÷', font=('Arial', 15, 'bold'), bg='black', fg='DarkOrange2', command=lambda: main('/')).place(x=240, y=100, width=80, height=60)
Button(text='(', font=('Arial', 15, 'bold'), bg='black', fg='DarkOrange2', command=lambda: main('(')).place(x=320, y=100, width=80, height=60)

Button(text='7', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('7')).place(x=0, y=160, width=80, height=60)
Button(text='8', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('8')).place(x=80, y=160, width=80, height=60)
Button(text='9', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('9')).place(x=160, y=160, width=80, height=60)
Button(text='×', font=('Arial', 15, 'bold'), bg='black', fg='DarkOrange2', command=lambda: main('*')).place(x=240, y=160, width=80, height=60)
Button(text=')', font=('Arial', 15, 'bold'), bg='black', fg='DarkOrange2', command=lambda: main(')')).place(x=320, y=160, width=80, height=60)

Button(text='4', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('4')).place(x=0, y=220, width=80, height=60)
Button(text='5', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('5')).place(x=80, y=220, width=80, height=60)
Button(text='6', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('6')).place(x=160, y=220, width=80, height=60)
Button(text='-', font=('Arial', 15, 'bold'), bg='black', fg='DarkOrange2', command=lambda: main('-')).place(x=240, y=220, width=80, height=60)
Button(text='sin', font=('Arial', 15, 'bold'), bg='black', fg='DarkOrange2', command=lambda: sinusCosinus('sin')).place(x=320, y=220, width=80, height=60)

Button(text='1', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('1')).place(x=0, y=280, width=80, height=60)
Button(text='2', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('2')).place(x=80, y=280, width=80, height=60)
Button(text='3', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('3')).place(x=160, y=280, width=80, height=60)
Button(text='+', font=('Arial', 15, 'bold'), bg='black', fg='DarkOrange2', command=lambda: main('+')).place(x=240, y=280, width=80, height=60)
Button(text='cos', font=('Arial', 15, 'bold'), bg='black', fg='DarkOrange2', command=lambda: sinusCosinus('cos')).place(x=320, y=280, width=80, height=60)

Button(text='e', font=('Arial', 15, 'bold'), bg='black', fg='DarkOrange2', command=lambda: main('2.71828')).place(x=0, y=340, width=80, height=60)
Button(text='0', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('0')).place(x=80, y=340, width=80, height=60)
Button(text='.', font=('Arial', 15, 'bold'), bg='black', fg='white', command=lambda: main('.')).place(x=160, y=340, width=80, height=60)
Button(text='=', font=('Arial', 15, 'bold'), bg='DarkOrange2', fg='white', command=result).place(x=240, y=340, width=80, height=60)
Button(text='Вихід', font=('Arial', 15, 'bold'), bg='black', fg='DarkOrange2', command=leave).place(x=320, y=340, width=80, height=60)


root.mainloop()