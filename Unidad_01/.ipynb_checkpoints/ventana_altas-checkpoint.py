import tkinter as tk
from tkinter import ttk
from tkinter import *


def altas():

    # funciones de cálculo u operativa, y otras ventanas superiores

    altas = tk.Toplevel()
    altas.title("Ventana altas")
    altas.geometry("300x300+400+400")
    altas.configure(bd=20)
    altas.resizable(False,False)

    Label(altas,text="Ventana superior").grid(row=2,column=2,padx=10,pady=10)


    altas.mainloop()