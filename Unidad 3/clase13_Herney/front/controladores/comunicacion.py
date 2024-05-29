import requests

class Comunicacion():

    def __init__(self, ventanaPrincipal):
        self.url = 'http://localhost:8000/v1/ropa'
        self.ventanaPrincipal = ventanaPrincipal
        pass
    
    def eliminar(self,id):
        resultado = requests.delete(self.url + '/' + str(id))
        return resultado

    def guardar(self, material, color, talla, marca):
        try:
            print(material, color, talla, marca)
            data = {
                'material': material,
                'color': color,
                'talla': talla,
                'marca': marca
            }
            resultado = requests.post(self.url, json=data)
            print(resultado.json)
            return resultado
        except:
            pass
        
    def actualizar(self, id, material, color, talla, marca):
        try:
            print(material, color, talla, marca)
            data = {
                'material': material,
                'color': color,
                'talla': talla,
                'marca': marca
            }
            resultado = requests.put(self.url + '/' + id + '/', json=data)
            print(resultado.json)
            return resultado
        except:
            pass
    
    def consultar(self, id):
        resultado = requests.get(self.url + '/' + str(id))
        print(resultado.text)
        print(resultado.status_code)
        try:
            return resultado.json()
        except ValueError:
            print("Respuesta no es un JSON válido.")
            return None
    
    def consultar_todo(self, marca, color, talla, material):
        url = self.url + "?"
        print(type(talla))
        if material != '':
            url = url + 'material=' + str(material) + "&"
        if color != '':
            url = url + 'color=' + str(color) + "&"
        if  talla != '':
            url = url + 'talla=' + str(talla) + "&"
        if  marca != '':
            url = url + 'marca=' + str(marca) + "&"
        resultado = requests.get(url)
        return resultado.json()