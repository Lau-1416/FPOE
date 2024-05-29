import tkinter as tk

class Usuario():
        
    def __init__(self, ventanaPrincipal):
        self.ventanaPrincipal = ventanaPrincipal
        self.material = tk.StringVar(ventanaPrincipal)
        self.color = tk.StringVar(ventanaPrincipal)
        self.talla = tk.StringVar(ventanaPrincipal)
        self.marca =tk.StringVar(ventanaPrincipal)

