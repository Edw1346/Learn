#itertools es un módulo que proporciona funciones para trabajar con iteradores eficientemente. 
# Ayudan a generar combinaciones, permutaciones, secuencias infinitas y manipular iterables sin necesidad de listas grandes en memoria.

"""Funciones principales:

Iteradores infinitos
count(start, step): Genera números secuenciales.
cycle(iterable): Repite indefinidamente un iterable.
repeat(item, times): Repite un valor times veces.

Combinaciones y permutaciones
permutations(iterable, r): Todas las formas posibles de r elementos.
combinations(iterable, r): Combinaciones únicas de r elementos.
product(*iterables, repeat=n): Producto cartesiano.

Manipulación de iterables
chain(*iterables): Une varios iterables en uno.
groupby(iterable, key): Agrupa elementos consecutivos con la misma clave.
accumulate(iterable, func): Acumula valores usando una función."""

import itertools

#Funciones del módulo itertools:

#itertools.count(start=0, step=1). Devuelve un iterador que genera números empezando desde start y avanzando por pasos de step:
for i in itertools.count(0,2): 
    if i > 20: 
        break 
print(i) 

##itertools.cycle(iterable). Devuelve un iterador que recorre los elementos de un iterable de forma infinita, repitiendo los elementos en bucle:
counter = 0 
for item in itertools.cycle([1,2,3]):
    if counter == 6: 
        break 
    print(item) 
    counter += 1 

#itertools.repeat(object, times=None). Devuelve un iterador que repite el objeto times veces. Si no se especifica times, se repite infinitamente: 
for i in itertools.repeat("Hello",3):
    print(i) 

#itertools.chain(*iterables). Combina varios iterables en uno solo, iterando a través de todos los elementos de los iterables proporcionados:
for item in itertools.chain([1, 2], ['a', 'b']): 
    print(item) #Une todos datos en una sola lista : ([1,2],[3,4]) a [1,2,3,4]
print("\n")

#itertools.combinations(iterable, r). Devuelve todas las combinaciones posibles de longitud r de los elementos del iterable:
for comb in itertools.combinations([1, 2, 3, 4], 3): 
    print(comb) #Combinacion de un r de tamaño, sin repetir elementos
print("\n")

#itertools.combinations_with_replacement(iterable, r). Devuelve todas las combinaciones posibles de longitud r, permitiendo que un mismo elemento se repita:
for comb in itertools.combinations_with_replacement([1, 2, 3], 3): 
    print(comb) #Combinacion de un r de tamaño, pero puede repetir elementos
print("\n")

#itertools.permutations(iterable, r=None). Devuelve todas permutaciones posibles de longitud r de elementos del iterable:
for perm in itertools.permutations([1, 2, 3]): 
    print(perm) #Combinacion de un r de tamaño, pero pueden cambiar el orden
print("\n")

#itertools.product(*iterables, repeat=1). Devuelve el producto cartesiano de los iterables. Es equivalente a un bucle anidado:
for prod in itertools.product([1, 2], ['a', 'b']): #Combina cada elemento, tomando un elemento en cada iteracion
    print(prod) #(1,'a'), (1,'b') en la primera iteracion. (2,'a'), (2,'b') en la segunda iteracion
print("\n")

#itertools.islice(iterable, start, stop, step). Devuelve una parte del iterable (similar a la técnica de "slice") especificando el inicio, el final y el paso:
print(list(itertools.islice([1, 2, 3, 4, 5], 1, 4, 2))) #Corta una lista hasta un longitud concreta
print("\n") #Agarra [1,2,3,4,5], inicia por 1, para en 4 y va de 2 en 2 [2,3] 

#itertools.starmap(function, iterable). Aplica una función a los elementos de un iterable, desempaquetándolos antes de pasarlos a la función:
def multiply(x, y):  return x * y #La funcion nmecesita n numeros de parametro, no mas ni menos
print(list(itertools.starmap(multiply, [(1, 2), (3, 4), (5, 6)]))) #Agarra cada lista y las envia a la funcion por separado
print("\n") #Envia los datos y los resultados los devuelve en la misma lista

#itertools.tee(iterable, n=2). Crea n copias independientes de un iterable:
it1, it2 = itertools.tee([1, 2, 3, 4], 2) #Indique cuantos variable se va a realizar las copias
print(list(it1)) # [1, 2, 3, 4] 
print(list(it2)) # [1, 2, 3, 4] 
print("\n")

#itertools.zip_longest(*iterables, fillvalue=None). Devuelve un iterador que combina elementos de los iterables. Si los iterables tienen diferentes longitudes, rellena con fillvalue:
for item in itertools.zip_longest([1, 2], ['a', 'b', 'c'], fillvalue='x'): 
    print(item) #Itera en el mismo indice segun avanza en la iteracion
#Pero rellena con none o se segun se coloque en fillvalue para cuando las lista estan impares en datos


#El módulo itertools  proporciona una serie de herramientas para la manipulación eficiente de iteradores. No tiene "submódulos" como tal, pero sí contiene diversas funciones especializadas.