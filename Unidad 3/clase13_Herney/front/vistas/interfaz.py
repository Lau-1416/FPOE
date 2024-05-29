import tkinter as tk
from controladores.comunicacion import Comunicacion
from modelos.usuario import Usuario
from controladores.validaciones import Validaciones
from tkinter import messagebox
from .tabla import Tabla

class Interfaz:

    def __init__(self):
        titulos = ['identificador','material' ,'color' ,'talla' ,'marca']
        comlumnas = ['id','material' ,'color' ,'talla' ,'marca' ]
        data = []
        self.ventanaPrincipal = tk.Tk()
        #self.ventanaPrincipal.resizable(0, 0)
        self.comunicacion = Comunicacion(self.ventanaPrincipal)
        self.ventanaPrincipal.state("zoomed")
        self.tabla = Tabla(self.ventanaPrincipal, titulos, comlumnas, data)
        self.ventanaPrincipal.config(bg="light pink")

    def validar_entrada(self, valor, etiqueta_error):
        mensaje_error = Validaciones.validarLetrasNumeros(valor)
        if mensaje_error:
            etiqueta_error.config(text=mensaje_error)
        else:
            etiqueta_error.config(text="")
    
    def limpiar_entradas(self):
        self.entrymaterial.delete(0, tk.END)
        self.entrycolor.delete(0, tk.END)
        self.entrytalla.delete(0, tk.END)
        self.entrymarca.delete(0, tk.END)
        self.entryId.delete(0, tk.END)

    def accion_guardar_boton(self, material, color, talla, marca, material_error, color_error, talla_error, marca_error):
        # Validaciones
        material_msg = Validaciones.validarLetrasNumeros(material)
        color_msg = Validaciones.validarLetrasNumeros(color)
        talla_msg = Validaciones.validarLetrasNumeros(talla)
        marca_msg = Validaciones.validarLetrasNumeros(marca)
        
        if material_msg or color_msg or talla_msg or marca_msg:
            material_error.config(text=material_msg or "")
            color_error.config(text=color_msg or "")
            talla_error.config(text=talla_msg or "")
            marca_error.config(text=marca_msg or "")
            # Mostrar un mensaje de error general si algún campo no es válido
            messagebox.showwarning("Error", "Por favor, complete todos los campos correctamente.")
        else:
            self.comunicacion.guardar(material, color, talla, marca)
            material_error.config(text="")
            color_error.config(text="")
            talla_error.config(text="")
            marca_error.config(text="")
            # Mostrar un mensaje de éxito
            messagebox.showinfo("Éxito", "Los datos han sido guardados correctamente.")
        
    
    def actualizar_boton(self, id, material, color, talla, marca):
        
        if id == '':
            self.comunicacion.guardar( material, color, talla, marca)
        
        else:
            self.comunicacion.actualizar(id, material, color, talla, marca)

    def accion_consultar_boton(self, labelConsultamaterial, labelConsultacolor, labelConsultatalla, labelConsultamarca, id):
        resultado = self.comunicacion.consultar(id)
        labelConsultamaterial.config(text=resultado.get('material'))
        labelConsultacolor.config(text=resultado.get('color'))
        labelConsultatalla.config(text=resultado.get('talla'))
        labelConsultamarca.config(text=resultado.get('marca'))
    
    def accion_consultar_todo(self, material, color, talla, marca):
        resultado = self.comunicacion.consultar_todo(marca, color, talla, material)
        data=[]
        print(resultado)
        print(type(resultado))
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('material'), elemento.get('color'), elemento.get('talla'), elemento.get('marca')))
        self.tabla.refrescar(data)

    def mostrar_interfaz(self):
        usuario = Usuario(self.ventanaPrincipal)
        
        def seleccionar_elemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                self.entryId.delete(0, tk.END)
                self.entryId.insert(0,str(valores[0]))
                self.entrymaterial.delete(0, tk.END)
                self.entrymaterial.insert(0,str(valores[1]))
                self.entrycolor.delete(0, tk.END)
                self.entrycolor.insert(0,str(valores[2]))             
                self.entrytalla.delete(0, tk.END)
                self.entrytalla.insert(0,str(valores[3]))
                self.entrymarca.delete(0, tk.END)
                self.entrymarca.insert(0,str(valores[4]))
                
        def borrar_elemento(_):
            for i in self.tabla.tabla.selection():
                self.comunicacion.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)

#Espacios de texto y entardas de texto principales
        labelmaterial = tk.Label(self.ventanaPrincipal, text="material", bg="light pink", font=("arial", 12))
        self.entrymaterial = tk.Entry(self.ventanaPrincipal, textvariable=usuario.material)
        labelcolor = tk.Label(self.ventanaPrincipal, text="color", bg="light pink", font=("arial", 12))
        self.entrycolor = tk.Entry(self.ventanaPrincipal, textvariable=usuario.color)
        labeltalla = tk.Label(self.ventanaPrincipal, text="talla", bg="light pink", font=("arial", 12))
        self.entrytalla = tk.Entry(self.ventanaPrincipal, textvariable=usuario.talla)
        labelmarca = tk.Label(self.ventanaPrincipal, text="marca", bg="light pink", font=("arial", 12))
        self.entrymarca = tk.Entry(self.ventanaPrincipal, textvariable=usuario.marca)
        labelId = tk.Label(self.ventanaPrincipal, text="ID", bg="light pink", font=("arial", 12))
        self.entryId = tk.Entry(self.ventanaPrincipal)

        labelConsultamaterial = tk.Label(self.ventanaPrincipal, text='',fg="red")
        labelConsultacolor = tk.Label(self.ventanaPrincipal, text='',fg="red")
        labelConsultatalla = tk.Label(self.ventanaPrincipal, text='',fg="red")
        labelConsultamarca = tk.Label(self.ventanaPrincipal, text='',fg="red")

        #Etiquetas de error
        material_error = tk.Label(self.ventanaPrincipal,bg="light pink", text="", fg="red")
        material_error.place(x=260, y=20)
        color_error = tk.Label(self.ventanaPrincipal,bg="light pink", text="", fg="red")
        color_error.place(x=260, y=60)
        talla_error = tk.Label(self.ventanaPrincipal,bg="light pink", text="", fg="red")
        talla_error.place(x=260, y=100)
        marca_error = tk.Label(self.ventanaPrincipal,bg="light pink", text="", fg="red")
        marca_error.place(x=260, y=140)

        #Comandos con el teclado
        self.entrymaterial.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entrymaterial.get(), material_error))
        self.entrycolor.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entrycolor.get(), color_error))
        self.entrytalla.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entrytalla.get(), talla_error))
        self.entrymarca.bind("<KeyRelease>", lambda event: self.validar_entrada(self.entrymarca.get(), marca_error))

        boton_actualizar = tk.Button(self.ventanaPrincipal, bg="plum1", text="actualizar", command=lambda:
        self.limpiar_y_actualizar_y_consultar(self.entryId.get(), self.entrymaterial.get(), self.entrycolor.get(), self.entrytalla.get(), self.entrymarca.get()))
        
        boton_guardar = tk.Button(self.ventanaPrincipal, bg="plum1",text="Guardar", command=lambda: 
        self.guardar_y_limpiar_y_consultar(self.entrymaterial.get(), self.entrycolor.get(), self.entrytalla.get(), self.entrymarca.get(), marca_error, color_error, material_error, talla_error))
        
        boton_consultar_1 = tk.Button(self.ventanaPrincipal, bg="plum1",text="Consultar 1", command=lambda:
        self.accion_consultar_boton(labelConsultamarca, labelConsultacolor, labelConsultamaterial, labelConsultatalla, self.entryId.get()))
        
        boton_limpiar = tk.Button(self.ventanaPrincipal, bg="plum1",text="limpiar", command= lambda:
        self.limpiar_entradas())
        
        boton_consultar_todos = tk.Button(self.ventanaPrincipal, bg="plum1", text="Consultar todos", command=lambda:
        self.accion_consultar_todo(self.entrymarca.get(), self.entrycolor.get(), self.entrymaterial.get(), self.entrytalla.get()))
        self.accion_consultar_todo(self.entrymarca.get(), self.entrycolor.get(), self.entrymaterial.get(), self.entrytalla.get())
        self.accion_consultar_todo(self.entrymarca.get(), self.entrycolor.get(), self.entrymaterial.get(), self.entrytalla.get())

        self.ventanaPrincipal.title("Ventana Principal")
        self.ventanaPrincipal.geometry("400x400")

        #Coordenadas de las entradas y texto principal
        labelmaterial.place(x=20, y=20)
        self.entrymaterial.place(x=120, y=20)
        labelcolor.place(x=20, y=60)
        self.entrycolor.place(x=120, y=60)
        labeltalla.place(x=20, y=100)
        self.entrytalla.place(x=120, y=100)
        labelmarca.place(x=20, y=140)
        self.entrymarca.place(x=120, y=140)

        boton_guardar.place(x=20, y=180)
        boton_consultar_1.place(x=100, y=180)
        boton_consultar_todos.place(x=180, y=180)
        boton_actualizar.place(x=320, y=180)
        boton_limpiar.place(x=420, y=180)
        
        
        self.tabla.tabla.place(x=100, y=220, width=1200)
        self.tabla.tabla.bind('<<TreeviewSelect>>', seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>', borrar_elemento)

        labelId.place(x=400, y=20)
        self.entryId.place(x=430, y=20)

        self.ventanaPrincipal.mainloop()
    
    def limpiar_y_actualizar_y_consultar(self, Id, material, color, talla, marca):
        self.limpiar_entradas()
        self.actualizar_boton(Id,material, color, talla, marca)
        self.accion_consultar_todo(material, color, talla, marca)
    
    def guardar_y_limpiar_y_consultar(self, material, color, talla, marca, material_error, color_error, talla_error, marca_error):
        self.accion_guardar_boton(material, color, talla, marca, material_error, color_error, talla_error, marca_error)

        self.limpiar_entradas()
        
        self.accion_consultar_todo(material, color, talla, marca)