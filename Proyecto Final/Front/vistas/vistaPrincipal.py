import tkinter as tk
from tkinter import ttk
import requests

class LavelopuesApp:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Lavelopues S.A.S.")
        self.ventana.geometry('800x800')
        




 
if __name__ == "__main__":
    ventana = tk.Tk()
    app = LavelopuesApp(ventana)
    ventana.mainloop()