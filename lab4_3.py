import InputBox
from tkinter import *

s = "Result:\n"

s += str("method 1\n")


InputBox.ShowDialog("enter the first number: ")
n1 = InputBox.GetInput()

InputBox.ShowDialog("enter the operator: ")
ops = InputBox.GetInput()

InputBox.ShowDialog("enter the second number: ")
n2 = InputBox.GetInput()

if ops == '+':
    s += str(float(n1) + float(n2))
if ops == '-':
    s += str(float(n1) - float(n2))
if ops == '*':
    s += str(float(n1) * float(n2))
if ops == '/':
    s += str(float(n1) / float(n2))
if ops == '%':
    s += str(float(n1) % float(n2))
if ops == '**':
    s += str(float(n1) ** float(n2))

s += str("\n\nmethod 2\n")

InputBox.ShowDialog("enter the first number: ")
n1 = InputBox.GetInput()

InputBox.ShowDialog("enter the operator: ")
ops = InputBox.GetInput()

InputBox.ShowDialog("enter the second number: ")
n2 = InputBox.GetInput()


def add():
    return str(float(n1) + float(n2))


def sub():
    return str(float(n1) - float(n2))


def mul():
    return str(float(n1) * float(n2))


def div():
    return str(float(n1) / float(n2))


def mod():
    return str(float(n1) % float(n2))


def exp():
    return str(float(n1) ** float(n2))

switch = {
    "+": add(),
    "-": sub(),
    "*": mul(),
    "/": div(),
    "%": mod(),
    "**": exp()
}
try:
    s += str(switch[ops])
except KeyError as ex:
    s += str("no matching case")

# Message Box Code#######


root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid(padx=10, pady=10)

root.mainloop()
