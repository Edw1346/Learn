import xlrd

"""El módulo xlrd es una biblioteca en Python utilizada para leer archivos de Excel (con extensión .xls y .xlsx). Es muy útil 
para extraer datos de hojas de cálculo en formato Excel, aunque su uso se ha visto limitado en las versiones recientes, ya 
que la compatibilidad con archivos .xlsx ha sido eliminada en la versión 2.0.1 en adelante. Sin embargo, aún puede manejar 
archivos .xls (el formato de Excel de 2003 o anterior)."""

#Ejemplo básico:
import xlrd 
# Abrir un archivo Excel 
workbook = xlrd.open_workbook("archivo.xls")
# Acceder a la primera hoja
sheet = workbook.sheet_by_index(0) 
# Leer el valor de la celda en la primera fila, primera columna 
valor = sheet.cell_value(0, 0)
print(valor) 

#Limitaciones:
#A partir de la versión 2.0.1, xlrd ya no es compatible con archivos .xlsx, por lo que se recomienda usar openpyxl para estos archivos.
#Para leer archivos .xls, xlrd sigue siendo una opción viable.


"""Funciones de xlrd:"""

#xlrd.open_workbook(filename, logfile=None, encoding_override=None, on_demand=False, formatting_info=False)
#Abre un archivo de Excel (.xls o .xlsx). Ejemplo: 
wb = xlrd.open_workbook('archivo.xls') 

#workbook.sheet_by_index(index) Obtiene una hoja de trabajo usando su índice. Ejemplo: 
sheet = wb.sheet_by_index(0) # Obtiene la primera hoja 

#workbook.sheet_by_name(name) Obtiene una hoja de trabajo por su nombre. Ejemplo:
sheet = wb.sheet_by_name('Hoja1') 

#sheet.nrows: Devuelve el número de filas de la hoja. Ejemplo: 
total_filas = sheet.nrows 
print(total_filas) 

#sheet.ncols: Devuelve el número de columnas de la hoja. Ejemplo:
total_columnas = sheet.ncols 
print(total_columnas) 

#sheet.cell_value(rowx, colx): Devuelve el valor de una celda específica (especificando fila y columna). Ejemplo: 
valor = sheet.cell_value(0, 0) # Valor de la celda en la primera fila y columna 
print(valor) 

#sheet.row_values(rowx, start_colx=0, end_colx=None): Devuelve todos los valores de una fila específica. Ejemplo: 
fila = sheet.row_values(0) # Valores de la primera fila 
print(fila) 

#sheet.col_values(colx, start_rowx=0, end_rowx=None): Devuelve todos los valores de una columna específica. Ejemplo: 
columna = sheet.col_values(0) # Valores de la primera columna 
print(columna) 

#sheet.cell(rowx, colx): Obtiene un objeto de celda que contiene más detalles sobre una celda (tipo de dato, valor, etc.). Ejemplo: 
celda = sheet.cell(0, 0) # Obtiene la celda de la primera fila y columna 
print(celda.value) 
print(celda.ctype) 

#sheet.get_row(rowx): Devuelve un objeto de tipo Row que representa una fila completa. Ejemplo: 
fila_completa = sheet.get_row(0) # Obtiene la primera fila como un objeto Row 
print(fila_completa) 


#sheet.get_column(colx): Devuelve un objeto de tipo Column que representa una columna completa. Ejemplo:
columna_completa = sheet.get_column(0) # Obtiene la primera columna
print(columna_completa) 

#xlrd.open_workbook(file_contents=None, filename=None, logfile=None, encoding_override=None, on_demand=False)
#Abre un libro de trabajo a partir del contenido del archivo (no necesariamente desde un archivo físico). Ejemplo: 
with open('archivo.xls', 'rb') as file: 
    contenido = file.read() 
    wb = xlrd.open_workbook(file_contents=contenido) 

#xlrd.xldate_as_tuple(xldate, datemode)
#Convierte una fecha de Excel (representada como un número flotante) en una tupla de fecha estándar de Python (año, mes, día, hora, minuto, segundo). Ejemplo: 
fecha = xlrd.xldate_as_tuple(41640, 0) # Convertir fecha de Excel a tupla
print(fecha) 

#xlrd.biffh
#Función para trabajar con estructuras de archivo BIFF (Binary Interchange and File Format). Ejemplo: Es una parte interna del módulo y no se usa directamente para la manipulación básica de archivos.

#xlrd.open_workbook(file, on_demand=False)
#Permite la apertura de un archivo Excel para lectura. Ejemplo:
workbook = xlrd.open_workbook('archivo.xlsx', on_demand=True) 



"""El módulo xlrd tiene varias clases"""

#1. Book
#Representa el libro de trabajo de Excel. Una instancia de esta clase se crea al abrir un archivo de Excel con xlrd.open_workbook(). Contiene todas las hojas del archivo Excel.
#Métodos principales: 
#sheet_by_index(index): Obtiene una hoja por su índice.
#sheet_by_name(name): Obtiene una hoja por su nombre.
#nsheets: Número total de hojas en el libro. Ejemplo: 
book = xlrd.open_workbook('archivo.xls') 
print(book.nsheets) # Número total de hojas 

#2. Sheet
#Descripción: Representa una hoja de cálculo dentro del libro de trabajo. Cada hoja tiene filas y columnas que pueden ser accedidas y modificadas.
#Métodos principales: 
#nrows: Número de filas en la hoja.
#ncols: Número de columnas en la hoja.
#cell_value(rowx, colx): Devuelve el valor de una celda específica.
#row_values(rowx): Devuelve todos los valores de una fila.
#col_values(colx): Devuelve todos los valores de una columna. Ejemplo: 
sheet = book.sheet_by_index(0) # Accede a la primera hoja 
print(sheet.cell_value(0, 0)) # Valor de la celda A1 

#3. Cell
#Representa una celda dentro de una hoja. Cada celda tiene propiedades como el valor, el tipo de dato, etc.
#Atributos principales: 
#value: El valor de la celda.
#ctype: El tipo de celda (texto, número, fecha, etc.).
#rowx: La fila en la que se encuentra la celda.
#colx: La columna en la que se encuentra la celda. Ejemplo: 
cell = sheet.cell(0, 0) # Obtiene la celda A1 
print(cell.value) # Imprime el valor de la celda 

#4. Row
#Representa una fila completa dentro de una hoja. Puede contener múltiples celdas.
#Métodos principales: 
#__getitem__(colx): Permite acceder a una celda en una fila por su índice de columna. Ejemplo: 
row = sheet.row(0) # Obtiene la primera fila 
print(row[0].value) # Imprime el valor de la primera celda de la fila 

#5. Column
#Representa una columna completa dentro de una hoja. Puede contener múltiples celdas.
#Métodos principales: 
#__getitem__(rowx): Permite acceder a una celda en una columna por su índice de fila. Ejemplo:
col = sheet.col(0) # Obtiene la primera columna
print(col[0].value) # Imprime el valor de la primera celda de la columna 

#6. Xldate
#Utilizada para trabajar con fechas representadas como números flotantes en archivos de Excel (fechas de Excel). Esta clase convierte números flotantes en fechas legibles.
#Métodos principales: 
#xldate_as_tuple(xldate, datemode): Convierte una fecha de Excel en una tupla estándar de Python (año, mes, día, hora, minuto, segundo). Ejemplo:
from xlrd import xldate_as_tuple
fecha_excel = 41640 # Un número flotante que representa una fecha en Excel 
fecha = xldate_as_tuple(fecha_excel, 0) # Convierte a tupla 
print(fecha) # (2022, 10, 25, 0, 0, 0) 


"""El módulo xlrd no tiene muchas "variables" en el sentido convencional, pero sí tiene algunas constantes y atributos 
importantes que se pueden utilizar durante el procesamiento de archivos de Excel."""

#1. xlrd.biffh
#Este es un submódulo interno de xlrd que maneja el formato BIFF (Binary Interchange File Format) de los archivos .xls. No es comúnmente utilizado directamente en las aplicaciones de usuario, pero está presente en el núcleo de la librería para procesar los archivos Excel. Ejemplo: Generalmente no se usa directamente, pero es importante saber que está disponible para trabajar con la estructura interna de los archivos Excel.

#2. xlrd.__version__
#Representa la versión del módulo xlrd que está instalada en el entorno. Ejemplo:
print(xlrd.__version__) # Imprime la versión instalada de xlrd 


"""Las constantes más importantes de xlrd:"""

#1. xlrd.XL_CELL_EMPTY
#Constante que representa una celda vacía. Si una celda no contiene ningún valor, su tipo será XL_CELL_EMPTY. Valor: 0 Ejemplo:
import xlrd 
cell_type = sheet.cell(0, 0).ctype
if cell_type == xlrd.XL_CELL_EMPTY:
    print("La celda está vacía.") 

#2. xlrd.XL_CELL_TEXT
#Constante que representa una celda que contiene texto. Valor: 1 Ejemplo: 
cell_type = sheet.cell(0, 0).ctype 
if cell_type == xlrd.XL_CELL_TEXT:
    print("La celda contiene texto.") 

#3. xlrd.XL_CELL_NUMBER
#Constante que representa una celda que contiene un número. Valor: 2 Ejemplo: 
cell_type = sheet.cell(0, 0).ctype
if cell_type == xlrd.XL_CELL_NUMBER: 
    print("La celda contiene un número.") 

#4. xlrd.XL_CELL_DATE
#Constante que representa una celda que contiene una fecha. Valor: 3 Ejemplo: 
cell_type = sheet.cell(0, 0).ctype
if cell_type == xlrd.XL_CELL_DATE:
    print("La celda contiene una fecha.") 

#5. xlrd.XL_CELL_BOOLEAN
#Constante que representa una celda que contiene un valor booleano (True o False). Valor: 4 Ejemplo: 
cell_type = sheet.cell(0, 0).ctype
if cell_type == xlrd.XL_CELL_BOOLEAN:
    print("La celda contiene un valor booleano.") 

#6. xlrd.XL_CELL_ERROR
#Constante que representa una celda que contiene un error (por ejemplo, #DIV/0!). Valor: 5 Ejemplo: 
cell_type = sheet.cell(0, 0).ctype 
if cell_type == xlrd.XL_CELL_ERROR: 
    print("La celda contiene un error.") 

#6. xlrd.XL_UNICODE
#Constante que se usa para especificar una celda que contiene texto en formato Unicode. Valor: 1. Ejemplo: 
if cell.ctype == xlrd.XL_UNICODE: 
    print("La celda contiene texto Unicode.") 

#7. xlrd.XL_CELL_BLANK (solo en versiones anteriores)
#Constante que se utilizaba para representar celdas en blanco. A partir de la versión 2.0.0 de xlrd, las celdas vacías son tratadas con XL_CELL_EMPTY. Valor: 0 Ejemplo:
if cell.ctype == xlrd.XL_CELL_BLANK:
    print("La celda está vacía.") 


"""El módulo xlrd define algunas excepciones"""

#1. xlrd.biffh.XLRDError
#Esta es la excepción principal de xlrd. Se lanza para indicar que hubo un error general durante la lectura de un archivo Excel, ya sea por un formato incorrecto o problemas al procesar el archivo. Ejemplo: 
import xlrd
try: 
    workbook = xlrd.open_workbook("archivo_invalido.xls") 
except xlrd.biffh.XLRDError as e: 
    print(f"Error al abrir el archivo: {e}") 

#2. xlrd.XLRDError
#Similar a xlrd.biffh.XLRDError, esta es una excepción general para errores al leer un archivo Excel. Se usa cuando ocurre un error relacionado con la lectura de los datos o el archivo en sí. Ejemplo: 
try: 
    workbook = xlrd.open_workbook("archivo_no_valido.xls") 
except xlrd.XLRDError as e: 
    print(f"Error al abrir el archivo: {e}") 

#3. xlrd.XLFormatException
#Esta excepción se lanza cuando el formato del archivo Excel es incorrecto o no es compatible con el formato que espera el módulo xlrd. Puede suceder si se intenta abrir un archivo que no es un archivo Excel válido o que no está bien formado. Ejemplo:
try: 
    workbook = xlrd.open_workbook("archivo_corrupto.xls") 
except xlrd.XLFormatException as e: 
    print(f"El archivo tiene un formato incorrecto: {e}") 

#4. xlrd.biffh.XLRDError
#Esta es una excepción lanzada cuando hay problemas con el tipo de archivo que se intenta abrir. Por ejemplo, si intentas abrir un archivo .xlsx (que es un formato más moderno) con una versión antigua de xlrd que solo soporta archivos .xls. Ejemplo:
try: 
    workbook = xlrd.open_workbook("archivo.xlsx") 
except xlrd.biffh.XLRDError as e: 
    print(f"Error: {e}") 

#5. xlrd.utils.XLRDError
#Se lanza para indicar que hubo un error al intentar convertir un objeto de datos o un tipo que no puede ser manejado por xlrd. Ejemplo: 
try: 
    data = xlrd.utils.text_to_num("texto_no_convertible") 
except xlrd.utils.XLRDError as e: 
    print(f"Error de conversión: {e}") 


"""El módulo xlrd tiene algunos submódulos"""

#1. xlrd.biffh
#Este submódulo se ocupa de los detalles internos relacionados con el formato BIFF de los archivos Excel .xls. BIFF es el formato binario antiguo que utilizaban las versiones de Excel anteriores a la 2007.
#Funciones principales: 
#Maneja la interpretación y la lectura de los archivos binarios de Excel.
#Permite leer los datos de una hoja de cálculo en formato BIFF8 (por ejemplo, archivos .xls de Excel 97-2003). Ejemplo:
from xlrd.biffh import XLRDError
try: # Intentar abrir un archivo en formato BIFF 
    workbook = xlrd.open_workbook("archivo.xls") 
except XLRDError as e: 
    print(f"Error en el archivo BIFF: {e}") 

#2. xlrd.sheet
#Este submódulo contiene funciones y clases relacionadas con las hojas de cálculo dentro de un libro de 
#Excel. Maneja las celdas, filas y columnas de un archivo Excel.
#Funciones principales: 
#Permite acceder a los datos de las celdas, así como realizar operaciones sobre ellas.
#Contiene métodos como cell_value(), nrows, ncols, etc., que se usan para trabajar con las hojas de cálculo dentro de un libro. Ejemplo:
import xlrd 
workbook = xlrd.open_workbook("archivo.xls")
sheet = workbook.sheet_by_index(0)
print(sheet.cell_value(0, 0)) # Imprime el valor de la celda en la primera fila y columna 

#3. xlrd.utils
#Este submódulo proporciona varias funciones utilitarias que se pueden usar para convertir, interpretar o modificar datos leídos de un archivo Excel. Es especialmente útil cuando se trabaja con datos numéricos o de fechas que requieren conversión.
#Funciones principales: 
#Proporciona herramientas para convertir datos de celdas a tipos de Python más útiles, como convertir fechas o números almacenados como texto en celdas de Excel.
#Una de las funciones más utilizadas es xldate_as_tuple(), que convierte fechas de Excel en una tupla de fecha de Python. Ejemplo:
from xlrd.utils import xldate_as_tuple 
date_tuple = xldate_as_tuple(41505, 0)
# Convierte la fecha de Excel 41505 a una tupla de fecha
print(date_tuple) # (2013, 5, 16, 0, 0, 0) 

#4. xlrd.text
#Submódulo utilizado para trabajar con cadenas de texto en archivos Excel. Aunque no se utiliza de forma común, es importante para la conversión o manejo de texto en ciertas celdas.
#Funciones principales: 
#Realiza conversiones entre diferentes formatos de texto dentro del archivo Excel. Ejemplo: 
# Este submódulo es más utilizado internamente por xlrd para manejar cadenas de texto 
# No se usa directamente en el código, pero forma parte de la estructura interna. 

