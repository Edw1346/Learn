import base64

"""El módulo base64 en Python proporciona funciones para codificar y decodificar datos en formato Base64, que es un esquema 
de codificación utilizado para convertir datos binarios (como imágenes o archivos) en una cadena de caracteres ASCII. 
Esto es útil cuando necesitas almacenar o transferir datos binarios en sistemas que solo aceptan texto, como correos electrónicos o URL."""


"""Funciones para trabajar con codificación y decodificación en Base64. """

#1. base64.b64encode(data, altchars=None)
#Codifica los datos binarios (data) en una cadena Base64. El parámetro altchars es opcional y permite especificar caracteres alternativos para los símbolos + y / que se utilizan en la codificación Base64 estándar.
#Parámetros: data: Datos a codificar (tipo bytes).
#altchars: Caracteres alternativos para reemplazar + y / (opcional). Ejemplo:
data = b'Hola Mundo' 
encoded = base64.b64encode(data) 
print(encoded) 

#2. base64.b64decode(encoded_data, altchars=None, validate=False)
#Decodifica los datos Base64 (encoded_data) a su formato binario original. Si se especifica validate=True, el método verifica si los datos codificados son válidos Base64.
#Parámetros: encoded_data: Datos codificados en Base64 (tipo bytes).
#altchars: Caracteres alternativos para reemplazar + y / (opcional).
#validate: Si se establece en True, se valida si la cadena está correctamente codificada en Base64. Ejemplo:
encoded = b'SG9sYSBNdW5kbw==' 
decoded = base64.b64decode(encoded) 
print(decoded) 

#3. base64.urlsafe_b64encode(data)
#Codifica los datos binarios (data) en una cadena Base64 de manera segura para URL, utilizando caracteres alternativos - y _ en lugar de + y /. Ejemplo: 
data = b'Hola Mundo' 
encoded = base64.urlsafe_b64encode(data)
print(encoded) 

#4. base64.urlsafe_b64decode(encoded_data)
#Decodifica una cadena codificada en Base64 de URL segura a su formato binario original. Ejemplo: 
encoded = b'SG9sYS1NdW5kbw==' 
decoded = base64.urlsafe_b64decode(encoded) 
print(decoded) 

#5. base64.b32encode(data)
#Codifica los datos binarios (data) en una cadena Base32. Base32 es una variante de codificación que utiliza 32 caracteres legibles, ideal para representar datos binarios en un formato más compacto. Ejemplo: 
data = b'Hola Mundo' 
encoded = base64.b32encode(data) 
print(encoded) 

#6. base64.b32decode(encoded_data)
#Decodifica los datos Base32 (encoded_data) a su formato binario original. Ejemplo: 
encoded = b'JBSWY3DPEBLW64TMMQ==' 
decoded = base64.b32decode(encoded) 
print(decoded) 

#7. base64.b16encode(data)
#Codifica los datos binarios (data) en una cadena Base16 (también conocida como hexadecimal). Ejemplo:
data = b'Hola Mundo' 
encoded = base64.b16encode(data) 
print(encoded) 

#8. base64.b16decode(encoded_data)
#Decodifica los datos Base16 (encoded_data) a su formato binario original. Ejemplo:
encoded = b'486F6C61 204D756E64' 
decoded = base64.b16decode(encoded) 
print(decoded) 


"""El módulo base64 en Python no contiene clases. Su funcionalidad se basa en funciones que permiten codificar y decodificar "
"datos en distintos formatos (Base64, Base32, Base16), pero no está estructurado en clases."""


"""El módulo base64 en Python no tiene variables globales explícitas como otros módulos. La mayoría de las operaciones 
"que se realizan con este módulo son funciones que trabajan directamente con los datos que se les pasan como argumentos. 
"Sin embargo, hay algunas configuraciones internas y valores asociados con el comportamiento del módulo que se pueden "
"considerar como "variables implícitas", aunque no sean accesibles como variables públicas."""

#1. base64.b64decode() y base64.b64encode()
#Aunque no son variables, estas funciones tienen parámetros predeterminados que podrían considerarse configuraciones internas para el funcionamiento de la codificación y decodificación.
#Parámetro altchars: Es un parámetro opcional en las funciones b64encode() y b64decode(). Permite especificar caracteres alternativos para los símbolos + y / que se usan en la codificación Base64 estándar. Si no se proporciona, se usan los caracteres por defecto (+ y /).
#Parámetro validate: Es un parámetro que se usa en b64decode(). Si se establece en True, verifica si los datos codificados son válidos Base64.


"""El módulo base64 en Python define algunas constantes"""

#1. base64.b64urlencode y base64.b64urldecode
#Estas funciones proporcionan la codificación y decodificación Base64 específica para URLs, usando los caracteres alternativos - y _ en lugar de + y / en la codificación Base64 estándar. Esto se puede considerar como una constante para este tipo de codificación.

#2. base64.standard_b64encode y base64.standard_b64decode
#Estas son versiones estándar de las funciones b64encode y b64decode, las cuales utilizan la codificación Base64 tradicional con los caracteres + y /.


"""El módulo base64 en Python tiene algunas excepciones"""

#1. base64.binascii.Error
#Esta es la excepción principal que puede ser lanzada cuando ocurren errores durante la codificación o decodificación. Se utiliza para indicar problemas con la entrada de datos, como una cadena Base64 mal formada o datos que no son válidos para el esquema de codificación. Ejemplo: 
try: # Intentar decodificar una cadena Base64 mal formada 
    invalid_base64 = b'!@#$%^&*()' 
    decoded_data = base64.b64decode(invalid_base64) 
except base64.binascii.Error as e: 
    print(f"Error de codificación/decodificación: {e}") 


"""El módulo base64 en Python no tiene submódulos"""
