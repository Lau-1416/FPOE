import requests
from tkinter import messagebox
from vistas import vistaUniversidad
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

    def mostrar_advertencia(event):
        nuevoValor = event.widget.get()
        if not nuevoValor or re.match("^[a-zA-Z ]*$", nuevoValor):
            event.widget.lblAdvertencia.grid_remove()
        else:
            event.widget.lblAdvertencia.grid(row=2, column=1)

    def mostrar_advertencia1(event):
        nuevoValor = event.widget.get()
        if not nuevoValor or re.match("^[a-zA-Z ]*$", nuevoValor):
            event.widget.lblAdvertencia1.grid_remove()
        else:
            event.widget.lblAdvertencia1.grid(row=4, column=1)

    def mostrar_advertencia_salon(event):
        nuevoValor = event.widget.get()
        if not nuevoValor:
            event.widget.lblAdvertencia.grid_remove() 
        elif not re.match("^[a-zA-Z0-9 ]*$", nuevoValor):
            event.widget.lblAdvertencia.grid(row=6, column=1) 
        else:
            event.widget.lblAdvertencia.grid_remove() 

    def mostrar_advertencia_local(event):
        nuevoValor = event.widget.get()
        if not re.match("^[a-zA-Z0-9 ]*$", nuevoValor):
            vistaUniversidad.txtLocal.lblAdvertencia.grid(row=8, column=1) 
        else:
            vistaUniversidad.txtLocal.lblAdvertencia.grid_remove() 