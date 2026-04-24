import smtplib
from config.settings import EMAIL, PASSWORD, EMAIL_TO
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class New_Email:

    def __init__(self, url: str, codigo_http: int):
        self.url = url
        self.codigo_http = codigo_http
        self.send_email()

    def send_email(self):
        
        try:
            new_email = self.create_email(self.url, self.codigo_http)
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
        

    def create_email(self, url: str, codigo_http: int):
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