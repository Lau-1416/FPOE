import requests
#from back.api.models.Universidad import Universidad
from tkinter import messagebox
import re 
import tkinter as tk

class Validaciones():
    pass

        

#lblAdvertencia4 = tk.Label(frame, text='Solo se permiten Numeros y "/"', fg="red")

'''class ControladorUniversidad:
    def __init__(self):
        pass

    def ingresar_universidad(self, docente, estudiante, salon, local):
        # Vinculacion con la vista API de la clase Universidad
        url = 'http://127.0.0.1:8000/v1/universidad'

        # Preparar los datos para enviar a la API en una estructura JSON
        data = {
            "docente": docente,
            "estudiante": estudiante,
            "salon": salon,
            "local": local
        }

        try:
            # Realizar la solicitud POST a tu API
            response = requests.post(url, json=data)

            # Verificar el código de estado de la respuesta
            if response.status_code == 201:  # 201 significa creado (created)
                messagebox.showinfo("Éxito", "Universidad creada exitosamente.")
            else:
                messagebox.showerror("Error", f"Error al crear universidad: {response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}")'''