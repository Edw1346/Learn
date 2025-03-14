import http.server


"""El módulo http.server de Python proporciona una forma sencilla de crear un servidor HTTP básico para probar y servir 
contenido web en un entorno local. Es útil principalmente para desarrollo y pruebas, no para producción, ya que carece 
de muchas características de seguridad y rendimiento que un servidor real como Nginx o Apache ofrece."""

#Características Principales
#Servir archivos estáticos: Puedes configurar un servidor que sirva archivos desde un directorio local.
#Desarrollo y pruebas: Ideal para probar tus aplicaciones web en un entorno controlado.
#Extensible: Puedes personalizar el comportamiento del servidor creando tus propios manejadores de solicitudes.

#Clases Principales
#http.server.SimpleHTTPRequestHandler. Este es el manejador de solicitudes predeterminado. Sirve archivos desde el directorio actual. Qué hace: Inicia un servidor en el puerto 8000 que servirá archivos desde el directorio donde se ejecuta el script.
#http.server.BaseHTTPRequestHandler. Clase base para manejar las solicitudes HTTP. Puedes crear tu propia clase heredando de esta y sobrescribiendo métodos como do_GET(), do_POST(), etc., para personalizar el manejo de las solicitudes.

#Cómo Usarlo
#Servidor Básico: Simplemente usa http.server para iniciar un servidor que sirva archivos estáticos desde un directorio. Por ejemplo, si ejecutas el script en el directorio de tu proyecto, podrás acceder a los archivos del directorio en tu navegador usando http://localhost:8000.
#Servidor Personalizado: Si necesitas más control sobre cómo se manejan las solicitudes (como el manejo de GET, POST, etc.), puedes crear una clase personalizada que herede de BaseHTTPRequestHandler.


"""Funciones del Módulo http.server"""

#http.server.test(): Esta función ejecuta un servidor HTTP básico para pruebas, utilizando el manejador SimpleHTTPRequestHandler por defecto. El servidor se ejecuta en el puerto 8000 de forma predeterminada. Ejemplo: 
http.server.test() 
http.server.serve_forever()

#Este método se utiliza dentro de un servidor, como TCPServer o HTTPServer, para mantenerlo corriendo indefinidamente y atender solicitudes. Ejemplo de uso (en un servidor personalizado): 
from http.server import HTTPServer, BaseHTTPRequestHandler 
class MiManejador(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200) 
        self.send_header('Content-type', 'text/html') 
        self.end_headers() 
        self.wfile.write(b"¡Hola Mundo!")

httpd = HTTPServer(('localhost', 8080), MiManejador) 
httpd.serve_forever() # El servidor se mantendrá activo. 

#http.server.shutdown(). Se utiliza para detener un servidor en ejecución de manera controlada. Ejemplo de uso (en un servidor personalizado): 
from http.server import HTTPServer, BaseHTTPRequestHandler 
class MiManejador(BaseHTTPRequestHandler): 
    def do_GET(self): 
        self.send_response(200) 
        self.send_header('Content-type', 'text/html') 
        self.end_headers() 
        self.wfile.write(b"¡Servidor detenido!") 
        self.server.shutdown() # Detener el servidor después de una solicitud. 

httpd = HTTPServer(('localhost', 8080), MiManejador) 
httpd.serve_forever() 

#http.server.set_internal_error_message(). Permite configurar el mensaje que se enviará en caso de un error interno del servidor. Esta función es principalmente para servidores personalizados y no se utiliza mucho en el uso estándar. Ejemplo: No es comúnmente utilizada, ya que generalmente se gestiona automáticamente por el servidor.
#http.server.BaseHTTPRequestHandler.log_request()
#Registra un mensaje de solicitud en el servidor. Este método se puede sobrescribir en un servidor personalizado para registrar información específica sobre cada solicitud. Ejemplo: 
from http.server import BaseHTTPRequestHandler 
class MiManejador(BaseHTTPRequestHandler): 
    def do_GET(self): 
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers() 
        self.wfile.write(b"¡Registro de solicitud!") 
        self.log_request() # Esto registrará el acceso de la solicitud GET en la consola. 

#http.server.SimpleHTTPRequestHandler.send_response(). Este método se utiliza para enviar una respuesta HTTP al cliente. Es una de las funciones clave dentro de SimpleHTTPRequestHandler. Ejemplo: 
from http.server import SimpleHTTPRequestHandler 
class MiManejador(SimpleHTTPRequestHandler): 
    def do_GET(self): 
        self.send_response(200) 
        self.send_header('Content-type', 'text/html') 
        self.end_headers() 
        self.wfile.write(b"¡Respuesta personalizada!") 


"""Clases del Módulo http.server"""

#http.server.BaseHTTPRequestHandler
#Esta es la clase base para manejar las solicitudes HTTP. Puedes sobrescribir los métodos de esta clase para personalizar el comportamiento del servidor, como el manejo de solicitudes GET, POST, entre otras.
#Métodos importantes: 
#do_GET(): Maneja las solicitudes GET.
#do_POST(): Maneja las solicitudes POST.
#send_response(): Envía una respuesta HTTP al cliente.
#send_header(): Envía un encabezado de respuesta. Ejemplo: 
from http.server import BaseHTTPRequestHandler, HTTPServer 
class MiManejador(BaseHTTPRequestHandler): 
    def do_GET(self): 
        self.send_response(200) 
        self.send_header('Content-type', 'text/html') 
        self.end_headers() 
        self.wfile.write(b"¡Hola Mundo!") 

httpd = HTTPServer(('localhost', 8080), MiManejador) 
httpd.serve_forever() 

#http.server.SimpleHTTPRequestHandler
#Esta clase hereda de BaseHTTPRequestHandler y se utiliza para servir archivos estáticos desde el directorio en el que se ejecuta el servidor. Es un manejador de solicitudes muy común y útil para pruebas.
#Métodos importantes: 
#do_GET(): Sirve los archivos solicitados.
#do_HEAD(): Similar a do_GET(), pero no envía el cuerpo de la respuesta. Ejemplo: 
import socketserver 
PORT = 8000 
Handler = http.server.SimpleHTTPRequestHandler 
with socketserver.TCPServer(("", PORT), Handler) as httpd: 
    print(f"Servidor corriendo en el puerto {PORT}") 
    httpd.serve_forever() 

#http.server.HTTPServer
#Esta clase se utiliza para crear un servidor HTTP. Recibe como parámetros la dirección y el manejador de solicitudes (como BaseHTTPRequestHandler o SimpleHTTPRequestHandler).
#Métodos importantes: 
#serve_forever(): Mantiene el servidor en ejecución, atendiendo solicitudes.
#shutdown(): Detiene el servidor. Ejemplo: 
from http.server import HTTPServer, BaseHTTPRequestHandler 
class MiManejador(BaseHTTPRequestHandler): 
    def do_GET(self): 
        self.send_response(200) 
        self.send_header('Content-type', 'text/html') 
        self.end_headers() 
        self.wfile.write(b"¡Hola Mundo!")

httpd = HTTPServer(('localhost', 8080), MiManejador) 
print("Servidor iniciado en el puerto 8080") 
httpd.serve_forever() 

#http.server.ThreadingHTTPServer (solo en Python 3.7+)
#Similar a HTTPServer, pero con soporte para manejar múltiples solicitudes de manera concurrente utilizando hilos. Esto permite que el servidor procese varias solicitudes al mismo tiempo.
#Métodos importantes: 
#serve_forever(): Mantiene el servidor en ejecución, pero ahora puede manejar múltiples solicitudes simultáneamente. Ejemplo: 
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
class MiManejador(BaseHTTPRequestHandler): 
    def do_GET(self): 
    self.send_response(200) 
    self.send_header('Content-type', 'text/html') 
    self.end_headers() 
    self.wfile.write(b"¡Hola Mundo!") 

httpd = ThreadingHTTPServer(('localhost', 8080), MiManejador) 
print("Servidor iniciado en el puerto 8080 con soporte para múltiples hilos") 
httpd.serve_forever() 

#http.server.SocketServer (solo en versiones antiguas de Python)
#Este es un servidor de propósito general que se utiliza en el sistema de redes de bajo nivel de Python. HTTPServer es una subclase de SocketServer, que es una implementación general de servidores de red, pero generalmente se prefiere usar HTTPServer para servidores HTTP. Nota: SocketServer se ha reemplazado en gran parte por clases más específicas como HTTPServer y ThreadingHTTPServer.
#BaseHTTPRequestHandler: Clase base para manejar solicitudes HTTP.
#SimpleHTTPRequestHandler: Implementación predeterminada que maneja solicitudes para servir archivos estáticos.
#HTTPServer: Clase principal para crear un servidor HTTP básico.
#ThreadingHTTPServer: Versión de HTTPServer que permite manejar solicitudes de manera concurrente mediante hilos.


"""Variables en el Módulo http.server"""

#http.server.ServerHandler
#Esta variable hace referencia al manejador de servidores que se utiliza por defecto cuando se crea un 
#servidor HTTP, como parte de la configuración de la clase HTTPServer. Ejemplo de uso: Generalmente no se manipula directamente, pero se puede personalizar en clases personalizadas del servidor.

#http.server.DOCUMENT_ROOT (Deprecada en versiones modernas de Python)
#Se usaba para definir el directorio raíz de los documentos que el servidor serviría. Sin embargo, en versiones modernas, esto ya no es común y se utiliza más comúnmente SimpleHTTPRequestHandler que sirve desde el directorio de trabajo actual. Ejemplo de uso: No se recomienda en versiones actuales de Python, ya que el manejo de directorios se realiza automáticamente.

#http.server.address_family (en SocketServer)
#En el contexto de un servidor que utiliza SocketServer, esta variable define el tipo de dirección que se utilizará para las conexiones (por ejemplo, IPv4 o IPv6). Ejemplo de uso: 
print(http.server.address_family) 

#Variables Internas Comunes
#Dentro de las clases de http.server, algunas variables internas son útiles para controlar el flujo de las solicitudes, como las siguientes:
#self.path: En la clase BaseHTTPRequestHandler, la variable self.path contiene la ruta solicitada en la URL, que es útil para determinar qué archivo o recurso se está pidiendo.
#self.headers: Esta variable contiene los encabezados de la solicitud HTTP recibida, y se puede acceder para obtener información como el tipo de contenido, el agente de usuario, entre otros.
#self.command: En la clase BaseHTTPRequestHandler, self.command contiene el tipo de solicitud HTTP (como GET o POST).



"""Constantes del Módulo http.server"""

#http.server.REQUEST_TIMEOUT
#Esta constante define el tiempo de espera en segundos para una solicitud HTTP antes de que se cierre. Es útil para evitar que las solicitudes que tardan demasiado tiempo bloqueen el servidor. Valor por defecto: 300 segundos (5 minutos). Ejemplo de uso: 
print(http.server.REQUEST_TIMEOUT) # Muestra el valor predeterminado: 300 segundos 

#http.server.SO_REUSEADDR
#Esta constante se usa para permitir que una dirección de red pueda ser reutilizada inmediatamente después de que un servidor se cierre. Es útil en servidores que necesitan reiniciarse rápidamente sin esperar por el cierre completo de las conexiones previas. Ejemplo de uso:
print(http.server.SO_REUSEADDR) # Muestra la constante relacionada con la reutilización de direcciones 

#http.server.HTTP_STATUS_CODES
#Es un diccionario que contiene los códigos de estado HTTP estándar y sus mensajes asociados. Por ejemplo, el código 200 tiene como mensaje "OK", y 404 tiene el mensaje "Not Found". Ejemplo de uso: 
print(http.server.HTTP_STATUS_CODES[200]) # Muestra "OK" 
print(http.server.HTTP_STATUS_CODES[404]) # Muestra "Not Found" 

#http.server.DEFAULT_ERROR_MESSAGE
#Es el mensaje de error predeterminado que se envía cuando el servidor encuentra un error inesperado. Esta constante puede ser útil cuando se quiere personalizar los errores en un servidor. Ejemplo de uso: 
print(http.server.DEFAULT_ERROR_MESSAGE) # Muestra el mensaje de error predeterminado 


#Constantes Internas
#En las clases como BaseHTTPRequestHandler y SimpleHTTPRequestHandler, existen algunas constantes internas, como los códigos de estado HTTP, que pueden ser utilizados para manejar diferentes respuestas HTTP. Por ejemplo:
#self.responses: Un diccionario dentro de las clases mencionadas, que contiene los códigos de estado HTTP y sus correspondientes descripciones. Aunque no es una constante global, actúa como una constante dentro del contexto de esas clases.



"""Excepciones del Módulo http.server"""

#http.server.BaseHTTPRequestHandler
#Aunque no es una excepción en sí, es relevante saber que esta clase base se utiliza para definir cómo se manejan las excepciones dentro de las solicitudes HTTP. Dentro de esta clase, puedes manejar o personalizar los errores para las solicitudes HTTP de manera específica.

#http.server.HTTPStatus
#Aunque técnicamente no es una excepción, HTTPStatus se usa para manejar los códigos de estado HTTP, lo que incluye muchos errores HTTP, como 404 (Not Found), 500 (Internal Server Error), etc. No es una excepción directa, pero los errores HTTP se gestionan a través de los códigos definidos por esta clase. Ejemplo de uso: 
from http import HTTPStatus 
print(HTTPStatus.NOT_FOUND) # Muestra '404 Not Found' 

#http.server.HTTPServer
#Si se produce un error al intentar iniciar un servidor, como un conflicto de puerto o una dirección no válida, HTTPServer puede generar excepciones como OSError, ValueError o socket.error. Estas no son excepciones específicas de http.server, pero son comunes al trabajar con servidores de red. Ejemplo de uso: 
from http.server import HTTPServer, BaseHTTPRequestHandler 
class MiManejador(BaseHTTPRequestHandler): 
    def do_GET(self): 
        self.send_response(200) 
        self.send_header('Content-type', 'text/html') 
        self.end_headers() 
        self.wfile.write(b"¡Hola Mundo!") 

try: 
    httpd = HTTPServer(('localhost', 8080), MiManejador) 
    httpd.serve_forever() 
except OSError as e: 
    print(f"Error al iniciar el servidor: {e}") 

#http.server.SimpleHTTPRequestHandler
#Al igual que con BaseHTTPRequestHandler, si hay problemas al servir archivos estáticos o al procesar solicitudes de archivos, pueden generarse excepciones del tipo OSError, FileNotFoundError o PermissionError, que no son exclusivas del módulo, pero son comunes cuando se trabajan con archivos. Ejemplo de uso: 
from http.server import SimpleHTTPRequestHandler, HTTPServer 
try: 
    httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler) 
    print("Servidor corriendo en el puerto 8000") 
    httpd.serve_forever() 
except PermissionError: 
    print("Error: No se tienen permisos suficientes para ejecutar el servidor.") 



"""El módulo http.server en Python no tiene submódulos adicionales. Sin embargo, está basado en algunos módulos estándar de 
Python, como socketserver y http, que proporcionan funcionalidades para manejar las conexiones de red y los códigos de 
estado HTTP. En resumen, http.server no tiene submódulos específicos, pero depende de otros módulos para su funcionamiento."""

"""Módulos relacionados con http.server:"""

#socketserver:
#Este es un módulo que proporciona las clases base para crear servidores de red. El servidor HTTPServer dentro de http.server hereda de la clase socketserver.TCPServer, lo que le permite gestionar las conexiones entrantes en el protocolo TCP. Ejemplo de uso relacionado: 
from http.server import HTTPServer, SimpleHTTPRequestHandler 
import socketserver 
with socketserver.TCPServer(('localhost', 8000), SimpleHTTPRequestHandler) as httpd:
    print("Servidor corriendo en el puerto 8000") 
    httpd.serve_forever() 

#http: El módulo http proporciona utilidades para trabajar con las cabeceras HTTP, los códigos de estado y las respuestas. A menudo se utiliza junto con http.server para manejar el comportamiento de los códigos de estado HTTP y las respuestas de error. Ejemplo de uso relacionado:
from http import HTTPStatus 
print(HTTPStatus.OK) # Muestra '200 OK' 
