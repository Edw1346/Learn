"""Logs permite monitorear y depurar el comportamiento de las apps en tiempo real. Los logs son registros de eventos, errores y comportamientos en un sistema. """

"""1. Módulo logging en Python
El módulo logging es el estándar para el registro de logs en Python. Proporciona una forma flexible de generar, manejar y almacenar mensajes de log en distintos niveles de gravedad (por ejemplo, DEBUG, INFO, WARNING, ERROR, CRITICAL).

Configuración básica de logs
La configuración más sencilla para comenzar a usar logging es la siguiente:"""
import logging 
# Configuración básica 
logging.basicConfig(level=logging.DEBUG) 
# Ejemplo de diferentes niveles de logs
logging.debug("Este es un mensaje de depuración") 
logging.info("Este es un mensaje informativo")
logging.warning("Este es un mensaje de advertencia")
logging.error("Este es un mensaje de error") 
logging.critical("Este es un mensaje crítico") 

"""Explicación de los niveles de log:
DEBUG: Mensajes detallados, típicamente utilizados para diagnosticar problemas.
INFO: Mensajes informativos, generalmente sobre el flujo de la aplicación.
WARNING: Mensajes sobre eventos que no son errores, pero que podrían requerir atención.
ERROR: Mensajes sobre errores que han afectado el funcionamiento de la aplicación.
CRITICAL: Mensajes sobre errores graves que pueden afectar el sistema de forma significativa."""

"""2. Configuración avanzada de logs
Para tener más control sobre cómo se manejan y almacenan los logs, se pueden configurar opciones avanzadas, como diferentes destinos (por ejemplo, archivo o consola), formateo personalizado, y niveles de severidad.
Ejemplo de configuración avanzada:"""

import logging 
# Configuración avanzada 
logging.basicConfig( level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", handlers=[ logging.FileHandler("mi_app.log"), """Registra en un archivo""" logging.StreamHandler() """Registra en consola""" ] ) 
logging.debug("Este es un mensaje de depuración")
logging.info("Este es un mensaje informativo") 
logging.warning("Este es un mensaje de advertencia") 

"""Parámetros de configuración:
level: Define el nivel mínimo de log que se registrará.
format: Personaliza el formato del mensaje de log. Se pueden incluir variables como asctime (hora del log), name (nombre del logger), levelname (nivel de severidad), y message (mensaje).
handlers: Se utilizan para definir los destinos de los logs, como archivos, consola, o incluso servidores remotos."""

"""3. Uso de Logger, Handler, y Formatter
En aplicaciones más complejas, es recomendable usar instancias específicas de Logger, Handler, y Formatter para personalizar aún más el manejo de logs.
Ejemplo usando Logger, Handler y Formatter:"""
import logging
# Crear un logger personalizado
logger = logging.getLogger('mi_logger') 
logger.setLevel(logging.DEBUG) 
# Crear un handler que escriba en un archivo
file_handler = logging.FileHandler('mi_app.log') 
file_handler.setLevel(logging.DEBUG) 
# Crear un formatter para personalizar el formato 
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s') 
file_handler.setFormatter(formatter) 
# Añadir el handler al logger 
logger.addHandler(file_handler)
# Crear otro handler que escriba en la consola 
console_handler = logging.StreamHandler() 
console_handler.setLevel(logging.ERROR) 
logger.addHandler(console_handler) 
# Mensajes de log 
logger.debug("Este es un mensaje de depuración")
logger.info("Este es un mensaje informativo") 
logger.warning("Este es un mensaje de advertencia") 
logger.error("Este es un mensaje de error") 

"""Componentes clave:

Logger: Se encarga de generar los mensajes de log.
Handler: Maneja los destinos donde se registran los logs, como archivos o consola.
Formatter: Personaliza el formato de los mensajes de log."""

"""4. Rotación de Logs (Log Rotation)
Es común que los archivos de logs crezcan demasiado con el tiempo. Para manejar esto, puedes usar el RotatingFileHandler o TimedRotatingFileHandler para crear un mecanismo de rotación de logs, asegurando que los archivos de log no crezcan de manera infinita.
Ejemplo de rotación de logs basada en tamaño:"""
import logging from logging.handlers 
import RotatingFileHandler
# Crear un handler de rotación de archivos
rotating_handler = RotatingFileHandler( 'mi_app.log', maxBytes=2000, backupCount=3) 
rotating_handler.setLevel(logging.DEBUG) 
# Crear un logger y añadir el handler 

logger = logging.getLogger('mi_logger') 
logger.setLevel(logging.DEBUG) 
logger.addHandler(rotating_handler) 
# Registrar algunos mensajes 
for i in range(1000): 
    logger.debug(f"Mensaje {i}") 

"""Explicación:
maxBytes: Tamaño máximo que puede alcanzar un archivo de log antes de que se cree un nuevo archivo.
backupCount: Número de archivos de respaldo a mantener."""

#Ejemplo de rotación de logs basada en tiempo:
from logging.handlers import TimedRotatingFileHandler 
# Crear un handler de rotación de archivos basado en tiempo 
timed_handler = TimedRotatingFileHandler( 'mi_app.log', when='midnight', interval=1, backupCount=7)
timed_handler.setLevel(logging.DEBUG) 
# Crear un logger y añadir el handler 
logger = logging.getLogger('mi_logger')
logger.setLevel(logging.DEBUG) 
logger.addHandler(timed_handler) 
# Registrar algunos mensajes 
logger.info("Este es un mensaje que se registrará") 

"""Explicación:
when: Define el intervalo de tiempo para rotar los logs. Puede ser midnight, hour, etc.
interval: Define el intervalo de rotación en unidades de tiempo.
backupCount: Número de archivos de respaldo que se mantienen."""

"""5. Filtrado de Logs
Los filtros permiten especificar condiciones más complejas para los mensajes de log, como filtrar por el nombre del logger o por el contenido del mensaje.

Ejemplo de filtro de logs:"""
import logging 
class MiFiltro(logging.Filter):
    def filter(self, record): 
        return "error" in record.getMessage().lower() 
# Crear un logger y añadir el filtro 
logger = logging.getLogger('mi_logger') 
logger.setLevel(logging.DEBUG) 
# Crear un handler para la consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG) 
# Añadir el filtro al handler 
console_handler.addFilter(MiFiltro())
# Añadir el handler al logger 
logger.addHandler(console_handler)
# Mensajes de log
logger.debug("Este es un mensaje de debug") 
logger.error("Este es un mensaje de error") 

"""Explicación:
El filtro permite personalizar aún más los mensajes que se registran. En este caso, el filtro solo pasa los mensajes que contienen la palabra "error"."""