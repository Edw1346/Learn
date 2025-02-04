from functools import lru_cache @lru_cache(maxsize=None) 

"""La recursividad. Una función es recursiva si se llama a sí misma directa o indirectamente. Se usa para resolver problemas dividiendo una tarea grande en subproblemas más pequeños y similares. Ejemplo básico:"""
def factorial(n): 
    if n == 1: # Caso base 
        return 1 
    return n * factorial(n - 1) # Llamada recursiva 

"""Componentes clave de una función recursiva
Caso base. La condición que detiene la recursión. Sin él, la función llamaría a sí misma indefinidamente, causando error.
    if n == 1: # Caso base return 1 
Llamada recursiva. La función se llama a sí misma con un subconjunto más pequeño del problema original.
        return n * factorial(n - 1) # Llamada recursiva """

"""Tipos de recursividad"""
#Recursividad directa: Una función se llama a sí misma directamente.
def cuenta_regresiva(n): 
    if n == 0: 
        return print(n) 
    
cuenta_regresiva(n - 1) 

#Recursividad indirecta. Una función llama a otra, que a su vez llama a la primera.
def funcion_a(n): 
    if n > 0: 
        print(n) 

funcion_b(n - 1) 

def funcion_b(n): 
    if n > 0: 
        print(n) 

funcion_a(n - 2) 

#Recursividad de cola (Tail Recursion). La llamada recursiva es la última operación que realiza la función. Algunos lenguajes optimizan este tipo de recursión, pero Python no lo hace.
def suma_acumulada(n, acumulado=0): 
    if n == 0: 
        return acumulado 
"""Rescribir funciones para que la llamada recursiva sea la última operación.
Límite de recursión en Python: Modificar el límite de recursión si es necesario usando sys.setrecursionlimit()."""
    import sys sys.setrecursionlimit(2000) 
    return suma_acumulada(n - 1, acumulado + n) 

#Recursividad mutua: Variación de la recursividad indirecta donde varias funciones se llaman entre sí en un ciclo.
#4. Ejemplos clásicos de recursividad Factorial
def factorial(n): 
    if n == 1: # Caso base return 1 
        return n * factorial(n - 1) # Llamada recursiva 

#4.2. Serie de Fibonacci
def fibonacci(n): 
    if n <= 1: # Casos base 
        return n 
    return fibonacci(n - 1) + fibonacci(n - 2) # Llamadas recursivas 

#4.3. Potencia
def potencia(base, exponente): 
    if exponente == 0: # Caso base 
        return 1 
    return base * potencia(base, exponente - 1) # Llamada recursiva 

#4.4. Búsqueda binaria
def busqueda_binaria(arr, objetivo, inicio, fin): 
    if inicio > fin: # Caso base 
        return -1 
    medio = (inicio + fin) // 2 

    if arr[medio] == objetivo: 
        return medio 
    elif arr[medio] < objetivo: 
        return busqueda_binaria(arr, objetivo, medio + 1, fin) 
    else: return busqueda_binaria(arr, objetivo, inicio, medio - 1) 

#4.5 Problemas basados en árboles: Recorridos preorden, inorden y postorden.
def preorden(nodo): 
    if nodo: 
        print(nodo.valor) 

preorden(nodo.izquierda) 
preorden(nodo.derecha) 

"""6. Optimización de recursividad
Memoización. Técnica que almacena los resultados de las llamadas recursivas para evitar cálculos repetidos."""
def fibonacci(n): 
    if n <= 1: 
        return n 
    return fibonacci(n - 1) + fibonacci(n - 2) 

#6.2. Recursividad de cola. Reescribir funciones para hacer la llamada recursiva como la última operación, aunque Python no optimiza este caso.

#6.3. Alternativa iterativa. Usar bucles en lugar de recursividad para problemas que pueden causar desbordamiento de pila.
def factorial_iterativo(n): 
    resultado = 1 
    for i in range(1, n + 1): 
        resultado *= i 
    return resultado 







"""Buenas prácticas"""

"""1. Define siempre un caso base claro. El caso base es crucial para detener la recursión. Sin él, tu programa puede entrar en un bucle infinito y causar un desbordamiento de pila. Asegúrate de que el caso base sea alcanzable para todos los posibles caminos en tu función. Ejemplo: Factorial con caso base correcto"""
def factorial(n): 
    if n == 0: # Caso base 
        return 1 
    return n * factorial(n - 1) 

"""2. Divide el problema en subproblemas más simples. Una buena función recursiva divide el problema en partes más pequeñas, asegurando que cada paso sea más fácil de resolver que el anterior. Ejemplo: Suma de una lista"""
def suma(lista): 
    if len(lista) == 0: # Caso base 
        return 0 
    return lista[0] + suma(lista[1:]) # Dividir el problema 

"""3. Evita redundancia con memoización. Usa técnicas como memoización o decoradores como functools.lru_cache para evitar llamadas repetidas que recalculen los mismos valores, especialmente en problemas como la serie de Fibonacci.
Ejemplo: Fibonacci optimizado con memoización"""
#from functools import lru_cache @lru_cache(maxsize=None) 
def fibonacci(n): 
    if n <= 1: # Casos base 
        return n 
    return fibonacci(n - 1) + fibonacci(n - 2) 

"""4. Considera los límites de recursión. En Python, el límite de recursión predeterminado es de 1000. Si tu problema necesita más llamadas recursivas, puedes ajustar el límite con sys.setrecursionlimit, pero no abuses de esto.
En su lugar, considera usar una solución iterativa y evitar problemas de memoria. Ejemplo: Ajustar el límite de recursión"""
#import sys sys.setrecursionlimit(2000) 

"""5. Usa recursividad de cola (Tail Recursion) si es posible. Aunque Python no optimiza la recursividad de cola, escribir funciones recursivas en este estilo puede facilitar la conversión a soluciones iterativas y mejorar la claridad.
Ejemplo: Suma acumulativa con recursión de cola"""
def suma_acumulada(n, acumulado=0): 
    if n == 0: # Caso base 
        return acumulado 
    return suma_acumulada(n - 1, acumulado + n) # Recursión de cola 

"""6. Evita usar recursión innecesariamente. No uses recursión para problemas que pueden resolverse fácilmente con un bucle, como calcular la suma de números de 1 a n. La recursión consume más memoria porque cada llamada se guarda en la pila de ejecución. Ejemplo innecesario (recursión en lugar de bucle):"""
def suma(n): 
    if n == 0: 
        return 0 
    return n + suma(n - 1) # Ineficiente 

#Alternativa iterativa eficiente:
def suma_iterativa(n): 
    total = 0 
    for i in range(1, n + 1): 
        total += i 
    return total 

"""7. Usa nombres de funciones y variables descriptivos. Elige nombres que indiquen claramente qué hace la función y el propósito de las variables. Esto facilita la comprensión del flujo recursivo. Ejemplo descriptivo:"""
def buscar_valor_en_arbol(nodo, valor): 
    if not nodo: # Caso base: nodo vacío 
        return False 

    if nodo.valor == valor: 
        return True 
    return buscar_valor_en_arbol(nodo.izquierda, valor) or buscar_valor_en_arbol(nodo.derecha, valor) 

"""8. Analiza la complejidad de tu función recursiva. Calcula tanto la complejidad temporal como la complejidad espacial.
Ten cuidado con funciones recursivas que generan muchas llamadas redundantes. Ejemplo:
Complejidad de Fibonacci sin memoización: .
Complejidad con memoización: ."""

"""9. Visualiza el flujo recursivo. Dibujar diagramas de las llamadas recursivas puede ayudarte a entender mejor cómo fluye la ejecución de la función. También puedes usar herramientas como print() para depurar y ver cómo cambian las variables en cada llamada. Ejemplo:"""
def cuenta_regresiva(n): 
    print(f"Llamada recursiva con n={n}") 
    if n == 0: 
        return cuenta_regresiva(n - 1) 

"""10. Considera alternativas iterativas. Antes de optar por recursión, analiza si un bucle puede resolver el problema de manera más eficiente y sin riesgos de desbordamiento de pila.

11. Mantén la función recursiva simple. Evita añadir lógica compleja o dependencias externas en la función recursiva.
Mantén cada llamada lo más limpia posible y delega cálculos complejos a funciones externas si es necesario.

12. Prueba tu función con diferentes casos
Valida la función con: 
Casos base.
Casos límites (valores pequeños o grandes).
Casos inesperados o incorrectos (como valores negativos o entradas vacías)."""




"""Técnicas avanzadas y eficaces"""

"""1. Recursión de cola (Tail Recursion). La recursión de cola es una técnica en la que la llamada recursiva es la última operación ejecutada en la función, lo que permite que el compilador o intérprete optimice la recursión para evitar el uso adicional de memoria en la pila. Aunque Python no soporta la optimización de recursión de cola (no elimina el uso de la pila), es una técnica importante en lenguajes como Scheme o JavaScript.
Ejemplo: Recursión de cola para sumar números"""
def suma_acumulada(n, acumulado=0): 
    if n == 0: 
        return acumulado 
    return suma_acumulada(n - 1, acumulado + n) 

"""2. Memoización. Memoización es una técnica de optimización que almacena los resultados de funciones recursivas para evitar cálculos repetidos, mejorando significativamente el rendimiento, especialmente en funciones como Fibonacci. En Python, se puede usar el decorador functools.lru_cache para aplicar memoización de forma sencilla.
Ejemplo: Fibonacci con memoización"""
#from functools import lru_cache @lru_cache(maxsize=None) 
def fibonacci(n): 
    if n <= 1: 
        return n 
    return fibonacci(n - 1) + fibonacci(n - 2) 

"""3. Transformación a iteración. En algunos casos, un algoritmo recursivo puede ser reescrito de manera iterativa, eliminando el riesgo de desbordamiento de pila y mejorando la eficiencia. La transformación iterativa también puede facilitar el uso de memoria constante si es necesario.
Ejemplo: Transformar recursión de Fibonacci a iteración"""
def fibonacci_iterativo(n): 
    a, b = 0, 1 
    for _ in range(n): 
        a, b = b, a + b 
        return a 

"""4. Uso de pilas explícitas (Stacks). Una técnica para evitar el desbordamiento de pila de recursión es simular la recursión usando una pila explícita. En lugar de confiar en la pila de llamadas del sistema, se gestionan las llamadas recursivas manualmente con una estructura de datos como una pila. Ejemplo: Simulación de recursión de búsqueda en profundidad (DFS) con pilas"""
def dfs_iterativo(grafo, inicio): 
    pila = [inicio] 
    visitados = set() 
    while pila: 
        nodo = pila.pop() 
        if nodo not in visitados: 
            visitados.add(nodo) 
        pila.extend(grafo[nodo] - visitados) 
    return visitados 

"""5. Reducción del tamaño del problema. En cada llamada recursiva, asegúrate de que el tamaño del problema se reduzca de manera efectiva. La reducción del problema es clave para que la recursividad se resuelva en un número finito de pasos.
Siempre que sea posible, divida el problema en subproblemas disjuntos que pueden ser resueltos de manera independiente. Ejemplo: Ordenamiento rápido (Quicksort)"""
def quicksort(arr): 
    if len(arr) <= 1: 
        return arr 
    pivot = arr[len(arr) // 2] 
    left = [x for x in arr if x < pivot] 
    middle = [x for x in arr if x == pivot] 
    right = [x for x in arr if x > pivot] 
    return quicksort(left) + middle + quicksort(right) 

"""6. Recursión híbrida (recursión con optimización iterativa). En algunos casos, se puede combinar recursión con iteración para obtener lo mejor de ambos mundos, especialmente si se enfrenta a problemas complejos como recorridos por árboles o grafos. Se puede usar una recursión profunda inicialmente y luego cambiar a una iteración para manejar grandes volúmenes de datos sin caer en un desbordamiento de pila. Ejemplo: Recorrido en un árbol con recursión e iteración"""
def recorrido_arbol_iterativo(arbol): 
    pila = [arbol] 
    while pila: 
        nodo = pila.pop() 
        procesar(nodo) 

    if nodo.derecha: 
        pila.append(nodo.derecha) 

    if nodo.izquierda: 
        pila.append(nodo.izquierda) 

"""7. Poda de recursión (Pruning). Poda de recursión significa detener ciertas ramas de la recursión si sabes que no se necesitan (o son redundantes). Es una técnica útil en problemas de búsqueda, como el backtracking, donde se exploran soluciones, pero se descartan aquellas que no son viables. Ejemplo: Poda en problemas de backtracking"""
def resolver_problema(estado): 
    if no_es_viable(estado): # Poda 
        return None 
    if es_solucion(estado): 
        return estado 
    for vecino in obtener_vecinos(estado): 
        solucion = resolver_problema(vecino) 
        if solucion: 
            return solucion 
    return None 

"""8. Funciones de ayuda auxiliares. Al trabajar con recursividad, a veces es útil crear funciones auxiliares dentro de la función recursiva principal para ayudar a reducir la complejidad y mejorar la legibilidad.
Las funciones de ayuda también pueden proporcionar un caso base más específico o manejar un estado adicional.
Ejemplo: Función recursiva de ordenación con función auxiliar"""
def ordenacion(arr): 
    def ordenar_recursivo(subarr): 
        if len(subarr) <= 1:   
            return subarr 
        pivot = subarr[0] 
        menores = [x for x in subarr[1:] if x < pivot] 
        mayores = [x for x in subarr[1:] if x >= pivot] 
        return ordenar_recursivo(menores) + [pivot] + ordenar_recursivo(mayores) 
    return ordenar_recursivo(arr) 

"""9. El uso de listas y tuplas para evitar la recomposición de estructuras. A veces, en lugar de modificar el estado de los datos de manera costosa, es mejor devolver nuevos objetos (como listas o tuplas) en cada llamada recursiva. Esto hace que el código sea más predecible y evita modificar el estado de los objetos pasados. 
Ejemplo: Usando tuplas para evitar la modificación de datos"""
def permutaciones(lista): 
    if len(lista) == 0: 
        return [[]] 
        resultado = [] 
        for i in range(len(lista)): 
            elemento = lista[i] 
            sublista = lista[:i] + lista[i+1:] 
        for perm in permutaciones(sublista): 
            resultado.append([elemento] + perm) 
            return resultado 

"""10. Profundización en las llamadas recursivas. A veces es necesario explorar profundamente un subproblema en lugar de hacer una simple llamada recursiva. En tales casos, asegúrate de comprender y gestionar bien la pila de llamadas recursivas. Ejemplo: Búsqueda DFS con profundización explícita"""
def dfs_profundidad(graph, node, visitados=None): 
    if visitados is None: 
        visitados = set() 
        visitados.add(node) 
        for vecino in graph[node]: 
            if vecino not in visitados: 
                dfs_profundidad(graph, vecino, visitados) 
                return visitados 
