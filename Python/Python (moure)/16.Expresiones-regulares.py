

"""Expresiones regulares """

#Patrón (Pattern): Es la secuencia de caracteres que define lo que estás buscando en una cadena. Ejemplo:
import re
pattern = r"\d+" # Coincide con uno o más dígitos 

#Coincidencia (Match): Es el proceso de encontrar una secuencia de caracteres que se ajusten a un patrón. Ejemplo:
import re
match = re.match(r"\d+", "123abc") 
if match: 
    print("Coincidencia:", match.group()) # Output: "123" 

#Grupo de Captura (Capture Group): Es una parte del patrón rodeada por paréntesis que captura una porción de la cadena. Ejemplo:
import re
pattern = r"(\d+)\s+(\w+)" 
match = re.match(pattern, "123 abc")
if match: 
    print("Grupo 1:", match.group(1)) # Output: "123"
    print("Grupo 2:", match.group(2)) # Output: "abc" 

#Búsqueda de Expresiones Regulares (Regex Search): Es el proceso de buscar un patrón en una cadena. Ejemplo:
import re 
match = re.search(r"abc", "123 abc 456")
if match: 
    print("Coincidencia encontrada:", match.group()) # Output: "abc" 

#Substitución (Substitution): Es el proceso de reemplazar las coincidencias de un patrón con una cadena específica. Ejemplo:
import re
result = re.sub(r"\d+", "X", "123 abc 456")
print(result) # Output: "X abc X" 

#Compilación (Compilation): El proceso de convertir una expresión regular en un objeto RegexObject. Ejemplo:
import re 
regex = re.compile(r"\d+")
result = regex.findall("123 abc 456")
print(result) # Output: ['123', '456'] 

#Escapado (Escaping): Se refiere al uso del carácter de barra invertida (\) para tratar caracteres especiales como literales. Ejemplo:
import re
pattern = r"\." 
# Coincide con el punto literal 
match = re.match(pattern, "a.b") 
if match: print("Coincidencia encontrada:", match.group()) # Output: "." 

#Expresión Regular Compilada (Compiled Regex): Es un objeto que resulta de la compilación de un patrón. Ejemplo:
import re
regex = re.compile(r"\d{3}") 
result = regex.findall("123 abc 456")
print(result) # Output: ['123', '456'] 

#Match Object: Es el objeto que se devuelve cuando se encuentra una coincidencia usando las funciones re.match() o 

re.search() #Ejemplo:
import re 
match = re.search(r"\d+", "abc123")
if match: print("Coincidencia encontrada:", match.group()) # Output: "123" 

#Multilíneas (Multiline Matching): Los metacaracteres ^ y $ coinciden también con el inicio y fin de cada línea en lugar de solo la cadena completa. Ejemplo:
import re 
text = """Línea 1 Línea 2 Línea 3"""
pattern = re.compile(r"^Línea", re.MULTILINE)
result = pattern.findall(text) 
print(result) # Output: ['Línea', 'Línea', 'Línea'] 

#Modificadores de Expresión Regular (Flags): Son configuraciones que alteran cómo se comportan las expresiones regulares, como re.IGNORECASE para ignorar mayúsculas y minúsculas. Ejemplo:
import re 
result = re.findall(r"abc", "ABC abc", re.IGNORECASE)
print(result) # Output: ['ABC', 'abc'] 

#No Captura (Non-Capturing Groups): Son paréntesis que no almacenan los resultados para su posterior uso, definidos con (?:...). Ejemplo:
import re 
pattern = r"(?:\d{3})-(\d{2})-(\d{4})" 
match = re.match(pattern, "123-45-6789")
if match: 
    print("Grupo 1:", match.group(1)) # Output: "45" 
    print("Grupo 2:", match.group(2)) # Output: "6789" 

#Repetición (Repetition): Se refiere a cómo un patrón puede coincidir múltiples veces, usando cuantificadores como *, +, {n}, {n,}. Ejemplo:
import re 
pattern = r"\d+" 
# Coincide con uno o más dígitos
result = re.findall(pattern, "123 abc 456")
print(result) # Output: ['123', '456'] 

#Límites de Palabra (Word Boundaries): El metacaracter \b se utiliza para coincidir con los límites entre un carácter de palabra y un carácter no palabra. Ejemplo:
import re 
pattern = r"\babc\b"
# Coincide con "abc" como palabra completa 
result = re.findall(pattern, "abc abcd abcdef") 
print(result) # Output: ['abc'] 

#Alternancia (Alternation): Permite hacer coincidir una de varias opciones posibles, usando el operador |. Ejemplo:
import re 
pattern = r"abc|def"
result = re.findall(pattern, "abc def abc")
print(result) # Output: ['abc', 'def', 'abc'] 

#Posiciones de Coincidencia (Anchors): Los caracteres como ^ (inicio de la cadena) y $ (fin de la cadena) indican posiciones específicas. Ejemplo:
import re 
pattern = r"^abc" 
# Coincide con "abc" al inicio de la cadena
match = re.match(pattern, "abc123")
if match: 
    print("Coincidencia encontrada:", match.group()) # Output: "abc" 

#Unicode y Expresiones Regulares: Las expresiones regulares pueden trabajar con cadenas Unicode. Ejemplo:
import re 
pattern = r"\w+" 

# Coincide con una secuencia de caracteres alfanuméricos
result = re.findall(pattern, "abc 123 ábc") 
print(result) # Output: ['abc', '123', 'ábc'] 

#Reemplazo (Replacement): El proceso de reemplazar las partes coincidentes de una cadena con otra cadena específica. Ejemplo:
import re 
result = re.sub(r"\d+", "X", "123 abc 456") 
print(result) # Output: "X abc X" 

#Optimización de Expresiones Regulares: Involucra escribir patrones de manera eficiente para evitar operaciones innecesarias. Ejemplo:
import re 
pattern = r"(?:\d{3})-(\d{2})-(\d{4})" 
# Uso de grupos no capturantes
match = re.match(pattern, "123-45-6789") 
if match: print("Grupo 1:", match.group(1)) # Output: "45" 

#Expresión Regular No Codificada (Raw String): En Python, las expresiones regulares se escriben frecuentemente como cadenas "raw" (r"expresión"). Ejemplo:
import re 
pattern = r"\d+" 
# La cadena raw evita tener que escapar las barras invertidas 
result = re.findall(pattern, "123 abc 456") 
print(result) # Output: ['123', '456'] 


"""Lista de las expresiones regulares:
. (Punto): Coincide con cualquier carácter, excepto el salto de línea.
^ (Caret): Coincide con el inicio de una línea o cadena.
$ (Signo de dólar): Coincide con el final de una línea o cadena.
* (Asterisco): Coincide con 0 o más repeticiones del patrón anterior.
+ (Más): Coincide con 1 o más repeticiones del patrón anterior.
? (Interrogación): Coincide con 0 o 1 repetición del patrón anterior.
{n}: Coincide con exactamente n repeticiones del patrón anterior.
{n,}: Coincide con n o más repeticiones del patrón anterior.
{n,m}: Coincide con al menos n, pero no más de m repeticiones del patrón anterior.
[] (Corchetes): Define un conjunto de caracteres. Coincide con cualquier carácter dentro de los corchetes.
| (Alternancia): Coincide con el patrón a la izquierda o a la derecha de la barra vertical.
() (Paréntesis): Agrupa expresiones para aplicar operadores a un grupo de caracteres.
\d: Coincide con cualquier dígito (equivalente a [0-9]).
\D: Coincide con cualquier carácter que no sea un dígito.
\w: Coincide con cualquier carácter alfanumérico (letras, dígitos y guion bajo) (equivalente a [a-zA-Z0-9_]).
\W: Coincide con cualquier carácter que no sea alfanumérico.
\s: Coincide con cualquier carácter de espacio en blanco (espacio, tabulación, salto de línea, etc.).
\S: Coincide con cualquier carácter que no sea un espacio en blanco.
\b: Coincide con un límite de palabra (el borde entre un carácter de palabra y un carácter no palabra).
\B: Coincide con cualquier lugar que no sea un límite de palabra.
\n: Coincide con un salto de línea.
\t: Coincide con un tabulador.
(?i): Establece que la expresión regular debe ser insensible a mayúsculas y minúsculas.
(?m): Establece que las coincidencias deben considerar múltiples líneas, haciendo que los metacaracteres ^ y $ coincidan también al inicio y al final de cada línea.
(?:...): Agrupa sin capturar, es decir, no se almacena la parte coincidente para su uso posterior.
(?P<nombre>...): Asigna un nombre al grupo de captura.
\ (Escape): Escapa un carácter especial para que sea interpretado literalmente.
\b (Límite de palabra): Coincide con el límite de una palabra.
\B (No límite de palabra): Coincide con un lugar que no es el límite de una palabra.
\: Permite escapar caracteres especiales en la expresión regular."""

