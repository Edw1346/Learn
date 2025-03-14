import datetime

"""El módulo datetime en Python proporciona clases para manipular fechas y horas de manera sencilla y flexible. 
Permite trabajar con fechas, horas y la diferencia entre ellas, así como formatear y parsear cadenas de texto como fechas."""

#Ejemplo de uso:
now = datetime.datetime.now()
print(now) # Crear una fecha específica 

d = datetime.date(2023, 2, 16) 
print(d) # Restar días 
delta = datetime.timedelta(days=5)
new_date = now + delta 
print(new_date) 



"""Funciones del módulo datetime"""
#datetime.datetime.now(tz=None)
#Devuelve la fecha y hora actual, con la opción de incluir la zona horaria (tz). Ejemplo:
now = datetime.datetime.now() 
print(now) 

#datetime.datetime.today()
#Devuelve la fecha y hora actual, sin zona horaria (equivalente a datetime.now() sin tz). Ejemplo:
today = datetime.datetime.today() 
print(today) 

#datetime.datetime.utcnow()
#Devuelve la fecha y hora actual en formato UTC (sin zona horaria). Ejemplo:
utc_now = datetime.datetime.utcnow() 
print(utc_now) 

#datetime.datetime.fromtimestamp(timestamp, tz=None)
#Convierte un valor de timestamp (segundos desde la época Unix) en una fecha y hora local. Ejemplo:
timestamp = 1676900000 
date_time = datetime.datetime.fromtimestamp(timestamp) 
print(date_time) 

#datetime.datetime.utcfromtimestamp(timestamp)
#Convierte un valor de timestamp a una fecha y hora en formato UTC. Ejemplo:
utc_date_time = datetime.datetime.utcfromtimestamp(1676900000) 
print(utc_date_time) 

#datetime.datetime.strptime(date_string, format)
#Convierte una cadena de texto que representa una fecha y hora en un objeto datetime según el formato especificado. Ejemplo:
date_string = "2023-02-16 14:00" 
date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M") 
print(date_obj) 

#datetime.datetime.strftime(format)
#Convierte un objeto datetime en una cadena de texto según el formato especificado. Ejemplo:
date = datetime.datetime.now() 
formatted_date = date.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date) 

#datetime.date.today()
#Devuelve la fecha actual (sin la hora). Ejemplo:
today_date = datetime.date.today() 
print(today_date) 

#datetime.date.fromtimestamp(timestamp)
#Convierte un valor de timestamp a una fecha (sin la hora). Ejemplo:
date_from_timestamp = datetime.date.fromtimestamp(1676900000) 
print(date_from_timestamp) 

#datetime.date.fromisoformat(date_string)
#Convierte una cadena en formato ISO 8601 (YYYY-MM-DD) a un objeto date. Ejemplo:
date_from_iso = datetime.date.fromisoformat("2023-02-16")
print(date_from_iso) 

#datetime.date.today() Devuelve la fecha actual. Ejemplo:
today = datetime.date.today()
print(today) 

#datetime.time(hour=0, minute=0, second=0, microsecond=0)
#Crea un objeto time con la hora, minuto, segundo y microsegundo especificados. Ejemplo:
time_obj = datetime.time(14, 30, 0) 
print(time_obj) 

#datetime.time.fromisoformat(time_string)
#Convierte una cadena en formato ISO 8601 (HH:MM:SS.mmmmmm) a un objeto time. Ejemplo:
time_from_iso = datetime.time.fromisoformat("14:30:00") 
print(time_from_iso) 

#datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
#Crea un objeto timedelta que representa una diferencia de tiempo. Ejemplo:
delta = datetime.timedelta(days=5, hours=2) 
print(delta) 

#datetime.tzinfo
#Clase base para la manipulación de zonas horarias. Generalmente no se usa directamente, pero se utiliza para definir objetos de zona horaria personalizados. Ejemplo:
from datetime import tzinfo 
class MyTimezone(tzinfo): 
    def utcoffset(self, dt):
        return datetime.timedelta(hours=2) 




"""Clases del módulo datetime"""

#Principales clases de datetime:
#datetime.datetime: Representa una fecha y hora combinadas.
#datetime.date: Representa solo una fecha (sin la hora).
#datetime.time: Representa solo una hora (sin la fecha).
#datetime.timedelta: Representa la diferencia entre dos fechas u horas.
#datetime.tzinfo: Clase base para la manipulación de zonas horarias (aunque rara vez se usa directamente).

#datetime.datetime
#Representa una fecha y hora combinadas, con microsegundos. Es la clase más completa y la que se usa comúnmente para trabajar con fechas y horas. Ejemplo:
now = datetime.datetime.now() 
print(now) # Fecha y hora actuales 

#datetime.date
#Representa una fecha (año, mes, día) sin la parte de la hora. Permite obtener y manipular fechas. Ejemplo:
today = datetime.date.today() 
print(today) # Fecha actual 

#datetime.time Representa una hora (hora, minuto, segundo, microsegundo) sin la parte de la fecha. Ejemplo:
t = datetime.time(14, 30, 0) 
print(t) # 14:30:00 

#datetime.timedelta
#Representa una duración o diferencia entre dos fechas u horas. Se utiliza para realizar operaciones de suma y resta con fechas y horas. Ejemplo:
delta = datetime.timedelta(days=5) 
print(delta) # Duración de 5 días 

#datetime.tzinfo
#Es la clase base para manejar zonas horarias. Generalmente se extiende para crear clases que gestionan zonas horarias personalizadas. Ejemplo:
from datetime import tzinfo 
class MyTimezonee(tzinfo): 
    def utcoffset(self, dt): 
        return datetime.timedelta(hours=2) 




"""Variables del módulo datetime"""

#datetime.Resolution
#Es la menor unidad de tiempo soportada por los objetos datetime. Normalmente, se refiere a microsegundos (1e-6 segundos). Ejemplo:
print(datetime.Resolution) # 0:00:00.000001 





"""Constantes del módulo datetime"""
#datetime.MAXYEAR
#Define el valor máximo permitido para el año (9999). Ejemplo:
print(datetime.MAXYEAR) # 9999 

#datetime.MINYEAR
#Define el valor mínimo permitido para el año (1). Ejemplo:
print(datetime.MINYEAR) # 1 





"""Excepciones del módulo datetime"""

#datetime.dateError
#Excepción base para errores relacionados con la clase date. No es comúnmente usada directamente, pero es una excepción general relacionada con los errores de las fechas. Ejemplo:
try: 
    invalid_date = datetime.date(2023, 13, 25) # Mes no válido 
except ValueError as e: 
    print(f"Error: {e}") 

#datetime.ValueError
#Se lanza cuando se da un valor inválido al intentar crear un objeto datetime, date, o time. Ejemplo:
try: 
    invalid_time = datetime.time(25, 0) # Hora fuera de rango 
except ValueError as e:
    print(f"Error: {e}") # Error: hour must be in 0..23 

#datetime.TypeError
#Se lanza cuando se pasa un tipo incorrecto a una función o método del módulo datetime. Ejemplo:
try: 
    invalid_type = datetime.datetime.now("invalid") # Argumento no válido
except TypeError as e: 
    print(f"Error: {e}") # Error: not enough arguments 





"""El módulo datetime en Python no tiene submódulos como tal, ya que es un módulo único que proporciona clases y
funciones para trabajar con fechas y horas. Sin embargo, dentro del propio módulo, puedes encontrar varias clases y 
funciones, que pueden parecer submódulos, pero no son submódulos verdaderos."""



