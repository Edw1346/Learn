"""Manejo de Fechas y Horas en Python"""

"""En Python, se utilizan principalmente dos módulos para trabajar con fechas y horas:
datetime: Es el módulo estándar en Python para manejar fechas y horas.
time: Este módulo proporciona funciones relacionadas con el tiempo, como convertir tiempos a diferentes formatos, pausas, etc."""

"""1. Módulo datetime
El módulo datetime es el más utilizado para trabajar con fechas y horas en Python. Este módulo ofrece clases y métodos para realizar operaciones con fechas y horas, tales como la obtención de la fecha actual, la creación de nuevas fechas, la comparación de fechas, el cálculo de diferencias, y la conversión entre formatos.

Clases principales del módulo datetime:
datetime.datetime: Representa tanto la fecha como la hora.

datetime.date: Representa solo la fecha (sin hora).
datetime.time: Representa solo la hora (sin fecha).
datetime.timedelta: Representa la diferencia entre dos fechas o tiempos.
datetime.tzinfo: Maneja la información sobre zonas horarias (se usa menos frecuentemente)."""

#Obtención de la fecha y hora actual:
import datetime 
# Fecha y hora actuales 
fecha_y_hora = datetime.datetime.now() 
print(fecha_y_hora) # Solo la fecha actual
fecha_actual = datetime.date.today()
print(fecha_actual) # Solo la hora actual 
hora_actual = datetime.datetime.now().time() 
print(hora_actual) 

#Creación de un objeto datetime específico:
# Crear un objeto datetime específico
fecha_hora = datetime.datetime(2025, 1, 27, 12, 30, 45) 
print(fecha_hora) 

#Operaciones con fechas:
#Restar dos fechas:
# Crear fechas 
fecha1 = datetime.datetime(2025, 1, 1) 
fecha2 = datetime.datetime(2025, 1, 27) 
# Diferencia entre fechas 
diferencia = fecha2 - fecha1 
print(diferencia) # Resultado: 26 días 

#Sumar o restar días con timedelta:
# Crear un timedelta de 5 días 
delta = datetime.timedelta(days=5) # Sumar 5 días a la fecha actual 
fecha_futura = datetime.datetime.now() + delta 
print(fecha_futura) 

#Formateo y análisis de cadenas de fecha y hora:
#Convertir una fecha a cadena (formatear):
# Formatear fecha y hora a cadena 
fecha_formateada = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
print(fecha_formateada) 

#Convertir una cadena a fecha:
# Convertir una cadena a un objeto datetime 
fecha_str = '2025-01-27 12:30:45' 
fecha_obj = datetime.datetime.strptime(fecha_str, '%Y-%m-%d %H:%M:%S') 
print(fecha_obj) 

"""2. Módulo time
El módulo time se utiliza principalmente para trabajar con el tiempo en términos de segundos desde la "época" (1 de enero de 1970 en la mayoría de los sistemas)."""

#Obtener la hora actual en segundos:
import time 
# Obtener la hora actual en segundos desde la época 
hora_actual_segundos = time.time()
print(hora_actual_segundos) 

#Convertir segundos a formato legible:

# Convertir segundos desde la época a un formato legible 
hora_legible = time.ctime(hora_actual_segundos)
print(hora_legible) 

#Pausar la ejecución del programa:
# Pausar la ejecución del programa durante 3 segundos 
time.sleep(3) 
print("Han pasado 3 segundos.") 

"""3. Manejo de Zonas Horarias (con pytz)
Python no incluye soporte completo para zonas horarias en el módulo datetime por defecto, pero puedes usar la librería externa pytz para gestionar zonas horarias."""
#pip install pytz 

import datetime 
import pytz 
# Obtener la zona horaria local
zona_local = pytz.timezone('America/New_York') 
# Obtener la fecha y hora actual en la zona horaria local 
fecha_local = datetime.datetime.now(zona_local)
print(fecha_local) # Convertir entre zonas horarias 
zona_utc = pytz.utc
fecha_utc = fecha_local.astimezone(zona_utc) 
print(fecha_utc) 

"""4. Buenas Prácticas en el Manejo de Fechas y Horas
Usa datetime siempre que sea posible: Para la mayoría de las operaciones con fechas y horas, datetime es el módulo más adecuado.
Evita el uso de time a menos que trabajes con tiempos en segundos: El módulo time es útil para algunos casos, como medir el tiempo de ejecución o pausar el programa, pero es menos adecuado para trabajar con fechas y horas completas.
Siempre usa zonas horarias: Si tu aplicación maneja fechas y horas que podrían provenir de diferentes zonas horarias, siempre usa la librería pytz para evitar problemas con la conversión entre zonas horarias.
Formatea y analiza las fechas correctamente: Siempre que trabajes con cadenas de fecha, asegúrate de usar los formatos correctos para evitar errores de conversión."""


"""El módulo datetime de Python es una de las herramientas más poderosas para trabajar con fechas y horas. Está diseñado para proporcionar tipos de datos para representar fechas, horas, intervalos de tiempo y zonas horarias. Aquí te explico a fondo los conceptos clave y las funcionalidades de este módulo."""

"""1. Clases principales en el módulo datetime
El módulo datetime está compuesto por varias clases que permiten trabajar con fechas, horas y sus combinaciones. Las clases más importantes son:

1.1 datetime.datetime
Esta clase representa tanto la fecha como la hora (es decir, una combinación de ambos). Tiene muchos métodos útiles para manipular y formatear fechas y horas.

Métodos principales:
now(): Devuelve la fecha y hora actuales.
today(): Devuelve solo la fecha actual (sin la hora).
fromtimestamp(timestamp): Convierte un timestamp (segundos desde la época) en un objeto datetime.
strftime(format): Formatea un objeto datetime en una cadena de texto según un formato especificado.Ejemplo:"""

import datetime 
# Fecha y hora actuales 
fecha_y_hora = datetime.datetime.now() 
print(fecha_y_hora) # Ejemplo de salida: 2025-01-27 14:55:35.564798 
# Formato personalizado de la fecha y hora 
fecha_formateada = fecha_y_hora.strftime('%Y-%m-%d %H:%M:%S') 
print(fecha_formateada) # Ejemplo de salida: 2025-01-27 14:55:35 

"""1.2 datetime.date
La clase date representa solo la fecha (año, mes, día) y no contiene información sobre la hora. Es útil cuando solo necesitas trabajar con fechas sin preocuparte por el tiempo.
Métodos principales:
today(): Devuelve la fecha actual.
fromisoformat(date_string): Convierte una cadena en formato ISO (YYYY-MM-DD) en un objeto date.
weekday(): Devuelve el día de la semana como un número (0=lunes, 6=domingo). Ejemplo:"""
import datetime 
# Obtener la fecha actual 
fecha_actual = datetime.date.today() 
print(fecha_actual) # Ejemplo de salida: 2025-01-27 
# Obtener el día de la semana (lunes=0, domingo=6) 
dia_semana = fecha_actual.weekday() 
print(dia_semana) # Ejemplo de salida: 0 (lunes) 

"""1.3 datetime.time
La clase time representa solo la hora (hora, minuto, segundo, microsegundo), sin ninguna referencia a la fecha.
Métodos principales:
isoformat(): Devuelve la hora en formato ISO (HH:MM:SS.mmmmmm).
replace(hour, minute, second, microsecond): Crea una nueva instancia de time con los valores modificados. Ejemplo:"""
import datetime 
# Crear un objeto time específico 
hora = datetime.time(14, 30, 45)
print(hora) # Ejemplo de salida: 14:30:45 
# Reemplazar la hora
nueva_hora = hora.replace(minute=45) 
print(nueva_hora) # Ejemplo de salida: 14:45:45 

"""1.4 datetime.timedelta
La clase timedelta representa una diferencia entre dos fechas u horas. Se puede usar para realizar cálculos con fechas y horas, como sumar o restar días, horas, minutos, etc.
Métodos principales:
total_seconds(): Devuelve el total de la diferencia en segundos.
days, seconds, microseconds: Accede a los diferentes componentes de la diferencia. Ejemplo:"""
import datetime 
# Crear un objeto timedelta 
delta = datetime.timedelta(days=5, hours=3) 
# Sumar un timedelta a la fecha actual 
nueva_fecha = datetime.datetime.now() + delta 
print(nueva_fecha) # Ejemplo de salida: 2025-02-01 17:30:00.562918
# Restar un timedelta 
nueva_fecha = datetime.datetime.now() - delta 
print(nueva_fecha) # Ejemplo de salida: 2025-01-22 11:30:00.562918 

"""1.5 datetime.tzinfo (y pytz)
La clase tzinfo es una clase base para trabajar con información sobre zonas horarias. Sin embargo, esta clase no proporciona una implementación real de la zona horaria. Si necesitas trabajar con zonas horarias completas, puedes usar la librería externa pytz. Ejemplo con pytz:"""
import datetime 
import pytz 
# Definir una zona horaria 
zona = pytz.timezone('America/New_York') 

# Obtener la fecha y hora actual en una zona horaria específica
fecha_con_zona = datetime.datetime.now(zona) 
print(fecha_con_zona) # Ejemplo de salida: 2025-01-27 14:55:35-05:00 

"""2. Operaciones con datetime
Comparar fechas y horas
Las fechas y horas en Python son objetos comparables. Puedes usar operadores como <, >, ==, etc., para comparar objetos datetime, date, y time."""
import datetime 
# Crear dos fechas 
fecha1 = datetime.datetime(2025, 1, 27, 14, 30) 
fecha2 = datetime.datetime(2025, 1, 28, 10, 00) # Comparar fechas 
print(fecha1 < fecha2) # True
print(fecha1 == fecha2) # False 

"""2.2 Restar fechas (timedelta)
Cuando restas dos fechas o dos objetos datetime, obtienes un objeto timedelta, que representa la diferencia entre las fechas."""
import datetime 
# Crear dos fechas 
fecha1 = datetime.datetime(2025, 1, 1) 
fecha2 = datetime.datetime(2025, 1, 27) # Calcular la diferencia 
diferencia = fecha2 - fecha1 
print(diferencia) # Ejemplo de salida: 26 days, 0:00:00 

"""2.3 Sumar o restar fechas usando timedelta
Puedes sumar o restar un objeto timedelta a un objeto datetime."""
import datetime 
# Crear una fecha y un timedelta
fecha = datetime.datetime(2025, 1, 27) 
delta = datetime.timedelta(days=5) 
# Sumar días 
fecha_futura = fecha + delta 
print(fecha_futura) # Ejemplo de salida: 2025-02-01 00:00:00
# Restar días
fecha_pasada = fecha - delta 
print(fecha_pasada) # Ejemplo de salida: 2025-01-22 00:00:00 

"""3. Formateo de Fechas y Horas
El módulo datetime permite formatear objetos datetime, date, y time a cadenas de texto en cualquier formato que necesites. El método strftime(format) es muy útil para convertir un objeto datetime en una cadena de texto con un formato específico.

Formatos comunes:
%Y: Año con 4 dígitos (e.g., 2025)
%m: Mes con 2 dígitos (e.g., 01, 02)
%d: Día del mes con 2 dígitos (e.g., 01, 02)
%H: Hora en formato de 24 horas (e.g., 00, 13)
%M: Minutos (e.g., 00, 45)
%S: Segundos (e.g., 00, 59) Ejemplo:"""
import datetime 
fecha = datetime.datetime(2025, 1, 27, 14, 30) 
# Formatear la fecha 
fecha_formateada = fecha.strftime('%Y-%m-%d %H:%M:%S') 
print(fecha_formateada) # Ejemplo de salida: 2025-01-27 14:30:00 





"""El módulo time de Python proporciona funciones relacionadas con el tiempo, en particular con la manipulación y medición del tiempo en términos de segundos desde la época (la "época" es generalmente el 1 de enero de 1970, también conocido como "Unix time"). Este módulo es útil para medir intervalos de tiempo, controlar la ejecución del programa, trabajar con el reloj del sistema y manipular tiempos a un nivel bajo.

1. Funciones del módulo time

1.1 time.time()
Devuelve el tiempo actual en segundos desde la "época" (el 1 de enero de 1970), como un número flotante. Es útil para medir intervalos de tiempo. Ejemplo:"""
import time
# Obtener el tiempo actual en segundos desde la época 
tiempo_actual = time.time() 
print(tiempo_actual) # Ejemplo de salida: 1674884537.348393 

"""1.2 time.sleep(seconds)
Esta función detiene la ejecución del programa durante el número de segundos especificado. Puede ser útil cuando deseas introducir pausas en un programa, como en la simulación de un proceso o en la ejecución de pruebas. Ejemplo:"""
import time 
print("Inicio del proceso.")
time.sleep(3) # Pausar la ejecución durante 3 segundos 
print("Fin del proceso después de 3 segundos.") 

"""1.3 time.ctime(seconds)
Convierte un número de segundos desde la época en una cadena de texto legible (por ejemplo, "Wed Jan 27 12:45:03 2025"). Si no se pasa un argumento, convierte el tiempo actual. Ejemplo:"""
import time 
# Convertir el tiempo actual en segundos desde la época 
tiempo_segundos = time.time() 
# Convertir los segundos a una cadena legible 
hora_legible = time.ctime(tiempo_segundos) 
print(hora_legible) # Ejemplo de salida: "Mon Jan 27 12:45:03 2025" 

"""1.4 time.localtime(seconds)
Convierte el tiempo en segundos desde la época en una estructura time.struct_time, que contiene los componentes de la fecha y hora (como el año, mes, día, hora, minuto, segundo, etc.). Ejemplo:"""
import time 
# Convertir los segundos actuales a una estructura time 
tiempo_struct = time.localtime(time.time())
print(tiempo_struct) # Ejemplo de salida: time.struct_time(tm_year=2025, tm_mon=1, tm_mday=27, tm_hour=12, tm_min=45, tm_sec=3, tm_wday=0, tm_yday=27, tm_isdst=0) 

"""1.5 time.gmtime(seconds)
Similar a localtime(), pero convierte el tiempo en segundos desde la época en una estructura time.struct_time en formato UTC (tiempo universal coordinado), sin tener en cuenta las zonas horarias locales. Ejemplo:"""
import time 
# Convertir los segundos actuales a UTC 
tiempo_utc = time.gmtime(time.time()) 
print(tiempo_utc) # Ejemplo de salida: time.struct_time(tm_year=2025, tm_mon=1, tm_mday=27, tm_hour=17, tm_min=45, tm_sec=3, tm_wday=0, tm_yday=27, tm_isdst=0) 

"""1.6 time.mktime(t)
Convierte una estructura time.struct_time en segundos desde la época. Es lo opuesto a localtime() o gmtime(). Ejemplo:"""
import time 

# Crear una estructura time con una fecha y hora específica 
struct_time = time.localtime(time.time()) # Obtenemos el tiempo actual 
# Convertir la estructura time a segundos desde la época 
segundos = time.mktime(struct_time) 
print(segundos) # Ejemplo de salida: 1674884537.348393 

"""1.7 time.strftime(format, t)
Convierte un objeto time.struct_time (obtenido con localtime() o gmtime()) a una cadena de texto en un formato específico.
%Y: Año con 4 dígitos.
%m: Mes con 2 dígitos.
%d: Día del mes con 2 dígitos.
%H: Hora en formato de 24 horas.
%M: Minuto.
%S: Segundo.
%A: Nombre completo del día.
%B: Nombre completo del mes.  Ejemplo:"""
import time
# Obtener la hora actual 
struct_time = time.localtime(time.time()) # Formatear la hora a una cadena legible 
hora_formateada = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
print(hora_formateada) # Ejemplo de salida: "2025-01-27 12:45:03" 

"""1.8 time.strptime(string, format)
Convierte una cadena que representa una fecha y hora a un objeto time.struct_time, según el formato especificado. Ejemplo:"""
import time
# Cadena de fecha y hora 
fecha_str = "2025-01-27 12:45:03" 
# Convertir la cadena a una estructura time 
fecha_struct = time.strptime(fecha_str, "%Y-%m-%d %H:%M:%S") 
print(fecha_struct) # Ejemplo de salida: time.struct_time(tm_year=2025, tm_mon=1, tm_mday=27, tm_hour=12, tm_min=45, tm_sec=3, tm_wday=0, tm_yday=27, tm_isdst=-1) 

"""1.9 time.perf_counter()
Devuelve un contador de alta resolución (en segundos) que se puede usar para medir el tiempo de ejecución de pequeñas secciones del código, especialmente útil para benchmarking. Ejemplo:"""
import time 
# Medir el tiempo de ejecución de un proceso 
inicio = time.perf_counter() # Simulación de un proceso
time.sleep(2) 
fin = time.perf_counter()
print(f"Tiempo transcurrido: {fin - inicio} segundos") 

"""1.10 time.process_time()
Devuelve el tiempo de CPU (en segundos) utilizado por el proceso, lo que es útil para medir el rendimiento de un programa sin estar afectado por las pausas o esperas externas. Ejemplo:"""
import time 
# Medir el tiempo de CPU usado por el proceso
inicio = time.process_time() # Simulación de un proceso
time.sleep(2) 
fin = time.process_time()
print(f"Tiempo de CPU utilizado: {fin - inicio} segundos") 

"""2. Buenas Prácticas al Usar time"""
"""Evita usar time para operaciones de fecha y hora: Para tareas más complejas que involucren fechas y horas (como comparar fechas o agregar días), utiliza el módulo datetime en lugar de time.
Usa time.sleep() con moderación: Si bien es útil para introducir retrasos en un programa, usarlo en exceso puede hacer que el código sea lento y menos eficiente.
Usa time.perf_counter() para medir el tiempo de ejecución: Si deseas medir con precisión el tiempo que tarda un 

segmento del código, perf_counter() es más preciso y confiable que otras funciones como time.time().

Medir el rendimiento con time.perf_counter(): Si necesitas medir el rendimiento o la duración de un fragmento de código, siempre utiliza time.perf_counter() en lugar de time.time(). Esto se debe a que perf_counter() proporciona la mayor precisión posible para medir el tiempo de ejecución. Ejemplo:"""
import time
inicio = time.perf_counter() # Código que deseas medir 
time.sleep(2) 
fin = time.perf_counter() 
print(f"Tiempo de ejecución: {fin - inicio} segundos") 

"""Evita el uso excesivo de time.sleep(): Aunque time.sleep() es útil para simular retrasos o pausas en tu código, un uso excesivo puede hacer que tu programa sea menos eficiente. En su lugar, busca soluciones basadas en eventos o temporizadores si necesitas que tu código espere sin detenerse por completo.

Usa time.time() para medir intervalos largos: Para medir intervalos de tiempo a gran escala (como la duración de un proceso o el tiempo transcurrido entre dos eventos en tu programa), puedes utilizar time.time(). Sin embargo, para mediciones de tiempo muy pequeñas, es mejor optar por time.perf_counter().

No confundas el tiempo local con UTC: Cuando trabajes con tiempos y zonas horarias, ten en cuenta que time.localtime() y time.gmtime() devuelven la hora local y la hora en formato UTC, respectivamente. Asegúrate de usar la función correcta según tus necesidades. Ejemplo:"""
import time # Hora local 
hora_local = time.localtime()
print("Hora local:", time.strftime("%Y-%m-%d %H:%M:%S", hora_local)) # Hora en UTC 
hora_utc = time.gmtime() 
print("Hora UTC:", time.strftime("%Y-%m-%d %H:%M:%S", hora_utc)) 

"""Uso de time.ctime() para formatos legibles: Cuando necesites mostrar un timestamp en un formato legible, usa time.ctime(). No es tan flexible como strftime(), pero es una forma rápida de obtener una cadena legible de un timestamp. Ejemplo:"""
import time 
print("Tiempo actual:", time.ctime()) 

"""Convierte fechas a estructuras time.struct_time con time.strptime(): Si recibes una fecha en formato de cadena (como una entrada del usuario o un archivo) y necesitas manipularla, utiliza time.strptime() para convertirla en una estructura struct_time que puedas usar para operaciones con fechas y horas. Ejemplo:"""
import time 
fecha_str = "2025-01-27 14:30:00" 
fecha_struct = time.strptime(fecha_str, "%Y-%m-%d %H:%M:%S") 
print(fecha_struct) # Ejemplo de salida: time.struct_time(tm_year=2025, tm_mon=1, tm_mday=27, tm_hour=14, tm_min=30, tm_sec=0, tm_wday=0, tm_yday=27, tm_isdst=-1) 

"""Preferir time.mktime() para conversiones de struct_time a segundos: Si trabajas con estructuras struct_time y necesitas obtener el número de segundos desde la época, usa time.mktime(). Asegúrate de que la estructura time.struct_time esté en el formato correcto para evitar errores de conversión. Ejemplo:"""
import time 
# Crear una estructura time con fecha específica
fecha_struct = time.localtime(time.time()) 
segundos = time.mktime(fecha_struct) 
print(segundos) # Ejemplo de salida: 1674884537.348393 

"""Técnicas Útiles con el Módulo time"""
"""Medir el tiempo de ejecución de un bloque de código (benchmarking): Si deseas medir cuán eficiente es un fragmento de código, usa time.perf_counter() antes y después de la ejecución del bloque de código.

Técnica de medición de rendimiento:"""
import time 
start = time.perf_counter() # Bloque de código cuya duración deseas medir 
for _ in range(1000000):
    pass 

end = time.perf_counter() 
print(f"Duración del bloque de código: {end - start} segundos") 

"""Programación basada en temporizadores o alarmas: Si deseas ejecutar un código en intervalos regulares sin bloquear el hilo principal del programa, puedes usar un temporizador o alarma con time.sleep() o utilizar bibliotecas como sched para programar eventos. Ejemplo usando time.sleep():"""
import time 
def evento_periodico(): 
    print("Este mensaje aparece cada 5 segundos.") 
    while True:
        evento_periodico() 
    time.sleep(5) # Esperar 5 segundos antes de ejecutar nuevamente 

"""Trabajar con múltiples zonas horarias: Si tu aplicación necesita soportar múltiples zonas horarias, puedes usar el módulo time junto con time.localtime() o time.gmtime(), y también considerar la librería pytz para manejar zonas horarias específicas de forma precisa. Ejemplo con time.gmtime():"""
import time 
# Hora UTC 
hora_utc = time.gmtime() 
print("Hora UTC:", time.strftime("%Y-%m-%d %H:%M:%S", hora_utc)) 

"""Conversión de tiempos para fechas futuras/pasadas: Si necesitas agregar o restar días, meses o años a una fecha, time no tiene funciones directas para esto. Sin embargo, puedes utilizar time.mktime() y luego hacer operaciones sobre los segundos. Técnica con time.mktime():"""
import time
# Obtener la fecha actual 
fecha_actual = time.localtime(time.time()) 
# Sumar 1 día (86400 segundos) 
fecha_futura = time.localtime(time.mktime(fecha_actual) + 86400) 
print(time.strftime("%Y-%m-%d %H:%M:%S", fecha_futura)) # Un día después de la fecha actual 

