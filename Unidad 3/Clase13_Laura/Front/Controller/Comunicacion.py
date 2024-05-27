import requests

class Comunicacion():

    def __init__(self, ventana_principal):
        self.url = 'http://127.0.0.1:8000/v1/bafle'

    def consultar(self, id):
        resultado = requests.get(self.url + '/' + str(id))
        return resultado.json()
    
    def ConsultarTodo(self, marca, tamaño, color, precio):
        url = self.url+ "?"
        print(type(precio))
        if precio != '':
            url = url + 'precio=' + str(precio) + "&"
        if marca != '':
            url = url + 'marca=' + str(marca) + "&"
        print(url)
        resultado = requests.get(url)
        return resultado.json()

    def eliminar(self, id):
        resultado = requests.delete(self.url + '/' + str(id))
        return resultado.status_code
    
    def actualizar(self, id, marca, tamaño, color, precio):
        try:
            print(marca, tamaño, color, precio)
            data = {
                'marca': marca,
                'tamaño': tamaño,
                'color': color,
                'precio': int(precio)
            }
            resultado = requests.put(self.url + '/' + id + '/', json=data)
            print(resultado.json)
            return resultado
        except:
            pass
        
    def guardar(self, marca, tamaño, color, precio):
            try:
                print(marca, tamaño, color, precio)
                data = {
                    'marca': marca,
                    'tamaño': tamaño,
                    'color': color,
                    'precio': int(precio)
                }
                resultado = requests.post(self.url, json=data)
                print(resultado.json)
                return resultado
            except:
                pass