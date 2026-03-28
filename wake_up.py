"""
wake_up.py — Structural Lab | Keep-Alive Automation
Autor: Sistema DevOps Structural Lab
Propósito: Mantener activas las apps de Streamlit Cloud enviando
           pulsos HTTP periódicos para prevenir el "sleep" por inactividad.
"""

import requests
import time
import random
import sys
from datetime import datetime

# ──────────────────────────────────────────────
#  LISTADO CORREGIDO DE APLICACIONES
#  Structural Lab — Portafolio de Ingeniería
# ──────────────────────────────────────────────
APPS_URLS = [
    # Cargas de Viento
    "https://mauricioriquelmea-sys-windload-viento-nch432-lzwdzg.streamlit.app/",
    # Sobrecarga de Uso
    "https://m9plmxftfpszdjvacinftg.streamlit.app/",
    # Nieve / Sismo Secundario
    "https://bjtx5s2rdy5ekuokhjl8v9.streamlit.app/",
    # Mullion (Montante)
    "https://mullion-atkbmf2cnuqksoxyt8izct.streamlit.app/",
    # Travesaño
    "https://travesano-eusssrykqfvpyngtr9vzpv.streamlit.app/",
    # Silicona Estructural
    "https://5m88qekh7gcrydaqy7x6xg.streamlit.app/",
    # Cinta 3M
    "https://cinta3m-wnepapp6esbay9pzmy8dgqi.streamlit.app/",
    # Torque
    "https://torque-slfubklryxkgpwanza9x3p.streamlit.app/",
    # Químico (Anclaje)
    "https://quimico-2pbzdm3zby4da8kzka8nhm.streamlit.app/",
    # Expansión (Anclaje)
    "https://expansion-upr2xinenp8sosay8zmqud.streamlit.app/",
    # SBT
    "https://7qmsvcrwsafxzgp8icsncu.streamlit.app/",
    # Perno / Tornillo
    "https://pernotornillo-dfxkvxnfnurkgzmnaknsx6.streamlit.app/",
    # Engine TopGal
    "https://engine-topgal-kqziwaj4vqugpluyepzban.streamlit.app/",
    # Ventana
    "https://ventana-bkswzb7jhr4w8crprwwjb9.streamlit.app/",
    # Unidades
    "https://unidades-wehz8ayjfpy6uxlzvf2fb9.streamlit.app/",
     #grua
    "https://jexexkgjqv5hoiys9jx4it.streamlit.app/",
     # muro de contencion
    "https://murocontencion-jsfrrr5jqijr3kqnmjpadz.streamlit.app/",


]

# ──────────────────────────────────────────────
#  CONFIGURACIÓN
# ──────────────────────────────────────────────
REQUEST_TIMEOUT_S   = 35    # segundos para el primer pulso
CONFIRM_TIMEOUT_S   = 25    # segundos para el pulso de confirmación
WAKE_PAUSE_S        = 12    # pausa tras detectar status 200 (app cargando)
DELAY_MIN_S         = 2.0   # delay mínimo entre apps (simula tráfico humano)
DELAY_MAX_S         = 5.5   # delay máximo entre apps

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "es-CL,es;q=0.9,en-US;q=0.8",
    "Connection": "keep-alive",
}

# ──────────────────────────────────────────────
#  LÓGICA PRINCIPAL
# ──────────────────────────────────────────────
def wake_up() -> int:
    """
    Recorre todas las apps y envía un doble pulso HTTP.
    Retorna el número de apps que fallaron (útil como exit code).
    """
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"\n{'═'*60}")
    print(f"  STRUCTURAL LAB — Keep-Alive Cycle")
    print(f"  {timestamp}")
    print(f"  Apps en cola: {len(APPS_URLS)}")
    print(f"{'═'*60}\n")

    ok_count    = 0
    error_count = 0

    for idx, url in enumerate(APPS_URLS, start=1):
        app_label = url.split("//")[1].split(".")[0]   # nombre corto para logs
        print(f"[{idx:02d}/{len(APPS_URLS)}] {app_label}")

        try:
            # ── Pulso 1: Despertar ──────────────────────────────
            r1 = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT_S)
            print(f"       Pulso 1 → HTTP {r1.status_code}")

            if r1.status_code == 200:
                # La app está respondiendo; segundo pulso tras pausa corta
                time.sleep(WAKE_PAUSE_S)
                r2 = requests.get(url, headers=HEADERS, timeout=CONFIRM_TIMEOUT_S)
                print(f"       Pulso 2 → HTTP {r2.status_code}  ✅ ACTIVA")
            else:
                # Respuesta inesperada: registrar y continuar
                print(f"       ⚠️  Status inesperado: {r1.status_code}")

            ok_count += 1

        except requests.exceptions.Timeout:
            print(f"       ❌ TIMEOUT — la app no respondió en el tiempo límite.")
            error_count += 1

        except requests.exceptions.ConnectionError as e:
            print(f"       ❌ CONNECTION ERROR — {e}")
            error_count += 1

        except Exception as e:
            print(f"       ❌ ERROR INESPERADO — {type(e).__name__}: {e}")
            error_count += 1

        finally:
            # Delay aleatorio entre peticiones (simula tráfico orgánico)
            if idx < len(APPS_URLS):
                delay = random.uniform(DELAY_MIN_S, DELAY_MAX_S)
                time.sleep(delay)

    # ── Resumen ────────────────────────────────────────────────
    print(f"\n{'─'*60}")
    print(f"  RESUMEN CICLO")
    print(f"  ✅ Apps confirmadas : {ok_count}")
    print(f"  ❌ Apps con error   : {error_count}")
    print(f"{'─'*60}\n")

    return error_count   # 0 = éxito total


if __name__ == "__main__":
    failures = wake_up()
    sys.exit(0 if failures == 0 else 1)
