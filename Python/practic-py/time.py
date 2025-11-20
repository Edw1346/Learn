"""El módulo time proporciona funciones para trabajar con el tiempo y realizar tareas relacionadas con la medición de tiempo, control de retrasos y conversiones entre d
iferentes representaciones del tiempo. 

Funciones comunes del módulo time:
time.time(): Devuelve tiempo actual en segundos desde la "época" (generalmente el 1 de enero de 1970).
time.sleep(): Detiene la ejecución del programa durante un número específico de segundos.
time.localtime(): Convierte un tiempo en formato de segundos desde la época a una estructura de tiempo local.
time.gmtime(): Convierte un tiempo en formato de segundos desde la época a una estructura de tiempo en UTC."""

import time 

#Funciones del módulo time

#time(). Devuelve el tiempo actual en segundos desde la "época" (generalmente 1 de enero de 1970):
print(time.time()) # Ejemplo de tiempo actual en segundos 

##sleep(seconds). Suspende la ejecución del programa durante el número de segundos especificado:
time.sleep(10) # Detiene el programa por 2 segundos 
print(time.time()) # Ejemplo de tiempo actual en segundos 

#localtime([secs]). Convierte el tiempo (en segundos desde la época) en una estructura de tiempo local (horas, minutos, segundos, etc.). Si no se pasa ningún argumento, usa el tiempo actual. Ejemplo:
print(time.localtime()) # Convierte el tiempo actual a hora local 

#gmtime([secs]). Convierte el tiempo (en segundos desde la época) en una estructura de tiempo en UTC (Tiempo Universal Coordinado). Si no se pasa un argumento, usa el tiempo actual. Ejemplo:
print(time.gmtime()) # Convierte el tiempo actual a UTC 

#asctime([t]). Convierte una estructura de tiempo a una cadena representando la fecha y la hora. Si no se pasa un argumento, utiliza el tiempo actual. Ejemplo:
print(time.asctime()) # Ejemplo de la fecha y hora actuales como cadena 

#ctime([secs]). Convierte un valor de tiempo (en segundos desde la época) a una cadena de caracteres representando la fecha y hora. Si no se pasa un argumento, usa el tiempo actual. Ejemplo:
print(time.ctime()) # Fecha y hora actuales como cadena 

#mktime(t). Convierte una estructura de tiempo (como la devuelta por localtime() o gmtime()) en un valor de tiempo (en segundos desde la época): 
t = time.localtime() 
print(time.mktime(t)) # Convierte la estructura de tiempo a segundos desde la época 

#perf_counter(). Devuelve un contador de alto rendimiento que se puede usar para medir intervalos de tiempo de alta precisión:
start = time.perf_counter() #Inicio de contador
time.sleep(5)
end = time.perf_counter()
print(f"El código tardó {end - start} segundos.") 

#process_time(). Devuelve el tiempo de CPU en segundos consumido por el proceso actual:
print(time.process_time()) # Tiempo de CPU utilizado por el proceso actual 

#monotonic(). Devuelve el tiempo en segundos desde algún momento arbitrario en el pasado, pero siempre ascendente, útil para medir intervalos de tiempo: 
start = time.monotonic() # Código a medir 
time.sleep(5)
end = time.monotonic() 
print(f"Intervalo de tiempo: {end - start} segundos") 

#time_ns(). Devuelve el tiempo actual en nanosegundos desde la época:
print(time.time_ns()) # Tiempo actual en nanosegundos 

#strptime(string, format). Convierte una cadena de caracteres que representa una fecha y hora, según un formato especificado, en una estructura de tiempo:
formated = ("%Y-%m-%d %H:%M:%S")
data_string = ("2025-11-15 13:40:30")
print(time.strptime(data_string,formated))

#strftime(format, t). Convierte una estructura de tiempo a una cadena de caracteres según el formato especificado: 
t = time.localtime() 
print(time.strftime("%Y-%m-%d %H:%M:%S", t)) # Fecha y hora formateada como cadena 

#tzset(). Asegura que la zona horaria esté configurada correctamente para la ejecución del script: 
time.tzset() # Establece la zona horaria 


#El módulo time de Python no tiene clases definidas, ya que está diseñado principalmente para trabajar 
#con funciones relacionadas con el tiempo (como obtener el tiempo actual, dormir, etc.). 



#Variables del módulo time

#time.altzone. Representa la diferencia en segundos entre la hora local estándar y la hora local de verano (si aplica):
print(time.altzone) # Muestra la diferencia en segundos de la hora de verano 

#time.daylight. Un valor booleano que indica si hay horario de verano en la zona horaria local (1 si hay horario de verano, 0 si no lo hay):
print(time.daylight) # 1 si hay horario de verano, 0 si no 

#time.timezone. Representa la diferencia en segundos entre UTC y la hora local estándar (sin tener en cuenta el horario de verano): 
print(time.timezone) # Diferencia en segundos con UTC 

#time.tzname. Una tupla que contiene los nombres de las zonas horarias estándar y de verano (si aplica). El primer valor es zona horaria estándar, y el segundo valor la zona horaria de verano (si existe):
print(time.tzname) # Tupla con el nombre de la zona horaria 



#Constantes del módulo time

#time.TIME_UTC. Representa la zona horaria UTC (Tiempo Universal Coordinado), utilizada en operaciones de tiempo y comparación: 
print(time.TIME_UTC) # Muestra la constante UTC 

#time.PERF_COUNTER. Representa un contador de alto rendimiento utilizado para medir intervalos de tiempo de alta precisión, sin preocuparse por el sistema de reloj o el ajuste de tiempo:
print(time.PERF_COUNTER) # Contador de alta precisión 


#El módulo time no tiene submódulos. Todo lo que ofrece está contenido dentro del propio módulo

