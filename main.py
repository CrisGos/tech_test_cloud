import time
from app.delivery import registrar_pedido_entregado
from app.monitor import mostrar_metrica

# Este archivo es el que "dirige" todo el programa.
# Hace que cada 10 segundos se registre un nuevo pedido y se muestren las métricas.
if __name__ == "__main__":
    while True:
        # Registramos un pedido entregado y lo enviamos a la API.
        registrar_pedido_entregado()
        # Mostramos las métricas en pantalla (entregas por repartidor y productos más vendidos).
        mostrar_metrica()
        # Esperamos 10 segundos antes de repetir todo el proceso.
        time.sleep(10)  # Refresca cada 10 segundos
