import tkinter as tk
from tkinter import *
from tkinter import messagebox
import re

principal =tk.Tk()
principal.title('Datos')
principal.geometry("350x400")

def validarLetras(entrada):
    #Patrón para aceptar solo letras (mayúsculas y minúsculas) y espacios todo lo demas esta restringido y validar nombre debe de dar True
    return re.match("^[a-zA-Z ]*$", entrada) is not None

def validarNombre(event=None):
    nuevoValor = txtNombre.get() # Obtener el valor de la caja de texto
    if nuevoValor == "":
        lblAdvertencia.grid_remove() # Ocultar el Label de advertencia si la entrada es vacía
        return True
    elif validarLetras(nuevoValor):
        lblAdvertencia.grid_remove() # Ocultar el Label de advertencia si la entrada es válida
        return True
    else:
        lblAdvertencia.grid(row=2, column=1) # Mostrar el Label de advertencia
        print(f'Caracter {nuevoValor} no es valido')
        return False
    

#Validar el campo de los apellidos
def validarLetrasApellido(entrada):
    #Patrón para aceptar solo letras (mayúsculas y minúsculas) y espacios todo lo demas esta restringido y validar nombre debe de dar True
    return re.match("^[a-zA-Z ]*$", entrada) is not None

def validarApellido(nuevoValor):
    nuevoValor = txtApellido.get() # Obtener el valor de la caja de texto
    if nuevoValor == "":
        lblAdvertencia1.grid_remove() # Ocultar el Label de advertencia si la entrada es vacía
        return True
    elif validarLetras(nuevoValor):
        lblAdvertencia1.grid_remove() # Ocultar el Label de advertencia si la entrada es válida
        return True
    else:
        lblAdvertencia1.grid(row=4,column=1)# Mostrar el Label de advertencia
        print(f'Caracter {nuevoValor} no es valido')
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
    
def validarEntrada(text):
    return all(c.isalpha() or c.isdigit() or c in ".@" for c in text) or text == ""

def validarTecla(event):
    if event.keysym != "BackSpace" and not validarEntrada(event.char):
        print(f"El caracter {event.char} no es valido en este campo")
        return "break"




frame = tk.Frame(principal, padx=10, pady=10)
lblTitulo = tk.Label(frame, text='Complete los campos')
lblTitulo.grid(row=0, column=0, columnspan=2) 


lblNombre = tk.Label(frame, text='Nombre:')
lblNombre.grid(row=1, column=0, padx=5, pady=10)
lblAdvertencia = tk.Label(frame, text='Solo se permiten letras')
#lblAdvertencia.grid(row=2,column=1)
lblApellido = tk.Label(frame, text='Apellido:')
lblApellido.grid(row=3, column=0, padx=5, pady=10)
lblAdvertencia1 = tk.Label(frame, text='Solo se permiten letras')
#lblAdvertencia1.grid(row=4,column=1)
lblEdad = tk.Label(frame, text='Edad:')
lblEdad.grid(row=5,column=0, padx=5, pady=10)
lblAdvertencia2 = tk.Label(frame, text='Solo se permiten numeros')
lblAdvertencia2.grid(row=6,column=1)
lblCorreoElectronico = tk.Label(frame, text='Correo Electrónico:')
lblCorreoElectronico.grid(row=7, column=0, padx=5, pady=10)
lblAdvertencia3 = tk.Label(frame, text='Solo se permiten(Aa, ., 0-9 ,@)')
lblAdvertencia3.grid(row=8,column=1)
lblFechaNacimiento = tk.Label(frame, text='Fecha Nacimiento:')
lblFechaNacimiento.grid(row=9, column=0, padx=5, pady=10)
lblAdvertencia4 = tk.Label(frame, text='Solo se permiten Numeros y "/"')
lblAdvertencia4.grid(row=10,column=1)

txtNombre = tk.Entry(frame, width=20)
txtNombre.grid(row=1,column=1, padx=5, pady=10)  
txtApellido = tk.Entry(frame, width=20)
txtApellido.grid(row=3,column=1, padx=5, pady=10)
txtEdad = tk.Entry(frame, width=20)
txtEdad.grid(row=5,column=1, padx=5, pady=10)  
txtCorreoElectronico = tk.Entry(frame, width=20)
txtCorreoElectronico.grid(row=7,column=1, padx=5, pady=10)  
txtFechaNacimiento = tk.Entry(frame, width=20)
txtFechaNacimiento.grid(row=9,column=1, padx=5, pady=10)  

#Unir las validaciones a el campo de texto

'''validacion = principal.register(validarNombre)
txtNombre.config(validate='key',validatecommand=(validacion, '%P'))'''
txtNombre.bind('<KeyRelease>', validarNombre)

validacion = principal.register(validarEdad)
txtEdad.config(validate="key", validatecommand=(validacion, '%P'))

'''validacion = principal.register(validarApellido)
txtApellido.config(validate='key',validatecommand=(validacion, '%P'))'''
txtApellido.bind('<KeyRelease>', validarApellido)


'''validacion = principal.register(validarFecha)
txtFechaNacimiento.config(validate='key', validatecommand=(validacion, '%P'))'''

txtFechaNacimiento.bind("<Key>", cuandoEscriba)
txtFechaNacimiento.bind("<BackSpace>", lambda _:txtFechaNacimiento.delete(tk.END))

txtCorreoElectronico.bind("<Key>", validarTecla)



frame.pack(padx=10, pady=10)


principal.mainloop()

