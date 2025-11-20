import datetime 
#El módulo datetime proporciona clases para manipular fechas y horas de manera sencilla y flexible. 
#Permite trabajar con fechas, horas y la diferencia entre ellas, así como formatear y parsear cadenas de texto como fechas.

#Funciones del módulo datetime


#datetime.datetime.now(tz=None). Devuelve fecha y hora actual, con opción de incluir la zona horaria (tz):
now = datetime.datetime.now() #datetime.datetime.now()
print(now) 

#datetime.today(). Devuelve la fecha y hora actual, sin zona horaria:
today = datetime.datetime.today() 
print(today) 

#datetime.utcnow(). Devuelve la fecha y hora actual en formato UTC (sin zona horaria):
utc_now = datetime.datetime.utcnow() 
print(utc_now) 

#datetime.fromtimestamp(timestamp, tz=None) Convierte un valor de timestamp (segundos desde la época Unix) en una fecha y hora local:
timestamp = 1676900000 
date_time = datetime.datetime.fromtimestamp(timestamp)
print(date_time) 

#datetime.utcfromtimestamp(timestamp). Convierte un valor timestamp a fecha y hora en formato UTC:
utc_date_time = datetime.datetime.utcfromtimestamp(timestamp)
print(utc_date_time) 

#datetime.datetime.strptime(date_string, format). Convierte una cadena de texto que representa una fecha y hora en un objeto datetime según el formato especificado:
date_string = "2025-11-15 13:30"
date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M")
print(date_obj) 

#datetime.strftime(format). Convierte objeto datetime en cadena de texto según el formato especificado:
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date) 

#datetime.date.today(). Devuelve la fecha actual (sin la hora). Ejemplo:
today_date = datetime.date.today()
print(today_date) 

#datetime.date.fromtimestamp(timestamp). Convierte un valor de timestamp a una fecha (sin la hora):
date_from_timestamp = datetime.date.fromtimestamp(1676900000) 
print(date_from_timestamp) 

#datetime.date.fromisoformat(date_string). Convierte una cadena en formato ISO 8601 (YYYY-MM-DD) a un objeto date:
date_from_iso = datetime.date.fromisoformat("2023-02-16")
print(date_from_iso) 

#datetime.time(hour=0, minute=0, second=0, microsecond=0). Crea un objeto time con la hora, minuto, segundo y microsegundo especificados:
time_obj = datetime.time(14, 30, 0) 
print(time_obj) 

#datetime.time.fromisoformat(time_string). Convierte una cadena en formato ISO 8601 (HH:MM:SS.mmmmmm) a un objeto time:
time_from_iso = datetime.time.fromisoformat("14:30:00") 
print(time_from_iso) 

#datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0). Crea un objeto timedelta que representa una diferencia de tiempo. Ejemplo:
delta = datetime.timedelta(days=5, hours=2) 
print(delta) 



#Clases de datetime:
#datetime.datetime: Representa una fecha y hora combinadas.
#datetime.date: Representa solo una fecha (sin la hora).
#datetime.time: Representa solo una hora (sin la fecha).
#datetime.timedelta: Representa la diferencia entre dos fechas u horas.
#datetime.tzinfo: Clase base para la manipulación de zonas horarias (rara vez se usa directamente).


#Constantes del módulo datetime

#datetime.MAXYEAR. Define el valor máximo permitido para el año (9999):
print(datetime.MAXYEAR) # 9999 

#datetime.MINYEAR. Define el valor mínimo permitido para el año (1). Ejemplo:
print(datetime.MINYEAR) # 1 

#datetime.Resolution. Es la menor unidad de tiempo soportada por los objetos datetime. Normalmente, se refiere a microsegundos (1e-6 segundos): 
print(datetime.Resolution) # 0:00:00.000001 

#El módulo datetime no tiene submódulos, proporciona clases y funciones a trabajar con fechas y horas.

