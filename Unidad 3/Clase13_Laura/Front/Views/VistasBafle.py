import tkinter as tk
import re
from tkinter import messagebox
from Front.Controller.Validaciones import Validaciones
from Front.Controller.Peticiones import Peticiones
from Front.Controller.Comunicacion import Comunicacion
from Front.Models import Bafle
from Front.Views.Tabla import Tabla
from functools import partial

def interfaz():
    titulos = ['Identificador', 'Marca', 'Tamaño', 'Color', 'Precio']
    columnas = ['id', 'Marca', 'Tamaño', 'Color', 'Precio']
    data = []
    ventana_principal = tk.Tk()
    comunicacion = Comunicacion(ventana_principal)
    tabla = Tabla(ventana_principal, titulos, columnas, data)
    pass
        
def Comunicacion_ConsultaBoton(lblConsultaPrecio, id):
    resultado = Comunicacion.consultar(id)
    print(resultado)
    print(type(resultado))
    lblConsultaPrecio.config(text = resultado.get())
    
def Comunicacion_ConsultarTodo(self, marca, tamaño, color, precio):
    resultado = self.Comunicacion.ConsultarTodo(marca, tamaño, color, precio) 
    data = [] 
    for elemento in resultado: 
        data.append((elemento.get('id'), elemento.get('marca'), elemento.get('tamaño'), elemento.get('color'), elemento.get('precio'))) 
    self.tabla.refrescar(data)
    print(resultado)
    print(type(resultado))
    Comunicacion.ConsultarTodo(text = resultado.get())
    
'''def seleccionar_elemento(_):
    for i in tabla.tabla.selection():
        valores = tabla.tabla.item(i)['values']
        entryId.delete(0, tk.END)
        entryId.insert(0, str(valores[0]))
        entryTema.delete(0, tk.END)
        entryTema.insert(0, str(valores[1]))
        entryDescripcion.delete(0, tk.END)
        entryDescripcion.insert(0, str(valores[2]))
        entryNumero.delete(0, tk.END)
        entryNumero.insert(0, str(valores[3]))

def borrar_elemento(_):
    for i in self.tabla.tabla.selection():
        self.comunicacion.eliminar(self.tabla.tabla.item(i)['values'][0])
        self.tabla.tabla.delete(i)'''

    
        
def Peticion_ingresar_bafle():
    Peticiones.ingresar_bafle(txtMarca, txtTamaño, txtColor, txtPrecio)
    
ventana_principal = tk.Tk()
ventana_principal.title('Bafle')
ventana_principal.geometry("300x350")  

frame = tk.Frame(ventana_principal, padx=10, pady=10)
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

lblId = tk.Label(frame, text='ID:')
lblId.grid(row=9, column=0, padx=5, pady=5)

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

txtId= tk.Entry(frame, text='ID:')
txtId.grid(row=9, column=1, padx=5, pady=5)

def ingresar_bafle():
    marca = txtMarca.get(),
    tamaño = txtTamaño.get(),
    color = txtColor.get(),
    precio = txtPrecio.get(),
    id = txtId.get()
    messagebox.showinfo("Información de Bafle", f"Marca: {marca}\nTamaño: {tamaño}\nColor: {color}\nPrecio: {precio}")
    
txtMarca.bind('<KeyRelease>', Validaciones.Advertencia1)
txtTamaño.bind('<KeyRelease>', Validaciones.Advertencia2)
txtColor.bind('<KeyRelease>', Validaciones.Advertencia3)
txtPrecio.bind('<KeyRelease>', Validaciones.Advertencia4)


btnIngresar = tk.Button(frame, text='Ingresar', command=Peticion_ingresar_bafle)
btnIngresar.grid(row=10, column=1, columnspan=2)


btnConsultas = tk.Button(frame, text='Consultar', command=Comunicacion_ConsultaBoton)
btnConsultas.grid(row=14, column=1, columnspan=2)


btnConsultartodo = tk.Button(frame, text='Consultar Todo', command=partial(Comunicacion_ConsultarTodo, txtMarca, txtTamaño, txtColor, txtPrecio, txtId))
btnConsultartodo.grid(row=16, column=1, columnspan=2)


ventana_principal.mainloop()
