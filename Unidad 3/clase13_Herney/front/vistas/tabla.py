import tkinter
from tkinter import ttk

class Tabla():
    def __init__(self, ventanaPrincipal, titulos, columnas, data):
        self.tabla = ttk.Treeview(ventanaPrincipal, columns=columnas, show='headings')
        for posicion in range (0, len(columnas)):
            self.tabla.heading(columnas[posicion], text=titulos[posicion])
        for elemento in data:
            self.tabla.insert(parent='',index=0, values=elemento)
            
    def refrescar(self, data):
        self.tabla.delete(*self.tabla.get_children())
        for elemento in data:
            self.tabla.insert(parent='', index=0, values=elemento)