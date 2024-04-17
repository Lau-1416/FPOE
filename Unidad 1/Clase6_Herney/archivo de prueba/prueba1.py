import requests






data = {
    "Localidad ":"suba",
    "direccion": "calle12 esquina3",
    "barrio": "san vicente",
    "valor":"1567900"
}

respuesta = requests.post('http://127.0.0.1:8000/v1/casa', data=data)

print(respuesta.status_code)
