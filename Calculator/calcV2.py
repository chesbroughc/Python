from tkinter import *
import math


# establish root
root = Tk()
root.title("Calculator 2.0")
root.iconbitmap(
    r"C:\Users\chesb\OneDrive\Documents\VSC\PY4E\Calculator\calc.ico")

# change window size
root.geometry("438x605")

# Create entry box
e = Entry(root, width=25, borderwidth=7,
          font="Calibri 20", justify=RIGHT, )
e.grid(row=0, columnspan=4, padx=2, pady=10)


# -------------------------------------------------------------------CREATE BUTTON FUNCTIONS-----------------------------------------------------------------------------


def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def clear():
    e.delete(0, END)


def add():
    num1 = e.get()
    global f_num
    global expression
    expression = "addition"
    f_num = int(num1)
    e.delete(0, END)


def subtract():
    num1 = e.get()
    global f_num
    global expression
    expression = "subtraction"
    f_num = int(num1)
    e.delete(0, END)


def multiply():
    num1 = e.get()
    global f_num
    global expression
    expression = "multiplication"
    f_num = int(num1)
    e.delete(0, END)


def divide():
    num1 = e.get()
    global f_num
    global expression
    expression = "division"
    f_num = int(num1)
    e.delete(0, END)


def square():
    num1 = e.get()
    global f_num
    global expression
    expression = "square"
    f_num = int(num1)
    e.delete(0, END)
    e.insert(0, int(math.pow(f_num, 2)))


def squareRoot():
    num1 = e.get()
    global f_num
    global expression
    expression = "squareRoot"
    f_num = int(num1)
    e.delete(0, END)
    e.insert(0, int(math.sqrt(f_num)))


def equals():
    num2 = e.get()
    e.delete(0, END)

    if expression == "addition":
        e.insert(0, f_num + int(num2))

    if expression == "subtraction":
        e.insert(0, f_num - int(num2))

    if expression == "multiplication":
        e.insert(0, int(f_num) * int(num2))

    if expression == "division":
        e.insert(0, int(f_num) / int(num2))


# -------------------------------------------------------------------CREATE BUTTONS--------------------------------------------------------------------------------------
button1 = Button(root, text="1", padx=40, pady=30,
                 bg="grey", font="Calibri 17 bold", command=lambda: click(1))
button2 = Button(root, text="2", padx=40, pady=30,
                 bg="grey", font="Calibri 17 bold", command=lambda: click(2))
button3 = Button(root, text="3", padx=40, pady=30,
                 bg="grey", font="Calibri 17 bold", command=lambda: click(3))
button4 = Button(root, text="4", padx=40, pady=30,
                 bg="grey", font="Calibri 17 bold", command=lambda: click(4))
button5 = Button(root, text="5", padx=40, pady=30,
                 bg="grey", font="Calibri 17 bold", command=lambda: click(5))
button6 = Button(root, text="6", padx=40, pady=30,
                 bg="grey", font="Calibri 17 bold", command=lambda: click(6))
button7 = Button(root, text="7", padx=40, pady=30,
                 bg="grey", font="Calibri 17 bold", command=lambda: click(7))
button8 = Button(root, text="8", padx=40, pady=30,
                 bg="grey", font="Calibri 17 bold", command=lambda: click(8))
button9 = Button(root, text="9", padx=40, pady=30,
                 bg="grey", font="Calibri 17 bold", command=lambda: click(9))
button0 = Button(root, text="0", padx=40, pady=30,
                 bg="grey", font="Calibri 17 bold", command=lambda: click(0))
buttonclear = Button(root, text="C", padx=40, pady=30,
                     bg="grey", font="Calibri 17 bold", command=clear)
buttonequals = Button(root, text="=", padx=40, pady=30,
                      bg="grey", font="Calibri 17 bold", command=equals)
buttonplus = Button(root, text="+", padx=40, pady=30,
                    bg="grey", font="Calibri 17 bold", command=add)
buttonminus = Button(root, text="-", padx=40, pady=30,
                     bg="grey", font="Calibri 17 bold", command=subtract)
buttonmultiply = Button(root, text="x", padx=40, pady=30,
                        bg="grey", font="Calibri 17 bold", command=multiply)
buttondivide = Button(root, text="÷", padx=40, pady=30,
                      bg="grey", font="Calibri 17 bold", command=divide)
buttonsquare = Button(root, text="x²", padx=40, pady=30,
                      bg="grey", font="Calibri 15 bold", command=square)
buttonsquareroot = Button(root, text="√x", padx=40, pady=30,
                          bg="grey", font="Calibri 15 bold", command=squareRoot)

# grid format buttons 1-3, add
button1.grid(column=0, row=1, sticky=NSEW)
button2.grid(column=1, row=1, sticky=NSEW)
button3.grid(column=2, row=1, sticky=NSEW)
buttonplus.grid(column=3, row=1, sticky=NSEW)

# grid format buttons 4-6
button4.grid(column=0, row=2, sticky=NSEW)
button5.grid(column=1, row=2, sticky=NSEW)
button6.grid(column=2, row=2, sticky=NSEW)
buttonminus.grid(column=3, row=2, sticky=NSEW)

# grid format buttons 7-9
button7.grid(column=0, row=3, sticky=NSEW)
button8.grid(column=1, row=3, sticky=NSEW)
button9.grid(column=2, row=3, sticky=NSEW)
buttonmultiply.grid(column=3, row=3, sticky=NSEW)


# grid format square root, 0, squared, and divide buttons
buttonsquareroot.grid(column=0, row=4, sticky=NSEW)
button0.grid(column=1, row=4, sticky=NSEW)
buttonsquare.grid(column=2, row=4, sticky=NSEW)
buttondivide.grid(column=3, row=4, sticky=NSEW)


buttonclear.grid(column=3, row=5, sticky=NSEW)


buttonequals.grid(column=0, columnspan=3, row=5, sticky=NSEW)

# run window
root.mainloop()
