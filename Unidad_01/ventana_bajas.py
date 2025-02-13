import tkinter as tk
from tkinter import ttk
from tkinter import *


def bajas():
    
    # Funciones para la ventana de bajas
    def sumar():
        res.set(float(num1.get()) + float(num2.get()))

    def resta():
        res.set(float(num1.get()) - float(num2.get()))

    def multi():
        res.set(float(num1.get()) * float(num2.get()))

    def borrar():
        num1.set("")
        num2.set("")
        res.set("")

    def creditos():
        creditos = tk.Toplevel()


        creditos.mainloop()
    # Crear la ventana de bajas
    bajas = tk.Toplevel()
    bajas.title("Bajas")
    bajas.configure(bd=20)
    bajas.resizable(width=False, height=False)
    
    # Variables de ventana
    num1 = StringVar()
    num2 = StringVar()
    res = StringVar()

    # Etiquetas y inputs
    Label(bajas,text="Primer número").pack()
    Entry(bajas,justify="center",textvariable=num1).pack() # Primer número de la operación

    Label(bajas,text="Segundo número").pack()
    Entry(bajas,justify="center",textvariable=num2).pack() # Segundo número de la operación

    Label(bajas,text="Resultado").pack()
    Entry(bajas,justify="center",textvariable=res,state="disabled").pack()

    Label(bajas,text="").pack() # Espacio de separación de botones

    Button(bajas, text="Sumar", command=sumar).pack(side="left")
    Button(bajas, text="Restar", command=resta).pack(side="left")
    Button(bajas, text="Multiplicar", command=multi).pack(side="left")
    Button(bajas, text="Borrar", command=borrar).pack(side="left")
    Button(bajas, text="Altas", command=creditos).pack(side="left")

    bajas.mainloop()