import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3

from ventana_altas import *
from ventana_bajas import *

principal = tk.Tk() # Creación del Objeto ventana 
principal.title("Ventana principal de ejemplo")
principal.geometry("600x400+300+300")
principal.minsize(400,300)
principal.configure(bd=20)
principal.resizable(False,False)

marco = ttk.Frame(principal)
marco.pack(expand=True)

boton1 = ttk.Button(marco, text="ALTAS", command=altas)
boton1.grid(row=0,column=0,padx=5,pady=5)

boton2 = ttk.Button(marco, text="BAJAS", command=bajas)
boton2.grid(row=0,column=1,padx=5,pady=5)

boton3 = ttk.Button(marco, text="INFORMES")
boton3.grid(row=1,column=0,padx=5,pady=5)

boton4 = ttk.Button(marco, text="CONTRATOS")
boton4.grid(row=1,column=1,padx=5,pady=5)

principal.mainloop() # Bucle principal de ventana
