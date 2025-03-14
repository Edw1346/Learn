"""El módulo re en Python se usa para trabajar con expresiones regulares, que son secuencias de caracteres que 
definen un patrón de búsqueda. Permite buscar, coincidir y manipular cadenas de texto basadas en patrones específicos."""

import re

"""Funciones del módulo re"""

#re.match(pattern, string)
#Intenta hacer coincidir un patrón al principio de una cadena. Si hay coincidencia, devuelve un objeto match; si no, devuelve None. Ejemplo:
result = re.match(r'\d+', '123abc')
print(result.group()) # '123' 

#re.search(pattern, string)
#Busca el primer lugar en la cadena donde el patrón se encuentre. Devuelve un objeto match si lo encuentra, de lo contrario None. Ejemplo:
result = re.search(r'\d+', 'abc123def') 
print(result.group()) # '123' 

#re.findall(pattern, string)
#Encuentra todas las ocurrencias del patrón en la cadena y devuelve una lista de todas las coincidencias. Ejemplo:
result = re.findall(r'\d+', 'abc123def456')
print(result) # ['123', '456'] 

#re.finditer(pattern, string)
#Similar a findall, pero devuelve un iterador de objetos match, lo que permite iterar sobre las coincidencias. Ejemplo:
for match in re.finditer(r'\d+', 'abc123def456'): 
    print(match.group()) # 123 # 456 

#re.sub(pattern, repl, string) Reemplaza las coincidencias del patrón en la cadena con otro texto (reemplazo). Ejemplo:
result = re.sub(r'\d+', 'number', 'abc123def456')
print(result) # 'abcnumberdefnumber' 

#re.split(pattern, string) Divide la cadena en partes donde se encuentra el patrón. Ejemplo:
result = re.split(r'\d+', 'abc123def456')
print(result) # ['abc', 'def', ''] 

#re.compile(pattern)
#Compila una expresión regular en un objeto Pattern, que puede ser usado más de una vez para realizar coincidencias eficientes. Ejemplo:
pattern = re.compile(r'\d+') 
result = pattern.findall('abc123def456') 
print(result) # ['123', '456'] 

#re.subn(pattern, repl, string) Similar a sub, pero también devuelve el número de sustituciones realizadas. Ejemplo:
result, num_subs = re.subn(r'\d+', 'number', 'abc123def456')
print(result) # 'abcnumberdefnumber' 
print(num_subs) # 2 

#re.escape(string)
#Escapa todos los caracteres especiales de una cadena para que puedan ser usados en un patrón de expresión regular. Ejemplo:
result = re.escape('Hello. How are you?') 
print(result) # 'Hello\. How are you\?' 

#re.purge() Limpia la caché interna de patrones compilados. Ejemplo:
re.purge() 



"""Clases del módulo re"""

#re.Match
#Esta clase es el objeto que se devuelve cuando una expresión regular encuentra una coincidencia. Un objeto Match contiene detalles sobre la coincidencia, como la cadena coincidente, las posiciones de inicio y fin, y las subcoincidencias (si las hay). Métodos importantes: 
#group([group1, ...]): Devuelve la(s) parte(s) de la cadena que coincidieron con el patrón.
#start([group]): Devuelve la posición de inicio de la coincidencia.
#end([group]): Devuelve la posición final de la coincidencia.
#span([group]): Devuelve una tupla con las posiciones de inicio y fin de la coincidencia. Ejemplo:
result = re.search(r'(\d+)', 'abc123def')
if result: 
    print(result.group()) # '123' 
    print(result.start()) # 3 
    print(result.end()) # 6 

#re.Pattern
#La clase Pattern es la representación de una expresión regular compilada, creada cuando usas re.compile(). Esta clase no se usa directamente, pero su objeto permite realizar varias búsquedas de manera eficiente sin tener que recompilar la expresión regular cada vez. Métodos importantes: 
#match(string): Intenta hacer coincidir el patrón al principio de la cadena.
#search(string): Busca el patrón en la cadena.
#findall(string): Encuentra todas las coincidencias en la cadena.
#finditer(string): Encuentra todas las coincidencias y devuelve un iterador de objetos Match. Ejemplo:
pattern = re.compile(r'\d+') 
result = pattern.findall('abc123def456') 
print(result) # ['123', '456'] 





"""Variables del módulo re"""

#re.error
#Esta es una clase de excepción que se lanza cuando hay un error en una expresión regular. Si la expresión regular es inválida, Python generará un re.error. Ejemplo:
try: 
    pattern = re.compile(r'[') # Expresión inválida 
except re.error as e: 
    print(f"Error en la expresión regular: {e}") 

#re.IGNORECASE
#Es una constante que se puede usar en las funciones re.match(), re.search(), re.findall(), y otras para hacer que la búsqueda no distinga entre mayúsculas y minúsculas. Ejemplo:
result = re.search(r'hello', 'Hello World', re.IGNORECASE) 
print(result.group()) # 'Hello' 

#re.MULTILINE
#Esta constante se utiliza para que los metacaracteres ^ (inicio de línea) y $ (final de línea) coincidan con el inicio y el final de cada línea en una cadena, no solo con el inicio o final de la cadena completa. Ejemplo:
text = '''first line second line third line''' 
result = re.findall(r'^line', text, re.MULTILINE) 
print(result) # ['first line', 'second line', 'third line'] 


#re.DOTALL
#Esta constante permite que el carácter . coincida con cualquier carácter, incluidos los saltos de línea. De forma predeterminada, . no coincide con saltos de línea. Ejemplo:
text = 'Hello\nWorld' 
result = re.search(r'Hello.World', text, re.DOTALL) 
print(result.group()) # 'Hello\nWorld' 

#re.VERBOSE
#Esta constante permite escribir expresiones regulares más legibles, permitiendo incluir comentarios y saltos de línea dentro de una expresión regular. Ejemplo:
pattern = re.compile(r""" \d+ # Coincide con uno o más dígitos \s+ # Coincide con uno o más espacios \w+ # Coincide con una palabra """, re.VERBOSE) 
result = pattern.findall("123 abc") 
print(result) # [('123', 'abc')] 

#re.ASCII
#Esta constante hace que los metacaracteres de las expresiones regulares solo coincidan con caracteres ASCII. Si se usa, se limita a la codificación estándar ASCII. Ejemplo:
result = re.search(r'\w+', 'abcé', re.ASCII) 
print(result.group()) # 'abc' 




"""Constantes del módulo re"""

#re.IGNORECASE
#Hace que las búsquedas de expresiones regulares no distingan entre mayúsculas y minúsculas. Ejemplo:
result = re.search(r'hello', 'HELLO', re.IGNORECASE)
print(result.group()) # 'HELLO' 

#re.MULTILINE
#Hace que los metacaracteres ^ (inicio de línea) y $ (fin de línea) coincidan con el inicio y el final de cada línea dentro de una cadena, no solo con el principio o el final de la cadena completa. Ejemplo:
text = '''first line second line third line''' 
result = re.findall(r'^line', text, re.MULTILINE) 
print(result) # ['first line', 'second line', 'third line'] 

#re.DOTALL
#Permite que el carácter . coincida con cualquier carácter, incluidos los saltos de línea. Sin esta constante, el . no coincide con los saltos de línea. Ejemplo:
text = 'Hello\nWorld' 
result = re.search(r'Hello.World', text, re.DOTALL) 
print(result.group()) # 'Hello\nWorld' 

#re.VERBOSE
#Permite que las expresiones regulares sean más legibles, permitiendo comentarios y saltos de línea dentro de la expresión regular para mejorar la comprensión del patrón. Ejemplo:
pattern = re.compile(r""" \d+ # Coincide con uno o más dígitos \s+ # Coincide con uno o más espacios \w+ # Coincide con una palabra """, re.VERBOSE) 

result = pattern.findall("123 abc")
print(result) # [('123', 'abc')] 

#re.ASCII
#Hace que los metacaracteres solo coincidan con caracteres ASCII, limitando el comportamiento de la expresión regular a los caracteres estándar de 7 bits. Ejemplo:
result = re.search(r'\w+', 'abcé', re.ASCII) 
print(result.group()) # 'abc' 

#re.DEBUG
#Muestra información de depuración sobre cómo se compila la expresión regular. Esta constante es útil para depurar y entender cómo Python está interpretando y compilando el patrón. Ejemplo:
re.compile(r'\d+', re.DEBUG) 




"""Excepciones del módulo re"""

#re.error
#Esta es la excepción principal que se lanza cuando una expresión regular es inválida. Si intentas compilar un patrón mal formado o utilizar un patrón incorrecto, se genera un re.error. Ejemplo:
try: 
    pattern = re.compile(r'[') # Expresión regular inválida
except re.error as e: 
    print(f"Error en la expresión regular: {e}") # Salida: Error en la expresión regular: unterminated character set at position 0 


"""El módulo re en Python no tiene submódulos definidos. Sin embargo, dentro de re puedes encontrar diferentes 
funciones y constantes que permiten trabajar con expresiones regulares de manera flexible."""
