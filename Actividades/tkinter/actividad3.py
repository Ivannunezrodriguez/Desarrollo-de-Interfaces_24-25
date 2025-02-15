import tkinter as tk
from tkinter import PhotoImage, font
import sqlite3
from tkinter import messagebox

with sqlite3.connect('empleados.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS empleados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        fecha_inicio TEXT,
        fecha_nacimiento TEXT,
        direccion TEXT,
        nif TEXT,
        datos_bancarios TEXT,
        afiliacion_ss TEXT,
        genero TEXT,
        departamento TEXT,
        puesto TEXT,
        telefono TEXT,
        email TEXT,
        salario_anual REAL,
        pagas_extra INTEGER,
        irpf REAL,
        seguridad_social REAL
    )''')
    conn.commit()

def mostrar_ventana_altas():
    ventana_altas = tk.Toplevel()
    ventana_altas.title("Altas de Empleados")
    ventana_altas.config(bg="#F0F0F0", padx=20, pady=20)

    etiquetas_font = font.Font(family="Arial", size=10, weight="normal")
    campos = [
        "Apellidos y Nombre",
        "Fecha Inicio",
        "Fecha Nacimiento",
        "Dirección",
        "NIF",
        "Datos Bancarios",
        "Número de Afiliación SS",
        "Género",
        "Departamento",
        "Puesto",
        "Teléfono",
        "Email",
        "Salario Anual",
        "Pagas Extra",
        "IRPF",
        "Seguridad Social"
    ]
    entradas = {}

    lbl_apellidos_nombre = tk.Label(ventana_altas, text="APELLIDOS Y NOMBRE", bg="#F0F0F0",
                                    font=etiquetas_font, anchor="center")
    lbl_apellidos_nombre.grid(row=1, column=0, columnspan=6, padx=5, pady=(5,0), sticky="ew")
    entradas["Apellidos y Nombre"] = tk.Entry(ventana_altas, width=60)
    entradas["Apellidos y Nombre"].grid(row=2, column=0, columnspan=6, padx=5, pady=(0,15), sticky="we")

    lbl_fecha_inicio = tk.Label(ventana_altas, text="FECHA INICIO", bg="#F0F0F0",
                                font=etiquetas_font, anchor="center")
    lbl_fecha_inicio.grid(row=3, column=0, padx=5, sticky="ew")
    entradas["Fecha Inicio"] = tk.Entry(ventana_altas, width=12)
    entradas["Fecha Inicio"].grid(row=4, column=0, padx=5, pady=5, sticky="w")

    lbl_fecha_nac = tk.Label(ventana_altas, text="FECHA NACIMIENTO", bg="#F0F0F0",
                             font=etiquetas_font, anchor="center")
    lbl_fecha_nac.grid(row=3, column=1, padx=(10,0), sticky="ew")
    entradas["Fecha Nacimiento"] = tk.Entry(ventana_altas, width=12)
    entradas["Fecha Nacimiento"].grid(row=4, column=1, padx=5, pady=5, sticky="w")

    lbl_direccion = tk.Label(ventana_altas, text="DIRECCIÓN", bg="#F0F0F0",
                             font=etiquetas_font, anchor="center")
    lbl_direccion.grid(row=3, column=2, columnspan=4, padx=(10,0), sticky="ew")
    entradas["Dirección"] = tk.Entry(ventana_altas, width=40)
    entradas["Dirección"].grid(row=4, column=2, columnspan=4, padx=5, pady=5, sticky="we")

    lbl_nif = tk.Label(ventana_altas, text="NIF", bg="#F0F0F0",
                       font=etiquetas_font, anchor="center")
    lbl_nif.grid(row=5, column=0, padx=5, sticky="ew")
    entradas["NIF"] = tk.Entry(ventana_altas, width=12)
    entradas["NIF"].grid(row=6, column=0, padx=5, pady=5, sticky="w")

    lbl_datos_banc = tk.Label(ventana_altas, text="DATOS BANCARIOS", bg="#F0F0F0",
                              font=etiquetas_font, anchor="center")
    lbl_datos_banc.grid(row=5, column=1, columnspan=2, padx=(10,0), sticky="ew")
    entradas["Datos Bancarios"] = tk.Entry(ventana_altas, width=30)
    entradas["Datos Bancarios"].grid(row=6, column=1, columnspan=2, padx=5, pady=5, sticky="we")

    lbl_afiliacion = tk.Label(ventana_altas, text="NÚMERO DE AFILIACIÓN SS", bg="#F0F0F0",
                              font=etiquetas_font, anchor="center")
    lbl_afiliacion.grid(row=5, column=3, columnspan=3, padx=(10,0), sticky="ew")
    entradas["Número de Afiliación SS"] = tk.Entry(ventana_altas, width=70)
    entradas["Número de Afiliación SS"].grid(row=6, column=3, columnspan=3, padx=5, pady=5, sticky="w")

    lbl_genero = tk.Label(ventana_altas, text="GÉNERO", bg="#F0F0F0",
                          font=etiquetas_font, anchor="center")
    lbl_genero.grid(row=7, column=0, padx=5, sticky="ew")
    entradas["Género"] = tk.Entry(ventana_altas, width=12)
    entradas["Género"].grid(row=8, column=0, padx=5, pady=5, sticky="w")

    lbl_depto = tk.Label(ventana_altas, text="DEPARTAMENTO", bg="#F0F0F0",
                         font=etiquetas_font, anchor="center")
    lbl_depto.grid(row=7, column=1, columnspan=2, padx=(10,0), sticky="ew")
    entradas["Departamento"] = tk.Entry(ventana_altas, width=30)
    entradas["Departamento"].grid(row=8, column=1, columnspan=2, padx=5, pady=5, sticky="we")

    lbl_puesto = tk.Label(ventana_altas, text="PUESTO", bg="#F0F0F0",
                          font=etiquetas_font, anchor="center")
    lbl_puesto.grid(row=7, column=3, columnspan=3, padx=(10,0), sticky="ew")
    entradas["Puesto"] = tk.Entry(ventana_altas, width=70)
    entradas["Puesto"].grid(row=8, column=3, columnspan=3, padx=5, pady=5, sticky="w")

    lbl_telefono = tk.Label(ventana_altas, text="TELÉFONO", bg="#F0F0F0",
                            font=etiquetas_font, anchor="center")
    lbl_telefono.grid(row=9, column=0, padx=5, sticky="ew")
    entradas["Teléfono"] = tk.Entry(ventana_altas, width=20)
    entradas["Teléfono"].grid(row=9, column=1, padx=5, pady=5, sticky="w")

    lbl_salario = tk.Label(ventana_altas, text="SALARIO ANUAL", bg="#F0F0F0",
                           font=etiquetas_font, anchor="center")
    lbl_salario.grid(row=9, column=2, padx=(10,0), sticky="ew")
    entradas["Salario Anual"] = tk.Entry(ventana_altas, width=20)
    entradas["Salario Anual"].grid(row=9, column=3, padx=5, pady=5, sticky="w")

    lbl_irpf = tk.Label(ventana_altas, text="IRPF", bg="#F0F0F0",
                        font=etiquetas_font, anchor="center")
    lbl_irpf.grid(row=9, column=4, padx=(10,0), sticky="ew")
    entradas["IRPF"] = tk.Entry(ventana_altas, width=20)
    entradas["IRPF"].grid(row=9, column=5, padx=5, pady=5, sticky="w")

    lbl_email = tk.Label(ventana_altas, text="EMAIL", bg="#F0F0F0",
                         font=etiquetas_font, anchor="center")
    lbl_email.grid(row=10, column=0, padx=(10,0), sticky="ew")
    entradas["Email"] = tk.Entry(ventana_altas, width=20)
    entradas["Email"].grid(row=10, column=1, padx=5, pady=5, sticky="w")

    lbl_pag_extras = tk.Label(ventana_altas, text="PAGAS EXTRA", bg="#F0F0F0",
                              font=etiquetas_font, anchor="center")
    lbl_pag_extras.grid(row=10, column=2, padx=(10,0), sticky="ew")
    entradas["Pagas Extra"] = tk.Entry(ventana_altas, width=20)
    entradas["Pagas Extra"].grid(row=10, column=3, padx=5, pady=5, sticky="w")

    lbl_seg_social = tk.Label(ventana_altas, text="SEG. SOCIAL", bg="#F0F0F0",
                              font=etiquetas_font, anchor="center")
    lbl_seg_social.grid(row=10, column=4, padx=(10,0), sticky="ew")
    entradas["Seguridad Social"] = tk.Entry(ventana_altas, width=20)
    entradas["Seguridad Social"].grid(row=10, column=5, padx=5, pady=5, sticky="w")

    def insertar_empleado():
        datos = {campo: entradas[campo].get() for campo in campos}
        try:
            with sqlite3.connect('empleados.db') as conn:
                cursor = conn.cursor()
                cursor.execute('''INSERT INTO empleados (
                    nombre, fecha_inicio, fecha_nacimiento, direccion,
                    nif, datos_bancarios, afiliacion_ss, genero,
                    departamento, puesto, telefono, email,
                    salario_anual, pagas_extra, irpf, seguridad_social
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (datos["Apellidos y Nombre"],
                 datos["Fecha Inicio"],
                 datos["Fecha Nacimiento"],
                 datos["Dirección"],
                 datos["NIF"],
                 datos["Datos Bancarios"],
                 datos["Número de Afiliación SS"],
                 datos["Género"],
                 datos["Departamento"],
                 datos["Puesto"],
                 datos["Teléfono"],
                 datos["Email"],
                 float(datos["Salario Anual"]) if datos["Salario Anual"].replace('.', '', 1).isdigit() else 0.0,
                 int(datos["Pagas Extra"]) if datos["Pagas Extra"].isdigit() else 0,
                 float(datos["IRPF"]) if datos["IRPF"].replace('.', '', 1).isdigit() else 0.0,
                 float(datos["Seguridad Social"]) if datos["Seguridad Social"].replace('.', '', 1).isdigit() else 0.0))
            try:
                with open('empleados.txt', 'a', encoding='utf-8') as f:
                    f.write(
                       f"{datos['Apellidos y Nombre']}\n"
                    f"{datos['Dirección']}\n"
                    f"NIF {datos['NIF']}     NAF {datos['Número de Afiliación SS']}     "
                    f"CCC {datos['Datos Bancarios']}\n"
                    "CONCEPTOS SALARIALES ----------------------------------------\n"
                    f"SALARIO ANUAL: {datos['Salario Anual']}    "
                    f"PAGAS: {datos['Pagas Extra']}    "
                    f"IRPF: {datos['IRPF']}    "
                    f"SEGURIDAD SOCIAL: {datos['Seguridad Social']}\n\n"
                    )
            except IOError as e:
                messagebox.showerror("Error", f"Error al escribir en el fichero: {e}")
            messagebox.showinfo("Éxito", "Empleado insertado correctamente")
            ventana_altas.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error al insertar empleado: {e}")

    boton_insertar = tk.Button(ventana_altas, text="INSERTAR", bg="#FEE88D",
                               font=("Arial", 12, "bold"), command=insertar_empleado)
    boton_insertar.grid(row=11, column=5, pady=10, sticky="e")

def mostrar_fichero_empleados():
    try:
        with open('empleados.txt', 'r', encoding='utf-8') as f:
            contenido = f.read()
        ventana_fichero = tk.Toplevel()
        ventana_fichero.title("Fichero de Empleados")
        text_area = tk.Text(ventana_fichero, wrap="word")
        text_area.insert("1.0", contenido)
        text_area.pack(expand=True, fill="both")
    except FileNotFoundError:
        messagebox.showerror("Error", "El fichero empleados.txt no existe")

ventana_principal = tk.Tk()
ventana_principal.title("Personal +")
ventana_principal.geometry("600x350")

titulo = tk.Label(ventana_principal, text="PERSONAL +", font=("Arial", 14, "bold"))
titulo.pack(pady=5)
imagen = tk.PhotoImage(file="D:/drive ivan/Curso DAM daw/UNIR/2_curso/Desarrollo de interfaces/Actividades/tkinter/seta.png")

logo = tk.Label(ventana_principal, image=imagen)
logo.pack(pady=10)

boton_alta = tk.Button(ventana_principal, text="ALTA EMPLEADO", bg="lightyellow", command=mostrar_ventana_altas)
boton_alta.pack(pady=5)

boton_fichero = tk.Button(ventana_principal, text="FICHERO EMPLEADOS", bg="lightyellow", command=mostrar_fichero_empleados)
boton_fichero.pack(pady=5)

ventana_principal.mainloop()
