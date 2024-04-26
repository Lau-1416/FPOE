import time
import logging
import threading


logging.basicConfig(level=logging.DEBUG)

class Hilo5(threading.Thread): 
    def __init__(self, nombreHilo):
        threading.Thread.__init__(self,name=nombreHilo, target=Hilo5.run)
        self.nombreHilo = nombreHilo

    def run(self):
        self.infinito()

    def infinito(self):
        while True:
            logging.debug('Esto se escribe infinnitamente: ')
            time.sleep(1)
        return