import tkinter as tk
from tkinter import ttk
import requests

class LavelopuesApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Lavelopues S.A.S.")
        self.ventana.geometry('800x800')
        
        tk.Label(self.ventana, text="Nombre:").grid(row=0, column=0)
        self.txtNombre = tk.Entry(self.ventana)
        self.txtNombre.grid(row=1, column=0)
        
        tk.Label(self.ventana, text="Apellido:").grid(row=2, column=0)
        self.txtApellido = tk.Entry(self.ventana)
        self.txtApellido.grid(row=3, column=0)
        
        tk.Label(self.ventana, text="Cedula:").grid(row=4, column=0)
        self.txtCedula = tk.Entry(self.ventana)
        self.txtCedula.grid(row=5, column=0)
        
        tk.Label(self.ventana, text="Telefono:").grid(row=6, column=0)
        self.txtTelefono = tk.Entry(self.ventana)
        self.txtTelefono.grid(row=7, column=0)
        
        tk.Label(self.ventana, text="Correo:").grid(row=8, column=0)
        self.txtCedula = tk.Entry(self.ventana)
        self.txtCedula.grid(row=9, column=0)

 
if __name__ == "__main__":
    ventana = tk.Tk()
    app = LavelopuesApp(ventana)
    ventana.mainloop()