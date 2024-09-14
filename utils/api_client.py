import requests

# Esta función se encarga de enviar datos a la API.
# Recibe dos parámetros: la URL donde se deben enviar los datos, y los datos mismos.
def post_data(url, data):
    # Aquí definimos los "headers", que indican que vamos a enviar información en formato JSON.
    headers = {"Content-Type": "application/json"}
    try:
        # Intentamos hacer la petición POST a la API, enviando los datos y los headers.
        response = requests.post(url, json=data, headers=headers)
        # Si hay algún problema con la respuesta (como un error del servidor), se lanza una excepción.
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        # Si la petición falla (por ejemplo, si no hay conexión), mostramos un mensaje de error.
        print(f"Error en la petición: {e}")
        return None
