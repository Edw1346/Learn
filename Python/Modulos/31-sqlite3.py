import sqlite3

"""El módulo sqlite3 en Python permite interactuar con bases de datos SQLite, que son bases de datos ligeras y almacenadas en 
archivos locales. SQLite es ideal para aplicaciones pequeñas y medianas donde no se necesita un servidor de base de datos completo."""



"""Funciones del módulo sqlite3"""

#connect(database[, timeout, detect_types, isolation_level, check_same_thread, factory, cached_statements])
#Establece una conexión a la base de datos SQLite. Si la base de datos no existe, se crea. Uso: 
conn = sqlite3.connect('mi_base_de_datos.db') 

#complete_statement(sql)
#Verifica si una sentencia SQL está completa, es decir, si puede ejecutarse sin error. Uso: 
is_complete = sqlite3.complete_statement("SELECT * FROM usuarios;") 

#dbapi2
#Este submódulo implementa la interfaz DB-API 2.0 de Python para bases de datos. Proporciona una interfaz estándar para interactuar con bases de datos. Uso: No se usa directamente, pero se refiere a las clases y métodos estándar de la API de bases de datos.

#register_adapter(type, callable)
#Permite registrar una función de adaptación para convertir tipos de Python a tipos que pueden ser utilizados en SQLite. Uso: 
def adapt_date(val): 
    return val.isoformat() 
sqlite3.register_adapter(datetime.date, adapt_date) 

#register_converter(type, callable)
#Permite registrar una función de conversión para convertir datos de SQLite de vuelta a un tipo de Python. Uso: 
def convert_date(val):
    return datetime.date.fromisoformat(val.decode()) 
sqlite3.register_converter("DATE", convert_date) 

#normalize_function(func)
#Normaliza una función personalizada para que se pueda utilizar dentro de una sentencia SQL como función definida por el usuario. Uso:
def add(x, y): 
    return x + y
sqlite3.normalize_function(add) 



"""Clases del módulo sqlite3"""

#Connection
#Representa una conexión abierta a una base de datos SQLite. A través de esta clase, puedes ejecutar consultas SQL, crear cursors, manejar transacciones, y cerrar la conexión.
#Métodos comunes: 
#cursor() - Crea un objeto Cursor que se puede usar para ejecutar sentencias SQL.
#commit() - Confirma las transacciones pendientes.
#close() - Cierra la conexión a la base de datos.
#rollback() - Revierte las transacciones no confirmadas. Ejemplo: 
conn = sqlite3.connect('mi_base_de_datos.db') 

#Cursor
#Se utiliza para ejecutar sentencias SQL a través de una conexión. Los cursores permiten interactuar con la base de datos, ejecutar consultas y recuperar resultados.
#Métodos comunes: 
#execute() - Ejecuta una sentencia SQL.
#fetchall() - Recupera todas las filas del resultado de una consulta.
#fetchone() - Recupera una sola fila del resultado.
#fetchmany(n) - Recupera n filas del resultado. Ejemplo:
conn = sqlite3.connect('mi_base_de_datos.db') 
cursor = conn.cursor() 
cursor.execute('SELECT * FROM usuarios') 
rows = cursor.fetchall() 

#Row
#Es una clase que permite acceder a las columnas de una fila de resultados por nombre o índice. Esta clase facilita el trabajo con los resultados de las consultas SQL.
#Métodos comunes: 
#Acceso a los valores por índice o por nombre de columna. Ejemplo: 
conn = sqlite3.connect('mi_base_de_datos.db') 
conn.row_factory = sqlite3.Row # Utiliza Row para acceder por nombre de columna 
cursor = conn.cursor() 
cursor.execute('SELECT * FROM usuarios') 
row = cursor.fetchone() 
print(row['nombre']) # Acceder a una columna por nombre 

#Statement (en versiones más antiguas)
#Representa una sentencia SQL preparada. En algunas versiones más antiguas de sqlite3, esta clase se usaba para manejar sentencias SQL precompiladas, pero ha sido reemplazada por Cursor en las versiones más recientes de Python. Ejemplo: El uso de Statement es menos común en versiones actuales.



"""El módulo sqlite3 en Python no tiene variables globales específicas de alto nivel, pero sí tiene algunas variables 
internas y de configuración que se utilizan para ajustar el comportamiento del módulo y las conexiones con bases de datos."""

#sqlite3.version
#Esta variable contiene la versión del módulo sqlite3 que está instalada en tu sistema. Uso: 
print(sqlite3.version) 

#sqlite3.sqlite_version
#Esta variable contiene la versión de la biblioteca SQLite subyacente (la versión de SQLite en la que se basa el módulo sqlite3). Uso:
print(sqlite3.sqlite_version) 

#sqlite3.threading
#Determina el comportamiento de SQLite con respecto a la concurrencia en hilos. Dependiendo de esta configuración, SQLite puede manejar múltiples hilos en la misma base de datos o puede estar limitado a un solo hilo. Uso: Generalmente no se cambia directamente, pero puede ser útil en aplicaciones multihilo.

#sqlite3.dbapi2
#Esta es una referencia a la especificación DB-API 2.0 para bases de datos, que el módulo sqlite3 implementa. Proporciona una interfaz estándar para interactuar con bases de datos en Python. Uso: 
dbapi = sqlite3.dbapi2 



"""Constantes del módulo sqlite3"""

#sqlite3.PARSE_DECLTYPES
#Esta constante se utiliza cuando se conecta a una base de datos para indicar que los tipos de datos definidos en la base de datos (por ejemplo, DATE, INTEGER) deben ser interpretados y convertidos automáticamente a sus correspondientes tipos de Python. Uso:
conn = sqlite3.connect('mi_base_de_datos.db', detect_types=sqlite3.PARSE_DECLTYPES) 

#sqlite3.PARSE_COLNAMES
#Esta constante se utiliza para indicar que los nombres de las columnas en las consultas SQL deben ser interpretados como los nombres de las columnas reales en lugar de ser considerados solo como datos de texto. Uso: 
conn = sqlite3.connect('mi_base_de_datos.db', detect_types=sqlite3.PARSE_COLNAMES) 

#sqlite3.Row
#Esta constante se utiliza para acceder a los resultados de las consultas SQL como un objeto Row. Las filas de resultados pueden ser accedidas por nombre o por índice. Uso: 
conn = sqlite3.connect('mi_base_de_datos.db') 
conn.row_factory = sqlite3.Row 
cursor = conn.cursor() 
cursor.execute('SELECT * FROM usuarios') 
row = cursor.fetchone() 
print(row['nombre']) # Acceder por nombre 

#sqlite3.Connection
#Es la constante que representa la clase Connection en el módulo sqlite3. Esta constante no se usa directamente en código normal, pero puede ser útil para la introspección de tipos. Uso: Generalmente se usa al crear una conexión: 
conn = sqlite3.connect('mi_base_de_datos.db') 
print(isinstance(conn, sqlite3.Connection)) # True 

#sqlite3.Cursor
#Es la constante que representa la clase Cursor en el módulo sqlite3. Se utiliza al crear un cursor para ejecutar consultas. Uso: También se utiliza al crear un cursor: 
conn = sqlite3.connect('mi_base_de_datos.db') 
cursor = conn.cursor() 
print(isinstance(cursor, sqlite3.Cursor)) # True 


#sqlite3.PARSE_DECLTYPES y sqlite3.PARSE_COLNAMES, que controlan cómo se interpretan los tipos y nombres de las columnas en las consultas SQL.

#sqlite3.Row, que permite trabajar con los resultados de las consultas como objetos Row accesibles por nombre de columna.

#sqlite3.Connection y sqlite3.Cursor, que son las representaciones de las clases de conexión y cursor, respectivamente.



"""Excepciones del módulo sqlite3"""

#sqlite3.DatabaseError
#Es la excepción base para todos los errores que ocurren durante el acceso o manipulación de la base de datos. Uso: 
try:
    conn = sqlite3.connect('mi_base_de_datos.db') 
    cursor = conn.cursor() 
    cursor.execute('SELECT * FROM tabla_inexistente') 
except sqlite3.DatabaseError as e: 
    print(f"Ocurrió un error en la base de datos: {e}") 

#sqlite3.DataError
#Esta excepción se lanza cuando hay un error relacionado con los datos, como un valor que no puede ser convertido o almacenado correctamente. Uso: 
try: 
    conn = sqlite3.connect('mi_base_de_datos.db') 
    cursor = conn.cursor() 
    cursor.execute("INSERT INTO usuarios (edad) VALUES (?)", ('texto',)) 
except sqlite3.DataError as e: 
    print(f"Error de datos: {e}") 

#sqlite3.IntegrityError
#Esta excepción se lanza cuando se viola una restricción de integridad en la base de datos, como una violación de clave primaria o de clave foránea. Uso: 
try: 
    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (id, nombre) VALUES (?, ?)", (1, 'Juan')) 
    cursor.execute("INSERT INTO usuarios (id, nombre) VALUES (?, ?)", (1, 'Pedro')) # Violación de clave primaria 
except sqlite3.IntegrityError as e:
    print(f"Error de integridad: {e}") 

#sqlite3.InterfaceError
#Esta excepción se lanza cuando hay un error relacionado con la interfaz entre Python y SQLite, como un intento de usar una conexión cerrada o un cursor que ya ha sido cerrado. Uso: 
try: 
    conn = sqlite3.connect('mi_base_de_datos.db') 
    conn.close() # Cerrar la conexión
    cursor = conn.cursor() # Intentar usar la conexión cerrada
except sqlite3.InterfaceError as e: 
    print(f"Error de interfaz: {e}") 

#sqlite3.OperationalError
#Se lanza cuando hay un error relacionado con la operación en la base de datos, como un error en la sintaxis SQL o una operación inválida. Uso:
try: 
    conn = sqlite3.connect('mi_base_de_datos.db') 
    cursor = conn.cursor()
    cursor.execute("SELEC * FROM usuarios") # Error de sintaxis SQL
except sqlite3.OperationalError as e: 
    print(f"Error operativo: {e}") 

#sqlite3.ProgrammingError
#Esta excepción se lanza cuando se realiza una operación SQL que es incorrecta desde el punto de vista del programa, como intentar usar un cursor después de que se haya cerrado. Uso: 
try: 
    conn = sqlite3.connect('mi_base_de_datos.db') 
    cursor = conn.cursor() 
    cursor.close() # Cerrar el cursor 
    cursor.execute('SELECT * FROM usuarios') # Intentar usar el cursor cerrado 
except sqlite3.ProgrammingError as e: 
    print(f"Error de programación: {e}") 

#sqlite3.NotFoundError (en algunas versiones)
#Se lanza cuando se intenta acceder a un archivo de base de datos que no existe o cuando no se encuentra una tabla o índice durante una consulta. Uso: 
try: 
    conn = sqlite3.connect('mi_base_de_datos_no_existente.db') 
except sqlite3.NotFoundError as e:
    print(f"Archivo no encontrado: {e}") 

#sqlite3.Timeout
#Se lanza cuando una operación en la base de datos excede el tiempo de espera (timeout) establecido.  Uso:
try: 
    conn = sqlite3.connect('mi_base_de_datos.db', timeout=1.0) 
    cursor = conn.cursor() 
    cursor.execute("SELECT * FROM usuarios") 
except sqlite3.Timeout as e:
    print(f"Tiempo de espera agotado: {e}") 

#DatabaseError: Excepción base para errores de base de datos.
#DataError: Errores relacionados con los datos.
#IntegrityError: Violaciones de restricciones de integridad.
#InterfaceError: Errores en la interfaz de conexión o cursor.
#OperationalError: Errores operacionales (como errores de sintaxis SQL).
#ProgrammingError: Errores de programación (como operaciones ilegales con cursores).
#NotFoundError: Errores al no encontrar archivos o elementos.
#Timeout: Errores de tiempo de espera agotado.


"""El módulo sqlite3 en Python no tiene submódulos. Sin embargo, dentro de él, hay algunas clases y funciones que ayudan a 
gestionar conexiones, cursores, y otros aspectos del manejo de bases de datos SQLite."""
