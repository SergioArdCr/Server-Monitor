import os
from dotenv import load_dotenv

# Rutas y archivos

# Ruta_Base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Ruta_DB = os.path.join(Ruta_Base, "data", "Task_Manager.db")

# .env 

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
EMAIL_TO = os.getenv("EMAIL_DESTINO")