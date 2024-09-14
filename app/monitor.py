import random
import datetime

# Esta función simula las entregas de pedidos que ha realizado cada repartidor en la última hora.
# No es un cálculo real, simplemente se generan números aleatorios para mostrar cómo funcionaría un reporte.
def get_metrica_entregas_por_hora():
    # Creamos un diccionario donde el número de repartidor es la clave y el valor es la cantidad de entregas.
    return {f"Repartidor {i}": random.randint(1, 20) for i in range(101, 111)}

# Esta función simula los productos más vendidos. Los números también son aleatorios.
def get_productos_mas_vendidos():
    productos = ["Moneda", "Estuche", "Pendrive", "Tijeras", "Goma"]
    # Creamos un diccionario donde cada producto tiene asociado un número de ventas aleatorio.
    return {producto: random.randint(5, 50) for producto in productos}

# Esta función combina las métricas de entregas por repartidor y los productos más vendidos.
# Todo se imprime en pantalla para que lo podamos ver.
def mostrar_metrica():
    print(f"--- Métricas {datetime.datetime.now()} ---")
    print(f"Entregas por repartidor: {get_metrica_entregas_por_hora()}")
    print(f"Productos más vendidos: {get_productos_mas_vendidos()}")
    print("--------------------------------------------")
