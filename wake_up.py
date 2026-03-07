import requests

# Listado corregido con comas y URLs verificadas
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
    "https://engine-topgal.streamlit.app/"
]

def wake_up():
    print(f"Despertando Structural Lab...")
    for url in apps_urls:
        try:
            # Usamos un User-Agent para que Streamlit no bloquee la petición
            headers = {'User-Agent': 'Mozilla/5.0'}
            r = requests.get(url, headers=headers, timeout=20) 
            print(f"Status {r.status_code} para {url}")
        except Exception as e:
            print(f"Error en {url}: {e}")

if __name__ == "__main__":
    wake_up()