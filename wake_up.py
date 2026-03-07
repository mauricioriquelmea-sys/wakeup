import requests
import time

# Listado de aplicaciones de Structural Lab (URLs de producción)
apps_urls = [
    "https://cinta3m-wnepapp6esbay9pzmy8dgqi.streamlit.app/",
    "https://engine-topgal-kqziwaj4vqugpluyepzban.streamlit.app/",
    "https://expansion-upr2xinenp8sosay8zmqud.streamlit.app/",
    "https://mullion-atkbmf2cnuqksoxyt8izct.streamlit.app/",
    "https://5m88qekh7gcrydaqy7x6xg.streamlit.app/",
    "https://pernotornillo-dfxkvxnfnurkgzmnaknsx6.streamlit.app/",
    "https://quimico-2pbzdm3zby4da8kzka8nhm.streamlit.app/",
    "https://m9plmxftfpszdjvacinftg.streamlit.app/",
    "https://bjtx5s2rdy5ekuokhjl8v9.streamlit.app/",
    "https://torque-slfubklryxkgpwanza9x3p.streamlit.app/",
    "hhttps://travesano-eusssrykqfvpyngtr9vzpv.streamlit.app/",
    "https://unidades-wehz8ayjfpy6uxlzvf2fb9.streamlit.app/",
    "hhttps://ventana-bkswzb7jhr4w8crprwwjb9.streamlit.app/",
    "https://mauricioriquelmea-sys-windload-viento-nch432-lzwdzg.streamlit.app/"
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