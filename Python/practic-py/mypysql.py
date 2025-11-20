
import pymysql  # Conectar a la base de datos 

#pymysql módulo que permite interactuar con bases de datos MySQL usando el protocolo MySQL de manera nativa.

"""Características principales:
Conexión a bases de datos MySQL.
Ejecución de consultas SQL (SELECT, INSERT, UPDATE, DELETE).
Manejo de transacciones.
Compatibilidad con MySQLdb"""

#Funciones del módulo pymysql

#pymysql.connect(). Abre una conexión a MySQL.
conn = pymysql.connect(host="localhost", user="Edwin", password="Edwin1012", database="pybases", charset="utf8mb4") 
print(conn)

#pymysql.install_as_MySQLdb(). Permite usar pymysql como reemplazo de MySQLdb.
#pymysql.install_as_MySQLdb() 

#Funciones del objeto Connection

#cursor() Crea un cursor para ejecutar consultas SQL.
cursor = conn.cursor()

#Funciones del objeto Cursor

#execute(query, params=None) Ejecuta una consulta SQL.
#execute = cursor.execute("create table test_pri (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), surname VARCHAR(50), numero VARCHAR(15));")

#executemany(query, param_list) Ejecuta múltiples consultas con una lista de valores.
sql = "INSERT INTO test_pri (name, surname, numero) VALUES (%s, %s, %s)" #La consulta normal como primer parametro
#En los valores se pone %s, para que executemany agarre los datos de la tupla qque se le envia en el otro parametro
datos = [("Juan","Soto","12345678"), ("María","Carmen","87654321")] 
cursor.executemany(sql, datos) 


filasAF = cursor.rowcount()   #numero de filas afectadas por la ultima sentencia
print(filasAF)

Ultfilas = cursor.lastrowid()   #id insertado  
print(Ultfilas)

#fetchone() Obtiene la primera fila del resultado.
fila = cursor.fetchone() 
print(fila) 

#fetchall() Obtiene todas las filas del resultado.
filas = cursor.fetchall()
print(filas)
for fila in filas: print(fila)

#fetchmany(size) Obtiene un número específico de filas.
filas = cursor.fetchmany(3) # Obtiene 3 filas 

#close() Cierra el cursor.
cursor.close() 

#commit() Guarda los cambios en la base de datos.
conn.commit() 

#rollback() Revierte la última transacción.
conn.rollback() 

#close() Cierra la conexión con la base de datos.
conn.close() 

#Otras
#conn.ping(reconnect=True) comprobar conexion
#conn.begin()  iniciar transaccion explicito
#conn.autocommit(True/False)  autivar o desactivar autocommit
#conn. 
#conn. 

#cursor.callproc(sp, args=())  llamar a un stored procedure
#cursor.scroll(value, mode='relative') mover el puntero
#cursor. 
#cursor. 
#cursor. 

#Clases principales de pymysql

#pymysql.Connection Representa una conexión a la base de datos MySQL.
conn = pymysql.Connection(host="localhost", user="root", password="1234", database="mi_base") 

#pymysql.cursors.Cursor Maneja la ejecución de consultas y recuperación de datos.
cursor = conn.cursor() 

#pymysql.cursors.DictCursor Devuelve resultados como diccionarios en lugar de tuplas.
cursor = conn.cursor(pymysql.cursors.DictCursor) 

#pymysql.cursors.SSCursor Un cursor que obtiene los resultados fila por fila, útil para grandes volúmenes de datos.
cursor = conn.cursor(pymysql.cursors.SSCursor) 

#pymysql.cursors.SSDictCursor Similar a SSCursor, pero devuelve resultados en forma de diccionario.
cursor = conn.cursor(pymysql.cursors.SSDictCursor) 

#Clases de Excepciones en pymysql Estas clases manejan errores específicos de MySQL:

#pymysql.MySQLError Clase base de todas las excepciones de MySQL.
try: conn = pymysql.connect(host="localhost", user="root", password="1234", database="mi_base") 
except pymysql.MySQLError as e: print(f"Error de MySQL: {e}") 

#pymysql.OperationalError Error relacionado con la conexión o disponibilidad del servidor.
try: conn = pymysql.connect(host="localhost", user="root", password="incorrecto", database="mi_base") 
except pymysql.OperationalError as e: print(f"Error operacional: {e}") 

#pymysql.ProgrammingError Errores en la sintaxis SQL.
try: cursor.execute("SELEC * FROM usuarios") # Error en "SELECT" 
except pymysql.ProgrammingError as e: print(f"Error de programación: {e}") 

#pymysql.IntegrityError Errores por violación de restricciones de la base de datos.
try: cursor.execute("INSERT INTO usuarios (id, nombre) VALUES (1, 'Carlos')") # Suponiendo que ya existe el ID 1 
except pymysql.IntegrityError as e: print(f"Error de integridad: {e}") 

#pymysql.InternalError Errores internos del servidor MySQL.
try: cursor.execute("SHOW STATUS WHERE 'variable_name' = 'Threads_connected'")
except pymysql.InternalError as e: print(f"Error interno: {e}") 

#pymysql.DatabaseError Errores generales de la base de datos.
try: cursor.execute("DROP TABLE tabla_inexistente") 
except pymysql.DatabaseError as e: print(f"Error de base de datos: {e}") 




#Variables principales en pymysql

#pymysql.__version__ Indica la versión actual de pymysql instalada.

#pymysql.apilevel Define el nivel de compatibilidad con la API DB-API 2.0 de Python.
print(pymysql.apilevel) # Salida: '2.0' 

#pymysql.threadsafety Indica el nivel de seguridad de hilos:
#0: No seguro
#1: Uso en diferentes hilos con precaución
#2: Compartido en diferentes hilos
#3: Totalmente seguro en múltiples hilos
print(pymysql.threadsafety) # Salida: 1 

#pymysql.paramstyle Define el estilo de parámetros usados en las consultas SQL. pymysql usa el estilo format.
print(pymysql.paramstyle) # Salida: 'format' 




#Constantes de pymysql

#pymysql.constants.FIELD_TYPE Define los tipos de datos de MySQL.
import pymysql.constants
print(pymysql.constants.FIELD_TYPE.VARCHAR) # Salida: 253 
print(pymysql.constants.FIELD_TYPE.INT24) # Salida: 9 

#pymysql.constants.FLAG Define los flags de las columnas en MySQL.
print(pymysql.constants.FLAG.NOT_NULL) # Salida: 1 
print(pymysql.constants.FLAG.PRI_KEY) # Salida: 2 

#pymysql.constants.CLIENT Define los flags para la conexión del cliente.
print(pymysql.constants.CLIENT.MULTI_STATEMENTS) # Salida: 65536 
print(pymysql.constants.CLIENT.SSL) # Salida: 2048 

#pymysql.constants.ER Define códigos de error de MySQL.
print(pymysql.constants.ER.DB_CREATE_EXISTS) # Salida: 1007 
print(pymysql.constants.ER.BAD_DB_ERROR) # Salida: 1049 

#pymysql.constants.CR Define códigos de error del cliente.
print(pymysql.constants.CR.CONNECTION_ERROR) # Salida: 2002 
print(pymysql.constants.CR.SERVER_GONE_ERROR) # Salida: 2006 

#pymysql.constants.FIELD_FLAG Define flags adicionales para los campos de MySQL.
print(pymysql.constants.FIELD_FLAG.UNSIGNED) # Salida: 32 
print(pymysql.constants.FIELD_FLAG.ZEROFILL) # Salida: 64 


#Excepciones en pymysql

#pymysql.MySQLError Excepción base de la que derivan todas las demás excepciones de MySQL.
try:conn = pymysql.connect(host="localhost", user="root", password="1234", database="mi_base")
except pymysql.MySQLError as e: print(f"Error de MySQL: {e}") 

#pymysql.Warning Advertencias generadas por el servidor MySQL.
try:cursor.execute("SET sql_mode='STRICT_TRANS_TABLES'")
except pymysql.Warning as w: print(f"Advertencia: {w}") 

#pymysql.Error Clase base para los errores generales de MySQL.
try: cursor.execute("DROP DATABASE bd_inexistente") 
except pymysql.Error as e: print(f"Error en la base de datos: {e}") 

#pymysql.InterfaceError Errores en la interfaz de conexión con MySQL.
try:conn.ping(reconnect=False) # Simula un error de interfaz 
except pymysql.InterfaceError as e: print(f"Error de interfaz: {e}") 

#pymysql.DatabaseError Errores generales en la base de datos.
try:cursor.execute("DELETE FROM usuarios WHERE id = 'abc'") # ID debe ser numérico 
except pymysql.DatabaseError as e: print(f"Error de base de datos: {e}") 

#pymysql.DataError Errores relacionados con valores de datos incorrectos.
try: cursor.execute("INSERT INTO usuarios (edad) VALUES (9999999999)") # Edad demasiado grande 
except pymysql.DataError as e: print(f"Error de datos: {e}") 

#pymysql.OperationalError Errores operacionales como pérdida de conexión.
try: conn = pymysql.connect(host="localhost", user="root", password="incorrecto", database="mi_base") 
except pymysql.OperationalError as e: print(f"Error operacional: {e}") 

#pymysql.IntegrityError Errores por violación de restricciones de integridad.
try: cursor.execute("INSERT INTO usuarios (id, nombre) VALUES (1, 'Carlos')") # Si ID=1 ya existe 
except pymysql.IntegrityError as e: print(f"Error de integridad: {e}") 

#pymysql.InternalError Errores internos del servidor MySQL.
try: cursor.execute("SHOW STATUS WHERE 'variable_name' = 'Threads_connected'") 
except pymysql.InternalError as e: print(f"Error interno: {e}") 

#pymysql.ProgrammingError Errores en la sintaxis SQL o en el uso de la API.
try:cursor.execute("SELEC * FROM usuarios") # Error en "SELECT" 
except pymysql.ProgrammingError as e:print(f"Error de programación: {e}") 

#pymysql.NotSupportedError Errores cuando se usa una función no soportada.
try: cursor.execute("ALTER TABLE usuarios SET AUTOCOMMIT = 1") # No soportado en algunos casos 
except pymysql.NotSupportedError as e: print(f"Error de compatibilidad: {e}") 


#Submódulos de pymysql

#pymysql.connections Maneja la conexión a MySQL.
from pymysql.connections import Connection 
conn = Connection(host="localhost", user="root", password="1234", database="mi_base") 

#pymysql.cursors Define los diferentes tipos de cursores para ejecutar consultas SQL.
from pymysql.cursors import DictCursor 
cursor = conn.cursor(DictCursor) 

#pymysql.converters Convierte datos entre Python y MySQL.
from pymysql.converters import escape_string 
dato = "O'Reilly"
print(escape_string(dato)) # Salida: O\'Reilly 

#pymysql.constants Contiene constantes usadas en pymysql.
from pymysql.constants import FIELD_TYPE 
print(FIELD_TYPE.VARCHAR) # Salida: 253 

"""Submódulos dentro de pymysql.constants
pymysql.constants.CLIENT - Flags del cliente MySQL.
pymysql.constants.ER - Códigos de error del servidor.
pymysql.constants.FIELD_TYPE - Tipos de datos en MySQL.
pymysql.constants.FLAG - Flags de columnas.
pymysql.constants.CR - Errores del cliente MySQL.
pymysql.constants.FIELD_FLAG - Flags adicionales de campos."""

#pymysql.err Define excepciones de MySQL.
from pymysql.err import IntegrityError 
try: cursor.execute("INSERT INTO usuarios (id) VALUES (1)") # Suponiendo que el ID 1 ya existe 
except IntegrityError as e: print(f"Error de integridad: {e}") 


#Ejemplo
conexion = pymysql.connect( host="localhost", user="root", password="1234", database="mi_base" ) 
try: 
    with conexion.cursor() as cursor: 
        cursor.execute("SELECT * FROM usuarios") 
        resultados = cursor.fetchall()
        for fila in resultados:print(fila) 
finally: conexion.close() # Cerrar conexión 