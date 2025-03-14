import queue

"""El módulo queue en Python proporciona estructuras de datos para manejar colas de manera segura en entornos de múltiples 
hilos (threads). No es compatible con multiprocessing, pero es útil en programación concurrente con threading."""


"""Todas las funciones para manejar colas de manera eficiente en entornos concurrentes"""

#1. put(item, block=True, timeout=None). Añade un elemento a la cola. Si la cola está llena y block=True, espera hasta que haya espacio.
q = queue.Queue(maxsize=2)
q.put("Mensaje 1") 
q.put("Mensaje 2") 
print("Cola llena:", q.full()) # True 

#2. put_nowait(item). Añade un elemento a la cola sin bloquear. Si la cola está llena, lanza una excepción queue.Full.
q = queue.Queue(maxsize=1) 
q.put_nowait("Mensaje 1") 
try: 
    q.put_nowait("Mensaje 2") # La cola está llena 
except queue.Full: 
    print("La cola está llena, no se pudo agregar el segundo mensaje.") 

#3. get(block=True, timeout=None). Extrae un elemento de la cola. Si está vacía y block=True, espera hasta que haya un elemento disponible.
q = queue.Queue()
q.put("Dato importante") 
print(q.get()) # "Dato importante" 

#4. get_nowait(). Obtiene un elemento sin bloquear. Si la cola está vacía, lanza una excepción queue.Empty.
q = queue.Queue() 
try: 
    q.get_nowait() # La cola está vacía 
except queue.Empty: 
    print("No hay elementos en la cola.") 

#5. task_done(). Indica que una tarea obtenida con get() ha sido procesada. Se usa con JoinableQueue.
q = queue.Queue() 
q.put("Tarea 1") 
q.get() 
q.task_done() 
print("Tarea completada.") 

#6. join(). Bloquea hasta que todas las tareas en la cola sean procesadas.
q = queue.Queue() 
def worker(): 
    while not q.empty(): 
        tarea = q.get() 
        print(f"Procesando {tarea}")
    q.task_done() 
    for i in range(3): 
        q.put(f"Tarea {i+1}") 

from threading import Thread 
t = Thread(target=worker) 
t.start() 
q.join() # Espera hasta que todas las tareas sean completadas 
print("Todas las tareas han sido procesadas.") 




"""El módulo queue en Python proporciona varias clases para manejar estructuras de datos en entornos concurrentes"""

#1. queue.Queue (FIFO - Primero en entrar, primero en salir). Esta es la cola estándar donde el primer elemento en entrar es el primero en salir.
q = queue.Queue() 
q.put("Mensaje 1") 
q.put("Mensaje 2") 
print(q.get()) # "Mensaje 1" 
print(q.get()) # "Mensaje 2" 
#Salida esperada: Mensaje 1 Mensaje 2: (El primero en entrar es el primero en salir.)

#2. queue.LifoQueue (LIFO - Último en entrar, primero en salir). Esta es una pila (stack), donde el último elemento agregado es el primero en salir.
q = queue.LifoQueue() 
q.put("A") 
q.put("B") 
print(q.get()) # "B" print(q.get()) # "A" 
#(El último en entrar es el primero en salir.)

#3. queue.PriorityQueue (Cola con prioridad). Los elementos se almacenan en orden de prioridad. Se usa una tupla (prioridad, valor), donde los valores con menor prioridad salen primero.
q = queue.PriorityQueue() 
q.put((2, "Segundo")) 
q.put((1, "Primero")) 
q.put((3, "Tercero")) 
print(q.get()) # (1, "Primero") 
print(q.get()) # (2, "Segundo") 
print(q.get()) # (3, "Tercero") 
#Salida esperada: (1, "Primero") (2, "Segundo") (3, "Tercero"): (El menor número de prioridad sale primero.)

#4. queue.SimpleQueue (Cola FIFO más ligera, desde Python 3.7). Es similar a Queue, pero sin funciones avanzadas como task_done() y join(), lo que la hace más rápida.
q = queue.SimpleQueue() 
q.put("Mensaje 1") 
q.put("Mensaje 2")
print(q.get()) # "Mensaje 1" 
print(q.get()) # "Mensaje 2" 
#Salida esperada: Mensaje 1 Mensaje 2: (Funciona igual que Queue, pero con menos funciones.)

#Queue → Cola FIFO normal.
#LifoQueue → Funciona como pila (stack).
#PriorityQueue → Organiza por prioridad.
#SimpleQueue → Versión más ligera de Queue.




"""El módulo queue en Python tiene tres variables de excepción predefinidas, que se utilizan para manejar errores cuando se 
trabaja con colas. No tiene otras variables globales o constantes."""

"""1. queue.Empty. Se lanza cuando intentas obtener un elemento de una cola vacía usando get_nowait() o get(timeout=segundos) y el tiempo se agota."""
q = queue.Queue() 
try: 
    q.get_nowait() # Intentar obtener un elemento de una cola vacía 
except queue.Empty: 
    print("La cola está vacía, no hay elementos para obtener.") 
#Salida esperada: La cola está vacía, no hay elementos para obtener. 

#2. queue.Full. Se lanza cuando intentas agregar un elemento a una cola llena usando put_nowait().
q = queue.Queue(maxsize=1)
q.put("Elemento único") 
try: 
    q.put_nowait("Otro elemento") # La cola ya está llena 
except queue.Full: 
    print("La cola está llena, no se pueden agregar más elementos.") 
#Salida esperada: La cola está llena, no se pueden agregar más elementos. 

3. queue.Deque (Desde Python 3.9). Esta variable apunta a collections.deque, una estructura de datos altamente eficiente para colas y pilas.
from queue import Deque 
dq = Deque() 
dq.append("Frente") # Agregar al final 
dq.appendleft("Atrás") # Agregar al inicio 
print(dq.pop()) # "Frente" 
print(dq.popleft()) # "Atrás" 
#Salida esperada: Frente Atrás: (Funciona como una doble cola eficiente.)



"""El módulo queue en Python no tiene variables globales o constantes, aparte de las excepciones (Empty, Full) y Deque que ya 
mencioné antes. No existen variables como multiprocessing.cpu_count() o constantes predefinidas."""

#El módulo queue en Python define dos excepciones principales para manejar errores cuando se trabaja con colas en entornos concurrentes. 

#1. queue.Empty. Se lanza cuando intentas obtener un elemento de una cola vacía usando:
get_nowait()
get(block=False)
get(timeout=n) si el tiempo se agota
q = queue.Queue() 
try: 
    q.get_nowait() # Intentar obtener un elemento de una cola vacía 
except queue.Empty: 
    print("La cola está vacía, no hay elementos para obtener.") 
#Salida esperada: La cola está vacía, no hay elementos para obtener: (Se lanza la excepción porque la cola no tiene elementos.)

#2. queue.Full. Se lanza cuando intentas agregar un elemento a una cola llena usando:
put_nowait()
put(block=False)
put(timeout=n) si el tiempo se agota
q = queue.Queue(maxsize=1) # Cola con solo 1 espacio 
q.put("Elemento único") # Se llena la cola 
try: 
    q.put_nowait("Otro elemento") # La cola ya está llena 
except queue.Full: 
    print("La cola está llena, no se pueden agregar más elementos.") 
#Salida esperada: La cola está llena, no se pueden agregar más elementos: (Se lanza la excepción porque la cola alcanzó su límite de elementos.)
#queue.Empty → Se lanza cuando intentas obtener un elemento de una cola vacía.
#queue.Full → Se lanza cuando intentas agregar un elemento a una cola llena.




E"""l módulo queue no tiene submódulos, solo clases y excepciones dentro de él."""

