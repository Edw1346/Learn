#El módulo email se usa para crear, manipular y analizar mensajes de correo electrónico. Permite construir correos con texto, HTML, archivos adjuntos y encabezados personalizados.
#Uso básico: Para crear y enviar un correo con email y smtplib:

import smtplib 
from email.mime.text import MIMEText 
# Crear el mensaje 
mensaje = MIMEText("Este es un correo de prueba") 
mensaje["Subject"] = "Prueba" 
mensaje["From"] = "elopez2215806@gmail.com"
mensaje["To"] = "edwinmi4828@gmail.com"
print(mensaje)
mensaje.set_payload("Este es el cuerpo del mensaje.") 

# Enviar el correo 
SMTP_SERVER = "smtp.gmail.com" 
SMTP_PORT = 587 
EMAIL = "edwinmi4828@gmail.com" 
PASSWORD = "xdps dxay oftc ndxo" 
EMAIL_REM = "elopez2215806@gmail.com"


server = smtplib.SMTP("smtp.gmail.com", 587) 
server.connect(SMTP_SERVER, SMTP_PORT) 
server.ehlo(name="Guapo") 
server.starttls()
server.login(EMAIL,PASSWORD) 
#server.sendmail(EMAIL, EMAIL_REM, mensaje) 
server.quit() 
server.close() 

#El módulo email en Python no es un módulo con funciones directas como smtplib, sino que es un paquete 
# que contiene varios submódulos con clases y funciones para construir y analizar correos electrónicos.

#email.message (Construcción de mensajes) email.message_from_bytes(bytes) Convierte un correo en formato bytes 
# a un objeto Message. Se usa para procesar correos en formato binario (por ejemplo, de un archivo .eml). Ejemplo:
from email import message_from_bytes 
correo_bytes = b"Subject: Hola\n\nMensaje de prueba" 
mensaje = message_from_bytes(correo_bytes) 
print(mensaje["Subject"]) # Salida: Hola 

#email.message_from_string(string) Similar a message_from_bytes(), pero acepta una cadena de texto en lugar de bytes:
from email import message_from_string 
correo_str = "Subject: Hola\n\nMensaje de prueba" 
mensaje = message_from_string(correo_str) 
print(mensaje.get_payload()) # Salida: Mensaje de prueba 

#email.mime (Construcción de correos MIME) MIMEText(texto, subtype="plain", charset="utf-8") Crea un mensaje de texto con formato MIME.
#subtype="plain" es texto sin formato, pero también puede ser "html". Ejemplo:
from email.mime.text import MIMEText 
mensaje = MIMEText("Este es el cuerpo del correo", "plain", "utf-8") 
print(mensaje.as_string()) 

#MIMEImage(datos, subtype="jpeg") Crea un mensaje MIME con una imagen. Ejemplo:
from email.mime.image import MIMEImage 
with open("imagen.jpg", "rb") as img: 
    mensaje = MIMEImage(img.read(), "jpeg") 

#MIMEMultipart(subtype="mixed") Permite crear correos con múltiples partes (texto, imágenes, adjuntos). Ejemplo:
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
mensaje = MIMEMultipart() 
mensaje.attach(MIMEText("Este es un correo con adjuntos", "plain")) 

#email.utils (Funciones de utilidad para correos) email.utils.formataddr((nombre, correo)) Formatea un nombre y una dirección de correo en un solo string. Ejemplo:
from email.utils import formataddr 
remitente = formataddr(("Mi Nombre", "miemail@gmail.com")) 
print(remitente) # Salida: Mi Nombre <miemail@gmail.com> 

#email.utils.parseaddr(cadena) Extrae el nombre y la dirección de correo de un string. Ejemplo:
from email.utils import parseaddr 
nombre, correo = parseaddr("Mi Nombre <miemail@gmail.com>") 
print(nombre) # Salida: Mi Nombre 
print(correo) # Salida: miemail@gmail.com 

#email.utils.formatdate(timeval=None, localtime=False, usegmt=False) Genera una fecha en formato RFC 2822 para el encabezado Date. Ejemplo:
from email.utils import formatdate 
print(formatdate()) # Salida: Tue, 20 Feb 2025 12:34:56 +0000 

# email.header (Codificación de encabezados) email.header.make_header(lista_codificada) Crea un encabezado codificado con caracteres especiales (como acentos). Ejemplo:
from email.header import make_header 
encabezado = make_header([("Correo con áccéntós", "utf-8")])
print(str(encabezado)) # Salida: Correo con áccéntós 

#email.header.decode_header(header_value) Decodifica un encabezado de correo con caracteres especiales. Ejemplo:
from email.header import decode_header 
resultado = decode_header("=?utf-8?b?Q29ycmVvIGNvbiDDsWFjY2VudMOzcw==?=") 
print(resultado) # Salida: [(b'Correo con áccéntós', 'utf-8')] 



#email.mime.base.MIMEBase Es una clase base para crear mensajes MIME de tipo general (como imágenes, documentos, archivos comprimidos, etc.). Se utiliza en conjunto con otras clases MIME (como MIMEImage, MIMEAudio, MIMEApplication, etc.) para especificar el tipo de archivo adjunto. Ejemplo:
from email.mime.base import MIMEBase 
from email import encoders 
mensaje = MIMEBase("application", "octet-stream") 
mensaje.set_payload(open("archivo.txt", "rb").read()) 
encoders.encode_base64(mensaje) 
mensaje.add_header("Content-Disposition", "attachment", filename="archivo.txt") 

#email.mime.image.MIMEImage Se usa para enviar imágenes en correos electrónicos. Permite adjuntar imágenes en formatos como JPEG, PNG, etc. Ejemplo:
from email.mime.image import MIMEImage 
with open("imagen.jpg", "rb") as f: 
    imagen = MIMEImage(f.read()) 
    print(imagen.as_string()) 

#email.header.Header Esta clase se utiliza para manejar los encabezados de los correos electrónicos, como el Subject, que pueden contener caracteres no ASCII (como acentos, símbolos, etc.). La clase se encarga de codificar y decodificar los encabezados en el formato adecuado para el correo. Ejemplo:
from email.header import Header 
encabezado = Header("Correo con acentos", "utf-8") 
print(encabezado.encode()) # Salida: =?utf-8?b?Q29ycmVvIGNvbiBhY2VudG9z?= 

"""email.utils (Funciones de utilidad) Aunque no es una clase, el submódulo email.utils contiene varias funciones útiles para 

trabajar con direcciones de correo electrónico y fechas. Algunas de las funciones más comunes son:
formataddr(): Formatea una dirección de correo con el nombre.
parseaddr(): Extrae el nombre y la dirección de un string.
formatdate(): Genera una fecha en formato RFC 2822 para usar en el encabezado Date. Ejemplo:"""
from email.utils import formataddr, parseaddr 
email_formateado = formataddr(("Mi Nombre", "miemail@gmail.com")) 
nombre, correo = parseaddr("Mi Nombre <miemail@gmail.com>") 
print(email_formateado) # Salida: Mi Nombre <miemail@gmail.com> 






#El módulo email en Python no tiene muchas variables definidas directamente. Sin embargo, contiene algunas constantes y valores predefinidos que se utilizan principalmente en el manejo de los encabezados y en la codificación de mensajes. 

#email.encoders.encode_base64() Aunque no es exactamente una variable, esta función codifica el contenido en base64. Es importante para los adjuntos y otros datos binarios dentro de los correos.

#email.header.decode_header() (Retorno de tuplas con codificación) La función decode_header devuelve una lista de tuplas con los valores codificados de los encabezados, especificando el texto decodificado y el conjunto de caracteres utilizado.
from email.header import decode_header 
result = decode_header("=?utf-8?b?U29ycnkgR2VzdHM=?=") 
print(result) # Devuelve: [(b'Sorry Gets', 'utf-8')] 

#email.header.PARAMS Es una constante que se encuentra dentro de email.header, la cual se usa para separar parámetros en los encabezados, por ejemplo, el tipo de contenido en el encabezado Content-Type.







#El módulo email incluye algunas constantes que se utilizan principalmente para manejar la codificación, el formato y las políticas de los correos electrónicos. 

#email.header.MAXLINE Esta constante define la longitud máxima permitida para una línea de encabezado en un correo electrónico. Si una línea de encabezado supera este valor, se debe dividir en varias líneas.
from email.header import MAXLINE 
print(MAXLINE) # Muestra el valor máximo de longitud de línea para un encabezado 

#email.utils.MAX_HEADER_SIZE Esta es una constante en el submódulo email.utils que define el tamaño máximo permitido para los encabezados de los correos electrónicos en bytes. Este valor puede ser útil si estás trabajando con encabezados muy largos.
from email.utils import MAX_HEADER_SIZE 
print(MAX_HEADER_SIZE) # Muestra el valor máximo de tamaño de encabezado 

#email.policy.default El módulo email usa el submódulo policy para definir las reglas de cómo manejar los correos electrónicos, como la codificación y el formato. default es el valor de política por defecto que controla cómo se tratan los correos electrónicos y sus partes:
from email import policy 
print(policy.default) # Muestra la política por defecto 

#email.charset.CHARSET Es una constante relacionada con la codificación de caracteres. Es útil cuando trabajas con correos que contienen caracteres no ASCII. Aunque CHARSET no se usa directamente para crear correos, es importante en el manejo de las cabeceras y cuerpos de los mensajes cuando se trata de codificar caracteres especiales.

#email.header._MAXLINELEN Esta constante también se encuentra en el submódulo header y se refiere al límite de longitud de una línea en el encabezado de un correo. Está relacionada con la constante MAXLINE pero es interna y se usa más a menudo en la implementación interna del módulo.

#email.mime.base.MIMEBase Aunque MIMEBase no es una constante, se puede considerar una clase clave para representar el contenido genérico de un mensaje MIME, que se utiliza para archivos adjuntos u otros tipos de contenido. Puedes usarla para crear mensajes con contenido binario.





#El módulo email de Python no define excepciones propias de manera explícita, pero puede generar algunas excepciones relacionadas con errores comunes que ocurren al manipular correos electrónicos. Estas excepciones son más bien derivadas de las excepciones estándar de Python. 

#. email.errors.MessageError Esta es la excepción base para los errores relacionados con los mensajes de correo. Se utiliza cuando algo sale mal al crear, procesar o analizar un mensaje. Ejemplo de uso: Podría ocurrir si intentas acceder a una parte del mensaje que no existe o si hay un error de formato. 
from email.errors import MessageError 
try: # Supón que intentas crear un mensaje malformado 
    raise MessageError("Error al procesar el mensaje.") 
except MessageError as e: print(f"Excepción capturada: {e}") 

#. email.errors.HeaderParseError Esta excepción se lanza cuando hay un error en el análisis del encabezado de un correo electrónico. Puede ocurrir si los encabezados no cumplen con el formato adecuado o si los datos de un encabezado no son válidos. Ejemplo de uso: Si el encabezado del correo está malformado o no se puede analizar correctamente.
from email.errors import HeaderParseError 
try: # Supón que el encabezado está malformado 
    raise HeaderParseError("Error al analizar el encabezado.") 
except HeaderParseError as e: print(f"Excepción capturada: {e}") 

#email.errors.MimeParseError Esta excepción ocurre cuando hay un error en el análisis de una estructura MIME. Si intentas crear un mensaje MIME incorrecto o malformado, se puede generar esta excepción. Ejemplo de uso: Si se está creando un mensaje MIME con partes mal formadas o no válidas.
from email.errors import MimeParseError 
try: # Supón que el contenido MIME está malformado 
    raise MimeParseError("Error en el análisis MIME.") 
except MimeParseError as e: print(f"Excepción capturada: {e}") 

# email.errors.EncodedWordsError Esta excepción se lanza cuando hay un error al tratar de decodificar o analizar palabras codificadas en los encabezados de un correo electrónico (por ejemplo, en el campo Subject). Esto es común cuando los encabezados contienen caracteres no ASCII que deben ser decodificados correctamente. Ejemplo de uso: Si el encabezado no puede ser decodificado correctamente.
from email.errors import EncodedWordsError 
try: # Simula un error en la decodificación de palabras codificadas 
    raise EncodedWordsError("Error al decodificar las palabras codificadas.") 
except EncodedWordsError as e: print(f"Excepción capturada: {e}") 

#email.mime.base.MIMEBaseError Aunque no es una excepción estándar, la clase base MIMEBase de email.mime.base puede generar errores si se usa incorrectamente o si el tipo de contenido no es adecuado.

# Excepciones Generales de Python El módulo email también puede generar excepciones más generales como:
#TypeError: Si los datos proporcionados no son del tipo adecuado (por ejemplo, pasando una cadena de texto cuando se esperaba un byte).
#ValueError: Si hay un valor no válido en los encabezados, en el cuerpo del mensaje o en cualquier otra parte del correo.



#El módulo email incluye varios submódulos que facilitan el trabajo con correos electrónicos, desde la creación de mensajes hasta el análisis de los mismos. 

#email.message Este submódulo contiene la clase Message, que es la base para la creación y manipulación de mensajes de correo electrónico. Permite acceder a los encabezados del mensaje, establecer el cuerpo, y obtener o modificar las partes del correo. 
#Clases principales: Message. Función principal: Message() permite crear un nuevo mensaje de correo, manipular sus partes, y obtener la información de los encabezados.
from email.message import Message 
mensaje = Message() 
mensaje["From"] = "miemail@example.com" 
mensaje.set_payload("Este es el cuerpo del mensaje.") 

""". email.mime El submódulo mime se utiliza para manejar el tipo MIME (Multipurpose Internet Mail Extensions) de los mensajes de correo electrónico. Permite crear mensajes con contenido multimedia, como imágenes, archivos adjuntos y diferentes tipos de texto.Dentro de email.mime, hay varios submódulos:
email.mime.text: Se usa para crear mensajes de texto, tanto en formato plano como HTML.
email.mime.multipart: Permite crear mensajes que contienen múltiples partes, como texto y archivos adjuntos.
email.mime.base: Contiene la clase MIMEBase, que se utiliza para definir tipos MIME genéricos (como archivos adjuntos).
email.mime.image: Se usa para crear mensajes que contienen imágenes.
email.mime.audio: Permite manejar archivos de audio.
email.mime.application: Se usa para archivos que no se corresponden con los tipos anteriores, como documentos PDF.""" 
from email.mime.text import MIMEText 
mensaje = MIMEText("Este es un mensaje de texto", "plain") 

"""email.utils Este submódulo contiene funciones útiles para trabajar con direcciones de correo electrónico, fechas y otros datos relacionados con el correo electrónico. Algunas de las funciones más comunes son:
formataddr(): Formatea una dirección de correo electrónico con el nombre.
parseaddr(): Extrae la dirección y el nombre de un campo de texto.
make_msgid(): Genera un identificador único para un mensaje de correo electrónico.
getaddresses(): Devuelve una lista de direcciones a partir de una cadena que puede contener múltiples direcciones:"""
from email.utils import formataddr 
direccion = formataddr(("Nombre", "correo@example.com")) 
print(direccion) # Salida: "Nombre" <correo@example.com> 

""". email.header Este submódulo proporciona funciones y clases para manejar los encabezados de los correos electrónicos. Las funciones comunes son: decode_header(): Decodifica los encabezados que contienen texto codificado.
Header(): Esta clase se usa para crear encabezados codificados:"""
from email.header import decode_header 
encabezado_decodificado = decode_header("=?utf-8?b?U29ycnkgR2VzdHM=?=") 
print(encabezado_decodificado) # Decodifica el encabezado 

""" email.policy El submódulo policy contiene clases que definen las políticas de codificación y formato que deben seguir los correos electrónicos. Por ejemplo, default es la política predeterminada que se utiliza para controlar la creación y el análisis de los mensajes. Clases principales: default Se usa para aplicar reglas sobre cómo tratar el formato de los correos electrónicos y sus partes:"""
from email import policy 
print(policy.default) # Muestra la política predeterminada 

""" email.charset Este submódulo se usa para manejar la codificación de caracteres de los mensajes. Contiene utilidades para manejar los conjuntos de caracteres, como UTF-8, ISO-8859-1, entre otros. Es importante cuando trabajas con correos electrónicos que contienen caracteres no ASCII."""
