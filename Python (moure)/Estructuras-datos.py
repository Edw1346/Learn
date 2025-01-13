"""
Estructuras de Datos en Python: 
Las estructuras de datos para organizar, almacenar y manipular datos de manera eficiente. 
"""

#1. Estructuras de Datos Básicas
"""Listas (list): Es una colección ordenada y mutable de elementos. Permite elementos duplicados.
Características: Soporta cualquier tipo de dato (mezcla de tipos). Se accede por índice. Ejemplo:"""
# Crear una lista
mi_lista = [1, 2, 3, "hola", True]
print(mi_lista[0])  # Salida: 1

# Modificar elementos
mi_lista[1] = "mundo"
print(mi_lista)  # Salida: [1, 'mundo', 3, 'hola', True]

# Métodos comunes
mi_lista.append(5)  # Agregar elemento
mi_lista.remove(3)  # Eliminar elemento
print(mi_lista)  # Salida: [1, 'mundo', 'hola', True, 5]



#Tuplas (tuple): Es una colección ordenada e inmutable. Útil para datos que no deben cambiar. Ejemplo:
mi_tupla = (1, 2, 3, "hola")
print(mi_tupla[0])  # Salida: 1

# No se puede modificar directamente
# mi_tupla[1] = 5  # Error

# Desempaquetar tuplas
a, b, c, d = mi_tupla
print(a, d)  # Salida: 1 hola

#Conjuntos (set): Rs una colección desordenada y mutable de elementos únicos. Ejemplo:
mi_conjunto = {1, 2, 3, 4, 4}  # No permite duplicados
print(mi_conjunto)  # Salida: {1, 2, 3, 4}

# Métodos comunes
mi_conjunto.add(5)  # Agregar elemento
mi_conjunto.discard(3)  # Eliminar elemento
print(mi_conjunto)  # Salida: {1, 2, 4, 5}

#Diccionarios (dict): Es una colección desordenada de pares clave-valor. Ejemplo:
mi_diccionario = {"nombre": "Juan", "edad": 25}

# Acceder y modificar valores
print(mi_diccionario["nombre"])  # Salida: Juan
mi_diccionario["edad"] = 26
print(mi_diccionario)  # Salida: {'nombre': 'Juan', 'edad': 26}

# Métodos comunes
print(mi_diccionario.keys())   # Salida: dict_keys(['nombre', 'edad'])
print(mi_diccionario.values()) # Salida: dict_values(['Juan', 26])



"""2. Técnicas y Uso Avanzado de Estructuras de Datos"""

#Listas por Comprensión (List Comprehension). Una forma compacta y eficiente de crear listas. Ejemplo:
# Crear una lista con números al cuadrado
cuadrados = [x**2 for x in range(10)]
print(cuadrados)  # Salida: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#Diccionarios por Comprensión (Dict Comprehension). Similar a las listas por comprensión en diccionarios. Ejemplo:
# Crear un diccionario con cuadrados
cuadrados = {x: x**2 for x in range(5)}
print(cuadrados)  # Salida: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#Operaciones Matemáticas en Conjuntos  Realiza intersecciones, uniones y diferencias. Ejemplo:
conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

print(conjunto1 & conjunto2)  # Intersección: {3, 4}
print(conjunto1 | conjunto2)  # Unión: {1, 2, 3, 4, 5, 6}
print(conjunto1 - conjunto2)  # Diferencia: {1, 2}

#Ordenar Diccionarios. Ordena un diccionario por clave o valor. Ejemplo:
mi_diccionario = {"b": 2, "a": 1, "c": 3}

# Ordenar por clave

ordenado_por_clave = dict(sorted(mi_diccionario.items()))
print(ordenado_por_clave)  # Salida: {'a': 1, 'b': 2, 'c': 3}

# Ordenar por valor
ordenado_por_valor = dict(sorted(mi_diccionario.items(), key=lambda x: x[1]))
print(ordenado_por_valor)  # Salida: {'a': 1, 'b': 2, 'c': 3}

#Pilas y Colas (Estructuras Especializadas). 
#Pilas (stack): Usa listas o deque de la biblioteca collections. Ejemplo:
from collections import deque
pila = deque()
pila.append(1)  # Agregar
pila.append(2)
print(pila.pop())  # Eliminar último: 2

#Colas (queue): Usa deque para colas eficientes. Ejemplo:
cola = deque()
cola.append(1)
cola.append(2)
print(cola.popleft())  # Eliminar primero: 1

#Usar defaultdict para Diccionarios con Valores por Defecto. Simplifica trabajar con diccionarios que necesitan inicialización. Ejemplo:
from collections import defaultdict
mi_diccionario = defaultdict(int)
mi_diccionario["clave"] += 1
print(mi_diccionario["clave"])  # Salida: 1








"""Buenas Prácticas """

"""Elige la Estructura Adecuada para el Problema. 
1) Listas: Si necesitas una colección ordenada y mutable. 2) Tuplas: Para datos constantes que no cambiarán.
3) Conjuntos: Cuando necesitas valores únicos o realizar operaciones matemáticas como intersección o unión.
4) Diccionarios: Para búsquedas rápidas por clave o para almacenar pares clave-valor. Ejemplo:"""
# Correcto
usuarios = {"Juan": 25, "María": 30}  # Diccionario para asociar nombres con edades

# Incorrecto
usuarios = [["Juan", 25], ["María", 30]]  # Menos eficiente y claro

#Nombra las Variables Claramente. Usa nombres descriptivos que indiquen el propósito de la estructura de datos.
#Correcto:
edades_usuarios = {"Juan": 25, "María": 30}

#Incorrecto:
x = {"Juan": 25, "María": 30}  # El nombre "x" no es descriptivo

#Evita Estructuras Redundantes. No almacenes datos que ya están disponibles o que pueden calcularse sobre la marcha.
#Incorrecto:
numeros = [1, 2, 3]
cuadrados = [x**2 for x in numeros]  # Se recalcula constantemente

#Correcto:
numeros = [1, 2, 3]
cuadrados = {x: x**2 for x in numeros}  # Uso de diccionario para acceso rápido

#Usa List Comprehension y Generadores. Prefiere las comprensiones para construir listas, conjuntos o diccionarios de manera más legible y eficiente. Ejemplo:
# Crear una lista de cuadrados
cuadrados = [x**2 for x in range(10)]

#Comprueba la Existencia de Elementos Antes de Acceder. Usa operadores como in para evitar errores por acceder a elementos inexistentes. Ejemplo:
mi_diccionario = {"nombre": "Juan"}
if "edad" in mi_diccionario:
    print(mi_diccionario["edad"])  # Evita KeyError

#2. Buenas Prácticas Específicas por Estructura
#Listas: Evita el Uso de Listas para Búsquedas Frecuentes Las búsquedas en listas son lentas (O(n)).
#Correcto:
conjunto = {1, 2, 3}
print(2 in conjunto)  # Uso de un conjunto para búsquedas rápidas

#Evita Crecer o Reducir Listas en un Bucle. Las operaciones repetidas en listas pueden ser lentas. Usa estructuras más eficientes como deque.
#Incorrecto:
lista = []
for i in range(1000):
    lista.append(i)

#Correcto:
from collections import deque
lista = deque()
for i in range(1000):
    lista.append(i)


#Tuplas. Usa para Datos Constantes. Prefiere tuplas en lugar de listas cuando los datos no cambian, ya son más eficientes. Ejemplo:
coordenadas = (10, 20)  # Correcto: los datos son inmutables

#Conjuntos. Elimina Duplicados con Conjuntos. Úsalos para eliminar duplicados de forma eficiente. Ejemplo:
lista = [1, 2, 2, 3, 3, 4]
sin_duplicados = list(set(lista))
print(sin_duplicados)  # Salida: [1, 2, 3, 4]

#Usa Métodos de Conjunto para Operaciones Matemáticas. Prefiere usar operadores específicos (&, |, -) en lugar de recorrer manualmente los elementos. Ejemplo:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
interseccion = set1 & set2  # Correcto: más legible y eficiente

#Diccionarios. Usa get para Acceder a Elementos. Usa get para evitar errores al acceder a claves inexistentes. Ejemplo:
mi_diccionario = {"nombre": "Juan"}
edad = mi_diccionario.get("edad", "No especificada")
print(edad)  # Salida: No especificada

#Prefiere Diccionarios en Lugar de Listas para Datos Relacionales. Diccionarios para búsquedas rápidas basadas en claves.
usuarios = {"Juan": 25, "María": 30}

#Usa defaultdict para Valores por Defecto: Cuando necesites inicializar valores automáticamente, usa defaultdict. Ejemplo:
from collections import defaultdict
contador = defaultdict(int)
contador["clave"] += 1
print(contador)  # Salida: {'clave': 1}

#Pilas y Colas: Usa deque para Pilas y Colas. deque es más eficiente que las listas para estas estructuras. Ejemplo:
from collections import deque
pila = deque()
pila.append(1)
pila.append(2)
print(pila.pop())  # Salida: 2

#Usa Generadores para Datos Grandes. Usa generadores en lugar de listas cuando trabajes con grandes volúmenes de datos para ahorrar memoria. Ejemplo:
generador = (x**2 for x in range(1000000))  # Generador

#Usa Estructuras Avanzadas de collections. Explora estructuras avanzadas como Counter, OrderedDict, y ChainMap.
#Ejemplo con Counter:
from collections import Counter
conteo = Counter("mississippi")
print(conteo)  # Salida: Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})



"""Técnicas para Trabajar con Estructuras de Datos"""

"""1. Uso de append y extend
append agrega un único elemento.
extend fusiona una lista con otra. Ejemplo:"""
lista = [1, 2, 3]
lista.append(4)  # Salida: [1, 2, 3, 4]
lista.extend([5, 6])  # Salida: [1, 2, 3, 4, 5, 6]

#2. Uso de índices negativos. Permite acceder a los elementos desde el final. Ejemplo:
lista = [1, 2, 3, 4]
print(lista[-1])  # Salida: 4
print(lista[-2])  # Salida: 3

#1. List Comprehension. Crea listas de forma compacta y eficiente. Ejemplo:
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # Salida: [0, 2, 4, 6, 8]

#2. Ordenar listas con sorted y key. Personaliza el criterio de ordenación usando key. Ejemplo:
nombres = ["Juan", "Ana", "Pedro"]
nombres_ordenados = sorted(nombres, key=len)  # Ordenar por longitud
print(nombres_ordenados)  # Salida: ['Ana', 'Juan', 'Pedro']

#1. Uso de heapq para Colas de Prioridad. Gestiona elementos de manera eficiente según prioridades. Ejemplo:
import heapq
numeros = [4, 1, 7, 3, 8, 5]
heapq.heapify(numeros)  # Convierte la lista en un heap
print(heapq.heappop(numeros))  # Salida: 1 (mínimo elemento)

#2. Combinación de Listas con zip. Combina múltiples listas en pares de elementos. Ejemplo:
nombres = ["Ana", "Juan", "Pedro"]
edades = [25, 30, 35]
combinados = list(zip(nombres, edades))

print(combinados)  # Salida: [('Ana', 25), ('Juan', 30), ('Pedro', 35)]

#2. Técnicas para Diccionarios (dict)

#1. Acceso Seguro con get. Evita errores si una clave no existe. Ejemplo: 
diccionario = {"nombre": "Ana", "edad": 25}
print(diccionario.get("altura", "No disponible"))  # Salida: No disponible

#2. Agregar o Actualizar Elementos. Usa una clave para agregar o modificar un valor. Ejemplo:
diccionario = {"a": 1}
diccionario["b"] = 2  # Agregar
diccionario["a"] = 3  # Modificar
print(diccionario)  # Salida: {'a': 3, 'b': 2}

#1. Diccionarios por Comprensión. Genera diccionarios rápidamente. Ejemplo:
cuadrados = {x: x**2 for x in range(5)}
print(cuadrados)  # Salida: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#2. Iterar sobre Claves y Valores. Usa items para recorrer claves y valores simultáneamente. Ejemplo:
diccionario = {"a": 1, "b": 2}
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")

#Nivel Avanzado

#1. Ordenar Diccionarios por Valores o Claves. Usa sorted con key. Ejemplo:
diccionario = {"a": 3, "b": 1, "c": 2}
ordenado = dict(sorted(diccionario.items(), key=lambda x: x[1]))
print(ordenado)  # Salida: {'b': 1, 'c': 2, 'a': 3}

#2. Uso de defaultdict. Simplifica el manejo de valores por defecto. Ejemplo:
from collections import defaultdict
contador = defaultdict(int)
palabras = ["rojo", "azul", "rojo", "verde", "azul"]
for palabra in palabras:
    contador[palabra] += 1
print(contador)  # Salida: {'rojo': 2, 'azul': 2, 'verde': 1}

#3. Técnicas para Conjuntos (set)
#1. Eliminar Duplicados. Convierte una lista a un conjunto. Ejemplo:
lista = [1, 2, 2, 3]
conjunto = set(lista)
print(conjunto)  # Salida: {1, 2, 3}

#1. Operaciones Matemáticas. Realiza intersecciones, uniones y diferencias. Ejemplo:
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)  # Intersección: {3}
print(a | b)  # Unión: {1, 2, 3, 4, 5}

#1. Comparar Conjuntos. Usa operadores para verificar subconjuntos o superset. Ejemplo:
a = {1, 2}
b = {1, 2, 3}
print(a <= b)  # Verifica si `a` es subconjunto: True

#4. Técnicas para Tuplas (tuple)
#Desempaquetado de Tuplas. Asigna elementos a variables directamente. Ejemplo:
coordenadas = (10, 20)
x, y = coordenadas
print(x, y)  # Salida: 10 20

#Tuplas como Claves en Diccionarios. Usa tuplas para representar pares de datos únicos. Ejemplo:
rutas = {(0, 0): "Inicio", (1, 1): "Destino"}
print(rutas[(0, 0)])  # Salida: Inicio