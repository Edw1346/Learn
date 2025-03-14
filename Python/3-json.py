"""El módulo json en Python se utiliza para trabajar con datos en formato JSON (JavaScript Object Notation). 
Permite convertir entre objetos de Python (como diccionarios y listas) y cadenas de texto en formato JSON, lo que 
es útil para intercambiar datos entre aplicaciones."""

"""Funciones del módulo json"""

#json.dumps(obj, *, indent=None, separators=None, default=None, ensure_ascii=True): Convierte un objeto de Python en una cadena JSON. Ejemplo:
json_str = json.dumps({"nombre": "Juan", "edad": 30}) 
print(json_str) 

#json.loads(s, *, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw) 
#Convierte una cadena JSON en un objeto Python. Ejemplo:
data = json.loads('{"nombre": "Juan", "edad": 30}') 
print(data) 

#json.dump(obj, fp, *, indent=None, separators=None, default=None, ensure_ascii=True)Convierte un objeto de Python y lo escribe en un archivo JSON. Ejemplo:
with open('data.json', 'w') as f:
    json.dump({"nombre": "Juan", "edad": 30}, f) 

#json.load(fp, *, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
#Lee un archivo JSON y lo convierte en un objeto Python. Ejemplo:
with open('data.json', 'r') as f: 
    data = json.load(f) 
    print(data) 

#json.JSONDecoder.decode(s) Decodifica una cadena JSON en un objeto Python. Es una versión más directa de json.loads(). Ejemplo:
decoder = json.JSONDecoder() 
data = decoder.decode('{"nombre": "Juan", "edad": 30}') 
print(data) 

#json.JSONEncoder.encode(obj) Convierte un objeto Python en una cadena JSON. Es una versión más directa de json.dumps(). Ejemplo:
encoder = json.JSONEncoder() 
json_str = encoder.encode({"nombre": "Juan", "edad": 30}) 
print(json_str) 

#json.dump(obj, fp, *, indent=None, separators=None, default=None, ensure_ascii=True) 
#Convierte un objeto Python en una cadena JSON y lo escribe en un archivo. Ejemplo:
with open("data.json", "w") as f:
    json.dump({"nombre": "Juan", "edad": 30}, f, indent=4) 

#json.load(fp, *, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
#Lee un archivo JSON y lo convierte en un objeto Python. Ejemplo:
with open('data.json', 'r') as f:
    data = json.load(f) 
    print(data) 

#json.JSONDecoder.raw_decode(s, idx=0)
#Decodifica una cadena JSON, devolviendo el primer objeto que encuentra y la posición final del objeto. Ejemplo:
json_str = '{"nombre": "Juan", "edad": 30}' 
obj, idx = json.JSONDecoder().raw_decode(json_str) 
print(obj) # {'nombre': 'Juan', 'edad': 30} 

#json.JSONDecoder.object_pairs_hook
#Usado para personalizar cómo se decodifican los objetos JSON, permitiendo que se devuelvan como una lista de tuplas en lugar de un diccionario. Ejemplo:
json_str = '{"nombre": "Juan", "edad": 30}' 
obj = json.loads(json_str, object_pairs_hook=lambda d: [(k, v) for k, v in d.items()]) 
print(obj) # [('nombre', 'Juan'), ('edad', 30)] 

#json.JSONEncoder.default(obj)
#Permite personalizar cómo se codifican los objetos en JSON, especialmente cuando el objeto no es directamente serializable. Ejemplo:
def custom_encoder(obj): 
    if isinstance(obj, set): 
        return list(obj) 
    raise TypeError(f"Type {type(obj)} not serializable") 

json_str = json.dumps({1, 2, 3}, default=custom_encoder) 
print(json_str) # [1, 2, 3] 

#json.JSONDecoder.object_hook
#Permite personalizar cómo se decodifican los objetos JSON, permitiendo usar una función de devolución personalizada para procesar los datos. Ejemplo:
def custom_hook(dct): 
    return {"nombre": dct.get("nombre").upper(), "edad": dct.get("edad")} 
json_str = '{"nombre": "Juan", "edad": 30}' 
data = json.loads(json_str, object_hook=custom_hook) 
print(data) # {'nombre': 'JUAN', 'edad': 30} 

#json.dumps(obj, separators=(',', ':'))
#Permite personalizar los separadores para los elementos JSON (comas y dos puntos). Ejemplo:
json_str = json.dumps({"nombre": "Juan", "edad": 30}, separators=(',', ':')) 
print(json_str) # {"nombre":"Juan","edad":30} 

#json.dumps(obj, ensure_ascii=False)
#Permite manejar caracteres no ASCII en las cadenas JSON. Ejemplo:
json_str = json.dumps({"nombre": "José"}, ensure_ascii=False) 
print(json_str) # {"nombre": "José"} 

#json.JSONDecoder.scan_once(string, idx=0)
#Escanea una cadena JSON una vez y devuelve el objeto y la posición final. Ejemplo:
decoder = json.JSONDecoder() 
obj, idx = decoder.scan_once('{"nombre": "Juan"}', 0) 
print(obj) # {'nombre': 'Juan'} 

#json.JSONDecoder.iterdecode(s)
#Devuelve un iterador que va decodificando objetos JSON a medida que encuentra partes de la cadena. Ejemplo:
for obj in json.JSONDecoder().iterdecode('[{"nombre": "Juan"}, {"nombre": "Ana"}]'):
print(obj) 

#json.JSONEncoder.iterencode(obj)
#Devuelve un iterador que codifica objetos de Python a JSON a medida que procesa. Ejemplo:
for chunk in json.JSONEncoder().iterencode({"nombre": "Juan", "edad": 30}): 
    print(chunk) 

#json.dump(obj, fp, sort_keys=True)
#Escribe un objeto de Python en un archivo JSON, ordenando las claves alfabéticamente. Ejemplo:
with open('data.json', 'w') as f: 
    json.dump({"nombre": "Juan", "edad": 30}, f, sort_keys=True) 

#json.dumps(obj, indent=2)
#Convierte un objeto de Python a JSON con formato de sangría para hacer el JSON legible. Ejemplo:
json_str = json.dumps({"nombre": "Juan", "edad": 30}, indent=2) 
print(json_str) 

#json.JSONDecoder.object_pairs_hook
#Usado para personalizar cómo se procesan las claves y valores en los objetos JSON, devolviendo una estructura de datos personalizada. Ejemplo:
json_str = '{"nombre": "Juan", "edad": 30}' 
data = json.loads(json_str, object_pairs_hook=dict) 
print(data) # {'nombre': 'Juan', 'edad': 30} 



"""Clases del módulo json"""

#json.JSONDecoder
#Esta clase es responsable de decodificar una cadena JSON en un objeto Python. Métodos principales: 
#decode(s): Convierte una cadena JSON en un objeto Python.
#raw_decode(s, idx=0): Decodifica una cadena JSON y devuelve el primer objeto encontrado, junto con el índice de la siguiente posición en la cadena.
#scan_once(s, idx=0): Escanea una sola vez una cadena JSON y devuelve el objeto y la posición final. Ejemplo:
decoder = json.JSONDecoder() 
data = decoder.decode('{"nombre": "Juan", "edad": 30}') 
print(data) # {'nombre': 'Juan', 'edad': 30} 

#json.JSONEncoder
#Esta clase es responsable de convertir objetos Python en cadenas JSON. Métodos principales: 
#encode(obj): Convierte un objeto Python en una cadena JSON.
#iterencode(obj): Devuelve un iterador que genera la codificación JSON para un objeto Python. Ejemplo:
encoder = json.JSONEncoder() 
json_str = encoder.encode({"nombre": "Juan", "edad": 30}) 
print(json_str) # '{"nombre": "Juan", "edad": 30}' 



"""Variables del módulo json"""

#json.JSONDecoder.encoding
#Esta variable contiene el valor predeterminado de la codificación que se utilizará durante la decodificación JSON. Su valor predeterminado es 'utf-8'. Ejemplo:
print(json.JSONDecoder.encoding) # 'utf-8' 

#json.JSONEncoder.default
#Es una función que se puede usar para proporcionar un comportamiento personalizado al codificar objetos que no son serializables de forma predeterminada. Este es un mecanismo de extensión para objetos complejos que no pueden ser convertidos a JSON de manera estándar. Ejemplo: 
def custom_encoder(obj): 
    if isinstance(obj, set): 
        return list(obj) 
raise TypeError(f"Type {type(obj)} not serializable") 
json_str = json.dumps({1, 2, 3}, default=custom_encoder) 
print(json_str) # [1, 2, 3] 

#json.JSONEncoder.ensure_ascii
#Esta variable, cuando se establece en True (que es el valor por defecto), asegura que los caracteres no ASCII se escapen en las cadenas JSON. Si se establece en False, los caracteres no ASCII se mantendrán en su forma original. Ejemplo:
json_str = json.dumps({"nombre": "José"}, ensure_ascii=False) 
print(json_str) # {"nombre": "José"} 

#json.JSONEncoder.sort_keys
#Esta variable es un parámetro utilizado en las funciones como json.dumps() para determinar si las claves en los diccionarios deben ordenarse alfabéticamente. Ejemplo:
json_str = json.dumps({"nombre": "Juan", "edad": 30}, sort_keys=True)
print(json_str) # '{"edad": 30, "nombre": "Juan"}' 




"""Constantes del módulo json"""

#json.JSONDecoder.DEFAULT
#Esta constante define el valor predeterminado para la configuración de decodificación cuando no se especifica ningún parámetro adicional. Ejemplo:
decoder = json.JSONDecoder() 
print(decoder.DEFAULT) # Puede devolver un valor predeterminado de configuración. 

#json.JSONDecoder.ERRORS
#Esta constante puede estar relacionada con los errores generados durante la decodificación de JSON. Sin embargo, no es tan común en el uso diario, ya que Python maneja las excepciones relacionadas con JSON de manera estándar.

#json.encoder.CJSONEncoder
#Aunque no es una constante en el sentido clásico, esta es una clase usada dentro del módulo json cuando se emplea el código de alto rendimiento basado en C para la codificación JSON, lo cual puede influir en el rendimiento de la codificación.

#Constantes en función de parámetros de configuración
#El módulo json permite configurar comportamientos específicos usando parámetros como ensure_ascii, sort_keys, indent, etc., pero estos no se definen como "constantes" de manera formal, sino más bien como opciones que puedes pasar a las funciones de json.dumps(), json.loads(), etc.





"""Excepciones del módulo json"""

#json.JSONDecodeError
#Es la excepción principal que se lanza cuando ocurre un error durante la decodificación de una cadena JSON. Puede ser causada por una cadena JSON mal formada o incorrecta. Ejemplo:
try: 
    data = json.loads('{"nombre": "Juan", "edad": 30')
except json.JSONDecodeError as e: 
    print(f"Error al decodificar JSON: {e}") 

#Atributos importantes: 
#msg: Mensaje de error.
#doc: La cadena JSON que causó el error.
#pos: La posición en la cadena donde ocurrió el error.

#json.JSONDecodeError.errno
#Esta es una subclase de JSONDecodeError que se usa cuando hay un error relacionado con la lectura del JSON. Generalmente, esta excepción no se maneja de forma directa, sino que es capturada dentro de JSONDecodeError.

#json.JSONDecodeError.msg
#Similar a errno, es una subclase que se refiere a mensajes de error relacionados con los problemas en la decodificación del JSON.




"""El módulo json en Python no tiene submódulos oficiales. Todo el contenido relacionado con JSON, como 
funciones, clases y excepciones, se encuentra directamente dentro del módulo json."""
