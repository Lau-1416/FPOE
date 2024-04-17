import tkinter as tk
import requests  #Para realizar solicitudes HTTP
from tkinter import messagebox


def ingresar_universidad():
    #Obtener los datos de los campos de entrada
    docente = txtDocente.get()
    estudiante = txtEstudiante.get()
    salon = txtSalon.get()
    local = txtLocal.get()

    #Validar si todos los campos están completos
    if not docente or not estudiante or not salon or not local:
        messagebox.showwarning("Error", "Por favor completa todos los campos.")
        return

    #Preparar los datos para enviar a la API en una estructura JSON
    data = {
        "docente": docente,
        "estudiante": estudiante,
        "salon": salon,
        "local": local
    }

    #Vinculacion con la vista APU de la clase Universidad
    url = 'http://127.0.0.1:8000/v1/universidad'

    try:
        # Realizar la solicitud POST a tu API
        response = requests.post(url, json=data)

        # Verificar el código de estado de la respuesta
        if response.status_code == 201:  # 201 significa creado (created)
            messagebox.showinfo("Éxito", "Universidad creada exitosamente.")
        else:
            messagebox.showerror("Error", f"Error al crear universidad: {response.text}")
    except Exception as e:
        messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}")

#Configuraracion la ventana principal
principal = tk.Tk()
principal.title('Universidad')
principal.geometry("240x220")

frame = tk.Frame(principal, padx=10, pady=10)
lblTitulo = tk.Label(frame, text='Ingresar Datos')
lblTitulo.grid(row=0, column=0, columnspan=2) 

lblDocente = tk.Label(frame, text='Docente:')
lblDocente.grid(row=1, column=0, padx=5, pady=5)  
lblEtudiante = tk.Label(frame, text='Estudiante:')
lblEtudiante.grid(row=2, column=0, padx=5, pady=5)
lblSalon = tk.Label(frame, text='Salón:')
lblSalon.grid(row=3, column=0, padx=5, pady=5)
lblLocal = tk.Label(frame, text='Local:')
lblLocal.grid(row=4, column=0, padx=5, pady=5)

txtDocente = tk.Entry(frame, width=20)
txtDocente.grid(row=1, column=1, padx=5, pady=5)  
txtEstudiante = tk.Entry(frame, width=20)
txtEstudiante.grid(row=2, column=1, padx=5, pady=5)
txtSalon = tk.Entry(frame, width=20)
txtSalon.grid(row=3, column=1, padx=5, pady=5)  
txtLocal = tk.Entry(frame, width=20)
txtLocal.grid(row=4, column=1, padx=5, pady=5)  

btnIngresar = tk.Button(frame, text='Ingresar', command=ingresar_universidad)
btnIngresar.grid(row=5, column=1, columnspan=2)

frame.pack(padx=10, pady=10)

principal.mainloop()