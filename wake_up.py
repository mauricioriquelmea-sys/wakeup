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
    "https://www.mauricioriquelme.com/topgal"
]

def wake_up():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Iniciando secuencia de activación...")
    for url in apps_urls:
        try:
            # Realizamos una petición GET con un timeout corto
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                print(f"✅ ACTIVA: {url}")
            else:
                print(f"⚠️ STATUS {response.status_code}: {url}")
        except Exception as e:
            print(f"❌ ERROR en {url}: {e}")

if __name__ == "__main__":
    # Ejecuta la activación una vez al día o cada 12 horas
    while True:
        wake_up()
        print("Esperando 12 horas para la próxima ronda...")
        time.sleep(43200) # 12 horas en segundos