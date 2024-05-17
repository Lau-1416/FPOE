import requests
from tkinter import messagebox
#import re
#from controladores import validaciones
#from front.controladores.validaciones import Validaciones
'''import sys
sys.path.append("controladores")
from controladores.validaciones import Validaciones'''
from .validaciones import Validaciones
from vistas import vistaUniversidad

import requests
from tkinter import messagebox

class Peticiones():
    @staticmethod
    def ingresar_universidad(txtDocente, txtEstudiante, txtSalon, txtLocal):
        docente = txtDocente.get()
        estudiante = txtEstudiante.get()
        salon = txtSalon.get()
        local = txtLocal.get()

        if not docente or not estudiante or not salon or not local:
            messagebox.showwarning("Error", "Por favor completa todos los campos.")
            return

        if (txtDocente.lblAdvertencia.winfo_viewable() or
            txtEstudiante.lblAdvertencia1.winfo_viewable() or
            txtSalon.lblAdvertencia.winfo_viewable() or
            txtLocal.lblAdvertencia.winfo_viewable()):
            messagebox.showwarning("Error", "Por favor completa todos los campos correctamente.")
            return

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


