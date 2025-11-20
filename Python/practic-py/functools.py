import functools
#functools módulo para trabajar con funciones eficiente, permitiendo optimizar, reutilizar y mejorar rendimiento del código

"""Funciones del módulo functools:"""

##functools.cache. Guarda los resultados de llamadas previas a una función para evitar cálculos repetidos.import functool
@functools.cache
def fibonacci(n): 
    if n < 2:  return n 
    return fibonacci(n - 1) + fibonacci(n - 2) 

print(fibonacci(10)) # 55 

##functools.lru_cache. Similar a cache, pero permite limitar el tamaño del caché."""
@functools.lru_cache(maxsize=50)
def factorial(n): 
    if n > 1: return n * factorial(n - 1)
    else: return 1

print(factorial(5)) # 120 

##Functools.cmp_to_key. Convierte una función de comparación en una clave para sorted()
def comparar(x, y): return x - y # Ordena de menor a mayor 
lista = [5, 3, 8, 1] 

lista.sort(key=functools.cmp_to_key(comparar)) 
print(lista) # [1, 3, 5, 8] 

##functools.partial. Crea una nueva función con algunos argumentos ya definidos."""
def potencia(base, exponente): return base ** exponente 
cuadrado = functools.partial(potencia, exponente=2) #Predefine ese parametro
print(cuadrado(4)) # 16 

##5. functools.partialmethod. Similar a partial, pero para métodos de clases."""
class Calculadora: 
    def operar(self, a, b): return a + b 

calc = Calculadora() 
suma = functools.partialmethod(calc.operar, b=10) 
print(calc.suma(5)) # 15 (5 + 10) 

##6. functools.reduce. Aplica una función acumulativa sobre un iterable.
numeros = [1, 2, 3, 4] 
resultado = functools.reduce(lambda x, y: x * y, numeros) 
print(resultado) # 24 (1 * 2 * 3 * 4) 

##7. functools.singledispatch. permite definir funciones genéricas según el tipo del argumento.
@functools.singledispatch
def procesar(valor):  print(f"Tipo no soportado:{type(valor)}") 

@procesar.register(int) 
def _(valor):  print(f"Procesando un entero: {valor}") 

@procesar.register(str) 
def _(valor):  print(f"Procesando un string: {valor}") 

procesar(10) # Procesando un entero: 10 
procesar("Hola") # Procesando un string: Hola 
procesar(3.14) # Tipo no soportado: <class 'float'> 

@functools.singledispatch
def s(val): return "No lo soporta"

@s.register(int)
def e(val): return "Valido"

@s.register(str)
def r(val): return "Valido"
print(s("Hola"))
print(s(10))
print(s(1.2))

##8. functools.singledispatchmethod. Lo mismo que singledispatch, pero para métodos de clases."""
class Procesador: 
    @functools.singledispatchmethod 
    def procesar(self, valor): print(f"Tipo desconocido: {type(valor)}")

    @procesar.register(int) 
    def _(self, valor): print(f"Entero recibido: {valor}") 

    @procesar.register(str) 
    def _(self, valor):  print(f"String recibido: {valor}")

p = Procesador()
p.procesar(42) # Entero recibido: 42 
p.procesar("Python") # String recibido: Python 

##9. functools.total_ordering. Facilita la implementación de operadores de comparación en clases."""
from functools import total_ordering 
@functools.total_ordering 
class Persona: 
    def __init__(self, edad):  self.edad = edad 
    def __eq__(self, otro):  return self.edad == otro.edad 
    def __lt__(self, otro):  return self.edad < otro.edad

p1 = Persona(25) 
p2 = Persona(30) 
print(p1 < p2) # True 
print(p1 > p2) # False (se genera automáticamente) 

##10. functools.wraps. Preserva metadatos de una función cuando se usa un decorador.
from functools import wraps 
def decorador(func): 
    @functools.wraps(func) 
    def envoltura(*args, **kwargs): return func(*args, **kwargs)  #Esta es una función decorada.
    return envoltura 

    @decorador 
    def mi_funcion():  return "Hola" # Esta es la docstring original.

print(mi_funcion.__doc__)  # "Esta es la docstring original." 




#El módulo functools no tiene submódulos, clases, variables y constantes. Solo contiene funciones y decoradores para mejorar la manipulación de funciones y métodos


