import time

"""El módulo time en Python proporciona funciones para trabajar con el tiempo y realizar tareas relacionadas con la 
medición de tiempo, control de retrasos y conversiones entre diferentes representaciones del tiempo. Ofrece herramientas 
para trabajar con marcas de tiempo, retrasos (pausas) en la ejecución y medición de intervalos de tiempo. Es 
especialmente útil cuando se necesita realizar operaciones con tiempos a nivel de segundos o microsegundos."""



"""Funciones del módulo time"""

#time() Devuelve el tiempo actual en segundos desde la "época" (generalmente 1 de enero de 1970, también conocido como Unix timestamp). Ejemplo: 
print(time.time()) # Ejemplo de tiempo actual en segundos 

#sleep(seconds) Suspende la ejecución del programa durante el número de segundos especificado. Ejemplo:
time.sleep(2) # Detiene el programa por 2 segundos 

#localtime([secs]) Convierte el tiempo (en segundos desde la época) en una estructura de tiempo local (horas, minutos, segundos, etc.). Si no se pasa ningún argumento, usa el tiempo actual. Ejemplo:
print(time.localtime()) # Convierte el tiempo actual a hora local 

#gmtime([secs]) Convierte el tiempo (en segundos desde la época) en una estructura de tiempo en UTC (Tiempo Universal Coordinado). Si no se pasa un argumento, usa el tiempo actual. Ejemplo:
print(time.gmtime()) # Convierte el tiempo actual a UTC 

#asctime([t]) Convierte una estructura de tiempo a una cadena representando la fecha y la hora. Si no se pasa un argumento, utiliza el tiempo actual. Ejemplo:
print(time.asctime()) # Ejemplo de la fecha y hora actuales como cadena 

#ctime([secs]) Convierte un valor de tiempo (en segundos desde la época) a una cadena de caracteres representando la fecha y hora. Si no se pasa un argumento, usa el tiempo actual. Ejemplo:
print(time.ctime()) # Fecha y hora actuales como cadena 

#mktime(t) Convierte una estructura de tiempo (como la devuelta por localtime() o gmtime()) en un valor de tiempo (en segundos desde la época). Ejemplo:
t = time.localtime() 
print(time.mktime(t)) # Convierte la estructura de tiempo a segundos desde la época 

#perf_counter() Devuelve un contador de alto rendimiento que se puede usar para medir intervalos de tiempo de alta precisión. Ejemplo:
start = time.perf_counter() # Código que quieres medir 
end = time.perf_counter()
print(f"El código tardó {end - start} segundos.") 

#process_time() Devuelve el tiempo de CPU en segundos consumido por el proceso actual. Ejemplo:
print(time.process_time()) # Tiempo de CPU utilizado por el proceso actual 

#monotonic() Devuelve el tiempo en segundos desde algún momento arbitrario en el pasado, pero siempre ascendente, útil para medir intervalos de tiempo. Ejemplo:
start = time.monotonic() # Código a medir 
end = time.monotonic() 
print(f"Intervalo de tiempo: {end - start} segundos") 

#time_ns() Devuelve el tiempo actual en nanosegundos desde la época. Ejemplo:
print(time.time_ns()) # Tiempo actual en nanosegundos 

#strptime(string, format) Convierte una cadena de caracteres que representa una fecha y hora, según un formato especificado, en una estructura de tiempo. Ejemplo:
date_string = "2025-02-16 14:30:00"
format = "%Y-%m-%d %H:%M:%S" 
print(time.strptime(date_string, format)) # Convierte la cadena a estructura de tiempo 

#strftime(format, t) Convierte una estructura de tiempo a una cadena de caracteres según el formato especificado. Ejemplo:
t = time.localtime() 
print(time.strftime("%Y-%m-%d %H:%M:%S", t)) # Fecha y hora formateada como cadena 

#tzset() Asegura que la zona horaria esté configurada correctamente para la ejecución del script. Ejemplo:
time.tzset() # Establece la zona horaria 




"""El módulo time de Python no tiene clases definidas, ya que está diseñado principalmente para trabajar con funciones 
relacionadas con el tiempo (como obtener el tiempo actual, dormir, etc.). A diferencia de otros módulos como datetime, 
que proporcionan clases como datetime, date o time, el módulo time se enfoca en funciones y no en estructuras de objetos."""



"""Variables del módulo time"""

#time.altzone Representa la diferencia en segundos entre la hora local estándar y la hora local de verano (si aplica). Ejemplo:
print(time.altzone) # Muestra la diferencia en segundos de la hora de verano 

#time.daylight Un valor booleano que indica si hay horario de verano en la zona horaria local (1 si hay horario de verano, 0 si no lo hay). Ejemplo:
print(time.daylight) # 1 si hay horario de verano, 0 si no 

#time.timezone Representa la diferencia en segundos entre UTC y la hora local estándar (sin tener en cuenta el horario de verano). Ejemplo:
print(time.timezone) # Diferencia en segundos con UTC 

#time.tzname Una tupla que contiene los nombres de las zonas horarias estándar y de verano (si aplica). El primer valor es la zona horaria estándar, y el segundo valor es la zona horaria de verano (si existe). Ejemplo:
print(time.tzname) # Tupla con el nombre de la zona horaria 





"""Constantes del módulo time"""

#time.TIME_UTC Representa la zona horaria UTC (Tiempo Universal Coordinado), utilizada en operaciones de tiempo y comparación. Ejemplo:
print(time.TIME_UTC) # Muestra la constante UTC 

#time.PERF_COUNTER Representa un contador de alto rendimiento utilizado para medir intervalos de tiempo de alta precisión, sin preocuparse por el sistema de reloj o el ajuste de tiempo. Ejemplo:
print(time.PERF_COUNTER) # Contador de alta precisión 

#time.ctime Devuelve una cadena que representa la fecha y hora local (generalmente en formato Sun Oct 21 14:35:15 2018), aunque esta es en realidad una función, se usa comúnmente como una forma predeterminada de acceder a la fecha y hora.




"""El módulo time en Python no define excepciones propias. Sin embargo, las funciones del módulo time pueden 
lanzar algunas excepciones estándar de Python cuando se encuentran con errores. """


#ValueError Ocurre si se pasa un argumento no válido a una función del módulo time. Por ejemplo, si intentas usar un formato incorrecto en funciones como strptime() o proporcionar un valor fuera de rango (por ejemplo, un número de mes mayor a 12). Ejemplo:
try:
    time.strptime("2025-02-30", "%Y-%m-%d") # Fecha no válida
except ValueError as e:
    print(f"Error: {e}") # 'unconverted data remains' 

#TypeError Ocurre cuando un argumento de tipo incorrecto se pasa a una función. Por ejemplo, pasar un valor no iterable a localtime() o gmtime(). Ejemplo:
try:
    time.localtime("not a number") # Tipo incorrecto
except TypeError as e:
    print(f"Error: {e}") # TypeError: argument must be a number 

#OSError Puede ocurrir en algunas funciones de manejo de tiempo que interactúan con el sistema operativo, como la configuración de la zona horaria o el uso de funciones de alto rendimiento (por ejemplo, perf_counter()) en plataformas no compatibles. Ejemplo:
try: # Usar función de reloj de alto rendimiento en un entorno que no lo soporta 
    time.perf_counter() 
except OSError as e: 
    print(f"Error: {e}") 



"""El módulo time en Python no tiene submódulos. Todo lo que ofrece está contenido dentro del propio módulo. A "
"diferencia de otros módulos más complejos, como datetime, que tiene submódulos adicionales o módulos relacionados, 
time se mantiene sencillo y directo, proporcionando funciones para trabajar con el tiempo, pero sin subdivisiones 
adicionales en submódulos."""
