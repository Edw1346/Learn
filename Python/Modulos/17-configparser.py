import configparse

"""El módulo configparser de Python permite trabajar con archivos de configuración, que suelen tener un formato similar al 
.ini. Estos archivos contienen secciones con pares clave-valor, lo que facilita almacenar configuraciones de manera sencilla y estructurada."""



"""Funciones del módulo configparser:"""

#ConfigParser.read(filename, encoding=None). Lee un archivo de configuración y carga sus secciones y opciones. Ejemplo: 
config.read('config.ini') 

#ConfigParser.read_file(fp, encoding=None). Lee un archivo de configuración desde un objeto de archivo (puede ser un archivo abierto). Ejemplo:
with open('config.ini', 'r') as f: 
    config.read_file(f) 

#ConfigParser.read_string(string). Lee la configuración a partir de una cadena de texto. Ejemplo: 
config.read_string("[sección]\nclave=valor") 

#ConfigParser.write(fp). Escribe la configuración en un archivo. Ejemplo: 
with open('config.ini', 'w') as f: 
    config.write(f) 

#ConfigParser.add_section(section). Añade una nueva sección al archivo de configuración. Ejemplo: 
config.add_section('NuevaSección') 

#ConfigParser.remove_section(section). Elimina una sección existente. Ejemplo: 
config.remove_section('SecciónAEliminar') 

#ConfigParser.has_section(section). Verifica si una sección existe en el archivo de configuración. Ejemplo:
if config.has_section('Sección'): 
    print("La sección existe.") 

#ConfigParser.options(section). Obtiene una lista de las opciones (claves) de una sección. Ejemplo: 
opciones = config.options('Sección') 

#ConfigParser.items(section). Devuelve una lista de tuplas (clave, valor) de todas las opciones de una sección. Ejemplo: 
items = config.items('Sección') 

#ConfigParser.keys(section). Devuelve una lista con las claves (opciones) de una sección. Ejemplo:
claves = config.keys('Sección') 

#ConfigParser.get(section, option, raw=False, vars=None). Obtiene el valor de una opción dentro de una sección. Ejemplo: 
valor = config.get('Sección', 'opción') 

#ConfigParser.getint(section, option, raw=False, vars=None). Obtiene el valor de una opción como un entero. Ejemplo: 
edad = config.getint('Sección', 'edad') 

#ConfigParser.getfloat(section, option, raw=False, vars=None). Obtiene el valor de una opción como un número flotante. Ejemplo: 
salario = config.getfloat('Sección', 'salario') 

#ConfigParser.getboolean(section, option, raw=False, vars=None). Obtiene el valor de una opción como un valor booleano. Ejemplo: 
es_admin = config.getboolean('Sección', 'admin') 

#ConfigParser.set(section, option, value). Modifica el valor de una opción dentro de una sección. Ejemplo: 
config.set('Sección', 'opción', 'nuevo valor') 

#ConfigParser.remove_option(section, option). Elimina una opción de una sección. Ejemplo: 
config.remove_option('Sección', 'opción') 

#ConfigParser.has_option(section, option). Verifica si una opción existe dentro de una sección. Ejemplo: 
if config.has_option('Sección', 'opción'): 
    print("La opción existe.") 

#ConfigParser.read_dict(dictionary). Lee una configuración a partir de un diccionario. Ejemplo:
config.read_dict({'Sección': {'clave': 'valor'}}) 

#ConfigParser.update(). Actualiza la configuración con valores de otro objeto ConfigParser. Ejemplo: 
config.update(other_config) 

#ConfigParser.clear(). Elimina todas las secciones y opciones de la configuración. Ejemplo: 
config.clear() 




"""Clases del módulo configparser:"""

#ConfigParser: Es la clase principal del módulo y proporciona las funciones para leer, escribir y modificar archivos de configuración. Puedes usarla para manejar secciones, opciones y sus valores en archivos de configuración.
#Métodos más utilizados de ConfigParser:
#read(): Lee un archivo de configuración.
#write(): Escribe la configuración a un archivo.
#add_section(): Añade una nueva sección.
#get(): Obtiene el valor de una opción dentro de una sección.
#set(): Establece el valor de una opción.
#remove_option(): Elimina una opción de una sección. Ejemplo:
config = configparser.ConfigParser() 
config.read('config.ini') 
print(config.get('Sección', 'opción')) 

#SafeConfigParser: Es una subclase de ConfigParser que proporciona una interfaz más segura para acceder a los valores de las opciones. Esta clase trata de evitar que se devuelvan valores None si no existe la opción o la sección solicitada. Nota: En versiones recientes de Python, SafeConfigParser ha sido renombrado a ConfigParser en Python 3.x, por lo que es común usar solo ConfigParser. Ejemplo:
config = configparser.SafeConfigParser() 
config.read('config.ini') 
print(config.get('Sección', 'opción')) 




"""El módulo configparser no tiene variables globales específicas definidas, pero algunas de las configuraciones que se 
pueden utilizar dentro de una instancia de ConfigParser son propiedades que puedes configurar. Estas propiedades no son 
variables globales del módulo, pero son configuraciones o ajustes que puedes modificar dentro de un objeto de la clase ConfigParser."""

#Propiedades de ConfigParser (que pueden funcionar como variables dentro de la instancia):

#ConfigParser._DEFAULT_ENCODING: Especifica el tipo de codificación que se usará al leer o escribir archivos. Generalmente, se utiliza 'utf-8' como valor por defecto. Ejemplo: 
config = configparser.ConfigParser()
print(config._DEFAULT_ENCODING) # Imprime 'utf-8' 

#ConfigParser.optionxform: Es una función que se usa para transformar el nombre de las opciones al acceder a ellas. Por defecto, convierte todas las opciones en minúsculas. Ejemplo: 
config = configparser.ConfigParser() 
print(config.optionxform('MI_OPCION')) # Imprime 'mi_opcion' 

#ConfigParser._interpolation: Define la forma en que las variables de las opciones se interpolan dentro de los archivos de configuración. Ejemplo: 
config = configparser.ConfigParser() print(config._interpolation) # Controla la interpolación, por defecto es 'BasicInterpolation' 

"""Notas: No existen muchas "variables" globales dentro de configparser, sino más bien propiedades de configuración dentro 
de una instancia de la clase ConfigParser. Las variables dentro de la clase ConfigParser generalmente están relacionadas 
con el manejo de la configuración del archivo, como la sección predeterminada, el tipo de codificación y la transformación 
de las opciones."""




"""El módulo configparser no tiene constantes definidas explícitamente como parte de su API, pero tiene algunas configuraciones 
predeterminadas que podrían considerarse "constantes" en el sentido de que sus valores son fijos y no cambian durante la ejecución."""

#"Constantes" en configparser:

#DEFAULTSECT: Es la constante que representa el nombre de la sección predeterminada dentro de un archivo de configuración. Su valor es 'DEFAULT' y se utiliza cuando no se especifica una sección para una opción en el archivo de configuración. Ejemplo: 
config = configparser.ConfigParser() 
print(config.DEFAULTSECT) # Imprime 'DEFAULT' 

#BASIC_INTERPOLATION: Es un valor de interpolación predeterminado, que permite que las opciones de configuración sean sustituidas por otras opciones dentro del mismo archivo de configuración. Ejemplo:
config = configparser.ConfigParser(interpolation=configparser.BasicInterpolation()) 

#NO_INTERPOLATION: Es una opción que se utiliza para indicar que no debe hacerse interpolación en las opciones. Si se pasa este valor, las variables de configuración no serán sustituidas por otras. Ejemplo: 
config = configparser.ConfigParser(interpolation=configparser.NoInterpolation()) 

#STRICT: Es una constante que se refiere al modo estricto de interpolación. Si se usa, generará un error si alguna de las opciones de interpolación no está definida. Ejemplo: 
config = configparser.ConfigParser(interpolation=configparser.STRICT) 

#DEFAULT: Representa una sección especial que se utiliza como un conjunto predeterminado de valores para otras secciones en el archivo de configuración. Ejemplo:
config = configparser.ConfigParser() 
config.read('config.ini') 



"""El módulo configparser tiene varias excepciones que se utilizan para manejar errores relacionados con la lectura, escritura 
y manipulación de archivos de configuración. Estas excepciones son específicas del módulo y están relacionadas principalmente 
con problemas de sintaxis o configuración."""

#Excepciones del módulo configparser:

#configparser.Error: Es la excepción base para todas las excepciones relacionadas con configparser. Se utiliza como clase base para las demás excepciones dentro del módulo. Ejemplo: 
try: 
    config = configparser.ConfigParser()
    config.read('config_no_existe.ini')
except configparser.Error as e: 
    print(f"Ocurrió un error de configuración: {e}") 

#configparser.NoSectionError: Se lanza cuando se intenta acceder a una sección que no existe en el archivo de configuración. Ejemplo: 
config = configparser.ConfigParser() 
config.read('config.ini')
try: 
    config.get('SecciónNoExistente', 'opción') 
except configparser.NoSectionError as e: 
    print(f"Sección no encontrada: {e}") 

#configparser.NoOptionError: Se lanza cuando se intenta acceder a una opción que no existe en una sección determinada. Ejemplo: 
config = configparser.ConfigParser()
config.read('config.ini')
try: 
    config.get('Sección', 'OpciónNoExistente') 
except configparser.NoOptionError as e: 
    print(f"Opción no encontrada: {e}") 

#configparser.DuplicateSectionError: Se lanza cuando se intenta agregar una sección que ya existe en el archivo de configuración. Ejemplo: 
config = configparser.ConfigParser() 
config.read('config.ini')
try: 
    config.add_section('SecciónExistente') 
except configparser.DuplicateSectionError as e:
    print(f"Sección duplicada: {e}") 

#configparser.DuplicateOptionError: Se lanza cuando se intenta agregar una opción que ya existe dentro de una sección. Ejemplo:
config = configparser.ConfigParser() 
config.read('config.ini') 
try: 
    config.set('Sección', 'opciónExistente', 'nuevoValor') 
except configparser.DuplicateOptionError as e: 
    print(f"Opción duplicada: {e}") 

#configparser.ParsingError: Se lanza cuando se detecta un error de sintaxis mientras se analiza un archivo de configuración. Ejemplo: 
config = configparser.ConfigParser() 
try: 
    config.read_string("[sección]\nclave = valor\n[sección2] clave2 = valor2") 
except configparser.ParsingError as e: 
    print(f"Error al analizar el archivo: {e}") 




"""Ahora las submodulo del modulo configparser"""

"""El módulo configparser no tiene submódulos dentro de él. Sin embargo, el módulo proporciona algunas funcionalidades 
adicionales que pueden ser configuradas a través de las opciones de interpolación y el comportamiento de lectura/escritura 
de archivos de configuración."""

#Componentes relacionados con configparser (sin ser submódulos):

#Interpolación: configparser permite configurar el comportamiento de interpolación (la sustitución de valores dentro de una cadena de texto). La interpolación se puede personalizar con diferentes clases, pero no son submódulos por sí mismos. Estas clases se encuentran directamente dentro del módulo configparser.
#Tipos de interpolación: BasicInterpolation: Realiza interpolación básica, donde los valores de las opciones se pueden sustituir por otras opciones dentro del archivo de configuración.
#ExtendedInterpolation: Permite interpolación avanzada con soporte para referencias más complejas.
#NoInterpolation: Desactiva la interpolación, es decir, no se hacen sustituciones de valores. Ejemplo:
config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation()) 
config.read('config.ini') 

#ConfigParser y SafeConfigParser: Estas son las clases principales dentro del módulo configparser. Aunque SafeConfigParser era una subclase de ConfigParser en versiones anteriores, en las versiones modernas de Python, SafeConfigParser ha sido renombrada como ConfigParser, por lo que ahora ambas clases son prácticamente iguales.
#DEFAULTSECT y otros atributos: Algunas configuraciones y constantes como DEFAULTSECT definen el comportamiento por defecto del módulo. Estos no son submódulos, pero son importantes para manejar cómo funcionan las secciones y las opciones dentro del archivo de configuración.
