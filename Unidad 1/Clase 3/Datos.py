import tkinter as tk
from tkinter import *
from tkinter import messagebox
import re
from tkcalendar import Calendar
from tkcalendar import DateEntry

principal =tk.Tk()
principal.title('Datos')
principal.geometry("420x400")

frame = tk.Frame(principal, padx=10, pady=10)
lblTitulo = tk.Label(frame, text='Complete los campos')
lblTitulo.grid(row=0, column=0, columnspan=2) 

lblAdvertencia = tk.Label(frame, text='Solo se permiten letras',fg="red")
lblAdvertencia.grid(row=2,column=1, sticky="w")
lblAdvertencia.grid_remove()

lblAdvertencia1 = tk.Label(frame, text='Solo se permiten letras',fg="red")
lblAdvertencia1.grid(row=4,column=1, sticky="w")
lblAdvertencia1.grid_remove()

lblAdvertencia2 = tk.Label(frame, text='Solo se permiten numeros',fg="red")
lblAdvertencia2.grid(row=6,column=1, sticky="w")
lblAdvertencia2.grid_remove()

lblAdvertencia3 = tk.Label(frame, text='Solo se permiten(Aa, ., 0-9 ,@)',fg="red")
lblAdvertencia3.grid(row=8,column=1, sticky="w")
lblAdvertencia3.grid_remove()

lblAdvertencia4 = tk.Label(frame, text='Solo se permiten Numeros y "/"', fg="red")
lblAdvertencia4.grid(row=10,column=1, sticky="w")
lblAdvertencia4.grid_remove()

def mostrarBoton():
    btnFormularioMal.grid(row=12, columnspan=2, pady=10)
    
def mostrarMensaje():
    messagebox.showerror("Error", "¡El formulario no es válido!")

def ocultarBoton():
    btnFormularioMal.grid_remove()


def validarLetras(entrada):
    return re.match("^[a-zA-Z ]*$", entrada) is not None

def validarNombre(event=None):
    nuevoValor = txtNombre.get()
    if nuevoValor == "":
        lblAdvertencia.grid_remove()
        ocultarBoton()
        return True 
    elif validarLetras(nuevoValor):
        lblAdvertencia.grid_remove()
        ocultarBoton()
        return True
    else:
        lblAdvertencia.grid(row=2, column=1)
        mostrarBoton()
        return False
    
def validarLetrasApellido(entrada):
    return re.match("^[a-zA-Z ]*$", entrada) is not None

def validarApellido(event=None):
    nuevoValor = txtApellido.get()
    if nuevoValor == "":
        lblAdvertencia1.grid_remove()
        ocultarBoton()
        return True
    elif validarLetrasApellido(nuevoValor):
        lblAdvertencia1.grid_remove()
        ocultarBoton()
        return True
    else:
        lblAdvertencia1.grid(row=4,column=1)
        mostrarBoton()
        return False

def validar_numeros(entrada):
    return re.match("^[0-9]{1,2}$", entrada) is not None and len(entrada) <= 2

def validarEdad(event=None):
    nueva_edad = txtEdad.get()
    if nueva_edad == '':
        lblAdvertencia2.grid_remove()
        ocultarBoton()
        return True
    elif validar_numeros(nueva_edad):
        lblAdvertencia2.grid_remove()
        ocultarBoton()
        return True
    else:
        lblAdvertencia2.grid(row=6,column=1)
        mostrarBoton()
        return False
    
def validarCorreoElectronico(event=None):
    email = txtCorreoElectronico.get()
    if email == '':
        lblAdvertencia3.grid_remove()
        ocultarBoton()
        return True
    elif re.match(r'^[a-zA-Z0-9.@]+$', email):
        lblAdvertencia3.grid_remove()
        ocultarBoton()
        return True
    else:
        lblAdvertencia3.grid(row=8, column=1)
        mostrarBoton()
        return False
    
def cuandoEscriba(event):
    if event.char and event.char.isdigit():
        texto = txtFechaNacimiento.get()
        letras = 0
        for i in texto:
            letras += 1

        if letras == 2:
            if int(txtFechaNacimiento.get()[:2]) > 31:
                print("El día debe estar entre 01 y 31")
                lblAdvertencia4.grid_remove()
                mostrarBoton()
                return "break"
            txtFechaNacimiento.insert(2, "/")
        elif letras == 5:
            if int(txtFechaNacimiento.get()[3:5]) > 12:
                print("El mes debe estar entre 01 y 12")
                lblAdvertencia4.grid_remove()
                mostrarBoton()
                return "break"
            txtFechaNacimiento.insert(5, "/")
        elif letras == 10:
            txtFechaNacimiento.delete(10, tk.END)  # Limitar la entrada a 10 caracteres
            ocultarBoton()
        else:
            lblAdvertencia4.grid_remove()
            ocultarBoton()
    elif event.char == '':
        return 
    else:
        print(f'El caracter {event.char} no es válido en este campo')
        lblAdvertencia4.grid(row=10, column=1)
        mostrarBoton()
        return "break"

def avisoFormulario():
    messagebox.showinfo('Verificación', 'Formulario completado correctamente')

def validarFormulario():
    if (validarNombre() and validarApellido() and validarEdad() and validarCorreoElectronico()):
        mostrarBotonFormularioBien()
    else:
        ocultarBotonFormularioBien()

def mostrarMensajeExito():
    messagebox.showinfo("Éxito", "¡El formulario está completo y correcto!")

def mostrarBotonFormularioBien():
    if (txtNombre.get() and txtApellido.get() and txtEdad.get() and txtCorreoElectronico.get() and txtFechaNacimiento.get()):
        ocultarBoton()
        btnFormularioBien.grid(row=12, columnspan=2, pady=10)

def ocultarBotonFormularioBien():
    btnFormularioBien.grid_remove()

lblNombre = tk.Label(frame, text='Nombre:')
lblNombre.grid(row=1, column=0, padx=5, pady=10)
lblApellido = tk.Label(frame, text='Apellido:')
lblApellido.grid(row=3, column=0, padx=5, pady=10)
lblEdad = tk.Label(frame, text='Edad:')
lblEdad.grid(row=5,column=0, padx=5, pady=10)
lblCorreoElectronico = tk.Label(frame, text='Correo Electrónico:')
lblCorreoElectronico.grid(row=7, column=0, padx=5, pady=10)
lblFechaNacimiento = tk.Label(frame, text='Fecha Nacimiento:')
lblFechaNacimiento.grid(row=9, column=0, padx=5, pady=10)

txtNombre = tk.Entry(frame, width=20)
txtNombre.grid(row=1,column=1, padx=5, pady=10)  
txtApellido = tk.Entry(frame, width=20)
txtApellido.grid(row=3,column=1, padx=5, pady=10)
txtEdad = tk.Entry(frame, width=20)
txtEdad.grid(row=5,column=1, padx=5, pady=10)  
txtCorreoElectronico = tk.Entry(frame, width=20)
txtCorreoElectronico.grid(row=7,column=1, padx=5, pady=10)  
txtFechaNacimiento = DateEntry(frame, date_pattern='dd/mm/yyyy', show_week_numbers=False)
txtFechaNacimiento.grid(row=9,column=1,padx=5, pady=10)

frame.pack(padx=10, pady=10)

btnFormularioMal = tk.Button(frame, text="Formulario Mal", command=mostrarMensaje)
btnFormularioBien = tk.Button(frame, text="Formulario Bien", command= mostrarMensajeExito)


txtNombre.bind('<KeyRelease>', lambda event: (validarNombre(), validarFormulario()))
txtApellido.bind('<KeyRelease>', lambda event: (validarApellido(), validarFormulario()))
txtEdad.bind('<KeyRelease>', lambda event: (validarEdad(), validarFormulario()))
txtCorreoElectronico.bind('<KeyRelease>', lambda event: (validarCorreoElectronico(), validarFormulario()))
txtFechaNacimiento.bind("<KeyRelease>", lambda event: (cuandoEscriba(event), validarFormulario()))
txtFechaNacimiento.bind("<BackSpace>", lambda event: (txtFechaNacimiento.delete(tk.END), validarFormulario()))

principal.mainloop()