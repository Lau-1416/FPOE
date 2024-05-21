import tkinter as tk
from tkinter import messagebox
import re
import requests
import sys
sys.path.append("Controladores")
from controladores.validaciones import Validaciones
from controladores.peticiones import Peticiones
from controladores.validaciones import Validaciones
from functools import partial
from tkinter import ttk


validaciones = Validaciones()

def peticion_ingresar_universidad():
    Peticiones.ingresar_universidad(txtDocente, txtEstudiante, txtSalon, txtLocal)


'''def ingresar_universidad():
    #Obtener los datos de los campos de entrada
    docente = txtDocente.get()
    estudiante = txtEstudiante.get()
    salon = txtSalon.get()
    local = txtLocal.get()

    #Validar si todos los campos están completos
    if not docente or not estudiante or not salon or not local:
        messagebox.showwarning("Error", "Por favor completa todos los campos.")
        return

    #Preparar los datos para enviar a la API en una estructura JSON
    data = {
        "docente": docente,
        "estudiante": estudiante,
        "salon": salon,
        "local": local
    }

    #Vinculacion con la vista APU de la clase Universidad
    url = 'http://127.0.0.1:8000/v1/universidad'

    try:
        #Realizar la solicitud POST a tu API
        response = requests.post(url, json=data)

        # Verificar el código de estado de la respuesta
        if response.status_code == 201:  # 201 significa creado (created)
            messagebox.showinfo("Éxito", "Universidad creada exitosamente.")
        else:
            messagebox.showerror("Error", f"Error al crear universidad: {response.text}")
    except Exception as e:
        messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}")'''

class ResultadosVentana(tk.Toplevel):
    def __init__(self, resultados):
        super().__init__()
        self.title('Resultados de Búsqueda')
        
        self.tabla = ttk.Treeview(self)
        self.tabla["columns"]=("docente","estudiante","salon","local","id")
        self.tabla.column("#0", width=0, stretch=tk.NO)
        self.tabla.column("docente", width=100)
        self.tabla.column("estudiante", width=100)
        self.tabla.column("salon", width=100)
        self.tabla.column("local", width=100)
        self.tabla.column("id", width=50)
        
        self.tabla.heading("docente", text="Docente")
        self.tabla.heading("estudiante", text="Estudiante")
        self.tabla.heading("salon", text="Salón")
        self.tabla.heading("local", text="Local")
        self.tabla.heading("id", text="ID")
        
        for resultado in resultados:
            self.tabla.insert("", 'end', text="", values=(resultado['docente'], resultado['estudiante'], resultado['salon'], resultado['local'], resultado['id']))
        
        self.tabla.pack(expand=True, fill="both")


def accion_buscar_boton(txtDocente, txtEstudiante, txtSalon, txtLocal, txtId):
    datos = {
        "docente": txtDocente.get(),
        "estudiante": txtEstudiante.get(),
        "salon": txtSalon.get(),
        "local": txtLocal.get(),
        "id": txtId.get()
    }
    resultados = Peticiones.buscar(datos)
    if resultados:
        ResultadosVentana(resultados)
    else:
        messagebox.showinfo("Información", "No se encontraron resultados.")

principal = tk.Tk()
principal.title('Universidad')
principal.geometry("290x310")

frame = tk.Frame(principal, padx=10, pady=10)
frame.pack(padx=10, pady=10)

lblTitulo = tk.Label(frame, text='Ingresar Datos')
lblTitulo.grid(row=0, column=0, columnspan=2) 

lblDocente = tk.Label(frame, text='Docente:')
lblDocente.grid(row=1, column=0, padx=5, pady=5)  
lblEtudiante = tk.Label(frame, text='Estudiante:')
lblEtudiante.grid(row=3, column=0, padx=5, pady=5)
lblSalon = tk.Label(frame, text='Salón:')
lblSalon.grid(row=5, column=0, padx=5, pady=5)
lblLocal = tk.Label(frame, text='Local:')
lblLocal.grid(row=7, column=0, padx=5, pady=5)
lblConsulta = tk.Label(frame)
lblConsulta.grid(row=11,column=1,columnspan=2)

txtDocente = tk.Entry(frame, width=20)
txtDocente.grid(row=1, column=1, padx=5, pady=5)  
txtDocente.lblAdvertencia = tk.Label(frame, text='Solo se permiten letras', fg="red")
txtDocente.lblAdvertencia.grid(row=2, column=1, sticky="w")
txtDocente.lblAdvertencia.grid_remove()

txtEstudiante = tk.Entry(frame, width=20)
txtEstudiante.grid(row=3, column=1, padx=5, pady=5)
txtEstudiante.lblAdvertencia1 = tk.Label(frame, text='Solo se permiten letras', fg="red")
txtEstudiante.lblAdvertencia1.grid(row=4, column=1, sticky="w")
txtEstudiante.lblAdvertencia1.grid_remove()

txtSalon = tk.Entry(frame, width=20)
txtSalon.grid(row=5, column=1, padx=5, pady=5)  
txtSalon.lblAdvertencia = tk.Label(frame, text='Solo se permiten Numeros-Letras', fg="red")
txtSalon.lblAdvertencia.grid(row=6, column=1, sticky="w")
txtSalon.lblAdvertencia.grid_remove()

txtLocal = tk.Entry(frame, width=20)
txtLocal.grid(row=7, column=1, padx=5, pady=5)
txtLocal.lblAdvertencia = tk.Label(frame, text='Solo se permiten Numeros-Letras', fg="red")
txtLocal.lblAdvertencia.grid(row=8, column=1, sticky="w")
txtLocal.lblAdvertencia.grid_remove()

btnIngresar = tk.Button(frame, text='Ingresar', command=peticion_ingresar_universidad)
btnIngresar.grid(row=12, column=1, columnspan=2)


lblId = tk.Label(frame, text='ID:')
lblId.grid(row=9, column=0, padx=5, pady=5)

txtId = tk.Entry(frame, width=20)
txtId.grid(row=9, column=1, padx=5, pady=5)

btnConsultar = tk.Button(frame, text='Consultar', command=partial(Peticiones.accion_consultar_boton, txtId, lblConsulta))
btnConsultar.grid(row=13, column=1, columnspan=2)


btnConsultarTodos = tk.Button(frame, text='Consultar Todos', command=partial(accion_buscar_boton, txtDocente, txtEstudiante, txtSalon, txtLocal, txtId))
btnConsultarTodos.grid(row=14, column=1, columnspan=2)



txtDocente.bind('<KeyRelease>', Validaciones.mostrar_advertencia)
txtEstudiante.bind('<KeyRelease>', Validaciones.mostrar_advertencia1)
txtSalon.bind('<KeyRelease>', Validaciones.mostrar_advertencia_salon)
txtLocal.bind('<KeyRelease>', Validaciones.mostrar_advertencia_local)

principal.mainloop()