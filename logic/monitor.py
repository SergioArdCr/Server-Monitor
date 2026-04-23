import httpx
import asyncio
from datetime import datetime, timezone
from logic.db import SessionLocal, Monitor
from logic.alertas import send_email

# Lista de URLs a monitorear
URLS = [
    "https://task-manager-api-production-36bd.up.railway.app",
    "https://apiadidassalesreport-production.up.railway.app",
    "https://google.com",
    "https://esta-url-no-existe-123456.com",
]

urls_alertadas = set()

async def chequear_url(url: str):
    inicio = datetime.now()
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(url)
            tiempo_ms = int((datetime.now() - inicio).total_seconds() * 1000)
            estado = "online" if response.status_code < 500 else "offline"
            codigo_http = response.status_code
    except Exception:
        tiempo_ms = int((datetime.now() - inicio).total_seconds() * 1000)
        estado = "offline"
        codigo_http = 0

    # Guardar en BD
    db = SessionLocal()
    registro = Monitor(
        url=url,
        estado=estado,
        codigo_http=codigo_http,
        tiempo_ms=tiempo_ms,
        chequeado_en=datetime.now()
    )
    db.add(registro)
    db.commit()
    db.close()

    print(f"[{estado.upper()}] {url} — {codigo_http} — {tiempo_ms}ms")

    # Enviar alerta si está caído
    if estado == "offline" and url not in urls_alertadas:
        send_email(url, codigo_http)
        urls_alertadas.add(url)

async def chequear_todas():
    print(f"\n🔍 Chequeando {len(URLS)} URLs — {datetime.now().strftime('%H:%M:%S')}")
    await asyncio.gather(*[chequear_url(url) for url in URLS])