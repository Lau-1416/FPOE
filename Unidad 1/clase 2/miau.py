from tkinter import Frame, Tk
from tkinter.messagebox import askyesno


def eventoDarClick(evento):
    frame.focus_set()
    print('Di click en las coodenadas: ', evento.x, evento.y)

def eventoPresionarTeclado(evento):
    print("Presione la tecla: ", repr(evento.char))

def usuarioQuiereSalir():
    if askyesno('Salir de la aplicacion', '¿Esta seguro de que quiere cerrar la aplicacion'):
        principal.destroy()


principal = Tk()
principal.title('Prueba  de eventos')

frame = Frame(principal, width=500, height=500)
frame.bind("<Button-1>", eventoDarClick)
frame.bind("<Key>", eventoPresionarTeclado)

frame.pack()

principal.protocol('WM_DELETE_WINDOW', usuarioQuiereSalir)
principal.mainloop()