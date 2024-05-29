import tkinter as tk
import re
from tkinter import messagebox
from Front.Controller.Validaciones import Validaciones
from Front.Controller.Comunicacion import Comunicacion
from Front.Models.Bafle import Bafle
from Front.Views.Tabla import Tabla
from functools import partial

class VistasBafle():
    def __init__(self):
        titulos = ['ID', 'Marca', 'Tamaño', 'Color', 'Precio']
        columnas = ['id', 'marca', 'tamaño', 'color', 'precio']
        data = []
        self.frame = tk.Tk()
        self.Comunicacion = Comunicacion()
        self.tabla = Tabla(self.frame, titulos, columnas, data)
        pass
    
    def BotonGuardar(self, id, marca, tamaño, color, precio):
        if id == '':
            self.Comunicacion.guardar(marca, tamaño, color, precio)
        else:
            self.Comunicacion.actualizar(id, marca, tamaño, color, precio)
    
    def ConsultarTodo(self, marca, tamaño, color, precio):
        resultado = self.Comunicacion.ConsultarTodo(marca, tamaño, color, precio)
        data = []
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('marca'), elemento.get('tamaño'), elemento('color'), elemento('precio')))
        self.tabla.refrescar(data)
    
    def ConsultarBoton(self, lblConsultaMarca, lblConsultaPrecio):
        resultado = self.Comunicacion.consultar(id)
        print(resultado)
        print(type(resultado))
        lblConsultaMarca.config(text=resultado.get('marca'))
        lblConsultaPrecio.config(text=resultado.get('precio'))
            
    def ver_interfaz(self):
        bafle = Bafle(self.frame, id)
        
        lblId = tk.Label(self.frame, text="id")
        lblId = tk.Entry(self.frame, width=20)
        lblId.pack()
    
        lblMarca = tk.Label(self.frame, text="Marca")
        lblMarca.pack()
        
        lblTamaño = tk.Label(self.frame, text="Tamaño")
        lblTamaño.pack()
        
        lblColor = tk.Label(self.frame, text="Color")
        lblColor.pack()
        
        lblPrecio = tk.Label(self.frame, text="Precio")
        lblPrecio.pack()
        
        lblConsultaMarca = tk.Label(self.frame, text='')
        lblConsultaMarca.pack()
        lblConsultaPrecio = tk.Label(self.frame, text='')
        lblConsultaPrecio.pack()
        
        btnGuardar = tk.Button(self.frame, text='Guardar', command=lambda: self.BotonGuardar(lblId.get(), lblMarca.get(), lblTamaño.get(), lblColor.get(), lblPrecio.get()))
        btnGuardar.pack()
        
        btnConsultar = tk.Button(self.frame, text= 'Consulta 1', command=lambda: self.ConsultarTodo(lblConsultaMarca,lblConsultaPrecio,lblPrecio))
        btnConsultar.pack()
        
        btnConsultaTodo = tk.Button(self.frame, text='Consulta de todo', command=lambda: self.ConsultarTodo(lblMarca.get(), lblTamaño.get(), lblColor.get(), lblPrecio.get()))
        btnConsultaTodo.pack()
        
        self.frame.title('Bafle')
        self.frame.geometry("1000x1000")
        self.tabla.tabla.pack()
        
        '''def SeleccionElemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                entryId.delete(0, tk.END)
                entryId.insert(0, str(valores[0]))
                
                entryMarca.delete(0, tk.END)
                entryMarca.insert(0, str(valores[1]))
                
                entryTamaño.delete(0, tk.END)
                entryTamaño.insert(0, str(valores[2]))
                
                entryColor.delete(0, tk.END)
                entryColor.insert(0, str(valores[3]))
                
                entryPrecio.delete(0, tk.END) 
                entryPrecio.insert (0, str(valores[4])) '''         
                
        def BorrarElemento(_):
            for i in self.tabla.tabla.selection():
                self.Comunicacion.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)
                
        '''self.tabla.tabla.bind('<<TreeviewSelect>>', SeleccionElemento)'''
        self.tabla.tabla.bind('<Delete>', BorrarElemento)

        self.frame.mainloop()        
        