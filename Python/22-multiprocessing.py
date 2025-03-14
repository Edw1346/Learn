import multiprocessing

"""El módulo multiprocessing en Python permite ejecutar código en múltiples procesos, aprovechando varios núcleos de la CPU para 
mejorar el rendimiento en tareas que requieren mucho tiempo de cómputo. A diferencia de los hilos (threading), los procesos 
son independientes y no comparten memoria, lo que puede evitar algunos problemas de sincronización."""
#Procesos: Puedes crear procesos paralelos utilizando la clase Process. Cada proceso tiene su propia memoria y se ejecuta en su propio espacio de direcciones.
#Colas y Pipes: Permiten la comunicación entre procesos. Las Queue y Pipe se utilizan para enviar datos entre procesos de manera segura.
#Pools de procesos: Con Pool, puedes crear un grupo de procesos para ejecutar tareas en paralelo y distribuir el trabajo.
#Sincronización: Usa Lock, Event, Semaphore, entre otros, para coordinar el acceso a recursos compartidos.





"""El módulo multiprocessing incluye una variedad de funciones útiles para trabajar con múltiples procesos."""

#1. multiprocessing.cpu_count(). Devuelve el número de núcleos de la CPU disponibles en el sistema.
print(multiprocessing.cpu_count()) # Muestra el número de núcleos de la CPU 

#2. multiprocessing.get_start_method(). Devuelve el método de inicio para crear nuevos procesos. Los métodos disponibles son 'fork', 'spawn' y 'forkserver'.
print(multiprocessing.get_start_method()) # Muestra el método de inicio actual 

#3. multiprocessing.set_start_method(). Establece el método de inicio para la creación de procesos.
multiprocessing.set_start_method('spawn') # Establece el método de inicio a 'spawn' 

#4. multiprocessing.get_start_method(). Devuelve el método de inicio actual (fork, spawn, o forkserver)
print(multiprocessing.get_start_method()) 

#5. multiprocessing.active_children(). Devuelve una lista de los procesos hijos que están todavía activos.
print(multiprocessing.active_children()) # Muestra los procesos hijos activos 

#6. multiprocessing.get_all_start_methods(). Devuelve los métodos de inicio de procesos disponibles en el sistema.
print(multiprocessing.get_all_start_methods()) # Muestra los métodos disponibles 

#7. multiprocessing.Manager(). Crea un objeto de administración compartido para gestionar datos entre procesos.
from multiprocessing import Manager 
with Manager() as manager: 
    d = manager.dict() # Crea un diccionario compartido entre procesos 

#8. multiprocessing.get_start_method(). Muestra el método actual para iniciar procesos.
print(multiprocessing.get_start_method()) # Muestra el método actual de inicio 



"""El módulo multiprocessing de Python contiene varias clases útiles para trabajar con procesos. """

#1. multiprocessing.Process. Representa un proceso en ejecución. Permite crear y controlar procesos paralelos.
#Métodos comunes: 
#start(): Inicia el proceso.
#join(): Espera a que el proceso termine.
#is_alive(): Verifica si el proceso está en ejecución.
from multiprocessing import Process 
def tarea(): 
    print("Proceso en ejecución") 
    p = Process(target=tarea) 
p.start() # Inicia el proceso 
p.join() # Espera a que termine 

#2. multiprocessing.Queue. Es una cola segura para usar en la comunicación entre procesos. Permite pasar datos entre procesos de manera segura.
#Métodos comunes: 
#put(): Inserta un item en la cola.
#get(): Extrae un item de la cola.
#empty(): Verifica si la cola está vacía.
from multiprocessing import Queue 
q = Queue() 
q.put(10) # Inserta un valor en la cola 
print(q.get()) # Extrae el valor de la cola 

#3. multiprocessing.Pool. Permite ejecutar tareas en paralelo utilizando un grupo de procesos (pool). Es útil para distribuir trabajos a varios procesos.
#Métodos comunes: 
#apply(): Ejecuta una función en un solo proceso.
#map(): Ejecuta una función en paralelo en múltiples entradas.
#close(): Cierra el pool de procesos.
#join(): Espera a que todos los procesos del pool terminen.
from multiprocessing import Pool 
def cuadrado(n): 
    return n * n 
with Pool(4) as p: # Crea un pool con 4 procesos 
    print(p.map(cuadrado, [1, 2, 3, 4])) # Ejecuta la función en paralelo 

#4. multiprocessing.Lock. Un objeto de bloqueo utilizado para sincronizar procesos y evitar la condición de carrera (race condition).
#Métodos comunes: 
#acquire(): Adquiere el bloqueo.
#release(): Libera el bloqueo.
from multiprocessing import Lock 
lock = Lock() 
def tarea(): 
    with lock: # Asegura que solo un proceso acceda a la sección crítica 
    print("Accediendo a la sección crítica") 

#5. multiprocessing.Semaphore. Es similar a un Lock, pero permite que múltiples procesos adquieran el semáforo hasta un límite máximo.
#Métodos comunes: 
#acquire(): Adquiere el semáforo.
#release(): Libera el semáforo.
from multiprocessing import Semaphore 
sem = Semaphore(2) # Permite que dos procesos accedan simultáneamente 
def tarea(): 
    with sem: 
        print("Accediendo a la sección crítica") 

#6. multiprocessing.Event. Se utiliza para comunicar procesos a través de un evento. Los procesos pueden esperar a que el evento se active.
#Métodos comunes: 
#set(): Activa el evento.
#clear(): Desactiva el evento.
#wait(): Espera a que el evento se active.
from multiprocessing import Event 
evento = Event() 
def tarea(): 
    evento.wait() # Espera hasta que el evento se active 
    print("Evento activado, tarea ejecutada") 

#7. multiprocessing.Condition. Utilizado para sincronizar el acceso a un recurso compartido, de manera que los procesos puedan esperar o notificar condiciones específicas.
#Métodos comunes: 
#wait(): Hace que el proceso espere hasta que se notifique la condición.
#notify(): Notifica a un proceso que puede continuar.
#notify_all(): Notifica a todos los procesos esperando la condición.
from multiprocessing import Condition 
cond = Condition() 
def tarea(): 
    with cond: 
        cond.wait() # Espera hasta que se notifique la condición 
        print("Condición cumplida") 

#8. multiprocessing.Value. Permite crear variables compartidas entre procesos. Las variables pueden ser de tipo int, float, etc.
from multiprocessing import Value 
val = Value('i', 0) # Crea un valor entero compartido 

#9. multiprocessing.Array. Similar a Value, pero permite crear arrays compartidos entre procesos.
from multiprocessing import Array 
arr = Array('i', range(10)) # Crea un array de enteros compartido entre procesos 




"""El módulo multiprocessing no contiene muchas variables definidas por defecto, pero hay algunas que son importantes y que 
puedes utilizar al trabajar con múltiples procesos. """
#Variables principales del módulo multiprocessing:

#multiprocessing.current_process(). Devuelve un objeto que representa el proceso actual. Puedes utilizarlo para obtener detalles sobre el proceso, como su nombre o ID.
from multiprocessing import current_process 
p = current_process() 
print(p.name) # Muestra el nombre del proceso actual 

#multiprocessing.active_children(). Devuelve una lista de los procesos hijos activos. Esta función puede ser útil para realizar un seguimiento de los procesos en ejecución.
from multiprocessing import Process, active_children 
def tarea(): 
    print("Proceso en ejecución") 

p1 = Process(target=tarea) 
p2 = Process(target=tarea) 
p1.start() 
p2.start() 
print(active_children()) # Muestra los procesos hijos activos 
p1.join() 
p2.join() 

#multiprocessing.get_start_method(). Devuelve el método actual de inicio de los procesos en el sistema. Los métodos disponibles son 'fork', 'spawn', y 'forkserver'.
from multiprocessing import get_start_method 
print(get_start_method()) # Muestra el método de inicio de procesos actual 

#multiprocessing.get_all_start_methods(). Devuelve todos los métodos de inicio de procesos disponibles en el sistema. Esto es útil para saber qué métodos de inicio puedes usar.
from multiprocessing import get_all_start_methods 
print(get_all_start_methods()) # Muestra todos los métodos de inicio disponibles 

#multiprocessing.pool._DEFAULT_CONTEXT. Esta variable interna se usa dentro de los Pool para determinar el contexto de inicio por defecto. En general, no es de uso frecuente fuera del contexto interno del módulo.

#multiprocessing.get_start_method(). Devuelve el método actual para la creación de nuevos procesos en el sistema.
print(multiprocessing.get_start_method()) 



"""Todas las constantes importantes del módulo multiprocessing"""

#1. multiprocessing.cpu_count(). Devuelve el número de núcleos del procesador disponibles en el sistema.
import multiprocessing # Obtener el número de núcleos de CPU 
num_procesadores = multiprocessing.cpu_count() 
print(f"Número de núcleos disponibles: {num_procesadores}") 
#Salida esperada: Número de núcleos disponibles: 8 

#2. multiprocessing.current_process(). Devuelve el objeto del proceso que se está ejecutando en ese momento.
import multiprocessing 
def worker(): 
    proceso = multiprocessing.current_process() 
    print(f"Proceso actual: {proceso.name}, PID: {proceso.pid}") 

if __name__ == "__main__": 
    proceso = multiprocessing.Process(target=worker) 
proceso.start() 
proceso.join() 
#Salida esperada: Proceso actual: Process-1, PID: 12345   (El número de PID cambiará según el sistema.)

#3. multiprocessing.active_children(). Devuelve una lista con los procesos hijos activos en ese momento.
import multiprocessing 
import time 
def worker(): 
    time.sleep(2) # Simulamos un trabajo en segundo plano 

if __name__ == "__main__": 
    procesos = [multiprocessing.Process(target=worker) for _ in range(3)] 
    for p in procesos: 
        p.start() 
        print(f"Procesos activos: {multiprocessing.active_children()}") 
    for p in procesos: 
        p.join() 
#Salida esperada: Procesos activos: [<Process(Process-1, started)>, <Process(Process-2, started)>, <Process(Process-3, started)>]  (Mientras los procesos estén corriendo, aparecerán en la lista.)

#4. multiprocessing.Lock(). Evita que varios procesos accedan a un recurso compartido al mismo tiempo.
import multiprocessing 
import time 
def tarea(lock): 
    with lock: # Bloqueamos el acceso para un solo proceso a la vez 
        print(f"{multiprocessing.current_process().name} accediendo...") 
        time.sleep(1) 
    if __name__ == "__main__": 
        lock = multiprocessing.Lock() 
        procesos = [multiprocessing.Process(target=tarea, args=(lock,)) for _ in range(3)] 
        for p in procesos: 
            p.start() 
        for p in procesos:
            p.join() 
#Salida esperada: Process-1 accediendo... Process-2 accediendo... Process-3 accediendo... 

#5. multiprocessing.Semaphore(). Controla el número máximo de procesos que pueden ejecutarse simultáneamente.
import multiprocessing 
import time 
def tarea(sem): 
    with sem: 
        print(f"{multiprocessing.current_process().name} ejecutándose...") 
        time.sleep(2)
    if __name__ == "__main__": 
        sem = multiprocessing.Semaphore(2) # Solo 2 procesos a la vez 
        procesos = [multiprocessing.Process(target=tarea, args=(sem,)) for _ in range(4)] 
    for p in procesos: 
        p.start() 
    for p in procesos: 
        p.join() 
#Salida esperada: Process-1 ejecutándose... Process-2 ejecutándose... Process-3 ejecutándose... Process-4 ejecutándose... 

#6. multiprocessing.get_start_method(). Devuelve el método de inicio de procesos usado en el sistema.
metodo = multiprocessing.get_start_method() 
print(f"Método de inicio: {metodo}") 
#Salida esperada en Windows: Método de inicio: spawn 
#Salida esperada en Linux/macOS: Método de inicio: fork 

#7. multiprocessing.Queue(). Permite la comunicación entre procesos mediante una cola de mensajes.
def worker(cola): 
    cola.put("Mensaje desde el proceso hijo")
    if __name__ == "__main__": 
        cola = multiprocessing.Queue()
p = multiprocessing.Process(target=worker, args=(cola,)) 
p.start()
p.join() 
mensaje = cola.get() 
print(f"Mensaje recibido: {mensaje}") 
#Salida esperada: Mensaje recibido: Mensaje desde el proceso hijo 

#8. multiprocessing.Pipe(). Permite la comunicación bidireccional entre dos procesos.
import multiprocessing 
def worker(conn): 
    conn.send("Hola desde el proceso hijo")
    conn.close() 
    if __name__ == "__main__": 
        parent_conn, child_conn = multiprocessing.Pipe() 

p = multiprocessing.Process(target=worker, args=(child_conn,)) 
p.start() 
p.join() 
mensaje = parent_conn.recv() 
print(f"Mensaje recibido: {mensaje}") 
#Salida esperada: Mensaje recibido: Hola desde el proceso hijo 


"""El módulo multiprocessing de Python define varias excepciones que se lanzan en situaciones específicas cuando trabajamos con procesos."""

#1. multiprocessing.ProcessError. Es la excepción base para todos los errores relacionados con procesos en multiprocessing. Todas las demás excepciones específicas heredan de esta.
try: 
    raise multiprocessing.ProcessError("Este es un error de prueba") 
except multiprocessing.ProcessError as e:
    print(f"Se ha producido un error en un proceso: {e}") 
#Salida esperada: Se ha producido un error en un proceso: Este es un error de prueba 

#2. multiprocessing.TimeoutError. Se lanza cuando una operación en un proceso o cola de mensajes tarda más de lo esperado.
import multiprocessing 
import time
def tarea(): 
    time.sleep(5) # Simula una tarea que tarda en ejecutarse 
    if __name__ == "__main__": 
        p = multiprocessing.Process(target=tarea) 
        p.start() 
        try: 
            p.join(timeout=2) # Esperamos solo 2 segundos 
            if p.is_alive(): 
                raise multiprocessing.TimeoutError("El proceso tardó demasiado en completarse") 
        except multiprocessing.TimeoutError as e: 
            print(f"Error: {e}") p.terminate() # Forzar la terminación del proceso 
#Salida esperada: Error: El proceso tardó demasiado en completarse 

#3. multiprocessing.AuthenticationError. Se lanza cuando hay un problema en la autenticación de una conexión de multiprocessing. Nota: Esta excepción se usa con multiprocessing.managers cuando se configura autenticación en una conexión entre procesos remotos.
import multiprocessing.managers 
try: 
    raise multiprocessing.AuthenticationError("Error en la autenticación de la conexión")
except multiprocessing.AuthenticationError as e: 
    print(f"Error de autenticación: {e}") 
#Salida esperada: Error de autenticación: Error en la autenticación de la conexión 

#4. multiprocessing.BrokenPipeError. Ocurre cuando un proceso intenta enviar datos a través de un Pipe cerrado o roto.
def worker(pipe): 
    pipe.close() # Cerramos la conexión intencionalmente 
    if __name__ == "__main__": 
        parent_conn, child_conn = multiprocessing.Pipe() 

p = multiprocessing.Process(target=worker, args=(child_conn,)) 
p.start() 
p.join() 
try: 
parent_conn.send("Mensaje") # Intentamos enviar un mensaje después de que la conexión se cerró 
except BrokenPipeError as e: 
print(f"Error: {e}") 
Salida esperada: Error: [Errno 32] Broken pipe 

#5. multiprocessing.BufferTooShort. Se lanza cuando se intenta recibir datos en un buffer que es demasiado pequeño para almacenarlos. Nota: Esta excepción es poco común y se usa en contextos avanzados con memoria compartida.
import multiprocessing 
import array
def worker(buffer): 
    try: 
        buffer[:3] = array.array("i", [1, 2, 3, 4]) # Intentamos escribir 4 elementos en un buffer de 3 
    except multiprocessing.BufferTooShort as e:
        print(f"Error: {e}") 
    if __name__ == "__main__": 
        buffer = array.array("i", [0, 0, 0]) # Un buffer de tamaño 3 

worker(buffer) 
#Salida esperada: Error: Buffer demasiado pequeño para almacenar los datos. (Este error no siempre se lanza automáticamente, pero este sería el concepto.)





"""El módulo multiprocessing en Python está compuesto por varios submódulos que proporcionan diferentes herramientas para la programación concurrente"""

#1. multiprocessing.process. Este submódulo define la clase Process, que se usa para crear y administrar procesos en Python.
def worker(): 
    print(f"Proceso hijo ejecutándose: {multiprocessing.current_process().name}")
    if __name__ == "__main__": 
        p = multiprocessing.Process(target=worker, name="MiProceso") 
p.start()
p.join() 
#Salida esperada: Proceso hijo ejecutándose: MiProceso. (El proceso se ejecuta y finaliza correctamente.)

#2. multiprocessing.queues. Contiene clases como Queue y JoinableQueue, permiten la comunicación entre procesos mediante colas.
def worker(q): 
    q.put("Mensaje desde el proceso hijo")
    if __name__ == "__main__": 
        q = multiprocessing.Queue() 
p = multiprocessing.Process(target=worker, args=(q,))
p.start()
p.join()
mensaje = q.get() 
print(f"Mensaje recibido: {mensaje}") 
#Salida esperada: Mensaje recibido: Mensaje desde el proceso hijo 

#3. multiprocessing.pool. Define la clase Pool, que permite manejar un conjunto de procesos de manera eficiente.
def cuadrado(x): 
    return x * x
    if __name__ == "__main__": 
        with multiprocessing.Pool(4) as pool: 
            resultados = pool.map(cuadrado, [1, 2, 3, 4, 5])
            print(resultados) 
#Salida esperada: [1, 4, 9, 16, 25] 

#4. multiprocessing.synchronize. Contiene herramientas para sincronizar procesos, como Lock, Event, Condition y Semaphore.
import multiprocessing 
import time
def tarea(lock): 
    with lock: 
        print(f"{multiprocessing.current_process().name} accediendo...") 
        time.sleep(1) 
    if __name__ == "__main__": 
        lock = multiprocessing.Lock() 
        procesos = [multiprocessing.Process(target=tarea, args=(lock,)) for _ in range(3)] 
        for p in procesos: 
            p.start() 
        for p in procesos: 
            p.join() 
#Salida esperada (procesos accediendo uno por uno): Process-1 accediendo... Process-2 accediendo... Process-3 accediendo... 

#5. multiprocessing.shared_memory. Permite compartir datos entre procesos sin necesidad de enviar copias. Disponible desde Python 3.8.
import multiprocessing.shared_memory
def worker(): 
    existing_shm = multiprocessing.shared_memory.SharedMemory(name="mi_memoria") 
    existing_shm.buf[0] = 42 # Modificamos el primer byte 
    existing_shm.close() 
    if __name__ == "__main__": 
        shm = multiprocessing.shared_memory.SharedMemory(create=True, size=10, name="mi_memoria") 
p = multiprocessing.Process(target=worker) 
p.start() 
p.join() 
print(f"Primer byte en memoria compartida: {shm.buf[0]}") 
shm.close() 
shm.unlink() 
#Salida esperada: Primer byte en memoria compartida: 42 

"6. multiprocessing.managers. Permite crear servidores que comparten objetos entre procesos, incluso en máquinas diferentes.
import multiprocessing 
import multiprocessing.managers
class MiManager(multiprocessing.managers.BaseManager): 
    pass 

MiManager.register("lista_compartida", list)

def worker(lista): 
    lista.append("Hola desde el proceso hijo") 
    if __name__ == "__main__": 
        with MiManager() as manager:
            lista = manager.lista_compartida() 
p = multiprocessing.Process(target=worker, args=(lista,)) 
p.start() 
p.join() 
print(lista) 
Salida esperada: ['Hola desde el proceso hijo'] 
