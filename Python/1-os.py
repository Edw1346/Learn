#El modulo os sirve p

#Métodos
import os 

#os.getcwd() Obtiene el directorio de trabajo actual.
print(os.getcwd()) # Ejemplo: /home/user/proyecto 

#os.chdir(path)  Cambia el directorio de trabajo actual.
os.chdir('/home/user/documentos') 
print(os.getcwd()) # Ahora apunta a /home/user/documentos 

#os.listdir(path='.') Lista archivos y carpetas en un directorio.
print(os.listdir('.'))  # ['archivo.txt', 'carpeta', 'script.py'] 

#os.mkdir(path)   Crea un nuevo directorio.
os.mkdir('nueva_carpeta') 

#os.makedirs(path, exist_ok=False)    Crea directorios de forma recursiva.
os.makedirs('proyectos/python/codigo', exist_ok=True) 

#os.remove(path)     Elimina un archivo.
os.remove('archivo.txt') 

os.rmdir(path)  # Elimina un directorio vacío.
os.rmdir('carpeta_vacia') 

#os.removedirs(path)  Elimina directorios de forma recursiva.
os.removedirs('proyectos/python/codigo') 

#os.rename(src, dst)  Renombra un archivo o directorio.
os.rename('documento.txt', 'nuevo_nombre.txt') 

#os.stat(path)  Obtiene información sobre un archivo o directorio.
info = os.stat('script.py') 
print(info.st_size) # Tamaño del archivo en bytes 

#os.path.join(path, *paths)  Une rutas de manera segura.
ruta = os.path.join('/home/user', 'documentos', 'archivo.txt') 
print(ruta) # '/home/user/documentos/archivo.txt' en Linux/Mac 

#os.path.exists(path)  Verifica si una ruta existe.
print(os.path.exists('archivo.txt')) # True o False 

#os.path.isfile(path)  Verifica si una ruta es un archivo.
print(os.path.isfile('archivo.txt')) # True o False 

#os.path.isdir(path)  Verifica si una ruta es un directorio.
print(os.path.isdir('carpeta')) # True o False 

#os.environ  Accede a las variables de entorno.
print(os.environ['HOME']) # Ruta del directorio de usuario 

#os.getenv(var_name, default=None)  Obtiene una variable de entorno.
print(os.getenv('PATH')) # Muestra el PATH del sistema 

#os.system(command)  Ejecuta un comando en la terminal.
os.system('ls') # En Linux/macOS muestra archivos; en Windows usar 'dir' 

#os.walk(top, topdown=True)  Recorre un directorio y sus subdirectorios.
for root, dirs, files in os.walk('.'): 
    print(root, dirs, files) 

#os.cpu_count()  Devuelve el número de núcleos del procesador.
print(os.cpu_count()) # Ejemplo: 8 

#os.urandom(n)  Genera n bytes aleatorios de forma segura.
print(os.urandom(8)) # b'\xa3\x98...' 


"""Clases del módulo os"""

os.DirEntry
#Representa una entrada en un directorio, que se obtiene al iterar sobre un directorio usando os.scandir(). Contiene información sobre archivos y directorios, como si es un archivo o un directorio, su nombre y otras propiedades.

with os.scandir('.') as entries: 
    for entry in entries: 
    print(entry.name, entry.is_file()) 

os.PathLike
#Esta clase es utilizada por objetos que representan rutas de archivo y directorios. La clase PathLike es una interfaz para objetos que pueden ser convertidos en una ruta válida. Muchos módulos como pathlib devuelven objetos que implementan esta clase.

from pathlib import Path 
p = Path('/home/user/documentos') 
print(isinstance(p, os.PathLike)) # True 

os.FSPath
#FSPath es una interfaz para los objetos que pueden ser utilizados como rutas del sistema de archivos. Es una clase base para objetos de rutas, como cadenas de texto o instancias de la clase pathlib.Path.

from pathlib import Path 
p = Path('archivo.txt') 
print(isinstance(p, os.FSPath)) # True 

os._exit(status)
#Aunque no es exactamente una clase, esta función de bajo nivel se utiliza para finalizar el proceso inmediatamente con un código de salida. No es una clase, pero vale la pena mencionarlo ya que se encuentra en el módulo os.
os._exit(0) # Finaliza el proceso con estado 0 (sin errores) 



"""Variables del módulo os"""

os.name
#Esta variable contiene el nombre del sistema operativo. Es útil para realizar comprobaciones entre diferentes sistemas operativos (por ejemplo, 'posix' para Linux/Mac, 'nt' para Windows).
print(os.name) # 'posix', 'nt', etc. 

os.environ
#Es un diccionario que contiene las variables de entorno del sistema. Puedes acceder y modificar las variables de entorno a través de esta variable.
print(os.environ) # Muestra todas las variables de entorno print(os.environ['HOME']) # Muestra el valor de la variable HOME 

os.curdir
#Esta variable representa el nombre del directorio actual, generalmente un punto (.), que es utilizado por varias funciones relacionadas con rutas.
print(os.curdir) # '.' 

os.pardir
#Representa el nombre del directorio padre, generalmente dos puntos (..). Se usa en rutas para hacer referencia al directorio superior.
print(os.pardir) # '..' 

os.sep
#Es el separador de directorios utilizado en el sistema operativo. En Windows es '\', y en Linux/macOS es '/'.
print(os.sep) # '\\' en Windows, '/' en Linux/Mac 

os.altsep
#Es un separador alternativo de directorios, que es usado en algunos sistemas, como en Windows con la barra invertida (\). Puede ser None en sistemas que no lo usan.
print(os.altsep) # '\\' en Windows, None en otros sistemas 

os.linesep
#Representa el carácter utilizado para separar líneas en el sistema operativo actual. En Windows es \r\n y en Linux/macOS es \n.
print(os.linesep) # '\r\n' en Windows, '\n' en Linux/Mac 

os.name
#Al igual que mencionamos antes, proporciona el nombre del sistema operativo. Esto se utiliza a menudo en bloques condicionales para detectar la plataforma y tomar decisiones específicas según sea necesario.
print(os.name) # 'posix', 'nt', 'os2', etc. 

os.path
#Es un submódulo dentro de os que contiene funciones útiles para trabajar con rutas de archivos, como os.path.join(), os.path.exists(), os.path.isdir(), etc.
print(os.path) # Acceso a funciones de ruta como os.path.join() 

os.urandom()
#Aunque es una función, también puede considerarse parte de las variables al usarla para generar datos aleatorios de manera segura. Se usa para obtener n bytes de datos aleatorios.
print(os.urandom(10)) # Genera 10 bytes de datos aleatorios 


"""Constantes del módulo os"""

os.O_RDONLY
#Especifica la constante para abrir un archivo en modo solo lectura.
fd = os.open('archivo.txt', os.O_RDONLY) 

os.O_WRONLY
#Especifica la constante para abrir un archivo en modo solo escritura.
fd = os.open('archivo.txt', os.O_WRONLY) 

os.O_RDWR
#Especifica la constante para abrir un archivo en modo de lectura y escritura.
fd = os.open('archivo.txt', os.O_RDWR) 

os.O_APPEND
#Especifica la constante para abrir un archivo en modo de solo anexado (agregar al final del archivo).
fd = os.open('archivo.txt', os.O_APPEND) 

os.O_CREAT
#Especifica la constante para crear un archivo si no existe.
fd = os.open('nuevo_archivo.txt', os.O_CREAT | os.O_WRONLY) 

os.O_EXCL
#Especifica la constante para garantizar que el archivo sea creado, es decir, no puede existir previamente.
fd = os.open('archivo_unico.txt', os.O_CREAT | os.O_EXCL) 

os.O_TRUNC
#Especifica la constante para truncar un archivo (eliminar su contenido) cuando se abre en modo escritura.
fd = os.open('archivo.txt', os.O_WRONLY | os.O_TRUNC) 

os.F_OK
#Especifica la constante para comprobar si un archivo existe.
if os.access('archivo.txt', os.F_OK): 
    print('El archivo existe.') 

os.R_OK
#Especifica la constante para comprobar si un archivo es legible.
if os.access('archivo.txt', os.R_OK): 
    print('El archivo es legible.') 

os.W_OK
#Especifica la constante para comprobar si un archivo es escribible.
if os.access('archivo.txt', os.W_OK): 
    print('El archivo es escribible.') 

os.X_OK
#Especifica la constante para comprobar si un archivo es ejecutable.
if os.access('archivo.sh', os.X_OK): 
    print('El archivo es ejecutable.') 

os.P_WAIT
#Especifica una constante usada para esperar a que un proceso hijo termine.
status = os.waitpid(0, os.P_WAIT) 

os.P_NOWAIT
#Especifica una constante usada para no esperar a que un proceso hijo termine.
pid = os.spawnl(os.P_NOWAIT, 'comando') 

os.P_DETACH
#Especifica una constante usada para separar un proceso hijo de su padre (en lugar de esperar).
os.spawnl(os.P_DETACH, 'comando') 

os.SEEK_SET
#Especifica la constante utilizada para reposicionar el puntero de archivo desde el principio del archivo.
os.lseek(fd, 0, os.SEEK_SET) 

os.SEEK_CUR
#Especifica la constante utilizada para reposicionar el puntero de archivo desde la posición actual.
os.lseek(fd, 0, os.SEEK_CUR) 

os.SEEK_END
#Especifica la constante utilizada para reposicionar el puntero de archivo desde el final del archivo.
os.lseek(fd, 0, os.SEEK_END) 

os.S_IFDIR
#Especifica la constante que representa un tipo de archivo de directorio en la información del archivo.
info = os.stat('directorio') if stat.S_IFDIR & info.st_mode: print('Es un directorio') 

os.S_IFREG
#Especifica la constante que representa un tipo de archivo regular (archivo de texto, por ejemplo).
info = os.stat('archivo.txt') 
if stat.S_IFREG & info.st_mode: 
    print('Es un archivo regular') 

os.TMP_MAX
#Especifica el número máximo de archivos temporales que se pueden generar.
print(os.TMP_MAX) # Generalmente 238 


"""Excepciones del módulo os"""

os.error
#Es la excepción base para todos los errores relacionados con el sistema operativo. Se utiliza cuando ocurre un error en las funciones del módulo os. En versiones más recientes de Python, OSError es más común, pero os.error aún está disponible por compatibilidad.
try: 
    os.remove('archivo_que_no_existe.txt') 
except os.error as e:
    print(f"Error del sistema operativo: {e}") 

OSError
#Es una subclase de os.error que se usa cuando ocurre un error relacionado con el sistema operativo, como problemas de permisos, fallos al abrir archivos, directorios no encontrados, etc. Es una de las excepciones más comunes en operaciones con el sistema de archivos.
try:
    os.remove('archivo_que_no_existe.txt') 
except OSError as e: 
    print(f"Error: {e.strerror}") 

FileNotFoundError
#Es una subclase de OSError que se genera cuando no se puede encontrar el archivo o directorio especificado. Se usa cuando se intenta abrir o manipular un archivo que no existe.
try: 
    os.remove('archivo_inexistente.txt') 
except FileNotFoundError as e: 
    print(f"Archivo no encontrado: {e}") 

IsADirectoryError
#Es una subclase de OSError que se genera cuando se intenta realizar una operación en un archivo que en realidad es un directorio, como intentar abrir un directorio con open().
try: 
    os.remove('directorio') # Intentando eliminar un directorio como archivo
except IsADirectoryError as e: 
    print(f"No se puede eliminar un directorio como archivo: {e}") 

PermissionError
#Es una subclase de OSError que se genera cuando se intenta realizar una operación en un archivo o directorio sin los permisos adecuados, como intentar modificar un archivo de solo lectura o escribir en un directorio de solo lectura.
try: 
    os.remove('archivo_solo_lectura.txt') 
except PermissionError as e: 
    print(f"Permiso denegado: {e}") 

NotADirectoryError
#Es una subclase de OSError que se genera cuando se espera que una ruta sea un directorio, pero es un archivo regular. Es útil cuando trabajas con funciones como os.listdir() que esperan directorios.
try: 
    os.listdir('archivo.txt') # Intentando listar archivos de un archivo regular 
except NotADirectoryError as e: 
    print(f"No es un directorio: {e}") 

TimeoutError
#Es una subclase de OSError que se genera cuando una operación de I/O supera el tiempo de espera establecido. Por 
#ejemplo, cuando se usa os.system() con un comando que tarda más tiempo de lo esperado.
try:  # Este ejemplo depende del sistema, pero simula una operación que podría exceder el tiempo de espera. 
    os.system('comando_que_tarda') # En caso de error por tiempo de espera 
except TimeoutError as e: 
    print(f"Tiempo de espera agotado: {e}") 




"""Submódulos del módulo os"""

os.path
#Proporciona funciones para manipular rutas de archivos y directorios. Es uno de los submódulos más utilizados y tiene métodos para realizar operaciones como unir rutas, comprobar si un archivo existe, obtener el nombre del archivo, y más.
import os.path 
print(os.path.exists('archivo.txt')) # Verifica si el archivo existe 

os.scandir
#Es un submódulo para iterar de manera eficiente sobre directorios. Utiliza os.DirEntry para representar las entradas en un directorio, y proporciona información como si una entrada es un archivo o un directorio.

with os.scandir('.') as entries:
    for entry in entries:
        print(entry.name, entry.is_file()) 

os.remove
#Aunque no es un submódulo en sí, esta función está incluida dentro del módulo os y permite eliminar archivos del sistema de archivos.
os.remove('archivo.txt') # Elimina el archivo 'archivo.txt' 

os.rename
#Similar a os.remove, os.rename permite cambiar el nombre de un archivo o moverlo a una nueva ubicación.
os.rename('archivo_viejo.txt', 'archivo_nuevo.txt') # Renombra un archivo 

os.urandom
#Utiliza este submódulo para generar números aleatorios de alta calidad criptográfica.
print(os.urandom(10)) # Genera 10 bytes de datos aleatorios 

os.fork
#En sistemas Unix, os.fork() crea un nuevo proceso al duplicar el proceso actual. Este submódulo se usa principalmente para trabajar con procesos y multitarea en sistemas tipo Unix.
pid = os.fork()
if pid == 0: print("Soy el proceso hijo") 
else: print("Soy el proceso padre") 

os.spawn
#El submódulo spawn se utiliza para ejecutar nuevos procesos en Unix, con opciones para controlar la forma en que se ejecutan los procesos (como esperar que terminen o no).
pid = os.spawnl(os.P_WAIT, 'comando', 'arg1', 'arg2') # Ejecuta un comando y espera su finalización 

os.environ
#Aunque es una variable dentro de os, es útil como un "submódulo" porque permite acceder y modificar las variables de entorno del sistema operativo.
print(os.environ['HOME']) # Accede al valor de la variable de entorno HOME 

os.stat
#El submódulo stat proporciona información detallada sobre un archivo o directorio, como sus permisos, fecha de modificación, y más.
print(os.stat('archivo.txt')) 

os.sysctl
#Este submódulo está presente en sistemas Unix (Linux/macOS) y permite consultar y modificar parámetros del núcleo del sistema operativo.
print(os.sysctl('kern.hostname')) # Ejemplo de consulta del nombre de host 

