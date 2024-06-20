import json
import threading
from tkinter import messagebox

def guardar_datos_en_archivo(data):
    try:
        with open('gestionLaveloPues.txt', 'a', encoding='utf-8') as archivo:
            archivo.write(json.dumps(data, ensure_ascii=False) + "\n")
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar el archivo: {str(e)}")

def guardar_datos_en_archivo_hilo(data):
    hilo = threading.Thread(target=guardar_datos_en_archivo, args=(data,))
    hilo.start()