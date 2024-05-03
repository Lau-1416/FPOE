import tkinter as tk


def ingresar_bafle():
    marca = txtMarca.get()
    tamaño = txtTamaño.get()
    color = txtColor.get()
    precio = txtPrecio.get()
    
principal = tk.Tk()
principal.title('Bafle')
principal.geometry("240x220")

frame = tk.Frame(principal, padx=10, pady=10)
lblTitulo = tk.Label(frame, text='Ingresar Datos')
lblTitulo.grid(row=0, column=0, columnspan=2) 

lblMarca = tk.Label(frame, text='Marca:')
lblMarca.grid(row=1, column=0, padx=5, pady=5)  
lblTamaño = tk.Label(frame, text='Tamaño:')
lblTamaño.grid(row=2, column=0, padx=5, pady=5)
lblColor = tk.Label(frame, text='Color:')
lblColor.grid(row=3, column=0, padx=5, pady=5)
lblPrecio = tk.Label(frame, text='Precio:')
lblPrecio.grid(row=4, column=0, padx=5, pady=5)

txtMarca = tk.Entry(frame, width=20)
txtMarca.grid(row=1, column=1, padx=5, pady=5)  
txtTamaño = tk.Entry(frame, width=20)
txtTamaño.grid(row=2, column=1, padx=5, pady=5)
txtColor = tk.Entry(frame, width=20)
txtColor.grid(row=3, column=1, padx=5, pady=5)  
txtPrecio = tk.Entry(frame, width=20)
txtPrecio.grid(row=4, column=1, padx=5, pady=5)  

btnIngresar = tk.Button(frame, text='Ingresar', command=ingresar_bafle)
btnIngresar.grid(row=5, column=1, columnspan=2)

frame.pack(padx=10, pady=10)

principal.mainloop()