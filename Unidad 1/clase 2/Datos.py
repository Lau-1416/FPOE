import tkinter as tk
from tkinter import *
from tkinter import messagebox


principal = Tk()
principal.title('Datos')


frame = Frame(principal, width=500, height=500)
lblTitulo = tk.Label(frame,text='Ingresar Datos')
lblNombre = tk.Label(frame, text='Nombre:')
lblNombre.grid(row=3, column=0)
lblApellido = tk.Label(frame, text='Apellido:')
lblApellido.grid(row=4, column=0)
lblTelefono = tk.Label(frame, text='Edad:')
lblTelefono.grid(row=5,column=0)
lblCorreoElectronico = tk.Label(frame, text='Correo Electrónico')
lblCorreoElectronico.grid(row=6, column=0)
lblFechaNacimiento = tk.Label(frame, text='Fecha Nacimiento')
lblFechaNacimiento.grid(row=7, column=0)

txtCedula = tk.Entry(frame, width=20)
txtCedula.grid(row=2,column=1)
txtNombre = tk.Entry(frame, width=20)
txtNombre.grid(row=3,column=1)
txtApellido = tk.Entry(frame, width=20)
txtApellido.grid(row=4,column=1)
txtTelefono = tk.Entry(frame, width=20)
txtTelefono.grid(row=5,column=1)
txtCorreoElectronico = tk.Entry(frame, width=20)
txtCorreoElectronico.grid(row=6,column=1)

frame.pack()

principal.mainloop()





