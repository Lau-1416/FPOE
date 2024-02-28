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

def validarNombre(nuevoValor):
    # Solo permitir la entrada si la función de validación de letras devuelve True
    if validarLetras(nuevoValor) or nuevoValor == "":
        return True
    else:
        print(f'El caracter {nuevoValor} no esta permitido')
        return False
    

#Validar el campo de los apellidos
def validarLetrasApellido(entrada):
    #Patrón para aceptar solo letras (mayúsculas y minúsculas) y espacios todo lo demas esta restringido y validar nombre debe de dar True
    return re.match("^[a-zA-Z ]*$", entrada) is not None

def validarApellido(nuevoValor):
    # Solo permitir la entrada si la función de validación de letras devuelve True
    if validarLetras(nuevoValor) or nuevoValor == "":
        return True
    else:
        print(f'El caracter {nuevoValor} no esta permitido')
        return False
    

def validar_numeros(entrada):
    return re.match("^[0-99]*$", entrada) is not None and len(entrada) <= 2

def validarEdad(nueva_edad):
    if validar_numeros(nueva_edad) or nueva_edad == "":
        return True
    else:
        print(f'El carcter {nueva_edad} no es valido en este campo')
        return False
    
'''def validarNumerosFecha(entrada):
    return re.match("^[0-9/]*$", entrada) is not None'''

'''def validarFecha(nuevaFecha):
    # Patrón para aceptar fechas en el formato DD/MM/AAAA
    if re.match("^[\d/]{1,10}$", nuevaFecha):
        return True
    else:
        print(f'Carácter no permitido: {"".join(c for c in nuevaFecha if not c.isdigit() and c != "/")}')
        return False'''

def cuandoEscriba(event):
    if event.char.isdigit():
        texto = txtFechaNacimiento.get()
        letras = 0
        for i in texto:
            letras += 1

        if letras == 2:
            if int(txtFechaNacimiento.get()[:2]) > 31:  # Verificar día
                print("El día debe estar entre 01 y 31")
                return "break"
            txtFechaNacimiento.insert(2, "/")
        elif letras == 5:
            if int(txtFechaNacimiento.get()[3:5]) > 12:  # Verificar mes
                print("El mes debe estar entre 01 y 12")
                return "break"
            txtFechaNacimiento.insert(5, "/")
    else:
        print(f'El caracter {event.char} no es valido en este campo')
        return "break"




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

validacion = principal.register(validarApellido)
txtApellido.config(validate='key',validatecommand=(validacion, '%P'))

'''validacion = principal.register(validarFecha)
txtFechaNacimiento.config(validate='key', validatecommand=(validacion, '%P'))'''

txtFechaNacimiento.bind("<Key>", cuandoEscriba)
txtFechaNacimiento.bind("<BackSpace>", lambda _:txtFechaNacimiento.delete(tk.END))




frame.pack(padx=10, pady=10)


principal.mainloop()

