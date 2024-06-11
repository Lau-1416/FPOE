import tkinter as tk
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

        self.clientes_ventana = None
        self.servicios_ventana = None

    def abrir_gestionar_clientes(self):
        if self.clientes_ventana is None or not self.clientes_ventana.winfo_exists():  # Verificar si la ventana ya está abierta
            self.ventana.withdraw()  # Ocultar ventana actual
            vistaPrincipal.iniciar_ventana_clientes(self.ventana, self.mostrar_ventana_inicio)

    def abrir_gestionar_servicios(self):
        if self.servicios_ventana is None or not self.servicios_ventana.winfo_exists():  # Verificar si la ventana ya está abierta
            self.ventana.withdraw()  # Ocultar ventana actual
            vistaServicios.iniciar_ventana_servicios(self.ventana, self.mostrar_ventana_inicio)

    def mostrar_ventana_inicio(self):
        self.ventana.deiconify()  # Mostrar ventana de inicio nuevamente

def iniciar_ventana_inicio():
    ventana = tk.Tk()
    app = InicioApp(ventana)
    ventana.mainloop()