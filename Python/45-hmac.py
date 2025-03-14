import hmac

"""El módulo hmac en Python proporciona una implementación de códigos de autenticación de mensajes basados en hash 
(HMAC, por sus siglas en inglés), que se utiliza para verificar la integridad y autenticidad de los datos. HMAC combina "
"un algoritmo de hash criptográfico con una clave secreta, lo que lo hace más seguro que un hash estándar."""


"""Funciones principales que permiten trabajar con códigos de autenticación de mensajes basados en hash (HMAC)"""

#1. hmac.new(key, msg=b'', digestmod=None)
#Crea un nuevo objeto HMAC con la clave secreta key, el mensaje msg y el algoritmo de hash digestmod.
#Parámetros: key: La clave secreta (debe ser de tipo bytes).
#msg: El mensaje que se va a autenticar (opcional, tipo bytes).
#digestmod: El algoritmo de hash que se usará (por ejemplo, hashlib.sha256). Ejemplo:
import hashlib 
key = b'secret_key' 
message = b'Hello World' 
h = hmac.new(key, message, hashlib.sha256) 
print(h.hexdigest()) # Muestra el HMAC en formato hexadecimal 

#2. hmac.compare_digest(a, b)
#Compara de manera segura dos secuencias de datos (generalmente HMACs) y devuelve True si son iguales, o False si no lo son. Utiliza una comparación a prueba de ataques de temporización.
#Parámetros: a: El primer valor a comparar.
#b: El segundo valor a comparar. Ejemplo:
digest1 = b'abc123' 
digest2 = b'abc123' 
print(hmac.compare_digest(digest1, digest2)) # Devuelve True si son iguales 



"""El módulo hmac en Python no tiene clases definidas directamente. Su funcionalidad principal se basa en funciones,
"como hmac.new() para crear objetos HMAC y hmac.compare_digest() para comparar valores de HMAC de forma segura."""



"""El módulo hmac no define variables, pero hay algunas configuraciones y valores implícitos que están asociados con su uso."""

#1. hmac.HMAC
#Aunque no es una "variable" tradicional, el nombre HMAC en el módulo hmac hace referencia al tipo de objeto que se crea cuando utilizas la función hmac.new(). Este objeto tiene métodos para actualizar el HMAC y obtener el resultado. Puedes considerarlo una "variable" implícita que maneja el estado del HMAC.

#2. hmac.digest_size (en algunos sistemas)
#El tamaño del digest (valor hash) generado por el algoritmo de hash utilizado, aunque no está siempre explícitamente documentado como una constante accesible, en algunos casos, puedes calcular o referenciar este valor en la instancia de un objeto HMAC.


"""El módulo hmac no tiene constantes, pero utiliza algunas configuraciones relacionadas con los algoritmos de hash y la implementación de HMAC."""

#1. hmac.blocksize
#El tamaño del bloque del algoritmo de hash utilizado por HMAC. Cada algoritmo de hash tiene un tamaño de bloque específico (por ejemplo, 64 bytes para SHA-1). Este valor es interno y determina el tamaño de los bloques de datos que el HMAC usa durante el proceso.



"""El módulo hmac tiene algunas excepciones """

#1. hmac.HMAC
#Aunque HMAC no es una excepción, si intentas usarlo de manera incorrecta o con datos inválidos, puede generar errores durante la creación o actualización de un objeto HMAC.

#2. hmac.InvalidDigest
#Esta excepción se lanza cuando el digest proporcionado al realizar alguna operación no es válido o no corresponde al algoritmo de hash utilizado. Es una excepción específica para cuando el valor del digest no es apropiado.Ejemplo de uso:
try: # Digesto inválido en la comparación 
    hmac.compare_digest(b'abc123', b'xyz456')
except hmac.InvalidDigest as e: 
    print(f"Error: {e}") 

#3. TypeError
#Aunque no es exclusiva de hmac, puedes encontrar este error si intentas pasar tipos de datos incorrectos al usar las funciones del módulo hmac. Por ejemplo, si no proporcionas una cadena de bytes como clave o mensaje.Ejemplo de uso:
try: # Usar un tipo no compatible 
    key = 'secret_key' # Tipo incorrecto (debería ser bytes) 
    message = b'Hello' 
    h = hmac.new(key, message) 
except TypeError as e: 
    print(f"Error: {e}") 


"""El módulo hmac en Python no tiene submódulos. Todo el funcionamiento relacionado con los códigos de autenticación de 
"mensajes basados en hash (HMAC) se encuentra directamente en el módulo principal hmac. Este módulo proporciona funciones 
"y clases para trabajar con HMAC, pero no está estructurado en submódulos adicionales."""
