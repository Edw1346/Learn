import copy

"""Variable por valor y referencia"

"""1. Variables por valor: Cuando trabajas con tipos de datos inmutables (como int, float, str, bool, y tuplas), Python trata las variables como si fueran por valor."""
#Aunque técnicamente Python no pasa copias completas (como en lenguajes como C++), los valores inmutables no pueden ser modificados en su lugar. Si intentas modificarlos, Python crea un nuevo objeto en memoria y la variable apunta a ese nuevo objeto. Ejemplo práctico (inmutables):
a = 10 # Se crea un objeto entero en memoria 
b = a # b apunta al mismo objeto que a (por referencia) 
print(a, b) # Salida: 10, 10 
b = 20 # b ahora apunta a un nuevo objeto 
print(a, b) # Salida: 10, 20 
#Aquí, a no cambia porque los enteros son inmutables, y b se asigna a un nuevo valor.

#2. Variables por referencia: Cuando trabajas con tipos de datos mutables (como listas, diccionarios, y conjuntos), las variables funcionan como referencias al mismo objeto en memoria. Si modificas el objeto usando una de las referencias, los cambios se reflejan en todas las referencias al mismo objeto. Ejemplo práctico (mutables):
x = [1, 2, 3] # Se crea una lista en memoria 
y = x # y es una referencia al mismo objeto que x 
y.append(4) # Modificamos el objeto a través de y 
print(x, y) # Salida: [1, 2, 3, 4] [1, 2, 3, 4] 
Aquí, tanto x como y apuntan al mismo objeto, por lo que cualquier cambio afecta a ambas referencias.

"""3. Clonar objetos para evitar cambios accidentales. Si no quieres que los cambios en una referencia afecten a otra, puedes hacer una copia del objeto. Ejemplo de copia:
x = [1, 2, 3] 
y = x[:] # Copia superficial 
y.append(4) 
print(x, y) # Salida: [1, 2, 3] [1, 2, 3, 4] 

"""4. Cambios en profundidad (copias profundas)
En estructuras más complejas (como listas de listas), necesitas usar el módulo copy para realizar copias profundas. Ejemplo de copia profunda: """
original = [[1, 2], [3, 4]] 
copia = copy.deepcopy(original) 
copia[0].append(5) 
print(original) # Salida: [[1, 2], [3, 4]] 
print(copia) # Salida: [[1, 2, 5], [3, 4]] 


#Consejos para entender bien las variables por valor y por referencia. Prueba modificando objetos y observa si el cambio afecta a otras variables. Usa funciones para ver cómo se pasan los valores o referencias: 
def modificar_lista(lista): 
    lista.append(10) 

def modificar_entero(numero): 
    numero += 10 

mi_lista = [1, 2, 3] 
mi_numero = 5 
modificar_lista(mi_lista) 
modificar_entero(mi_numero) 
print(mi_lista) # Salida: [1, 2, 3, 10] 
print(mi_numero) # Salida: 5 


"""Conceptos clave relacionados"""

"""1. Tipos de datos en Python
Inmutables: No pueden ser modificados después de su creación. Ejemplos: int, float, str, tuple, bool, frozenset.
Mutables: Pueden ser modificados después de su creación. Ejemplos: list, dict, set.

Relación con valor y referencia:
Los inmutables se comportan como si fueran pasados por valor, porque no pueden modificarse.
Los mutables se comportan como si fueran pasados por referencia, porque pueden modificarse directamente en memoria.

2. Asignación de variables: En Python, las variables no almacenan los valores directamente, sino que son referencias a objetos en memoria. Esto significa que múltiples variables pueden apuntar al mismo objeto. Ejemplo:"""
a = [1, 2, 3] # 'a' apunta a una lista en memoria 
b = a # 'b' apunta al mismo objeto 
b.append(4) 
print(a) # Salida: [1, 2, 3, 4] (ambas referencias afectan al mismo objeto) 

#3. Identidad vs. Equivalencia. Identidad (is): Comprueba si dos variables apuntan al mismo objeto en memoria.
#Equivalencia (==): Comprueba si dos variables tienen el mismo valor. Ejemplo:
x = [1, 2, 3] 
y = [1, 2, 3] 
print(x == y) # Salida: True (tienen el mismo valor) 
print(x is y) # Salida: False (son objetos diferentes en memoria) 

"""4. Pasaje de parámetros a funciones. Cuando pasas una variable a una función:
Tipos inmutables: La función trabaja con una copia del valor, porque los objetos no pueden modificarse.
Tipos mutables: La función puede modificar directamente el objeto original, la referencia al objeto es compartida:"""
def modificar_lista(lista): 
    lista.append(100) 

mi_lista = [1, 2, 3] 
modificar_lista(mi_lista) 
print(mi_lista) # Salida: [1, 2, 3, 100] (modificado directamente) 

def modificar_entero(numero): 
    numero += 10 

mi_numero = 5 
modificar_entero(mi_numero) 
print(mi_numero) # Salida: 5 (no cambia, porque los enteros son inmutables) 

"""5. Gestión de memoria y recolector de basura. Python usa un sistema de gestión automática de memoria. Los objetos que no están referenciados son eliminados por el recolector de basura. Cuando asignas una nueva referencia, el recolector puede liberar el objeto si ya no está referenciado por ninguna variable. Ejemplo:"""
a = [1, 2, 3] 
b = a 
a = None # La lista sigue existiendo porque 'b' aún la referencia 

print(b) # Salida: [1, 2, 3] 

"""6. Copias (Superficial vs. Profunda). Copia superficial: Crea una nueva referencia, pero las subestructuras (como listas dentro de listas) siguen apuntando a los mismos objetos. Copia profunda: Copia todas las subestructuras, creando un nuevo objeto completo:"""
original = [[1, 2], [3, 4]] 
copia_superficial = original[:] 
copia_profunda = copy.deepcopy(original) 
copia_superficial[0].append(5) 
print(original) # Salida: [[1, 2, 5], [3, 4]] 
print(copia_superficial) # Salida: [[1, 2, 5], [3, 4]] 
copia_profunda[0].append(6) 
print(original) # Salida: [[1, 2, 5], [3, 4]] 
print(copia_profunda) # Salida: [[1, 2, 5, 6], [3, 4]] 

"""7. id() y direcciones de memoria. Cada objeto en Python tiene una dirección única en memoria, que se puede obtener usando id(). Esto te ayuda a verificar si dos variables apuntan al mismo objeto. Ejemplo:"""
a = [1, 2, 3] 
b = a 
c = a[:] 
print(id(a)) # Dirección de memoria de 'a' 
print(id(b)) # Igual que 'a' (misma referencia) 
print(id(c)) # Diferente de 'a' (copia) 

"""8. Scope y tiempo de vida. Variables locales: Existen solo dentro del bloque donde fueron definidas.
Variables globales: Existen mientras el programa esté en ejecución.
Los objetos referenciados solo desaparecen cuando su conteo de referencias llega a cero. Ejemplo:"""
def funcion(): 
x = 10 # Variable local 
print(x) 

funcion() # 
print(x) # Error: 'x' no está definida fuera de la función 

"""9. Mutabilidad e inmutabilidad en estructuras anidadas. En una estructura anidada, las partes internas pueden ser mutables, aunque la estructura externa sea inmutable. Ejemplo:"""
tupla = ([1, 2], 3) # Tupla inmutable, pero contiene una lista mutable 
tupla[0].append(4) 
print(tupla) # Salida: ([1, 2, 4], 3) 

"""10. isinstance y validación de tipos. Puedes usar isinstance para determinar si un objeto es mutable o inmutable, y actuar en consecuencia. Ejemplo:"""
def procesar_datos(dato): 
    if isinstance(dato, list): 
        dato.append(100) 
    elif isinstance(dato, (int, str)): 
        print("Dato inmutable:", dato) 

procesar_datos([1, 2, 3]) # Salida: [1, 2, 3, 100] 
procesar_datos(10) # Salida: Dato inmutable: 10 


"""Las buenas prácticas""" 

"""1. Evita modificaciones accidentales en objetos mutables. Problema: Los objetos mutables (listas, diccionarios, etc.) se modifican por referencia, lo que puede causar cambios inesperados si varias variables apuntan al mismo objeto. Solución: Usa copias si no deseas modificar el objeto original:"""
# Mala práctica: Modifica la lista original 
def agregar_elemento(lista): 
    lista.append(100) 

mi_lista = [1, 2, 3] 
agregar_elemento(mi_lista) 
print(mi_lista) # Salida: [1, 2, 3, 100] # Buena práctica: Usa una copia 

def agregar_elemento_copia(lista): 
    copia = lista[:] 
    copia.append(100) 
    return copia 

mi_lista = [1, 2, 3] 
nueva_lista = agregar_elemento_copia(mi_lista) 
print(mi_lista) # Salida: [1, 2, 3] 
print(nueva_lista) # Salida: [1, 2, 3, 100] 

"""2. Usa copy o deepcopy para objetos anidados. Problema: Una copia superficial ([:] o list.copy()) no copia objetos anidados; modifica el original. Solución: Usa el módulo copy para realizar copias profundas. Ejemplo:"""
lista_original = [[1, 2], [3, 4]] 
copia = lista_original[:] 
copia[0].append(5) 
print(lista_original) # Salida: [[1, 2, 5], [3, 4]] 

# Copia profunda 
copia_profunda = copy.deepcopy(lista_original) 
copia_profunda[0].append(6) 
print(lista_original) # Salida: [[1, 2, 5], [3, 4]] 
print(copia_profunda) # Salida: [[1, 2, 5, 6], [3, 4]] 

"""3. Evita reutilizar objetos mutables como valores predeterminados Problema: Los valores predeterminados mutables en funciones pueden persistir entre llamadas. Solución: Usa None como valor predeterminado y crea el objeto dentro de la función:"""
# Mala práctica 
def agregar_a_lista(elemento, lista=[]): 
    lista.append(elemento) 
    return lista 

print(agregar_a_lista(1)) # Salida: [1] 
print(agregar_a_lista(2)) # Salida: [1, 2] (problema) 

# Buena práctica 
def agregar_a_lista(elemento, lista=None): 
    if lista is None: 
        lista = [] 
        lista.append(elemento) 
        return lista 
print(agregar_a_lista(1)) # Salida: [1] 
print(agregar_a_lista(2)) # Salida: [2] 

"""4. Usa tipos inmutables para datos constantes. Problema: Modificar objetos constantes puede ser peligroso.
Solución: Usa tuplas en lugar de listas o frozenset en lugar de conjuntos cuando el objeto no deba cambiar. Ejemplo:"""
# Mejor usar tupla para datos constantes coordenadas = (10, 20) 
# Inmutable configuracion = frozenset({"opcion1", "opcion2"}) 
# Inmutable 
# Evita modificar objetos como lista o set si no es necesario 

"""5. Comprueba el tipo de referencia si trabajas con funciones. Problema: Las funciones pueden modificar el argumento si es mutable. Solución: Valida el tipo y usa copias cuando sea necesario. Ejemplo:"""
def procesar_datos(dato): 
    if isinstance(dato, list): # Trabaja con una copia si el dato es mutable 
        copia = dato[:] 
        copia.append("nuevo") 
        return copia 
    elif isinstance(dato, (int, str)): # Trabaja directamente si el dato es inmutable 
        return dato 

print(procesar_datos([1, 2, 3])) # Salida: [1, 2, 3, 'nuevo'] 

print(procesar_datos("Hola")) # Salida: Hola 

"""6. Documenta cómo manejas las referencias en tus funciones. Especifica claramente en los comentarios o la documentación si una función modifica el argumento original o trabaja con copias. Ejemplo:"""
def agregar_elemento(lista): """ Modifica la lista original añadiendo un nuevo elemento. """ 
    lista.append(10) 

def nueva_lista(lista): """ Devuelve una copia de la lista con un nuevo elemento añadido. """ 
    copia = lista[:] 
    copia.append(10) 
    return copia 




"""Las técnicas para manejar variables por valor y por referencia"""

"""1. Técnica de Copia Superficial. Úsala cuando necesites copiar un objeto no anidado (sin estructuras internas) o cuando solo quieras copiar el nivel superior de un objeto mutable. Ejemplo:"""
mi_lista = [1, 2, 3] 
copia_lista = mi_lista[:] # También puedes usar mi_lista.copy()
copia_lista.append(4) 
print(mi_lista) # Salida: [1, 2, 3] 
print(copia_lista) # Salida: [1, 2, 3, 4] 

"""2. Técnica de Copia Profunda. Úsala cuando trabajes con estructuras de datos anidadas (como listas de listas o diccionarios dentro de listas). Utiliza el módulo copy para asegurarte de que todas las capas del objeto sean copiadas:"""
original = [[1, 2], [3, 4]] 
copia_profunda = copy.deepcopy(original) 
copia_profunda[0].append(5) 
print(original) # Salida: [[1, 2], [3, 4]] 
print(copia_profunda) # Salida: [[1, 2, 5], [3, 4]] 

"""3. Técnica de Clonación Manual. En lugar de usar métodos automáticos ([:] o copy), puedes construir una nueva copia manualmente. Útil para objetos personalizados o estructuras complejas. Ejemplo:"""
mi_lista = [1, 2, 3] 
copia_manual = [item for item in mi_lista] # Reconstrucción de la lista 
copia_manual.append(4) 
print(mi_lista) # Salida: [1, 2, 3] 
print(copia_manual) # Salida: [1, 2, 3, 4] 

"""4. Técnica de Variables Inmutables. Usa tipos inmutables (como tuples, frozenset) para garantizar que los datos no puedan ser modificados. Esto es útil cuando quieres proteger valores constantes. Ejemplo:"""
# Usando tuplas en lugar de listas coordenadas = (10, 20) # Intentar modificar: coordenadas[0] = 15 causará un error 

"""5. Técnica de None para Valores Predeterminados. Evita usar mutables como valores predeterminados en funciones, ya que pueden causar efectos secundarios. Usa None y crea el objeto dentro de la función. Ejemplo:"""
def agregar_elemento(elemento, lista=None): 
    if lista is None: 
        lista = [] 
        lista.append(elemento) 
        return lista 

print(agregar_elemento(1)) # Salida: [1] 
print(agregar_elemento(2)) # Salida: [2] 

"""6. Técnica de Referencias Controladas. Cuando trabajas con objetos mutables, explícitamente haz copias para evitar modificar el objeto original, a menos que sea tu intención. Ejemplo:"""
def modificar_lista(lista): 
# Trabaja con una copia si no quieres afectar la original 
    copia = lista[:] 
    copia.append(10) 
    return copia 

mi_lista = [1, 2, 3] 
nueva_lista = modificar_lista(mi_lista) 
print(mi_lista) # Salida: [1, 2, 3] 
print(nueva_lista) # Salida: [1, 2, 3, 10] 

"""7. Técnica de Pasaje Explícito de Referencias. Si necesitas modificar el objeto original, asegúrate de documentarlo y diseñar tu función para que sea explícito. Ejemplo:"""
def modificar_directamente(lista): """Modifica la lista original.""" 
    lista.append(10) 

mi_lista = [1, 2, 3] 
modificar_directamente(mi_lista) 
print(mi_lista) # Salida: [1, 2, 3, 10] 

#8. Técnica de Validación de Tipos. Verifica si estás trabajando con un tipo mutable o inmutable para evitar errores. Usa isinstance. Ejemplo:
def procesar_dato(dato): 
    if isinstance(dato, list): # Trabaja con una copia para listas 
        return dato + [100] 
    elif isinstance(dato, (int, str)): # No necesitas copiar datos inmutables return dato 

print(procesar_dato([1, 2, 3])) # Salida: [1, 2, 3, 100] 
print(procesar_dato(10)) # Salida: 10 

#9. Técnica de Desempaquetado (Shallow vs Deep Unpacking). Usa desempaquetado para copiar partes específicas de un objeto. Ejemplo:
# Shallow unpacking 
a, *b = [1, 2, 3, 4] 
print(a) # Salida: 1 
print(b) # Salida: [2, 3, 4] 

#10. Técnica de Gestión de Memoria con id(). Usa id() para verificar si dos variables apuntan al mismo objeto en memoria. Esto es útil para depuración. Ejemplo:
a = [1, 2, 3] 
b = a c = a[:] 
print(id(a)) # ID de a 
print(id(b)) # Mismo ID que a (misma referencia) 
print(id(c)) # ID diferente (copia) 

