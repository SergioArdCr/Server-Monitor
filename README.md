# 🖥️ Server Monitor (Español)

---

## 📌 Descripción

Script de automatización que monitorea la disponibilidad de servidores en tiempo real. Chequea múltiples URLs en paralelo usando programación asíncrona, guarda el historial de resultados en PostgreSQL y envía alertas por correo cuando detecta que un servidor está caído.

Proyecto desarrollado como parte de un plan de aprendizaje de Python enfocado en desarrollo backend y automatización de procesos.

**GitHub:** https://github.com/SergioArdCr/Server-Monitor

## 🛠️ Tecnologías

- `httpx` — cliente HTTP asíncrono para chequear URLs
- `asyncio` — programación asíncrona para chequear múltiples URLs en paralelo
- `schedule` — ejecución periódica del monitor
- `SQLAlchemy` — ORM para manejo de base de datos
- `PostgreSQL` — almacenamiento del historial de chequeos
- `smtplib` — envío de alertas por correo

## 📁 Estructura

```
W18-Server-Monitor/
├── main.py
├── .env
├── .gitignore
├── config/
│   └── settings.py
├── logic/
│   ├── db.py
│   ├── monitor.py
│   └── alertas.py
└── data/
```

## ⚙️ Instalación

```bash
# Clonar el repositorio
git clone https://github.com/SergioArdCr/Server-Monitor.git
cd Server-Monitor

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus valores

# Correr el monitor
python main.py
```

## 🔐 Variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/server_monitor
SMTP_EMAIL=tu_correo@gmail.com
SMTP_PASSWORD=tu_contraseña_de_aplicacion
EMAIL_DESTINO=correo_destino@gmail.com
```

## 🗃️ Modelo de base de datos

```
monitor
├── id           — identificador único
├── url          — URL chequeada
├── estado       — "online" o "offline"
├── codigo_http  — código de respuesta HTTP (200, 404, 500, 0)
├── tiempo_ms    — tiempo de respuesta en milisegundos
└── chequeado_en — fecha y hora del chequeo
```

## 💡 Ejemplo de uso

```python
# Agregar URLs a monitorear en logic/monitor.py
URLS = [
    "https://tu-api.up.railway.app",
    "https://otro-servidor.com",
    "https://google.com",
]

# Correr el monitor
python main.py
```

```
🟢 Monitor iniciado — chequeando cada 5 minutos
🔍 Chequeando 3 URLs — 22:00:01
[ONLINE]  https://google.com — 200 — 312ms
[ONLINE]  https://tu-api.up.railway.app — 200 — 1243ms
[OFFLINE] https://otro-servidor.com — 0 — 153ms
✅ Alerta enviada para https://otro-servidor.com
```

## 📧 Alerta de correo

Cuando se detecta un servidor caído, se envía automáticamente un correo con el siguiente formato:

```
Asunto: 🚨 Alerta: https://otro-servidor.com está caído

Buen día,

Se detectó que el siguiente servidor no está respondiendo:

  URL: https://otro-servidor.com
  Código HTTP: 0

Por favor revisa el servidor.

Monitor automático.
```

## 💡 Aprendizajes clave

- Programación asíncrona con `asyncio` — chequeo de múltiples URLs en paralelo
- `asyncio.gather()` para ejecutar corrutinas concurrentemente
- `asyncio.run()` como puente entre código síncrono y asíncrono
- Cliente HTTP asíncrono con `httpx.AsyncClient`
- Protocolo SMTP correcto — `ehlo()` antes y después de `starttls()`
- `sendmail` vs `send_message` — cuándo usar cada uno
- Entornos virtuales con `venv` — aislamiento de dependencias
- Datetime consciente de timezone con `datetime.now(timezone.utc)`
- Guardado de historial en PostgreSQL con SQLAlchemy

---

---

# 🖥️ Server Monitor (English)

---

## 📌 Description

Automation script that monitors server availability in real time. Checks multiple URLs in parallel using asynchronous programming, saves results history in PostgreSQL, and sends email alerts when a server goes down.

Built as part of a Python learning plan focused on backend development and process automation.

**GitHub:** https://github.com/SergioArdCr/Server-Monitor

## 🛠️ Tech Stack

- `httpx` — async HTTP client for checking URLs
- `asyncio` — asynchronous programming to check multiple URLs in parallel
- `schedule` — periodic execution of the monitor
- `SQLAlchemy` — ORM for database management
- `PostgreSQL` — storage for check history
- `smtplib` — email alert delivery

## 📁 Structure

```
W18-Server-Monitor/
├── main.py
├── .env
├── .gitignore
├── config/
│   └── settings.py
├── logic/
│   ├── db.py
│   ├── monitor.py
│   └── alertas.py
└── data/
```

## ⚙️ Setup

```bash
# Clone the repository
git clone https://github.com/SergioArdCr/Server-Monitor.git
cd Server-Monitor

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your values

# Run the monitor
python main.py
```

## 🔐 Environment Variables

Create a `.env` file at the project root:

```
DATABASE_URL=postgresql://user:password@localhost:5432/server_monitor
SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_app_password
EMAIL_DESTINO=destination_email@gmail.com
```

## 🗃️ Database Model

```
monitor
├── id           — unique identifier
├── url          — checked URL
├── estado       — "online" or "offline"
├── codigo_http  — HTTP response code (200, 404, 500, 0)
├── tiempo_ms    — response time in milliseconds
└── chequeado_en — check timestamp
```

## 💡 Usage Example

```python
# Add URLs to monitor in logic/monitor.py
URLS = [
    "https://your-api.up.railway.app",
    "https://another-server.com",
    "https://google.com",
]

# Run the monitor
python main.py
```

```
🟢 Monitor started — checking every 5 minutes
🔍 Checking 3 URLs — 22:00:01
[ONLINE]  https://google.com — 200 — 312ms
[ONLINE]  https://your-api.up.railway.app — 200 — 1243ms
[OFFLINE] https://another-server.com — 0 — 153ms
✅ Alert sent for https://another-server.com
```

## 📧 Email Alert

When a server goes down, an email is automatically sent in the following format:

```
Subject: 🚨 Alert: https://another-server.com is down

Hello,

The following server is not responding:

  URL: https://another-server.com
  HTTP Code: 0

Please check the server.

Automatic Monitor.
```

## 💡 Key Learnings

- Asynchronous programming with `asyncio` — parallel URL checking
- `asyncio.gather()` to run coroutines concurrently
- `asyncio.run()` as bridge between sync and async code
- Async HTTP client with `httpx.AsyncClient`
- Correct SMTP protocol — `ehlo()` before and after `starttls()`
- `sendmail` vs `send_message` — when to use each
- Virtual environments with `venv` — dependency isolation
- Timezone-aware datetime with `datetime.now(timezone.utc)`
- History storage in PostgreSQL with SQLAlchemy
