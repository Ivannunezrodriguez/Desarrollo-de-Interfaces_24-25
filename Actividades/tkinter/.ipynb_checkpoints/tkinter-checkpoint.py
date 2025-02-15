import tkinter as tk
from tkinter import messagebox
import sqlite3

# Crear base de datos y tabla
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

    campos = [
        "Apellidos y Nombre", "Fecha Inicio", "Fecha Nacimiento", "Dirección", "NIF", "Datos Bancarios", 
        "Número de Afiliación SS", "Género", "Departamento", "Puesto", "Teléfono", "Email", 
        "Salario Anual", "Pagas Extra", "IRPF", "Seguridad Social"
    ]

    entradas = {}

    for i, campo in enumerate(campos):
        label = tk.Label(ventana_altas, text=campo)
        label.grid(row=i, column=0, padx=5, pady=5, sticky="w")
        entrada = tk.Entry(ventana_altas, width=30)
        entrada.grid(row=i, column=1, padx=5, pady=5)
        entradas[campo] = entrada

    def insertar_empleado():
        datos = {campo: entradas[campo].get() for campo in campos}

        try:
            with sqlite3.connect('empleados.db') as conn:
                cursor = conn.cursor()
                cursor.execute('''INSERT INTO empleados (nombre, fecha_inicio, fecha_nacimiento, direccion, nif, datos_bancarios, afiliacion_ss, 
                    genero, departamento, puesto, telefono, email, salario_anual, pagas_extra, irpf, seguridad_social) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                    (datos["Apellidos y Nombre"], datos["Fecha Inicio"], datos["Fecha Nacimiento"], datos["Dirección"], datos["NIF"], datos["Datos Bancarios"],
                     datos["Número de Afiliación SS"], datos["Género"], datos["Departamento"], datos["Puesto"], datos["Teléfono"], datos["Email"],
                     float(datos["Salario Anual"]) if datos["Salario Anual"].replace('.', '', 1).isdigit() else 0.0,
                     int(datos["Pagas Extra"]) if datos["Pagas Extra"].isdigit() else 0,
                     float(datos["IRPF"]) if datos["IRPF"].replace('.', '', 1).isdigit() else 0.0,
                     float(datos["Seguridad Social"]) if datos["Seguridad Social"].replace('.', '', 1).isdigit() else 0.0))

            try:
                with open('empleados.txt', 'a') as f:
                    f.write(f"{datos['Apellidos y Nombre']}, {datos['Dirección']}, NIF {datos['NIF']}, NAF {datos['Número de Afiliación SS']}")
                    f.write(f"\nSalario Anual: {datos['Salario Anual']}, Pagas: {datos['Pagas Extra']}, IRPF: {datos['IRPF']}, Seguridad Social: {datos['Seguridad Social']}\n\n")
            except IOError as e:
                messagebox.showerror("Error", f"Error al escribir en el fichero: {e}")

            messagebox.showinfo("Éxito", "Empleado insertado correctamente")
            ventana_altas.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error al insertar empleado: {e}")

    boton_insertar = tk.Button(ventana_altas, text="INSERTAR", bg="lightyellow", command=insertar_empleado)
    boton_insertar.grid(row=len(campos), column=0, columnspan=2, pady=10)

def mostrar_fichero_empleados():
    try:
        with open('empleados.txt', 'r') as f:
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
ventana_principal.geometry("400x500")
ventana_principal.iconbitmap("icono.ico")

logo = tk.Label(ventana_principal, text="🍄", font=("Arial", 50))
logo.pack(pady=10)

titulo = tk.Label(ventana_principal, text="PERSONAL +", font=("Arial", 14, "bold"))
titulo.pack(pady=5)

boton_alta = tk.Button(ventana_principal, text="ALTA EMPLEADO", bg="lightyellow", command=mostrar_ventana_altas)
boton_alta.pack(pady=5)

boton_fichero = tk.Button(ventana_principal, text="FICHERO EMPLEADOS", bg="lightyellow", command=mostrar_fichero_empleados)
boton_fichero.pack(pady=5)

ventana_principal.mainloop()
