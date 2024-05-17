import requests
from tkinter import messagebox
from Front.Controller.Validaciones import Validaciones
from Front.Views import VistasBafle

class Peticiones():
    def ingresar_bafle(txtMarca, txtTamaño, txtColor, txtPrecio):
        marca = txtMarca.get()
        tamaño = txtTamaño.get()
        color = txtColor.get()
        precio = txtPrecio.get()

        if not marca or not tamaño or not color or not precio:
            messagebox.showwarning("Error", "Por favor completa todos los campos.")
            return
        
        if (txtMarca.lblAdvertencia1.winfo_viewable() or
            txtTamaño.lblAdvertencia2.winfo_viewable() or
            txtColor.lblAdvertencia3.winfo_viewable() or
            txtPrecio.lblAdvertencia4.winfo_viewable()):
            messagebox.showwarning("Error", "Por favor completa todos los campos correctamente.")
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
