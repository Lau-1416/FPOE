import requests
from tkinter import messagebox

class PeticionesServicios:
    url_base = 'http://127.0.0.1:8000/v1/servicio'

    @staticmethod
    def ingresar_servicio(nombre, cedula_widget, descripcion, valor):
        cedula = cedula_widget.get()
        data = {
            "nombreServicio": nombre,
            "cedulaCliente_id": cedula,
            "descripcion": descripcion,
            "valor": valor
        }


        if not nombre or not cedula or not descripcion or not valor:
            messagebox.showwarning("Error", "Por favor completa todos los campos.")
            return
        
        if cedula_widget.lblAdvertencia.winfo_viewable():
            messagebox.showwarning("Error", "Por favor completa todos los campos correctamente.")
            return
        url = PeticionesServicios.url_base

        try:
            response = requests.post(url, json=data)
            if response.status_code == 201:
                messagebox.showinfo("Éxito", "Servicio registrado exitosamente.")
            else:
                pass
                #messagebox.showerror("Error", f"Error al ingresar servicio: {response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}")

    @staticmethod
    def actualizar_servicio(id, nombre, cedula, descripcion, valor):
        data = {
            "nombre": nombre,
            "cedula": cedula,
            "descripcion": descripcion,
            "valor": valor
        }
        url = f'{PeticionesServicios.url_base}/{id}/'

        try:
            response = requests.put(url, json=data)
            if response.status_code == 200:
                messagebox.showinfo("Éxito", "Servicio actualizado exitosamente.")
            else:
                messagebox.showerror("Error", f"Error al actualizar servicio: {response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}")

    @staticmethod
    def eliminar_servicio(id):
        url = f'{PeticionesServicios.url_base}/{id}/'

        try:
            response = requests.delete(url)
            if response.status_code == 204:
                messagebox.showinfo("Éxito", "Servicio eliminado exitosamente.")
            else:
                messagebox.showerror("Error", f"Error al eliminar servicio: {response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}")

    @staticmethod
    def consultar_servicio(id):
        url = f'{PeticionesServicios.url_base}/{id}/'

        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Error al consultar servicio: {response.text}")
                return None
        except Exception as e:
            messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}")
            return None
        

    @staticmethod
    def buscar(datos):
        try:
            url = 'http://127.0.0.1:8000/v1/servicio?'
            for key, value in datos.items():
                if value:
                    url += f"{key}={value}&"
            
            resultado = requests.get(url)
            resultado.raise_for_status()
            return resultado.json()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}")
            return None