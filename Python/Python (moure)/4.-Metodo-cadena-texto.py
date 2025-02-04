"""Métodos de cadenas de texto"""

#1. Una cadena de caracteres es una secuencia inmutable de caracteres encerrada entre comillas simples (') o dobles ("): 
cadena1 = 'Hola' 
cadena2 = "Mundo" 
#Cadenas multilínea: Se definen con triple comilla simple o doble (''' o """).
cadena_multilinea = """Este es un texto multilínea.""" 

#2. Inmutabilidad: Las cadenas son inmutables, lo que significa que no pueden modificarse después de ser creadas:
cadena = "Hola" 
cadena[0] = "h" # Esto arrojará un error 

#3. Operaciones básicas. Concatenación. Unir cadenas con el operador +.
saludo = "Hola" + " " + "Mundo" # Salida: "Hola Mundo" 

#Repetición. Repetir cadenas con el operador *.
eco = "Hola " * 3 # Salida: "Hola Hola Hola " 

#Longitud. Obtener el número de caracteres con len().
longitud = len("Python") # Salida: 6 

#4. Indexación y segmentación. Indexación. Acceder a caracteres por su posición (índices comienzan en 0).
cadena = "Python" 
primera = cadena[0] # Salida: 'P' 
ultima = cadena[-1] # Salida: 'n' 

#Segmentación (Slicing). Extraer subcadenas mediante índices.
cadena = "Python" 
subcadena = cadena[0:3] # Salida: 'Pyt' 
#Sintaxis: cadena[inicio:fin:paso].

"""5. Métodos de cadenas. Manipulación de texto
lower() y upper(): Convertir a minúsculas/mayúsculas.
capitalize() y title(): Capitalizar la primera letra o cada palabra. 
strip(): Eliminar espacios al inicio y final. 
replace(): Reemplazar texto. 

División y unión
split(): Dividir cadenas en una lista. 
join(): Unir elementos de una lista en una cadena.

Búsqueda
find() y index(): Buscar la posición de una subcadena.  
startswith() y endswith(): Verificar si comienza/termina con una subcadena.
"""

#6. Formateo de cadenas. Operador %. Método antiguo para formatear texto.
"Hola %s" % "Mundo" # Salida: "Hola Mundo" 

#6.2. Método format(). Formatear cadenas con marcadores.
"Hola {}".format("Mundo") # Salida: "Hola Mundo" 

#6.3. F-strings. Método moderno y eficiente para formatear texto (Python 3.6+).
nombre = "Mundo" 
f"Hola {nombre}" # Salida: "Hola Mundo" 


#7. Expresiones regulares. Herramienta avanzada para búsqueda y manipulación de texto con el módulo re:
import re 
patron = r"\d+" 
resultado = re.findall(patron, "Hay 123 manzanas y 456 peras") 
print(resultado) # Salida: ['123', '456'] 

#8. Codificación y decodificación. Convertir cadenas a bytes y viceversa: 
cadena = "Hola" 
bytes_cadena = cadena.encode("utf-8") 
cadena_original = bytes_cadena.decode("utf-8") 

#9. Comparación de cadenas. Las cadenas se comparan lexicográficamente: 
print("apple" > "banana") # Salida: False 

#10. Unicode y caracteres especiales. Las cadenas en Python son compatibles con Unicode, lo que permite usar caracteres de múltiples idiomas.
cadena = "😀 Python" 

#11. Mutabilidad con bytearray. Aunque las cadenas son inmutables, bytearray permite una manipulación similar.
ba = bytearray(b"Hola") 
ba[0] = ord("h") # Salida: b'hola' 

#12. Seguridad en el manejo de cadenas. Sanitización de entradas para prevenir inyecciones.
entrada = "123 OR 1=1" 
if entrada.isdigit(): 
    print("Entrada segura") 




"""1. capitalize(). Para qué sirve: Convierte el primer carácter de una cadena en mayúscula y el resto en minúscula.
Limitaciones: Solo afecta el primer carácter y no modifica la cadena original.
Uso: Para formatear cadenas en estilo de oración. Ejemplo: """
texto = "hola mundo" 
print(texto.capitalize()) # Hola mundo 

"""2. casefold(). Para qué sirve: Convierte una cadena a minúsculas, más agresivamente que lower().
Limitaciones: No admite personalización del formato. Uso: Ideal para comparaciones insensibles a mayúsculas/minúsculas. Ejemplo: """
texto = "ßtraße" 
print(texto.casefold()) # strasse 

"""3. center(). Para qué sirve: Centra una cadena dentro de un ancho específico, rellenando con un carácter.
Limitaciones: Si el ancho es menor que la longitud de la cadena, no hace nada. Uso: Formatear textos visualmente: """
texto = "hola" 
print(texto.center(10, '-')) # ---hola--- 

"""4. count(). Para qué sirve: Cuenta las apariciones de un substring en una cadena.
Limitaciones: Sensible a mayúsculas y minúsculas. Uso: Buscar la frecuencia de una palabra o carácter. Ejemplo: """
texto = "hola hola" 
print(texto.count("hola")) # 2 

"""5. encode(). Para qué sirve: Codifica la cadena a bytes usando un encoding específico.
Limitaciones: Requiere un encoding válido (UTF-8, ASCII, etc.). Uso: Procesar texto en aplicaciones que requieren codificación. Ejemplo: """
texto = "hola" 
print(texto.encode("utf-8")) # b'hola' 

"""6. endswith(). Para qué sirve: Verifica si una cadena termina con un substring dado.

Limitaciones: Es sensible a mayúsculas y minúsculas. Uso: Validar extensiones o terminaciones. Ejemplo: """
texto = "archivo.txt" 
print(texto.endswith(".txt")) # True 

"""7. expandtabs(). Para qué sirve: Reemplaza caracteres de tabulación (\t) por espacios.
Limitaciones: Debes definir el tamaño del espacio. Uso: Mejorar la presentación de cadenas con tabulación. Ejemplo: """
texto = "hola\tmundo" 
print(texto.expandtabs(4)) # hola mundo 

"""8. find(). Para qué sirve: Devuelve el índice del primer substring encontrado, o -1 si no está.
Limitaciones: Solo devuelve el primer índice. Uso: Buscar substrings en cadenas. Ejemplo: """
texto = "hola mundo" 
print(texto.find("mundo")) # 5 

"""9. format(). Para qué sirve: Formatea cadenas con marcadores de posición ({}) sustituidos por valores.
Limitaciones: Puede ser más complejo que usar f-strings. Uso: Construir cadenas dinámicas. Ejemplo: """
print("Hola, {}!".format("mundo")) # Hola, mundo! 

"""10. format_map(). Para qué sirve: Similar a format(), pero utiliza un diccionario para reemplazar.
Limitaciones: Solo funciona con diccionarios u objetos similares. Uso: Más dinámico que format en algunos casos: """
datos = {"nombre": "Juan"}
print("Hola, {nombre}!".format_map(datos)) # Hola, Juan! 

"""11. index(). Para qué sirve: Devuelve el índice del primer substring encontrado.
Limitaciones: Lanza un error si no encuentra el substring. Uso: Similar a find(), pero más estricto. Ejemplo: """
texto = "hola mundo" 
print(texto.index("mundo")) # 5 

"""12. isalnum(). Para qué sirve: Verifica si todos los caracteres son alfanuméricos.
Limitaciones: Devuelve False si hay espacios o caracteres especiales. Uso: Validar identificadores. Ejemplo: """
texto = "hola123" 
print(texto.isalnum()) # True 

"""13. isalpha(). Para qué sirve: Verifica si todos los caracteres son alfabéticos.
Limitaciones: No acepta números ni espacios. Uso: Validar cadenas con solo letras. Ejemplo: """
texto = "hola" 
print(texto.isalpha()) # True 

"""14. isascii(). Para qué sirve: Verifica si todos los caracteres pertenecen al rango ASCII.
Limitaciones: No soporta caracteres Unicode fuera del rango ASCII. Uso: Validar texto ASCII puro. Ejemplo: """
texto = "hola" 
print(texto.isascii()) # True 

"""15. isdecimal(). Para qué sirve: Verifica si todos los caracteres son números decimales.
Limitaciones: No acepta puntos decimales ni signos. Uso: Validar cadenas con números enteros. Ejemplo: """
texto = "123" 
print(texto.isdecimal()) # True 

"""16. isdigit(). Para qué sirve: Verifica si todos los caracteres son dígitos (0-9).
Limitaciones: No acepta números con signos, decimales o espacios.
Uso: Validar cadenas como números enteros positivos. Ejemplo: """
texto = "12345" 
print(texto.isdigit()) # True 

"""17. isidentifier(). Para qué sirve: Verifica si la cadena es un identificador válido en Python.
Limitaciones: No admite espacios ni caracteres especiales (excepto _). Uso: Validar nombres de variables o funciones: """
texto = "variable_1" 
print(texto.isidentifier()) # True 

"""18. islower(). Para qué sirve: Verifica si todos los caracteres están en minúsculas.

Limitaciones: Ignora caracteres no alfabéticos. Uso: Validar estilo de texto. Ejemplo: """
texto = "hola mundo" 
print(texto.islower()) # True 

"""19. isnumeric(). Para qué sirve: Verifica si todos los caracteres son numéricos (incluye fracciones y números Unicode).
Limitaciones: No admite signos ni puntos decimales. Uso: Validar cadenas con números matemáticos. Ejemplo: """
texto = "12345" 
print(texto.isnumeric()) # True 

"""20. isprintable(). Para qué sirve: Verifica si todos los caracteres son imprimibles (incluye espacios).
Limitaciones: Excluye caracteres como \n o \t. Uso: Validar texto que se puede mostrar en pantalla. Ejemplo: """
texto = "hola mundo" 
print(texto.isprintable()) # True 

"""21. isspace(). Para qué sirve: Verifica si la cadena contiene solo espacios (o caracteres de espacio).
Limitaciones: Devuelve False si la cadena está vacía.Uso: Comprobar espacios en texto. Ejemplo: """
texto = " " 
print(texto.isspace()) # True 

"""22. istitle(). Para sirve: Verifica si cada palabra en la cadena comienza con una mayúscula y el resto está en minúscula.
Limitaciones: Ignora caracteres no alfabéticos. Uso: Validar títulos o encabezados. Ejemplo: """
texto = "Hola Mundo" 
print(texto.istitle()) # True 

"""23. isupper(). Para qué sirve: Verifica si todos los caracteres alfabéticos están en mayúsculas.
Limitaciones: Ignora caracteres no alfabéticos. Uso: Validar cadenas en mayúsculas. Ejemplo: """
texto = "HOLA MUNDO" 
print(texto.isupper()) # True 

"""24. join(). Para qué sirve: Une elementos de un iterable en una sola cadena, separándolos por la cadena original.
Limitaciones: Los elementos del iterable deben ser cadenas. Uso: Crear cadenas combinadas a partir de listas o tuplas: """
lista = ["hola", "mundo"] 
print(" ".join(lista)) # hola mundo 

"""25. ljust(). Para qué sirve: Justifica una cadena a la izquierda dentro de un ancho específico.
Limitaciones: Rellena con carácter, pero no modifica la cadena original. Uso: Formatear texto con alineación izquierda: """
texto = "hola" 
print(texto.ljust(10, "-")) # hola------ 

"""26. lower(). Para qué sirve: Convierte todos los caracteres alfabéticos a minúsculas.
Limitaciones: No modifica caracteres no alfabéticos. Uso: Normalizar texto. Ejemplo: """
texto = "HOLA Mundo" 
print(texto.lower()) # hola mundo 

"""27. lstrip(). Para qué sirve: Elimina los espacios (u otros caracteres específicos) al inicio de una cadena.
Limitaciones: No afecta los caracteres finales. Uso: Limpiar prefijos innecesarios. Ejemplo: """
texto = " hola" 
print(texto.lstrip()) # hola 

"""28. maketrans(). Para qué sirve: Crea una tabla de mapeo para sustituir caracteres.
Limitaciones: Se usa junto con translate(). Uso: Reemplazar caracteres según un mapeo. Ejemplo: """
tabla = str.maketrans("aeiou", "12345") 
print("hola mundo".translate(tabla)) # h4l1 m5nd4 

"""29. partition(). Para qué sirve: Divide una cadena en tres partes: antes, el separador y después.
Limitaciones: Solo divide en la primera aparición del separador. Uso: Separar cadenas por un delimitador. Ejemplo: """
texto = "hola mundo" 
print(texto.partition(" ")) # ('hola', ' ', 'mundo') 

"""30. replace(). Para qué sirve: Reemplaza un substring por otro en una cadena.
Limitaciones: No modifica la cadena original. Uso: Sustituir palabras o caracteres. Ejemplo: """
texto = "hola mundo" 
print(texto.replace("hola", "adiós")) # adiós mundo 

"""31. rfind(). Para qué sirve: Busca la última aparición de un substring y devuelve su índice.
Limitaciones: Retorna -1 si no encuentra el substring. Uso: Localizar la última ocurrencia de una subcadena. Ejemplo: """
texto = "hola mundo mundo" 
print(texto.rfind("mundo")) # 10 

"""32. rindex(). Para qué sirve: Similar a rfind(), pero lanza un error si no encuentra el substring.
Limitaciones: Lanza una excepción ValueError si no encuentra el substring. Uso: Localizar la última ocurrencia de forma estricta. Ejemplo: """
texto = "hola mundo mundo" 
print(texto.rindex("mundo")) # 10 

"""33. rjust(). Para qué sirve: Justifica la cadena a la derecha dentro de un ancho específico.
Limitaciones: No afecta la cadena original. Uso: Formatear texto con alineación derecha. Ejemplo: """
texto = "hola" 
print(texto.rjust(10, "-")) # ------hola 

"""34. rpartition(). Para qué sirve: Divide una cadena en tres partes: antes, el último separador, y después.
Limitaciones: Solo divide en la última aparición del separador. Uso: Separar cadenas desde el final. Ejemplo: """
texto = "hola mundo mundo" 
print(texto.rpartition(" ")) # ('hola mundo', ' ', 'mundo') 

"""35. rsplit(). Para qué sirve: Divide una cadena en una lista, desde la derecha, usando un separador.
Limitaciones: Limita las divisiones si especifica un máximo. Uso: Separar cadenas desde el final en partes específicas: """
texto = "a,b,c" 
print(texto.rsplit(",", 1)) # ['a,b', 'c'] 

"""36. rstrip(). Para qué sirve: Elimina los espacios (u otros caracteres específicos) al final de una cadena.
Limitaciones: No afecta caracteres al inicio. Uso: Limpiar sufijos innecesarios. Ejemplo: """
texto = "hola " 
print(texto.rstrip()) # 'hola' 

"""37. split(). Para qué sirve: Divide una cadena en una lista, desde el inicio, usando un separador.
Limitaciones: Divide todas ocurrencias del separador a menos que se limite. Uso: Separar cadenas en partes. Ejemplo: """
texto = "a,b,c" 
print(texto.split(",")) # ['a', 'b', 'c'] 

"""38. splitlines(). Para qué sirve: Divide una cadena en líneas, considerando saltos de línea.
Limitaciones: Mantiene los saltos de línea si se especifica. Uso: Procesar texto con líneas múltiples. Ejemplo: """
texto = "hola\nmundo" 
print(texto.splitlines()) # ['hola', 'mundo'] 

"""39. startswith(). Para qué sirve: Verifica si una cadena comienza con un substring específico.
Limitaciones: Es sensible a mayúsculas y minúsculas. Uso: Validar prefijos. Ejemplo: """
texto = "hola mundo" 
print(texto.startswith("hola")) # True 

"""40. strip(). Para qué sirve: Elimina espacios (u otros caracteres específicos) al inicio y final de una cadena.
Limitaciones: No afecta caracteres en medio de la cadena. Uso: Limpiar texto. Ejemplo: """
texto = " hola " 
print(texto.strip()) # 'hola' 

"""41. swapcase(). Para qué sirve: Invierte las mayúsculas y minúsculas de una cadena.
Limitaciones: No afecta caracteres no alfabéticos. Uso: Cambiar el estilo de texto. Ejemplo: """
texto = "Hola Mundo" 
print(texto.swapcase()) # hOLA mUNDO 

"""42. title(). Para qué sirve: Convierte el texto a formato de título (mayúscula inicial en cada palabra).
Limitaciones: No respeta las capitalizaciones internas. Uso: Formatear títulos. Ejemplo: """
texto = "hola mundo" 
print(texto.title()) # Hola Mundo 

"""43. translate(). Para qué sirve: Reemplaza caracteres según una tabla creada con maketrans().
Limitaciones: Requiere una tabla de traducción. Uso: Modificar caracteres de texto. Ejemplo: """
tabla = str.maketrans("aeiou", "12345") 
print("hola mundo".translate(tabla)) # h4l1 m5nd4 

"""44. upper(). Para qué sirve: Convierte todos los caracteres alfabéticos a mayúsculas.
Limitaciones: No afecta caracteres no alfabéticos. Uso: Normalizar texto a mayúsculas. Ejemplo: """
texto = "hola mundo" 
print(texto.upper()) # HOLA MUNDO 

"""45. zfill(). Para qué sirve: Rellena una cadena con ceros a la izquierda hasta alcanzar una longitud específica.
Limitaciones: No modifica la cadena original. Uso: Formatear números o cadenas con ceros. Ejemplo: """
texto = "42" 
print(texto.zfill(5)) # 00042 

"""Los métodos más comunes o más usados de las cadenas de texto:
upper()
lower()
strip()
replace()
split()
find()
startswith()
endswith()
rfind()
splitlines()
join()
count()
format()
rjust()
zfill()
"""

"""Métodos mágicos más comunes para las cadenas de texto"""

"""1. __len__(). Para qué sirve: Permite usar la función len() en una cadena de texto.
Limitaciones: Solo funciona en objetos de tipo str. Uso: Se utiliza para obtener la longitud de la cadena de texto. Ejemplo:""" 
texto = "Hola" 
print(len(texto)) # Output: 4 

"""2. __getitem__(). Para qué sirve: Permite acceder a los elementos de la cadena como si fuera una lista (usando índices).
Limitaciones: Solo funciona en objetos str y permite acceso a un índice específico de la cadena. 
Uso: Se usa para obtener un carácter en un índice específico de la cadena. Ejemplo: """
texto = "Python" 
print(texto[1]) # Output: 'y' 

"""3. __iter__(). Para qué sirve: Permite iterar sobre la cadena de texto.
Limitaciones: Solo funciona en objetos str, y convierte la cadena en un iterador.
Uso: Se usa para recorrer los caracteres de la cadena en un bucle. Ejemplo: """
texto = "abc" 
for char in texto: 
    print(char) # Output: a, b, c (en líneas separadas) 

"""4. __contains__(). Para qué sirve: Permite usar el operador in para verificar si una subcadena está dentro de la cadena.
Limitaciones: Solo funciona en objetos str.
Uso: Se utiliza para comprobar si una subcadena está presente en una cadena. Ejemplo: """

texto = "Python" 
print("Py" in texto) # Output: True 

"""5. __eq__(). Para qué sirve: Permite usar el operador == para comparar dos cadenas de texto.
Limitaciones: Solo funciona en objetos str. Uso: Se utiliza para comparar si dos cadenas son iguales. Ejemplo: """
texto1 = "Hola" 
texto2 = "Hola" 
print(texto1 == texto2) # Output: True 

"""6. __ne__(). Para qué sirve: Permite usar el operador != para comparar si dos cadenas de texto son diferentes.
Limitaciones: Solo funciona en objetos str. Uso: Se utiliza para comprobar si dos cadenas no son iguales. Ejemplo: """
texto1 = "Hola" 
texto2 = "Adiós" 
print(texto1 != texto2) # Output: True 

"""7. __lt__(). Para qué sirve: Permite usar el operador < para comparar si una cadena es menor que otra.
Limitaciones: Solo funciona en objetos str. Uso: Para comparar cadenas lexicográficamente (según el orden alfabético): """
texto1 = "abc" 
texto2 = "def" 
print(texto1 < texto2) # Output: True 

"""8. __gt__(). Para qué sirve: Permite usar el operador > para comparar si una cadena es mayor que otra.
Limitaciones: Solo funciona en objetos str. Uso: Para comparar cadenas lexicográficamente (según el orden alfabético): """
texto1 = "xyz" 
texto2 = "abc" 
print(texto1 > texto2) # Output: True 

"""9. __add__(). Para qué sirve: Permite usar el operador + para concatenar dos cadenas de texto.
Limitaciones: Solo funciona en objetos str. Uso: Se utiliza para concatenar cadenas de texto. Ejemplo: """
texto1 = "Hola" 
texto2 = " Mundo" 
print(texto1 + texto2) # Output: 'Hola Mundo' 

"""10. __mul__(). Para qué sirve: Permite usar el operador * para repetir una cadena un número específico de veces.
Limitaciones: Solo funciona en objetos str. Uso: Se usa para repetir una cadena un número determinado de veces: """
texto = "Hola" 
print(texto * 3) # Output: 'HolaHolaHola' 

"""11. __str__(). Para qué sirve: Permite definir cómo se representa una cadena cuando se usa str().
Limitaciones: Especifica cómo mostrar la cadena en formato string, generalmente se utiliza en clases personalizadas.
Uso: Se usa para representar el objeto como una cadena. Ejemplo: """
class Persona: 
    def __init__(self, nombre): 
        self.nombre = nombre 

    def __str__(self): 
        return f"Nombre: {self.nombre}" 
    
p = Persona("Juan") 
print(str(p)) # Output: 'Nombre: Juan' 

"""12. __repr__(). Para qué sirve: Similar a __str__(), pero más para representar el objeto de manera que sea evaluable por Python. Limitaciones: Generalmente se usa para depuración y no debe ser utilizado como el método principal de representación. Uso: Se usa para obtener una representación "oficial" de la cadena. Ejemplo: """
texto = "Hola" 
print(repr(texto)) # Output: "'Hola'" 

"""13. __contains__(). Para qué sirve: Permite usar el operador in para verificar si una subcadena está contenida en la cadena principal. Limitaciones: Solo funciona en objetos str. Uso: Se usa para comprobar si una subcadena está en una cadena: """
texto = "Python" 
print("Py" in texto) # Output: True 


"""14. __call__(). Para qué sirve: Permite que una cadena de texto sea llamada como una función (si se redefine este método). Limitaciones: Usualmente no se usa en cadenas de texto estándar.
Uso: Se usa para ejecutar un comportamiento personalizado al intentar llamar una cadena como si fuera una función: """
class Cadena: 
    def __init__(self, texto): 
        self.texto = texto 
        
        def __call__(self): 
            return self.texto.upper()

c = Cadena("hola") 
print(c()) # Output: 'HOLA' 

"""15. __delitem__(). Para qué sirve: Permite eliminar un elemento de la cadena (generalmente no aplicable en cadenas, pero útil para otros objetos). Limitaciones: No es útil para cadenas de texto ya que no son modificables en lugar; se aplica más a listas u otros objetos mutables. Uso: Se usa para eliminar elementos, pero no se utiliza comúnmente en cadenas. Ejemplo: (No aplicable en cadenas directamente). """