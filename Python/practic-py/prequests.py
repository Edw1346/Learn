import requests 

#El módulo requests es una biblioteca de Python que facilita el trabajo con peticiones HTTP. 

"""Características principales del módulo requests:
Envío de peticiones HTTP: Puedes realizar peticiones como GET, POST, PUT, DELETE, etc.
Manejo de parámetros: Puedes enviar parámetros en la URL o en el cuerpo de la solicitud (como en formularios o JSON).
Manejo de respuestas: Puedes obtener fácilmente el contenido de la respuesta, el código de estado, las cabeceras, etc.
Manejo de cookies, redirecciones y autenticación: Ofrece soporte integrado para trabajar con cookies, redirecciones automáticas y autenticación. """

u1 = 'https://jsonplaceholder.typicode.com/posts/1'
u2 = 'https://jsonplaceholder.typicode.com/comments/1'
u3 = 'https://jsonplaceholder.typicode.com/users/1'
u4 = 'https://jsonplaceholder.typicode.com/todos/1'
u5 = 'https://jsonplaceholder.typicode.com/albums/1'
u6 = 'https://jsonplaceholder.typicode.com/photos/1'
u7 = 'https://jsonplaceholder.typicode.com/posts'
u8 = 'https://jsonplaceholder.typicode.com/comments'
u9 = 'https://jsonplaceholder.typicode.com/users'
u10 = 'https://jsonplaceholder.typicode.com/todos'
u11 = 'https://jsonplaceholder.typicode.com/albums'
u12 = 'https://jsonplaceholder.typicode.com/photos'


#Funciones del módulo requests

## requests.options(url, **kwargs). Realiza una petición HTTP OPTIONS. Solicita información sobre los métodos HTTP soportados por el servidor para una URL específica.  
response = requests.options(u1) 
#response.headers) 
#response.status_code)
#response.cookies)
#response.content)
#response.apparent_encoding)
#response.elapsed)
#response.connection)
#response.history)
#response.is_permanent_redirect)
#response.is_redirect)
#response.ok)
#response.reason)
#response.request)
#response.json)
#response.raw)
#response.links)
#header, data, auth, timeout, allow_redirects

#requests.get(url, params=None, **kwargs). Realiza una petición HTTP GET. Se usa para obtener información de un servidor:
response = requests.get(u1) 
print(response.text) 
print(response.headers) 
print(response.status_code)
print(response.cookies)
print(response.content)
print(response.apparent_encoding)
print(response.elapsed)
print(response.connection)
print(response.history)
print(response.is_permanent_redirect)
print(response.is_redirect)
print(response.ok)
print(response.reason)
print(response.request)
print(response.json)
print(response.raw)
print(response.links)

# requests.post(url, data=None, json=None, **kwargs). Realiza una petición HTTP POST. Se usa para enviar datos a un servidor:
data = {'Edwin':'Guapo'}
response = requests.post(u7, data)
print(response)
print(response.text)

# requests.put(url, data=None, **kwargs). Realiza una petición HTTP PUT. Se utiliza para actualizar o reemplazar datos en el servidor. 
data = {'Edwin': 'Craft'}
response = requests.put(u3, data=data) 
print(response.text) 

# requests.delete(url, **kwargs). Realiza una petición HTTP DELETE. Se usa para eliminar recursos en el servidor: 
response = requests.delete(u2) 
print(response.text) 

## requests.head(url, **kwargs). Realiza una petición HTTP HEAD. Es similar a una petición GET, pero solo devuelve los encabezados de la respuesta, sin el cuerpo: 
response = requests.head(u5) 
print(response.headers) 

##requests.patch(url, data=None, **kwargs). Realiza una petición HTTP PATCH. Se usa para aplicar modificaciones parciales a un recurso en el servidor: 
data = {'key': 'new_partial_value'} 
response = requests.patch(u2, data=data) 
print(response.text) 

#requests.request(method, url, **kwargs). Permite hacer cualquier tipo de petición HTTP (GET, POST, PUT, DELETE, etc.):
response = requests.request('GET', u3) 
print(response.text) 

##requests.get() (con parámetros de sesión). Permite la creación de sesiones persistentes entre peticiones para manejar cookies y mantener el estado: 
session = requests.Session()
response = session.get(u5) 

#Funciones adicionales

## requests.Session(). Crea una sesión que permite mantener cookies y configuraciones de parámetros entre peticiones: 
session = requests.Session()
response = session.get(u3) 

# requests.exceptions.RequestException. Es la clase base para todas las excepciones del módulo requests. Puedes usarla para capturar cualquier error en las peticiones:
from requests.exceptions import RequestException
try: 
    response = requests.get(u2)
    response.raise_for_status() # Lanza una excepción para errores HTTP 
except RequestException as e: 
    print(f"Hubo un error: {e}") 

##requests.auth. Contiene clases para la autenticación en las peticiones HTTP, como autenticación básica o autenticación mediante tokens. Ejemplo de autenticación básica:
from requests.auth import HTTPBasicAuth
response = requests.get(u1, auth=HTTPBasicAuth('user', 'pass')) 


#Clases del módulo requests

# requests.Request. La clase Request representa una petición HTTP que aún no se ha enviado. Se utiliza para construir una solicitud antes de enviarla al servidor. 
#Esta clase no realiza la solicitud directamente, permite construir y preparar la petición, para luego ser enviada por requests.Session.:
req = requests.Request('GET', u3) 
prepared = req.prepare() # Prepara la solicitud 
response = requests.Session().send(prepared) # Enviar la solicitud 
print(response.text) 

#requests.Response. La clase Response es respuesta de una petición HTTP realizada con requests. 
#Esta clase contiene los datos que el servidor envía de vuelta como resultado de una solicitud, incluyendo el contenido, el código de estado HTTP, las cabeceras, etc:
response = requests.get(u5) 
print(response.status_code) # Código de estado HTTP 
print(response.text) # Cuerpo de la respuesta 

#requests.Session. La clase Session permite mantener una sesión persistente a través de múltiples peticiones HTTP. Las sesiones permiten conservar cookies y otros parámetros entre peticiones, como cabeceras personalizadas, sin tener que configurar manualmente cada solicitud:
session = requests.Session() 
request = session.get(u2) 
#response = session.request.post(u2) 
#response = session.request.delete(u2) 
#response = session.request.put(u2) 
#response = session.request.patch(u2) 
#response = session.request.header(u2) 
#response = session.request.opcions(u2) informacion de lo que sopprta el servidor
prepared = session.prepare_request(request)  #lo convierte en preparedRequest
response1 = session.send(prepared)  #envia la peticion ya preparada
response2 = session.get_adapter(u2) #Que adaptador se usa para la url
response3 = session.mount(u2, HTTPAdapter(max_retrices=3))  #reintentos automaticos
print(response.cookies) # Las cookies mantenidas en la sesión 
response = session.close()  #cierra la seccion

#requests.adapters.HTTPAdapter. La clase HTTPAdapter se utiliza para definir un adaptador para gestionar la conexión HTTP. Esto incluye la configuración de opciones como reintentos, tiempo de espera, y otros detalles relacionados con la conexión HTTP. Ejemplo:
from requests.adapters import HTTPAdapter 
session = requests.Session() 
adapter = HTTPAdapter(max_retries=3) # Reintentos en caso de fallos 
session.mount('http://', adapter) 
response = session.get(u3) 

#requests.auth.HTTPBasicAuth. La clase HTTPBasicAuth proporciona una forma fácil de agregar autenticación básica en las solicitudes HTTP. Esta clase toma un nombre de usuario y una contraseña y los incluye en las cabeceras de la solicitud para la autenticación. Ejemplo:
from requests.auth import AuthBase
class TokenPerso(AuthBase):
    def __init__(r, self):
        self.r = r
    
    def __call__(self, r):
        r.headers['Authorization'] = f"Bearer {self.r}"
        return r

response = requests.get(u2, auth=HTTPBasicAuth('user', 'pass')) #envia el user y pass codificado
response = requests.get(u2, auth=HTTPDigestAuth('user', 'pass')) #envia el user y pass de manera mas segura
print(response.text) 

#requests.cookies.RequestsCookieJar. La clase RequestsCookieJar es utilizada para manejar las cookies en una sesión. Permite almacenar y manipular las cookies que se intercambian entre el cliente y el servidor en el contexto de las peticiones HTTP. :
session = requests.Session() 
cookie_jar = session.cookies
cookie_jar.set('my_cookie', 'value') # Establecer una cookie 
cookie_jar.get('my_cookie', 'value') # ver una cookie
print(cookie_jar) 
#Metodos items(), keys(); values() para iterar
#Tiene un modulo http.cookie_jar que se descarga y tiene mas funciones


#Constantes del módulo requests

"""requests.codes, representan los códigos de estado HTTP. Estas constantes se utilizan para hacer que el código sea más legible, en lugar de usar los números de código de estado directamente. requests.codes.ok: 200 (Solicitud exitosa)
requests.codes.created: 201 (Recurso creado)
requests.codes.accepted: 202 (Solicitud aceptada, pero no procesada aún.
requests.codes.no_content: 204 (No hay contenido)

requests.codes.moved_permanently: 301 (Redirección permanente)
requests.codes.found: 302 (Redirección temporal)
requests.codes.not_modified: 304 (No modificado)
requests.codes.bad_request: 400 (Solicitud incorrecta)
requests.codes.unauthorized: 401 (No autorizado)
requests.codes.forbidden: 403 (Prohibido)
requests.codes.not_found: 404 (No encontrado)
requests.codes.internal_server_error: 500 (Error interno del servidor)
requests.codes.not_implemented: 501 (Método no implementado)
requests.codes.bad_gateway: 502 (Puerta de enlace incorrecta)
requests.codes.service_unavailable: 503 (Servicio no disponible)"""

response = requests.get('https://api.example.com/data') # Comprobar si la respuesta fue exitosa 
if response.status_code == requests.codes.ok: 
    print("La solicitud fue exitosa.") 

