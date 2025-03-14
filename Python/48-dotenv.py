import dotenv

"""El módulo dotenv en Python se utiliza para cargar variables de entorno desde un archivo .env en el sistema. Esto es útil 
cuando necesitas almacenar configuraciones sensibles, como claves API o credenciales, de manera segura y fuera del código fuente."
"El archivo .env contiene pares clave-valor, y el módulo dotenv carga esas variables en el entorno de ejecución de Python para que puedas acceder a ellas con os.getenv() o os.environ"""


"""Funciones útiles para manejar archivos .env""" 

#1. load_dotenv()
#Carga las variables de entorno desde un archivo .env en el entorno de ejecución de Python. Uso: Se usa generalmente al inicio del código para asegurar que las variables de entorno estén disponibles. Sintaxis:
from dotenv import load_dotenv 
load_dotenv() # Carga el archivo .env por defecto 

#Parámetros: dotenv_path (opcional): El camino al archivo .env. Si no se proporciona, busca un archivo .env en el directorio actual.
#override (opcional): Booleano que indica si las variables ya definidas en el entorno deben ser sobrescritas. Por defecto, es False.
#verbose (opcional): Booleano que activa los mensajes detallados durante el proceso de carga del archivo .env. Ejemplo:
from dotenv import load_dotenv 
import os 
load_dotenv() # Carga el archivo .env automáticamente 
api_key = os.getenv("API_KEY") 
print(api_key) 

#2. dotenv_values()
#Devuelve un diccionario con las variables definidas en el archivo .env sin modificar el entorno de ejecución. Uso: Es útil cuando solo necesitas acceder a las variables del archivo .env pero no deseas que se agreguen al entorno global de Python. Sintaxis:
from dotenv import dotenv_values 
config = dotenv_values() # Devuelve las variables del .env como un diccionario 

#Parámetros: dotenv_path (opcional): El camino al archivo .env. Si no se proporciona, busca un archivo .env en el directorio actual. Ejemplo:
from dotenv import dotenv_values 
config = dotenv_values(".env") # Cargar variables desde el archivo .env 
print(config["API_KEY"]) 

#3. set_key()
#Modifica o agrega una clave en el archivo .env. Uso: Esta función permite modificar un archivo .env directamente, agregando o actualizando una variable de entorno. Sintaxis:
from dotenv import set_key 
set_key(dotenv_path, key_to_set, value_to_set) 

#Parámetros: dotenv_path: El camino al archivo .env donde se modificará la clave.
#key_to_set: La clave (nombre de la variable de entorno) que deseas modificar o agregar.
#value_to_set: El valor que deseas asignar a esa clave. Ejemplo:
from dotenv import set_key 
set_key(".env", "NEW_KEY", "new_value") # Agrega o modifica la clave "NEW_KEY" en el archivo .env 

#4. unset_key()
#Elimina una clave del archivo .env. Uso: Sirve para borrar una variable de entorno definida en el archivo .env. Sintaxis:
from dotenv import unset_key 
unset_key(dotenv_path, key_to_unset) 

#Parámetros: dotenv_path: El camino al archivo .env donde se eliminará la clave.
#key_to_unset: La clave (nombre de la variable de entorno) que deseas eliminar. Ejemplo:
from dotenv import unset_key 
unset_key(".env", "API_KEY") # Elimina la clave "API_KEY" del archivo .env 

#5. find_dotenv()
#Busca un archivo .env en el directorio actual o en los directorios superiores. Uso: Si no conoces la ubicación exacta del archivo .env, esta función lo buscará automáticamente comenzando desde el directorio actual. Sintaxis:
from dotenv import find_dotenv 
dotenv_path = find_dotenv() 

#Parámetros: dotenv_path (opcional): El camino al archivo .env que se desea buscar. Si no se proporciona, comienza a buscar desde el directorio actual.
#raise_error_if_not_found (opcional): Si es True, se lanzará una excepción si no se encuentra el archivo .env. Ejemplo:
from dotenv import find_dotenv 
dotenv_path = find_dotenv() # Busca el archivo .env en el directorio actual y superiores 
print(dotenv_path) 

#6. get_key()
#Obtiene el valor de una clave específica dentro del archivo .env. Uso: Sirve para recuperar el valor de una clave definida en el archivo .env, sin cargar todas las variables al entorno. Sintaxis:
from dotenv import get_key 
value = get_key(dotenv_path, key_to_get) 

#Parámetros: dotenv_path: El camino al archivo .env donde se encuentra la clave.
#key_to_get: El nombre de la clave cuyo valor deseas obtener. Ejemplo:

from dotenv import get_key 
value = get_key(".env", "API_KEY") # Obtiene el valor de la clave "API_KEY" 
print(value) 

#load_dotenv(): Carga el archivo .env en el entorno de ejecución.
#dotenv_values(): Devuelve las variables de un archivo .env como un diccionario sin modificar el entorno global.
#set_key(): Modifica o agrega una clave en el archivo .env.
#unset_key(): Elimina una clave del archivo .env.
#find_dotenv(): Busca un archivo .env en el directorio actual o superiores.
#get_key(): Obtiene el valor de una clave específica del archivo .env.



"""El módulo dotenv en Python no tiene clases definidas. Este módulo está diseñado principalmente para cargar y gestionar 
"variables de entorno desde archivos .env mediante funciones. Las operaciones clave se realizan a través de funciones como 
"load_dotenv(), dotenv_values(), y otras mencionadas previamente, pero no involucra clases o estructuras orientadas a objetos en su diseño."""


"""El módulo dotenv en Python no tiene variables globales predefinidas"""


"""El módulo dotenv en Python no tiene constantes predefinidas accesibles para el usuario. La funcionalidad del módulo se 
basa en funciones que gestionan la carga de variables de entorno desde archivos .env, pero no define constantes internas 
que se usen explícitamente en su API. En algunos módulos o bibliotecas, las constantes pueden ser usadas para configurar 
comportamientos, pero dotenv se enfoca en proporcionar funciones como load_dotenv(), dotenv_values(), set_key(), etc., 
sin exponer constantes directamente."""


"""El módulo dotenv en Python no define excepciones específicas propias"""

#Excepciones comunes que podrían surgir:
#FileNotFoundError: Si intentas cargar un archivo .env que no existe y no se especifica una ruta válida. Ejemplo: 
from dotenv import load_dotenv 
load_dotenv(".env_no_existe") # Si el archivo no existe, lanzará FileNotFoundError 

#UnicodeDecodeError: Si el archivo .env tiene un formato o codificación incompatible. Ejemplo: 
from dotenv import load_dotenv 
load_dotenv("archivo_invalido.env") # Si el archivo no puede ser decodificado, lanzará UnicodeDecodeError 

#KeyError: Si accedes a una clave que no existe en el diccionario de variables de entorno. Ejemplo: 
from dotenv import dotenv_values
config = dotenv_values(".env")
value = config["KEY_NO_EXISTE"] # Si la clave no está en el archivo, lanzará KeyError 



"""El módulo dotenv en Python no tiene submódulos específicos. Todo el funcionamiento del módulo se maneja a través de las 
funciones principales, como load_dotenv(), dotenv_values(), set_key(), entre otras, y no está estructurado en submódulos 
adicionales accesibles por el usuario."""


