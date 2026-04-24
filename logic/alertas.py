import smtplib
from config.settings import EMAIL, PASSWORD, EMAIL_TO
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(url: str, codigo_http: int):
    
    try:

        new_email = create_email(url, codigo_http)
        with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
            servidor.ehlo()
            servidor.starttls()
            servidor.ehlo()
            servidor.login(EMAIL, PASSWORD)
            servidor.sendmail(EMAIL, EMAIL_TO, new_email.as_string())
        
    except smtplib.SMTPAuthenticationError:
        print("Error: credenciales incorrectas, verifica el .env")
    except smtplib.SMTPException as e:
        print(f"Error al enviar el correo: {e}")
    

def create_email(url: str, codigo_http: int):
    mensaje = MIMEMultipart()
    mensaje["From"] = EMAIL
    mensaje["To"] = EMAIL_TO
    mensaje["Subject"] = f"🚨 Alerta: {url} está caído"

    EMAIL_BODY = f"""Buen día,

                Se detectó que el siguiente servidor no está respondiendo:

                URL: {url}
                Código HTTP: {codigo_http}

                Por favor revisa el servidor.

                Monitor automático."""


    mensaje.attach(MIMEText(EMAIL_BODY, "plain"))
    return mensaje