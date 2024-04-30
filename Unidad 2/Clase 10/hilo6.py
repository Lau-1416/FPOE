import threading
import time
from hilo5 import Hilo5

class Hilo6(threading.Thread):
    def __init__(self, nombre_hilo):
        threading.Thread.__init__(self, name=nombre_hilo)
        self.nombre_hilo = nombre_hilo
        self.detenido = threading.Event()  #Evento para detener el hilo
        self.nombrePersona = None #nombrePersona

    def run(self):
        while not self.detenido.is_set():
            self.pedir_nombre()
            self.imprimir_nombre()
            self.guardar_nombre()
            time.sleep(5)

    def pedir_nombre(self):
        self.nombre = input("Ingrese su nombre: " + '\n')

    def imprimir_nombre(self):
        print("Nombre: ", self.nombre)

    def guardar_nombre(self):
        with open("nombres.txt", "a") as archivo:
            archivo.write(self.nombre + "\n")

    def detener(self):
        self.detenido.set()

if __name__ == "__main__":
    hilo = Hilo6("Hilo6")
    hilo.start()

    hilo5 = Hilo5("Hilo5")
    hilo5.start()

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        hilo.detener()
        hilo5.detener()
        hilo.join()
        hilo5.join()