import tkinter as tk
from tkinter import ttk
from vistas import vistaPrincipal
from vistas import vistaServicios

class InicioApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Inicio - Lavelopues S.A.S.")
        self.ventana.geometry('300x200')

        self.frame = tk.Frame(self.ventana, padx=10, pady=10)
        self.frame.pack(padx=10, pady=10)

        self.btnGestionarClientes = tk.Button(self.frame, text="Gestionar Clientes", command=self.abrir_gestionar_clientes)
        self.btnGestionarClientes.pack(fill=tk.BOTH, expand=True, pady=10)

        self.btnGestionarServicios = tk.Button(self.frame, text="Gestionar Servicios", command=self.abrir_gestionar_servicios)
        self.btnGestionarServicios.pack(fill=tk.BOTH, expand=True, pady=10)

    def abrir_gestionar_clientes(self):
        self.ventana.destroy()  # Cerrar ventana actual
        vistaPrincipal.iniciar_ventana_clientes()

    def abrir_gestionar_servicios(self):
        self.ventana.destroy()  # Cerrar ventana actual
        vistaServicios.iniciar_ventana_servicios()

def iniciar_ventana_inicio():
    ventana = tk.Tk()
    app = InicioApp(ventana)
    ventana.mainloop()
