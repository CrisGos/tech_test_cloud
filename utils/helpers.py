import uuid
import random

# Lista de productos de ejemplo. Cada producto tiene un ID, nombre y precio.
productos = [
    {
        "IdProducto": "pk0001",
        "producto": "Moneda",
        "precio": 1.00
    },
    {
        "IdProducto": "pk0002",
        "producto": "Estuche para gafas",
        "precio": 8.00
    },
    {
        "IdProducto": "pk0003",
        "producto": "Pequeño espejo de bolsillo",
        "precio": 5.00
    },
    {
        "IdProducto": "pk0004",
        "producto": "Pendrive",
        "precio": 12.00
    },
    {
        "IdProducto": "pk0005",
        "producto": "Tarjeta SIM",
        "precio": 3.00
    },
    {
        "IdProducto": "pk0006",
        "producto": "Adaptador de corriente",
        "precio": 10.00
    },
    {
        "IdProducto": "pk0007",
        "producto": "Tijeras pequeñas",
        "precio": 4.00
    },
    {
        "IdProducto": "pk0008",
        "producto": "Pila de botón",
        "precio": 2.50
    },
    {
        "IdProducto": "pk0009",
        "producto": "Goma de borrar",
        "precio": 0.50
    },
    {
        "IdProducto": "pk0010",
        "producto": "Clip sujetapapeles",
        "precio": 0.20
    }
]

# Lista de repartidores de ejemplo. Cada repartidor tiene un ID y un nombre.
repartidores = [
    {
        "IdRepartidor": 101,
        "Nombre": "María López"
    },
    {
        "IdRepartidor": 102,
        "Nombre": "Carlos García"
    },
    {
        "IdRepartidor": 103,
        "Nombre": "Ana Fernández"
    },
    {
        "IdRepartidor": 104,
        "Nombre": "Juan Martínez"
    },
    {
        "IdRepartidor": 105,
        "Nombre": "Laura Sánchez"
    },
    {
        "IdRepartidor": 106,
        "Nombre": "Pedro Gómez"
    },
    {
        "IdRepartidor": 107,
        "Nombre": "Elena Rodríguez"
    },
    {
        "IdRepartidor": 108,
        "Nombre": "Jorge Pérez"
    },
    {
        "IdRepartidor": 109,
        "Nombre": "Sofía Morales"
    },
    {
        "IdRepartidor": 110,
        "Nombre": "Daniel Castillo"
    }
]


# Esta función genera un código único para cada pedido usando la librería `uuid`.
# Este código es como un número de referencia que identifica al pedido.
def generate_order_id():
    return str(uuid.uuid4())

# Esta función elige un repartidor al azar de la lista de repartidores.
# Nos aseguramos de que cada vez se asigne un repartidor diferente.
def choose_random_repartidor():
    return random.choice(repartidores)

# Esta función selecciona productos al azar de la lista de productos.
# El número de productos que se elige también es aleatorio, entre 1 y 10.
def choose_random_products():
    return random.choices(productos, k=random.randint(1, 10))
