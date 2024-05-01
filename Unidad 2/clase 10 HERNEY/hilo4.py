import time
import logging
import threading


logging.basicConfig(level=logging.DEBUG)

class Hilo4(threading.Thread): 
    def __init__(self, nombreHilo, nombrePersona):
        threading.Thread.__init__(self,name=nombreHilo, target=Hilo4.run)
        self.nombreHilo = nombreHilo
        self.nombrePersona = nombrePersona


    def run(self):
        self.consultar(self.nombrePersona)

    def consultar(self, nombrePersona):
        logging.debug('Consultando: ' + nombrePersona)
        time.sleep(5)
        return