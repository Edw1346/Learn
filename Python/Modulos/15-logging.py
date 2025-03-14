import logging

"""El módulo logging de Python tiene muchas funciones útiles para generar logs. """


"""Ahora todas, todas las Funciones del modulo logging """

#1. basicConfig() Configura el sistema de logging. Esta función se utiliza para establecer la configuración predeterminada de los registros. Ejemplo:
logging.basicConfig(level=logging.DEBUG) 

#2. getLogger() Crea o recupera un logger con un nombre específico. Si no se le pasa un nombre, retorna el logger raíz. Ejemplo:
logger = logging.getLogger("mi_logger")
logger.debug("Mensaje de depuración") 

#3. debug() Registra un mensaje con nivel de gravedad DEBUG. Este nivel se usa generalmente para la depuración detallada. Ejemplo:
logging.debug("Mensaje de depuración") 

#4. info() Registra un mensaje con nivel de gravedad INFO. Usado para información general sobre la ejecución. Ejemplo:
logging.info("Mensaje informativo") 

#5. warning() Registra un mensaje con nivel de gravedad WARNING. Indica que algo inesperado ocurrió, pero no es grave. Ejemplo:
logging.warning("Advertencia") 

#6. error() Registra un mensaje con nivel de gravedad ERROR. Indica que algo salió mal, pero el programa puede continuar. Ejemplo:
logging.error("Mensaje de error") 

#7. exception() Registra un mensaje con nivel de gravedad ERROR y agrega la traza de la excepción actual (si está en un bloque try-except). Ejemplo:
try: 
    1 / 0 
except ZeroDivisionError: 
    logging.exception("Ocurrió un error") 

#8. critical() Registra un mensaje con nivel de gravedad CRITICAL. Indica que ocurrió un error grave que probablemente hará que el programa termine. Ejemplo:
logging.critical("Error crítico") 

#9. log() Permite registrar un mensaje en cualquier nivel de severidad. El nivel es pasado como un número (por ejemplo, logging.DEBUG, logging.INFO, etc.). Ejemplo:
logging.log(logging.INFO, "Mensaje con log") 

#10. addHandler() Añade un manejador (handler) a un logger para enviar los logs a un destino específico (archivo, consola, etc.). Ejemplo:
console_handler = logging.StreamHandler() 
logger = logging.getLogger()
logger.addHandler(console_handler) 

#11. removeHandler() Elimina un manejador de un logger. Ejemplo:
logger.removeHandler(console_handler) 

#12. shutdown() Detiene el sistema de logging y maneja cualquier recurso de salida pendiente (por ejemplo, cerrar archivos). Ejemplo:
logging.shutdown() 

#13. basicConfig() Esta función configura el sistema de logging con parámetros personalizados, como el nivel, formato, archivo de salida, etc. Ejemplo:
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') 

#14. captureWarnings() Permite capturar las advertencias de la librería warnings y enviarlas a los logs. Ejemplo:
import warnings 
logging.captureWarnings(True)
warnings.warn("Esto es una advertencia") 

#15. disable() Desactiva el sistema de logging globalmente, deteniendo la salida de mensajes de registro. Ejemplo:
logging.disable(logging.CRITICAL) # Desactiva los logs de nivel crítico y menores 





"""El módulo logging de Python contiene varias clases que te permiten personalizar y manejar de manera eficiente el 
"registro de logs. Aquí están las clases principales que se encuentran en el módulo logging:"""

#1. Logger Es la clase principal que se utiliza para registrar los mensajes. Cada logger tiene un nombre y puede tener 
# diferentes niveles de registro. Esta clase es responsable de emitir los mensajes de log, basándose en el nivel de gravedad configurado. Ejemplo:
logger = logging.getLogger("mi_logger")
logger.setLevel(logging.DEBUG)
logger.debug("Este es un mensaje de depuración.") 

#2. Handler. Es la clase base para los manejadores que envían los registros de log a diferentes destinos 
# (como consola, archivos, o incluso servidores remotos). Hay varios tipos de manejadores, como StreamHandler, FileHandler, etc. Ejemplo de uso:
handler = logging.StreamHandler() # Envía los logs a la consola 
logger = logging.getLogger() 
logger.addHandler(handler) 
logger.info("Este es un mensaje informativo.") 

#3. StreamHandler
#Es un tipo específico de Handler que envía los mensajes de log a un flujo de salida, como la consola (sys.stdout o sys.stderr). Ejemplo:
stream_handler = logging.StreamHandler()
logging.basicConfig(level=logging.DEBUG) 
logging.getLogger().addHandler(stream_handler) 
logging.debug("Mensaje en la consola") 

#4. FileHandler
#Es un tipo de Handler que se utiliza para escribir los mensajes de log en un archivo. Ejemplo:
file_handler = logging.FileHandler('mi_log.log')
logging.getLogger().addHandler(file_handler) 
logging.error("Este mensaje se escribe en un archivo.") 

#5. Formatter
#Es la clase que se encarga de definir el formato de los mensajes de log. Con esta clase puedes personalizar cómo se ven los mensajes de log, como agregar la fecha, el nivel del log, el mensaje, etc. Ejemplo:
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s') 
console_handler = logging.StreamHandler() 
console_handler.setFormatter(formatter)
logging.getLogger().addHandler(console_handler)
logging.warning("Este es un mensaje con formato personalizado.") 

#6. Filter
#La clase Filter se utiliza para incluir o excluir ciertos registros de log, según ciertas condiciones. Es útil cuando deseas aplicar una lógica de filtrado avanzada. Ejemplo:
class MiFiltro(logging.Filter): 
    def filter(self, record):
        return 'error' in record.getMessage().lower() 

logger = logging.getLogger()
logger.addFilter(MiFiltro()) 
logger.debug("Mensaje debug")
logger.error("Este es un error") # Solo este mensaje se imprimirá 

#7. NullHandler
#Este manejador especial es útil cuando se desea desactivar los logs sin que se generen mensajes de error por no tener un manejador definido. Se usa principalmente cuando creas librerías que no deben generar logs, pero no quieres que se produzcan errores si el usuario no configura su propio manejador de logs. Ejemplo:
null_handler = logging.NullHandler()
logger = logging.getLogger("mi_logger") 
logger.addHandler(null_handler) 
logger.warning("Este mensaje no se mostrará ni guardará.") 

#8. LoggerAdapter
#Es una clase que permite adaptar un logger existente para agregar información adicional al mensaje de log, como un contexto extra o metadatos (por ejemplo, el ID de un usuario o transacción). Ejemplo:
logger = logging.getLogger("mi_logger") 
class ContextAdapter(logging.LoggerAdapter): 
    def process(self, msg, kwargs): 
        return f"[Contexto] {msg}", kwargs 

logger_adapter = ContextAdapter(logger, {}) 
logger_adapter.info("Mensaje con contexto.") 



"""El módulo logging de Python no tiene muchas variables predefinidas como otros módulos, pero existen algunas variables 
globales y configuraciones que son útiles al trabajar con registros. Aquí te dejo una descripción de las variables más 
importantes que puedes encontrar en el módulo logging:"""

#1. logging.DEBUG
#Es un nivel de log predefinido que indica que los mensajes de log deben ser más detallados, usualmente utilizados para la depuración. Ejemplo:
logging.basicConfig(level=logging.DEBUG) 

#2. logging.INFO
#Es un nivel de log predefinido que se utiliza para mensajes informativos, que describen el progreso normal de la aplicación. Ejemplo:
logging.basicConfig(level=logging.INFO) 

#3. logging.WARNING
#Es un nivel de log predefinido que se utiliza para advertencias sobre situaciones no ideales, pero que no afectan el funcionamiento del programa. Ejemplo:
logging.basicConfig(level=logging.WARNING) 

#4. logging.ERROR
#Es un nivel de log predefinido que se utiliza para indicar que ocurrió un error en el programa que puede afectar su comportamiento. Ejemplo:
logging.basicConfig(level=logging.ERROR) 

#5. logging.CRITICAL
#Es el nivel de log más alto, usado para situaciones extremadamente graves que probablemente harán que el programa falle. Ejemplo:
logging.basicConfig(level=logging.CRITICAL) 

#6. logging.NOTSET
#Es un nivel especial que se utiliza para indicar que no se ha establecido un nivel de log, lo que permite que los mensajes de todos los niveles se registren. Ejemplo:
logging.basicConfig(level=logging.NOTSET) 

#7. logging.root
#Es la instancia raíz del logger, que es el logger principal que utiliza el módulo para registrar los mensajes. Ejemplo:
logging.root.debug("Este es un mensaje del logger raíz.") 

#8. logging.basicConfig() (aunque no es una variable, es una función importante)
#Esta función configura el logging de forma predeterminada, especificando el nivel, el formato y otros parámetros básicos. Ejemplo:
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') 





"""El módulo logging de Python incluye varias constantes que se utilizan para definir el comportamiento y la configuración 
de los logs. Estas constantes principalmente están relacionadas con los niveles de log, los formatos, y el comportamiento 
de los manejadores. """

#1. logging.DEBUG
#Es una constante que define el nivel de log DEBUG, que se utiliza para registrar mensajes detallados que ayudan en la depuración del código. Es el nivel más bajo de severidad. Ejemplo:
logging.basicConfig(level=logging.DEBUG) 

#2. logging.INFO
#Es una constante que define el nivel de log INFO, que se utiliza para registrar mensajes informativos sobre el flujo normal de la aplicación. Ejemplo:
logging.basicConfig(level=logging.INFO) 

#3. logging.WARNING
#Es una constante que define el nivel de log WARNING, que se utiliza para advertir sobre condiciones inesperadas que no son errores graves pero que podrían causar problemas más adelante. Ejemplo:
logging.basicConfig(level=logging.WARNING) 

#4. logging.ERROR
#Es una constante que define el nivel de log ERROR, que se utiliza para registrar errores que ocurren en la ejecución del programa. Ejemplo:
logging.basicConfig(level=logging.ERROR) 

#5. logging.CRITICAL
#Es una constante que define el nivel de log CRITICAL, que se utiliza para registrar errores extremadamente graves que pueden hacer que el programa falle. Ejemplo:
logging.basicConfig(level=logging.CRITICAL) 

#6. logging.NOTSET
#Es una constante que representa el nivel más bajo de log. Cuando se usa, todos los mensajes de log serán procesados sin importar su nivel de severidad. Ejemplo:
logging.basicConfig(level=logging.NOTSET) 

#7. logging.TimedRotatingFileHandler
#Es una constante relacionada con el manejador TimedRotatingFileHandler, que se usa para guardar logs en un archivo y que el archivo se rote (se cree un nuevo archivo) después de un período de tiempo específico. Ejemplo:
import logging.handlers 
handler = logging.handlers.TimedRotatingFileHandler('mi_log.log', when="midnight", interval=1) 

#8. logging.StreamHandler
#Es una constante que se refiere al manejador StreamHandler, utilizado para enviar los registros a un flujo de salida, como la consola o un archivo. Ejemplo:
handler = logging.StreamHandler() 

#9. logging.FileHandler
#Es una constante que se refiere al manejador FileHandler, que se usa para registrar los mensajes de log en un archivo. Ejemplo:
handler = logging.FileHandler('mi_log.log') 

#10. logging.NullHandler
#Es una constante que hace que los mensajes de log sean ignorados, útil cuando no se desea emitir ningún log o cuando no se ha configurado un manejador de log. Ejemplo:
null_handler = logging.NullHandler() 

#11. logging.Formatter
#Aunque Formatter no es una constante en sí, el formato de registro se puede definir con constantes como %(asctime)s, %(levelname)s, etc., que son placeholders para la hora, el nivel del log, y el mensaje. Ejemplo:
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s') 






"""El módulo logging de Python define algunas excepciones específicas que son útiles para manejar errores relacionados con 
el registro de logs. Aunque no son muchas, estas excepciones permiten capturar problemas que pueden surgir cuando 
trabajas con los logs. A continuación te las explico:"""

#1. logging.Error
#Esta es la excepción base para todas las excepciones relacionadas con el módulo logging. Aunque no es utilizada directamente en la mayoría de los casos, sirve como base para otras excepciones más específicas.

#2. logging.LogRecord
#Aunque no es una excepción en sí misma, esta clase se usa para crear objetos de log, y si ocurre un error durante la creación de un LogRecord (por ejemplo, con una mala configuración de formato), podrías recibir una excepción. Pero, de nuevo, esta clase no es una excepción per se.

#3. logging.Handler
#El Handler en logging se puede utilizar para manejar excepciones, aunque no es una excepción en sí misma. Si se configura mal un Handler o se produce un error al escribir los logs, puede lanzar excepciones estándar de Python (como IOError), pero no tiene excepciones propias predefinidas.

#Excepciones relacionadas que podrías encontrar:
#IOError: Si se intenta escribir en un archivo de log y hay un error de entrada/salida (como si el archivo está siendo usado por otro proceso o no existe).
#ValueError: Si se configuran valores incorrectos al establecer el formato o los manejadores de los logs.

#Ejemplo de manejo de excepciones con logging:
import logging # Configuración básica del logging 
logging.basicConfig(level=logging.DEBUG) 
try: # Aquí podríamos tener un error como un archivo no accesible 
    handler = logging.FileHandler("logfile.log") 
    logging.getLogger().addHandler(handler) 
    logging.info("Este es un mensaje de log.")
except (IOError, ValueError) as e: 
    logging.error("Ocurrió un error al configurar el manejador: %s", e) 



"""El módulo logging en Python no tiene submódulos internos. Sin embargo, se puede usar de manera extensiva con varios 
componentes y clases para manejar la configuración y los registros. Los submódulos a los que comúnmente puedes referirte 
dentro del contexto de logging son los "handlers", "filters", "formatters", y "loggers", que permiten personalizar el 
comportamiento de los logs, pero todos ellos están dentro del módulo principal logging."""

#Componentes dentro del módulo logging:
#Loggers. Son responsables de recibir los mensajes de log y enviar esos mensajes a los manejadores (handlers).
#Puedes tener múltiples loggers, cada uno configurado para manejar mensajes en diferentes partes de tu aplicación.
logger = logging.getLogger('mi_logger') 

#Handlers
#Los manejadores (Handler) determinan cómo y dónde se envían los mensajes de log (por ejemplo, a un archivo, consola, red, etc.). Algunos ejemplos son StreamHandler (para enviar logs a la consola), FileHandler (para escribir los logs en un archivo), y RotatingFileHandler (para manejar logs rotativos).
handler = logging.StreamHandler() # Manejador para la consola 

#Formatters
#Los Formatters definen cómo se formatean los mensajes de log.
#Puedes especificar cosas como la fecha y hora, el nivel de severidad, el mensaje, etc.
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s') 

#Filters
#Los filtros permiten aplicar condiciones personalizadas a los mensajes de log antes de que sean manejados, dándote más control sobre lo que se registra.
class MiFiltro(logging.Filter): 
    def filter(self, record):
        return 'ERROR' in record.msg 

