import threading
import datetime
import time
import logging
from hilo4 import Hilo4
from hilo5 import Hilo5
from hilo6 import Hilo6

logging.basicConfig(level=logging.DEBUG)

tiempoInicial = datetime.datetime.now()


def consultar(nombre):
    logging.debug('Consultando: ' + nombre)
    time.sleep(5)
    return


def numeros():
    list =[1,2,3,4,5]
    for element in list:
        logging.debug(element)
    time.sleep(1)
    #logging.debug('Consultando: a Julian')
    return

def letras():
    list =['a','b','c','d','e']
    for element in list:
        logging.debug(element)
    time.sleep(2)
    return

hilo1 = threading.Thread(name='hilo1', target=numeros)
hilo2 = threading.Thread(name='hilo2', target=letras)
hilo3 = threading.Thread(name='hilo3', target=consultar, args=('Julian', ))
hilo4 = Hilo4('hilo4', 'Julian')
hilo5 = Hilo5('hilo5')
hilo6 = Hilo6('Hilo6')


#hilo1.start()
#hilo1.join()
#hilo2.start()
#hilo2.join()
#hilo3.start()
#hilo3.join()
#hilo4.start()
hilo6.start()
hilo5.start()
hilo6.join()
hilo5.join()




tiempoFinal = datetime.datetime.now()

logging.debug('Tiempo Transcurrido: '  + str(tiempoFinal.second - tiempoInicial.second) + '\n')














