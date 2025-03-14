import threading

"""El módulo threading en Python permite ejecutar múltiples hilos (threads) de forma concurrente en un solo proceso. Esto es 
útil cuando quieres realizar varias tareas a la vez, como por ejemplo descargar varios archivos simultáneamente o realizar 
cálculos sin bloquear la ejecución del programa principal."""
#Hilo (Thread): Un hilo es una unidad de ejecución dentro de un proceso. En Python, los hilos permiten que el programa haga varias cosas a la vez (aunque, debido al GIL de Python, los hilos no ejecutan código de Python al mismo tiempo en un solo núcleo, pero son útiles para tareas I/O).
#Threading: Usando threading, puedes crear y manejar hilos fácilmente, lo que mejora el rendimiento en tareas de I/O, como la lectura de archivos o solicitudes a servidores.


"""Las funciones disponibles en este módulo"""

#1. threading.active_count(). Devuelve el número de hilos activos en el sistema, incluidos los hilos principales y los de la biblioteca.
print(threading.active_count()) 

#2. threading.current_thread(). Devuelve el objeto Thread del hilo que está ejecutando el código actual.
print(threading.current_thread()) 

#3. threading.enumerate(), Devuelve una lista de todos los hilos activos (los que no han terminado aún).
print(threading.enumerate()) 

#4. threading.main_thread(). Devuelve el hilo principal del programa.
print(threading.main_thread()) 

#5. threading.settrace(). Establece una función de seguimiento (trace function) que se ejecutará en cada hilo.
def mi_funcion_trace(frame, event, arg): 
    print(f"Evento: {event}") 
    return mi_funcion_trace threading.settrace(mi_funcion_trace) 

#6. threading.local(). Crea un objeto local de datos, lo que permite tener variables específicas para cada hilo.
data = threading.local() 
data.valor = 42 

#7. threading.get_ident(). Devuelve la identificación única del hilo actual.
print(threading.get_ident()) 

#8. threading.Event(). Devuelve un objeto Event que se puede usar para sincronizar hilos.
event = threading.Event() 
event.set() # Establece el evento 
event.wait() # Bloquea hasta que el evento esté activado 

#9. threading.Lock(). Devuelve un objeto Lock, que es utilizado para manejar el acceso exclusivo a un recurso compartido por múltiples hilos.
lock = threading.Lock() 
lock.acquire() # Bloquea el lock 
lock.release() # Libera el lock 

#10. threading.RLock(). Devuelve un objeto RLock (lock recursivo), que permite que un hilo lo adquiera varias veces.
rlock = threading.RLock() 
rlock.acquire() 
rlock.acquire() # Puedes adquirirlo dos veces rlock.release() rlock.release() 

#11. threading.Semaphore().Devuelve un objeto Semaphore, utilizado para limitar el número de hilos que pueden acceder a un recurso en particular.
semaphore = threading.Semaphore(2) 
semaphore.acquire() # Bloquea hasta que el semáforo se libere 
semaphore.release() # Libera el semáforo 

#12. threading.Condition(). Devuelve un objeto Condition, utilizado para coordinar múltiples hilos de forma más compleja.
condition = threading.Condition() 
with condition: condition.wait() # Espera que se notifique 
    condition.notify() # Notifica a los hilos esperando 

#13. threading.Timer(). Devuelve un objeto Timer que ejecuta una función después de un tiempo específico.
def decir_hola(): 
    print("¡Hola!") 
    timer = threading.Timer(2.0, decir_hola) 
    timer.start() # Ejecuta decir_hola después de 2 segundos 





"""El módulo threading en Python incluye varias clases que permiten manejar y coordinar la ejecución de hilos"""

#1. Thread. Es la clase principal para crear y manejar hilos en Python. Se utiliza para definir el hilo que se va a ejecutar y gestionar su vida útil (iniciar, esperar, etc.).
#Métodos principales: 
#start(): Inicia la ejecución del hilo.
#join(): Bloquea el hilo principal hasta que el hilo termine.
#is_alive(): Devuelve True si el hilo está en ejecución.
#run(): Define la tarea que ejecutará el hilo.
def tarea(): 
    print("Ejecutando tarea en hilo") 
    hilo = threading.Thread(target=tarea) 
    hilo.start() 
    hilo.join() 

#2. Lock. Es una clase utilizada para manejar el acceso exclusivo a un recurso compartido. El Lock permite que solo un hilo pueda acceder al recurso en un momento dado.
#Métodos principales: 
#acquire(): Bloquea el Lock.
#release(): Libera el Lock.
lock = threading.Lock() 
def tarea(): 
    with lock: 
        print("Accediendo al recurso exclusivo") 
hilo1 = threading.Thread(target=tarea) 
hilo2 = threading.Thread(target=tarea) 
hilo1.start() 
hilo2.start() 
hilo1.join() 
hilo2.join() 

#3. RLock (Reentrant Lock). Es una variante de Lock que permite que el mismo hilo adquiera el bloqueo varias veces sin causar un deadlock.
#Métodos principales: 
#acquire(): Bloquea el RLock.
#release(): Libera el RLock.
#rlock = threading.RLock() 
def tarea(): 
    with rlock:
        print("Accediendo al recurso con RLock") 

hilo1 = threading.Thread(target=tarea) 
hilo1.start() 
hilo1.join() 

#4. Semaphore. Un semáforo es utilizado para limitar el número de hilos que pueden acceder a un recurso compartido simultáneamente. Puede contar hasta un valor específico y decrecer con cada acquire() y aumentar con cada release().
#Métodos principales: 
#acquire(): Disminuye el contador del semáforo.
#release(): Aumenta el contador del semáforo.
semaforo = threading.Semaphore(2) 
def tarea(): 
    semaforo.acquire() 
    print("Recurso adquirido")
    semaforo.release()

hilo1 = threading.Thread(target=tarea) 
hilo2 = threading.Thread(target=tarea) 
hilo3 = threading.Thread(target=tarea) 
hilo1.start() 
hilo2.start() 
hilo3.start() 
hilo1.join() 
hilo2.join() 
hilo3.join() 

#5. Condition. Es una clase utilizada para sincronizar hilos de manera más avanzada. Los objetos Condition permiten que los hilos se bloqueen y se despierten bajo ciertas condiciones.
#Métodos principales: 
#acquire(): Bloquea el objeto Condition.
#release(): Libera el objeto Condition.
#wait(): Bloquea el hilo hasta que reciba una notificación.
#notify(): Despierta un hilo bloqueado en wait().
#notify_all(): Despierta a todos los hilos bloqueados en wait().
condition = threading.Condition() 
def tarea(): 
    with condition: 
        condition.wait() # Espera a que se notifique 
        print("Tarea ejecutada después de la notificación") 

hilo = threading.Thread(target=tarea) 
hilo.start() 
condition.notify() # Notifica al hilo que está esperando 
hilo.join() 

#6. Event. Es una clase que permite la sincronización entre hilos. Un Event puede ser usado para que un hilo espere hasta que otro hilo le notifique que puede continuar.
#Métodos principales: 
#set(): Establece el evento, permitiendo que otros hilos lo usen para continuar.
#clear(): Borra el evento, bloqueando a los hilos que están esperando.
#wait(): Bloquea el hilo hasta que el evento sea establecido.
event = threading.Event() 
def tarea(): 
    print("Esperando evento") 
    event.wait() # Espera a que el evento se establezca 
    print("Evento recibido, tarea ejecutada") 
hilo = threading.Thread(target=tarea) 
hilo.start() 
event.set() # Establece el evento, permitiendo que el hilo continúe 
hilo.join() 

#7. Timer. Es una clase utilizada para ejecutar una función después de un tiempo específico. Se puede usar para crear hilos que ejecuten tareas después de un retraso.
#Métodos principales: 
#start(): Inicia el temporizador.
#cancel(): Cancela el temporizador antes de que se ejecute.
def tarea(): 
    print("Tarea ejecutada después de un retraso") 
    timer = threading.Timer(2.0, tarea) # Ejecutará `tarea` después de 2 segundos 
    timer.start() 

#Thread: Clase para crear y manejar hilos.
#Lock: Bloqueo simple para evitar el acceso concurrente a recursos.
#RLock: Bloqueo recursivo que permite múltiples adquisiciones por un hilo.
#Semaphore: Controla el acceso a un número limitado de recursos compartidos.
#Condition: Sincroniza hilos más complejamente con condiciones de espera y notificación.
#Event: Permite la sincronización de hilos mediante la señalización de eventos.
#Timer: Ejecuta una función después de un retraso especificado.



"""El módulo threading en Python no tiene muchas "variables" explícitas como tal, pero incluye algunas variables de configuración 
y propiedades que se pueden usar para manejar el comportamiento de los hilos y la sincronización"""

#1. threading.active_count(): Devuelve el número de hilos activos actualmente.
print(threading.active_count()) # Muestra el número de hilos activos 

#2. threading.current_thread(): Devuelve el objeto del hilo que está ejecutando el código en el momento. Esto te permite obtener información sobre el hilo que está ejecutando el código.
print(threading.current_thread().name) # Muestra el nombre del hilo actual 

#3. threading.main_thread(): Devuelve el objeto del hilo principal (el hilo que inicia la ejecución del programa).
print(threading.main_thread().name) # Muestra el nombre del hilo principal 

#4. threading.local(): Crea un objeto local para almacenar datos específicos de cada hilo. Este objeto permite almacenar información que es accesible solo dentro del hilo en el que se ha creado.
thread_local = threading.local() 
thread_local.value = 42 
def tarea(): 
    print(thread_local.value) 
hilo = threading.Thread(target=tarea) 
hilo.start() 
hilo.join() 

#5. threading.TIMEOUT_MAX: Es un valor constante que indica el tiempo máximo para un bloqueo de sincronización. Si se supera, se lanzará una excepción TimeoutError en algunos métodos, como en los de Lock, Semaphore, etc. Se utiliza cuando se necesita especificar el tiempo máximo de espera en ciertas funciones, pero no es una variable que se configure explícitamente en el código de forma frecuente.
try: # Intentar adquirir un lock con timeout 
    lock = threading.Lock()
    lock.acquire(timeout=threading.TIMEOUT_MAX) 
except TimeoutError: 
    print("Se ha superado el tiempo de espera máximo") 





"""El módulo threading en Python incluye algunas constantes útiles para manejar y trabajar con hilos y sincronización. """

#1. threading.BARRIER_DEFAULT. Es el valor por defecto para el número de hilos en un Barrier cuando no se especifica uno.
print(threading.BARRIER_DEFAULT) # Muestra el valor por defecto para un Barrier 

#2. threading.Event. Aunque Event es una clase, no es una constante como tal, pero se usa de forma frecuente para manejar eventos de sincronización entre hilos.

#3. threading.MAX_THREADS (Nota: no es una constante oficial en el módulo, pero algunas implementaciones o configuraciones pueden definir el límite de hilos)
#Aunque no está definido como una constante en el módulo threading estándar, es común encontrarse con configuraciones que limitan el número de hilos en la ejecución, que puede ser considerado como el máximo número de hilos que se pueden ejecutar simultáneamente.

#4. threading.TIMEOUT_MAX. Esta constante es utilizada para indicar el tiempo máximo que un hilo puede esperar en operaciones de bloqueo (como en acquire() de un Lock, Semaphore, etc.). Si el tiempo se supera, puede lanzar una excepción TimeoutError.
print(threading.TIMEOUT_MAX) # Muestra el valor del tiempo de espera máximo 




"""El módulo threading en Python define algunas excepciones relacionadas con el manejo de hilos y sincronización"""

#1. threading.ThreadError. Es la excepción base para errores específicos de los hilos. Si ocurre un error relacionado con la manipulación de hilos, esta excepción puede ser levantada.
try: # Código que causa un error relacionado con hilos 
    raise threading.ThreadError("Error en el hilo") 
except threading.ThreadError as e: 
    print(f"Error de hilo: {e}") 

#2. threading.TimeoutError. Es una excepción específica que se lanza cuando se supera el tiempo de espera (timeout) en operaciones que involucran espera de un bloqueo, como acquire() en un Lock, Semaphore, etc.
lock = threading.Lock() 
try: # Intentar adquirir el lock con un timeout 
    lock.acquire(timeout=1) # Supongamos que se supera el tiempo de espera 
except threading.TimeoutError: 
    print("Tiempo de espera excedido al intentar adquirir el lock") 

#3. threading._MainThread. No es una excepción que se levante de forma habitual en código de usuario, pero se refiere al hilo principal en Python. Sin embargo, esta clase no es comúnmente usada de forma explícita por el usuario.



"""El módulo threading en Python no tiene submódulos en el sentido tradicional de un módulo separado dentro del paquete threading"""
#1. threading._thread. Este es un submódulo interno que proporciona las funciones básicas para trabajar con hilos, pero no está diseñado para usarse directamente en código de usuario. En lugar de eso, se utilizan las clases y funciones de alto nivel proporcionadas por threading (como Thread, Lock, etc.). Generalmente no se utiliza directamente en el código, ya que está destinado a la implementación interna de threading.
#2. threading._dummy_thread


"""Este es un submódulo que proporciona una versión simplificada de threading para entornos donde el soporte de hilos no está disponible. 
Por ejemplo, cuando se ejecuta Python en un entorno que no admite hilos nativos (como algunas plataformas de pruebas o entornos restringidos). 
Generalmente no se usa directamente en el código, ya que es para situaciones especiales."""
