import requests
import time

# Listado de aplicaciones de Structural Lab (URLs de producción)
apps_urls = [
    "https://viento-nch432.streamlit.app/",
    "https://sobrecarga-techo-nch1537.streamlit.app/",
    "https://nieve-nch431.streamlit.app/",
    "https://sismo-secundario.streamlit.app/",
    "https://mullion.streamlit.app/",
    "https://travesanos.streamlit.app/",
    "https://siliconaestructural.streamlit.app/",
    "https://cinta3m.streamlit.app/",
    "https://torque.streamlit.app/",
    "https://quimico.streamlit.app/",
    "https://expansion.streamlit.app/",
    "https://perno-tornillo.streamlit.app/",
    "https://engine-topgal.streamlit.app/",
    "https://ventana-nch3532.streamlit.app/",
    "https://unidades-ingenieria.streamlit.app/"
]

def wake_up():
    print(f"--- Iniciando despertar de Structural Lab: {time.strftime('%Y-%m-%d %H:%M:%S')} ---")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    for url in apps_urls:
        try:
            # Enviamos la petición. Si la app está dormida, esto la activará.
            r = requests.get(url, headers=headers, timeout=25) 
            print(f"✅ Status {r.status_code} para: {url}")
        except Exception as e:
            print(f"❌ Error en {url}: {e}")
    print("--- Proceso finalizado ---")

if __name__ == "__main__":
    wake_up()