import tkinter as tk

class Bafle():
    
    def __init__(self, ventana_principal, id):
        self.ventana_principal = ventana_principal
        self.id = id
        self.marca = tk.StringVar(ventana_principal)
        self.tamaño = tk.StringVar(ventana_principal)
        self.color = tk.StringVar(ventana_principal)
        self.precio = tk.StringVar(ventana_principal)
        