
"""Conjuntos en Python (Sets)"""

"""1. Características principales de los conjuntos

Elementos únicos: No puede haber duplicados en un conjunto.
Sin orden: Los conjuntos no garantizan un orden específico de los elementos.
Mutables: Los conjuntos pueden modificarse (agregar o eliminar elementos), aunque también existen conjuntos inmutables (frozenset).
Eficiencia: Las operaciones de búsqueda (in) y eliminación son rápidas porque los conjuntos están implementados usando tablas hash.

2. Crear conjuntos
Conjunto vacío:"""
conjunto_vacio = set()
# Usa 'set()', no '{}', ya que '{}' crea un diccionario. 

#Conjunto con elementos:
conjunto = {1, 2, 3, 4} 

#A partir de un iterable (lista, cadena, etc.):
conjunto_desde_lista = set([1, 2, 3, 1, 2])
# Elimina duplicados
print(conjunto_desde_lista) # Output: {1, 2, 3} 
conjunto_desde_cadena = set("hola") 
print(conjunto_desde_cadena) # Output: {'h', 'o', 'l', 'a'} 

#3. Operaciones básicas con conjuntos
#Agregar elementos:
conjunto = {1, 2} 
conjunto.add(3)
print(conjunto) # Output: {1, 2, 3} 

#Eliminar elementos:
conjunto = {1, 2, 3}
conjunto.remove(2) 
# Lanza un error si el elemento no existe 
print(conjunto) # Output: {1, 3}
conjunto.discard(4) 
# No lanza error si el elemento no existe 

#Eliminar y devolver un elemento aleatorio:
conjunto = {1, 2, 3}
elemento = conjunto.pop() 
# Devuelve y elimina un elemento aleatorio 
print(elemento, conjunto) 

#Limpiar un conjunto:
conjunto.clear() 
print(conjunto) # Output: set() 

#4. Operaciones de conjunto (Matemáticas)
#Unión (| o union()):
#Une los elementos de dos conjuntos (sin duplicados).
A = {1, 2, 3} 
B = {3, 4, 5}
print(A | B) # Output: {1, 2, 3, 4, 5} 

print(A.union(B)) # Output: {1, 2, 3, 4, 5} 

#Intersección (& o intersection()):
#Obtiene los elementos comunes.
print(A & B)
# Output: {3} 
print(A.intersection(B)) # Output: {3} 

#Diferencia (- o difference()):
#Obtiene los elementos en el primer conjunto que no están en el segundo.
print(A - B) # Output: {1, 2} 
print(A.difference(B)) # Output: {1, 2} 

#Diferencia simétrica (^ o symmetric_difference()):
#Obtiene los elementos que están en uno u otro conjunto, pero no en ambos.
print(A ^ B) # Output: {1, 2, 4, 5} 
print(A.symmetric_difference(B)) # Output: {1, 2, 4, 5} 

#5. Comparación de conjuntos
#Subconjunto (issubset() o <=):
#Verifica si un conjunto está completamente contenido en otro.
C = {1, 2}
print(C <= A) # Output: True
print(C.issubset(A)) # Output: True 

#Superconjunto (issuperset() o >=):
#Verifica si un conjunto contiene completamente a otro.
print(A >= C) # Output: True 
print(A.issuperset(C)) # Output: True 

#Conjuntos disjuntos (isdisjoint()):
#Verifica si dos conjuntos no tienen elementos comunes.
D = {4, 5}
print(A.isdisjoint(D)) # Output: True 

#6. Iterar sobre un conjunto
#Puedes recorrer un conjunto con un bucle for.
conjunto = {1, 2, 3}
for elemento in conjunto:
    print(elemento) 

#7. Métodos avanzados de conjuntos
#Copiar un conjunto:
conjunto = {1, 2, 3} 
copia = conjunto.copy() 

#Actualizar un conjunto con otro (update()):
#Agrega elementos de otro conjunto o iterable.
A.update(B) 
print(A) # Output: {1, 2, 3, 4, 5} 

#Actualizar la intersección (intersection_update()):
#Deja solo los elementos comunes entre dos conjuntos.
A.intersection_update(B) 
print(A) # Output: {3} 

#Actualizar la diferencia (difference_update()):

#Elimina del conjunto actual los elementos presentes en otro conjunto.
A.difference_update(B)
print(A) # Output: {1, 2} 

#Actualizar la diferencia simétrica (symmetric_difference_update()):
#Actualiza el conjunto actual con la diferencia simétrica.
A.symmetric_difference_update(B) 
print(A) # Output: {1, 2, 4, 5} 

#8. Conjuntos inmutables (frozenset)
#El tipo frozenset es una variante inmutable de los conjuntos. No se pueden modificar después de su creación.
fs = frozenset([1, 2, 3]) 
print(fs) # Output: frozenset({1, 2, 3}) 
#Aunque no puedes agregar ni eliminar elementos, puedes realizar operaciones como unión, intersección, etc.

#9. Usos comunes de conjuntos
#Eliminar duplicados de una lista:
lista = [1, 2, 2, 3, 3, 3] 
sin_duplicados = list(set(lista))
print(sin_duplicados) # Output: [1, 2, 3] 

#Comprobar pertenencia:
vocales = {"a", "e", "i", "o", "u"} 
print("a" in vocales) # Output: True 
print("z" in vocales) # Output: False 

"""Operaciones matemáticas:
Calcular intersección, unión o diferencias entre conjuntos de datos.

Optimización de búsquedas:
Los conjuntos son mucho más rápidos que listas para comprobar si un elemento existe."""
