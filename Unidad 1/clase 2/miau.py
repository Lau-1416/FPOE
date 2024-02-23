from tkinter import Frame, Tk

def eventoDarClick(evento):
    frame.focus_set()
    print('Di click en las coodenadas: ', evento.x, evento.y)

def eventoPresionarTeclado(evento):
    print("Presione la tecla: ", repr(evento.char) )


principal = Tk()
principal.title('Prueba  de eventos')

frame = Frame(principal, width=500, height=500)
frame.bind("<Button-1>", eventoDarClick)
frame.bind("<Key>", eventoPresionarTeclado)
frame.pack

principal.mainloop()