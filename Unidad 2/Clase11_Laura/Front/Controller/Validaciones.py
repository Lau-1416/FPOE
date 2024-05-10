import re 
from tkinter import messagebox
from Front.Views import VistasBafle
import requests

class Validaciones():
    
    def __init__(self):
        pass
    def ingresar_bafle(self):
        marca = VistasBafle.txtMarca.get()
        tamaño = VistasBafle.txtTamaño.get()
        color = VistasBafle.txtColor.get()
        precio = VistasBafle.txtPrecio.get()

        if not marca or not tamaño or not color or not precio:
            messagebox.showwarning("Error", "Por favor completa todos los campos.")
            return

        data = {
            "marca": marca,
            "tamaño": tamaño,
            "color": color,
            "precio": precio
        }

        #url
        url = 'http://127.0.0.1:8000/v1/bafle'

        try:
            response = requests.post(url, json=data)
            if response.status_code == 201:  
                messagebox.showinfo("Exito", "Información creada con exito")
            else:
                messagebox.showerror("Error", f"Error al agregar la información sobre el bafle: {response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}") 

            
    def validarLetras(entrada):
        return re.match("^[a-zA-Z ]*$", entrada) is not None

    def mostrar_advertencia1(event):
            nuevoValor = event.widget.get()
            if not nuevoValor:
                event.widget.lblAdvertencia1.grid_remove() 
            elif not re.match("^[a-zA-Z0-9 ]*$", nuevoValor):
                event.widget.lblAdvertencia1.grid(row=6, column=1) 
            else:
                event.widget.lblAdvertencia1.grid_remove() 
                
    def mostrar_advertencia2(event):
            nuevoValor = event.widget.get()
            if not nuevoValor or re.match("^[a-zA-Z ]*$", nuevoValor):
                event.widget.lblAdvertencia2.grid_remove()
            else:
                event.widget.lblAdvertencia2.grid(row=4, column=1)
                
    def mostrar_advertencia3(event):
            nuevoValor = event.widget.get()
            if not nuevoValor:
                event.widget.lblAdvertencia.grid_remove() 
            elif not re.match("^[a-zA-Z0-9 ]*$", nuevoValor):
                event.widget.lblAdvertencia3.grid(row=6, column=1) 
            else:
                event.widget.lblAdvertencia3.grid_remove() 
            
    def mostrar_advertencia4(event):
            nuevoValor = event.widget.get()
            if not re.match("^[a-zA-Z0-9 ]*$", nuevoValor):
                VistasBafle.txtLocal.lblAdvertencia4.grid(row=8, column=1) 
            else:
                VistasBafle.txtLocal.lblAdvertencia4.grid_remove() 
    