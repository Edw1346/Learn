"""Petición HTTP?"""
"""Una petición HTTP es una solicitud enviada por un cliente (generalmente un navegador o aplicación) a un servidor para obtener datos, enviar información o realizar alguna acción. Los métodos HTTP más comunes son:
GET: Solicita datos de un servidor (lectura).
POST: Envía datos al servidor (creación).
PUT: Actualiza datos en el servidor.
DELETE: Elimina datos en el servidor.
HEAD: Solicita solo los encabezados de la respuesta.
OPTIONS: Recupera las opciones soportadas por el servidor.

Módulo requests
El módulo requests es una biblioteca de Python diseñada para realizar peticiones HTTP de manera sencilla. A continuación, se describen sus características principales.

Instalación
pip install requests 

Realizar peticiones básicas"""
import requests
# Petición GET 
response = requests.get('https://jsonplaceholder.typicode.com/posts') 
print(response.status_code) 
# Código de estado (200, 404, etc.)
print(response.text) 
# Contenido de la respuesta 
# Petición POST 
data = {"title": "foo", "body": "bar", "userId": 1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data) 
print(response.json()) 
# Muestra la respuesta en formato JSON 

"""Componentes de una petición HTTP
Método: GET, POST, PUT, DELETE, etc.
URL: Dirección del recurso solicitado.
Headers: Metadatos adicionales, como autenticación o tipo de contenido.
Cuerpo (Body): Datos enviados en la petición (POST/PUT).

1. Métodos HTTP principales
1.1 GET
Se usa para obtener datos."""
response = requests.get('https://jsonplaceholder.typicode.com/posts/1') 
print(response.json()) # Muestra la respuesta como un diccionario 

#1.2 POST
#Se usa para enviar datos al servidor.
data = {"title": "foo", "body": "bar", "userId": 1} 
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
print(response.status_code) 

#1.3 PUT
#Se usa para actualizar datos existentes.
data = {"title": "nuevo titulo", "body": "contenido actualizado", "userId": 1}
response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=data) 
print(response.json()) 

#1.4 DELETE

#Se usa para eliminar datos.
response = requests.delete('https://jsonplaceholder.typicode.com/posts/1') 
print(response.status_code) # Código de respuesta 

"""2. Cabeceras (Headers)
Los headers proporcionan información adicional sobre la petición o respuesta. Por ejemplo, la autenticación o el formato de los datos. Ejemplo:"""
headers = {"Authorization": "Bearer <token>", "Content-Type": "application/json"} 
response = requests.get('https://api.example.com/endpoint', headers=headers) 
print(response.headers) # Cabeceras de la respuesta 

#3. Parámetros en la URL (Query Parameters)
#Los parámetros pueden enviarse en el URL para filtrar o personalizar las solicitudes.
params = {"userId": 1, "completed": True}
response = requests.get('https://jsonplaceholder.typicode.com/todos', params=params) 
print(response.url) # Muestra la URL con los parámetros
print(response.json()) # Datos filtrados 

"""4. Manejo de errores
Es importante verificar el estado de las respuestas para detectar errores (como 404 o 500)."""
response = requests.get('https://jsonplaceholder.typicode.com/invalid-url')
if response.status_code == 200:
    print("Petición exitosa") 
elif response.status_code == 404: 
    print("Recurso no encontrado") 
else: 
    print(f"Error: {response.status_code}") 

"""5. Tiempo de espera (Timeout)
Evita que la aplicación quede bloqueada por una respuesta lenta del servidor."""
try: 
    response = requests.get('https://jsonplaceholder.typicode.com/posts', timeout=5) 
    print(response.json()) 
except requests.Timeout:
    print("La petición tardó demasiado tiempo y fue interrumpida.") 

"""6. Sesiones con requests
Puedes usar una sesión para mantener cookies o encabezados comunes entre múltiples peticiones."""
session = requests.Session() 
session.headers.update({"Authorization": "Bearer <token>"})
response = session.get('https://api.example.com/resource') 
print(response.status_code) 

"""7. Subir archivos
Puedes subir archivos usando el método POST."""
files = {'file': open('archivo.txt', 'rb')}
response = requests.post('https://example.com/upload', files=files)
print(response.status_code) 

"""8. Descarga de archivos
Descargar contenido binario (como imágenes o documentos)."""
response = requests.get('https://example.com/imagen.jpg', stream=True)
with open('imagen.jpg', 'wb') as file: 
    for chunk in response.iter_content(chunk_size=8192): 
        file.write(chunk) 

"""9. Autenticación
El módulo requests ofrece soporte para distintos métodos de autenticación.

9.1 Básica"""
from requests.auth import HTTPBasicAuth 
response = requests.get('https://example.com/protected', auth=HTTPBasicAuth('usuario', 'contraseña')) 

#9.2 Token Bearer
headers = {"Authorization": "Bearer <token>"} 
response = requests.get('https://api.example.com/resource', headers=headers) 

"""10. Bibliotecas adicionales para peticiones HTTP avanzadas
http.client
Es una biblioteca de bajo nivel para gestionar peticiones HTTP. Aunque es menos conveniente que requests, puede ser útil para operaciones personalizadas.

aiohttp
Se utiliza para peticiones HTTP asíncronas, permitiendo manejar múltiples solicitudes en paralelo."""






"""Conceptos relacionados """

"""HTTP (HyperText Transfer Protocol)
Es el protocolo de comunicación que regula la interacción entre un cliente (como un navegador o script) y un servidor.
Se utiliza para transferir datos como HTML, JSON, XML, imágenes, etc.

Código de estado HTTP
Los servidores responden con códigos de estado que indican el resultado de la solicitud:
2xx (Éxito): 
200 OK: La solicitud fue exitosa.
201 Created: Recurso creado con éxito.

3xx (Redirección): 
301 Moved Permanently: URL movida permanentemente.
302 Found: URL temporalmente redirigida.

4xx (Errores del cliente): 
400 Bad Request: Solicitud malformada.
401 Unauthorized: Falta autenticación.
404 Not Found: Recurso no encontrado.

5xx (Errores del servidor): 
500 Internal Server Error: Error interno del servidor.
503 Service Unavailable: Servicio no disponible.

5. Headers HTTP (Encabezados)
Los encabezados se usan para proporcionar información adicional sobre la petición o la respuesta:

Encabezados de solicitud: 
Authorization: Información de autenticación (token, credenciales, etc.).
Content-Type: Tipo de datos enviados (ej. application/json).
User-Agent: Identifica el cliente que realiza la solicitud.

Encabezados de respuesta: 
Content-Length: Tamaño del contenido devuelto.
Set-Cookie: Establece cookies en el cliente.

6. Tipos de datos en HTTP
Texto plano: Archivos de texto o contenido HTML.
JSON (JavaScript Object Notation): Formato de datos estructurados.
XML: Formato más antiguo pero aún usado en algunas APIs.
Datos binarios: Imágenes, videos, archivos comprimidos, etc.

7. JSON y APIs REST
JSON: Es el formato más común para enviar y recibir datos en aplicaciones web modernas.
REST (Representational State Transfer): Arquitectura utilizada para construir APIs basadas en HTTP.

8. Autenticación
Las peticiones HTTP pueden requerir autenticación para acceder a recursos protegidos:
Autenticación básica: Envío de usuario y contraseña.
Tokens de acceso: Uso de Bearer Tokens o API Keys.
OAuth: Protocolo de autenticación para obtener acceso seguro.

9. Conexiones seguras
HTTP vs HTTPS: HTTPS es HTTP con una capa de seguridad (SSL/TLS) que cifra las peticiones y respuestas.

10. Librerías en Python para peticiones HTTP
requests: Biblioteca más utilizada para realizar peticiones HTTP.
http.client: Biblioteca nativa para manejar HTTP de bajo nivel.
urllib: Biblioteca estándar para manejo de URLs y peticiones.
aiohttp: Para peticiones asíncronas y paralelas.

11. Tipos de tiempo de espera (Timeout)
Timeout de conexión: Tiempo máximo para establecer la conexión con el servidor.
Timeout de lectura: Tiempo máximo para recibir una respuesta del servidor.

12. Redirecciones
Los servidores pueden redirigir una petición HTTP (códigos 301 o 302).
Python maneja automáticamente redirecciones en bibliotecas como requests.

13. Manejo de errores y excepciones
Errores comunes que pueden surgir al realizar peticiones:
Errores de red: Fallos de conexión, tiempo de espera agotado.
Errores HTTP: Códigos 4xx o 5xx.
Excepciones en Python: 
requests.exceptions.Timeout: Tiempo de espera excedido.
requests.exceptions.ConnectionError: Error de conexión.

14. Sesiones HTTP
Una sesión mantiene la información de estado entre múltiples peticiones, como cookies y encabezados comunes.

15. Descarga y subida de archivos
Descarga: Peticiones GET con contenido binario.
Subida: Uso de POST con el argumento files.

16. Mecanismos de caché
HTTP permite almacenar temporalmente recursos (como imágenes o respuestas) para mejorar el rendimiento."""



"""Modulo requests """

"""1. Instalación del módulo
El módulo requests no está incluido en la biblioteca estándar de Python, por lo que primero necesitas instalarlo:
pip install requests 

2. Características principales
Soporte para métodos HTTP: GET, POST, PUT, DELETE, etc.
Gestión de parámetros de consulta (query parameters) y encabezados (headers).
Soporte para autenticación (básica, Bearer tokens, etc.).
Gestión automática de cookies y sesiones.
Manejo sencillo de excepciones relacionadas con peticiones HTTP.
Capacidad para subir y descargar archivos.
Compatibilidad con tiempo de espera (timeout) y redirecciones automáticas.

4. Componentes clave del módulo requests"""

"""4.1 Parámetros en la URL (Query Parameters)
Los parámetros se pueden enviar como un diccionario en la petición."""
params = {"userId": 1, "completed": True}
response = requests.get('https://jsonplaceholder.typicode.com/todos', params=params) 
print(response.url) # URL con los parámetros incluidos
print(response.json()) 

"""4.2 Encabezados (Headers)
Puedes enviar encabezados personalizados en una solicitud."""
headers = {"Authorization": "Bearer <token>", "Content-Type": "application/json"} 
response = requests.get('https://api.example.com/resource', headers=headers)
print(response.headers) # Ver los encabezados de respuesta 

"""4.3 Cuerpo de la solicitud (Request Body)
Para enviar datos en el cuerpo de una solicitud, puedes usar:
data: Para datos de formulario.
json: Para datos en formato JSON."""

# Datos como formulario 
data = {"username": "usuario", "password": "contraseña"} 
response = requests.post('https://api.example.com/login', data=data) 
# Datos como JSON 
json_data = {"key": "value"} 
response = requests.post('https://api.example.com/resource', json=json_data) 

"""5. Gestión de respuestas
El módulo requests ofrece varias formas de interactuar con la respuesta del servidor.

5.1 Atributos principales"""
response = requests.get('https://jsonplaceholder.typicode.com/posts/1') 
print(response.status_code) 
# Código de estado HTTP 
print(response.text) # Contenido de la respuesta como texto
print(response.json()) # Contenido de la respuesta como JSON
print(response.headers) # Encabezados de la respuesta
print(response.url) # URL de la petición 

"""5.2 Manejo de errores
El código de estado HTTP indica si la solicitud fue exitosa:
2xx: Éxito.
4xx: Error del cliente.
5xx: Error del servidor."""
response = requests.get('https://jsonplaceholder.typicode.com/invalid-url')
if response.status_code == 200: 
    print("Petición exitosa")
elif response.status_code == 404:
    print("Recurso no encontrado") 
else: 
    print(f"Error: {response.status_code}") 

"""6. Sesiones
Una sesión en requests permite reutilizar conexiones, encabezados y cookies entre varias solicitudes."""
session = requests.Session() 
session.headers.update({"Authorization": "Bearer <token>"}) 
# Todas las peticiones comparten la misma sesión
response1 = session.get('https://api.example.com/resource1') 
response2 = session.get('https://api.example.com/resource2') 

"""7. Subir y descargar archivos
7.1 Subir archivos
Puedes subir archivos usando el método POST y el argumento files."""
files = {"file": open("archivo.txt", "rb")}
response = requests.post('https://example.com/upload', files=files) 
print(response.status_code) 

"""7.2 Descargar archivos
Para descargar archivos binarios (imágenes, PDFs, etc.), usa el argumento stream."""
response = requests.get('https://example.com/imagen.jpg', stream=True) 
with open('imagen.jpg', 'wb') as file:
    for chunk in response.iter_content(chunk_size=8192):
        file.write(chunk) 

"""8. Tiempo de espera (Timeout)
Puedes definir un límite de tiempo para evitar que la solicitud quede colgada."""
try: 
    response = requests.get('https://example.com', timeout=5) 
    print(response.status_code) 

except requests.Timeout: 
    print("La solicitud tardó demasiado tiempo.") 

"""9. Autenticación
9.1 Autenticación básica"""
from requests.auth import HTTPBasicAuth 
response = requests.get('https://example.com/protected', auth=HTTPBasicAuth('usuario', 'contraseña')) print(response.status_code) 

#9.2 Token Bearer
headers = {"Authorization": "Bearer <token>"} 
response = requests.get('https://api.example.com/resource', headers=headers) 

"""10. Manejo de redirecciones

Por defecto, requests sigue automáticamente redirecciones."""
response = requests.get('http://example.com') 
print(response.url) # URL final después de la redirección 

#Si no deseas seguir redirecciones:
response = requests.get('http://example.com', allow_redirects=False) 

"""11. Excepciones comunes
requests proporciona excepciones específicas para manejar errores:
requests.exceptions.Timeout: Error de tiempo de espera.
requests.exceptions.ConnectionError: Error de conexión.
requests.exceptions.HTTPError: Error HTTP."""

try:
    response = requests.get('https://example.com', timeout=5)
    response.raise_for_status()

# Lanza excepción si hay error HTTP 
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}") 



"""Buenas prácticas útiles """

"""1. Hacer una solicitud GET básica
Objetivo: Obtener datos de una API pública."""
import requests
# API de prueba para obtener posts
url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url) 
# Validar respuesta y mostrar datos
if response.status_code == 200:
    print("Título del post:", response.json()['title']) 
else:
    print(f"Error: {response.status_code}") 

"""2. Enviar parámetros en una URL
Objetivo: Enviar parámetros como parte de la URL (query parameters)."""
import requests
# Parámetros de consulta 
params = {"userId": 1} 
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=params) 
# Mostrar resultados 
if response.status_code == 200:
    print("Posts del usuario 1:") 
    for post in response.json(): 
        print(post['title'])
else: 
    print(f"Error: {response.status_code}") 

"""3. Enviar datos JSON con POST
Objetivo: Enviar datos en formato JSON para crear un recurso."""
import requests 
# Datos a enviar 
data = { "title": "Mi nuevo post", "body": "Este es el contenido del post", "userId": 1 } 
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data) 
# Mostrar respuesta 
if response.status_code == 201: 
# Código 201: Recurso creado 
    print("Post creado exitosamente:", response.json()) 
else: 
    print(f"Error al crear el post: {response.status_code}") 

"""4. Manejar errores HTTP
Objetivo: Capturar y manejar errores al hacer solicitudes."""
import requests 
url = 'https://jsonplaceholder.typicode.com/posts/99999' 
try: 
    response = requests.get(url) 
    response.raise_for_status() 
# Lanza excepción para errores HTTP 
    print("Datos recibidos:", response.json()) 
except requests.exceptions.HTTPError as e: 
    print("Error HTTP:", e) 
except requests.exceptions.RequestException as e: 
    print("Error en la solicitud:", e) 

"""5. Descargar un archivo de internet
Objetivo: Descargar un archivo binario y guardarlo localmente."""
import requests 
url = 'https://via.placeholder.com/300.png'
response = requests.get(url, stream=True) 
# Guardar el archivo localmente 
if response.status_code == 200: 
    with open('imagen.png', 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024): 
            file.write(chunk) 
        print("Imagen descargada exitosamente.") 
else: 
    print(f"Error al descargar: {response.status_code}") 

"""6. Subir un archivo
Objetivo: Subir un archivo a un servidor mediante POST."""
import requests 
# Archivo a subir
files = {"file": open("archivo.txt", "rb")}
response = requests.post('https://httpbin.org/post', files=files)
# Mostrar respuesta del servidor 
if response.status_code == 200:
    print("Archivo subido exitosamente.")
else:
    print(f"Error al subir archivo: {response.status_code}") 

"""7. Usar encabezados personalizados
Objetivo: Enviar encabezados específicos en una solicitud."""
import requests
# Encabezados personalizados 
headers = { "User-Agent": "MiApp/1.0", "Authorization": "Bearer token_de_prueba" } 
response = requests.get('https://jsonplaceholder.typicode.com/posts', headers=headers)
if response.status_code == 200: 
    print("Datos recibidos con encabezados personalizados.") 
else: 
    print(f"Error: {response.status_code}") 

"""8. Manejar sesiones HTTP
Objetivo: Reutilizar cookies y encabezados con una sesión persistente."""

import requests 
# Crear sesión 
session = requests.Session()
session.headers.update({"Authorization": "Bearer token_de_prueba"})
# Primera solicitud 
response1 = session.get('https://jsonplaceholder.typicode.com/posts/1') 
print("Primera solicitud:", response1.json()) 
# Segunda solicitud con la misma sesión 
response2 = session.get('https://jsonplaceholder.typicode.com/posts/2') 
print("Segunda solicitud:", response2.json()) 

"""9. Tiempo de espera (timeout)
Objetivo: Evitar que una solicitud quede colgada indefinidamente."""
import requests 
url = 'https://httpbin.org/delay/5'
# Simula una demora de 5 segundos 
try: 
    response = requests.get(url, timeout=3)
# Límite de 3 segundos 
    print("Respuesta recibida:", response.json()) 
except requests.exceptions.Timeout: 
    print("La solicitud excedió el tiempo de espera.") 

"""10. Redirecciones
Objetivo: Manejar redirecciones automáticas o evitarlas."""
import requests 
url = 'http://httpbin.org/redirect/2' 
# Redirige 2 veces 
# Permitir redirecciones (por defecto) 
response = requests.get(url, allow_redirects=True) 
print("Redirección final:", response.url) 
# Evitar redirecciones 
response_no_redirect = requests.get(url, allow_redirects=False) 
print("Sin seguir redirecciones, código:", response_no_redirect.status_code) 

"""11. Consumir una API REST con autenticación
Objetivo: Acceder a una API con autenticación básica."""
import requests from requests.auth 
import HTTPBasicAuth 
# Autenticación básica 
auth = HTTPBasicAuth('usuario', 'contraseña') 
response = requests.get('https://httpbin.org/basic-auth/usuario/contraseña', auth=auth)
if response.status_code == 200:
    print("Autenticación exitosa:", response.json())
else:
    print("Error de autenticación.") 

"""12. Procesar JSON avanzado
Objetivo: Manipular y filtrar datos de una respuesta JSON."""
import requests 
response = requests.get('https://jsonplaceholder.typicode.com/posts') 
if response.status_code == 200: 
    data = response.json()
# Filtrar posts del usuario 1 
    user_posts = [post for post in data if post['userId'] == 1] 
    print("Posts del usuario 1:", user_posts) 
else: 
    print(f"Error: {response.status_code}") 

"""13. Pruebas de carga (Simulación de múltiples peticiones)
Objetivo: Simular varias solicitudes para probar un servidor."""
import requests from concurrent.futures 
import ThreadPoolExecutor 
url = 'https://jsonplaceholder.typicode.com/posts/1' 

def make_request(): 
    response = requests.get(url) 
    return response.status_code 

# Ejecutar múltiples solicitudes concurrentes 
with ThreadPoolExecutor(max_workers=5) as executor:
    results = list(executor.map(make_request, range(10))) 
    print("Códigos de estado:", results) 


"""Técnicas """

"""1. Reutilizar Sesiones para Mejorar el Rendimiento
Las sesiones permiten reutilizar conexiones HTTP, lo que reduce el tiempo y los recursos en comparación con crear nuevas conexiones para cada solicitud.
Técnica: Configurar sesiones persistentes"""
import requests
# Crear una sesión 
session = requests.Session() 
# Configurar encabezados y autenticación en la sesión
session.headers.update({ "Authorization": "Bearer <token>", "User-Agent": "MiAplicación/1.0" }) 
# Reutilizar la sesión en múltiples solicitudes 
response1 = session.get('https://jsonplaceholder.typicode.com/posts/1') 
response2 = session.get('https://jsonplaceholder.typicode.com/posts/2') 
print("Primera respuesta:", response1.json())
print("Segunda respuesta:", response2.json()) 

"""2. Manejo Avanzado de Redirecciones
Por defecto, requests sigue automáticamente redirecciones HTTP. Puedes controlar este comportamiento.
Técnica: Detectar redirecciones manualmente"""
import requests 
response = requests.get('http://httpbin.org/redirect/3', allow_redirects=False) 
if 300 <= response.status_code < 400:
    print("Redirigido a:", response.headers['Location'])
else: 
    print("Respuesta final:", response.status_code) 

"""3. Establecer Timeouts Adecuados
Las solicitudes pueden quedar colgadas indefinidamente si el servidor no responde. Establecer un timeout evita bloqueos en tu aplicación.
Técnica: Usar timeouts para todas las solicitudes"""
import requests 
try: 
    response = requests.get('https://httpbin.org/delay/5', timeout=3) 
    print(response.json()) 

except requests.exceptions.Timeout: 
    print("La solicitud excedió el tiempo de espera.") 

"""4. Retries Automáticos en Caso de Fallos
Cuando trabajas con servicios externos, puede haber fallos temporales (como errores de red). Implementar reintentos 

automáticos mejora la resiliencia.
Técnica: Reintentos automáticos con urllib3"""
from requests.adapters import HTTPAdapter 
from requests.packages.urllib3.util.retry import Retry 
import requests 

# Configurar reintentos 
retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504]) 
adapter = HTTPAdapter(max_retries=retries) 

# Crear una sesión con reintentos configurados
session = requests.Session() 
session.mount('http://', adapter) 
session.mount('https://', adapter)
response = session.get('https://httpbin.org/status/503')
print("Respuesta:", response.status_code) 

"""5. Subir Archivos Grandes Eficientemente
En lugar de cargar todo un archivo en memoria, puedes subirlo en partes para ahorrar recursos.
Técnica: Subir archivos en modo streaming"""
import requests
# Abrir archivo en modo binario 
with open('archivo_grande.txt', 'rb') as file: 
    response = requests.post('https://httpbin.org/post', files={'file': file}) 
    print("Respuesta del servidor:", response.json()) 

"""6. Descargar Archivos Grandes en Chunks
Descargar archivos grandes directamente a memoria puede causar problemas. Usa la descarga por chunks para guardar datos directamente en disco.
Técnica: Descargar en partes"""
import requests
url = 'https://via.placeholder.com/1000.png'
response = requests.get(url, stream=True) 
# Guardar el archivo en disco 
with open('imagen_grande.png', 'wb') as file: 
    for chunk in response.iter_content(chunk_size=1024):
        file.write(chunk) 
    print("Descarga completada.") 

"""7. Uso de Parámetros Dinámicos
Si trabajas con una API que requiere múltiples parámetros, puedes generarlos dinámicamente para solicitudes eficientes.
Técnica: Construcción dinámica de parámetros"""
import requests 
base_url = 'https://jsonplaceholder.typicode.com/posts' 
query_params = {"userId": 1, "completed": True} 
response = requests.get(base_url, params=query_params) 
print("URL generada:", response.url) 
print("Respuesta:", response.json()) 

"""8. Validación Automática de Respuestas
Asegúrate de que las respuestas cumplen con tus expectativas antes de procesarlas.
Técnica: Verificar respuestas antes de procesar"""
import requests
response = requests.get('https://jsonplaceholder.typicode.com/posts/1') 
# Verificar código de estado
if response.status_code == 200: 
    print("Contenido recibido:", response.json()) 

else:
    print(f"Error: {response.status_code}") 

"""9. Manejar Cookies
Si necesitas mantener sesiones activas, usa cookies para gestionar la autenticación y los estados de sesión.
Técnica: Gestionar cookies con sesiones"""
import requests
session = requests.Session() 
# Realizar una solicitud y guardar cookies 
response = session.get('https://httpbin.org/cookies/set?mi_cookie=valor') 
# Verificar cookies almacenadas 
print("Cookies almacenadas:", session.cookies.get_dict()) 

"""10. Registro de Peticiones para Depuración
Habilitar registros detallados de solicitudes y respuestas ayuda a depurar problemas.
Técnica: Habilitar logging"""
import requests 
import logging 

# Configurar logging 
logging.basicConfig(level=logging.DEBUG) 
logging.getLogger("urllib3").setLevel(logging.DEBUG)
# Realizar una solicitud con registros habilitados 
response = requests.get('https://jsonplaceholder.typicode.com/posts/1') 
print("Respuesta recibida:", response.json()) 

"""11. Uso de Middleware para Peticiones
Si tienes varias funciones que requieren configuraciones similares, crea un middleware para centralizar la lógica.
Técnica: Crear una función middleware"""
import requests 
def make_request(method, url, **kwargs): 
    session = requests.Session() 
    session.headers.update({"Authorization": "Bearer token_de_prueba"}) 
    response = session.request(method, url, **kwargs)
    response.raise_for_status() 
    # Lanza excepción si hay error
    return response
    # Usar el middleware 
response = make_request('GET', 'https://jsonplaceholder.typicode.com/posts/1')
print("Datos recibidos:", response.json()) 

"""12. Configurar Proxy
Si necesitas conectarte a internet a través de un proxy, puedes configurarlo en tus peticiones.
Técnica: Uso de proxies"""
import requests 
proxies = { "http": "http://mi_proxy:8080", "https": "https://mi_proxy:8080" } 
response = requests.get('https://httpbin.org/ip', proxies=proxies) 
print("IP obtenida:", response.json()) 
