import shutill

"""El módulo shutil de Python proporciona una serie de funciones de alto nivel para manejar y manipular archivos y directorios. 
Está diseñado para facilitar tareas comunes como copiar, mover, renombrar y eliminar archivos o directorios."""



"""Funciones del módulo shutil:"""

#1. Copia de archivos y directorios
#shutil.copy(src, dst). Copia un archivo de src a dst. Si dst es un directorio, copia el archivo dentro de él.
shutil.copy("archivo.txt", "copia.txt") # Copia archivo.txt a copia.txt 

#shutil.copy2(src, dst). Copia un archivo conservando la metadata (fecha de modificación, permisos, etc.).
shutil.copy2("archivo.txt", "copia.txt") # Copia con metadatos 

#shutil.copyfile(src, dst). Copia solo el contenido del archivo, sin metadatos.
shutil.copyfile("archivo.txt", "copia.txt") # Copia solo el contenido 

#shutil.copymode(src, dst). Copia los permisos de archivo, sin copiar el contenido.
shutil.copymode("archivo.txt", "copia.txt") # Solo copia los permisos 

#shutil.copystat(src, dst). Copia los permisos, fecha de modificación y acceso, sin copiar el contenido.
shutil.copystat("archivo.txt", "copia.txt") # Copia solo metadatos 

shutil.copytree(src, dst). Copia recursivamente un directorio entero.
shutil.copytree("directorio_origen", "directorio_copia") 

#shutil.rmtree(path). Elimina recursivamente un directorio y su contenido.
shutil.rmtree("directorio_copia") # Elimina el directorio entero 


#2. Movimiento y renombrado de archivos y directorios
#shutil.move(src, dst). Mueve o renombra un archivo o directorio.
shutil.move("archivo.txt", "nueva_carpeta/archivo.txt") # Mueve el archivo 

#shutil.disk_usage(path). Devuelve información del disco donde está path (total, usado, libre).
uso = shutil.disk_usage("/") 
print(uso) # (total, usado, libre) en bytes 

#3. Gestión de archivos temporales
#shutil.gettempdir(). Devuelve la ruta del directorio de archivos temporales del sistema.
print(shutil.gettempdir()) # Ruta del directorio temporal 

#shutil.get_terminal_size((columns, lines)). Obtiene el tamaño de la terminal en columnas y filas.
print(shutil.get_terminal_size()) # (columnas, filas) 


#4. Funciones avanzadas de copia y archivos especiales
#shutil.which(cmd). Busca la ruta de un comando ejecutable.
print(shutil.which("python")) # Ruta del ejecutable de Python 

#shutil.chown(path, user=None, group=None). Cambia el propietario y grupo de un archivo o directorio (solo en Unix).
shutil.chown("archivo.txt", user="usuario", group="grupo") 


#5. Archivos Comprimidos
#shutil.make_archive(base_name, format, root_dir). Crea un archivo comprimido (zip, tar, etc.).
shutil.make_archive("backup", "zip", "mi_carpeta") 

#shutil.unpack_archive(filename, extract_dir). Extrae un archivo comprimido.
shutil.unpack_archive("backup.zip", "carpeta_extraida") 

#shutil.get_archive_formats(). Lista los formatos de compresión disponibles.
print(shutil.get_archive_formats()) 

#shutil.get_unpack_formats(). Lista los formatos que se pueden descomprimir.
print(shutil.get_unpack_formats()) 




"""El módulo shutil no define clases específicas, ya que está orientado principalmente a funciones para la manipulación de 
archivos y directorios. A diferencia de otros módulos de Python que utilizan clases, shutil se basa principalmente en funciones 
de alto nivel para tareas como copiar, mover, eliminar y archivar archivos."""



"""Variables comunes en shutil:"""

#shutil._USE_CPUPROFILING: Esta es una variable interna utilizada en ciertas funciones del módulo shutil para activar el perfilado de la CPU. No se utiliza directamente en la mayoría de los casos y es parte de la implementación interna. Ejemplo:
print(shutil._USE_CPUPROFILING) 






"""Algunas "constantes" o valores predeterminados en shutil:"""

#shutil.SAME_FILE: Se utiliza en el contexto de la función copy2() cuando se detecta que el archivo de origen y destino son el mismo. En lugar de copiar el archivo, la función devuelve esta constante para indicar que no se realizó ninguna acción.
#Valor: None

#shutil.ignore_patterns(*patterns): Aunque no es una constante, ignore_patterns actúa como una función que se utiliza para ignorar archivos/directorios durante una operación como copytree(), basándose en patrones proporcionados.






"""El módulo shutil no define excepciones específicas propias, pero algunas funciones dentro de shutil pueden lanzar 
excepciones estándar de Python si ocurre un error al manipular archivos o directorios."""

#Excepciones comunes en shutil:

#FileNotFoundError: Se lanza cuando una función intenta acceder a un archivo o directorio que no existe. Ejemplo: 
try:
    shutil.copy('archivo_inexistente.txt', 'destino.txt') 
except FileNotFoundError:
    print("El archivo no existe.") 

#IsADirectoryError: Se lanza cuando se intenta realizar una operación de archivo (como copy() o remove()) sobre un directorio en lugar de un archivo. Ejemplo: 
try: 
    shutil.copy('directorio', 'destino.txt') # Esto causará un error si 'directorio' es un directorio 
except IsADirectoryError: 
    print("Intentaste copiar un directorio como si fuera un archivo.") 

#PermissionError: Se lanza cuando no se tienen permisos suficientes para realizar una operación en un archivo o directorio (como leer, escribir o eliminar). Ejemplo: 
try: 
    shutil.copy('archivo.txt', '/directorio_restringido/') 
except PermissionError: 
    print("No tienes permisos suficientes para realizar esta operación.") 

#OSError: Puede ser lanzada por errores del sistema operativo, como problemas con las rutas de archivos o problemas de hardware. Ejemplo: 
try: 
    shutil.rmtree('/ruta/invalida') 
except OSError as e: 
    print(f"Ocurrió un error del sistema de archivos: {e}") 

#shutil.Error: Es una excepción general que se lanza en algunos casos específicos cuando ocurre un error durante operaciones como copytree() y rmtree(). Ejemplo: 
try: 
    shutil.copytree('directorio_origen', 'directorio_destino') 
except shutil.Error as e: 
    print(f"Hubo un error al copiar el directorio: {e}") 
