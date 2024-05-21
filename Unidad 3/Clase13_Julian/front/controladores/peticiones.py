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
  
    @staticmethod
    def consultar(id):
        try:
            resultado = requests.get('http://127.0.0.1:8000/v1/universidad/' + str(id))
            resultado.raise_for_status()  # Verifica si la solicitud tuvo éxito
            return resultado.json()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}")
            return None

    @staticmethod
    def accion_consultar_boton(txtId, lblConsulta):
        id_estudiante = txtId.get()
        if not id_estudiante.isdigit():
            lblConsulta.config(text="Por favor ingrese un ID válido.")
            return

        resultado = Peticiones.consultar(id_estudiante)
        
        if resultado and 'estudiante' in resultado:
            lblConsulta.config(text=f"Estudiante: {resultado['estudiante']}")
        else:
            lblConsulta.config(text="No se encontraron resultados")


    @staticmethod
    def buscar(datos):
        try:
            url = 'http://127.0.0.1:8000/v1/universidad?'
            for key, value in datos.items():
                if value:
                    url += f"{key}={value}&"
            
            resultado = requests.get(url)
            resultado.raise_for_status()
            return resultado.json()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}")
            return None
        

