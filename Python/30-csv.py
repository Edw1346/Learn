import csv

"""El módulo csv sirve para leer y escribir archivos CSV (valores separados por comas), que son archivos de texto donde cada 
línea es un registro y los valores están separados por comas (o algún otro delimitador)."""


"""Funciones del módulo csv"""

#csv.reader(csvfile, dialect='excel', **fmtparams)
#Lee un archivo CSV y devuelve un objeto iterador que itera sobre las filas del archivo. Los valores de cada fila están representados como listas. Ejemplo: 
with open('data.csv', 'r') as file:
    reader = csv.reader(file) 
    for row in reader: 
        print(row) 

#csv.writer(csvfile, dialect='excel', **fmtparams)
#Escribe en un archivo CSV. Permite escribir las filas de datos que se pasan en formato de lista. Ejemplo: 
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file) 
    writer.writerow(['name', 'age']) 
    writer.writerow(['John', 25]) 

#csv.DictReader(csvfile, fieldnames=None, restkey=None, restval=None, dialect='excel', **fmtparams)
#Lee un archivo CSV y lo convierte en un diccionario donde las claves son los encabezados de las columnas. Ejemplo: 
with open('data.csv', 'r') as file: 
    reader = csv.DictReader(file) 
    for row in reader: 
        print(row) 

#csv.DictWriter(csvfile, fieldnames, restval='', extrasaction='raise', dialect='excel', **fmtparams)
#Escribe en un archivo CSV desde un diccionario. Las claves del diccionario corresponden a los encabezados de las columnas. Ejemplo: 
with open('output.csv', 'w', newline='') as file: 
    fieldnames = ['name', 'age'] 
    writer = csv.DictWriter(file, fieldnames=fieldnames) 
    writer.writeheader() 
    writer.writerow({'name': 'John', 'age': 25}) 

#csv.register_dialect(name, dialect)
#Registra un nuevo dialecto CSV o reemplaza uno existente. Un dialecto define cómo se formatean los archivos CSV (por ejemplo, delimitadores, comillas, etc.). Ejemplo: 
csv.register_dialect('mydialect', delimiter=';', quotechar='"') 
with open('data.csv', 'r') as file: 
    reader = csv.reader(file, dialect='mydialect') 
    for row in reader: 
        print(row) 

#csv.get_dialect(name)
#Obtiene un dialecto previamente registrado por su nombre. Ejemplo:
dialect = csv.get_dialect('excel') 
print(dialect) 

#csv.list_dialects()
#Devuelve una lista con los nombres de todos los dialectos registrados. Ejemplo:
dialects = csv.list_dialects() 
print(dialects) 

#csv.unregister_dialect(name)
#Elimina un dialecto previamente registrado. Ejemplo: 
csv.unregister_dialect('mydialect') 



"""Clases del módulo csv"""

#csv.reader
#Esta clase se utiliza para leer archivos CSV. Permite iterar sobre el contenido de un archivo CSV, devolviendo cada fila como una lista de valores.
#Métodos comunes: 
#__iter__(): Permite que el objeto reader sea iterable, es decir, se puede usar en un bucle for.__next__(): Devuelve la siguiente fila del archivo como una lista. 

#csv.writer
#Esta clase se usa para escribir datos en un archivo CSV. Permite escribir filas de datos en un archivo, donde cada fila debe ser una lista.
#Métodos comunes: 
#writerow(row): Escribe una sola fila de datos.
#writerows(rows): Escribe múltiples filas de datos.

#csv.DictReader
#Esta clase es similar a csv.reader, pero en lugar de devolver filas como listas, devuelve cada fila como un diccionario. Las claves del diccionario son los encabezados del archivo CSV.
#Métodos comunes: 
#__iter__(): Permite iterar sobre el archivo y obtener cada fila como un diccionario.
#__next__(): Devuelve la siguiente fila como un diccionario.

#csv.DictWriter
#Similar a csv.writer, pero en lugar de escribir listas, escribe diccionarios. Cada diccionario debe tener claves que coincidan con los encabezados de las columnas.
#Métodos comunes: 
#writeheader(): Escribe los encabezados del archivo CSV.
#writerow(row): Escribe una sola fila de datos desde un diccionario.

#writerows(rows): Escribe múltiples filas de datos desde diccionarios.Ejemplo: 
with open('output.csv', 'w', newline='') as file: 
    fieldnames = ['name', 'age'] 
    writer = csv.DictWriter(file, fieldnames=fieldnames) 
    writer.writeheader() writer.writerow({'name': 'John', 'age': 25}) 



"""El módulo csv en Python no tiene variables predefinidas, """



"""Constantes del módulo csv"""

#csv.QUOTE_ALL
#Especifica que todos los campos deben ser encerrados entre comillas. Valor: 0 Uso: 
with open('output.csv', 'w', newline='') as file: 
    writer = csv.writer(file, quoting=csv.QUOTE_ALL) 
    writer.writerow(['name', 'age']) 

#csv.QUOTE_MINIMAL
#Solo se colocan comillas alrededor de los campos que contienen caracteres especiales, como el delimitador o las comillas. Valor: 0 Uso:
with open('output.csv', 'w', newline='') as file: 
    writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['name', 'age']) 

#csv.QUOTE_NONNUMERIC
#Solo se colocan comillas alrededor de los campos que no son numéricos. Valor: 0 Uso:
with open('output.csv', 'w', newline='') as file: 
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC) 
    writer.writerow(['name', 'age']) 

#csv.QUOTE_NONE
#No se colocan comillas alrededor de los campos, incluso si contienen caracteres especiales. Valor: 0 Uso: 
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONE) 
    writer.writerow(['name', 'age']) 

#csv.DIALECT
#No es una constante directa, pero es el mecanismo a través del cual se configuran los dialectos. Los dialectos son colecciones de configuraciones que definen cómo se debe leer y escribir un archivo CSV, como el delimitador o las comillas. Uso: 
class MyDialect(csv.Dialect): 
    delimiter = ';' 
    quotechar = '"' 
    quoting = csv.QUOTE_MINIMAL 
    csv.register_dialect('mydialect', MyDialect) 


"""Excepciones del módulo csv"""

#csv.Error
#Es la excepción base del módulo csv. Se lanza para indicar que ha ocurrido un error genérico durante la lectura o escritura de un archivo CSV. Esta clase es rara vez utilizada directamente, pero se puede capturar si se desea manejar todos los errores relacionados con CSV. Uso: 
try: 
    with open('data.csv', 'r') as file: 
    reader = csv.reader(file) 
    for row in reader: 
        if len(row) != 3:
            raise csv.Error("Número incorrecto de campos en una fila.")
except csv.Error as e: 
    print(f"Error en CSV: {e}") 

#csv.Dialect
#Aunque no es una excepción en sí misma, la clase Dialect es la base para crear y gestionar dialectos personalizados en archivos CSV. Los dialectos son configuraciones predefinidas que indican cómo se deben leer y escribir los archivos CSV, pero si no se usan correctamente, podrían causar errores en la escritura o lectura de archivos. Si no se configura correctamente un dialecto, podría generar errores relacionados con el formato. Uso: 
try: 
    csv.register_dialect('mydialect', dialect) 
except csv.Error:
    print("Error al registrar el dialecto") 


"""El módulo csv no tiene submódulos adicionales. Es un módulo de nivel único, lo que significa que todas las funcionalidades 
relacionadas con la lectura y escritura de archivos CSV se encuentran dentro del propio módulo, sin necesidad de submódulos adicionales."""

