
"""iteraciones """

"""1. Iteraciones con for
El bucle for es una de las herramientas más comunes para iterar sobre elementos de una secuencia (listas, cadenas, tuplas, conjuntos, diccionarios, etc.). Ejemplo básico:"""
numeros = [1, 2, 3, 4] 
for numero in numeros:
    print(numero) 
#Salida:1 2 3 4 

"""2. Iteraciones con índices (enumerate)
Puedes iterar sobre una secuencia y obtener tanto el índice como el valor."""
frutas = ["manzana", "naranja", "banana"] 
for indice, fruta in enumerate(frutas): 
    print(f"Índice: {indice}, Fruta: {fruta}") 

#Salida: Índice: 0, Fruta: manzana Índice: 1, Fruta: naranja Índice: 2, Fruta: banana 

"""3. Iteraciones con un rango (range)
El objeto range genera una secuencia de números enteros que puedes usar en iteraciones. Ejemplo básico:"""
for i in range(5): 
    print(i) # De 0 a 4 

#Ejemplo con límites:
for i in range(1, 10, 2):
# De 1 a 9, con un paso de 2
    print(i) 

"""4. Iteraciones con while
El bucle while repite un bloque de código mientras una condición sea verdadera. Ejemplo básico:"""
contador = 0 
while contador < 5: 
    print(contador) 
    contador += 1 

#Ejemplo infinito (con break para detenerlo):
while True: 
    print("Bucle infinito")
    break 
# Detenemos el bucle 

#5. Iteraciones con estructuras de datos
#Listas:
    numeros = [10, 20, 30] 
    for numero in numeros: 
        print(numero) 

#Cadenas:
texto = "Python" 
for letra in texto: 
    print(letra) 

#Diccionarios:
diccionario = {"a": 1, "b": 2, "c": 3} 
for clave, valor in diccionario.items(): 
    print(f"{clave}: {valor}") 

#Conjuntos:
conjunto = {1, 2, 3} 
for elemento in conjunto: 
    print(elemento) 

#Tuplas:
tupla = (1, 2, 3) 
for elemento in tupla: 
    print(elemento) 

"""6. Iteraciones anidadas
Puedes tener iteraciones dentro de iteraciones para recorrer estructuras más complejas."""
matriz = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
for fila in matriz:
    for columna in fila: 
        print(columna, end=" ") 
#Salida: 1 2 3 4 5 6 7 8 9 

"""7. Iteraciones con generadores
Los generadores son estructuras que producen elementos bajo demanda.

Usando yield:"""
def generador(): 
    for i in range(5): 
        yield i 
        for valor in generador():
            print(valor) 

#8. Iteraciones con itertools (módulo avanzado)
#Combinaciones:
from itertools import combinations
elementos = [1, 2, 3] 
for combinacion in combinations(elementos, 2):
    print(combinacion) 

#Producto cartesiano:
from itertools import product
for combinacion in product("AB", repeat=2): 
    print(combinacion) 

#Ciclos infinitos:
from itertools import cycle
ciclo = cycle("ABC")
for _ in range(6): print(next(ciclo)) 

#9. Control de flujo en iteraciones
#break: Detiene un bucle.
for i in range(10):
    if i == 5:
        break 
    
print(i) 

#continue: Salta a la siguiente iteración.
for i in range(5): 
    if i == 2: 
        continue
print(i) 

#else: Ejecuta un bloque si el bucle no se interrumpe.
for i in range(3): 
    print(i) 
else: 
    print("Bucle completado sin interrupciones") 

"""10. Iteradores personalizados
Puedes definir tus propios iteradores implementando los métodos __iter__ y __next__."""
class Contador: 
    def __init__(self, limite): 
        self.limite = limite 
        self.contador = 0 
        
    def __iter__(self):
        return self 
        
    def __next__(self):
        if self.contador < self.limite:
            valor = self.contador 
            self.contador += 1 
            return valor
        else: 
            raise StopIteration 
            mi_iterador = Contador(5) 
            for valor in mi_iterador:
                print(valor) 

#11. Iteraciones con comprensión de listas (List Comprehensions) Ejemplo básico:
cuadrados = [x**2 for x in range(5)] 
print(cuadrados) 

#Con condición:
pares = [x for x in range(10) if x % 2 == 0] 
print(pares) 

#12. Iteraciones sobre archivos
with open("archivo.txt", "r") as archivo: 
    for linea in archivo:
        print(linea.strip()) 