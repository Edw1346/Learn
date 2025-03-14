import itertools

"""itertools es un módulo de Python que proporciona funciones para trabajar con iteradores de manera eficiente. Sus 
funciones ayudan a generar combinaciones, permutaciones, secuencias infinitas y manipular iterables sin necesidad de 
listas grandes en memoria."""

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
accumulate(iterable, func): Acumula valores usando una función.

Ejemplo rápido:"""
import itertools # Genera combinaciones de 2 elementos 
print(list(itertools.combinations([1, 2, 3], 2))) # Salida: [(1, 2), (1, 3), (2, 3)] # Cuenta desde 5 en pasos de 2 
contador = itertools.count(5, 2)
print(next(contador)) # 5 
print(next(contador)) # 7 





"""Funciones del módulo itertools:"""

#itertools.count(start=0, step=1) Devuelve un iterador que genera números empezando desde start y avanzando por pasos de step. Ejemplo:
from itertools import count 
for i in count(10, 2): 
    if i > 20: 
        break 
print(i) 

#itertools.cycle(iterable) Devuelve un iterador que recorre los elementos de un iterable de forma infinita, repitiendo los elementos en bucle. Ejemplo:
from itertools import cycle 
counter = 0 
for item in cycle([1, 2, 3]): 
    if counter == 6: 
        break 
print(item) 
counter += 1 

#itertools.repeat(object, times=None) Devuelve un iterador que repite el objeto times veces. Si no se especifica times, se repite infinitamente. Ejemplo:
from itertools import repeat 
for i in repeat('hello', 3): 
    print(i) 

#itertools.chain(*iterables) Combina varios iterables en uno solo, iterando a través de todos los elementos de los iterables proporcionados. Ejemplo:
from itertools import chain 
for item in chain([1, 2], ['a', 'b']): 
    print(item) 

#itertools.combinations(iterable, r) Devuelve todas las combinaciones posibles de longitud r de los elementos del iterable. Ejemplo:
from itertools import combinations
for comb in combinations([1, 2, 3, 4], 2): 
    print(comb) 

#itertools.combinations_with_replacement(iterable, r) Devuelve todas las combinaciones posibles de longitud r, permitiendo que un mismo elemento se repita. Ejemplo:
from itertools import combinations_with_replacement 
for comb in combinations_with_replacement([1, 2, 3], 2): 
    print(comb) 

#itertools.permutations(iterable, r=None) Devuelve todas las permutaciones posibles de longitud r de los elementos del iterable. Ejemplo:
from itertools import permutations
for perm in permutations([1, 2, 3]): 
    print(perm) 

#itertools.product(*iterables, repeat=1) Devuelve el producto cartesiano de los iterables. Es equivalente a un bucle anidado. Ejemplo:
from itertools import product
for prod in product([1, 2], ['a', 'b']): 
    print(prod) 

#itertools.islice(iterable, start, stop, step) Devuelve una parte del iterable (similar a la técnica de "slice") especificando el inicio, el final y el paso. Ejemplo:
from itertools import islice 
print(list(islice([1, 2, 3, 4, 5], 1, 4, 2))) 

#itertools.starmap(function, iterable) Aplica una función a los elementos de un iterable, desempaquetándolos antes de pasarlos a la función. Ejemplo:
from itertools import starmap 
def multiply(x, y): 
    return x * y 
print(list(starmap(multiply, [(1, 2), (3, 4), (5, 6)]))) 

#itertools.tee(iterable, n=2) Crea n copias independientes de un iterable. Ejemplo:
from itertools import tee
it1, it2 = tee([1, 2, 3, 4], 2)
print(list(it1)) # [1, 2, 3, 4] 
print(list(it2)) # [1, 2, 3, 4] 

#itertools.zip_longest(*iterables, fillvalue=None) Devuelve un iterador que combina elementos de los iterables. Si los iterables tienen diferentes longitudes, rellena con fillvalue.Ejemplo:
from itertools import zip_longest 
for item in zip_longest([1, 2], ['a', 'b', 'c'], fillvalue='x'): 
    print(item) 


"""El módulo itertools no define clases propias como tal. En lugar de eso, proporciona varias funciones que operan sobre 
iteradores, pero no introduce clases como parte de su API. Las funciones devuelven iteradores o generadores, que son 
objetos iterables pero no son clases del módulo en sí."""


"""El módulo itertools no define variables específicas como parte de su API pública. Su propósito principal es proporcionar 
funciones que operan sobre iteradores, como combinaciones, permutaciones y otros tipos de operaciones de iteración."""


"""El módulo itertools no define constantes específicas como parte de su API. Su propósito es proporcionar funciones para 
trabajar con iteradores y colecciones de manera eficiente, pero no incluye constantes definidas explícitamente."""



"""El módulo itertools no define excepciones específicas. Sin embargo, algunas de las funciones pueden generar excepciones 
estándar de Python si se usan de manera incorrecta. Por ejemplo:"""

#StopIteration: Algunas funciones, como itertools.count, itertools.cycle o itertools.repeat, pueden generar esta excepción si se consumen completamente sin ningún control, pero generalmente este tipo de excepción es manejado de manera interna en los iteradores.

#ValueError: Puede ocurrir si se pasan parámetros no válidos a algunas funciones, como en el caso de itertools.combinations si se pide una combinación con un valor mayor que el número de elementos del iterable.



"""El módulo itertools en Python proporciona una serie de herramientas para la manipulación eficiente de iteradores. No 
tiene "submódulos" como tal, pero sí contiene diversas funciones especializadas."""
