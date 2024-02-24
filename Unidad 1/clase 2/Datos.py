import tkinter as tk
from tkinter import *
from tkinter import messagebox
import re

principal =tk.Tk()
principal.title('Datos')
principal.geometry("240x220")

def validarLetras(entrada):
    #Patrón para aceptar solo letras (mayúsculas y minúsculas) y espacios todo lo demas esta restringido y validar nombre debe de dar True
    return re.match("^[a-zA-Z ]*$", entrada) is not None

def validarNombre(nuevo_valor):
    # Solo permitir la entrada si la función de validación de letras devuelve True
    if validarLetras(nuevo_valor) or nuevo_valor == "":
        return True
    else:
        return False
    
def validar_numeros(entrada):
    return re.match("^[0-99]*$", entrada) is not None and len(entrada) <= 2

def validarEdad(nueva_edad):
    if validar_numeros(nueva_edad) or nueva_edad == "":
        return True
    else:
        return False


frame = tk.Frame(principal, padx=10, pady=10)
lblTitulo = tk.Label(frame, text='Ingresar Datos')
lblTitulo.grid(row=0, column=0, columnspan=2) 


lblNombre = tk.Label(frame, text='Nombre:')
lblNombre.grid(row=1, column=0, padx=5, pady=5)  
lblApellido = tk.Label(frame, text='Apellido:')
lblApellido.grid(row=2, column=0, padx=5, pady=5)
lblEdad = tk.Label(frame, text='Edad:')
lblEdad.grid(row=3,column=0, padx=5, pady=5)
lblCorreoElectronico = tk.Label(frame, text='Correo Electrónico:')
lblCorreoElectronico.grid(row=4, column=0, padx=5, pady=5)
lblFechaNacimiento = tk.Label(frame, text='Fecha Nacimiento:')
lblFechaNacimiento.grid(row=5, column=0, padx=5, pady=5)

txtNombre = tk.Entry(frame, width=20)
txtNombre.grid(row=1,column=1, padx=5, pady=5)  
txtApellido = tk.Entry(frame, width=20)
txtApellido.grid(row=2,column=1, padx=5, pady=5)
txtEdad = tk.Entry(frame, width=20)
txtEdad.grid(row=3,column=1, padx=5, pady=5)  
txtCorreoElectronico = tk.Entry(frame, width=20)
txtCorreoElectronico.grid(row=4,column=1, padx=5, pady=5)  
txtFechaNacimiento = tk.Entry(frame, width=20)
txtFechaNacimiento.grid(row=5,column=1, padx=5, pady=5)  

#Unir las validaciones a el campo de texto

validacion = principal.register(validarNombre)
txtNombre.config(validate='key',validatecommand=(validacion, '%P'))

validacion = principal.register(validarEdad)
txtEdad.config(validate="key", validatecommand=(validacion, '%P'))

frame.pack(padx=10, pady=10)


principal.mainloop()

