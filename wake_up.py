"""
wake_up.py — Structural Lab | Keep-Alive con Playwright
"""

import asyncio
import sys
import random
from datetime import datetime
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout

APPS_URLS = [
    ("Viento NCh432",        "https://mauricioriquelmea-sys-windload-viento-nch432-lzwdzg.streamlit.app/"),
    ("Sobrecarga de Uso",    "https://m9plmxftfpszdjvacinftg.streamlit.app/"),
    ("Nieve / Sismo Sec.",   "https://bjtx5s2rdy5ekuokhjl8v9.streamlit.app/"),
    ("Mullion",              "https://mullion-atkbmf2cnuqksoxyt8izct.streamlit.app/"),
    ("Travesaño",            "https://travesano-eusssrykqfvpyngtr9vzpv.streamlit.app/"),
    ("Silicona Estructural", "https://5m88qekh7gcrydaqy7x6xg.streamlit.app/"),
    ("Cinta 3M",             "https://cinta3m-wnepapp6esbay9pzmy8dgqi.streamlit.app/"),
    ("Torque",               "https://torque-slfubklryxkgpwanza9x3p.streamlit.app/"),
    ("Anclaje Químico",      "https://quimico-2pbzdm3zby4da8kzka8nhm.streamlit.app/"),
    ("Expansión",            "https://expansion-upr2xinenp8sosay8zmqud.streamlit.app/"),
    ("Perno / Tornillo",     "https://pernotornillo-dfxkvxnfnurkgzmnaknsx6.streamlit.app/"),
    ("Engine TopGal",        "https://engine-topgal-kqziwaj4vqugpluyepzban.streamlit.app/"),
    ("Ventana",              "https://ventana-bkswzb7jhr4w8crprwwjb9.streamlit.app/"),
    ("Unidades",             "https://unidades-wehz8ayjfpy6uxlzvf2fb9.streamlit.app/"),
    ("SBT",                  "https://7qmsvcrwsafxzgp8icsncu.streamlit.app/"),
    ("Grúa / ForkLoad",      "https://jexexkgjqv5hoiys9jx4it.streamlit.app/"),
    ("Muro de Contención",   "https://murocontencion-jsfrrr5jqijr3kqnmjpadz.streamlit.app/"),
]

PAGE_TIMEOUT_MS = 60_000
WAKE_WAIT_MS    = 15_000
DELAY_MIN_S     = 2.0
DELAY_MAX_S     = 4.0

SLEEPING_SIGNALS = ["This app has gone to sleep", "Zzzz", "zzzz", "Wake up"]

async def wake_single(browser, idx, total, name, url):
    print(f"[{idx:02d}/{total}] {name}")
    context = await browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        viewport={"width": 1280, "height": 800},
    )
    page = await context.new_page()
    try:
        await page.goto(url, timeout=PAGE_TIMEOUT_MS, wait_until="domcontentloaded")
        content = await page.content()
        is_sleeping = any(s in content for s in SLEEPING_SIGNALS)

        if is_sleeping:
            print(f"       💤 Dormida — despertando...")
            clicked = False
            # Intento 1: botón dentro de iframe
            try:
                frame = page.frame_locator("iframe").first
                btn = frame.locator("text=Yes, get this app back up!")
                await btn.click(timeout=15_000)
                clicked = True
                print(f"       🔔 Botón clickeado (iframe)")
            except Exception:
                pass
            # Intento 2: botón directo en la página
            if not clicked:
                try:
                    await page.click("text=Yes, get this app back up!", timeout=10_000)
                    clicked = True
                    print(f"       🔔 Botón clickeado (página)")
                except Exception:
                    pass
            if not clicked:
                print(f"       ⚠️  Botón no encontrado — señal de visita enviada")
            await page.wait_for_timeout(WAKE_WAIT_MS)
            content2 = await page.content()
            if any(s in content2 for s in SLEEPING_SIGNALS):
                print(f"       ⚠️  Aún cargando — esperar próximo ciclo")
            else:
                print(f"       ✅ ACTIVA")
        else:
            print(f"       ✅ YA ESTABA ACTIVA")
        return True

    except PlaywrightTimeout:
        print(f"       ❌ TIMEOUT")
        return False
    except Exception as e:
        print(f"       ❌ ERROR — {type(e).__name__}: {e}")
        return False
    finally:
        await context.close()

async def wake_all():
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    total = len(APPS_URLS)
    print(f"\n{'═'*55}")
    print(f"  STRUCTURAL LAB — Keep-Alive (Playwright)")
    print(f"  {timestamp}  |  Apps: {total}")
    print(f"{'═'*55}\n")

    ok = errors = 0
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"],
        )
        for idx, (name, url) in enumerate(APPS_URLS, start=1):
            success = await wake_single(browser, idx, total, name, url)
            if success: ok += 1
            else: errors += 1
            if idx < total:
                await asyncio.sleep(random.uniform(DELAY_MIN_S, DELAY_MAX_S))
        await browser.close()

    print(f"\n{'─'*55}")
    print(f"  ✅ OK: {ok}   ❌ Errores: {errors}")
    print(f"{'─'*55}\n")
    return errors

if __name__ == "__main__":
    sys.exit(0 if asyncio.run(wake_all()) == 0 else 1)