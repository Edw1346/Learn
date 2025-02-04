"""Funciones de orden superior 
Son aquellas que pueden tomar otras funciones como argumentos, devolver funciones como resultados o ambas cosas. """

"""Prácticas con Funciones de Orden Superior"""

"""1. Uso de funciones como argumentos
Una práctica común es pasar una función como argumento a otra. Esto permite aplicar una función a diferentes contextos sin modificar el código de la función original.

Práctica: Funciones como argumentos"""
def aplicar_operacion(a, b, operacion): 
    """Aplica una operación sobre dos números""" 
    return operacion(a, b) 
def sumar(x, y): 
    return x + y
def restar(x, y):
    return x - y 

# Usamos las funciones como argumentos
print(aplicar_operacion(5, 3, sumar)) # 8 
print(aplicar_operacion(5, 3, restar)) # 2 

#

"""2. Devolver funciones como resultados
Otra práctica importante es devolver funciones como resultados de otras funciones. Esto te permite crear funciones dinámicas o personalizadas en tiempo de ejecución.

Práctica: Devolver funciones"""
def multiplicador(factor): 
    """Devuelve una función que multiplica su argumento por un factor""" 

    def multiplicar(x):
        return x * factor
    return multiplicar
# Crear una función para multiplicar por 5 
multiplicar_por_5 = multiplicador(5)
print(multiplicar_por_5(10)) # 50 

#

"""3. Composición de funciones
Puedes combinar varias funciones de manera sencilla usando funciones de orden superior. Este patrón permite construir una nueva función a partir de otras funciones ya existentes.

Práctica: Composición de funciones"""
def sumar(x, y): 
    return x + y 

def multiplicar(x, y): 
    return x * y # Componer las funciones 

def sumar_y_multiplicar(x, y, z): 
        return multiplicar(sumar(x, y), z) 

print(sumar_y_multiplicar(1, 2, 3)) # 9 (primero suma, luego multiplica) 

#

"""4. Uso de map(), filter() y reduce()
Estas funciones son ejemplos clásicos de funciones de orden superior que aplican una operación sobre un iterable.

Práctica: Usar map(), filter() y reduce()"""
from functools import reduce 
# map: Aplica una función a cada elemento de un iterable 
numeros = [1, 2, 3, 4] 
doblar = map(lambda x: x * 2, numeros) 
print(list(doblar)) # [2, 4, 6, 8]
# filter: Filtra elementos de un iterable según una condición 
pares = filter(lambda x: x % 2 == 0, numeros) 
print(list(pares)) # [2, 4]
# reduce: Reduce un iterable a un solo valor aplicando una función acumuladora 
suma = reduce(lambda x, y: x + y, numeros) 
print(suma) # 10 

#

"""5. Evitar efectos secundarios en funciones de orden superior
Una buena práctica es asegurarse de que las funciones de orden superior no tengan efectos secundarios. Esto significa que las funciones deben ser puramente funcionales y no modificar el estado global o los argumentos pasados.

Práctica: Funciones puras"""
def sumar(a, b):
    """Función pura: no modifica el estado global ni tiene efectos secundarios""" 
    return a + b 
def restar(a, b): 
    """Función pura"""
    return a - b 

#

"""Técnicas con Funciones de Orden Superior"""

"""1. Funciones Anidadas
Las funciones de orden superior en Python pueden usar funciones anidadas para aplicar diferentes comportamientos a las funciones que devuelven.

Técnica: Uso de funciones anidadas"""
def operacion(a, b): 
    def suma(): 
        return a + b 
    def resta():
        return a - b 
    if a > b: 
        return suma() 
    else: 
        return resta() 

print(operacion(5, 3)) # 8 (suma) 
print(operacion(3, 5)) # -2 (resta) 

#

"""3. Funciones de Orden Superior con Decoradores
Los decoradores en Python son funciones que reciben otra función como argumento y la modifican de alguna manera. Es una forma común de usar funciones de orden superior para añadir comportamientos adicionales.

Técnica: Crear un decorador"""
def decorador(func): 
    def wrapper():
        print("Antes de ejecutar la función") 
    func()
    print("Después de ejecutar la función") 
    return wrapper 

@decorador 
def saludar():
    print("¡Hola Mundo!") # Ejecutar la función decorada saludar() 

#

"""4. Generadores de Funciones de Orden Superior
Puedes crear funciones de orden superior que devuelvan otras funciones generadoras. Este patrón es útil cuando necesitas una serie de funciones que generen resultados bajo demanda.

Técnica: Funciones generadoras como callbacks"""
def generador_funciones(): 
    def suma(x, y): 
        return x + y 
    def resta(x, y): 
        return x - y 
    return suma, resta 

suma, resta = generador_funciones() 
print(suma(3, 2)) # 5 
print(resta(3, 2)) # 1 
