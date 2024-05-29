import tkinter as tk
from tkinter import ttk

class Tabla():
    def __init__(self, ventana_principal, titulos, columnas, data):
        self.tabla = ttk.Treeview(ventana_principal, columns=columnas, show='headings')
        for posicion in range(0, len(columnas)):
            self.tabla.heading(columnas[posicion], text=titulos[posicion])
        for elemento in data:
            self.tabla.insert(parent='', index=0, values=elemento)
            
    def refrescar(self, data):
            print(*self.tabla.get_children())
            self.tabla.delete(*self.tabla.get_children())
            for elemento in data:
                self.tabla.insert(parent='', index=tk.END, values=elemento)