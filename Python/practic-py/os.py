import os 
from pathlib import Path 

#Métodos más útiles con ejemplos

# Obtiene el directorio de trabajo actual.
print(os.getcwd()) # Ejemplo: /home/user/proyecto 

# Cambia el directorio de trabajo actual. 
os.chdir('/home/edwin/Documentos/Proyectos/') 
print(os.getcwd()) # Ahora apunta a /home/user/documentos 

# Lista archivos y carpetas en un directorio. os.listdir
print(os.listdir('.')) 
# ['archivo.txt', 'carpeta', 'script.py'] 

# Crea un nuevo directorio. 
os.mkdir('Cap-Python') 

## Crea directorios de forma recursiva. #
#os.makedirs('proyectos/python/codigo', exist_ok=True) 

# Renombra un archivo o directorio.
os.rename('descargas.txt', 'documento.txt') 

# Elimina un directorio vacío.
os.rmdir('Cap-Python') 

## Elimina directorios de forma recursiva. #
#os.removedirs('proyectos/python/codigo') 

# Obtiene información sobre un archivo o directorio.
info = os.stat('documento.txt') 
print(info)
print(info.st_size) # Tamaño del archivo en bytes 

# Une rutas de manera segura. $
ruta = os.path.join('/home/edwin', 'Documentos', 'documento.txt') 
print(ruta) # '/home/user/documentos/archivo.txt' en Linux/Mac 

# Verifica si una ruta existe.
print(os.path.exists('/home/edwin/Documentos/Proyectos/')) # True o False 

# Verifica si una ruta es un archivo. #
print(os.path.isfile('documento.txt')) # True o False 

# Verifica si una ruta es un directorio. #
print(os.path.isdir('/home/edwin/Documentos/Proyectos')) # True o False 

# Accede a las variables de entorno. #
print(os.environ['HOME']) # Ruta del directorio de usuario 

# Obtiene una variable de entorno.
print(os.getenv('PATH')) # Muestra el PATH del sistema 

# Ejecuta un comando en la terminal.
os.system('ls') # En Linux/macOS muestra archivos; en Windows usar 'dir' 

# Recorre un directorio y sus subdirectorios.
for root, dirs, files in os.walk('.'): 
    print(root, dirs, files) 

# Devuelve el número de núcleos del procesador.
print(os.cpu_count()) # Ejemplo: 8 

# Genera n bytes aleatorios de forma segura.
print(os.urandom(8)) # b'\xa3\x98...' 

# Elimina un archivo.
os.remove('documento.txt') 


#Clases del módulo os

#os.DirEntry: Representa una entrada en un directorio, que se obtiene al iterar sobre un directorio usando os.scandir(). Contiene información sobre archivos y directorios, como si es un archivo o un directorio, su nombre y otras propiedades.
#with os.scandir('.') as entries: 
#    for entry in entries: 
#        print(entry.name, entry.is_file()) 

#os.PathLike: Esta clase es utilizada por objetos que representan rutas de archivo y directorios. La clase PathLike es una interfaz para objetos que pueden ser convertidos en una ruta válida. Muchos módulos como pathlib devuelven objetos que implementan esta clase.
p = Path('/home/user/documentos') 
print(isinstance(p, os.PathLike)) # True 

#os.FSPath: FSPath es una interfaz para los objetos que pueden ser utilizados como rutas del sistema de archivos. Es una clase base para objetos de rutas, como cadenas de texto o instancias de la clase pathlib.Path.
#p = Path('archivo.txt') 
#print(isinstance(p, os.FSPath)) # True 

#os._exit(status): No es exactamente una clase, esta función de bajo nivel se utiliza para finalizar proceso inmediatamente con un código de salida. No es una clase, pero vale la pena mencionarlo ya que se encuentra en el módulo os.
os._exit(0) # Finaliza el proceso con estado 0 (sin errores) 



#Variables del módulo os
#os.name: Contiene el nombre del sistema operativo. Para realizar comprobaciones entre diferentes sistemas operativos print(os.name) # 'posix', 'nt', etc. (por ejemplo, 'posix' para Linux/Mac, 'nt' para Windows).

#os.environ: Es un diccionario que contiene las variables de entorno del sistema. Puedes acceder y modificar las variables de entorno a través de esta variable.
print(os.environ) # Muestra todas las variables de entorno print(os.environ['HOME']) # Muestra el valor de la variable HOME 

#os.curdir: Esta variable representa el nombre del directorio actual, generalmente un punto (.), que es utilizado por varias funciones relacionadas con rutas.
print(os.curdir) # '.' 

#os.pardir: Representa el nombre del directorio padre, generalmente dos puntos (..). Se usa en rutas para hacer referencia al directorio superior.
print(os.pardir) # '..' 

#os.sep: Es el separador de directorios utilizado en el sistema operativo. En Windows es '\', y en Linux/macOS es '/'.
print(os.sep) # '\\' en Windows, '/' en Linux/Mac 

#os.altsep: Es un separador alternativo de directorios, que es usado en algunos sistemas
print(os.altsep) # '\\' en Windows, None en otros sistemas 

#os.linesep: Representa el carácter utilizado para separar líneas en el sistema operativo actual. 
print(os.linesep) # '\r\n' en Windows, '\n' en Linux/Mac 

#os.path: Es un submódulo dentro de os que contiene funciones útiles para trabajar con rutas de archivos, como os.path.join(), os.path.exists(), os.path.isdir(), etc.
print(os.path) # Acceso a funciones de ruta como os.path.join() 

#os.urandom(): Aunque es una función, también puede considerarse parte de las variables al usarla para generar datos aleatorios de manera segura. Se usa para obtener n bytes de datos aleatorios.
print(os.urandom(10)) # Genera 10 bytes de datos aleatorios 


#Constantes del módulo os

#os.O_RDONLY: Especifica la constante para abrir un archivo en modo solo lectura.
fd = os.open('archivo.txt', os.O_RDONLY) 

#os.O_WRONLY: Especifica la constante para abrir un archivo en modo solo escritura.
fd = os.open('archivo.txt', os.O_WRONLY) 

#os.O_RDWR: Especifica la constante para abrir un archivo en modo de lectura y escritura.
fd = os.open('archivo.txt', os.O_RDWR) 

#os.O_APPEND: Especifica la constante para abrir un archivo en modo de solo anexado (agregar al final del archivo).
fd = os.open('archivo.txt', os.O_APPEND) 

#os.O_CREAT: Especifica la constante para crear un archivo si no existe.
fd = os.open('nuevo_archivo.txt', os.O_CREAT | os.O_WRONLY) 

#os.O_EXCL: Especifica la constante para garantizar que el archivo sea creado, es decir, no puede existir previamente.
fd = os.open('archivo_unico.txt', os.O_CREAT | os.O_EXCL) 

#os.F_OK: Especifica la constante para comprobar si un archivo existe.
if os.access('archivo.txt', os.F_OK): 
    print('El archivo existe.') 

#os.R_OK: Especifica la constante para comprobar si un archivo es legible.
if os.access('archivo.txt', os.R_OK): 
    print('El archivo es legible.') 

#os.W_OK: Especifica la constante para comprobar si un archivo es escribible.
if os.access('archivo.txt', os.W_OK): 
    print('El archivo es escribible.') 

#os.X_OK: Especifica la constante para comprobar si un archivo es ejecutable.
if os.access('archivo.sh', os.X_OK): 
    print('El archivo es ejecutable.') 

#os.SEEK_SET: Especifica la constante utilizada para reposicionar el puntero de archivo desde el principio del archivo.
os.lseek(fd, 0, os.SEEK_SET) 

#os.SEEK_CUR: Especifica la constante utilizada para reposicionar el puntero de archivo desde la posición actual.
os.lseek(fd, 0, os.SEEK_CUR) 

#os.SEEK_END: Especifica la constante utilizada para reposicionar el puntero de archivo desde el final del archivo.
os.lseek(fd, 0, os.SEEK_END) 




#Submódulos del módulo os

#os.path: Proporciona funciones para manipular rutas de archivos y directorios. Tiene métodos para realizar operaciones como unir rutas, comprobar si un archivo existe, obtener el nombre del archivo, y más.
print(os.path.exists('archivo.txt')) # Verifica si el archivo existe 

#os.scandir: Es un submódulo para iterar de manera eficiente sobre directorios. Utiliza os.DirEntry para representar las entradas en un directorio, y proporciona información como si una entrada es un archivo o un directorio.
with os.scandir('.') as entries:
    for entry in entries:
        print(entry.name, entry.is_file()) 

#os.urandom: Utiliza este submódulo para generar números aleatorios de alta calidad criptográfica.
print(os.urandom(10)) # Genera 10 bytes de datos aleatorios 

#os.environ: Es una variable dentro de os, permite acceder y modificar las variables de entorno del sistema operativo.
print(os.environ['HOME']) # Accede al valor de la variable de entorno HOME 

#os.stat: Proporciona información detallada sobre un archivo o directorio, como permisos, fecha de modificación, y más.
print(os.stat('archivo.txt')) 

#os.sysctl: Presente en sistemas Unix (Linux/macOS), permite consultar y modificar parámetros núcleo sistema operativo.
print(os.sysctl('kern.hostname')) # Ejemplo de consulta del nombre de host 
