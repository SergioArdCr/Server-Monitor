import smtplib
from config.settings import EMAIL, PASSWORD, EMAIL_TO
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(url: str, codigo_http: int):
    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(EMAIL, PASSWORD)
        
        new_email = create_email(url, codigo_http)

        servidor.send_message(new_email)
        servidor.quit()
        
    except smtplib.SMTPAuthenticationError:
        print("Error: credenciales incorrectas, verifica el .env")
    except smtplib.SMTPException as e:
        print(f"Error al enviar el correo: {e}")
    

def create_email(url: str, codigo_http: int):
    mensaje = MIMEMultipart()
    mensaje["From"] = EMAIL
    mensaje["To"] = ",".join(EMAIL_TO)
    mensaje["Subject"] = f"🚨 Alerta: {url} está caído"

    EMAIL_BODY = f"""Buen día,

                Se detectó que el siguiente servidor no está respondiendo:

                URL: {url}
                Código HTTP: {codigo_http}

                Por favor revisa el servidor.

                Monitor automático."""


    mensaje.attach(MIMEText(EMAIL_BODY, "plain"))
    return mensaje