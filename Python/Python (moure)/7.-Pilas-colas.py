"""Las pilas y colas"""

"""Pilas (Stack): Una pila es una estructura de datos que sigue el principio LIFO (Last In, First Out), lo que significa que el último elemento insertado es el primero en ser retirado.
Las operaciones más comunes son: 
push(): Insertar un elemento en la pila.
pop(): Eliminar el elemento superior de la pila.
peek() (o top): Obtener el valor del elemento superior sin eliminarlo.
isEmpty(): Verificar si la pila está vacía.
Ejemplo en Python con lista (que funciona como pila):"""
pila = [] 
pila.append(1) # push 
pila.append(2) # push
pila.append(3) # push 
print(pila.pop()) # pop: 3 
print(pila[-1]) # peek: 2 

"""Colas (Queue): Una cola es una estructura de datos que sigue el principio FIFO (First In, First Out), lo que significa que el primer elemento insertado es el primero en ser retirado. Las operaciones más comunes son: 
enqueue(): Insertar un elemento al final de la cola.
dequeue(): Eliminar el primer elemento de la cola.
front(): Obtener el valor del primer elemento sin eliminarlo.
isEmpty(): Verificar si la cola está vacía.

Ejemplo en Python con deque (de collections) que funciona como cola:"""
from collections import deque 
cola = deque() 
cola.append(1) # enqueue 
cola.append(2) # enqueue 
cola.append(3) # enqueue 
print(cola.popleft()) # dequeue: 1 
print(cola[0]) # front: 2 


"""Conceptos clave relacionados con pilas y colas:"""

"""1. Estructura de Datos: Estructura de datos se refiere a una manera de organizar y almacenar datos en un sistema para poder acceder y modificarlos de manera eficiente. Las pilas y las colas son ejemplos de estructuras de datos.

2. Operaciones Básicas
Push: Inserción de un elemento en una pila.
Pop: Eliminación del elemento superior de una pila.
Peek o Top: Acceso al elemento superior de la pila sin eliminarlo.
Enqueue: Inserción de un elemento en una cola.
Dequeue: Eliminación del primer elemento de una cola.
Front: Acceso al primer elemento de la cola sin eliminarlo.

3. Principios de Ordenación
LIFO (Last In, First Out): El último elemento insertado es el primero en ser retirado (aplica a pilas).
FIFO (First In, First Out): El primer elemento insertado es el primero en ser retirado (aplica a colas)."""

"""Conceptos Relacionados con Pilas"""
"""1. Pila Estática vs. Pila Dinámica
Pila Estática: Utiliza una cantidad fija de memoria, típicamente implementada con arrays o listas, limita capacidad de pila.
Pila Dinámica: Se ajusta según la cantidad de elementos que contiene, generalmente implementada mediante listas enlazadas.

2. Desbordamiento de Pila (Stack Overflow): Ocurre cuando una pila supera su límite de capacidad. Esto es común en recursión profunda o cuando no se gestionan adecuadamente las llamadas recursivas.

3. Funciones de Recursión y Pila: Las funciones recursivas utilizan la pila de llamadas del sistema. Cada vez que se realiza una llamada recursiva, se empuja un nuevo contexto de ejecución en la pila. Si la recursión es demasiado profunda, puede causar un desbordamiento de pila.

4. Pila de Llamadas (Call Stack): Es una pila interna del sistema utilizada para gestionar las llamadas a funciones. Cada vez que una función es llamada, se agrega un nuevo marco a la pila, y al retornar, se elimina el marco superior."""

"""Conceptos Relacionados con Colas"""
"""1. Cola Estática vs. Cola Dinámica
Cola Estática: Similar a la pila estática, tiene una capacidad fija. Usualmente se implementa con un arreglo.
Cola Dinámica: De tamaño variable, comúnmente implementada con listas enlazadas.

2. Cola Circular: Es una variación de la cola, donde cuando el final de la cola alcanza el final de la estructura, se "envuelve" al principio. Esto ayuda a evitar la necesidad de mover los elementos cuando se hace un dequeue o un enqueue."""
#Ejemplo de Cola Circular:
class ColaCircular: 
    def __init__(self, capacidad): 
        self.capacidad = capacidad 
        self.cola = [None] * capacidad 
        self.frente = 0 
        self.final = 0 

    def enqueue(self, valor): 
        if (self.final + 1) % self.capacidad == self.frente: 
            print("Cola llena") 
            return self.cola[self.final] = valor
        self.final = (self.final + 1) % self.capacidad 

    def dequeue(self): 
        if self.frente == self.final: 
            print("Cola vacía") 
            return None 
        valor = self.cola[self.frente] 
        self.frente = (self.frente + 1) % self.capacidad 
        return valor 

"""3. Cola de Prioridad: Una cola de prioridad es una variante de la cola que da prioridad a los elementos con una prioridad más alta, en lugar de seguir estrictamente el orden de llegada. Se utiliza con frecuencia en algoritmos Dijkstra y A (A-star)*.

4. Implementación de Cola con Deque: El deque (Double-ended Queue) es una estructura que permite insertar y eliminar elementos tanto por el principio como por el final, lo que lo hace útil para implementar colas de forma eficiente."""

"""Conceptos Relacionados con Pilas y Colas en Algoritmos"""
"""1. Recursión y Pilas: Las pilas se utilizan para gestionar las llamadas recursivas. Cada vez que se llama a una función recursiva, el marco de ejecución se apila. La recursión también puede ser convertida en una solución iterativa utilizando una pila explícita.

2. Búsqueda en Profundidad (DFS) y Pilas: El DFS (Depth-First Search) explora los nodos de un grafo o árbol a través de pilas, visitando primero un nodo y sus hijos antes de retroceder a los nodos anteriores.

3. Búsqueda en Anchura (BFS) y Colas: El BFS (Breadth-First Search) explora los nodos de un grafo o árbol por niveles, visitando todos los nodos de un nivel antes de pasar al siguiente. Se implementa con una cola."""

"""Conceptos Avanzados Relacionados"""
"""1. Complejidad de Tiempo de Pilas y Colas: Las operaciones básicas de pilas y colas (como push(), pop(), enqueue(), y dequeue()) generalmente tienen una complejidad de tiempo de O(1), lo que las hace muy eficientes.

2. Pila de Operadores (En Evaluación de Expresiones): En la evaluación de expresiones aritméticas, las pilas se utilizan para almacenar operadores y operandos, especialmente en algoritmos de evaluación de notación infija a postfija (algoritmo de Shunting Yard).

3. Algoritmo de Dijkstra: El algoritmo de Dijkstra, utilizado para encontrar el camino más corto en un grafo ponderado, puede usar una cola de prioridad para obtener el nodo más cercano no visitado de manera eficiente."""



"""Buenas Prácticas:"""

"""1. Uso de pilas para problemas de recursión. En muchos lenguajes de programación, las llamadas recursivas se manejan mediante una pila interna (la pila de llamadas), útil simular la recursión utilizando una pila para evitar el desbordamiento de pila, especialmente en casos donde la recursión es profunda. Ejemplo: DFS (Depth-First Search) con pila"""
def dfs(grafo, nodo_inicial): 
    visitados = set() 
    pila = [nodo_inicial] 
    while pila: 
        nodo = pila.pop() 
        if nodo not in visitados: 
            visitados.add(nodo) 
            pila.extend(grafo[nodo] - visitados) 
            return visitados 


"""2. Uso de colas para problemas de búsqueda de nivel
Las colas son útiles en problemas como el búsqueda en anchura (BFS), donde los nodos se exploran de manera ordenada por niveles (primero los nodos más cercanos a la raíz). Ejemplo: BFS (Breadth-First Search) con cola"""
from collections import deque 
def bfs(grafo, nodo_inicial): 
    visitados = set() 
    cola = deque([nodo_inicial]) 
    while cola: 
        nodo = cola.popleft() 
        if nodo not in visitados: 
            visitados.add(nodo) 
            cola.extend(grafo[nodo] - visitados) 
            return visitados 

"""3. Implementación eficiente con colecciones estándar
Para implementar pilas y colas, las listas pueden ser utilizadas para pilas, pero para colas es más eficiente utilizar la clase deque de la biblioteca collections, ya que la operación pop(0) en una lista es costosa () mientras que popleft() en un deque es eficiente ()."""

"""4. Evitar el uso de índices en listas para simulaciones de pilas y colas
Para evitar problemas de manejo de índices y mejorar la claridad del código, es mejor usar funciones como append() y pop() para pilas y append() y popleft() para colas, ya que proporcionan una forma clara y directa de manipular los elementos de estas estructuras."""

"""Técnicas Avanzadas:"""

"""1. Colas con prioridad (Priority Queues)
Las colas con prioridad son una variante de las colas tradicionales donde cada elemento tiene una prioridad. El elemento con la prioridad más alta se elimina primero. En Python, la implementación estándar es la heapq, que proporciona una cola de prioridad mínima (el valor más pequeño tiene la prioridad más alta). Ejemplo: Cola con prioridad usando heapq"""
import heapq 
cola_prioridad = [] 
heapq.heappush(cola_prioridad, (1, 'tarea baja')) # Prioridad 1 
heapq.heappush(cola_prioridad, (3, 'tarea alta')) # Prioridad 3 
heapq.heappush(cola_prioridad, (2, 'tarea media')) # Prioridad 2 
print(heapq.heappop(cola_prioridad)) # (1, 'tarea baja') 

"""2. Implementación de pila con doble enlace (Doubly Linked List)
Si necesitas una pila de tamaño variable en la que las operaciones de inserción y eliminación sean muy rápidas, una lista doblemente enlazada es más eficiente que una lista tradicional en términos de complejidad de tiempo. Ejemplo de pila con lista doblemente enlazada"""
class Nodo: 
    def __init__(self, valor): 
        self.valor = valor 
        self.siguiente = None 
        self.anterior = None 

class Pila: 
    def __init__(self): 
        self.tope = None 

    def push(self, valor): 
        nuevo_nodo = Nodo(valor) 
        if self.tope is None:
            self.tope = nuevo_nodo 
        else: 
            nuevo_nodo.siguiente = self.tope 
            self.tope.anterior = nuevo_nodo 
            self.tope = nuevo_nodo   
    
    def pop(self): 
        if self.tope is None: 
            return None 
        valor = self.tope.valor 
        self.tope = self.tope.siguiente 
        if self.tope: 
            self.tope.anterior = None 
            return valor 

"""3. Simulación de recursión con pila explícita
Si una función recursiva consume demasiado espacio de pila, puedes simular la recursión utilizando una pila explícita, lo que permite controlar mejor el flujo y la memoria. Ejemplo: Recursión de árbol simulado con pila"""
def recorrido_arbol(arbol): 
    pila = [arbol] 
    while pila: 
        nodo = pila.pop() 
        if nodo: 
            print(nodo.valor) 
            pila.append(nodo.derecha) 
            pila.append(nodo.izquierda)