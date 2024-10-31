from tkinter import *
import math
import random

root = Tk()
root.title("Calculatrice")
root.resizable(0, 0)
root.configure(bg="#5ea88a")
root.iconbitmap('calculator.ico')

calculator = Frame(root)
calculator.grid()

menubar = Menu(calculator)
filemenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label='Fichier', menu=filemenu)


e = Entry(root, width=55, borderwidth=5, )
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
root.resizable(height = None, width = None)

π = math.pi
RC = math.sqrt
RandInt = random.randint

sin = math.sin
cos = math.cos
tan = math.tan
arcsin = math.asin
arccos = math.acos
arctan = math.atan

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_equal():
    number = e.get()
    e.delete(0, END)
    e.insert(0, eval(number))


button_1 = Button(root, text="1", width=1, height=1, padx=40, pady=20, bg='#98c7b2', font=("Berlin Sans FB", 15), command=lambda:button_click('1'))
button_2 = Button(root, text="2", width=1, height=1, padx=40, pady=20, bg='#98c7b2', font=("Berlin Sans FB", 15), command=lambda:button_click('2'))
button_3 = Button(root, text="3", width=1, height=1, padx=40, pady=20, background='#98c7b2', font=("Berlin Sans FB", 15), command=lambda:button_click('3'))
button_4 = Button(root, text="4", width=1, height=1, padx=40, pady=20, background='#98c7b2', font=("Berlin Sans FB", 15), command=lambda:button_click('4'))
button_5 = Button(root, text="5", width=1, height=1, padx=40, pady=20, background='#98c7b2', font=("Berlin Sans FB", 15), command=lambda:button_click('5'))
button_6 = Button(root, text="6", width=1, height=1, padx=40, pady=20, background='#98c7b2', font=("Berlin Sans FB", 15), command=lambda:button_click('6'))
button_7 = Button(root, text="7", width=1, height=1, padx=40, pady=20, background='#98c7b2', font=("Berlin Sans FB", 15), command=lambda:button_click('7'))
button_8 = Button(root, text="8", width=1, height=1, padx=40, pady=20, background='#98c7b2', font=("Berlin Sans FB", 15), command=lambda:button_click('8'))
button_9 = Button(root, text="9", width=1, height=1, padx=40, pady=20, background='#98c7b2', font=("Berlin Sans FB", 15), command=lambda:button_click('9'))
button_0 = Button(root, text="0", width=1, height=1, padx=40, pady=20, background='#98c7b2', font=("Berlin Sans FB", 15), command=lambda:button_click('0'))
button_C = Button(root, text="C", width=1, height=1, padx=40, pady=20, bg='#d0444a', font=("Berlin Sans FB", 15), command=lambda:button_clear())
button_addition = Button(root, text="+", width=1, height=1, padx=40, pady=20, bg='gray', font=("Berlin Sans FB", 15),command=lambda:button_click('+'))
button_soustraction = Button(root, text="-", width=1, height=1, padx=40, pady=20, bg='gray', font=("Berlin Sans FB", 15),command=lambda:button_click('-'))
button_division = Button(root, text="÷", width=1, height=1, padx=40, pady=20, bg='gray', font=("Berlin Sans FB", 15), command=lambda:button_click('/'))
button_multiplication = Button(root, text="×", width=1, height=1, padx=40, pady=20, bg='gray', font=("Berlin Sans FB", 15), command=lambda:button_click('*'))
button_e = Button(root, text="=", width=1, height=1, padx=40, pady=20, background='#ffd903', font=("Berlin Sans FB", 15), command=lambda:button_equal())
button_v = Button(root, text=",", width=1, height=1, padx=40, pady=20, background='#5ea88a', font=("Berlin Sans FB", 15), command=lambda:button_click('.'))
button_rc = Button(root, text="√", width=1, height=1, padx=40, pady=20, background='#5ea88a', font=("Arial", 15), command=lambda:button_click('RC('))
button_pl = Button(root, text="(", width=1, height=1, padx=40, pady=20, background='#5ea88a', font=("Berlin Sans FB", 15), command=lambda:button_click('('))
button_pr = Button(root, text=")", width=1, height=1, padx=40, pady=20, background='#5ea88a', font=("Berlin Sans FB", 15), command=lambda:button_click(')'))
button_pi = Button(root, text="π", width=1, height=1, padx=40, pady=20, background='#5ea88a', font=("Arial", 15), command=lambda:button_click('π'))
button_randInt = Button(root, text="RandInt", width=1, height=1, padx=40, pady=20, background='#5ea88a', font=("Arial", 15), command=lambda:button_click('RandInt('))
button_pv = Button(root, text=";", width=1, height=1, padx=40, pady=20, background='#5ea88a', font=("Berlin Sans FB", 15), command=lambda:button_click(','))
button_sin = Button(root, text="Sin", width=1, height=1, padx=40, pady=20, background='#5ea88a', font=("Berlin Sans FB", 15), command=lambda:button_click('sin('))
button_cos = Button(root, text="Cos", width=1, height=1, padx=40, pady=20, background='#5ea88a', font=("Berlin Sans FB", 15), command=lambda:button_click('cos('))
button_tan = Button(root, text="Tan", width=1, height=1, padx=40, pady=20, background='#5ea88a', font=("Berlin Sans FB", 15), command=lambda:button_click('tan('))
button_asin = Button(root, text="ArcSin", width=1, height=1, padx=40, pady=20, background='#5ea88a', font=("Berlin Sans FB", 15), command=lambda:button_click('arcsin('))
button_acos = Button(root, text="ArcCos", width=1, height=1, padx=40, pady=20, background='#5ea88a', font=("Berlin Sans FB", 15), command=lambda:button_click('arccos('))
button_atan = Button(root, text="ArcTan", width=1, height=1, padx=40, pady=20, background='#5ea88a', font=("Berlin Sans FB", 15), command=lambda:button_click('arctan('))
button_carre = Button(root, text="_²", width=1, height=1, padx=40, pady=20, background='#5ea88a', font=("Berlin Sans FB", 15), command=lambda:button_click('**'))


button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_addition.grid(row=1, column=3)
button_sin.grid(row=1, column=4)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_soustraction.grid(row=2, column=3)
button_cos.grid(row=2, column=4)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_division.grid(row=3, column=3)
button_tan.grid(row=3, column=4)

button_C.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_e.grid(row=4, column=2)
button_multiplication.grid(row=4, column=3)
button_asin.grid(row=4, column=4)

button_pi.grid(row=5, column=0)
button_rc.grid(row=5, column=1)
button_pl.grid(row=5, column=2)
button_pr.grid(row=5, column=3)
button_acos.grid(row=5, column=4)

button_randInt.grid(row=6, column=0)
button_carre.grid(row=6, column=1)
button_v.grid(row=6, column=2)
button_pv.grid(row=6, column=3)
button_atan.grid(row=6, column=4)


root.mainloop()
