import smtplib

"""El módulo smtplib en Python se usa para enviar correos electrónicos mediante el protocolo SMTP (Simple Mail Transfer 
Protocol). Permite conectarse a servidores de correo, autenticarse y enviar mensajes."""

#Ejemplo básico: enviar un correo con Gmail
#import smtplib 
# Configuración del servidor SMTP de Gmail 
SMTP_SERVER = "smtp.gmail.com" 
SMTP_PORT = 587 
EMAIL = "tu_email@gmail.com" 
PASSWORD = "tu_contraseña" 

# Mensaje 
mensaje = """\ From: tu_email@gmail.com To: destinatario@example.com Subject: Prueba de smtplib Este es un correo enviado desde Python. """ 
# Enviar correo 
with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server: 
    server.starttls() 
# Seguridad 
server.login(EMAIL, PASSWORD) 
# Autenticación 
server.sendmail(EMAIL, "destinatario@example.com", mensaje) 
print("Correo enviado.") 

#Notas:
#Usa starttls() para cifrar la conexión.
#Necesitas una cuenta con acceso SMTP (como Gmail, Outlook).
#En Gmail, podrías necesitar una contraseña de aplicación.


"""Funciones principales de smtplib"""

#smtplib.SMTP(host='', port=0, local_hostname=None, [timeout], [source_address], [context])
#Crea una conexión con un servidor SMTP.
#host: Dirección del servidor SMTP, como "smtp.gmail.com".
#port: Puerto del servidor, comúnmente 587 para TLS o 465 para SSL.
#local_hostname: Nombre del cliente (se detecta automáticamente si no se especifica).
#timeout: Tiempo máximo para la conexión (opcional).
#source_address: Dirección IP desde la cual se inicia la conexión (opcional).
#context: Contexto SSL/TLS (opcional). Ejemplo:
import smtplib 
server = smtplib.SMTP("smtp.gmail.com", 587) 

#smtplib.SMTP_SSL(host='', port=0, local_hostname=None, [timeout], [source_address], [context])
#Igual que SMTP(), pero establece una conexión segura con SSL desde el inicio. Se usa con port=465. Ejemplo:
server = smtplib.SMTP_SSL("smtp.gmail.com", 465) 

#Métodos de SMTP y SMTP_SSL
#.connect(host='', port=0)
#Conecta al servidor SMTP si no se hizo al crear la instancia. Ejemplo:
server = smtplib.SMTP() 
server.connect("smtp.gmail.com", 587) 

#.starttls(context=None)
#Inicia una conexión segura usando TLS. Se debe llamar antes de autenticarse (login). Ejemplo:
server.starttls()

#.login(user, password)
#Inicia sesión en el servidor SMTP. Ejemplo:
server.login("tu_email@gmail.com", "tu_contraseña") 

#.sendmail(from_addr, to_addrs, msg, mail_options=(), rcpt_options=())
#Envía un correo electrónico.
#from_addr: Dirección del remitente.
#to_addrs: Lista de destinatarios.
#msg: Mensaje en formato de texto. Ejemplo:
server.sendmail("tu_email@gmail.com", "destinatario@example.com", "Subject: Hola\n\nMensaje") 

#.quit()
#Cierra la conexión de forma correcta. Ejemplo:
server.quit() 

#.close()
#Cierra la conexión sin enviar el comando QUIT. Ejemplo:
server.close() 

#.ehlo(name='')
#Se identifica ante el servidor SMTP. Es necesario antes de starttls(). Ejemplo:
server.ehlo() 

#.helo(name='')
#Similar a ehlo(), pero usa un saludo más antiguo. Ejemplo:
server.helo() 

#.verify(email)
#Pregunta al servidor si el correo existe. No siempre es compatible. Ejemplo:
response = server.verify("destinatario@example.com") 
print(response) 

#.set_debuglevel(level)
#Activa la depuración para ver detalles de la conexión. Si level=1, se activan los mensajes de depuración. Ejemplo:
server.set_debuglevel(1) 

#.noop()
#Comprueba si el servidor SMTP sigue activo. Ejemplo:
response = server.noop() 
print(response) 

#.rset()
#Restablece la conexión a su estado inicial. Ejemplo:
server.rset() 

#.docmd(cmd, args='')
#Envía un comando SMTP personalizado. Ejemplo:
response = server.docmd("HELP") 
print(response) 


"""El módulo smtplib en Python tiene dos clases principales"""

#1. Clase SMTP
#Es la clase principal para establecer una conexión con un servidor SMTP y enviar correos. Constructor:
#smtplib.SMTP(host='', port=0, local_hostname=None, timeout=None, source_address=None, context=None) 
#host: Dirección del servidor SMTP (por ejemplo, "smtp.gmail.com").
#port: Puerto del servidor (por defecto 25, pero generalmente 587 para TLS).
#local_hostname: Nombre del cliente (se detecta automáticamente si no se especifica).
#timeout: Tiempo máximo de espera para la conexión.
#source_address: Dirección IP de origen (opcional).
#context: Objeto de configuración SSL/TLS (opcional). Ejemplo de uso:
import smtplib 
# Crear una conexión SMTP 
server = smtplib.SMTP("smtp.gmail.com", 587) 
# Iniciar comunicación 
server.ehlo() 
# Habilitar seguridad TLS 
server.starttls() 
# Iniciar sesión 
server.login("tu_email@gmail.com", "tu_contraseña") 
# Enviar correo 
server.sendmail("tu_email@gmail.com", "destinatario@example.com", "Subject: Prueba\n\nEste es un mensaje de prueba.") 
# Cerrar conexión server.quit() 

#2. Clase SMTP_SSL
#Es una subclase de SMTP, pero usa SSL desde el inicio en lugar de establecer la conexión en texto plano. Se usa para conexiones seguras desde el principio (por ejemplo, con port=465). Constructor:
#smtplib.SMTP_SSL(host='', port=0, local_hostname=None, timeout=None, source_address=None, context=None) 
#Los parámetros son los mismos que en SMTP, pero SMTP_SSL usa cifrado SSL de inmediato. Ejemplo de uso:
import smtplib 
# Crear una conexión SMTP con SSL 
server = smtplib.SMTP_SSL("smtp.gmail.com", 465) 
# Iniciar sesión 
server.login("tu_email@gmail.com", "tu_contraseña") 
# Enviar correo 
server.sendmail("tu_email@gmail.com", "destinatario@example.com", "Subject: Prueba\n\nEste es un mensaje seguro.") 
# Cerrar conexión 
server.quit() 

#Diferencias entre SMTP y SMTP_SSL
#SMTP usa una conexión sin cifrar y luego activa TLS con starttls().
#SMTP_SSL usa SSL desde el inicio, sin necesidad de starttls().


"""El módulo smtplib tiene tres variables importantes"""

#1. smtplib.SMTP_PORT
#Representa el puerto predeterminado para conexiones SMTP sin cifrado: 25.
#Si no se especifica un puerto en smtplib.SMTP(), usará este por defecto. Ejemplo:
print(smtplib.SMTP_PORT) # Salida: 25 

#2. smtplib.SMTP_SSL_PORT
#Representa el puerto predeterminado para conexiones seguras con SSL: 465.
#Se usa con smtplib.SMTP_SSL(). Ejemplo:
print(smtplib.SMTP_SSL_PORT) # Salida: 465 

#3. smtplib.CRLF
#Representa la secuencia de caracteres de nueva línea en SMTP: "\r\n".
#En SMTP, los mensajes deben terminar con CRLF para cumplir con el protocolo. Ejemplo:
print(repr(smtplib.CRLF)) # Salida: '\r\n' 

#Uso práctico en un mensaje SMTP manual:
mensaje = "Subject: Hola" + smtplib.CRLF + "Este es un mensaje de prueba." 
print(mensaje) 


"""El módulo smtplib no tiene constantes adicionales aparte de las variables que ya mencioné (SMTP_PORT, SMTP_SSL_PORT y CRLF)."""


"""El módulo smtplib define varias excepciones"""

#1. smtplib.SMTPException
#Es la excepción base para todos los errores en smtplib.
#Todas las demás excepciones heredan de esta.
#Se usa para capturar cualquier error SMTP genérico. Ejemplo:
try: 
    raise smtplib.SMTPException("Error genérico de SMTP")
except smtplib.SMTPException as e:
    print(f"Ocurrió un error SMTP: {e}") 

#2. smtplib.SMTPServerDisconnected
#Se lanza cuando la conexión con el servidor SMTP se interrumpe inesperadamente. Ejemplo:
try: 
    server = smtplib.SMTP("smtp.gmail.com", 587) 
    server.quit() # Se cierra la conexión 
    server.sendmail("correo@gmail.com", "destinatario@example.com", "Mensaje") 
# Error aquí 
except smtplib.SMTPServerDisconnected: 
    print("Error: Conexión con el servidor perdida.") 

#3. smtplib.SMTPResponseException
#Se lanza cuando el servidor responde con un código de error específico.
#Tiene dos atributos importantes: 
#.smtp_code: Código de error SMTP (ej. 550 para "correo no entregado").
#.smtp_error: Mensaje de error del servidor. Ejemplo:
try: 
    raise smtplib.SMTPResponseException(550, "Mailbox unavailable") 
except smtplib.SMTPResponseException as e: 
    print(f"Error {e.smtp_code}: {e.smtp_error}") 

#4. smtplib.SMTPSenderRefused
#Se lanza si el servidor rechaza la dirección del remitente.
#Atributos importantes: 
#.smtp_code: Código de error SMTP.
#.smtp_error: Mensaje de error.
#.sender: Dirección del remitente rechazada. Ejemplo:
try: 
    raise smtplib.SMTPSenderRefused(451, "Sender rejected", "correo@gmail.com") 
except smtplib.SMTPSenderRefused as e: 
    print(f"Error {e.smtp_code}: {e.smtp_error} (Remitente: {e.sender})") 

#5. smtplib.SMTPRecipientsRefused
#Se lanza si el servidor rechaza todos los destinatarios.
#Contiene un diccionario con los destinatarios rechazados y sus códigos de error. Ejemplo:
try: 
    raise smtplib.SMTPRecipientsRefused({"destinatario@example.com": (550, "Mailbox unavailable")}) 
except smtplib.SMTPRecipientsRefused as e: 
    print(f"Destinatario rechazado: {e.recipients}") 

#6. smtplib.SMTPDataError
#Se lanza si el servidor SMTP rechaza el contenido del correo después de enviarlo. Ejemplo:
try: 
    raise smtplib.SMTPDataError(554, "Message rejected") 
except smtplib.SMTPDataError as e: 
    print(f"Error {e.smtp_code}: {e.smtp_error}") 

#7. smtplib.SMTPHeloError
#Se lanza si el servidor SMTP rechaza el saludo HELO o EHLO. Ejemplo:
try: 
    raise smtplib.SMTPHeloError(501, "Invalid HELO") 
except smtplib.SMTPHeloError as e: 
    print(f"Error {e.smtp_code}: {e.smtp_error}") 

#8. smtplib.SMTPNotSupportedError
#Se lanza si se intenta usar una función no compatible con el servidor.
#Por ejemplo, si el servidor no soporta starttls(). Ejemplo:
try: 
    raise smtplib.SMTPNotSupportedError("TLS no soportado") 
except smtplib.SMTPNotSupportedError as e: 
    print(f"Error: {e}") 

#9. smtplib.SMTPAuthenticationError
#Se lanza cuando la autenticación con login(user, password) falla.
#Tiene dos atributos: 
#.smtp_code: Código de error.
#.smtp_error: Mensaje del servidor. Ejemplo:
try: 
    raise smtplib.SMTPAuthenticationError(535, "Incorrect password") 
except smtplib.SMTPAuthenticationError as e: 
    print(f"Error {e.smtp_code}: {e.smtp_error}") 


"""El módulo smtplib no tiene submódulos. Es un módulo independiente dentro de la biblioteca estándar de Python y no 
contiene otros módulos internos."""

