import requests
from tkinter import messagebox
import re
#from controladores.peticiones import Peticiones


class Validaciones():
    def __init__(self):
        pass
            
    def validar_entrada(entrada):
        if not entrada or re.match("^[a-zA-Z ]*$", entrada):
            return True
        else:
            return False

    def mostrar_advertencia_nombre(event):
        nuevoValor = event.widget.get()
        if not nuevoValor or re.match("^[a-zA-Z ]*$", nuevoValor):
            event.widget.lblAdvertencia.grid_remove()
        else:
            event.widget.lblAdvertencia.grid(row=2, column=1)

    def mostrar_advertencia_apellido(event):
        nuevoValor = event.widget.get()
        if not nuevoValor or re.match("^[a-zA-Z ]*$", nuevoValor):
            event.widget.lblAdvertencia1.grid_remove()
        else:
            event.widget.lblAdvertencia1.grid(row=5, column=1)

    def mostrar_advertencia_cedula(event):
        nuevoValor = event.widget.get()
        if not nuevoValor:
            event.widget.lblAdvertencia.grid_remove() 
        elif not re.match("^[0-9]*$", nuevoValor):
            event.widget.lblAdvertencia.grid(row=8, column=1) 
        else:
            event.widget.lblAdvertencia.grid_remove() 

    def mostrar_advertencia_telefono(event):
        nuevoValor = event.widget.get()
        if not nuevoValor:
            event.widget.lblAdvertencia.grid_remove() 
        elif not re.match("^[0-9]*$", nuevoValor):
            event.widget.lblAdvertencia.grid(row=11, column=1) 
        else:
            event.widget.lblAdvertencia.grid_remove() 

    def mostrar_advertencia_correo(event):
        nuevoValor = event.widget.get()
        # Expresión regular mejorada para validar correos electrónicos
        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not nuevoValor:
            event.widget.lblAdvertencia.grid_remove()
        elif re.match(patron, nuevoValor):
            event.widget.lblAdvertencia.grid_remove()
        else:
            event.widget.lblAdvertencia.grid(row=14, column=1)
    
