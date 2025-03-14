import request

"""El módulo requests es una biblioteca de Python que facilita el trabajo con peticiones HTTP. Es ampliamente utilizada 
para interactuar con APIs web, enviar y recibir datos a través de la web, y manejar respuestas de manera sencilla. Su 
principal ventaja es su simplicidad en comparación con las bibliotecas estándar como urllib."""

#Características principales del módulo requests:
#Envío de peticiones HTTP: Puedes realizar peticiones como GET, POST, PUT, DELETE, etc.
#Manejo de parámetros: Puedes enviar parámetros en la URL o en el cuerpo de la solicitud (como en formularios o JSON).
#Manejo de respuestas: Puedes obtener fácilmente el contenido de la respuesta, el código de estado, las cabeceras, etc.
#Manejo de cookies, redirecciones y autenticación: Ofrece soporte integrado para trabajar con cookies, redirecciones automáticas y autenticación. Ejemplo básico:

response = requests.get('https://api.example.com/data')
# Verificar el estado de la respuesta
if response.status_code == 200: print(response.text) # Contenido de la respuesta
else: print(f"Error {response.status_code}") 

#Petición POST (enviar datos):
data = {'username': 'user', 'password': 'password'} 
response = requests.post('https://api.example.com/login', data=data) 
print(response.status_code) 

#Petición con parámetros en la URL:
params = {'search': 'Python', 'page': 1} 
response = requests.get('https://api.example.com/search', params=params) 
print(response.text) 




"""Funciones del módulo requests"""

#1. requests.get(url, params=None, **kwargs). Realiza una petición HTTP GET. Se usa para obtener información de un servidor. Ejemplo:
response = requests.get('https://api.example.com/data') 
print(response.text) 

#2. requests.post(url, data=None, json=None, **kwargs). Realiza una petición HTTP POST. Se usa para enviar datos a un servidor. Ejemplo:
data = {'key': 'value'}
response = requests.post('https://api.example.com/data', data=data)
print(response.text) 

#3. requests.put(url, data=None, **kwargs). Realiza una petición HTTP PUT. Se utiliza para actualizar o reemplazar datos en el servidor. Ejemplo:
data = {'key': 'new_value'}
response = requests.put('https://api.example.com/data/1', data=data) 
print(response.text) 

#4. requests.delete(url, **kwargs). Realiza una petición HTTP DELETE. Se usa para eliminar recursos en el servidor. Ejemplo:
response = requests.delete('https://api.example.com/data/1') 
print(response.text) 

#5. requests.head(url, **kwargs). Realiza una petición HTTP HEAD. Es similar a una petición GET, pero solo devuelve los encabezados de la respuesta, sin el cuerpo. Ejemplo:
response = requests.head('https://api.example.com/data') 
print(response.headers) 

#6. requests.options(url, **kwargs). Realiza una petición HTTP OPTIONS. Solicita información sobre los métodos HTTP soportados por el servidor para una URL específica. Ejemplo:
response = requests.options('https://api.example.com/data') 
print(response.headers) 

#7. requests.patch(url, data=None, **kwargs). Realiza una petición HTTP PATCH. Se usa para aplicar modificaciones parciales a un recurso en el servidor. Ejemplo:
data = {'key': 'new_partial_value'} 
response = requests.patch('https://api.example.com/data/1', data=data) 
print(response.text) 

#8. requests.request(method, url, **kwargs). Permite hacer cualquier tipo de petición HTTP (GET, POST, PUT, DELETE, etc.). Es la función más general, a la que se le puede pasar el método HTTP como un argumento. Ejemplo:
import requests 
response = requests.request('GET', 'https://api.example.com/data') 
print(response.text) 

#9. requests.head(url, **kwargs). Realiza una petición HEAD, similar a GET pero sin devolver el cuerpo del mensaje.

#10. requests.get() (con parámetros de sesión). Permite la creación de sesiones persistentes entre peticiones para manejar cookies y mantener el estado. Ejemplo:
session = requests.Session()
response = session.get('https://api.example.com/data') 

#Funciones adicionales

#11. requests.Session(). Crea una sesión que permite mantener cookies y configuraciones de parámetros entre peticiones. Ejemplo:
session = requests.Session()
 response = session.get('https://api.example.com/data') 

#12. requests.exceptions.RequestException. Es la clase base para todas las excepciones del módulo requests. Puedes usarla para capturar cualquier error en las peticiones. Ejemplo:
import requests from requests.exceptions 
import RequestException 
try: 
    response = requests.get('https://api.example.com/data') 
    response.raise_for_status() # Lanza una excepción para errores HTTP 
except RequestException as e: 
    print(f"Hubo un error: {e}") 

#13. requests.adapters.HTTPAdapter. Se utiliza para manejar conexiones HTTP, permitiendo controlar los detalles del transporte de las peticiones (como reintentos o tiempo de conexión).

#14. requests.auth. Contiene clases para la autenticación en las peticiones HTTP, como autenticación básica o autenticación mediante tokens. Ejemplo de autenticación básica:
from requests.auth import HTTPBasicAuth
response = requests.get('https://api.example.com/data', auth=HTTPBasicAuth('user', 'pass')) 



"""Clases del módulo requests"""

#1. requests.Request. La clase Request representa una petición HTTP que aún no se ha enviado. Se utiliza para construir una solicitud antes de enviarla al servidor. Esta clase no realiza la solicitud directamente, sino que permite construir y preparar la petición, para luego ser enviada por requests.Session. Ejemplo:
req = requests.Request('GET', 'https://api.example.com/data') 
prepared = req.prepare() # Prepara la solicitud 
response = requests.Session().send(prepared) # Enviar la solicitud 
print(response.text) 

#2. requests.Response. La clase Response es la respuesta de una petición HTTP realizada con requests. Esta clase contiene los datos que el servidor envía de vuelta como resultado de una solicitud, incluyendo el contenido, el código de estado HTTP, las cabeceras, etc. Ejemplo:
response = requests.get('https://api.example.com/data') 
print(response.status_code) # Código de estado HTTP 
print(response.text) # Cuerpo de la respuesta 

#3. requests.Session. La clase Session permite mantener una sesión persistente a través de múltiples peticiones HTTP. Las sesiones permiten conservar cookies y otros parámetros entre peticiones, como cabeceras personalizadas, sin tener que configurar manualmente cada solicitud. Ejemplo:
session = requests.Session() 
response = session.get('https://api.example.com/data') 
print(response.cookies) # Las cookies mantenidas en la sesión 

#4. requests.adapters.HTTPAdapter. La clase HTTPAdapter se utiliza para definir un adaptador para gestionar la conexión HTTP. Esto incluye la configuración de opciones como reintentos, tiempo de espera, y otros detalles relacionados con la conexión HTTP. Ejemplo:
import requests from requests.adapters 
import HTTPAdapter
session = requests.Session() 
adapter = HTTPAdapter(max_retries=3) # Reintentos en caso de fallos 
session.mount('http://', adapter) 
response = session.get('https://api.example.com/data') 

#5. requests.auth.HTTPBasicAuth. La clase HTTPBasicAuth proporciona una forma fácil de agregar autenticación básica en las solicitudes HTTP. Esta clase toma un nombre de usuario y una contraseña y los incluye en las cabeceras de la solicitud para la autenticación. Ejemplo:
from requests.auth import HTTPBasicAuth 
response = requests.get('https:/ api.example.com/data', auth=HTTPBasicAuth('user', 'pass')) 
print(response.text) 

#6. requests.cookies.RequestsCookieJar. La clase RequestsCookieJar es utilizada para manejar las cookies en una sesión. Permite almacenar y manipular las cookies que se intercambian entre el cliente y el servidor en el contexto de las peticiones HTTP. Ejemplo:
session = requests.Session() 
cookie_jar = session.cookies
cookie_jar.set('my_cookie', 'value') # Establecer una cookie 
print(cookie_jar) 



"""El módulo requests no tiene variables globales específicas que se utilicen directamente como las de algunos otros 
módulos. Sin embargo, existen constantes que pueden considerarse "variables" en el sentido de que están predefinidas en 
el módulo y se utilizan en las interacciones con las solicitudes HTTP. Estas constantes generalmente se utilizan para 
manejar configuraciones comunes o predeterminadas para las peticiones."""



"""Constantes del módulo requests"""

#1. requests.codes. requests.codes es un objeto que contiene constantes que representan los códigos de estado HTTP. Estas constantes se utilizan para hacer que el código sea más legible, en lugar de usar los números de código de estado directamente. Algunos de los códigos de estado más comunes son:
#requests.codes.ok: 200 (Solicitud exitosa)
#requests.codes.created: 201 (Recurso creado)
#requests.codes.accepted: 202 (Solicitud aceptada, pero no procesada aún)
#requests.codes.no_content: 204 (No hay contenido)
#requests.codes.moved_permanently: 301 (Redirección permanente)
#requests.codes.found: 302 (Redirección temporal)
#requests.codes.not_modified: 304 (No modificado)
#requests.codes.bad_request: 400 (Solicitud incorrecta)
#requests.codes.unauthorized: 401 (No autorizado)
#requests.codes.forbidden: 403 (Prohibido)
#requests.codes.not_found: 404 (No encontrado)
#requests.codes.internal_server_error: 500 (Error interno del servidor)
#requests.codes.not_implemented: 501 (Método no implementado)
#requests.codes.bad_gateway: 502 (Puerta de enlace incorrecta)
#requests.codes.service_unavailable: 503 (Servicio no disponible) Ejemplo:
response = requests.get('https://api.example.com/data') # Comprobar si la respuesta fue exitosa 
if response.status_code == requests.codes.ok: print("La solicitud fue exitosa.") 

#2. requests.status_codes. requests.status_codes es una clase que contiene los códigos de estado HTTP de manera estructurada, lo que proporciona una manera de acceder a estos códigos con nombres en lugar de solo números. Ejemplo:
response = requests.get('https://api.example.com/data') 
if response.status_code == requests.codes.not_found: print("Recurso no encontrado.") 

#3. requests.__version__. Esta constante almacena la versión del módulo requests que estás utilizando. Es útil si necesitas verificar o depurar qué versión de requests está instalada. Ejemplo:
print(requests.__version__) 

#4. requests.utils.default_headers(). Aunque no es una constante directa, la función requests.utils.default_headers() devuelve los encabezados predeterminados utilizados por el módulo requests en las solicitudes. Estos encabezados incluyen valores como User-Agent. Ejemplo:
headers = requests.utils.default_headers()
print(headers) 

#5. requests.packages (Depreciado). En versiones antiguas, requests.packages contenía varios paquetes que requests utilizaba internamente. Sin embargo, este uso ha sido descontinuado y no se recomienda su uso en versiones recientes de requests. 



"""Excepciones del módulo requests"""

#1. requests.exceptions.RequestException. Es la clase base de todas las excepciones en el módulo requests. Si capturas esta excepción, estarás capturando cualquier error relacionado con las solicitudes realizadas con requests. Generalmente, se utiliza para capturar errores genéricos, pero se recomienda capturar excepciones más específicas cuando sea necesario Ejemplo:
from requests.exceptions import RequestException 
try: 
    response = requests.get('https://api.example.com/data') 
    response.raise_for_status() # Lanza una excepción para errores HTTP 
except RequestException as e: 
    print(f"Hubo un error con la solicitud: {e}") 

#2. requests.exceptions.HTTPError. Esta excepción se lanza cuando una solicitud HTTP devuelve un código de estado que indica un error, como 400 (Bad Request) o 404 (Not Found). Si usas response.raise_for_status(), esta excepción se lanzará automáticamente si el código de estado de la respuesta indica un error. Ejemplo:
from requests.exceptions import HTTPError 
try: 
    response = requests.get('https://api.example.com/data')
    response.raise_for_status() # Lanza HTTPError si la respuesta es un error
except HTTPError as err: 
    print(f"Error HTTP ocurrido: {err}") 

#3. requests.exceptions.ConnectionError. Esta excepción se lanza cuando hay un problema de red, como la falta de conexión al servidor o un error de DNS. Ejemplo:
from requests.exceptions import ConnectionError 
try: 
    response = requests.get('https://api.example.com/data')
except ConnectionError as err: 
    print(f"Error de conexión: {err}") 

#4. requests.exceptions.Timeout. Esta excepción ocurre cuando la solicitud excede el tiempo de espera (timeout). Puede ser un error tanto al intentar establecer la conexión como al esperar la respuesta del servidor. Ejemplo:
from requests.exceptions import Timeout
try:
    response = requests.get('https://api.example.com/data', timeout=3) 
except Timeout as err:
    print(f"Tiempo de espera excedido: {err}") 

#5. requests.exceptions.TooManyRedirects. Se lanza cuando la solicitud excede el número máximo de redirecciones. Esto puede ocurrir si la URL solicitada redirige a una página en un bucle. Ejemplo:
from requests.exceptions import TooManyRedirects 
try: 
    response = requests.get('https://api.example.com/data')
except TooManyRedirects as err: 
    print(f"Demasiadas redirecciones: {err}") 

#6. requests.exceptions.URLRequired. Esta excepción ocurre cuando no se proporciona una URL en una solicitud o la URL proporcionada es inválida. Ejemplo:
from requests.exceptions import URLRequired 
try: 
    response = requests.get('')
except URLRequired as err: 
    print(f"URL requerida: {err}") 

#7. requests.exceptions.MissingSchema. Se lanza cuando la URL proporcionada no tiene un esquema válido (por ejemplo, falta http:// o https://). Ejemplo:
from requests.exceptions import MissingSchema 
try: 
    response = requests.get('example.com') 
except MissingSchema as err: 
    print(f"Esquema faltante en la URL: {err}") 

#8. requests.exceptions.InvalidURL. Se lanza cuando la URL proporcionada es sintácticamente incorrecta o no válida. Ejemplo:
from requests.exceptions import InvalidURL 
try:
    response = requests.get('htp://invalid-url') 
except InvalidURL as err:
    print(f"URL inválida: {err}") 

#9. requests.exceptions.ChunkedEncodingError. Esta excepción ocurre cuando hay un problema al decodificar una respuesta de codificación por partes (chunked transfer encoding). Ejemplo:
from requests.exceptions import ChunkedEncodingError
try:
    response = requests.get('https://api.example.com/data')
except ChunkedEncodingError as err: 
    print(f"Error de codificación en partes: {err}") 




"""El módulo requests no tiene submódulos internos oficiales en su estructura. Es un módulo relativamente simple, 
diseñado para realizar solicitudes HTTP de manera fácil, sin necesidad de depender de submódulos complejos. Sin embargo, 
en el paquete requests, algunos componentes que pueden parecer submódulos o utilidades adicionales incluyen:"""

#1. requests.adapters. requests.adapters es un submódulo utilizado para configurar y manejar adaptadores que gestionan la conexión HTTP y HTTPS, como la conexión por defecto que utiliza requests.Session().
#Clase HTTPAdapter: Se utiliza para configurar adaptadores HTTP personalizados, que permiten gestionar configuraciones más avanzadas como la reutilización de conexiones. Ejemplo:
from requests.adapters import HTTPAdapter 
session = requests.Session()
adapter = HTTPAdapter(max_retries=3) 
session.mount('http://', adapter) 
response = session.get('http://httpbin.org/get') 

#2. requests.models. requests.models contiene las clases esenciales para manejar la solicitud y la respuesta. Las clases más destacadas son:
#Clase Request: Representa una solicitud HTTP.
#Clase Response: Contiene la respuesta de una solicitud HTTP, con acceso al contenido, encabezados, y más. Ejemplo:
from requests.models import Response 
response = requests.get('https://api.example.com/data')
print(isinstance(response, Response)) # True 

#3. requests.sessions. El submódulo requests.sessions está relacionado con la clase Session, que permite mantener ciertas configuraciones a lo largo de múltiples solicitudes, como cabeceras y cookies persistentes.
#Clase Session: Permite reutilizar configuraciones, como cookies, entre múltiples solicitudes HTTP. Ejemplo:
session = requests.Session()
session.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
response = session.get('https://httpbin.org/cookies') 
print(response.text) # Verá la cookie que se ha establecido 

#4. requests.utils. requests.utils contiene diversas funciones de utilidad para trabajar con solicitudes HTTP, como la manipulación de cabeceras, manejo de URL, codificación y decodificación de parámetros, y más.
#Función default_headers(): Devuelve los encabezados predeterminados utilizados por requests.
#Función get_encoding_from_headers(): Obtiene la codificación de los encabezados HTTP. Ejemplo:
default_headers = requests.utils.default_headers() 
print(default_headers) 

#5. requests.hooks. requests.hooks se utiliza para gestionar "ganchos" (hooks) que permiten ejecutar acciones personalizadas cuando ciertos eventos ocurren en una solicitud o respuesta HTTP, como antes o después de enviar una solicitud o recibir una respuesta. Ejemplo:
def print_request(response, *args, **kwargs): 
    print(f"Request completed with status code {response.status_code}")
    return response 

response = requests.get('https://httpbin.org/get', hooks={'response': print_request}) 
