import schedule
import time
import asyncio
from logic.monitor import chequear_todas

def job():
    asyncio.run(chequear_todas())

# Chequea cada 5 minutos
schedule.every(5).minutes.do(job)

if __name__ == "__main__":
    print("🟢 Monitor iniciado — chequeando cada 5 minutos")
    job()  # corre inmediatamente al iniciar
    while True:
        schedule.run_pending()
        time.sleep(1)