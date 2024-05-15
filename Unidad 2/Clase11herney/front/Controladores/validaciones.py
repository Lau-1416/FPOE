import requests
from tkinter import messagebox
from Vistas import vistaUniversidad
import re

class Validaciones():
    def __init__(self):
        pass

    def ingresar_universidad(self):
        docente = vistaUniversidad.txtDocente.get()
        estudiante = vistaUniversidad.txtEstudiante.get()
        salon = vistaUniversidad.txtSalon.get()
        local = vistaUniversidad.txtLocal.get()

        # Verificar si alguna advertencia está visible
        if (vistaUniversidad.txtDocente.lblAdvertencia.winfo_viewable() or
            vistaUniversidad.txtEstudiante.lblAdvertencia1.winfo_viewable() or
            vistaUniversidad.txtSalon.lblAdvertencia.winfo_viewable() or
            vistaUniversidad.txtLocal.lblAdvertencia.winfo_viewable()):
            messagebox.showwarning("Error", "Por favor completa todos los campos correctamente.")
            return

        # Validar los campos antes de enviar los datos a la API
        if not docente or not estudiante or not salon or not local:
            messagebox.showwarning("Error", "Por favor completa todos los campos.")
            return

        # Si todos los campos están bien diligenciados, enviar los datos a la API
        data = {
            "docente": docente,
            "estudiante": estudiante,
            "salon": salon,
            "local": local
        }

        url = 'http://127.0.0.1:8000/v1/universidad'

        try:
            response = requests.post(url, json=data)
            if response.status_code == 201:
                messagebox.showinfo("Éxito", "Universidad creada exitosamente.")
            else:
                messagebox.showerror("Error", f"Error al crear universidad: {response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}")
    
    def validar_entrada(entrada):
        if not entrada or re.match("^[a-zA-Z ]*$", entrada):
            return True
        else:
            return False

    def mostrar_advertencia(event):
        nuevoValor = event.widget.get()
        if not nuevoValor or re.match("^[a-zA-Z ]*$", nuevoValor):
            event.widget.lblAdvertencia.grid_remove()
        else:
            event.widget.lblAdvertencia.grid(row=2, column=1)

    def mostrar_advertencia1(event):
        nuevoValor = event.widget.get()
        if not nuevoValor or re.match("^[a-zA-Z ]*$", nuevoValor):
            event.widget.lblAdvertencia1.grid_remove()
        else:
            event.widget.lblAdvertencia1.grid(row=4, column=1)

    def mostrar_advertencia_salon(event):
        nuevoValor = event.widget.get()
        if not nuevoValor:
            event.widget.lblAdvertencia.grid_remove() 
        elif not re.match("^[a-zA-Z0-9 ]*$", nuevoValor):
            event.widget.lblAdvertencia.grid(row=6, column=1) 
        else:
            event.widget.lblAdvertencia.grid_remove() 

    def mostrar_advertencia_local(event):
        nuevoValor = event.widget.get()
        if not re.match("^[a-zA-Z0-9 ]*$", nuevoValor):
            vistaUniversidad.txtLocal.lblAdvertencia.grid(row=8, column=1) 
        else:
            vistaUniversidad.txtLocal.lblAdvertencia.grid_remove() 