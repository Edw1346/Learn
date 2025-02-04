"""Fichero
Es un contenedor de datos que puede almacenar información de forma permanente en un disco u otro medio de almacenamiento. Los ficheros pueden ser de texto (legibles para humanos) o binarios (datos en formato no legible directamente)."""

"""Modos de Apertura: Al abrir un fichero, se especifica el propósito mediante modos como:
'r': Lectura (read). El fichero debe existir.
'w': Escritura (write). Si el fichero existe, se sobrescribe; si no, se crea.
'a': Añadir (append). Escribe al final del fichero sin sobrescribir su contenido.
'rb', 'wb', 'ab': Modo binario para lectura, escritura o añadir.
'r+': Lectura y escritura.

Operaciones Comunes:
Leer datos: Obtener el contenido del fichero.
Escribir datos: Añadir o sobrescribir contenido.
Cerrar el fichero: Liberar recursos del sistema.

Context Manager:
Utiliza la instrucción with para manejar automáticamente la apertura y cierre de ficheros. Ejemplo:"""
with open("archivo.txt", "r") as fichero: 
    contenido = fichero.read() 

"""Puntero de Archivo:
Es la posición en el fichero desde donde se realiza la próxima operación de lectura o escritura.
Se controla con métodos como seek() y tell().

Operaciones con Ficheros"""

#Abrir un Fichero:
fichero = open("archivo.txt", "r") 

#Leer un Fichero: Leer todo el contenido: 
contenido = fichero.read() 

#Leer línea por línea: 
for linea in fichero: print(linea) 

#Escribir en un Fichero:
with open("archivo.txt", "w") as fichero: 
    fichero.write("Hola, mundo\n") 

#Añadir al Final de un Fichero:
with open("archivo.txt", "a") as fichero: 
    fichero.write("Nueva línea\n") 

#Cerrar un Fichero:
fichero.close() 


"""Tipos de Ficheros
Texto: Almacenan datos como cadenas de caracteres. Codificación común: UTF-8.
Binarios: Almacenan datos en formato binario. Ejemplo: imágenes, vídeos o archivos ejecutables.

Modos Avanzados
Lectura y Escritura Simultánea:"""
with open("archivo.txt", "r+") as fichero:
    contenido = fichero.read() 
    fichero.write("Texto adicional\n") 

#Manejo de Ficheros Binarios:
with open("imagen.png", "rb") as fichero: 
    datos = fichero.read() 

#Mover el Puntero con seek():
with open("archivo.txt", "r") as fichero: 
    fichero.seek(5) # Moverse al byte 5 
    contenido = fichero.read(10) # Leer 10 bytes 

#Obtener la Posición del Puntero con tell():
with open("archivo.txt", "r") as fichero: 
    posicion = fichero.tell() 
    print(f"Posición actual: {posicion}") 


"""Puntero de Archivo
Marca la posición actual en el archivo desde donde se realiza la próxima operación de lectura o escritura. Métodos asociados: 
seek(pos): Mover el puntero a una posición específica.
tell(): Obtener la posición actual del puntero.

6. Excepciones Relacionadas
Al trabajar con ficheros, pueden surgir errores como:
FileNotFoundError: El fichero no existe.
PermissionError: No se tienen permisos para acceder al fichero.
EOFError: Se alcanzó el final del archivo inesperadamente.

7. Codificación
La codificación define cómo se representan los caracteres en el fichero.
Codificaciones comunes: 
UTF-8: Ideal para la mayoría de los textos en Python.
ASCII: Solo para caracteres en inglés.

8. Ficheros Temporales
Ficheros creados para almacenamiento temporal durante la ejecución del programa. En Python, se pueden manejar con el módulo tempfile.

9. Ficheros de Gran Tamaño
Técnicas para manejar archivos grandes: 
Leer en partes (buffers) en lugar de cargar todo en memoria: """
with open("archivo_grande.txt", "r") as fichero: 
    while (linea := fichero.readline()): 
        print(linea) 

"""10. Formatos de Ficheros
CSV (Comma-Separated Values): 
Almacenan datos tabulares separados por comas. Manejados con el módulo csv en Python.

JSON (JavaScript Object Notation): 
Formato de intercambio de datos legible y estructurado. Manejados con el módulo json.

XML (eXtensible Markup Language): 
Almacenan datos jerárquicos. Manejados con el módulo xml.etree.ElementTree.

11. Manejo de Ficheros Binarios

Leer y escribir archivos binarios como imágenes o vídeos."""
with open("imagen.png", "rb") as fichero: 
    datos = fichero.read() 

"""12. Librerías Relacionadas
os: Operaciones con el sistema de archivos (crear, renombrar, eliminar archivos o carpetas). Ejemplo: """
import os 
os.rename("archivo_viejo.txt", "archivo_nuevo.txt") 
#shutil: Copia, mueve y elimina archivos o directorios completos.
#pathlib: Manipulación más moderna de rutas y archivos.

"""13. Ficheros y Streams
Flujo de datos: Modelo para leer/escribir datos de manera continua en lugar de cargar todo el archivo. Ejemplo: Leer un archivo línea por línea para optimizar memoria.

14. Sincronización y Bloqueo
En aplicaciones concurrentes, es importante bloquear el acceso a ficheros para evitar conflictos.
Usado con el módulo threading o multiprocessing.

15. Seguridad en el Manejo de Ficheros
Validar las rutas de archivos para evitar vulnerabilidades (e.g., ataques de path traversal).
Manejar excepciones correctamente al interactuar con archivos sensibles."""




"""Buenas Prácticas"""

"""1. Usar Context Manager (with)
Siempre usa la instrucción with al abrir ficheros para garantizar que se cierren automáticamente, incluso si ocurre una excepción. Ejemplo:"""
with open("archivo.txt", "r") as fichero: 
    contenido = fichero.read() 
#Ventaja: Evita fugas de recursos y simplifica el manejo del fichero.

"""2. Manejar Excepciones
Implementa bloques try-except para capturar errores como FileNotFoundError o PermissionError. Ejemplo:"""
try: 
    with open("archivo.txt", "r") as fichero: 
        contenido = fichero.read() 

except FileNotFoundError: 
    print("Error: El archivo no existe.") 
except PermissionError: 
    print("Error: No tienes permisos para acceder al archivo.") 

"""3. Validar la Entrada del Usuario
Si el usuario introduce el nombre del archivo, valida que el fichero exista antes de abrirlo. Ejemplo:"""
import os 
archivo = input("Introduce el nombre del archivo: ") 
if os.path.exists(archivo): 
    with open(archivo, "r") as fichero: 
        print(fichero.read()) 
else: print("Error: El archivo no existe.") 

"""4. Trabajar con Codificaciones
Usa siempre una codificación explícita, como UTF-8, para evitar errores con caracteres especiales. Ejemplo:"""
with open("archivo.txt", "r", encoding="utf-8") as fichero: 
    contenido = fichero.read() 

"""5. No Sobrescribir Datos Involuntariamente
Verifica si un archivo existe antes de abrirlo en modo escritura (w) para evitar borrar datos accidentalmente. Ejemplo:"""
import os 
archivo = "archivo.txt" 
if os.path.exists(archivo): 
    print("El archivo ya existe. ¿Deseas sobrescribirlo?") 
else: 
    with open(archivo, "w") as fichero: 
        fichero.write("Contenido nuevo.") 

"""6. Liberar Recursos Manualmente (En Casos Especiales)
Si no usas with, siempre cierra el fichero manualmente. Ejemplo:"""
fichero = open("archivo.txt", "r") 
contenido = fichero.read() 
fichero.close() 

"""Técnicas Avanzadas"""

"""1. Leer Archivos Grandes por Fragmentos
En lugar de cargar todo el contenido en memoria, lee los datos en partes. Ejemplo:"""
with open("archivo_grande.txt", "r") as fichero: 
    for linea in fichero: print(linea.strip()) 
#Ventaja: Ideal para trabajar con archivos grandes, ahorrando memoria.

"""2. Usar seek() y tell() para Mover el Puntero
Controla la posición en el archivo para realizar operaciones específicas. Ejemplo:"""
with open("archivo.txt", "r") as fichero: 
    fichero.seek(5) # Mover el puntero al byte 5 
    print(fichero.read(10)) # Leer 10 bytes desde esa posición 
    print(f"Puntero actual: {fichero.tell()}") 

"""3. Crear Archivos Temporales
Usa el módulo tempfile para crear ficheros temporales que se eliminan automáticamente. Ejemplo:"""
import tempfile 
with tempfile.NamedTemporaryFile(delete=True) as temp: 
    temp.write(b"Datos temporales\n") 
    temp.seek(0) 
    print(temp.read().decode("utf-8")) 

"""4. Procesar Archivos CSV o JSON
Usa las librerías csv y json para manejar formatos estructurados. Ejemplo CSV:"""
import csv 
with open("datos.csv", "r") as fichero: 
    lector = csv.reader(fichero) 
    for fila in lector: print(fila) 

#Ejemplo JSON:
import json 
with open("datos.json", "r") as fichero: 
    datos = json.load(fichero) 
    print(datos) 

"""5. Manipular Archivos Binarios
Al trabajar con imágenes, vídeos o cualquier archivo binario, usa los modos rb y wb. Ejemplo:"""
with open("imagen.png", "rb") as fichero: 
    datos = fichero.read() 

with open("copia_imagen.png", "wb") as copia: 
    copia.write(datos) 

"""6. Usar os y pathlib para Operaciones con Ficheros
Usa os y pathlib para realizar operaciones como mover, renombrar o eliminar archivos. Ejemplo:"""
import os 
os.rename("archivo_viejo.txt", "archivo_nuevo.txt") 
os.remove("archivo_a_borrar.txt") 

#Con pathlib:
from pathlib import Path 
archivo = Path("archivo.txt") 
if archivo.exists(): 
    archivo.unlink() # Eliminar archivo 

"""7. Copiar y Mover Archivos con shutil
Usa la librería shutil para mover o copiar archivos y directorios. Ejemplo:"""
import shutil 
shutil.copy("archivo.txt", "copia_archivo.txt") 
shutil.move("archivo.txt", "nueva_carpeta/") 

"""8. Leer y Escribir en Múltiples Archivos Simultáneamente
Abre y manipula varios ficheros a la vez usando múltiples with. Ejemplo:"""
with open("entrada.txt", "r") as entrada, open("salida.txt", "w") as salida: 
    for linea in entrada: salida.write(linea.upper()) # Convertir el texto a mayúsculas 
