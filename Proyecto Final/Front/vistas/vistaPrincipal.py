import tkinter as tk
from tkinter import ttk
import requests
from tkinter import messagebox
from controladores.peticiones import Peticiones
from vistas.tabla import Tabla
from controladores.validaciones import Validaciones
from functools import partial

class LavelopuesApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Lavelopues S.A.S.")
        self.ventana.geometry('500x390')

        self.frame = tk.Frame(self.ventana, padx=10, pady=10)
        self.frame.pack(padx=10, pady=10)

        titulos = ['Identificador', 'Nombre', 'Apellido', 'Cedula', 'Telefono', 'Correo Electronico']
        columnas = ['id', 'nombre', 'apellido', 'cedula', 'telefono', 'correoElectronico']
        self.data = []

        self.peticiones = Peticiones()
        self.tabla = Tabla(self.ventana, titulos, columnas, self.data)
        self.tabla.refrescar(self.data)
        self.actualizar_tabla()

        self.tabla.tabla.pack(fill=tk.BOTH, expand=True)#para mostrar la tabla es que se me olvida :)
       

        
        tk.Label(self.frame, text="Nombre:").grid(row=0, column=1, columnspan=2, pady=5)
        self.txtNombre = tk.Entry(self.frame)
        self.txtNombre.grid(row=1, column=1, columnspan=2, padx=30, pady=5)
        self.txtNombre.lblAdvertencia = tk.Label(self.frame, text='Solo se permiten letras', fg="red")
        self.txtNombre.lblAdvertencia.grid(row=2, column=1, sticky="w", columnspan=2,padx=60, pady=5)
        self.txtNombre.lblAdvertencia.grid_remove()

        tk.Label(self.frame, text="Apellido:").grid(row=3, column=1, columnspan=2, pady=5)
        self.txtApellido = tk.Entry(self.frame)
        self.txtApellido.grid(row=4, column=1, columnspan=2, padx=30, pady=5)
        self.txtApellido.lblAdvertencia1 = tk.Label(self.frame, text='Solo se permiten letras', fg="red")
        self.txtApellido.lblAdvertencia1.grid(row=5, column=1, sticky="w",columnspan=2,padx=60, pady=5)
        self.txtApellido.lblAdvertencia1.grid_remove()

        tk.Label(self.frame, text="Cédula:").grid(row=6, column=1, columnspan=2, pady=5)
        self.txtCedula = tk.Entry(self.frame)
        self.txtCedula.grid(row=7, column=1, columnspan=2, padx=30, pady=5)
        self.txtCedula.lblAdvertencia = tk.Label(self.frame, text='Solo se permiten numeros', fg="red")
        self.txtCedula.lblAdvertencia.grid(row=8, column=1, sticky="w",columnspan=2,padx=60, pady=5)
        self.txtCedula.lblAdvertencia.grid_remove()

        tk.Label(self.frame, text="Teléfono:").grid(row=9, column=1, columnspan=2, pady=5)
        self.txtTelefono = tk.Entry(self.frame)
        self.txtTelefono.grid(row=10, column=1, columnspan=2, padx=30, pady=5)
        self.txtTelefono.lblAdvertencia = tk.Label(self.frame, text='Solo se permiten numeros', fg="red")
        self.txtTelefono.lblAdvertencia.grid(row=11, column=1, sticky="w",columnspan=2,padx=60, pady=5)
        self.txtTelefono.lblAdvertencia.grid_remove()

        tk.Label(self.frame, text="Correo:").grid(row=12, column=1, columnspan=2, pady=5)
        self.txtCorreo = tk.Entry(self.frame)
        self.txtCorreo.grid(row=13, column=1, columnspan=2, padx=30, pady=5)
        self.txtCorreo.lblAdvertencia = tk.Label(self.frame, text='El correo no es valido', fg="red")
        self.txtCorreo.lblAdvertencia.grid(row=14, column=1, sticky="w",columnspan=2,padx=60, pady=5)
        self.txtCorreo.lblAdvertencia.grid_remove()

        tk.Label(self.frame, text="ID:").grid(row=15, column=1, columnspan=2, pady=5)
        self.txtId = tk.Entry(self.frame)
        self.txtId.grid(row=16, column=1, columnspan=2, padx=30, pady=5)




        self.btnAgregar = tk.Button(self.frame, text="Agregar Cliente", command= self.verificar_cliente)
        self.btnAgregar.grid(row=17, column=0, pady=20, padx=10, sticky='ew')

        self.btnActualizar= tk.Button(self.frame, text="Actualizar Cliente", command=self.actualizar_cliente)
        self.btnActualizar.grid(row=17, column=1, pady=20, padx=10, sticky='ew')

        self.btnLimpiar = tk.Button(self.frame, text="Limpiar Campos", command=self.limpiar_campos)
        self.btnLimpiar.grid(row=17, column=2, pady=20, padx=10, sticky='ew')

        self.bntConsultar = tk.Button(self.frame, text="Consultar Clientes", command=partial(self.accion_buscar_boton, self.txtNombre, self.txtApellido, self.txtCedula, self.txtTelefono, self.txtCorreo,self.txtId, self.tabla))
        self.bntConsultar.grid(row=17, column=3, pady=20, padx=10, sticky='ew')


        self.txtNombre.bind('<KeyRelease>', Validaciones.mostrar_advertencia_nombre)
        self.txtApellido.bind('<KeyRelease>', Validaciones.mostrar_advertencia_apellido)
        self.txtCedula.bind('<KeyRelease>', Validaciones.mostrar_advertencia_cedula)
        self.txtTelefono.bind('<KeyRelease>', Validaciones.mostrar_advertencia_telefono)
        self.txtCorreo.bind('<KeyRelease>', Validaciones.mostrar_advertencia_correo)
        
        self.tabla.tabla.bind('<<TreeviewSelect>>', self.seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>', self.borrar_elemento)  # Vincular la tecla Suprimir
       


    def peticion_ingresar_clientes(self):
        id_seleccionado = self.obtener_id_seleccionado()
        if id_seleccionado:
            confirmacion = messagebox.askyesno("Confirmar Actualización", "¿Estás seguro de que deseas actualizar este cliente?")
            if confirmacion:
                self.actualizar_cleintes(id_seleccionado)
            else:
                self.ingresar_clientes()
        else:
            self.ingresar_clientes()

    def obtener_id_seleccionado(self):
        id_seleccionado = None
        for i in self.tabla.tabla.selection():
            id_seleccionado = self.tabla.tabla.item(i)['values'][0]
            break  # Solo necesitamos el ID de la primera fila seleccionada
        return id_seleccionado

    def actualizar_cliente(self):
        # Obtener los valores de los campos
        id = self.txtId.get()
        nombre = self.txtNombre.get()
        apellido = self.txtApellido.get()
        cedula = self.txtCedula.get()
        telefono = self.txtTelefono.get()
        correoElectronico = self.txtCorreo.get()

        if not id:
            messagebox.showwarning("Error", "No hay ningún cliente seleccionado.")
            return

        cliente_actual = self.peticiones.consultar(id)
        if cliente_actual and cliente_actual.get('cedula') != cedula:
            messagebox.showwarning("Error", "No se puede cambiar la cédula de un cliente existente.")
            self.txtCedula.delete(0, tk.END)
            self.txtCedula.insert(0, cliente_actual.get('cedula'))
            return

        if not nombre or not apellido or not cedula or not telefono or not correoElectronico:
            messagebox.showwarning("Error", "Por favor completa todos los campos.")
            return

        respuesta = messagebox.askyesno("Confirmar actualización", "¿Está seguro de que desea actualizar este cliente?")
        if respuesta:
            status_code = self.peticiones.actualizar(id, nombre, apellido, cedula, telefono, correoElectronico)
            if status_code == 200:
                messagebox.showinfo("Éxito", "Cliente actualizado correctamente")
                self.actualizar_tabla()  # Actualizar la tabla para reflejar los cambios
                self.limpiar_campos()
            else:
                messagebox.showerror("Error", f"Error al actualizar el cliente: Código de estado {status_code}")

    
    def ingresar_clientes(self):
        cedula = self.txtCedula.get()
        if self.peticiones.cedula_existe(cedula):
            messagebox.showinfo("Aviso", "La cédula ya ha sido registrada.")
            return
        
        Peticiones.ingresar_clientes(self.txtNombre, self.txtApellido, self.txtCedula, self.txtTelefono, self.txtCorreo)
        self.actualizar_tabla()  #Actualizar la tabla después de la inserción
        self.limpiar_campos()

    
        
    def actualizar_tabla(self):
        # Obtener los datos de la API y actualizar la tabla
        parametrosBusqueda = {}  # Puedes agregar parámetros específicos si los necesitas
        resultado = self.peticiones.buscar(parametrosBusqueda)
        if resultado is not None:
            self.data = []  # Reinicializa data si hay resultado
            for elemento in resultado:
                self.data.append((
                    elemento.get('id'),
                    elemento.get('nombre'),
                    elemento.get('apellido'),
                    elemento.get('cedula'),
                    elemento.get('telefono'),
                    elemento.get('correoElectronico')
                ))
            self.tabla.refrescar(self.data)

    # Funcion para el boton de buscar
    def accion_buscar_boton(self, txtNombre, txtApellido, txtCedula, txtTelefono, txtCorreo, txtId, tabla):
        datos = {
            "nombre": txtNombre.get(),
            "apellido": txtApellido.get(),
            "cedula": txtCedula.get(),
            "telefono": txtTelefono.get(),
            "correoElectronico": txtCorreo.get(),
            "id": txtId.get()
        }
        resultados = self.peticiones.buscar(datos)  # Se debe llamar a través de self.peticiones
        if resultados is not None:
            data = []
            for elemento in resultados:
                data.append((
                    elemento.get('id'),
                    elemento.get('nombre'),
                    elemento.get('apellido'),
                    elemento.get('cedula'),
                    elemento.get('telefono'),
                    elemento.get('correoElectronico')
                ))
            tabla.refrescar(data)

    def seleccionar_elemento(self, event):
        for i in self.tabla.tabla.selection():
            valores = self.tabla.tabla.item(i)['values']
            self.txtId.delete(0, tk.END)
            self.txtId.insert(0, str(valores[0]))
            self.txtNombre.delete(0, tk.END)
            self.txtNombre.insert(0, str(valores[1]))
            self.txtApellido.delete(0, tk.END)
            self.txtApellido.insert(0, str(valores[2]))
            self.txtCedula.delete(0, tk.END)
            self.txtCedula.insert(0, str(valores[3]))
            self.txtTelefono.delete(0, tk.END)
            self.txtTelefono.insert(0, str(valores[4]))
            self.txtCorreo.delete(0, tk.END)
            self.txtCorreo.insert(0, str(valores[5]))    

    def verificar_cliente(self):
        id = self.txtId.get()
        cedula = self.txtCedula.get()

        if self.peticiones.cedula_existe(cedula):
            messagebox.showinfo("Aviso", "La cédula ya ha sido registrada.")
            return

        if id:
            messagebox.showinfo("Aviso", "Este cliente ya está registrado.")
            '''if confirmacion:
                self.actualizar_cliente()'''
        else:
            self.ingresar_clientes()
    
    def limpiar_campos(self):
        self.txtNombre.delete(0, tk.END)
        self.txtApellido.delete(0, tk.END)
        self.txtCedula.delete(0, tk.END)
        self.txtTelefono.delete(0, tk.END),
        self.txtCorreo.delete(0, tk.END),
        self.txtId.delete(0, tk.END)


    def borrar_cliente(self):
        for i in self.tabla.tabla.selection():
            id = self.tabla.tabla.item(i)['values'][0]
            confirmacion = messagebox.askyesno("Confirmar eliminación", f"¿Estás seguro de que deseas eliminar el cliente con ID {id}?")
            if confirmacion:
                status_code = self.peticiones.eliminar(id)
                if status_code == 200:
                    self.tabla.tabla.delete(i)
                    messagebox.showinfo("Confirmación", "El cliente ha sido eliminado correctamente")
                else:
                    messagebox.showerror("Error", f"Error al eliminar el cliente con ID {id}")

    def borrar_elemento(self, event):
        print("Tecla Suprimir presionada")
        self.borrar_cliente()
                
    

 
def iniciar_ventana_clientes(ventana_principal, callback_volver_inicio):
    ventana_clientes = tk.Toplevel(ventana_principal)
    app = LavelopuesApp(ventana_clientes)

    # Detectar cierre de ventana
    def volver_a_inicio():
        ventana_clientes.withdraw()
        callback_volver_inicio()  # Mostrar ventana de inicio nuevamente

    ventana_clientes.protocol("WM_DELETE_WINDOW", volver_a_inicio)
    ventana_clientes.mainloop()
