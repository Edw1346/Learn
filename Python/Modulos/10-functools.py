import functools

"""functools es un módulo de Python que proporciona herramientas para trabajar con funciones de manera más eficiente, 
permitiendo optimizar, reutilizar y mejorar el rendimiento del código."""

#Ejemplo rápido:
# 1. Caché para mejorar rendimiento 
@functools.lru_cache(maxsize=3) 
def factorial(n): 
    return n * factorial(n - 1) 

if n > 1 
else 1 
print(factorial(5)) # 120, se guarda en caché 

# 2. Función parcial con argumentos predefinidos 
from functools import partial 
def potencia(base, exponente): 
    return base ** exponente 
    
elevar_al_cuadrado = partial(potencia, exponente=2)
print(elevar_al_cuadrado(5)) # 25 




"""Funciones del módulo functools:"""

#1. functools.cache: Guarda los resultados de llamadas previas a una función para evitar cálculos repetidos.import functools
@functools.cache 
def fibonacci(n): 
    if n < 2: 
        return n 
    return fibonacci(n - 1) + fibonacci(n - 2) 
print(fibonacci(10)) # 55 

#2. functools.lru_cache: Similar a cache, pero permite limitar el tamaño del caché
@functools.lru_cache(maxsize=3) 
def factorial(n):
    return n * factorial(n - 1)
if n > 1 
else 1 
    print(factorial(5)) # 120 

#3. functools.cmp_to_key: Convierte una función de comparación en una clave para sorted().
from functools import cmp_to_key 
def comparar(x, y): 
    return x - y # Ordena de menor a mayor 
lista = [5, 3, 8, 1] 
lista.sort(key=cmp_to_key(comparar)) 
print(lista) # [1, 3, 5, 8] 

#4. functools.partial: Crea una nueva función con algunos argumentos ya definidos.
from functools import partial 
def potencia(base, exponente): 
    return base ** exponente 
cuadrado = partial(potencia, exponente=2) 
print(cuadrado(4)) # 16 

#5. functools.partialmethod: Similar a partial, pero para métodos de clases."""
class Calculadora: 
    def operar(self, a, b): 
        return a + b 

suma = functools.partialmethod(operar, b=10) 
calc = Calculadora() 
print(calc.suma(5)) # 15 (5 + 10) 

#6. functools.reduce: Aplica una función acumulativa sobre un iterable."""
from functools import reduce 
numeros = [1, 2, 3, 4] 
resultado = reduce(lambda x, y: x * y, numeros) 
print(resultado) # 24 (1 * 2 * 3 * 4) 

#7. functools.singledispatch: Permite definir funciones genéricas según el tipo del argumento.
from functools import singledispatch 
@singledispatch
def procesar(valor): 
    print(f"Tipo no soportado:{type(valor)}") 

@procesar.register(int) 
def _(valor): 
    print(f"Procesando un entero: {valor}") 
@procesar.register(str) 
def _(valor): 
    print(f"Procesando un string: {valor}") 

procesar(10) # Procesando un entero: 10 
procesar("Hola") # Procesando un string: Hola 
procesar(3.14) # Tipo no soportado: <class 'float'> 

#8. functools.singledispatchmethod: Lo mismo que singledispatch, pero para métodos de clases."""
class Procesador: 
    @functools.singledispatchmethod 
    def procesar(self, valor):
        print(f"Tipo desconocido: {type(valor)}")
    
    @procesar.register(int) 
        def _(self, valor): 
            print(f"Entero recibido: {valor}") 

    @procesar.register(str) 
    def _(self, valor): 
        print(f"String recibido: {valor}")

p = Procesador()
p.procesar(42) # Entero recibido: 42 
p.procesar("Python") # String recibido: Python 

#9. functools.total_ordering: Facilita la implementación de operadores de comparación en clases."""
from functools import total_ordering 
@total_ordering 
class Persona: 
    def __init__(self, edad): 
        self.edad = edad 

    def __eq__(self, otro): 
        return self.edad == otro.edad 

    def __lt__(self, otro): 
        return self.edad < otro.edad

p1 = Persona(25) 
p2 = Persona(30) 
print(p1 < p2) # True 
print(p1 > p2) # False (se genera automáticamente) 

#10. functools.wraps: Preserva metadatos de una función cuando se usa un decorador."""
from functools import wraps 
def decorador(func): 
@wraps(func) 
def envoltura(*args, **kwargs): 
    """Esta es una función decorada.""" 
        return func(*args, **kwargs) 
    return envoltura 

@decorador 
def mi_funcion(): 
    """Esta es la docstring original.""" 
    return "Hola" 

print(mi_funcion.__doc__)  # "Esta es la docstring original." 




"""El módulo functools no tiene clases, solo contiene funciones para optimizar el uso de funciones en Python.
Sin embargo, algunas de sus funciones, como partial y partialmethod, devuelven objetos de clase interna (functools.partial y functools.partialmethod), pero estas no son clases que puedas instanciar directamente.
Si necesitas trabajar con clases en functools, las funciones más útiles son: 
total_ordering: Para definir operadores de comparación en clases.
singledispatchmethod: Para hacer métodos polimórficos.
partialmethod: Para definir métodos preconfigurados."""



"""El módulo functools no tiene variables globales definidas explícitamente. Todo lo que ofrece functools son 
funciones y clases internas, pero no hay constantes ni variables predefinidas."""


"""El módulo functools no tiene variables globales definidas explícitamente.
Todo lo que ofrece functools son funciones y clases internas, pero no hay constantes ni variables predefinidas."""




"""El módulo functools no define excepciones propias.
Sin embargo, algunas de sus funciones pueden generar excepciones estándar de Python si se usan incorrectamente.

TypeError
Si partial recibe argumentos incorrectos.
Si reduce recibe un iterable vacío sin valor inicial.
Si singledispatch se usa con un tipo de argumento no registrado.

RecursionError
Si una función decorada con cache o lru_cache entra en recursión infinita."""



"""El módulo functools no tiene submódulos. Es un módulo estándar de Python que solo contiene funciones y decoradores 
para mejorar la manipulación de funciones y métodos."""