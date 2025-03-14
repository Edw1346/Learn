"""Ahora las Funciones del modulo sys Proporciona funciones y variables que permiten interactuar directamente con
el intérprete de Python y el entorno de ejecución del sistema operativo."""

"""Funciones del módulo sys"""

import sys 

#sys.argv: Una lista que contiene los argumentos de la línea de comandos que se pasaron al script de Python al ejecutarlo.
print(sys.argv) # Imprime los argumentos pasados al script 

#sys.exit([arg]): Sale del programa con un código de salida opcional. Si se proporciona un valor, este será el código de salida del proceso.
sys.exit("Error fatal") # Sale del programa y muestra el mensaje de error 

#sys.getdefaultencoding():Retorna el nombre de la codificación que utiliza Python por defecto para las cadenas de texto.
print(sys.getdefaultencoding()) # Imprime la codificación por defecto 

#sys.getfilesystemencoding(): Retorna el nombre de la codificación utilizada para la manipulación de archivos y directorios.
print(sys.getfilesystemencoding()) # Imprime la codificación del sistema de archivos 

#sys.getsizeof(object): Devuelve el tamaño en bytes de un objeto en memoria, lo que puede ser útil para medir el consumo de memoria de objetos.
x = 42
print(sys.getsizeof(x)) # Imprime el tamaño de la variable x en bytes 

#sys.maxsize: Devuelve el valor más grande que puede tener un entero en el sistema actual, lo que puede ser útil para definir límites en estructuras de datos o cálculos.
print(sys.maxsize) # Imprime el valor máximo de un entero en el sistema 

#sys.platform: Devuelve una cadena que indica el sistema operativo en el que se está ejecutando Python.
print(sys.platform) # Imprime el sistema operativo actual (por ejemplo, 'linux', 'win32', etc.) 

#sys.path: Una lista de cadenas que contiene los directorios que Python buscará para encontrar los módulos importados. Puede modificarse para añadir rutas adicionales.
sys.path.append('/ruta/adicional') # Añadir una nueva ruta para buscar módulos print(sys.path) 

#sys.stdin: Permite leer la entrada estándar (como si fuera un archivo). Se usa comúnmente con input() o en programas de línea de comandos.
data = sys.stdin.read() # Lee todo lo que se ingresa por la entrada estándar 
print(data) 

#sys.stdout: Permite redirigir la salida estándar. Se puede usar para escribir datos directamente a la consola o a un archivo.
sys.stdout.write("Hola Mundo\n") # Escribe directamente a la salida estándar 

#sys.stderr: Similar a sys.stdout, pero para escribir errores o mensajes de advertencia.
sys.stderr.write("¡Este es un error!\n") # Escribe un mensaje de error en la salida de error estándar 

#sys.version: Retorna una cadena que contiene la versión de Python que se está ejecutando.
print(sys.version) # Imprime la versión actual de Python 

#sys.getrefcount(object): Devuelve el número de referencias a un objeto. Es útil para la depuración de la gestión de memoria.
x = [] 
print(sys.getrefcount(x)) # Imprime el número de referencias al objeto x 

#sys.setrecursionlimit(limit): Establece el límite de recursión del intérprete de Python, es decir, cuántas veces puede llamarse recursivamente una función antes de que ocurra un error.
sys.setrecursionlimit(1500) # Establece un límite de recursión más alto 

#sys.api_version: Devuelve la versión de la API de Python que está en uso, lo que puede ser útil para los desarrolladores de extensiones en C o C++.
print(sys.api_version) # Imprime la versión de la API de Python 

#sys.byteorder: Devuelve una cadena que indica el orden de los bytes en el sistema. Puede ser 'little' o 'big'.
print(sys.byteorder) # Imprime el orden de los bytes ('little' o 'big') 

#sys._getframe([depth]): Devuelve el objeto frame para la pila de llamadas. Esto es útil para el rastreo de pilas y la depuración.
frame = sys._getframe(0) # Obtiene el marco de la pila actual 
print(frame.f_code.co_name) # Imprime el nombre de la función actual 

#sys.getrefcount(object): Devuelve el número de referencias al objeto. Este es un método útil para investigar el manejo de la memoria en Python y realizar depuración.
x = [] 
print(sys.getrefcount(x)) # Muestra el número de referencias al objeto x 

#sys.getsizeof(object): Devuelve el tamaño en bytes de un objeto en la memoria.
x = 'texto' 
print(sys.getsizeof(x)) # Muestra el tamaño en bytes del objeto x 

#sys.setrecursionlimit(limit): Establece el límite de recursión del intérprete de Python. Se usa para cambiar el número máximo de llamadas recursivas que un programa puede realizar.
sys.setrecursionlimit(2000) # Establece el límite de recursión a 2000 

#sys.exc_info(): Devuelve una tupla que contiene información sobre la excepción más reciente, en caso de que haya ocurrido alguna. Esto se utiliza comúnmente para manejar errores.
try:
    1 /0
except ZeroDivisionError: 
    print(sys.exc_info()) # Imprime la información sobre la excepción 

#sys.getfilesystemencoding(): Devuelve la codificación utilizada por el sistema de archivos del sistema operativo. Es útil cuando se trabaja con archivos que contienen texto en diferentes codificaciones.
print(sys.getfilesystemencoding()) # Imprime la codificación del sistema de archivos 

#sys.api_version: Devuelve la versión de la API de Python, que es útil cuando se trabaja con extensiones de C: import sys 
print(sys.api_version) # Imprime la versión de la API de Python 

#sys.byteorder: Devuelve el orden de los bytes en el sistema, que puede ser 'little' o 'big'. Esto se utiliza para comprender cómo el sistema maneja los datos binarios.
print(sys.byteorder) # Imprime 'little' o 'big', dependiendo del sistema 

#sys._getframe([depth]): Obtiene el objeto frame de la pila de llamadas de Python. Esto es útil para la depuración o la inspección de la pila de ejecución.
frame = sys._getframe(1) # Obtiene el marco de la pila que lo llamó
print(frame.f_code.co_name) # Imprime el nombre de la función que lo llamó 

#sys.setcheckinterval(interval): Establece el intervalo de comprobación de operaciones de bytecode. Este valor se usa para controlar el número de instrucciones de bytecode ejecutadas antes de que se verifique si debe ceder el control al recolector de basura.
sys.setcheckinterval(10) # Establece el intervalo de verificación de operaciones 

#sys.getallocatedblocks(): Devuelve el número total de bloques de memoria asignados por el administrador de memoria de Python. Es útil para inspeccionar el uso de la memoria.
print(sys.getallocatedblocks()) # Imprime el número de bloques de memoria asignados 

#sys.getwindowsversion(): En sistemas Windows, devuelve una tupla que contiene la versión de Windows.
print(sys.getwindowsversion()) # Imprime la versión de Windows 

#sys.setdlopenflags(flags): Establece los valores de los flags para la carga dinámica de bibliotecas en sistemas Unix.
sys.setdlopenflags(0x100) # Establece los flags de carga dinámica 

#sys._clear_type_cache(): Borra el caché de tipos internos en Python. Es útil cuando se realizan manipulaciones avanzadas de tipos.
sys._clear_type_cache() # Borra el caché de tipos internos 



"""Clases del módulo sys"""

#sys.stdout: Aunque sys.stdout no es una clase directamente definida en sys, se comporta como un objeto que representa la salida estándar de datos. Es un archivo de texto que recibe lo que se escribe en la consola. Se puede redirigir para capturar la salida de la aplicación y escribirla en un archivo o manejarla de otra manera. Ejemplo de uso:
sys.stdout.write("Este es un mensaje en la salida estándar.\n") 

#sys.stderr: Similar a sys.stdout, sys.stderr es un objeto de archivo que se utiliza para la salida de errores. Es el flujo de salida estándar para los mensajes de error, y se puede redirigir de manera similar a sys.stdout. Ejemplo de uso:
sys.stderr.write("Este es un mensaje de error.\n") 

#sys.stdin: También es un objeto de archivo, pero está asociado con la entrada estándar. Se usa para leer datos desde la entrada estándar del sistema (teclado por defecto). Al igual que stdout y stderr, se puede redirigir para leer de fuentes diferentes (como archivos o pipes). Ejemplo de uso:
input_data = sys.stdin.read() # Lee todo lo que se ingresa por la entrada estándar 
print("Entrada leída:", input_data) 

#sys.exc_info(): Aunque sys.exc_info() devuelve una tupla y no una clase propiamente dicha, se utiliza para obtener información sobre las excepciones que están ocurriendo. Esta información se devuelve como una tupla que contiene el tipo de excepción, el valor de la excepción y el traceback. Ejemplo de uso:
try:
    1 / 0
except ZeroDivisionError: 
    print(sys.exc_info()) # Imprime la tupla con la información sobre la excepción 




"""Variables del módulo sys"""

#sys.argv: Una lista de los argumentos de la línea de comandos que se pasaron al script de Python al ejecutarlo Ejemplo:
print(sys.argv) # Muestra los argumentos de la línea de comandos 

#sys.version: Una cadena que contiene la versión actual de Python. Ejemplo:
print(sys.version) # Imprime la versión de Python actual 


#sys.platform: Una cadena que indica el sistema operativo en el que se ejecuta Python (por ejemplo, 'linux', 'win32', 'darwin'). Ejemplo:
print(sys.platform) # Imprime el sistema operativo actual 

#sys.maxsize: El valor más grande que puede tener un entero en el sistema actual. Útil para trabajar con límites en algoritmos que manejan enteros grandes. Ejemplo:
print(sys.maxsize) # Muestra el tamaño máximo de un entero en el sistema 

#sys.path: Una lista de cadenas que especifican los directorios donde Python busca los módulos. Se puede modificar para agregar rutas personalizadas de búsqueda de módulos. Ejemplo:
sys.path.append('/mi/ruta/personalizada') # Agrega una nueva ruta de búsqueda 
print(sys.path) # Muestra las rutas de búsqueda de módulos 

#sys.exc_info(): Devuelve una tupla que contiene información sobre la excepción que ocurrió más recientemente, si la hubiera. Ejemplo:
try:
    1 / 0
except ZeroDivisionError:
    print(sys.exc_info()) # Imprime la información sobre la excepción capturada 

#sys.getrefcount(object): Devuelve el número de referencias al objeto en memoria. Esta es una medida útil para el manejo de memoria en Python. Ejemplo:
x = [] 
print(sys.getrefcount(x)) # Muestra el número de referencias al objeto x 

#sys.getsizeof(object): Retorna el tamaño en bytes de un objeto en memoria. Es útil para medir el consumo de memoria de los objetos. Ejemplo:
x = 'Hola Mundo' 
print(sys.getsizeof(x)) # Muestra el tamaño en bytes del objeto x 

#sys.stdin: El flujo de entrada estándar, que permite leer los datos de la entrada estándar (por lo general, el teclado). Se puede redirigir para leer desde un archivo o una fuente externa. Ejemplo:
input_data = sys.stdin.read() # Lee todo lo que se ingresa por la entrada estándar 
print("Entrada leída:", input_data) 

#sys.stdout: El flujo de salida estándar, utilizado para imprimir datos en la consola. También puede redirigirse para 
#escribir en archivos o en otros destinos. Ejemplo:
sys.stdout.write("Esto es un mensaje en la salida estándar.\n") 

#sys.stderr: El flujo de salida de error estándar, donde se escriben los mensajes de error. Al igual que stdout, se puede redirigir a archivos o a otros destinos. Ejemplo:
sys.stderr.write("Este es un mensaje de error.\n") 

#sys.version_info: Una tupla que contiene la versión de Python como números (principal, menor, micro). Esta variable se usa comúnmente para hacer verificaciones de compatibilidad entre versiones de Python. Ejemplo:
print(sys.version_info) # Muestra la versión de Python como tupla (principal, menor, micro) 

#sys.byteorder: Devuelve una cadena que indica el orden de bytes del sistema. Puede ser 'little' o 'big', dependiendo de la arquitectura de la máquina. Ejemplo:
print(sys.byteorder) # Imprime 'little' o 'big', dependiendo del sistema 

#sys.api_version: Devuelve la versión de la API de Python, útil principalmente para los desarrolladores de extensiones en C. Ejemplo:
print(sys.api_version) # Muestra la versión de la API de Python 

#sys.getdefaultencoding(): Devuelve el nombre de la codificación utilizada por defecto para las cadenas de texto en Python. Ejemplo:
print(sys.getdefaultencoding()) # Muestra la codificación por defecto utilizada por Python 





"""Constantes del módulo sys"""
sys.argv
#Aunque sys.argv es una lista, es comúnmente referenciada como una constante porque contiene los argumentos de la línea de comandos y no suele cambiar durante la ejecución del programa.

sys.version_info
#Una constante que contiene la versión de Python en forma de tupla (principal, menor, micro). No es algo que cambie, por lo tanto, se puede tratar como una constante.

sys.executable
#Contiene la ruta completa del ejecutable de Python que se está utilizando para ejecutar el script. Es una constante porque generalmente no cambia durante la ejecución.

sys.maxsize
#Esta constante indica el valor más grande que puede tener un entero en el sistema. Es útil para determinar los límites de tamaño de datos y la arquitectura del sistema.

sys.path
#Es una lista que contiene las rutas en las que Python busca los módulos, pero es esencialmente constante en el contexto de la ejecución del programa, aunque puede modificarse explícitamente durante la ejecución.

sys.platform
#Es una constante que contiene el nombre del sistema operativo en el que se ejecuta Python (como 'linux', 'win32', 'darwin', etc.).

sys.maxunicode
#Define el valor más grande que puede tener un código Unicode en el sistema. Esta constante puede ser útil cuando se trabaja con caracteres Unicode y se necesita saber el límite.

sys.setcheckinterval()
#Aunque sys.setcheckinterval() se usa para establecer el intervalo de verificación, su valor por defecto es considerado una constante si no se cambia durante la ejecución.
sys.flags
#Es un conjunto de constantes que contienen los valores de las banderas de ejecución de Python, como si el intérprete se ejecuta en modo optimizado o con el modo de depuración habilitado.




"""Excepciones del módulo sys"""

#sys.exit() no es exactamente una excepción en sí misma, pero se utiliza para salir del programa de manera controlada. Lanza una excepción de tipo SystemExit que puede ser capturada si es necesario. Ejemplo:
sys.exit("Fin del programa") # Lanza una excepción SystemExit con un mensaje 

#SystemExit: Esta es la excepción que se lanza cuando se llama a sys.exit(). Generalmente, esta excepción no se captura a menos que se quiera realizar una acción antes de terminar el programa.
#sys.exc_info() no lanza una excepción directamente, pero devuelve una tupla que contiene información sobre la última excepción ocurrida en el programa, lo cual puede ser útil en el manejo de excepciones. Ejemplo:
try: 
    1 / 0 
except ZeroDivisionError: 
    print(sys.exc_info()) # Muestra la información sobre la excepción ocurrida 

#sys.setrecursionlimit(): Aunque no lanza una excepción directamente, sys.setrecursionlimit() se puede usar para establecer el límite de recursión. Si el límite se excede, Python lanzará una excepción RecursionError. Ejemplo:
sys.setrecursionlimit(50) 
try: 
    def recursive(): 
        recursive() 
    
    recursive() 
except RecursionError: 
    print("Límite de recursión excedido.") 

#sys.stderr: Al igual que sys.stdout, sys.stderr es un objeto de archivo donde se pueden escribir errores. No lanza excepciones directamente, pero se utiliza para redirigir los errores de la aplicación. Ejemplo:
sys.stderr.write("Esto es un mensaje de error.\n") 

#sys.getrecursionlimit(): Aunque esta función solo devuelve el valor del límite de recursión, si se cambia el límite con sys.setrecursionlimit(), y el programa excede ese límite, se lanzará una RecursionError. Ejemplo:
print(sys.getrecursionlimit()) # Devuelve el límite de recursión 




"""Excepción relacionada con el sistema"""

#RecursionError: Esta es una excepción que se lanza cuando se excede el límite de recursión, que se puede establecer o consultar con sys.setrecursionlimit() y sys.getrecursionlimit() respectivamente. Ejemplo:
sys.setrecursionlimit(10) 
try: 
    def recurse(): 
        return recurse() 
    
    recurse() 
except RecursionError: 
    print("Se ha alcanzado el límite de recursión.") 


"""Submódulos relacionados con sys"""

#sysconfig: Este módulo proporciona acceso a configuraciones específicas de la instalación de Python y su entorno, como las rutas de búsqueda de los módulos, las configuraciones de compilación, etc. Ejemplo:
import sysconfig 
print(sysconfig.get_paths()) # Muestra las rutas de instalación del sistema Python 

#platform: Aunque no es un submódulo directo de sys, el módulo platform está muy relacionado con él. Permite obtener información sobre la plataforma del sistema operativo en el que se ejecuta Python. A menudo se utiliza junto con sys.platform para obtener detalles más específicos. Ejemplo:
import platform 
print(platform.system()) # Devuelve el nombre del sistema operativo, similar a sys.platform 

#os: Similar a platform, el módulo os también interactúa con el sistema operativo y puede ofrecer 
#funcionalidades complementarias a las que ofrece sys, como la gestión de archivos, directorios y variables de entorno. Ejemplo:
import os
print(os.name) # Imprime el nombre del sistema operativo ('posix', 'nt', etc.) 

#site: Este módulo se utiliza para configurar el entorno de Python, incluyendo la configuración de rutas de búsqueda de módulos y otros ajustes específicos de la instalación. Funciona junto con sys.path. Ejemplo:
import site 
print(site.getsitepackages()) # Muestra las rutas donde están instalados los paquetes