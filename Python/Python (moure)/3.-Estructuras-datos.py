"""
Estructuras de Datos en Python: 
Las estructuras de datos para organizar, almacenar y manipular datos de manera eficiente. 
"""
#1. Estructuras de Datos Básicas
#Listas (list): Es una colección ordenada y mutable de elementos. Permite elementos duplicados. Características: Soporta cualquier tipo de dato (mezcla de tipos). Se accede por índice. Ejemplo:
# Crear una lista
mi_lista = [1, 2, 3, "hola", True]
print(mi_lista[0])  # Salida: 1

# Métodos comunes
"""1. append(). Qué hace: Agrega un elemento al final de la lista.
Limitaciones: Solo permite agregar un elemento a la vez. Usos: Ideal para construir listas dinámicamente."""
mi_lista = [1, 2, 3] 
mi_lista.append(4) 
print(mi_lista) # Salida: [1, 2, 3, 4] 

"""2. extend(). Qué hace: Agrega múltiples elementos (de un iterable) al final de la lista.
Limitaciones: Solo funciona con iterables (listas, tuplas, etc.). Usos: Combinar o expandir listas."""
mi_lista = [1, 2, 3] 
mi_lista.extend([4, 5]) 
print(mi_lista) # Salida: [1, 2, 3, 4, 5] 

"""3. insert(). Qué hace: Inserta un elemento en una posición específica.
Limitaciones: Puede ralentizarse con listas muy grandes, ya que desplaza elementos. Usos: Cuando necesitas insertar algo en un índice específico."""
mi_lista = [1, 3, 4] 
mi_lista.insert(1, 2) 
print(mi_lista) # Salida: [1, 2, 3, 4] 

"""4. remove(). Qué hace: Elimina la primera aparición de un elemento.
Limitaciones: Lanza un error si el elemento no está en la lista. Usos: Para eliminar un elemento conocido."""
mi_lista = [1, 2, 3, 2] 
mi_lista.remove(2) 
print(mi_lista) # Salida: [1, 3, 2] 

"""5. pop(). Qué hace: Elimina y retorna el elemento de un índice específico (por defecto, el último).
Limitaciones: Lanza un error si la lista está vacía. Usos: Cuando necesitas el valor eliminado."""
mi_lista = [1, 2, 3] 
elemento = mi_lista.pop() 
print(mi_lista) # Salida: [1, 2] 
print(elemento) # Salida: 3 

"""6. clear(). Qué hace: Elimina todos los elementos de la lista.
Limitaciones: No elimina la lista como tal, solo sus elementos. Usos: Reiniciar una lista sin eliminarla."""
mi_lista = [1, 2, 3] 
mi_lista.clear() 
print(mi_lista) # Salida: [] 

"""7. index(). Qué hace: Retorna el índice de la primera aparición de un elemento.
Limitaciones: Lanza un error si el elemento no está en la lista. Usos: Encontrar la posición de un elemento."""
mi_lista = [1, 2, 3, 2] 
posicion = mi_lista.index(2) 
print(posicion) # Salida: 1 

"""8. count(). Qué hace: Retorna cuántas veces aparece un elemento en la lista.
Limitaciones: Puede ser lento en listas muy grandes. Usos: Contar ocurrencias específicas."""
mi_lista = [1, 2, 2, 3] 
repeticiones = mi_lista.count(2) 
print(repeticiones) # Salida: 2 

"""9. sort(). Qué hace: Ordena la lista en su lugar (ascendente por defecto).
Limitaciones: Modifica la lista original; solo funciona con tipos comparables. Usos: Ordenar listas de números o cadenas."""

mi_lista = [3, 1, 2] 
mi_lista.sort() 
print(mi_lista) # Salida: [1, 2, 3] 

"""10. reverse(). Qué hace: Invierte el orden de los elementos de la lista.
Limitaciones: Modifica la lista original. Usos: Cuando necesitas invertir el orden de los elementos."""
mi_lista = [1, 2, 3] 
mi_lista.reverse() 
print(mi_lista) # Salida: [3, 2, 1] 

"""11. copy(). Qué hace: Crea una copia superficial de la lista.
Limitaciones: No copia estructuras anidadas (es decir, "shallow"). Usos: Clonar una lista para evitar modificar la original."""
mi_lista = [1, 2, 3] 
copia = mi_lista.copy() 
copia.append(4) 
print(mi_lista) # Salida: [1, 2, 3] 
print(copia) # Salida: [1, 2, 3, 4] 


"""Métodos especiales"""

"""1. __len__(). Qué hace: Retorna la cantidad de elementos en la lista.
Limitaciones: Es utilizado internamente por len(), no se llama directamente. Usos: Saber el tamaño de una lista."""
mi_lista = [1, 2, 3] 
tamaño = mi_lista.__len__() 
print(tamaño) # Salida: 3 # Normalmente usarías len(mi_lista), pero esto es lo que ocurre internamente. 

"""2. __getitem__(index). Qué hace: Retorna el elemento en el índice especificado.
Limitaciones: Lanza un error si el índice está fuera del rango. Usos: Es lo que ocurre internamente al usar corchetes para acceder a elementos."""
mi_lista = [1, 2, 3] 
elemento = mi_lista.__getitem__(1) 
print(elemento) # Salida: 2 # Equivalente a hacer mi_lista[1]. 

"""3. __setitem__(index, value). Qué hace: Asigna un valor a un índice específico.
Limitaciones: Lanza un error si el índice está fuera del rango. Usos: Se utiliza al modificar elementos con corchetes."""
mi_lista = [1, 2, 3] 
mi_lista.__setitem__(1, 99) 
print(mi_lista) # Salida: [1, 99, 3] # Equivalente a hacer mi_lista[1] = 99. 

"""4. __delitem__(index). Qué hace: Elimina el elemento en un índice específico.
Limitaciones: Lanza un error si el índice está fuera del rango. Usos: Internamente utilizado al usar del."""
mi_lista = [1, 2, 3] 
mi_lista.__delitem__(1) 
print(mi_lista) # Salida: [1, 3] # Equivalente a hacer del mi_lista[1]. 

"""5. __iter__(). Qué hace: Retorna un iterador para la lista.
Limitaciones: No se usa directamente; se invoca al iterar con un bucle for. Usos: Permite recorrer elementos uno por uno."""
mi_lista = [1, 2, 3] 
iterador = mi_lista.__iter__() 
print(next(iterador)) # Salida: 1 print(next(iterador)) # Salida: 2 

"""6. __contains__(item). Qué hace: Retorna True si el elemento está en la lista, False si no.
Limitaciones: Utilizado internamente por in. Usos: Comprobar si un elemento existe en la lista."""
mi_lista = [1, 2, 3] 
existe = mi_lista.__contains__(2) 
print(existe) # Salida: True # Equivalente a hacer 2 in mi_lista. 

"""7. __reversed__(). Qué hace: Retorna un iterador que recorre la lista en orden inverso.
Limitaciones: Devuelve el iterador, pero no modifica la lista original. Usos: Para iterar al revés sin usar [::-1]."""

mi_lista = [1, 2, 3] 
for elemento in mi_lista.__reversed__(): 
    print(elemento) # Salida: 3, luego 2, luego 1 

"""8. __add__(other). Qué hace: Combina dos listas y retorna una nueva.
Limitaciones: Solo funciona con listas; no modifica las originales. Usos: Sumar listas directamente."""
mi_lista = [1, 2] 
otra_lista = [3, 4] 
nueva_lista = mi_lista.__add__(otra_lista) 
print(nueva_lista) # Salida: [1, 2, 3, 4] Equivalente a hacer mi_lista + otra_lista. 

"""9. __mul__(times). Qué hace: Repite los elementos de la lista el número de veces indicado.
Limitaciones: Solo acepta números enteros como argumento. Usos: Para crear repeticiones."""
mi_lista = [1, 2] 
repetida = mi_lista.__mul__(3) 
print(repetida) # Salida: [1, 2, 1, 2, 1, 2] 
# Equivalente a hacer mi_lista * 3. 

"""10. __eq__(other). Qué hace: Compara si dos listas son iguales.
Limitaciones: La comparación es elemento por elemento y sensible al orden. Usos: Para verificar igualdad."""
mi_listua = [1, 2, 3] 
otra_lista = [1, 2, 3] 
son_iguales = mi_lista.__eq__(otra_lista) 
print(son_iguales) # Salida: True 
# Equivalente a hacer mi_lista == otra_lista. 




#Tuplas (tuple): Es una colección ordenada e inmutable. Útil para datos que no deben cambiar. Ejemplo:
mi_tupla = (1, 2, 3, "hola")
print(mi_tupla[0])  # Salida: 1

# No se puede modificar directamente
# mi_tupla[1] = 5  # Error

# Desempaquetar tuplas
a, b, c, d = mi_tupla
print(a, d)  # Salida: 1 hola

"""métodos normales"""

"""1. count(). ¿Qué hace? Devuelve el número de veces que un elemento específico aparece en la tupla.
Limitaciones: Solo busca coincidencias exactas. No funciona con comparaciones complejas o búsqueda parcial. 
Usos: Útil para contar elementos repetidos dentro de una tupla. Ejemplo: """
tupla = (1, 2, 3, 2, 4, 2) 
print(tupla.count(2)) # Salida: 3 

"""2. index(). ¿Qué hace? Devuelve el índice de la primera aparición de un elemento específico en la tupla. Si el elemento no está en la tupla, lanza un error ValueError. 
Limitaciones: Solo devuelve el índice de la primera aparición. No funciona con elementos ausentes.
Usos: Se usa para encontrar la posición de un elemento específico. Ejemplo: """
tupla = (10, 20, 30, 20, 40) 
print(tupla.index(20)) # Salida: 1 

"""métodos mágicos """
#1. __len__. ¿Qué hace? Devuelve el número de elementos en la tupla. Este método es llamado internamente cuando usas la función len() con una tupla. Ejemplo: 
tupla = (1, 2, 3) 
print(tupla.__len__()) # Salida: 3 

# Equivalente a: 
print(len(tupla)) # Salida: 3 

#2. __getitem__. ¿Qué hace? Permite acceder a un elemento de la tupla por su índice. Se invoca cuando usas la notación tupla[indice]. Ejemplo: 
tupla = (10, 20, 30) 
print(tupla.__getitem__(1)) # Salida: 20 
# Equivalente a: 
print(tupla[1]) # Salida: 20 

#3. __iter__. ¿Qué hace? Devuelve un iterador para la tupla, permitiendo que pueda ser recorrida en un bucle for. Ejemplo: 
tupla = (1, 2, 3) 
iterador = tupla.__iter__() 
print(next(iterador)) # Salida: 1 
print(next(iterador)) # Salida: 2 
print(next(iterador)) # Salida: 3 

#4. __contains__. ¿Qué hace? Verifica si un elemento está en la tupla. Este método es invocado cuando usas el operador in. Ejemplo: 
tupla = (1, 2, 3) 
print(tupla.__contains__(2)) # Salida: True 
# Equivalente a: 
print(2 in tupla) # Salida: True 

#5. __add__. ¿Qué hace? Combina dos tuplas y devuelve una nueva tupla con los elementos concatenados. Se invoca con el operador +. Ejemplo: 
tupla1 = (1, 2) 
tupla2 = (3, 4) 
print(tupla1.__add__(tupla2)) # Salida: (1, 2, 3, 4) 
# Equivalente a: 
print(tupla1 + tupla2) # Salida: (1, 2, 3, 4) 

#6. __mul__. ¿Qué hace? Permite repetir los elementos de una tupla un número específico de veces. Se invoca con el operador *. Ejemplo: 
tupla = (1, 2) 
print(tupla.__mul__(3)) # Salida: (1, 2, 1, 2, 1, 2) 
# Equivalente a: 
print(tupla * 3) # Salida: (1, 2, 1, 2, 1, 2) 

"""7. __eq__, __ne__, __lt__, __le__, __gt__, __ge__. ¿Qué hacen? Permiten comparar tuplas con otros objetos (usualmente, con otras tuplas).  __eq__: Verifica igualdad.
__ne__: Verifica desigualdad.
__lt__: Verifica si una tupla es menor que otra.
__le__: Verifica si una tupla es menor o igual a otra.
__gt__: Verifica si una tupla es mayor que otra.
__ge__: Verifica si una tupla es mayor o igual a otra. Ejemplo: """
tupla1 = (1, 2) 
tupla2 = (1, 3) 
print(tupla1.__eq__(tupla2)) # Salida: False 
print(tupla1.__lt__(tupla2)) # Salida: True 
# Equivalente a: 
print(tupla1 == tupla2) # Salida: False 
print(tupla1 < tupla2) # Salida: True 

#8. __hash__. ¿Qué hace? Devuelve un valor hash único para la tupla. Este método permite que las tuplas sean utilizadas como claves en diccionarios o elementos de un conjunto (set). Ejemplo: 
tupla = (1, 2, 3) 
print(tupla.__hash__()) # Salida: Un valor hash (puede variar) 

"""9. __repr__ y __str__. ¿Qué hacen? 
__repr__: Devuelve una representación formal de la tupla (útil para desarrolladores).

__str__: Devuelve una representación legible (útil para usuarios). Ejemplo: """
tupla = (1, 2, 3) 
print(tupla.__repr__()) # Salida: '(1, 2, 3)' 
print(tupla.__str__()) # Salida: '(1, 2, 3)' 





#Conjuntos (set): Rs una colección desordenada y mutable de elementos únicos. Ejemplo:
mi_conjunto = {1, 2, 3, 4, 4}  # No permite duplicados
print(mi_conjunto)  # Salida: {1, 2, 3, 4}


"""Métodos normales"""

"""1. add(elemento). ¿Qué hace? Añade un elemento al conjunto. Si el elemento ya está presente, no lo añade.
Limitaciones:  Solo acepta elementos inmutables (por ejemplo, no se pueden añadir listas o conjuntos). Ejemplo: """
conjunto = {1, 2, 3} 
conjunto.add(4) 
print(conjunto) # Salida: {1, 2, 3, 4} 

"""2. remove(elemento). ¿Qué hace? Elimina un elemento del conjunto. Si el elemento no está presente, lanza un error KeyError. Limitaciones:  Usar con precaución si no estás seguro de que el elemento esté presente. Ejemplo: """
conjunto = {1, 2, 3} 
conjunto.remove(2) 
print(conjunto) # Salida: {1, 3} 

"""3. discard(elemento). ¿Qué hace? Elimina un elemento del conjunto si está presente. Si no está presente, no lanza error.
Limitaciones:  Es más seguro que remove cuando no sabes si el elemento está en el conjunto. Ejemplo:""" 
conjunto = {1, 2, 3} 
conjunto.discard(2) 
conjunto.discard(5) # No lanza error 
print(conjunto) # Salida: {1, 3} 

"""4. pop(). ¿Qué hace? Elimina y devuelve un elemento arbitrario del conjunto. Si el conjunto está vacío, lanza un error KeyError. Limitaciones:  No se garantiza qué elemento se elimina, ya que los conjuntos son desordenados. Ejemplo: """
conjunto = {1, 2, 3} 
elemento = conjunto.pop() 
print(elemento) # Salida: 1 (puede variar) 
print(conjunto) # Salida: {2, 3} (puede variar) 

#5. clear(). ¿Qué hace? Elimina todos los elementos del conjunto, dejándolo vacío. Ejemplo: 
conjunto = {1, 2, 3} 
conjunto.clear() 
print(conjunto) # Salida: set() 

#6. union(*otros). ¿Qué hace? Devuelve un nuevo conjunto que contiene la unión de los elementos del conjunto original y los otros conjuntos dados. Ejemplo: 
conjunto1 = {1, 2, 3} 
conjunto2 = {3, 4, 5} 
resultado = conjunto1.union(conjunto2) 
print(resultado) # Salida: {1, 2, 3, 4, 5} 

#7. update(*otros). ¿Qué hace? Añade los elementos de otros conjuntos al conjunto actual (modifica el conjunto original): 
conjunto = {1, 2, 3} 
conjunto.update({3, 4, 5}) 
print(conjunto) # Salida: {1, 2, 3, 4, 5} 

#8. intersection(*otros). ¿Qué hace? Devuelve un nuevo conjunto con los elementos que están presentes en todos los 
#conjuntos dados. Ejemplo: 
conjunto1 = {1, 2, 3} 
conjunto2 = {2, 3, 4} 
resultado = conjunto1.intersection(conjunto2) 
print(resultado) # Salida: {2, 3} 

#9. intersection_update(*otros). ¿Qué hace? Modifica el conjunto actual para que solo contenga los elementos que están presentes en todos los conjuntos dados. Ejemplo: 
conjunto = {1, 2, 3} 
conjunto.intersection_update({2, 3, 4}) 
print(conjunto) # Salida: {2, 3} 

#10. difference(*otros). ¿Qué hace? Devuelve un nuevo conjunto con los elementos que están en el conjunto original pero no en los otros conjuntos dados. Ejemplo: 
conjunto1 = {1, 2, 3} 
conjunto2 = {2, 3, 4} 
resultado = conjunto1.difference(conjunto2) 
print(resultado) # Salida: {1} 

#11. difference_update(*otros). ¿Qué hace? Modifica el conjunto actual eliminando los elementos que están en los otros conjuntos dados. Ejemplo: 
conjunto = {1, 2, 3} 
conjunto.difference_update({2, 3}) 
print(conjunto) # Salida: {1} 

#12. symmetric_difference(otro). ¿Qué hace? Devuelve un nuevo conjunto con los elementos que están en uno u otro conjunto, pero no en ambos. Ejemplo: 
conjunto1 = {1, 2, 3} 
conjunto2 = {3, 4, 5} 
resultado = conjunto1.symmetric_difference(conjunto2) 
print(resultado) # Salida: {1, 2, 4, 5} 

#13. symmetric_difference_update(otro). ¿Qué hace? Modifica el conjunto actual para que contenga solo los elementos que están en uno u otro conjunto, pero no en ambos. Ejemplo: 
conjunto = {1, 2, 3} 
conjunto.symmetric_difference_update({3, 4, 5}) 
print(conjunto) # Salida: {1, 2, 4, 5} 

#14. isdisjoint(otro). ¿Qué hace? Devuelve True si el conjunto actual no tiene elementos en común con el otro conjunto: 
conjunto1 = {1, 2, 3} 
conjunto2 = {4, 5, 6} 
print(conjunto1.isdisjoint(conjunto2)) # Salida: True 

#15. issubset(otro). ¿Qué hace? Devuelve True si todos los elementos del conjunto actual están en el otro conjunto: 
conjunto1 = {1, 2} 
conjunto2 = {1, 2, 3} 
print(conjunto1.issubset(conjunto2)) # Salida: True 

#16. issuperset(otro). ¿Qué hace? Devuelve True si todos los elementos del otro conjunto están en el conjunto actual: 
conjunto1 = {1, 2, 3} 
conjunto2 = {1, 2} 
print(conjunto1.issuperset(conjunto2)) # Salida: True 


"""métodos especiales"""

#1. __len__(). ¿Qué hace? Devuelve el número de elementos en el conjunto. Es utilizado por la función len(). Ejemplo: 
conjunto = {1, 2, 3} 
print(len(conjunto)) # Salida: 3 

#2. __iter__(). ¿Qué hace? Permite iterar sobre el conjunto utilizando un bucle for o una comprensión de listas. Ejemplo: 
conjunto = {1, 2, 3} 
for elemento in conjunto: 
    print(elemento) # Salida: 1, 2, 3 (en orden arbitrario) 

#3. __contains__(elemento). ¿Qué hace? Permite verificar si un elemento está en el conjunto usando el operador in: 
conjunto = {1, 2, 3} 
print(2 in conjunto) # Salida: True 
print(5 in conjunto) # Salida: False 

#4. __eq__(otro_conjunto). ¿Qué hace? Verifica si dos conjuntos son iguales (contienen los mismos elementos). Ejemplo: 
conjunto1 = {1, 2, 3} 
conjunto2 = {3, 2, 1} 
print(conjunto1 == conjunto2) # Salida: True 

#5. __ne__(otro_conjunto). ¿Qué hace? Verifica si dos conjuntos no son iguales. Ejemplo: 
conjunto1 = {1, 2, 3} 
conjunto2 = {4, 5, 6} 
print(conjunto1 != conjunto2) # Salida: True 

#6. __or__(otro_conjunto). ¿Qué hace? Realiza la unión de dos conjuntos usando el operador |. Ejemplo: 
conjunto1 = {1, 2} 
conjunto2 = {3, 4} 
print(conjunto1 | conjunto2) # Salida: {1, 2, 3, 4} 

#7. __and__(otro_conjunto). ¿Qué hace? Realiza la intersección de dos conjuntos usando el operador &. Ejemplo: 
conjunto1 = {1, 2, 3} 
conjunto2 = {2, 3, 4} 
print(conjunto1 & conjunto2) # Salida: {2, 3} 

#8. __sub__(otro_conjunto). ¿Qué hace? Realiza la diferencia de dos conjuntos usando el operador -. Ejemplo: 
conjunto1 = {1, 2, 3} 
conjunto2 = {2, 3, 4} 
print(conjunto1 - conjunto2) # Salida: {1} 

#9. __xor__(otro_conjunto). ¿Qué hace? Realiza la diferencia simétrica entre dos conjuntos usando el operador ^. Ejemplo: 
conjunto1 = {1, 2, 3} 
conjunto2 = {3, 4, 5} 
print(conjunto1 ^ conjunto2) # Salida: {1, 2, 4, 5} 

#10. __le__(otro_conjunto). ¿Qué hace? Verifica si el conjunto actual es un subconjunto del otro (<=). Ejemplo: 
conjunto1 = {1, 2} 
conjunto2 = {1, 2, 3} 
print(conjunto1 <= conjunto2) # Salida: True 

#11. __lt__(otro_conjunto). ¿Qué hace? Verifica si el conjunto actual es un subconjunto propio del otro (<). Ejemplo: 
conjunto1 = {1, 2} 
conjunto2 = {1, 2, 3} 
print(conjunto1 < conjunto2) # Salida: True 

#12. __ge__(otro_conjunto). ¿Qué hace? Verifica si el conjunto actual es un superconjunto del otro (>=). Ejemplo: 
conjunto1 = {1, 2, 3} 
conjunto2 = {1, 2} 
print(conjunto1 >= conjunto2) # Salida: True 

#13. __gt__(otro_conjunto). ¿Qué hace? Verifica si el conjunto actual es un superconjunto propio del otro (>). Ejemplo: 
conjunto1 = {1, 2, 3} 
conjunto2 = {1, 2} 
print(conjunto1 > conjunto2) # Salida: True 

#14. __repr__(). ¿Qué hace? Devuelve una representación legible del conjunto. Es utilizado cuando el conjunto se imprime: 
conjunto = {1, 2, 3} 
print(repr(conjunto)) # Salida: {1, 2, 3} 

"""15. __eq__() y __hash__() en conjuntos inmutables (frozenset)
¿Qué hacen?  __eq__: Verifica si dos frozenset son iguales.
__hash__: Permite usar frozenset como clave en un diccionario o elemento en otro conjunto. Ejemplo: """
conjunto1 = frozenset({1, 2, 3}) 
conjunto2 = frozenset({3, 2, 1}) 
print(conjunto1 == conjunto2) # Salida: True 
diccionario = {conjunto1: "valor"} 
print(diccionario) # Salida: {frozenset({1, 2, 3}): 'valor'} 





#Diccionarios (dict): Es una colección desordenada de pares clave-valor. Ejemplo:
mi_diccionario = {"nombre": "Juan", "edad": 25}

# Acceder y modificar valores
print(mi_diccionario["nombre"])  # Salida: Juan
mi_diccionario["edad"] = 26
print(mi_diccionario)  # Salida: {'nombre': 'Juan', 'edad': 26}


"""Métodos normales"""

"""1. clear(). ¿Qué hace?. Elimina todos los elementos del diccionario.
Limitaciones: No devuelve nada, solo limpia el diccionario en su lugar. Ejemplo: """
diccionario = {"a": 1, "b": 2} 
diccionario.clear() 
print(diccionario) # Salida: {} 

"""2. copy(). ¿Qué hace?. Devuelve una copia superficial del diccionario.
Limitaciones: Si el diccionario contiene estructuras anidadas (como listas), las referencias internas no se copian profundamente. Ejemplo: """
diccionario = {"a": 1, "b": [2, 3]} 
copia = diccionario.copy() 
copia["b"].append(4) 
print(diccionario) # Salida: {'a': 1, 'b': [2, 3, 4]} 

"""3. fromkeys(iterable, valor=None). ¿Qué hace?. Crea un nuevo diccionario claves del iterable y valores establecidos en valor. Limitaciones: Si el valor es mutable, todas las claves compartirán la misma referencia al objeto mutable. Ejemplo: """
claves = ["a", "b", "c"] 
diccionario = dict.fromkeys(claves, 0) 
print(diccionario) # Salida: {'a': 0, 'b': 0, 'c': 0} 

"""4. get(clave, valor_por_defecto=None). ¿Qué hace?. Devuelve el valor asociado a la clave. Si la clave no existe, devuelve valor_por_defecto. Limitaciones: No lanza una excepción si la clave no existe, a diferencia de acceder directamente con diccionario[clave]. Ejemplo: """
diccionario = {"a": 1, "b": 2} 
print(diccionario.get("a")) # Salida: 1 
print(diccionario.get("c", "No existe")) # Salida: No existe 

"""5. items(). ¿Qué hace?. Devuelve una vista de todos los pares clave-valor como tuplas.
Limitaciones: La vista se actualiza automáticamente si el diccionario cambia. Ejemplo: """
diccionario = {"a": 1, "b": 2} 
print(diccionario.items()) # Salida: 
dict_items([('a', 1), ('b', 2)]) 


"""6. keys(). ¿Qué hace?. Devuelve una vista de todas las claves del diccionario.
Limitaciones: La vista refleja cambios en el diccionario. Ejemplo: """
diccionario = {"a": 1, "b": 2} 
print(diccionario.keys()) # Salida: dict_keys(['a', 'b']) 

"""7. pop(clave, valor_por_defecto=None). ¿Qué hace?. Elimina la clave especificada y devuelve su valor. Si la clave no existe, devuelve valor_por_defecto si se proporciona; de lo contrario, lanza un error.
Limitaciones: Lanza KeyError si la clave no existe y no se proporciona un valor por defecto. Ejemplo: """
diccionario = {"a": 1, "b": 2} 
valor = diccionario.pop("a") 
print(valor) # Salida: 1 
print(diccionario) # Salida: {'b': 2} 

"""8. popitem(). ¿Qué hace?. Elimina y devuelve el último par clave-valor como una tupla.
Limitaciones: Lanza KeyError si el diccionario está vacío. Ejemplo: """
diccionario = {"a": 1, "b": 2} 
clave_valor = diccionario.popitem() 
print(clave_valor) # Salida: ('b', 2) 
print(diccionario) # Salida: {'a': 1} 

"""9. setdefault(clave, valor_por_defecto=None). ¿Qué hace?. Devuelve el valor de la clave si existe. Si no existe, la añade con el valor por defecto. Limitaciones: Si la clave ya existe, no modifica el diccionario. Ejemplo: """
diccionario = {"a": 1} 
valor = diccionario.setdefault("b", 2) 
print(valor) # Salida: 2 
print(diccionario) # Salida: {'a': 1, 'b': 2} 

"""10. update(otro_diccionario). ¿Qué hace?. Actualiza el diccionario con los pares clave-valor de otro diccionario o iterable.
Limitaciones: Si una clave ya existe, su valor será sobrescrito. Ejemplo: """
diccionario = {"a": 1} 
diccionario.update({"b": 2, "a": 3}) 
print(diccionario) # Salida: {'a': 3, 'b': 2} 

"""11. values(). ¿Qué hace? Devuelve una vista de todos los valores del diccionario.
Limitaciones: No permite modificar los valores directamente desde la vista. Ejemplo: """
diccionario = {"a": 1, "b": 2} 
print(diccionario.values()) # Salida: dict_values([1, 2]) 


"""Métodos mágicos"""

"""1. __getitem__(self, key). ¿Qué hace? Permite acceder al valor de una clave como si fuese un índice (diccionario[clave]).
Usos: Se utiliza para definir cómo se recuperan los valores de un diccionario personalizado. Ejemplo: """
class MiDiccionario: 
    def __init__(self): 
        self.datos = {"a": 1, "b": 2} 

    def __getitem__(self, key): 
        return self.datos.get(key, "Clave no encontrada") 

dic = MiDiccionario() 
print(dic["a"]) # Salida: 1 print(dic["c"]) # Salida: Clave no encontrada 

"""2. __setitem__(self, key, value). ¿Qué hace? Define cómo se asignan valores a las claves (diccionario[clave] = valor).
Usos: Permite agregar lógica personalizada al agregar o modificar elementos. Ejemplo: """
class MiDiccionario: 
    def __init__(self): 
        self.datos = {} 

    def __setitem__(self, key, value): 
        print(f"Asignando {value} a la clave '{key}'") 
        self.datos[key] = value 
        dic = MiDiccionario() 
        dic["a"] = 10 # Salida: Asignando 10 a la clave 'a' 
        print(dic.datos) # Salida: {'a': 10} 

"""3. __delitem__(self, key). ¿Qué hace? Permite eliminar claves del diccionario (del diccionario[clave]).
Usos: Útil para agregar lógica o restricciones al eliminar elementos. Ejemplo: """
class MiDiccionario: 
    def __init__(self): 
        self.datos = {"a": 1, "b": 2} 

    def __delitem__(self, key): 
        print(f"Eliminando clave '{key}'") 
        del self.datos[key] 

dic = MiDiccionario() 
del dic["a"] # Salida: Eliminando clave 'a' 
print(dic.datos) # Salida: {'b': 2} 

"""4. __contains__(self, key). ¿Qué hace? Permite verificar si una clave está en el diccionario usando el operador in.
Usos: Personaliza el comportamiento de la verificación de existencia. Ejemplo: """
class MiDiccionario: 
    def __init__(self): 
        self.datos = {"a": 1, "b": 2} 

    def __contains__(self, key): 
        return key in self.datos 
    
dic = MiDiccionario() 
print("a" in dic) # Salida: True 
print("c" in dic) # Salida: False 

"""5. __iter__(self). ¿Qué hace? Devuelve un iterador para recorrer las claves del diccionario.
Usos: Necesario para que la clase sea iterable con for. Ejemplo: """
class MiDiccionario: 
    def __init__(self): 
        self.datos = {"a": 1, "b": 2} 

    def __iter__(self): 
        return iter(self.datos) 

dic = MiDiccionario() 
for clave in dic: 
    print(clave) # Salida: 'a' 'b' 

"""6. __len__(self). ¿Qué hace? Devuelve el número de elementos del diccionario (len(diccionario)).
Usos: Personaliza cómo se calcula el tamaño del diccionario. Ejemplo: """
class MiDiccionario: 
    def __init__(self): 
        self.datos = {"a": 1, "b": 2} 

    def __len__(self): 
        return len(self.datos) 
    
dic = MiDiccionario() 
print(len(dic)) # Salida: 2 

"""7. __repr__(self). ¿Qué hace? Devuelve una representación en cadena del diccionario (por ejemplo, en la consola).

Usos: Personaliza cómo se representa el diccionario al imprimirlo. Ejemplo: """
class MiDiccionario: 
    def __init__(self): 
        self.datos = {"a": 1, "b": 2} 

    def __repr__(self): 
        return f"MiDiccionario({self.datos})"          

dic = MiDiccionario() 
print(dic) # Salida: MiDiccionario({'a': 1, 'b': 2}) 

"""8. __eq__(self, other). ¿Qué hace? Define el comportamiento de igualdad (==) entre dos diccionarios.
Usos: Compara diccionarios personalizados según criterios específicos. Ejemplo: """
class MiDiccionario:
    def __init__(self, datos): 
        self.datos = datos 
        
    def __eq__(self, other): 
        return self.datos == other.datos 
            
dic1 = MiDiccionario({"a": 1, "b": 2}) 
dic2 = MiDiccionario({"a": 1, "b": 2}) 
print(dic1 == dic2) # Salida: True 

"""9. __missing__(self, key). ¿Qué hace? Se invoca automáticamente si una clave no existe en el diccionario.
Usos: Útil para manejar valores predeterminados al acceder a claves inexistentes. Ejemplo: """
class MiDiccionario(dict): 
    def __missing__(self, key): 
        return f"Clave '{key}' no encontrada" 

dic = MiDiccionario({"a": 1}) 
print(dic["b"]) # Salida: Clave 'b' no encontrada 






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




"""Métodos mágicos"""

"""1. ¿Qué son los métodos mágicos?
Los métodos mágicos (también llamados métodos especiales) son métodos predefinidos en Python que permiten personalizar el comportamiento de objetos en situaciones donde el lenguaje realiza operaciones de manera automática, como cuando usamos operadores o funciones especiales.

Estos métodos están envueltos en dobles guiones bajos (__init__, __add__, __iter__, etc.) y son invocados implícitamente cuando realizas ciertas acciones con objetos (por ejemplo, cuando usas un + entre dos objetos, Python usa internamente el método __add__).

Permiten interactuar con operadores y funciones estándar de Python, como la suma, la comparación, la iteración, etc., pero permiten modificar su comportamiento según las necesidades de tu código.

2. ¿Por qué utilizamos métodos mágicos si ya existen métodos normales?
Los métodos mágicos se utilizan cuando quieres personalizar el comportamiento de los objetos para que interactúen de forma más natural con los operadores o con las estructuras de control del lenguaje (como los bucles for o las comparaciones ==).

Aunque existen métodos normales (como append para listas), los métodos mágicos permiten que puedas sobrecargar o redefinir cómo ciertos operadores y acciones predeterminadas interactúan con tus objetos, especialmente en el contexto de programación orientada a objetos (OOP).

Se usan principalmente en clases personalizadas cuando deseas que tus objetos tengan comportamientos similares a los tipos de datos predefinidos de Python (listas, enteros, cadenas, etc.).

3. ¿Qué diferencia hay entre métodos mágicos y métodos normales?
Métodos normales: Son los métodos que Python proporciona por defecto para operar sobre sus tipos de datos. Por ejemplo, append para agregar un elemento a una lista o pop para eliminar el último elemento.

Métodos mágicos: Son métodos especiales que permiten que un objeto personalizado interactúe con operaciones estándar de Python, como la suma (__add__), la comparación (__eq__), la longitud de un objeto (__len__), entre otros. Se usan para redefinir el comportamiento de los operadores y las funciones que Python aplica automáticamente en ciertas circunstancias.
Ejemplo: Si tienes una clase que representa un número, puedes redefinir la suma usando el método mágico __add__ para que tu clase se comporte como un número cuando usas el operador +.

4. ¿Por qué usar los métodos mágicos si ya tenemos operadores predefinidos en Python?
Los métodos mágicos no reemplazan los métodos normales; más bien, permiten que los operadores estándar de Python 

trabajen con clases personalizadas.

Un ejemplo práctico es cuando quieres que tus objetos personalizados se puedan sumar, restar o comparar como si fueran tipos de datos predefinidos. Sin métodos mágicos, necesitarías métodos normales específicos para cada caso, pero con los mágicos, puedes usar operadores de forma directa.

5. ¿Para qué sirven los métodos mágicos en OOP?
En programación orientada a objetos (OOP), los métodos mágicos son muy útiles porque permiten que tus clases personalizadas se comporten de una forma más intuitiva al interactuar con objetos de otros tipos.

Por ejemplo, si estás creando una clase que maneja una lista de elementos y quieres que esa clase sea iterable, puedes implementar el método mágico __iter__, lo que permite que tu clase sea utilizada directamente en un bucle for, sin tener que llamar a un método como next() o iter() explícitamente.

6. ¿Cuáles son ejemplos de métodos mágicos comunes?

Algunos de los métodos mágicos más comunes son: 
__init__: Inicializa un objeto cuando se crea (similar a un constructor en otros lenguajes).
__str__: Devuelve una cadena legible del objeto para impresión.
__add__: Permite usar el operador + entre objetos de una clase personalizada.
__len__: Permite que el objeto sea usado con la función len().
__eq__: Permite comparar si dos objetos son iguales (==).
__iter__: Permite que el objeto sea iterable (utilizable en un for).
__next__: Permite definir el siguiente valor en la iteración.

7. ¿Cómo se utilizan los métodos mágicos para personalizar el comportamiento de un objeto?
Los métodos mágicos permiten personalizar cómo un objeto responde a operaciones que Python considera estándar. Por ejemplo: 

Suma de objetos: Si tienes una clase Punto que representa un punto en el espacio, puedes usar __add__ para definir cómo se suman dos objetos Punto.

Iteración: Si quieres que una clase se pueda recorrer con un bucle for, debes implementar __iter__ y __next__.

8. ¿Qué pasa si quiero usar un for con una clase personalizada?
Si quieres que tu clase sea iterable (que pueda ser recorrida en un bucle for), necesitas implementar el método mágico __iter__ y __next__.

Sin estos métodos, no podrás usar la clase en un for porque Python no sabría cómo recorrerla.
Ejemplo: Si tienes una clase que representa una colección de datos y quieres recorrerla, debes definir esos métodos para permitir la iteración.

9. ¿Qué sucede si trato de iterar una clase sin definir estos métodos mágicos?
Si intentas iterar sobre una clase que no tiene los métodos __iter__ y __next__, Python lanzará un error porque no sabe cómo manejar la iteración.

10. ¿Dónde más se usan los métodos mágicos?
Módulos personalizados: Si estás escribiendo un módulo y quieres que ciertos objetos de ese módulo se comporten de forma personalizada con los operadores (por ejemplo, el operador + para fusionar objetos), puedes usar los métodos mágicos. Cuando no existen métodos estándar: Si quieres agregar comportamientos a tus clases que no están cubiertos por los métodos predefinidos de Python, los métodos mágicos te permiten hacerlo. Esto es útil, por ejemplo, cuando escribes tus propios objetos y necesitas que interactúen con operadores como si fueran objetos integrados de Python.
"""

