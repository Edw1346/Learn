import urllib

"""El módulo urllib de Python es una librería estándar utilizada para trabajar con URLs (Uniform Resource Locators), que 
te permite manejar tareas comunes relacionadas con la web, como descargar archivos, manipular URLs, realizar solicitudes 
HTTP, y más."""


"""Las funciones de cada submódulo del módulo urllib."""

#1. urllib.parse. Este submódulo proporciona funciones para dividir, construir y manipular URLs.
#urlparse(url, scheme='', allow_fragments=True): Analiza una URL en sus componentes (esquema, redireccionamiento, dominio, ruta, etc.). Ejemplo:
import urllib.parse 
url = 'https://www.example.com/path?name=value#fragment' 
parsed_url = urllib.parse.urlparse(url)
print(parsed_url) 

#urlunparse(parts): Combina una tupla de componentes de URL en una URL completa. Ejemplo:
parts = ('https', 'www.example.com', '/path', '', 'name=value', 'fragment') 
url = urllib.parse.urlunparse(parts) 
print(url) 

#urlsplit(url, scheme='', allow_fragments=True): Similar a urlparse(), pero no divide la URL en parámetros de consulta. Ejemplo:
url = 'https://www.example.com/path?name=value#fragment' 
split_url = urllib.parse.urlsplit(url) 
print(split_url) 

#urlunsplit(parts): Combina los componentes de la URL, similar a urlunparse() pero para el formato de urlsplit(). Ejemplo:
parts = ('https', 'www.example.com', '/path', 'name=value', 'fragment') 
url = urllib.parse.urlunsplit(parts) 
print(url) 

#urljoin(base, url): Combina una URL base con una URL relativa. Ejemplo:
base_url = 'https://www.example.com/' 
relative_url = 'path?name=value' 
rull_url = urllib.parse.urljoin(base_url, relative_url) 
print(full_url) 

#urldefrag(url): Elimina el fragmento de una URL, si existe. Ejemplo:
url = 'https://www.example.com/path?name=value#fragment' 
url_no_frag, frag = urllib.parse.urldefrag(url) 
print(url_no_frag) 

#parse_qs(qs, keep_blank_values=False, strict_parsing=False): Convierte una cadena de consulta en un diccionario de claves y valores. Ejemplo:
query_string = 'name=John&age=30' 
parsed_query = urllib.parse.parse_qs(query_string) 
print(parsed_query) 

#parse_qsl(qs, keep_blank_values=False, strict_parsing=False): Similar a parse_qs(), pero devuelve una lista de tuplas. Ejemplo:
query_string = 'name=John&age=30' 
parsed_query = urllib.parse.parse_qsl(query_string)
print(parsed_query) 

#quote(string, safe='/', encoding=None, errors=None): Codifica una cadena para ser usada en una URL. Ejemplo:
string = 'Hello World!' 
encoded_string = urllib.parse.quote(string) 
print(encoded_string) 

#quote_plus(string, safe='', encoding=None, errors=None): Codifica una cadena, pero reemplaza los espacios con un + en lugar de %20. Ejemplo:
string = 'Hello World!' 
encoded_string = urllib.parse.quote_plus(string) 
print(encoded_string) 

#unquote(string, encoding=None, errors=None): Decodifica una URL codificada. Ejemplo:
encoded_string = 'Hello%20World%21' 
decoded_string = urllib.parse.unquote(encoded_string) 
print(decoded_string) 

#unquote_plus(string, encoding=None, errors=None): Similar a unquote(), pero también reemplaza el + por un espacio. Ejemplo:
encoded_string = 'Hello+World%21' 
decoded_string = urllib.parse.unquote_plus(encoded_string) 
print(decoded_string) 

#encode_qs(query, doseq=0): Codifica una cadena de parámetros de consulta. Ejemplo:
params = {'name': 'John', 'age': 30} 
encoded_params = urllib.parse.encode_qs(params) 
print(encoded_params) 

#splitattr(text): Divide un atributo de URL en nombre y valor. Ejemplo:
text = 'name=value' 
attribute = urllib.parse.splitattr(text)
print(attribute) 


#2. urllib.request
#Este submódulo facilita la apertura y manejo de URLs y solicitudes HTTP.
#urlopen(url, data=None, timeout=<object>, cafile=None, capath=None, cadefault=False, context=None): Abre una URL, devolviendo un objeto de respuesta. Ejemplo:
import urllib.request 
response = urllib.request.urlopen('https://www.example.com') 
print(response.read()) 

#Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None): Crea un objeto de solicitud HTTP. Ejemplo:
req = urllib.request.Request('https://www.example.com', headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req) 
print(response.read()) 

#urlretrieve(url, filename=None, reporthook=None, data=None): Descarga un archivo de una URL y lo guarda en un archivo local. Ejemplo:
url = 'https://www.example.com/image.jpg' 
urllib.request.urlretrieve(url, 'image.jpg') 

#pathname2url(path): Convierte una ruta del sistema de archivos a una URL. Ejemplo:
path = '/home/user/file.txt' 
url = urllib.request.pathname2url(path) 
print(url) 

#url2pathname(url): Convierte una URL a una ruta de sistema de archivos. Ejemplo:
url = 'file:///home/user/file.txt' 
path = urllib.request.url2pathname(url)
 print(path) 

#getproxies(): Obtiene los proxies configurados en el entorno. Ejemplo:
proxies = urllib.request.getproxies() 
print(proxies) 

#getproxies_environment(): Obtiene las configuraciones de proxies directamente del entorno. Ejemplo:
proxies = urllib.request.getproxies_environment()
 print(proxies) 

#build_opener(*handlers): Crea un objeto OpenerDirector que maneja la apertura de URLs utilizando los manejadores proporcionados. Ejemplo:
opener = urllib.request.build_opener(urllib.request.ProxyHandler())
response = opener.open('https://www.example.com') 
print(response.read()) 

#install_opener(opener): Establece un "opener" global para las solicitudes HTTP. Ejemplo:
opener = urllib.request.build_opener() 
urllib.request.install_opener(opener) 


#3. urllib.error: Este submódulo contiene las excepciones relacionadas con errores en la manipulación de URLs y solicitudes HTTP.
#URLError(reason): Excepción base para todos los errores relacionados con la URL. Ejemplo:
import urllib.request 
try: 
    urllib.request.urlopen('https://invalid-url.com') 
except urllib.error.URLError as e: 
    print(e.reason) 

#HTTPError(url, code, msg, hdrs, fp): Excepción para errores HTTP específicos. Ejemplo:
try:
    urllib.request.urlopen('https://httpbin.org/status/404') 
except urllib.error.HTTPError as e: 
    print(e.code) 

#ContentTooShortError(): Excepción cuando el contenido descargado es más corto de lo esperado. Ejemplo:
try: 
    urllib.request.urlretrieve('https://www.example.com', 'file.txt') 
except urllib.error.ContentTooShortError as e:
    print("Error: El contenido es demasiado corto.") 


#4. urllib.robotparser: Este submódulo es utilizado para analizar archivos robots.txt y determinar si una URL puede ser accedida por los robots de búsqueda.
#RobotFileParser(): Clase para analizar y manejar archivos robots.txt. Ejemplo:
import urllib.robotparser 
rp = urllib.robotparser.RobotFileParser() 
rp.set_url('https://www.example.com/robots.txt') 
rp.read() 
print(rp.can_fetch('*', 'https://www.example.com/path')) 





"""El módulo urllib contiene varias clases útiles, agrupadas en diferentes submódulos"""

#1. urllib.request
#Request: Esta clase es utilizada para representar una solicitud HTTP. Permite personalizar una solicitud, incluyendo los encabezados y el método HTTP (GET, POST, etc.).
#OpenerDirector: Esta clase gestiona los "opener handlers" que permiten realizar solicitudes HTTP de forma más personalizada (manejadores de cookies, proxies, autenticación, etc.). Ejemplo:
import urllib.request 
opener = urllib.request.build_opener() 
with opener.open('https://www.example.com') as response:
    print(response.read()) 

#ProxyHandler: Esta clase es un manejador para configurar proxies HTTP. Es utilizada por el OpenerDirector. Ejemplo:
import urllib.request 
proxy = urllib.request.ProxyHandler({'http': 'http://10.10.1.10:3128'})
opener = urllib.request.build_opener(proxy) 
with opener.open('https://www.example.com') as response: 
    print(response.read()) 

#HTTPPasswordMgr y HTTPPasswordMgrWithDefaultRealm: Estas clases manejan credenciales HTTP para autenticación básica. Ejemplo:
import urllib.request
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm() 
password_mgr.add_password(None, 'https://www.example.com', 'user', 'password') 
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler) 
with opener.open('https://www.example.com') as response: 
    print(response.read()) 


#2. urllib.parse
#ParseResult: Es la clase que representa el resultado de analizar una URL con funciones como urlparse(). Contiene los componentes de la URL: esquema, dominio, ruta, etc. Ejemplo:
import urllib.parse 
parsed_url = urllib.parse.urlparse('https://www.example.com/path?name=value#fragment') 
print(parsed_url) 

SplitResult: Similar a ParseResult, pero se utiliza con urlsplit(), que no divide los parámetros de consulta. Ejemplo:
import urllib.parse 
split_url = urllib.parse.urlsplit('https://www.example.com/path?name=value#fragment') 
print(split_url) 


#3. urllib.robotparser
#RobotFileParser: Esta clase permite leer y analizar un archivo robots.txt, determinando si una URL puede ser accedida por robots o crawlers según las reglas del archivo robots.txt. Ejemplo:
import urllib.robotparser
rp = urllib.robotparser.RobotFileParser()
rp.set_url('https://www.example.com/robots.txt') 
rp.read() 
print(rp.can_fetch('*', 'https://www.example.com/path')) 


#4. urllib.error
#URLError: Esta clase es una excepción base para los errores relacionados con las URL, como cuando no se puede acceder a una URL o si no se encuentra. Ejemplo:
import urllib.request
try: 
    urllib.request.urlopen('https://nonexistent-url.com')
except urllib.error.URLError as e: 
    print(f"Error: {e.reason}") 

#HTTPError: Esta clase es una subclase de URLError y se utiliza para manejar errores específicos de HTTP (como errores 404, 500, etc.). Ejemplo:
import urllib.request
try:
    urllib.request.urlopen('https://httpbin.org/status/404') 
except urllib.error.HTTPError as e: 
    print(f"Error HTTP {e.code}: {e.reason}") 

#ContentTooShortError: Excepción que ocurre cuando el contenido descargado es más corto de lo esperado. Ejemplo:
import urllib.request 
try:
    urllib.request.urlretrieve('https://www.example.com', 'file.txt')
except urllib.error.ContentTooShortError as e: 
    print("Content is too short.") 





"""Variables y Constantes del Módulo urllib"""

#urllib.__version__: Contiene la versión actual del módulo urllib. Ejemplo: 
print(urllib.__version__) #Esto te devuelve la versión del módulo instalado en tu entorno.

#urllib.parse._MAXCACHE: Controla el tamaño máximo de la caché interna que usa urllib.parse para almacenar los resultados de análisis de URL. Si la caché supera este tamaño, los elementos más antiguos se eliminan. Ejemplo: 
print(urllib.parse._MAXCACHE) # Muestra el valor por defecto de la caché 

#urllib.request.urlopen: Aunque no es una "variable", es una función que permite abrir una URL. Se puede ver como un "valor" central que facilita acceder a recursos en línea. Ejemplo:
with urllib.request.urlopen('https://www.example.com') as response: 
    print(response.read()) 

#urllib.request._opener: Es un objeto OpenerDirector utilizado internamente por urllib.request para realizar las operaciones de apertura de URL. No es comúnmente utilizado directamente, pero puede ser útil para tareas avanzadas de configuración personalizada de manejo de URLs. Ejemplo: 
print(urllib.request._opener) # Muestra el OpenerDirector interno 

#urllib.robotparser._DEFAULT_AGENT: Es la cadena de agente de usuario que se utiliza por defecto en RobotFileParser. Esta cadena se usa para simular el comportamiento de un robot/crawler web al leer archivos robots.txt. Ejemplo: 
import urllib.robotparser
print(urllib.robotparser._DEFAULT_AGENT) # Muestra el agente predeterminado 



"""Constantes del Módulo urllib"""

#urllib.parse.urlsplit: Define cómo dividir una URL en sus componentes (esquema, netloc, path, query y fragmento). Ejemplo: 
result = urllib.parse.urlsplit('https://www.example.com/path?name=value#fragment') 
print(result) # Esto devuelve un objeto SplitResult con los componentes de la URL.

#urllib.parse.urlparse: Similar a urlsplit, pero más detallado, incluye la posibilidad de manejar parámetros, como params en la URL. Ejemplo:
result = urllib.parse.urlparse('https://www.example.com/path;params?name=value#fragment') 
print(result) # Esto devuelve un objeto ParseResult que divide la URL en sus partes.

#urllib.parse.uses_relative: Una lista de esquemas que permiten URLs relativas, es decir, que no requieren un esquema explícito como http o https. Ejemplo: 
print(urllib.parse.uses_relative) #Esto devuelve una lista de esquemas que pueden utilizar rutas relativas, como ftp, file, etc.

#urllib.parse.uses_netloc: Una lista de esquemas que requieren un componente de netloc (dominio o dirección de red). Ejemplo: 
print(urllib.parse.uses_netloc) # Esto muestra los esquemas que requieren un componente de red, como http, https, ftp, entre otros.

#urllib.parse.uses_params: Una lista de esquemas que permiten parámetros en la URL. Ejemplo: 
print(urllib.parse.uses_params) 

#urllib.parse.uses_query: Una lista de esquemas que permiten consultas (query) en la URL. Ejemplo: 
print(urllib.parse.uses_query) 

#urllib.parse.uses_fragment: Una lista de esquemas que permiten un fragmento (fragment) en la URL. Ejemplo: 
print(urllib.parse.uses_fragment) 

#urllib.request.URLopener.version: Especifica la versión del agente de usuario (User-Agent) que se usará en las solicitudes realizadas con URLopener. Ejemplo: 
opener = urllib.request.URLopener() 
print(opener.version) #Esto muestra la versión del agente de usuario que usa URLopener.

#urllib.robotparser.RobotFileParser._DEFAULT_AGENT : La constante que define el agente de usuario predeterminado que se utiliza para las solicitudes al archivo robots.txt. Ejemplo: 
import urllib.robotparser 
print(urllib.robotparser.RobotFileParser._DEFAULT_AGENT) 



"""Excepciones del Módulo urllib"""

#urllib.error.URLError: Es la excepción base para todos los errores relacionados con URLs. Se lanza cuando ocurre un error al intentar acceder a una URL, como cuando no se puede llegar a un servidor o la URL no es válida. Ejemplo: 
import urllib.request 
try:
    urllib.request.urlopen('https://nonexistent-url.com') 
except urllib.error.URLError as e: 
    print(f"Error: {e.reason}") #Esto captura y muestra el error, como hostname not found.

#urllib.error.HTTPError: Es una subclase de URLError y se lanza cuando hay un error específico de HTTP, como un código de estado 404 (No encontrado), 500 (Error interno del servidor), etc. Ejemplo: 
import urllib.request
try: 
    urllib.request.urlopen('https://httpbin.org/status/404')
except urllib.error.HTTPError as e: 
    print(f"Error HTTP {e.code}: {e.reason}")
# Esto captura un error HTTP y muestra el código de estado y la razón (por ejemplo, "404 Not Found").

#urllib.error.ContentTooShortError: Se lanza cuando se descarga menos contenido del esperado. Esto puede ocurrir al intentar descargar un archivo y el contenido recibido es más corto de lo que se esperaba. Ejemplo:
import urllib.request 
try: 
    urllib.request.urlretrieve('https://www.example.com/smallfile.txt', 'file.txt')
except urllib.error.ContentTooShortError as e:
    print("El contenido descargado es más corto de lo esperado.") 

#urllib.error._splitnport: Esta excepción se lanza internamente cuando se produce un error relacionado con la división de un puerto en una URL, pero generalmente no es utilizada directamente por el usuario.
#urllib.robotparser.RobotFileParserError: Se lanza cuando se encuentra un error al intentar leer un archivo robots.txt, como si el archivo tiene un formato incorrecto o no es accesible. Ejemplo: 
import urllib.robotparser 
try:
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url('https://www.example.com/robots.txt') 
    rp.read() except urllib.robotparser.RobotFileParserError as e: 
    print("Error al leer el archivo robots.txt") 

#URLError: Excepción base para errores relacionados con URLs.
#HTTPError: Error específico de un código HTTP, como 404 o 500.
#ContentTooShortError: Cuando el contenido descargado es más corto de lo esperado.
#RobotFileParserError: Error al leer o procesar archivos robots.txt.



"""Submódulos del Módulo urllib"""

#urllib.parse: Este submódulo se utiliza para analizar, construir y modificar URLs. Permite separar una URL en sus componentes (como esquema, dominio, path, parámetros, etc.) y recomponerlos de nuevo.
#Funciones principales: 
#urlparse(): Analiza una URL y la descompone en sus componentes.
#urlunparse(): Reconstruye una URL a partir de sus componentes.
#urlencode(): Codifica un diccionario o secuencia de tuplas en una cadena de consulta.
#quote(), unquote(): Codifica o decodifica partes de una URL. Ejemplo:
import urllib.parse
result = urllib.parse.urlparse('https://www.example.com/path?query=value#fragment') 
print(result) 

#urllib.request: Este submódulo permite realizar solicitudes HTTP, abrir URLs, y descargar contenido desde la web. También permite configurar encabezados, autenticación, y manejar errores en las solicitudes.
#Funciones principales: 
#urlopen(): Abre una URL y devuelve un objeto de respuesta.
#urlretrieve(): Descarga un archivo desde una URL.
#Request(): Crea una solicitud HTTP personalizada. Ejemplo: 
import urllib.request
with urllib.request.urlopen('https://www.example.com') as response: 
    print(response.read()) 

#urllib.error: Contiene las excepciones que pueden ocurrir al trabajar con URLs y solicitudes HTTP, como URLError y HTTPError. Ejemplo: 
import urllib.request
try: 
    urllib.request.urlopen('https://nonexistent-url.com') 
except urllib.error.URLError as e: 
    print(f"Error: {e.reason}") 

#urllib.robotparser: Este submódulo permite analizar archivos robots.txt para determinar si un agente de usuario (como un crawler) tiene permiso para acceder a ciertas partes de un sitio web.
#Funciones principales: 
#RobotFileParser(): Analiza un archivo robots.txt y permite consultar las reglas para acceder a un sitio.
#read(): Lee el contenido de un archivo robots.txt.
#can_fetch(): Determina si una URL puede ser accedida según las reglas de robots.txt. Ejemplo:
import urllib.robotparser 
rp = urllib.robotparser.RobotFileParser() 
rp.set_url('https://www.example.com/robots.txt') 
rp.read()
print(rp.can_fetch('*', 'https://www.example.com/somepath')) 

#urllib.parse: Manipulación y análisis de URLs.
#urllib.request: Realización de solicitudes HTTP y manejo de respuestas.
#urllib.error: Excepciones relacionadas con las solicitudes HTTP y URLs.
#urllib.robotparser: Análisis de archivos robots.txt para gestionar el acceso de crawlers a los sitios web.

