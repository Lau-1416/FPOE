import tkinter as tk
import re
from tkinter import messagebox
from Front.Controller.Validaciones import Validaciones
from Front.Controller.Peticiones import Peticiones

def Peticion_ingresar_bafle():
    Peticiones.ingresar_universidad(txtMarca, txtTamaño, txtColor, txtPrecio)
    
principal = tk.Tk()
principal.title('Bafle')
principal.geometry("300x250")  

frame = tk.Frame(principal, padx=10, pady=10)
frame.pack()  

lblTitulo = tk.Label(frame, text='Ingresar Datos')
lblTitulo.grid(row=0, column=0, columnspan=2) 

lblMarca = tk.Label(frame, text='Marca:')
lblMarca.grid(row=1, column=0, padx=5, pady=5)  
lblTamaño = tk.Label(frame, text='Tamaño:')
lblTamaño.grid(row=3, column=0, padx=5, pady=5)
lblColor = tk.Label(frame, text='Color:')
lblColor.grid(row=5, column=0, padx=5, pady=5)
lblPrecio = tk.Label(frame, text='Precio:')
lblPrecio.grid(row=7, column=0, padx=5, pady=5)

txtMarca = tk.Entry(frame, width=20)
txtMarca.grid(row=1, column=1, padx=5, pady=5)  
txtMarca.lblAdvertencia1 = tk.Label(frame, text='Solo se permiten letras y números', fg="red")
txtMarca.lblAdvertencia1.grid(row=2, column=1, sticky="w")
txtMarca.lblAdvertencia1.grid_remove()

txtTamaño = tk.Entry(frame, width=20)
txtTamaño.grid(row=3, column=1, padx=5, pady=5)
txtTamaño.lblAdvertencia2 = tk.Label(frame, text='Solo se permiten letras y números', fg="red")
txtTamaño.lblAdvertencia2.grid(row=4, column=1, sticky="w")
txtTamaño.lblAdvertencia2.grid_remove()

txtColor = tk.Entry(frame, width=20)
txtColor.grid(row=5, column=1, padx=5, pady=5)  
txtColor.lblAdvertencia3 = tk.Label(frame, text='Solo se permiten letras', fg="red")
txtColor.lblAdvertencia3.grid(row=6, column=1, sticky="w")
txtColor.lblAdvertencia3.grid_remove()

txtPrecio = tk.Entry(frame, width=20)
txtPrecio.grid(row=7, column=1, padx=5, pady=5)
txtPrecio.lblAdvertencia4 = tk.Label(frame, text='Solo se permiten números', fg="red")
txtPrecio.lblAdvertencia4.grid(row=8, column=1, sticky="w")
txtPrecio.lblAdvertencia4.grid_remove()

def ingresar_bafle():
    marca = txtMarca.get()
    tamaño = txtTamaño.get()
    color = txtColor.get()
    precio = txtPrecio.get()
    messagebox.showinfo("Información de Bafle", f"Marca: {marca}\nTamaño: {tamaño}\nColor: {color}\nPrecio: {precio}")
    
txtMarca.bind('<KeyRelease>', Validaciones.Advertencia1)
txtTamaño.bind('<KeyRelease>', Validaciones.Advertencia2)
txtColor.bind('<KeyRelease>', Validaciones.Advertencia3)
txtPrecio.bind('<KeyRelease>', Validaciones.Advertencia4)

btnIngresar = tk.Button(frame, text='Ingresar', command=Peticion_ingresar_bafle)
btnIngresar.grid(row=10, column=1, columnspan=2, pady=10)

principal.mainloop()
