"""¿Qué es una Excepción?
Una excepción es un evento que ocurre durante la ejecución de un programa y que interrumpe su flujo normal. Generalmente, representa errores que no pueden ser resueltos automáticamente, como: Intentar dividir entre cero. Acceder a un índice fuera de los límites de una lista. Abrir un archivo que no existe.

2. Tipos de Excepciones
Excepciones Predefinidas: Errores estándar proporcionados por el lenguaje de programación (como ZeroDivisionError, FileNotFoundError en Python).
Excepciones Personalizadas: Definidas por el programador para manejar errores específicos de una aplicación.

3. Flujo de Manejo de Excepciones
Lanzar una Excepción (Raising): Una excepción se genera automáticamente o se lanza manualmente usando una instrucción específica (por ejemplo, raise en Python).
Capturar la Excepción (Catching): Se utiliza un bloque de código especial para interceptar la excepción y manejarla.
Propagación de Excepciones: Si no se captura, la excepción se propaga hacia arriba en la pila de llamadas hasta que encuentre un manejador. Si no se maneja, el programa se interrumpe.

4. Bloques de Manejo de Excepciones
try: Bloque donde se coloca el código que podría generar excepciones.
except: Bloque para capturar y manejar la excepción.
else: Se ejecuta si no ocurre ninguna excepción.
finally: Código que se ejecuta siempre, independientemente de si ocurrió o no una excepción.

5. Propagación de Excepciones
Cuando ocurre una excepción, se busca un manejador en el bloque actual. Si no se encuentra, la excepción se propaga hacia la función llamadora, y así sucesivamente hasta llegar al nivel superior.

6. Excepciones Controladas y No Controladas
Controladas: Aquellas que el programador prevé y maneja explícitamente.
No Controladas: Aquellas que no se anticiparon y detienen la ejecución del programa.

Elementos Clave en la Gestión de Excepciones
Instrucción raise
Se utiliza para generar excepciones de forma manual en Python.
raise ValueError("Esto es un error personalizado") 

Bloques de Excepción"""
#try-except: 
try: 
    x = 10 / 0 

except ZeroDivisionError as e: 
    print(f"Error: {e}")

#finally: 
try: 
    archivo = open("datos.txt", "r") 


except FileNotFoundError: 
    print("El archivo no existe.") 

finally: 
    print("Esto siempre se ejecuta.") 

#else: 
try: 
    resultado = 10 / 2 

except ZeroDivisionError: 
    print("Error de división entre cero.") 

else: print(f"Resultado: {resultado}") 

#Excepciones Personalizadas
#Se crean subclasando la clase base de excepciones del lenguaje (Exception en Python).

class MiError(Exception): 
    pass
raise MiError("Este es un error definido por el usuario") 

#Encadenamiento de Excepciones
#Permite propagar información de excepciones originales al manejar nuevos errores.
try: 
    raise ValueError("Error original") 

except ValueError as e: 
    raise RuntimeError("Error nuevo") from e 

"""Usos Comunes de las Excepciones
Validación de entradas del usuario. Manejo de errores de archivo, como abrir o leer archivos no existentes. Gestión de errores en operaciones de red. Control de recursos como conexiones a bases de datos o archivos abiertos. Garantizar la limpieza de recursos mediante bloques finally."""



"""Conceptos Relacionados con las Excepciones

1. Contexto de Excepciones
Mensaje de error: Texto que describe el problema.
Tipo de excepción: Clase que identifica la naturaleza del error.
Traza de la pila (stack trace): Información sobre dónde ocurrió la excepción en el código.

2. Excepciones Silenciadas
Situaciones donde se captura una excepción pero no se realiza ninguna acción útil. Ejemplo: """
try: 
    resultado = 10 / 0 

except ZeroDivisionError: 
    pass # No se maneja el error, se ignora. 

"""3. Excepciones Jerárquicas
Las excepciones en lenguajes como Python están organizadas en una jerarquía de clases. 
BaseException: Clase base de todas las excepciones.
Exception: Clase base para errores de programa.

Errores específicos: Subclases de Exception como ValueError, TypeError, etc.

4. Excepciones Genéricas
Capturan cualquier excepción, pero se consideran una mala práctica si no se utilizan correctamente. """
try: 
    resultado = 10 / 0 

except Exception as e: 
    print(f"Error: {e}") 

"""5. Múltiples Excepciones
Capturar diferentes tipos de excepciones en un solo bloque: """
try: 
    resultado = 10 / x 

except (ZeroDivisionError, NameError): 
    print("Error de división o variable no definida.") 

"""6. Manejo de Recursos con Excepciones
Asegurar la liberación de recursos como archivos o conexiones.
Utiliza finally o contextos (with en Python): """
try: 
    archivo = open("datos.txt", "r") 
finally: archivo.close() 

"""7. Diseño de Excepciones Personalizadas
Crear excepciones específicas para situaciones únicas en una aplicación. 
Deben heredar de Exception o una subclase."""
class MiError(Exception): 
    def __init__(self, mensaje): 
        super().__init__(mensaje) 

"""8. Logging de Excepciones
Registro de errores para su análisis. Ejemplo con el módulo logging en Python: """
import logging 
try: x = 10 / 0 

except ZeroDivisionError as e: 
    logging.error("Ocurrió un error: %s", e) 

"""9. Errores Fatales
Excepciones que no se pueden manejar y detienen la ejecución. Ejemplo: Errores de memoria o de sistema en lenguajes de bajo nivel.

10. Excepciones y Depuración
Las trazas de excepciones ayudan a identificar dónde y por qué ocurrió un error, facilitando el proceso de depuración.

11. Excepciones en Funciones y Métodos
Las excepciones generadas dentro de una función o método deben ser capturadas por quien llama a esa función, si no se manejan internamente.

12. Programación Defensiva
Diseñar tu código para prever errores antes de que ocurran, reduciendo la necesidad de excepciones. Ejemplo: Validar datos antes de realizar operaciones sensibles."""




"""Buenas Prácticas al Trabajar con Excepciones"""

"""1. Manejar solo las Excepciones Necesarias
No uses excepciones genéricas como except Exception o except: a menos que sea estrictamente necesario, ya que podrían ocultar errores inesperados. Maneja únicamente los tipos de excepciones que esperas encontrar: """
try: 
    resultado = 10 / x 

except ZeroDivisionError: 
    print("No se puede dividir entre cero.") 

except NameError: 
    print("Variable no definida.") 

"""2. No Silenciar Excepciones
Evita capturar una excepción sin realizar ninguna acción, ya que dificulta la depuración. """
try: 
    resultado = 10 / 0 

except ZeroDivisionError: 
    pass # Mala práctica, el error queda ignorado. 

"""En su lugar:
Registra o maneja el error de manera adecuada: import logging """
try: resultado = 10 / 0 

except ZeroDivisionError as e: 
    logging.error(f"Error: {e}") 

"""3. Usa finally para Limpieza de Recursos
Utiliza el bloque finally para liberar recursos (archivos, conexiones, etc.), asegurando que esto ocurra sin importar si hubo o no una excepción. """
try: 
    archivo = open("datos.txt", "r") 
    contenido = archivo.read() 

except FileNotFoundError: 
    print("El archivo no existe.") 

finally: archivo.close() # Siempre se ejecuta. 

"""4. Usa Context Managers
En Python, los context managers (with) son más seguros que usar try-finally para manejar recursos."""
with open("datos.txt", "r") as archivo: 
    contenido = archivo.read() # No necesitas cerrar el archivo manualmente. 

"""5. Evita el Abuso de Excepciones
No uses excepciones para el flujo normal del programa. Por ejemplo: """
# Mala práctica
try: 
    lista = [1, 2, 3] 
    elemento = lista[5] 

except IndexError: 
    elemento = None 


#En su lugar: Usa estructuras condicionales para evitar errores: 
lista = [1, 2, 3] 
if len(lista) > 5: 
    elemento = lista[5] 
else: elemento = None 

"""6. No Expongas Detalles Internos
Evita mostrar mensajes de error crudos al usuario final, ya que pueden contener información sensible. """
try: 
    resultado = 10 / 0 

except ZeroDivisionError:
    print("Ocurrió un error. Inténtelo nuevamente.") 

"""7. Crea Excepciones Personalizadas
Cuando manejes errores específicos de tu aplicación, define excepciones personalizadas para mayor claridad. """
class MiError(Exception): 
    """Excepción personalizada para mi aplicación."""
pass 

def validar_edad(edad): 
    if edad < 18: 
        raise MiError("La edad debe ser mayor o igual a 18.") 

"""8. Agrega Mensajes Descriptivos
Al lanzar excepciones, proporciona mensajes claros que expliquen el problema. raise ValueError("El valor debe ser positivo y mayor a cero.") 

9. Usa else para el Código Libre de Errores
Coloca el código que solo debe ejecutarse si no ocurre una excepción en el bloque else. """
try: 
    resultado = 10 / 2

except ZeroDivisionError: 
    print("Error: División entre cero.") 
else: 
    print(f"El resultado es: {resultado}") 

"""10. No Atrapes Excepciones Fatales
No manejes excepciones relacionadas con el sistema, como KeyboardInterrupt o SystemExit, a menos que sea necesario. """
try: 
    resultado = 10 / x 

except (SystemExit, KeyboardInterrupt): 
    raise # Repropaga estas excepciones para no interrumpir el sistema. 

"""11. Registra las Excepciones
Usa herramientas de registro (logging) en lugar de imprimir los errores, para facilitar el monitoreo y la depuración. """
import logging 
logging.basicConfig(level=logging.ERROR) 
try: 
    x = 10 / 0 

except ZeroDivisionError as e: 
    logging.error(f"Ocurrió un error: {e}") 


"""12. Maneja Excepciones en Funciones Específicas
Es mejor capturar y manejar errores dentro de funciones donde ocurren, para evitar que las excepciones se propaguen innecesariamente. """
def dividir(a, b):
    try: 
        return a / b 

    except ZeroDivisionError: 
        return "No se puede dividir entre cero." 

"""13. Limita el Alcance del Bloque try
Coloca solo el código que podría generar una excepción dentro del bloque try para evitar errores difíciles de depurar."""
# Mala práctica 
try: 
    archivo = open("datos.txt", "r") 
    contenido = archivo.read() 
    procesar_datos(contenido) 

except FileNotFoundError: 
    print("El archivo no existe.") 

# Buena práctica:
try: archivo = open("datos.txt", "r") 
except FileNotFoundError: 
    print("El archivo no existe.") 
else: 
    contenido = archivo.read() 
    procesar_datos(contenido) 
finally: archivo.close() 

"""14. Usa Excepciones como Documentación
El manejo explícito de errores mejora la claridad del propósito del código y actúa como documentación implícita. """
def obtener_precio(producto):
    """Obtiene el precio del producto. Lanza KeyError si el producto no existe.""" 
    precios = {"manzana": 1.0, "banana": 0.5} 
    return precios[producto] 

"""15. Validación Preventiva
Antes de realizar operaciones propensas a fallar, valida las condiciones para reducir la posibilidad de excepciones."""
if divisor != 0:
    resultado = dividendo / divisor 
else: 
    print("Error: División entre cero.") 






"""Técnicas para Manejo Eficiente de Excepciones"""

"""1. Validación Preventiva
En lugar de dejar que las excepciones ocurran, valida condiciones antes de ejecutar operaciones que podrían fallar. 
# Ejemplo: Validar divisor antes de realizar una división """
def dividir(a, b): 
    if b == 0: 
        return "Error: División entre cero" 
    return a / b 

"""2. Uso de Excepciones Personalizadas
Define excepciones específicas para tu aplicación o dominio para manejar errores particulares. """
class EdadInvalidaError(Exception):
    pass 

def verificar_edad(edad): 
    if edad < 18: 
        raise EdadInvalidaError("La edad debe ser mayor o igual a 18.") 
    try: 
        verificar_edad(15) 
    except EdadInvalidaError as e: 
        print(e) 

"""3. Encadenamiento de Excepciones
Usa raise ... from ... para capturar una excepción, lanzar otra y conservar el contexto del error original. """
try: 
    resultado = 10 / 0 
except ZeroDivisionError as e: 
    raise ValueError("Error al realizar la operación") from e 

"""4. Manejo de Excepciones Múltiples
Captura múltiples tipos de excepciones en un mismo bloque. """
try: 
    valor = int(input("Introduce un número: ")) 
    resultado = 10 / valor 
except (ZeroDivisionError, ValueError) as e: 
    print(f"Error: {e}") 

"""5. Bloque else para Código Seguro
Usa el bloque else para código que se ejecutará solo si no ocurrió ninguna excepción."""
try: resultado = 10 / 2 
except ZeroDivisionError: 
    print("Error: División entre cero.") 
else: print(f"Resultado: {resultado}") 

"""6. Limitación del Bloque try
Coloca solo el código que puede generar excepciones dentro del bloque try para reducir errores y mejorar la legibilidad."""
# Mala práctica 
try: 
    archivo = open("datos.txt", "r") 
    contenido = archivo.read() 
    procesar_datos(contenido) 
except FileNotFoundError: 
    print("El archivo no existe.") 

# Buena práctica 
try: archivo = open("datos.txt", "r") 
except FileNotFoundError: 
    print("El archivo no existe.") 
else: contenido = archivo.read() 
procesar_datos(contenido) 

"""10. Captura de Excepciones Globales
En aplicaciones grandes, implementa un manejador global de excepciones para capturar errores inesperados."""
import sys 
import logging 
def manejador_global(tipo, valor, traza): 
    ogging.error("Excepción no manejada", exc_info=(tipo, valor, traza)) 
    sys.excepthook = manejador_global 


"""11. Uso de Decoradores para Manejar Excepciones
Crea un decorador que capture y maneje excepciones para reducir redundancia en múltiples funciones."""
def manejar_excepciones(func): 
    def wrapper(*args, **kwargs): 
        try: 
            return func(*args, **kwargs) 
        except Exception as e: 
            print(f"Error en {func.__name__}: {e}") 
        return wrapper 

@manejar_excepciones 
def dividir(a, b): 
    return a / b 

dividir(10, 0) 

"""12. Excepciones y Retries
Implementa un mecanismo de reintentos para operaciones críticas."""
import time 
def reintentar(func, intentos=3, espera=2): 
    for i in range(intentos): 
        try: 
            return func() 
        except Exception as e: 
            print(f"Error: {e}. Reintentando...") 

time.sleep(espera) 
raise RuntimeError("Operación fallida tras múltiples intentos.") 

def operacion_critica(): 
    raise ValueError("Error crítico") 
reintentar(operacion_critica) 

"""13. Documentación de Excepciones
Documenta las excepciones que puede lanzar tu función para que los usuarios sepan cómo manejarlas."""
def dividir(a, b): 
    """ Realiza la división de dos números. Args: a (float): Numerador. b (float): Denominador. Raises: ZeroDivisionError: Si el denominador es cero. """ 
    if b == 0: 
        raise ZeroDivisionError("El denominador no puede ser cero.") 
    return a / b 

"""14. Excepciones Encapsuladas
Usa funciones de nivel superior para encapsular y manejar excepciones de manera centralizada."""
def ejecutar_operacion(func, *args): 
    try: 
        return func(*args) 
    except Exception as e: 
        print(f"Error al ejecutar {func.__name__}: {e}") 

def dividir(a, b): 
    return a / b 

ejecutar_operacion(dividir, 10, 0) 

"""15. Evita el Uso Excesivo de Excepciones
Usa excepciones únicamente para manejar errores, no para controlar el flujo normal del programa."""