import pandas

"""Pandas es una biblioteca de Python diseñada para el análisis y manipulación de datos. Permite trabajar con datos 
estructurados, como tablas (similares a hojas de cálculo o bases de datos), y facilita tareas como limpiar, transformar, 
analizar y visualizar esos datos."""

#Principales características:
#Estructuras de datos: Pandas tiene dos estructuras principales: 
#DataFrame: Una tabla bidimensional, similar a una hoja de cálculo, con filas y columnas.
#Series: Una estructura unidimensional, similar a una lista o una columna de una tabla.

#Instalación:
#pip install pandas 

#Ejemplo básico:
import pandas as pd 

#Crear un DataFrame:
data = {'Nombre': ['Carlos', 'Ana', 'Luis'], 'Edad': [23, 30, 25]} 
df = pd.DataFrame(data) 
print(df) 
#Salida: Nombre Edad 0 Carlos 23 1 Ana 30 2 Luis 25 

#Acceder a columnas:
print(df['Nombre']) # Devuelve la columna 'Nombre' 

#Filtrar datos:
adultos = df[df['Edad'] > 25] 
print(adultos) 

#Leer y escribir archivos: 
#Leer un archivo CSV:
df = pd.read_csv('archivo.csv') 

#Escribir a un archivo CSV:
df.to_csv('archivo_salida.csv', index=False) 

#Funciones comunes:
#head(): Muestra las primeras 5 filas del DataFrame.
print(df.head()) 

#describe(): Proporciona estadísticas resumidas sobre los datos numéricos.
print(df.describe()) 




"""Funciones"""

#1. Funciones de creación y lectura de datos:
#read_csv() Lee un archivo CSV y lo convierte en un DataFrame.
df = pd.read_csv('archivo.csv') 

#read_excel() Lee un archivo Excel y lo convierte en un DataFrame.
df = pd.read_excel('archivo.xlsx') 

#read_sql() Lee una consulta SQL en un DataFrame.
import sqlite3
connection = sqlite3.connect('database.db') 
df = pd.read_sql('SELECT * FROM tabla', connection) 

#read_json() Lee un archivo JSON y lo convierte en un DataFrame.
df = pd.read_json('archivo.json') 

#read_html() Lee una página HTML que contiene tablas y las convierte en una lista de DataFrames.
dfs = pd.read_html('https://www.ejemplo.com') 

#read_parquet() Lee un archivo Parquet y lo convierte en un DataFrame.
df = pd.read_parquet('archivo.parquet') 

#read_sql_table() Lee una tabla SQL y la convierte en un DataFrame.
df = pd.read_sql_table('tabla', connection) 

#read_sql_query() Lee una consulta SQL y la convierte en un DataFrame.
df = pd.read_sql_query('SELECT * FROM tabla', connection) 

#to_csv() Escribe el DataFrame en un archivo CSV.
df.to_csv('salida.csv', index=False) 

#to_excel() Escribe el DataFrame en un archivo Excel.
df.to_excel('salida.xlsx', index=False) 

#to_sql() Escribe el DataFrame en una base de datos SQL.
df.to_sql('tabla', connection, if_exists='replace', index=False) 

#to_json() Escribe el DataFrame en un archivo JSON.
df.to_json('salida.json') 

#to_html() Convierte el DataFrame a una tabla HTML.
html_table = df.to_html() 

#to_parquet() Escribe el DataFrame en un archivo Parquet.
df.to_parquet('salida.parquet') 


#2. Funciones de manipulación y transformación de datos:
#head() Devuelve las primeras n filas del DataFrame (por defecto n=5).
print(df.head()) 

#tail() Devuelve las últimas n filas del DataFrame (por defecto n=5).
print(df.tail()) 

#drop() Elimina columnas o filas del DataFrame.
df = df.drop(columns=['columna_a_eliminar']) 
df = df.drop(index=[0, 1]) 

#rename() Renombra columnas o índices.
df = df.rename(columns={'antigua_columna': 'nueva_columna'}) 

#fillna() Rellena los valores NaN con un valor específico.
df = df.fillna(0) # Rellena NaN con 0 

#dropna() Elimina las filas con valores NaN.
df = df.dropna() 

#replace() Reemplaza valores específicos en el DataFrame.
df = df.replace({1: 'uno', 2: 'dos'}) 

#apply() Aplica una función a lo largo de un eje (filas o columnas).
df['nueva_columna'] = df['columna'].apply(lambda x: x * 2) 

#map() Aplica una función elemento por elemento.
df['columna'] = df['columna'].map({'a': 1, 'b': 2}) 

#astype() Convierte el tipo de datos de una columna.
df['columna'] = df['columna'].astype('float') 

#merge() Fusiona dos DataFrames en función de una clave común.
df_merged = pd.merge(df1, df2, on='id') 

#concat() Concatena dos o más DataFrames.
df_combined = pd.concat([df1, df2]) 

#pivot() Realiza un pivot de los datos (reorganiza las columnas).
df_pivot = df.pivot(index='id', columns='fecha', values='valor') 

#melt() Convierte las columnas en filas.
df_melted = df.melt(id_vars=['id'], value_vars=['columna1', 'columna2']) 

#groupby() Agrupa los datos según una o varias columnas.
df_grouped = df.groupby('columna').sum() 


#3. Funciones estadísticas:
#describe() Genera estadísticas descriptivas del DataFrame.
print(df.describe()) 

#mean() Calcula la media de cada columna numérica.
print(df.mean()) 

#sum() Suma los valores de cada columna.
print(df.sum()) 

#count() Cuenta el número de elementos no nulos de cada columna.
print(df.count()) 

#std() Calcula la desviación estándar de cada columna numérica.
print(df.std()) 

#min() Devuelve el valor mínimo de cada columna.
print(df.min()) 

#max() Devuelve el valor máximo de cada columna.
print(df.max()) 

#corr() Calcula la correlación entre las columnas numéricas.
print(df.corr()) 


#4. Funciones de selección y filtrado:
#loc[] Selecciona un subconjunto del DataFrame por etiquetas de fila y columna.
df_selected = df.loc[df['columna'] > 5] 

#iloc[] Selecciona un subconjunto del DataFrame por posición de fila y columna.
df_selected = df.iloc[0:5, 1:3] # Filas 0-4, columnas 1-2 

#query() Filtra el DataFrame utilizando una expresión de consulta.
df_selected = df.query('columna > 5') 

#at[] Accede a un único valor en el DataFrame por fila y columna.
value = df.at[0, 'columna'] 

#iat[] Accede a un único valor en el DataFrame por índice numérico de fila y columna.
value = df.iat[0, 1] 


#5. Funciones de manejo de índices y fechas:
#set_index() Establece una o más columnas como el índice del DataFrame.
df = df.set_index('columna') 

#reset_index() Restablece el índice a los valores predeterminados.
df = df.reset_index() 

#to_datetime() Convierte una columna a tipo de dato datetime.
df['fecha'] = pd.to_datetime(df['fecha']) 

#date_range() Genera un rango de fechas.
dates = pd.date_range('2022-01-01', periods=10) 


"""Clases"""
#1. DataFrame
#La clase DataFrame es la estructura de datos principal en pandas y es utilizada para representar tablas bidimensionales, donde cada columna puede tener un tipo de dato diferente (números, cadenas, fechas, etc.). Ejemplo:
import pandas as pd 
# Crear un DataFrame 
data = {'Nombre': ['Carlos', 'Ana', 'Luis'], 'Edad': [23, 30, 25]} 
df = pd.DataFrame(data) 
print(df) 
#Métodos comunes:
#head(): Muestra las primeras filas del DataFrame.
#tail(): Muestra las últimas filas del DataFrame.
#drop(): Elimina filas o columnas.
#groupby(): Agrupa los datos según una columna.

#2. Series
#La clase Series es una estructura de datos unidimensional, similar a una lista o un arreglo. Representa una columna en un DataFrame o una secuencia de datos. Ejemplo:
import pandas as pd 
# Crear una Series
s = pd.Series([10, 20, 30, 40])
print(s) 
#Métodos comunes:
#mean(): Calcula la media de los elementos.
#sum(): Calcula la suma de los elementos.
#apply(): Aplica una función a cada elemento de la Series.

#3. Index
#La clase Index representa los índices de un DataFrame o Series, y se usa para identificar las filas o columnas en estas estructuras de datos. Es similar a una lista de etiquetas. Ejemplo:
import pandas as pd 
# Crear un índice 
index = pd.Index(['a', 'b', 'c', 'd']) 
print(index) 
#Métodos comunes:
#union(): Devuelve la unión de dos índices.
#intersection(): Devuelve la intersección de dos índices.
#difference(): Devuelve la diferencia entre dos índices.

#4. Categorical
#La clase Categorical es una estructura de datos para almacenar variables categóricas, es decir, variables con un número limitado de posibles valores. Ejemplo:
import pandas as pd
# Crear una Categorical
cat = pd.Categorical(['a', 'b', 'a', 'c', 'b'])
print(cat) 
#Métodos comunes:
#categories: Devuelve las categorías únicas.
#codes: Devuelve los códigos que representan las categorías.

#5. DatetimeIndex
#La clase DatetimeIndex es una subclase de Index que maneja fechas y horas, permitiendo realizar operaciones de fecha y hora más fácilmente. Ejemplo:
import pandas as pd 
# Crear un DatetimeIndex 
dates = pd.date_range('2022-01-01', periods=5) 
print(dates) 
#Métodos comunes:
#dayofweek: Devuelve el día de la semana.
#month: Devuelve el mes.
#year: Devuelve el año.

#6. Timedelta
#La clase Timedelta representa una diferencia de tiempo entre dos fechas. Es útil cuando se trabaja con intervalos de tiempo. Ejemplo:
import pandas as pd 
# Crear un Timedelta
delta = pd.Timedelta('2 days 3 hours') 
print(delta) 
#Métodos comunes:
#days: Devuelve los días del Timedelta.
#seconds: Devuelve los segundos del Timedelta.
#total_seconds(): Devuelve el total de segundos como un número de punto flotante.

#7. Period
#La clase Period representa un intervalo de tiempo específico, como un mes, un trimestre o un año. Es útil cuando se trabaja con datos de series temporales. Ejemplo:
import pandas as pd
# Crear un Period
period = pd.Period('2022-01', freq='M')
print(period) 
#Métodos comunes:
#start_time: Devuelve el inicio del período.
#end_time: Devuelve el final del período.

#8. MultiIndex
#La clase MultiIndex es una subclase de Index que permite tener índices jerárquicos, es decir, usar varios niveles de índices en un DataFrame. Ejemplo:
import pandas as pd 
# Crear un MultiIndex 
arrays = [['A', 'A', 'B', 'B'], [1, 2, 1, 2]] 
index = pd.MultiIndex.from_arrays(arrays, names=('letter', 'number')) 
df = pd.DataFrame({'value': [10, 20, 30, 40]}, index=index) 
print(df) 
#Métodos comunes:
#get_level_values(): Devuelve los valores de un nivel específico del índice.
#swaplevel(): Intercambia dos niveles del índice.

#9. SparseDtype
#La clase SparseDtype representa un tipo de datos disperso, útil cuando tienes muchas filas con valores nulos o repetidos. Ejemplo:
import pandas as pd 
# Crear un SparseDtype 
sparse_type = pd.SparseDtype('float', fill_value=0)
print(sparse_type) 
#Métodos comunes:
#subtype: Devuelve el tipo subyacente de los datos dispersos.


"""El módulo pandas no tiene muchas "variables" definidas explícitamente, ya que es un conjunto de herramientas que ofrece 
clases, funciones y objetos para trabajar con datos estructurados. Sin embargo, podemos hablar sobre las variables que se 
pueden usar dentro de pandas, tales como configuraciones globales, constantes y parámetros predefinidos dentro de la biblioteca."""

#1. pandas.options
#La variable options es un objeto que contiene una serie de configuraciones globales que afectan el comportamiento de pandas. Esto te permite cambiar cómo pandas maneja la salida de los datos, el formato de visualización, etc. Ejemplo:
import pandas as pd 
# Cambiar la opción de visualización de la cantidad de columnas mostradas 
pd.set_option('display.max_columns', 10) # Ver la opción actual 
print(pd.get_option('display.max_columns')) 

#2. pandas.__version__
#Esta variable contiene la versión actual del módulo pandas. Es útil cuando necesitas verificar qué versión de pandas estás usando. Ejemplo:
import pandas as pd
# Obtener la versión de pandas 
print(pd.__version__) 

#4. pandas.Timestamp.now()
#Esta variable es una función que devuelve el timestamp (marca de tiempo) actual. Se puede usar para obtener la fecha y hora actual en formato Timestamp de pandas. Ejemplo:
import pandas as pd
# Obtener la fecha y hora actual 
current_time = pd.Timestamp.now() 
print(current_time) 

#5. pandas.set_option()
#Aunque técnicamente no es una variable, la función set_option() se utiliza para configurar las opciones globales de pandas, como la forma en que se visualizan los datos, el tamaño de las columnas, etc. Ejemplo:
import pandas as pd
# Establecer la opción de visualización para la cantidad máxima de filas 
pd.set_option('display.max_rows', 10) 

#6. pandas.get_option()
#Similar a set_option(), esta función se utiliza para obtener las configuraciones actuales que pandas tiene almacenadas, como el tamaño de la ventana de visualización, el formato de fechas, etc. Ejemplo:
import pandas as pd 
# Obtener la configuración actual de pandas para el número máximo de columnas 
max_columns = pd.get_option('display.max_columns')
print(max_columns) 

#Resumen de las Variables y Constantes
#pandas.options: Contiene opciones de configuración global.
#pandas.__version__: Contiene la versión actual del módulo pandas.
#pandas.Timestamp.now(): Devuelve la marca de tiempo actual.
#pandas.set_option(): Establece las opciones de configuración global.
#pandas.get_option(): Obtiene las configuraciones globales de pandas.

 

"""Constantes definidas en el módulo pandas"""

#1. pandas.NA
#NA es una constante que representa valores nulos o faltantes en pandas, y se usa principalmente en tipos de datos que permiten valores nulos. Es más robusto que None o numpy.nan en algunos casos. Ejemplo:
import pandas as pd
# Crear un DataFrame con un valor NA
df = pd.DataFrame({'A': [1, pd.NA, 3]})
print(df) 

#2. pandas.Timedelta(0)
#Timedelta(0) representa un intervalo de tiempo de cero. Se utiliza para representar diferencias entre fechas y tiempos. Ejemplo:
import pandas as pd
# Crear un intervalo de tiempo de 0 
zero_timedelta = pd.Timedelta(0) 
print(zero_timedelta) 

#3. pandas.Timestamp
#Timestamp es una constante que representa un valor de fecha y hora. Puede usarse para trabajar con marcas de tiempo (timestamps) en pandas, y es equivalente a un objeto datetime de Python. Ejemplo:
import pandas as pd 
# Crear un Timestamp de una fecha específica
timestamp = pd.Timestamp('2025-01-01') 
print(timestamp) 

#4. pandas.DataFrame.empty
#Esta es una constante utilizada para verificar si un DataFrame está vacío o no. Devuelve un valor booleano (True o False). Ejemplo:
import pandas as pd 
# Crear un DataFrame vacío
df = pd.DataFrame() # Verificar si el DataFrame está vacío 
print(df.empty) 

#5. pandas.DataFrame.columns
#Esta constante se refiere al atributo de un DataFrame que almacena el índice de las columnas. Es una referencia directa a las etiquetas de las columnas de un DataFrame. Ejemplo:
import pandas as pd 
# Crear un DataFrame 
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}) # Acceder a las columnas 
print(df.columns) 

#6. pandas.errors.EmptyDataError
#Esta constante es una excepción utilizada para indicar que se intentó cargar un archivo vacío usando funciones como read_csv(). Ejemplo:
import pandas as pd 
from pandas.errors import EmptyDataError
try: # Intentar leer un archivo vacío
    df = pd.read_csv('archivo_vacio.csv') 
except EmptyDataError: 
    print("El archivo está vacío.") 

#7. pandas.Interval
#Interval es una constante que se utiliza para representar intervalos de datos, como un rango numérico o de fechas. Ejemplo:
import pandas as pd # Crear un intervalo
interval = pd.Interval(1, 5) 
print(interval) 

#8. pandas.DatetimeIndex
#DatetimeIndex es una constante utilizada para trabajar con índices de fechas y horas. Se utiliza especialmente en series temporales para representar las fechas en el índice de un DataFrame. Ejemplo:
import pandas as pd 
# Crear un DatetimeIndex 
dates = pd.date_range('2025-01-01', periods=5) 
print(dates) 

#9. pandas.Series.isnull() y pandas.Series.notnull()
#Estas son funciones constantes para verificar si los elementos en una Series son nulos o no. Aunque no son "constantes" literales, actúan de manera similar a constantes dentro de pandas. Ejemplo:
import pandas as pd 
# Crear una Serie con valores nulos 
s = pd.Series([1, 2, None, 4]) # Verificar si los elementos son nulos 
print(s.isnull()) # Verificar si los elementos no son nulos print(s.notnull()) 


#pandas.NA: Representa valores nulos.
#pandas.Timedelta(0): Intervalo de tiempo de cero.
#pandas.Timestamp: Marca de tiempo para representar fechas y horas.
#pandas.DataFrame.empty: Verifica si un DataFrame está vacío.
#pandas.DataFrame.columns: Refleja el índice de las columnas de un DataFrame.
#pandas.errors.EmptyDataError: Excepción para archivos vacíos.
#pandas.Interval: Representa intervalos de datos.
#pandas.DatetimeIndex: Índice de fechas y horas.
#pandas.Series.isnull() y pandas.Series.notnull(): Métodos para verificar valores nulos o no nulos.



"""El módulo pandas define varias excepciones que se pueden utilizar para manejar errores específicos al trabajar con datos."""

#1. pandas.errors.EmptyDataError
#Esta excepción se lanza cuando se intenta leer un archivo que está vacío (por ejemplo, usando funciones como read_csv() o read_excel()). Ejemplo:
from pandas.errors import EmptyDataError 
try: 
# Intentar leer un archivo vacío 
    df = pd.read_csv('archivo_vacio.csv') 
except EmptyDataError: 
    print("El archivo está vacío.") 

#2. pandas.errors.DtypeWarning
#Se lanza cuando hay advertencias relacionadas con los tipos de datos en el DataFrame, especialmente cuando se encuentran columnas con tipos de datos inesperados o ambiguos. Ejemplo:
# Intentar leer un archivo donde se espera un tipo de dato pero es ambigua 
df = pd.read_csv('archivo_con_warning.csv', dtype={'columna': 'int64'}) 

#3. pandas.errors.ParserError
#Esta excepción ocurre cuando hay un error al analizar un archivo (por ejemplo, cuando el formato del archivo CSV o el delimitador es incorrecto). Ejemplo:
from pandas.errors import ParserError 
try:
# Intentar leer un archivo con un formato incorrecto
    df = pd.read_csv('archivo_incorrecto.csv') 
except ParserError:
    print("Error al analizar el archivo.") 

#4. pandas.errors.MergeError
#Se lanza cuando hay un error al intentar realizar una operación de combinación (merge) de dos DataFrame con claves que no coinciden correctamente. Ejemplo:
from pandas.errors import MergeError 
# Crear dos DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3]}) 
df2 = pd.DataFrame({'B': [4, 5, 6]}) 
try:  # Intentar hacer merge sin una clave común
    result = pd.merge(df1, df2) 
except MergeError: 
    print("Error al combinar los DataFrames.") 

#5. pandas.errors.HDFSError
#Se lanza cuando ocurre un error al interactuar con un archivo HDF5, como al intentar leer o escribir en archivos .h5 usando pandas. Ejemplo:
from pandas.errors import HDFSError 
try: # Intentar leer un archivo HDF5 con problemas
    df = pd.read_hdf('archivo_problema.h5') 
except HDFSError: 
    print("Error al leer el archivo HDF5.") 

#6. pandas.errors.OptionError
#Esta excepción se lanza cuando se intenta acceder o configurar una opción de pandas que no es válida. Ejemplo:
from pandas.errors import OptionError
try: # Intentar establecer una opción no válida 
    pd.set_option('display.invalid_option', 10) 
except OptionError: 
    print("Opción no válida.") 

#7. pandas.errors.InvalidIndexError
#Se lanza cuando se intenta usar un índice no válido en un DataFrame o Series. Ejemplo:
from pandas.errors import InvalidIndexError 
try: # Intentar usar un índice no válido 
    df = pd.DataFrame([1, 2, 3], index=[1, 2]) 
except InvalidIndexError:
    print("Índice no válido.") 

#8. pandas.errors.PerformanceWarning
#Se lanza cuando pandas detecta que el código podría no ser eficiente y podría necesitar optimización. Ejemplo:
from pandas.errors import PerformanceWarning
# Operación que puede generar una advertencia de rendimiento 
df = pd.DataFrame({'A': range(1000)}) 
df['B'] = df['A'].apply(lambda x: x ** 2) 

#pandas.errors.EmptyDataError: Lanza cuando se intenta leer un archivo vacío.
#pandas.errors.DtypeWarning: Advertencia sobre tipos de datos inesperados o ambiguos.
#pandas.errors.ParserError: Lanza cuando hay un error de análisis de archivo (formato incorrecto).
#pandas.errors.MergeError: Error al intentar realizar un merge de DataFrame con claves incorrectas.
#pandas.errors.HDFSError: Lanza errores al trabajar con archivos HDF5.
#pandas.errors.OptionError: Lanza cuando se intenta usar una opción no válida.
#pandas.errors.InvalidIndexError: Lanza cuando se usa un índice no válido en un DataFrame o Series.
#pandas.errors.PerformanceWarning: Advertencia sobre problemas de rendimiento.



"""El módulo pandas no contiene submódulos pero, tiene varios subcomponentes, clases y funciones organizadas"""

#operaciones con datos temporales, IO, estadísticas, etc. Algunos de estos subcomponentes o submódulos son:

#1. pandas.plotting
#Este submódulo proporciona herramientas para realizar gráficos directamente desde los objetos de pandas. Ofrece funciones como scatter_matrix() y andrews_curves() para visualización. Ejemplo:
import pandas.plotting as pd_plotting 
# Crear un DataFrame 
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}) # Graficar una matriz de dispersión 
pd_plotting.scatter_matrix(df) 

#2. pandas.api
#Este submódulo proporciona acceso a la API interna de pandas. Se utiliza principalmente para interactuar con elementos de bajo nivel de pandas, como la configuración del motor de computación de pandas. Ejemplo:
import pandas.api as pd_api
# Ver la lista de opciones configurables
print(pd_api.options) 

#3. pandas.tseries
#Este submódulo maneja las series temporales y proporciona funciones para trabajar con fechas y horas, como DatetimeIndex, Timedelta, etc. Ejemplo:
import pandas.tseries as pd_tseries 
# Crear una fecha usando `Timestamp`
timestamp = pd_tseries.Timestamp('2025-01-01') 
print(timestamp) 

#4. pandas.io
#Este submódulo contiene funciones de entrada y salida (I/O) para leer y escribir datos en diferentes formatos como CSV, Excel, HDF5, SQL, JSON, etc. Ejemplo:
import pandas.io as pd_io
# Leer un archivo CSV usando pandas 
df = pd_io.parsers.read_csv('archivo.csv') 

#5. pandas.core
#Este submódulo contiene la lógica interna más avanzada de pandas, incluidos los DataFrame y Series, así como las implementaciones de operaciones fundamentales. Aunque no se accede directamente de la misma forma que otros submódulos, es donde residen las clases y operaciones principales de pandas.

#6. pandas.testing
#Este submódulo se utiliza para realizar pruebas unitarias dentro de pandas. Contiene funciones para verificar la igualdad de objetos de pandas, como assert_frame_equal() y assert_series_equal(). Ejemplo:
import pandas.testing as pd_testing
# Crear dos DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3]})
df2 = pd.DataFrame({'A': [1, 2, 3]}) # Comparar los DataFrames 
pd_testing.assert_frame_equal(df1, df2) 

#7. pandas.plot
#Este submódulo es un alias de pandas.plotting y proporciona funciones para la visualización de datos en pandas. Aunque no es común usarlo de forma directa, tiene la misma funcionalidad que pandas.plotting.

#8. pandas.errors
#Este submódulo contiene las excepciones específicas de pandas, como EmptyDataError, ParserError, entre otras, que ya hemos revisado. Ejemplo:
import pandas.errors as pd_errors
# Usar alguna excepción como EmptyDataError
try: # Intentar leer un archivo vacío 
    df = pd.read_csv('archivo_vacio.csv') 
except pd_errors.EmptyDataError: 
    print("El archivo está vacío.") 

#pandas.plotting: Herramientas para realizar gráficos.
#pandas.api: Acceso a la API interna de pandas
#pandas.tseries: Funciones para trabajar con series temporales.
#pandas.io: Funciones de entrada y salida de datos (I/O).
#pandas.core: Implementaciones internas y operaciones fundamentales de pandas.
#pandas.testing: Herramientas para realizar pruebas unitarias en pandas.
#pandas.plot: Alias de pandas.plotting para visualización de datos.
#pandas.errors: Excepciones específicas de pandas.
