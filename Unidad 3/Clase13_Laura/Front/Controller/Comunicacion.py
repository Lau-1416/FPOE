import requests
from tkinter import messagebox

class Comunicacion():

    def __init__(self, ventana_principal):
        self.url = 'http://127.0.0.1:8000/v1/bafle'
        self.ventana_principal = ventana_principal
        pass
    
    def consultar(id):
        try:
            resultado = requests.get('http://127.0.0.1:8000/v1/bafle' + str(id))
            resultado.raise_for_status()  # Verifica si la solicitud tuvo éxito
            return resultado.json()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}")
            return None
    
    def ConsultarTodo(txtId, ConsultarTodo):
        id_marca = txtId.get()
        if not id_marca.isdigit():
            ConsultarTodo.config(text="Por favor ingrese un ID válido.")
            return 

        resultado = Comunicacion(id_marca)
        
        if resultado and 'marca' in resultado:
            ConsultarTodo.config(text=f"Marca: {resultado['marca']}")
        else:
            ConsultarTodo.config(text="No se encontraron resultados")