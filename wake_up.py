import requests
import time
from datetime import datetime

# Listado de tus aplicaciones en Structural Lab
apps_urls = [
    "https://www.mauricioriquelme.com/wind",
    "https://www.mauricioriquelme.com/techo",
    "https://www.mauricioriquelme.com/nieve",
    "https://www.mauricioriquelme.com/sismo",
    "https://www.mauricioriquelme.com/mullion",
    "https://www.mauricioriquelme.com/travesanos",
    "https://www.mauricioriquelme.com/silicona",
    "https://www.mauricioriquelme.com/cinta",
    "https://www.mauricioriquelme.com/unidades",
    "https://www.mauricioriquelme.com/torque",
    "https://www.mauricioriquelme.com/ventana"
    "https://www.mauricioriquelme.com/quimico"
    "https://www.mauricioriquelme.com/expansion"
    "https://www.mauricioriquelme.com/topgal"
]

def wake_up():
    print("Despertando Structural Lab...")
    for url in apps_urls:
        try:
            # Importante: poner un timeout para que no se quede pegado
            r = requests.get(url, timeout=15) 
            print(f"Status {r.status_code} para {url}")
        except Exception as e:
            print(f"Error en {url}: {e}")

if __name__ == "__main__":
    wake_up() # Se ejecuta UNA VEZ y termina.