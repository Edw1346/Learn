import socket

"""El módulo socket de Python proporciona una interfaz para trabajar con redes y conexiones de bajo nivel, como crear servidores 
y clientes para la comunicación en red utilizando TCP, UDP y otros protocolos de red."""



"""Funciones del módulo socket"""

#1. socket.socket(family, type, proto=0). Crea un nuevo objeto socket. Puedes especificar la familia (como AF_INET para IPv4 o AF_INET6 para IPv6) y el tipo (como SOCK_STREAM para TCP o SOCK_DGRAM para UDP). Ejemplo:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#2. socket.connect(address). Conecta el socket a la dirección remota especificada por address (una tupla de (host, puerto)). Ejemplo:
s.connect(('localhost', 8080)) 

#3. socket.bind(address). Asocia el socket a la dirección local especificada por address (una tupla de (host, puerto)). Ejemplo:
s.bind(('localhost', 8080)) 

#4. socket.listen(backlog). Hace que el socket escuche conexiones entrantes. backlog es el número de conexiones que pueden estar en espera. Ejemplo:
s.listen(5) 

#5. socket.accept(). Bloquea el proceso y espera a aceptar una conexión entrante. Devuelve una nueva conexión de socket y la dirección del cliente. Ejemplo:
conn, addr = s.accept() 

#6. socket.send(bytes). Envía datos a través de un socket. El argumento bytes debe ser un objeto de tipo bytes. Ejemplo:
s.send(b'Hola, servidor') 

#7. socket.recv(bufsize). Recibe datos a través del socket. El argumento bufsize especifica el tamaño máximo del búfer de recepción. Ejemplo:
data = s.recv(1024) 

#8. socket.sendall(bytes). Envía todos los datos en un solo bloque. Esta función asegura que todos los datos sean enviados. Ejemplo:
s.sendall(b'Envio completo de datos') 

#9. socket.recvfrom(bufsize). Recibe datos desde un socket de tipo SOCK_DGRAM (UDP). Devuelve una tupla (data, address). Ejemplo:
data, addr = s.recvfrom(1024) 

#10. socket.sendto(bytes, address). Envía datos a una dirección específica. Este método se usa para sockets UDP. Ejemplo:
s.sendto(b'Hola', ('localhost', 8080)) 

#11. socket.setsockopt(level, optname, value). Establece una opción de socket. Los parámetros incluyen el nivel de la opción (como SOL_SOCKET) y el valor que deseas establecer. Ejemplo:
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

#12. socket.getsockopt(level, optname). Obtiene el valor de una opción de socket. Ejemplo:
value = s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR) 

#13. socket.setblocking(flag). Controla si el socket está en modo de bloqueo o no bloqueo. Si flag es False, el socket está en modo no bloqueante. Ejemplo:
s.setblocking(False) 

#14. socket.getpeername(). Devuelve la dirección remota (cliente) de un socket conectado. Ejemplo:
addr = s.getpeername() 

#15. socket.getsockname(). Devuelve la dirección local (servidor) del socket. Ejemplo:
addr = s.getsockname() 

#16. socket.shutdown(how). Cierra una parte de la conexión del socket. how puede ser:
#socket.SHUT_RD: Cierra solo la parte de lectura.
#socket.SHUT_WR: Cierra solo la parte de escritura.
#socket.SHUT_RDWR: Cierra ambas. Ejemplo:
s.shutdown(socket.SHUT_WR) 

#17. socket.close(). Cierra el socket. Es importante cerrar el socket después de usarlo para liberar los recursos. Ejemplo:
s.close() 

#18. socket.getaddrinfo(host, port). Obtiene información de la dirección de un host y puerto. Devuelve una lista de tuplas con detalles sobre la dirección y el tipo de socket. Ejemplo:
info = socket.getaddrinfo('localhost', 8080) 

#19. socket.gethostbyname(hostname). Convierte un nombre de host en una dirección IP. Ejemplo:
ip = socket.gethostbyname('localhost') 

#20. socket.gethostbyname_ex(hostname). Obtiene información completa de un host, incluyendo el nombre completo del dominio y las direcciones IP asociadas. Ejemplo:
hostname, aliaslist, ipaddrlist = socket.gethostbyname_ex('localhost') 

#21. socket.getservbyname(servicename). Obtiene el número de puerto para un nombre de servicio (como http). Ejemplo:
port = socket.getservbyname('http') 

#22. socket.inet_aton(ip_string). Convierte una dirección IPv4 en su formato binario. Ejemplo:
binary_ip = socket.inet_aton('192.168.1.1') 

#23. socket.inet_ntoa(packed_ip). Convierte una dirección IPv4 desde su formato binario a una cadena de texto. Ejemplo:
ip = socket.inet_ntoa(b'\xc0\xa8\x01\x01') 

#24. socket.inet_pton(address_family, ip_string). Convierte una dirección IP en su formato binario según el tipo de dirección (AF_INET o AF_INET6). Ejemplo:
binary_ip = socket.inet_pton(socket.AF_INET, '192.168.1.1') 

#25. socket.inet_ntop(address_family, packed_ip). Convierte una dirección IP desde su formato binario a una cadena de texto según el tipo de dirección. Ejemplo:
ip = socket.inet_ntop(socket.AF_INET, b'\xc0\xa8\x01\x01') 



"""Clases del módulo socket"""

#1. socket.socket. La clase principal en el módulo socket. Representa un socket de red que puede ser usado para crear conexiones cliente o servidor, enviar y recibir datos, y realizar otras operaciones de red.
#Atributos importantes:
#family: Define la familia de direcciones (como AF_INET para IPv4).
#type: Define el tipo de socket (como SOCK_STREAM para TCP o SOCK_DGRAM para UDP).
#Métodos comunes:
#connect(): Conecta el socket a un servidor.
#bind(): Enlaza el socket a una dirección y puerto.
#listen(): Configura el socket para escuchar conexiones entrantes.
#accept(): Acepta una conexión entrante.
#send(): Envía datos a través del socket.
#recv(): Recibe datos a través del socket.
#close(): Cierra el socket. Ejemplo:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Conectar a un servidor 
s.connect(('localhost', 8080)) # Enviar datos 
s.send(b'Hola, servidor') # Recibir datos 
data = s.recv(1024) # Cerrar el socket s.close() 

#2. socket.socketpair(). Esta función crea un par de sockets conectados entre sí, lo cual es útil para la comunicación entre procesos (IPC). Los sockets pueden ser utilizados para enviar y recibir datos entre ellos, como si fueran un socket cliente-servidor, pero en un único programa.
sock1, sock2 = socket.socketpair() # Enviar un mensaje desde 
sock1 sock1.send(b'Hola desde sock1') # Recibir el mensaje en sock2 
data = sock2.recv(1024) 
print(data.decode()) # Cerrar los sockets 
sock1.close()
sock2.close() 

#3. socket.socket.fileno(). Este método devuelve un descriptor de archivo para el socket. El descriptor de archivo es un número entero que se puede utilizar en operaciones de bajo nivel, como en el uso de la selección de multiplexación de entrada/salida (por ejemplo, select.select()).
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Obtener el descriptor de archivo del socket 
fd = s.fileno() 
print(f'Descriptor de archivo del socket: {fd}') 

#4. socket.timeout. Aunque no es exactamente una "clase" como tal, socket.timeout es una excepción que puede ser lanzada por los métodos de socket cuando se alcanza el tiempo de espera durante la operación de red (por ejemplo, al intentar hacer una conexión o recibir datos). Esta excepción se utiliza cuando un socket está configurado con un tiempo de espera específico.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.settimeout(5) # Tiempo de espera de 5 segundos 
try: 
    s.connect(('localhost', 8080)) 
except socket.timeout: 
    print('La conexión ha superado el tiempo de espera.') 
finally: s.close() 

#5. socket.HOSTNAME (Constante). Es una constante que devuelve el nombre del host local. Se usa generalmente con gethostbyname() y otros métodos relacionados.
hostname = socket.gethostname()
print(f'Nombre del host local: {hostname}') 





"""El módulo socket de Python no tiene muchas "variables" pero tiene varias constantes y valores predefinidos para establecer las configuraciones y co configuración de los sockets."""



"""Constantes del módulo socket"""

#1. socket.AF_INET. Define la familia de direcciones para IPv4. Es utilizada cuando se está trabajando con direcciones IPv4. Ejemplo de uso:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#2. socket.AF_INET6. Define la familia de direcciones para IPv6. Se utiliza cuando se está trabajando con direcciones IPv6. Ejemplo de uso:
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM) 

#3. socket.AF_UNIX. Define la familia de direcciones para Unix Domain Sockets. Se utiliza para crear sockets de comunicación entre procesos en la misma máquina (no requiere red). Ejemplo de uso:
s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) 

#4. socket.SOCK_STREAM. Define el tipo de socket TCP (orientado a la conexión). Es el tipo de socket más comúnmente usado para comunicación fiable. Ejemplo de uso:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#5. socket.SOCK_DGRAM. Define el tipo de socket UDP (sin conexión). Se utiliza para aplicaciones que no requieren una conexión fiable, como transmisión de datos en tiempo real. Ejemplo de uso:
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

#6. socket.SOCK_RAW. Define un socket RAW. Se usa para acceder a protocolos de bajo nivel (como ICMP) o para la creación de paquetes personalizados. Ejemplo de uso:
s = socket.socket(socket.AF_INET, socket.SOCK_RAW) 

#7. socket.SOL_SOCKET. Especifica que la opción de socket que se está configurando o consultando se refiere al nivel de socket. Ejemplo de uso:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

#8. socket.IPPROTO_TCP. Define que el protocolo utilizado es TCP. Se utiliza con sockets de tipo RAW para indicar que se trabaja con el protocolo TCP. Ejemplo de uso:
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP) 

#9. socket.IPPROTO_UDP. Define que el protocolo utilizado es UDP. Se usa con sockets RAW para indicar que se está utilizando el protocolo UDP. Ejemplo de uso:
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP) 

#10. socket.SO_REUSEADDR. Esta constante se usa con setsockopt() para permitir la reutilización de una dirección y puerto en el mismo socket. Es útil para servidores que deben reiniciarse rápidamente. Ejemplo de uso:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

#11. socket.SO_BROADCAST. Habilita el envío de paquetes de broadcast (difusión) para un socket UDP. Ejemplo de uso:
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) 

#12. socket.SO_RCVBUF. Define el tamaño del búfer de recepción del socket. Se usa con setsockopt() para controlar el tamaño de la memoria asignada para recibir datos. Ejemplo de uso:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024) 

#13. socket.SO_SNDBUF. Define el tamaño del búfer de envío del socket. Se usa con setsockopt() para controlar el tamaño de la memoria asignada para enviar datos. Ejemplo de uso:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2048) 

#14. socket.SO_LINGER. Establece la opción linger (tiempo de espera) para controlar el comportamiento de cierre del socket. Si se activa, el socket intentará enviar los datos pendientes antes de cerrarse. Ejemplo de uso:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
linger = socket.struct.pack('ii', 1, 5) # Activar linger, esperando 5 segundos 
s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, linger) 

#15. socket.MSG_OOB. Especifica que los datos enviados deben ser fuera de banda. Se utiliza para enviar señales urgentes en una conexión TCP.Ejemplo de uso:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.send(b'Hola', socket.MSG_OOB) 

#16. socket.MSG_PEEK. Permite ver los datos que están en el búfer de recepción, pero no eliminarlos del búfer. Ejemplo de uso:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
data = s.recv(1024, socket.MSG_PEEK) # Ver los datos sin eliminarlos del búfer 

#17. socket.AI_PASSIVE. Indica que se deben buscar direcciones locales pasivas, usadas por ejemplo para servidores.

#18. socket.AI_CANONNAME. Se utiliza en getaddrinfo() para obtener el nombre canónico del host.

#19. socket.AI_NUMERICHOST. Se utiliza en getaddrinfo() para obtener una dirección numérica en lugar de un nombre de host.

#20. socket.PF_INET (deprecated). Antiguamente se utilizaba para especificar la familia de direcciones IPv4. Actualmente, se recomienda usar AF_INET.



"""Excepciones del módulo socket"""

#1. socket.error. Es la excepción base para todos los errores relacionados con los sockets. Si ocurre un error en las operaciones de sockets, esta excepción es la que se lanza. En la mayoría de los casos, es mejor usar excepciones más específicas (como socket.timeout o socket.gaierror), pero socket.error captura errores generales de sockets. Ejemplo de uso:
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect(('localhost', 80)) 
except socket.error as e: 
    print(f"Ocurrió un error de socket: {e}") 

#2. socket.timeout. Es una subclase de socket.error que se lanza cuando una operación de socket excede el tiempo de espera (timeout). Esto puede ocurrir, por ejemplo, cuando intentas conectarte a un servidor que no responde en el tiempo especificado. Ejemplo de uso:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.settimeout(5) # Establecer un timeout de 5 segundos
try: 
    s.connect(('localhost', 80)) 
except socket.timeout: 
    print("Se agotó el tiempo de espera para la conexión") 

#3. socket.gaierror. Esta excepción se lanza cuando ocurre un error al resolver un nombre de host utilizando getaddrinfo(). Es un error relacionado con el sistema de nombres de dominio (DNS), como cuando el nombre de host no se puede resolver a una dirección IP válida. Ejemplo de uso:
try: 
    host = "noexiste.com" socket.getaddrinfo(host, 80)
except socket.gaierror: 
    print(f"Error al resolver el nombre de host: {host}") 

#4. socket.herror. Es una excepción más específica que socket.gaierror. Se lanza cuando ocurre un error en la resolución de nombres de host mediante el sistema de nombres de dominio (DNS) de forma más detallada (por ejemplo, un error al obtener un nombre de host en particular). Ejemplo de uso:
try: 
    socket.gethostbyname("invalid_host")
except socket.herror as e: 
    print(f"Error de host: {e}") 

#5. socket.address. Aunque no es común, esta es una excepción más rara que puede ocurrir cuando se utiliza una dirección de socket incorrecta.

#6. socket.timeout. Cuando el socket no responde dentro del tiempo especificado, se lanza esta excepción, generalmente cuando no se recibe una respuesta de un servidor o la respuesta tarda demasiado tiempo.

#7. socket.sslerror. Esta excepción se lanza cuando se produce un error en la capa de seguridad de los sockets (SSL/TLS), generalmente cuando se establece una conexión segura (por ejemplo, HTTPS) y ocurre un error durante el protocolo SSL/TLS. Ejemplo de uso:
import ssl 
context = ssl.create_default_context() 
try: 
    connection = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname="example.com") 
    connection.connect(('example.com', 443)) 
except socket.sslerror as e: 
    print(f"Error SSL: {e}") 



"""El módulo socket en Python no tiene submódulos oficiales dentro de su propia estructura. Sin embargo, algunas funcionalidades 
adicionales relacionadas con sockets y redes se pueden encontrar en otros módulos de la biblioteca estándar de Python o en bibliotecas externas. """

#Módulos y Bibliotecas Relacionadas con socket

#1. ssl. El submódulo ssl se utiliza para proporcionar soporte de capa de seguridad (SSL/TLS) sobre un socket. Permite crear conexiones seguras a través de un socket, como HTTPS, y se usa típicamente cuando se necesitan conexiones cifradas. Ejemplo de uso:
import ssl # Crear un socket seguro (SSL)
context = ssl.create_default_context() 
connection = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname='example.com') 
connection.connect(('example.com', 443)) 

#2. socketserver. El módulo socketserver es útil para construir servidores de red. Facilita la creación de servidores TCP y UDP al proporcionar una abstracción de servidor que maneja la creación y administración de sockets. Ejemplo de uso:
import socketserver
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self): 
        data = self.request.recv(1024)
        self.request.sendall(data) 
        if __name__ == "__main__": 
            server = socketserver.TCPServer(("localhost", 9999), MyTCPHandler) 
            server.serve_forever() 

#3. selectors. El módulo selectors permite usar una interfaz de alto nivel para la multiplexación de I/O, que es útil cuando deseas manejar múltiples sockets de manera eficiente sin usar múltiples hilos o procesos. Ejemplo de uso:
import selectors 
sel = selectors.DefaultSelector() 
def accept_connection(sock):
    conn, addr = sock.accept()
    print(f"Conexión aceptada de {addr}") 
    conn.close() 

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_sock.bind(("localhost", 8080))
server_sock.listen(5) 
server_sock.setblocking(False) 
sel.register(server_sock, selectors.EVENT_READ, accept_connection) 

while True: 
    events = sel.select()
    for key, mask in events: 
        callback = key.data
        callback(key.fileobj) 

4. asyncio. Aunque asyncio no es un submódulo directo de socket, proporciona una API asíncrona para trabajar con sockets, permitiendo la creación de servidores y clientes asíncronos. Ejemplo de uso:
import asyncio 
async def handle_client(reader, writer): 
    data = await reader.read(100) 
    message = data.decode()
    addr = writer.get_extra_info('peername') 
    print(f"Received {message} from {addr}") 
    writer.close() 

async def main(): 
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888) 
    addr = server.sockets[0].getsockname() 
    print(f"Serving on {addr}") 

async with server:
    await server.serve_forever() 
    asyncio.run(main()) 

#5. http.client. Aunque no es un submódulo de socket, el módulo http.client permite realizar peticiones HTTP a través de sockets, proporcionando una interfaz para trabajar con servidores HTTP directamente. Ejemplo de uso:
import http.client 
conn = http.client.HTTPConnection("www.example.com") 
conn.request("GET", "/") 
response = conn.getresponse() 
print(response.status, response.reason) 
data = response.read() 
conn.close() 
