import hashlib 

"""El módulo hashlib en Python proporciona interfaces para crear resúmenes de mensajes (o hashes) mediante algoritmos 
criptográficos. Los hashes son cadenas de longitud fija que representan de manera única un conjunto de datos. Este módulo 
es muy útil para tareas como verificar integridad de datos, almacenar contraseñas de manera segura o generar firmas digitales."""

#Uso Básico: Crear un objeto hash usando un algoritmo.
#Actualizar el hash con datos.
#Obtener el hash final en forma de cadena hexadecimal.


"""Funciones"""

#1. hashlib.algorithms_guaranteed
#Devuelve un conjunto de nombres de los algoritmos de hash que están garantizados para estar disponibles en tu instalación de Python. Ejemplo de uso:
print(hashlib.algorithms_guaranteed) # Muestra los algoritmos disponibles 

#2. hashlib.algorithms_available
#Devuelve un conjunto de los algoritmos de hash disponibles en tu instalación de Python. A diferencia de algorithms_guaranteed, este puede incluir algoritmos adicionales que no son garantizados en todas las plataformas. Ejemplo de uso:
print(hashlib.algorithms_available) # Muestra todos los algoritmos disponibles 

#3. hashlib.new(name, data=b'')
#Crea un nuevo objeto de hash utilizando el nombre del algoritmo proporcionado como una cadena. Puedes pasar datos iniciales que serán procesados al instante.
#Parámetros: name: El nombre del algoritmo de hash (como 'md5', 'sha256', etc.).
#data: Datos opcionales para actualizar el hash al instante (por defecto es un byte vacío). Ejemplo de uso:
hash_object = hashlib.new('sha256', b'Hola Mundo') 
print(hash_object.hexdigest()) 

#4. hashlib.md5(data=b'')
#Devuelve un objeto hash que utiliza el algoritmo MD5. El parámetro data es opcional y se utiliza para actualizar el hash al momento de crear el objeto. Ejemplo de uso:
hash_object = hashlib.md5(b'Hola Mundo') 
print(hash_object.hexdigest()) # Muestra el hash MD5 
 
#5. hashlib.sha1(data=b'')
#Devuelve un objeto hash que utiliza el algoritmo SHA-1. Ejemplo de uso:
hash_object = hashlib.sha1(b'Hola Mundo') 
print(hash_object.hexdigest()) # Muestra el hash SHA-1 

#6. hashlib.sha224(data=b'')
#Devuelve un objeto hash que utiliza el algoritmo SHA-224. Ejemplo de uso:
hash_object = hashlib.sha224(b'Hola Mundo') 
print(hash_object.hexdigest()) # Muestra el hash SHA-224 

#7. hashlib.sha256(data=b'')
#Devuelve un objeto hash que utiliza el algoritmo SHA-256. Ejemplo de uso:
hash_object = hashlib.sha256(b'Hola Mundo') 
print(hash_object.hexdigest()) # Muestra el hash SHA-256 

#8. hashlib.sha384(data=b'')
#Devuelve un objeto hash que utiliza el algoritmo SHA-384. Ejemplo de uso:
hash_object = hashlib.sha384(b'Hola Mundo') 
print(hash_object.hexdigest()) # Muestra el hash SHA-384 

#9. hashlib.sha512(data=b'')
#Devuelve un objeto hash que utiliza el algoritmo SHA-512. Ejemplo de uso:
hash_object = hashlib.sha512(b'Hola Mundo') 
print(hash_object.hexdigest()) # Muestra el hash SHA-512 

#10. hashlib.sha3_224(data=b'')
#Devuelve un objeto hash que utiliza el algoritmo SHA-3-224. Ejemplo de uso:
hash_object = hashlib.sha3_224(b'Hola Mundo') 
print(hash_object.hexdigest()) # Muestra el hash SHA-3-224 

#11. hashlib.sha3_256(data=b'')
#Devuelve un objeto hash que utiliza el algoritmo SHA-3-256. Ejemplo de uso:
hash_object = hashlib.sha3_256(b'Hola Mundo') 
print(hash_object.hexdigest()) # Muestra el hash SHA-3-256 

#12. hashlib.sha3_384(data=b'')
#Devuelve un objeto hash que utiliza el algoritmo SHA-3-384. Ejemplo de uso:
hash_object = hashlib.sha3_384(b'Hola Mundo') 
print(hash_object.hexdigest()) # Muestra el hash SHA-3-384 

#13. hashlib.sha3_512(data=b'')
#Devuelve un objeto hash que utiliza el algoritmo SHA-3-512. Ejemplo de uso:
hash_object = hashlib.sha3_512(b'Hola Mundo') 
print(hash_object.hexdigest()) # Muestra el hash SHA-3-512 

#14. hashlib.blake2b(data=b'')
#Devuelve un objeto hash que utiliza el algoritmo BLAKE2b. Este es un algoritmo de hash rápido y seguro que es más eficiente que SHA-2 en algunas situaciones. Ejemplo de uso:
hash_object = hashlib.blake2b(b'Hola Mundo') 
print(hash_object.hexdigest()) # Muestra el hash BLAKE2b 

#15. hashlib.blake2s(data=b'')
#Devuelve un objeto hash que utiliza el algoritmo BLAKE2s, una variante de BLAKE2 más rápida y con menor tamaño de salida. Ejemplo de uso:
hash_object = hashlib.blake2s(b'Hola Mundo') 
print(hash_object.hexdigest()) # Muestra el hash BLAKE2s 

#Métodos Comunes de los Objetos Hash:
#Los objetos hash generados por cualquier función anterior tienen los siguientes métodos disponibles:

#update(data): Actualiza el objeto hash con los datos proporcionados (en formato bytes).
hash_object.update(b"Más datos") 

#hexdigest(): Devuelve el hash final como una cadena hexadecimal.
print(hash_object.hexdigest()) # Muestra el hash como hexadecimal 

#digest(): Devuelve el hash final como una secuencia de bytes.
#print(hash_object.digest()) # Muestra el hash en formato de bytes 




"""El módulo hashlib, existen algunas clases que puedes encontrar dentro del módulo"""

#1. hashlib.Hash
#La clase Hash es la clase base para todos los algoritmos de hash que se crean con el módulo hashlib. Cuando se crea un objeto hash, como con hashlib.md5() o hashlib.sha256(), lo que realmente estás creando es una instancia de la clase Hash.
#Métodos principales de la clase Hash:
#update(data): Actualiza el objeto Hash con los datos proporcionados (debe ser en formato bytes).
#hexdigest(): Devuelve el hash como una cadena hexadecimal.
#digest(): Devuelve el hash como una secuencia de bytes.
#copy(): Devuelve una copia del objeto Hash. Ejemplo de uso:
# Crear un objeto hash usando SHA-256 
hash_object = hashlib.sha256() 
# Actualizar el hash con datos 
hash_object.update(b"Hola Mundo") # Obtener el hash en formato hexadecimal print(hash_object.hexdigest()) 



"""El módulo hashlib no define variables, pero tiene algunas variables relacionadas con la configuración y la disponibilidad de algoritmos"""

#1. hashlib.algorithms_guaranteed
#Esta variable contiene un conjunto de nombres de algoritmos de hash que están garantizados para estar disponibles en la instalación de Python que estés utilizando. Esto incluye algoritmos como md5, sha1, sha224, sha256, sha384, sha512, entre otros.Ejemplo de uso:
print(hashlib.algorithms_guaranteed) # Muestra los algoritmos garantizados disponibles 

#2. hashlib.algorithms_available
#Es una variable que contiene un conjunto de los algoritmos de hash que están disponibles en tu instalación de Python, incluyendo tanto los algoritmos garantizados como otros que podrían ser específicos a tu entorno o sistema. Ejemplo de uso:
print(hashlib.algorithms_available) # Muestra todos los algoritmos disponibles 

#algorithms_guaranteed: los algoritmos garantizados disponibles.

#algorithms_available: los algoritmos que están disponibles en tu entorno de Python, tanto garantizados como adicionales.


"""El módulo hashlib no tiene constantes definidas"""



"""El módulo hashlib de Python tiene algunas excepciones"""

#1. hashlib.Hash
#Aunque no es una excepción por sí misma, el objeto Hash puede generar errores si intentas usarlo de manera incorrecta. Sin embargo, las excepciones más relevantes que podrían surgir son las siguientes:

#2. hashlib.ValueError
#Esta excepción es lanzada en situaciones donde los valores proporcionados no son válidos para el algoritmo de hash. Por ejemplo, intentar usar un nombre de algoritmo no soportado o pasar datos incorrectos al objeto Hash. Ejemplo:
try: # Intentamos crear un objeto hash con un nombre de algoritmo no válido 
    hash_object = hashlib.new('invalid_algo') 
except ValueError as e: 
    print(f"Error: {e}") 

#3. hashlib.UnsupportedAlgorithm
#Esta excepción se lanza si intentas usar un algoritmo de hash que no está soportado por el sistema en el que se ejecuta el código, o si el nombre del algoritmo es incorrecto. Ejemplo:
try: # Intentamos crear un hash con un algoritmo que no está soportado 
    hash_object = hashlib.new('sha3_512') 
except hashlib.UnsupportedAlgorithm as e: 
    print(f"Error: {e}") 

#ValueError: Cuando se pasa un valor no válido al crear un objeto de hash, como un nombre de algoritmo incorrecto o datos mal formateados.
#UnsupportedAlgorithm: Si el algoritmo solicitado no está disponible o no es compatible con tu entorno.


"""El módulo hashlib no tiene submódulos adicionales en su estructura. Todo el comportamiento relacionado con la creación 
y manipulación de hashes se encuentra directamente dentro de hashlib, que proporciona funciones y clases para generar y
manipular algoritmos de hash. No hay una jerarquía de submódulos como en otros módulos de Python."""
