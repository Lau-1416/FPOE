import tkinter as tk
from tkinter import *
from tkinter import messagebox
import re

principal =tk.Tk()
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
lblSalon.grid(row=3,column=0, padx=5, pady=5)
lblLocal = tk.Label(frame, text='Local:')
lblLocal.grid(row=4, column=0, padx=5, pady=5)

txtDocente = tk.Entry(frame, width=20)
txtDocente.grid(row=1,column=1, padx=5, pady=5)  
txtEstudiante = tk.Entry(frame, width=20)
txtEstudiante.grid(row=2,column=1, padx=5, pady=5)
txtSalon = tk.Entry(frame, width=20)
txtSalon.grid(row=3,column=1, padx=5, pady=5)  
txtLocal = tk.Entry(frame, width=20)
txtLocal.grid(row=4,column=1, padx=5, pady=5)  


btnIngresar = tk.Button(frame, text='Ingresar')
btnIngresar.grid(row=5, column=1,columnspan=2)

frame.pack(padx=10, pady=10)


principal.mainloop()