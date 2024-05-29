import re

class Validaciones():
    
    def __init__(self):
        pass

    @staticmethod
    def validarLetrasNumeros(valor):
        patron = re.compile("^[A-Za-zñÑ0-9. ]+$")
        resultado = patron.match(valor) is not None
        if not resultado:
            return "Solo caracteres validos."
        return None
    
    