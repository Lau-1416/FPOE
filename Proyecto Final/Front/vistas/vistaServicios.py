import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from controladores.peticionesServicios import PeticionesServicios
from vistas.tablaServicios import Tabla
from functools import partial
from controladores.validaciones import Validaciones


class ServiciosApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Servicios - Lavelopues S.A.S.")
        self.ventana.geometry('600x400')

        

        self.frame = tk.Frame(self.ventana, padx=10, pady=10)
        self.frame.pack(padx=10, pady=10)

        titulos = ['ID Servicio', 'Nombre Servicio', 'Cédula Cliente', 'Descripción', 'Valor']
        columnas = ['id', 'nombreServicio', 'cedulaCliente', 'descripcion', 'valor']
        self.data = []


        self.peticiones = PeticionesServicios()
        self.tabla = Tabla(self.ventana, titulos, columnas, self.data)
        self.tabla.refrescar(self.data)
        self.actualizar_tabla()

        self.tabla.tabla.pack(fill=tk.BOTH, expand=True)#para mostrar la tabla es que se me olvida :)

        self.detalles_servicios = {
        "Lavado Exterior Básico": {"descripcion": "Limpieza exterior del auto con agua y jabón.", "valor": 10000},
        "Lavado Interior y Exterior Completo": {"descripcion": "Lavado y secado exterior.", "valor": 20000},
        "Lavado y Encerado": {"descripcion": "Lavado completo del vehículo. Aplicación de cera.", "valor": 30000},
        "Lavado de Motor": {"descripcion": "Limpieza detallada del motor y sus componentes.", "valor": 15000},
        "Pulido y Descontaminación de Pintura": {"descripcion": "Eliminación de contaminantes y pulido de la pintura.", "valor": 25000},
        "Limpieza y Tratamiento de Asientos de Cuero": {"descripcion": "Limpieza profunda de asientos de cuero.", "valor": 22000},
        "Limpieza de Tapicería y Alfombras": {"descripcion": "Limpieza profunda de asientos de tela, alfombras y tapetes.", "valor": 18000},
        "Limpieza de Llantas y Rines": {"descripcion": "Limpieza detallada de llantas y rines para eliminar suciedad y residuos de frenos.", "valor": 12000},
        "Tratamiento Antilluvia para Parabrisas": {"descripcion": "Aplicación de productos hidrofóbicos en el parabrisas.", "valor": 9000},
        "Desodorización y Eliminación de Olores": {"descripcion": "Uso de tratamientos especiales para eliminar malos olores", "valor": 11000}
        }

        # Campos de entrada para los servicios
        tk.Label(self.frame, text="Nombre del Servicio:").grid(row=0, column=1, columnspan=2, pady=5)
        self.txtNombreServicio = ttk.Combobox(self.frame, values=["Lavado Exterior Básico", "Lavado Interior y Exterior Completo", "Lavado y Encerado", "Lavado de Motor", "Pulido y Descontaminación de Pintura", "Limpieza y Tratamiento de Asientos de Cuero", "Limpieza de Tapicería y Alfombras", "Limpieza de Llantas y Rines", "Tratamiento Antilluvia para Parabrisas", "Desodorización y Eliminación de Olores"])
        self.txtNombreServicio.grid(row=1, column=1, columnspan=2, padx=30, pady=5)
        self.txtNombreServicio.bind("<<ComboboxSelected>>", self.actualizar_detalles)

        tk.Label(self.frame, text="Cédula del Cliente:").grid(row=2, column=1, columnspan=2, pady=5)
        self.txtCedulaCliente = tk.Entry(self.frame)
        self.txtCedulaCliente.grid(row=3, column=1, columnspan=2, padx=30, pady=5)
        self.txtCedulaCliente.lblAdvertencia = tk.Label(self.frame, text='Solo se permiten numeros', fg="red")
        self.txtCedulaCliente.lblAdvertencia.grid(row=4, column=2, sticky="w",columnspan=2,padx=60, pady=5)
        self.txtCedulaCliente.lblAdvertencia.grid_remove()

        tk.Label(self.frame, text="Descripción:").grid(row=5, column=1, columnspan=2, pady=5)
        self.txtDescripcion = tk.Entry(self.frame)
        self.txtDescripcion.grid(row=6, column=1, columnspan=2, padx=30, pady=5)

        tk.Label(self.frame, text="Valor:").grid(row=7, column=1, columnspan=2, pady=5)
        self.txtValor = tk.Entry(self.frame)
        self.txtValor.grid(row=8, column=1, columnspan=2, padx=30, pady=5)

        tk.Label(self.frame, text="ID:").grid(row=9, column=1, columnspan=2, pady=5)
        self.txtId = tk.Entry(self.frame)
        self.txtId.grid(row=10, column=1, columnspan=2, padx=30, pady=5)

        # Botones para CRUD
        self.btnAgregar = tk.Button(self.frame, text="Agregar Servicio", command=self.agregar_servicio)
        self.btnAgregar.grid(row=11, column=0, pady=20, padx=10, sticky='ew')

        self.btnActualizar = tk.Button(self.frame, text="Actualizar Servicio", command=self.actualizar_servicio)
        self.btnActualizar.grid(row=11, column=1, pady=20, padx=10, sticky='ew')

        self.btnLimpiar = tk.Button(self.frame, text="Limpiar Campos", command=self.limpiar_campos)
        self.btnLimpiar.grid(row=11, column=2, pady=20, padx=10, sticky='ew')

        self.bntConsultar = tk.Button(self.frame, text="Consultar Servicios", command=partial(self.accion_buscar_boton, self.txtNombreServicio, self.txtCedulaCliente, self.txtDescripcion,self.txtValor,self.txtId, self.tabla))
        self.bntConsultar.grid(row=11, column=3, pady=20, padx=10, sticky='ew')

        self.txtCedulaCliente.bind('<KeyRelease>', Validaciones.mostrar_advertencia_cedula_cliente)


        self.tabla.tabla.bind('<<TreeviewSelect>>', self.seleccionar_elemento)
        self.tabla.tabla.bind('<Delete>', self.borrar_servicio)  # Vincular la tecla Suprimir


    def actualizar_detalles(self, event):
        # Obtiene el nombre del servicio seleccionado
        nombre_servicio = self.txtNombreServicio.get()
        # Actualiza el campo de descripción y el campo de precio del servicio con los detalles correspondientes
        detalles = self.detalles_servicios[nombre_servicio]
        self.txtDescripcion.delete(0, tk.END)
        self.txtDescripcion.insert(0, detalles["descripcion"])
        self.txtValor.delete(0, tk.END)
        self.txtValor.insert(0, detalles["valor"])

    def actualizar_tabla(self):
        parametros_busqueda = {}
        resultado = self.peticiones.buscar(parametros_busqueda)
        if resultado is not None:
            self.data = []
            for servicio in resultado:
                self.data.append((
                    servicio.get('id'),
                    servicio.get('nombreServicio'),
                    servicio.get('cedulaCliente'),
                    servicio.get('descripcion'),
                    servicio.get('valor')
                )) 
            self.tabla.refrescar(self.data)

    def agregar_servicio(self):
        nombre = self.txtNombreServicio.get()
        cedula = self.txtCedulaCliente
        descripcion = self.txtDescripcion.get()
        valor = self.txtValor.get()
        status_code = self.peticiones.ingresar_servicio(nombre,cedula, descripcion,valor)
        if status_code == 200:
            messagebox.showinfo("Éxito", "Servicio agregado correctamente")
            self.actualizar_tabla()
            self.limpiar_campos()
        else:
            pass
            #messagebox.showerror("Error", "Error al agregar el servicio")

    def actualizar_servicio(self):
        id = self.obtener_id_seleccionado()
        if not id:
            messagebox.showwarning("Error", "No hay ningún servicio seleccionado")
            return
        nombre = self.txtNombreServicio.get()
        cedula = self.txtCedulaCliente.get()
        descripcion = self.txtDescripcion.get()
        valor = self.txtValor.get()
        status_code = self.peticiones.actualizar_servicio(id, nombre, cedula, descripcion, valor)
        if status_code == 200:
            messagebox.showinfo("Éxito", "Servicio actualizado correctamente")
            self.actualizar_tabla()
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "Error al actualizar el servicio")

    def consultar_servicios(self):
        self.actualizar_tabla()

    def borrar_servicio(self, event=None):
        id = self.obtener_id_seleccionado()
        if not id:
            messagebox.showwarning("Error", "No hay ningún servicio seleccionado")
            return
        confirmacion = messagebox.askyesno("Confirmar eliminación", f"¿Estás seguro de que deseas eliminar el servicio con ID {id}?")
        if confirmacion:
            status_code = self.peticiones.eliminar_servicio(id)
            if status_code == 200:
                messagebox.showinfo("Éxito", "Servicio eliminado correctamente")
                self.actualizar_tabla()
            else:
                pass
                #messagebox.showerror("Error", "Error al eliminar el servicio")

    def seleccionar_elemento(self, event):
        # Verifica si hay alguna selección
        seleccion = self.tabla.tabla.selection()
        if not seleccion:
            return

        for i in seleccion:
            valores = self.tabla.tabla.item(i)['values']

        # Rellena los campos con los valores seleccionados
        self.txtId.delete(0, tk.END)
        self.txtId.insert(0, valores[0])  # ID debería estar en el índice 0
        
        self.txtNombreServicio.delete(0, tk.END)
        self.txtNombreServicio.insert(0, valores[1])

        self.txtCedulaCliente.delete(0, tk.END)
        self.txtCedulaCliente.insert(0, valores[2])

        self.txtDescripcion.delete(0, tk.END)
        self.txtDescripcion.insert(0, valores[3])

        self.txtValor.delete(0, tk.END)
        self.txtValor.insert(0, valores[4])

            

    def obtener_id_seleccionado(self):
        for i in self.tabla.tabla.selection():
            return self.tabla.tabla.item(i)['values'][0]
        return None

    def limpiar_campos(self):
        self.txtNombreServicio.delete(0, tk.END)
        self.txtCedulaCliente.delete(0, tk.END)
        self.txtDescripcion.delete(0, tk.END)
        self.txtValor.delete(0, tk.END)
        self.txtId.delete(0, tk.END)

    # Funcion para el boton de buscar
    def accion_buscar_boton(self, txtNombreServicio, txtCedulaCliente, txtDescripcion, txtValor, txtId, tabla):
        datos = {
            "id": txtId.get(),
            "nombreServicio": txtNombreServicio.get(),
            "cedulaCliente": txtCedulaCliente.get(),
            "descripcion": txtDescripcion.get(),
            "valor": txtValor.get(),
              
        }
        resultados = self.peticiones.buscar(datos)  # Se debe llamar a través de self.peticiones
        if resultados is not None:
            data = []
            for elemento in resultados:
                data.append((
                    elemento.get('id'),
                    elemento.get('nombreServicio'),
                    elemento.get('cedulaCliente'),
                    elemento.get('descripcion'),
                    elemento.get('valor')
                ))
            tabla.refrescar(data)





# Método principal para iniciar la ventana de servicios
def iniciar_ventana_servicios():
    ventana = tk.Tk()
    app = ServiciosApp(ventana)
    ventana.mainloop()


def iniciar_ventana_servicios(ventana_principal, callback_volver_inicio):
    ventana_servicios = tk.Toplevel(ventana_principal)
    app = ServiciosApp(ventana_servicios)

    # Detectar cierre de ventana
    def volver_a_inicio():
        ventana_servicios.withdraw()
        callback_volver_inicio()  # Mostrar ventana de inicio nuevamente

    ventana_servicios.protocol("WM_DELETE_WINDOW", volver_a_inicio)
    ventana_servicios.mainloop()