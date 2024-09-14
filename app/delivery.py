import requests
import json
import datetime
from utils.helpers import generate_order_id, choose_random_repartidor, choose_random_products

API_URL = "https://api-endpoint.com/registrar_pedido_entregado"  # Aquí debería ir la URL real de la API.

# Esta función es la encargada de registrar un pedido "entregado". Simula que un pedido ha sido entregado
# por un repartidor a un cliente y envía la información a la API que la va a procesar.
def registrar_pedido_entregado():
    # Generamos un número de pedido único usando una función auxiliar.
    pedido_id = generate_order_id()
    # Elegimos un repartidor al azar de una lista predefinida.
    repartidor = choose_random_repartidor()
    # Seleccionamos algunos productos al azar para el pedido.
    productos = choose_random_products()

    # Creamos un paquete de datos (payload) que contendrá toda la información del pedido.
    payload = {
        "pedido_id": pedido_id,
        "repartidor": repartidor,
        "productos": productos,
        "timestamp": str(datetime.datetime.now())  # Guardamos el momento exacto en que se registra el pedido.
    }

    # Estos son los encabezados necesarios para que la API entienda qué tipo de datos estamos enviando.
    headers = {
        "Content-Type": "application/json"
    }

    # Ahora enviamos los datos a la API usando el método POST.
    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        # Si la respuesta no es exitosa, lanzamos una excepción (error).
        response.raise_for_status()
        # Si todo va bien, imprimimos en la pantalla los detalles del pedido entregado.
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        print("### Pedido entregado, registrado exitosamente")
    except requests.RequestException as e:
        # Si algo sale mal, como que no tengamos conexión a internet o la API esté caída, mostramos el error.
        print(f"### Error al registrar el pedido entregado: {e}")

