import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG)

class Hilo6(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        while True:
            nombre = input("Por favor, ingresa tu nombre: ")
            logging.debug(nombre)
            with open("nombres.txt", "a") as archivo:
                archivo.write(nombre + "\n")
                archivo.close
            time.sleep(5)