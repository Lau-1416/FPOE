import requests
from tkinter import messagebox
from controladores.hilo import guardar_datos_en_archivo_hilo  # Importa la función


#from .validaciones import Validaciones
from vistas import vistaPrincipal
import threading

import requests
from tkinter import messagebox

class Peticiones():
    url_base = 'http://127.0.0.1:8000/v2/cliente'
    @staticmethod
    def ingresar_clientes(txtNombre, txtApellido, txtCedula, txtTelefono, txtCorreo):
        nombre = txtNombre.get()
        apellido = txtApellido.get()
        cedula = txtCedula.get()
        telefono = txtTelefono.get()
        correoElectronico = txtCorreo.get()

        if not nombre or not apellido or not cedula or not telefono or not correoElectronico:
            messagebox.showwarning("Error", "Por favor completa todos los campos.")
            return

        if (txtNombre.lblAdvertencia.winfo_viewable() or
            txtApellido.lblAdvertencia1.winfo_viewable() or
            txtCedula.lblAdvertencia.winfo_viewable() or
            txtTelefono.lblAdvertencia.winfo_viewable() or
            txtCorreo.lblAdvertencia.winfo_viewable()):
            messagebox.showwarning("Error", "Por favor completa todos los campos correctamente.")
            return

        data = {
            "nombre": nombre,
            "apellido": apellido,
            "cedula": cedula,
            "telefono": telefono,
            "correoElectronico": correoElectronico
        }

        url = 'http://127.0.0.1:8000/v2/cliente'

        try:
            response = requests.post(url, json=data)
            if response.status_code == 201:
                messagebox.showinfo("Éxito", "Cliente registrado exitosamente.")
                guardar_datos_en_archivo_hilo(data)
            else:
                messagebox.showerror("Error", f"Error al ingresar cliente: {response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}")

    @staticmethod
    def actualizar(id, nombre, apellido, cedula, telefono, correoElectronico):
        try:
            data = {
                "nombre": nombre,
                "apellido": apellido,
                "cedula": cedula,
                "telefono": telefono,
                "correoElectronico": correoElectronico
            }
            url = f'http://127.0.0.1:8000/v2/cliente/{id}/'
            resultado = requests.put(url, json=data)
            resultado.raise_for_status()  # Esto lanzará una excepción si la respuesta no es 2xx
            guardar_datos_en_archivo_hilo(data)
            return resultado.status_code
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}")
            return None
  
    @staticmethod
    def consultar(id):
        try:
            resultado = requests.get('http://127.0.0.1:8000/v2/cliente/' + str(id))
            resultado.raise_for_status()  # Verifica si la solicitud tuvo éxito
            return resultado.json()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}")
            return None


    @staticmethod
    def buscar(datos):
        try:
            url = 'http://127.0.0.1:8000/v2/cliente?'
            for key, value in datos.items():
                if value:
                    url += f"{key}={value}&"
            
            resultado = requests.get(url)
            resultado.raise_for_status()
            return resultado.json()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}")
            return None
    @staticmethod     
    def eliminar(id):
        try:
            url = f"{Peticiones.url_base}/{id}"
            resultado = requests.delete(url)
            if resultado.status_code == 204:
                data = {"id": id, "action": "deleted"}
                guardar_datos_en_archivo_hilo(data)
                return 200  # Cambiamos el código de estado a 200 cuando la eliminación es exitosa
            else:
                return resultado.status_code
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}")
            return None
        


    def cedula_existe(self, cedula):
        try:
            url = f"{Peticiones.url_base}?cedula={cedula}"
            resultado = requests.get(url)
            resultado.raise_for_status()
            data = resultado.json()
            
            # Verifica si la respuesta es una lista y si tiene elementos
            if isinstance(data, list) and len(data) > 0:
                return True
            else:
                return False
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}")
            return False  # Cambia None a False para manejo más consistente 
        

    
    ''' def guardar_datos_en_archivo(data):
            try:
                with open('gestionLaveloPues.txt', 'a', encoding='utf-8') as archivo:
                    archivo.write(json.dumps(data) + "\n")
            except Exception as e:
                messagebox.showerror("Error", f"Error al guardar el archivo: {str(e)}")

        @staticmethod
        def guardar_datos_en_archivo_hilo(data):
            hilo = threading.Thread(target=Peticiones.guardar_datos_en_archivo, args=(data,))
            hilo.start()'''