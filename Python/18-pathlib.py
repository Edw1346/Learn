import pathlib

"""El módulo pathlib proporciona una forma orientada a objetos de trabajar con rutas de archivos y directorios en Python. 
Permite manejar rutas de manera más sencilla y más legible que utilizando cadenas de texto tradicionales. Utiliza objetos 
Path para representar las rutas y realizar operaciones sobre ellas."""
#Características principales de pathlib:
#Rutas de archivo: Permite crear y manipular rutas de archivos y directorios de forma simple y eficiente.
#Métodos útiles: Puedes realizar operaciones como comprobar si una ruta existe, obtener el nombre de un archivo, crear directorios, etc.
#Compatible con todos los sistemas operativos: Funciona bien en Windows, Linux y macOS. Ejemplo básico:
from pathlib import Path # Crear un objeto Path 
p = Path('/home/usuario/documentos') # Verificar si la ruta existe 
print(p.exists()) # Imprime True o False dependiendo si la ruta existe 

# Obtener el nombre del archivo 
archivo = p / 'archivo.txt' # Concatenar para crear una nueva ruta 
print(archivo.name) # Imprime 'archivo.txt' # Crear un directorio 
directorio = p / 'nuevo_directorio' 
directorio.mkdir(parents=True, exist_ok=True) # Crea el directorio si no existe 



"""Ahora todas, todas las Funciones del modulo pathlib"""

#Métodos de la clase Path:
#Path.cwd(): Devuelve el directorio de trabajo actual (el directorio donde se ejecuta el programa). Ejemplo: 
from pathlib import Path 
print(Path.cwd()) # Imprime el directorio de trabajo actual 

#Path.home(): Devuelve el directorio home del usuario. Ejemplo: 
from pathlib import Path 
print(Path.home()) # Imprime el directorio home del usuario 

#Path.exists(): Devuelve True si la ruta existe en el sistema de archivos. Ejemplo:
p = Path('archivo.txt') 
print(p.exists()) # Imprime True si el archivo existe 

#Path.is_dir(): Devuelve True si la ruta es un directorio. Ejemplo:
p = Path('/ruta/al/directorio') 
print(p.is_dir()) # Imprime True si es un directorio 

#Path.is_file(): Devuelve True si la ruta es un archivo. Ejemplo:
p = Path('archivo.txt') 
print(p.is_file()) # Imprime True si es un archivo 

#Path.is_symlink(): Devuelve True si la ruta es un enlace simbólico. Ejemplo: 
p = Path('/ruta/a/symlink') 
print(p.is_symlink()) # Imprime True si es un enlace simbólico 

#Path.rename(): Renombra el archivo o directorio en la ruta. Ejemplo: 
p = Path('archivo.txt')
p.rename('nuevo_nombre.txt') # Renombra el archivo 

#Path.unlink(): Elimina el archivo en la ruta. Ejemplo: 
p = Path('archivo.txt')
p.unlink() # Elimina el archivo 

#Path.mkdir(): Crea un directorio en la ruta. Ejemplo: 

p = Path('nuevo_directorio') 
p.mkdir() # Crea el directorio 

#Path.rmdir(): Elimina el directorio vacío en la ruta. Ejemplo: 
p = Path('directorio_vacio')
p.rmdir() # Elimina el directorio vacío 

#Path.chmod(): Cambia los permisos del archivo o directorio en la ruta. Ejemplo:
p = Path('archivo.txt') 
p.chmod(0o777) # Cambia los permisos del archivo 

#Path.touch(): Crea un archivo vacío en la ruta si no existe, o actualiza la fecha de modificación si el archivo ya existe. Ejemplo:
p = Path('nuevo_archivo.txt') 
p.touch() # Crea o actualiza el archivo 

#Path.glob(): Devuelve un generador de todos los archivos y directorios que coinciden con un patrón específico. Ejemplo: 
p = Path('.') 
for archivo in p.glob('*.txt'): 
    print(archivo) # Imprime todos los archivos .txt en el directorio 

#Path.rglob(): Similar a glob(), pero realiza una búsqueda recursiva en subdirectorios. Ejemplo: 
p = Path('.') 
for archivo in p.rglob('*.txt'): 
    print(archivo) # Imprime todos los archivos .txt en el directorio y subdirectorios 

#Path.read_text(): Lee el contenido de un archivo de texto. Ejemplo: 
p = Path('archivo.txt') 
contenido = p.read_text() 
print(contenido) # Imprime el contenido del archivo 

#Path.write_text(): Escribe texto en un archivo. Ejemplo: 
p = Path('archivo.txt') 
p.write_text('Hola, Mundo!') # Escribe "Hola, Mundo!" en el archivo 

#Path.read_bytes(): Lee el contenido de un archivo como bytes. Ejemplo:
p = Path('archivo.bin') 
contenido = p.read_bytes() 
print(contenido) # Imprime el contenido en bytes del archivo 

#Path.write_bytes(): Escribe bytes en un archivo. Ejemplo: 
p = Path('archivo.bin') 
p.write_bytes(b'Hola en bytes') # Escribe datos en bytes en el archivo 

#Path.relative_to(): Devuelve la ruta relativa de un archivo o directorio respecto a otro. Ejemplo: 
p = Path('/home/usuario/proyecto/archivo.txt') 
print(p.relative_to('/home/usuario')) # Imprime 'proyecto/archivo.txt' 

#Path.resolve(): Devuelve la ruta absoluta, resolviendo enlaces simbólicos. Ejemplo: 
p = Path('archivo.txt') 
print(p.resolve()) # Imprime la ruta absoluta 

#Path.stem():Devuelve el nombre del archivo sin su extensión. Ejemplo: 
p = Path('archivo.txt') 
print(p.stem) # Imprime 'archivo' 

#Path.suffix(): Devuelve la extensión del archivo. Ejemplo: 
p = Path('archivo.txt') 
print(p.suffix) # Imprime '.txt' 




"""Clases principales del módulo pathlib:"""

#Path: La clase principal para trabajar con rutas de archivos y directorios de manera concreta. Hereda de PurePath y agrega métodos que permiten interactuar con el sistema de archivos (como leer y escribir archivos, crear directorios, etc.). Ejemplo:
from pathlib import Path 
p = Path('archivo.txt') 
print(p.exists()) # Verifica si el archivo existe 

#PurePath: Es una clase base para representar rutas de manera abstracta, sin realizar operaciones relacionadas con el sistema de archivos. Es útil para manipular rutas sin depender del sistema operativo, pero no permite acceder al sistema de archivos. Ejemplo:
from pathlib import PurePath
 p = PurePath('carpeta') / 'archivo.txt'
 print(p) # Imprime 'carpeta/archivo.txt' 


#Subclases de PurePath:
#PurePosixPath: Subclase de PurePath que representa una ruta en un sistema de archivos tipo POSIX (como Linux o macOS). Ejemplo:
from pathlib import PurePosixPath 
p = PurePosixPath('/home/usuario/archivo.txt') 
print(p) # Imprime '/home/usuario/archivo.txt' 

#PureWindowsPath: Subclase de PurePath que representa una ruta en un sistema de archivos tipo Windows (con letras de unidad y barras invertidas). Ejemplo:
from pathlib import PureWindowsPath 
p = PureWindowsPath('C:\\Users\\Usuario\\archivo.txt') 
print(p) # Imprime 'C:\\Users\\Usuario\\archivo.txt' 

#Subclases de Path:
#PosixPath:Subclase de Path para sistemas tipo POSIX (como Linux o macOS). Permite realizar operaciones reales sobre rutas y archivos en sistemas POSIX. Ejemplo:
from pathlib import PosixPath
 p = PosixPath('/home/usuario/archivo.txt') 
print(p.exists()) # Verifica si el archivo existe en un sistema POSIX 

#WindowsPath: Subclase de Path para sistemas Windows. Permite trabajar con rutas y archivos en sistemas Windows. Ejemplo:
from pathlib import WindowsPath 
p = WindowsPath('C:\\Users\\Usuario\\archivo.txt') 
print(p.exists()) # Verifica si el archivo existe en un sistema Windows 

#Path es la clase principal para trabajar con rutas y archivos, con métodos para interactuar con el sistema de archivos.
#PurePath es para manipular rutas de manera abstracta, sin interacción con el sistema de archivos.
#PurePosixPath y PureWindowsPath son subclases de PurePath para representar rutas en sistemas POSIX o Windows, respectivamente.
#PosixPath y WindowsPath son subclases de Path que permiten operar con rutas y archivos en sistemas POSIX o Windows.



"""Variables relevantes dentro del módulo pathlib:"""

#Path.cwd(): Esta es una función que devuelve la ruta del directorio de trabajo actual. Aunque no es una variable per se, se utiliza para obtener la variable de entorno que representa el directorio donde se está ejecutando el programa. Ejemplo:
from pathlib import Path 
print(Path.cwd()) # Imprime el directorio de trabajo actual 

#Path.home(): Esta es otra función que devuelve la ruta del directorio home del usuario, es decir, la carpeta principal del usuario donde suelen almacenarse sus archivos. Ejemplo: 
from pathlib import Path 
print(Path.home()) # Imprime el directorio home del usuario 

#Path: Aunque Path no es una "variable" en el sentido clásico, es la clase principal del módulo pathlib. Puedes pensar en ella como una "variable" importante dentro del módulo, ya que te permite crear objetos de tipo Path que representan rutas de archivos. Ejemplo: 
from pathlib import Path 
p = Path('documentos') # Crear un objeto de tipo Path 

#PurePath: Similar a Path, PurePath es una clase base de la que heredan otras clases como PurePosixPath y PureWindowsPath. De nuevo, no es una variable directamente accesible, pero es una clase clave en la que se basan otras funcionalidades. Ejemplo: 
from pathlib import PurePath 
p = PurePath('carpeta/archivo.txt') # Crear una ruta sin acceso al sistema de archivos 



"""Algunos valores constantes relevantes en pathlib:"""

#PurePath.PATH_SEPARATOR: Es una constante que representa el separador de rutas utilizado en el sistema operativo. En sistemas POSIX (como Linux y macOS) es '/', mientras que en sistemas Windows es '\\'. Ejemplo: 
from pathlib import PurePath 
print(PurePath.PATH_SEPARATOR) # '/' en sistemas POSIX y '\\' en Windows 

#PurePath.PURE_PATH: Esta constante se refiere a la clase base de PurePath, pero no se utiliza directamente en código como una constante. Más bien, su valor y rol son implícitos en el comportamiento del módulo.

#Observación sobre el módulo: Pathlib está más orientado a clases, métodos y propiedades en lugar de tener constantes definidas explícitamente. Sin embargo, el comportamiento de las rutas es dinámico y está basado en el sistema operativo en el que se ejecuta el código. Esto implica que, aunque no hay "constantes" claras como tal, las funciones como Path.cwd() o Path.home() son accesos a valores que se comportan de manera constante, dependiendo del entorno.



"""Excepciones comunes en pathlib:"""

#FileNotFoundError: Esta excepción se lanza cuando intentas acceder a un archivo o directorio que no existe. Ejemplo: 
from pathlib import Path
try: 
    p = Path('archivo_que_no_existe.txt')
    p.read_text()
except FileNotFoundError: 
    print("El archivo no se encontró.") 

#IsADirectoryError: Se lanza cuando se intenta abrir un directorio como si fuera un archivo. Ejemplo: 
from pathlib import Path 
try: 
    p = Path('directorio') 
    p.read_text() # Esto causará un error si 'directorio' es un directorio y no un archivo 
except IsADirectoryError:
    print("No se puede leer un directorio como archivo.") 

#PermissionError: Esta excepción se lanza cuando no tienes los permisos necesarios para realizar una operación en un archivo o directorio. Ejemplo:
from pathlib import Path 
try: 
    p = Path('archivo_sin_permisos.txt') 
    p.write_text('Texto nuevo') # Si no tienes permiso para escribir, esto lanzará un PermissionError 
except PermissionError: 
    print("No tienes permisos para escribir en este archivo.") 

OSError: Puede ser lanzada en casos más generales relacionados con el sistema de archivos, como un problema con la ruta o el sistema operativo. Ejemplo: 
from pathlib import Path 
try: 
    p = Path('/ruta/incorrecta/archivo.txt') 
    p.rename('/otra/ruta/nueva.txt') # Si la ruta no es válida, podría lanzar un OSError 
except OSError as e: 
    print(f"Ocurrió un error del sistema de archivos: {e}") 




"""El módulo pathlib no tiene submódulos internos. Es un módulo principal que proporciona clases y funciones para trabajar 
con rutas de archivos y directorios de manera orientada a objetos. Aunque se puede dividir en subclases como PurePath, 
Path, PurePosixPath, PureWindowsPath, etc., no existen submódulos como en otros módulos de Python."""
