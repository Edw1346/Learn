import asyncio

"""El módulo asyncio en Python se usa para manejar programación asíncrona y concurrencia. Te permite escribir programas que 
pueden ejecutar múltiples tareas de manera concurrente sin bloquear el flujo de ejecución. Esto es útil cuando necesitas 
manejar muchas operaciones I/O (como leer archivos o hacer solicitudes HTTP) sin que el programa se quede esperando a que 
se complete una tarea."""
#Corutinas: Funciones especiales que se pueden pausar y reanudar usando async y await.
#Bucle de eventos (Event Loop): Es el encargado de gestionar las tareas asíncronas.
#¿Por qué usar asyncio?
#Permite ejecutar muchas tareas concurrentemente sin bloqueos.
#Es útil para aplicaciones de red, I/O o donde muchas tareas pequeñas deben ejecutarse al mismo tiempo.



"""El módulo asyncio proporciona varias funciones para manejar programación asíncrona en Python."""

#1. asyncio.run(main(), debug=False). Ejecuta una corutina, estableciendo el bucle de eventos y gestionando su cierre. Esta es la forma más común de iniciar programas asyncio.
async def main(): 
    print("Hola, asyncio!") 
    asyncio.run(main()) 

#2. asyncio.create_task(coro, name=None). Crea una tarea asíncrona a partir de una corutina y la ejecuta en el bucle de eventos. Devuelve un objeto Task.
async def tarea():
    print("Tarea ejecutada") 

async def main(): .
    tarea1 = asyncio.create_task(tarea()) 
    await tarea1 
    asyncio.run(main()) 

#3. asyncio.sleep(delay, result=None). Suspende la ejecución de la corutina actual durante el número de segundos especificado en delay. Es útil para simular operaciones de I/O.
async def tarea(): 
    print("Esperando...") 
    await asyncio.sleep(2) 
    print("Ya pasó el tiempo") 
    asyncio.run(tarea()) 

4. asyncio.gather(*tasks, return_exceptions=False). Ejecuta múltiples corutinas simultáneamente y espera a que todas terminen. Devuelve una lista de resultados.
async def tarea_1(): 
    await asyncio.sleep(1) 
    return "Tarea 1 terminada" 

async def tarea_2(): 
    await asyncio.sleep(2) 
    return "Tarea 2 terminada"

async def main(): 
    resultados = await asyncio.gather(tarea_1(), tarea_2()) 
    print(resultados) 
    asyncio.run(main()) 

#5. asyncio.wait(futures, *, timeout=None, return_when=ALL_COMPLETED). Espera hasta que se completen algunas o todas las tareas dadas en futures. Puedes especificar un tiempo de espera.
async def tarea(id): 
    await asyncio.sleep(id) 
    return f"Tarea {id} terminada"

async def main(): 
    tareas = [tarea(1), tarea(2), tarea(3)] 
    done, pending = await asyncio.wait(tareas) 
    for t in done:
        print(t.result()) 
        asyncio.run(main()) 

#6. asyncio.as_completed(futures, *, timeout=None). Devuelve un generador que produce los resultados de las tareas conforme se completan.
async def tarea(id): 
    await asyncio.sleep(id) 
    return f"Tarea {id} terminada" 

async def main(): 
    tareas = [tarea(1), tarea(2), tarea(3)] 
    for resultado in asyncio.as_completed(tareas): 
        print(await resultado) 
        asyncio.run(main()) 

#7. asyncio.shield(aw, *, loop=None). Evita que una tarea sea cancelada. Puede usarse para proteger tareas que no deberían ser interrumpidas.
async def tarea(): 
    await asyncio.sleep(2) 
    return "Tarea terminada" 

async def main(): 
    protected_task = asyncio.shield(tarea())
    print(await protected_task) 
    asyncio.run(main()) 

#8. asyncio.get_event_loop(). Devuelve el bucle de eventos actual. Obsoleto en versiones recientes de Python, se recomienda usar asyncio.run().
loop = asyncio.get_event_loop()
print(loop) 

#9. asyncio.set_event_loop(loop). Establece el bucle de eventos actual.
loop = asyncio.new_event_loop() 
asyncio.set_event_loop(loop) 
print(loop) 

#10. asyncio.Event(). Devuelve un objeto de evento que permite a las tareas sincronizarse entre sí.
async def tarea(event): 
    print("Esperando el evento...") 
    await event.wait() 
    print("Evento recibido!") 

async def main(): 
    event = asyncio.Event() 
    await asyncio.gather(tarea(event), asyncio.sleep(1), event.set()) 
    asyncio.run(main()) 

#11. asyncio.Future(). Representa un resultado que aún no está disponible. Las corutinas pueden esperar en un Future.
async def tarea(futuro): 
    await asyncio.sleep(2) 
    futuro.set_result("Resultado listo")

async def main(): 
    futuro = asyncio.Future() 
    await asyncio.gather(tarea(futuro))
    print(futuro.result()) 
    asyncio.run(main()) 

#12. asyncio.Queue(maxsize=0). Proporciona una cola asincrónica para la comunicación entre corutinas.
async def productor(queue): 
    await queue.put("Elemento 1") 
    await queue.put("Elemento 2") 

async def consumidor(queue):
    item1 = await queue.get()
    print(item1)

async def main(): 
    queue = asyncio.Queue() 
    await asyncio.gather(productor(queue), consumidor(queue)) 
    asyncio.run(main()) 



"""El módulo asyncio proporciona varias clases importantes que se utilizan para trabajar con programación asíncrona y manejo de tareas concurrentes. """

#1. asyncio.Task. Esta clase representa una tarea asíncrona que se ejecuta en el bucle de eventos. Las tareas son corutinas envueltas que se ejecutan de manera concurrente.
async def tarea():
    print("Tarea ejecutada") # Crear y ejecutar la tarea 
async def main(): 
    task = asyncio.create_task(tarea()) # Crea una tarea asíncrona 
    await task # Espera a que la tarea termine
    asyncio.run(main()) 

#2. asyncio.Future. Representa un resultado eventual de una operación asíncrona. Las corutinas pueden esperar a que el Future se complete.
async def tarea(futuro): 
    await asyncio.sleep(2) 
    futuro.set_result("Tarea completada") 

async def main(): 
    futuro = asyncio.Future() # Crear un objeto Future 
    await asyncio.gather(tarea(futuro)) 
    print(futuro.result()) # Imprime el resultado cuando la tarea se completa 
    asyncio.run(main()) 

#3. asyncio.Event. Representa un evento de sincronización en el que una o más corutinas pueden esperar hasta que el evento se establezca. Es útil para coordinar tareas.
import asyncio 
async def tarea(evento):
    print("Esperando el evento...")     
    await evento.wait() # Espera hasta que el evento sea activado 
    print("Evento recibido") 

async def main(): 
    evento = asyncio.Event() # Crear un evento 
    await asyncio.gather(tarea(evento), asyncio.sleep(2), evento.set()) # Activar el evento 
    asyncio.run(main()) 

4. asyncio.Queue. Una cola asincrónica que se puede usar para pasar datos entre corutinas. Es útil para la comunicación entre productores y consumidores.
async def productor(queue): 
    await queue.put("Elemento 1") 
    await queue.put("Elemento 2") 

async def consumidor(queue):
    item1 = await queue.get() 
    print(item1) 

async def main(): 
    queue = asyncio.Queue() 
    await asyncio.gather(productor(queue), consumidor(queue)) 
    asyncio.run(main()) 

5. asyncio.Loop (Event Loop). El bucle de eventos maneja la ejecución de tareas asíncronas. Aunque es más común usar asyncio.run(), puedes acceder al bucle de eventos directamente con get_event_loop()import asyncio
async def tarea(): 
    print("Tarea ejecutada")
    loop = asyncio.get_event_loop() # Obtener el bucle de eventos
    loop.run_until_complete(tarea()) # Ejecutar la tarea hasta su finalización 

#6. asyncio.Semaphore. Una clase de sincronización que limita el número de tareas que pueden ejecutarse de manera concurrente. Es útil para controlar el acceso a recursos compartidos.
async def tarea(sem): 
    async with sem: # Asegura que solo un número limitado de tareas accedan al recurso 
        await asyncio.sleep(1) 
        print("Tarea ejecutada") 

async def main(): 
    sem = asyncio.Semaphore(2) # Limitar a 2 tareas concurrentes 
    await asyncio.gather(tarea(sem), tarea(sem), tarea(sem)) 
    asyncio.run(main()) 

#7. asyncio.Lock. Un bloqueo que puede ser utilizado para garantizar que solo una corutina pueda acceder a un recurso en un momento dado, previniendo condiciones de carrera.
async def tarea(lock): 
    async with lock: 
        await asyncio.sleep(1) 
        print("Tarea ejecutada") 

async def main(): 
    lock = asyncio.Lock() # Crear un bloqueo 
    await asyncio.gather(tarea(lock), tarea(lock)) 
    asyncio.run(main()) 

#8. asyncio.Condition. Una clase de sincronización que permite que las corutinas esperen hasta que se cumpla una condición.
async def tarea(condicion): 
    print("Esperando a que se cumpla la condición...") 

async with condicion: 
    await condicion.wait() # Espera hasta que se active la condición 
        print("Condición cumplida") 

async def main(): 
    condicion = asyncio.Condition() # Crear una condición 
    await asyncio.gather(tarea(condicion), asyncio.sleep(2), condicion.notify()) 
    asyncio.run(main()) 

#9. asyncio.PriorityQueue. Una variante de Queue donde los elementos tienen una prioridad y se recuperan en el orden de menor a mayor prioridad.
async def productor(queue): 
    await queue.put((2, "Elemento 2")) 
    await queue.put((1, "Elemento 1"))

async def consumidor(queue): 
    while not queue.empty(): 
        prioridad, item = await queue.get()
        print(f"Procesando {item} con prioridad {prioridad}")

async def main():
    queue = asyncio.PriorityQueue() 
    await asyncio.gather(productor(queue), consumidor(queue)) 
    asyncio.run(main()) 
#Task: Representa una tarea asíncrona.
#Future: Representa un resultado eventual de una operación asíncrona.
#Event: Permite sincronizar tareas con un evento.
#Queue: Una cola asincrónica para la comunicación entre tareas.
#Semaphore: Limita la concurrencia de tareas.
#Lock: Un mecanismo para evitar el acceso concurrente a un recurso.
#Condition: Permite a las tareas esperar hasta que se cumpla una condición.
#PriorityQueue: Una cola con prioridades.





"""El módulo asyncio no tiene "variables" pero existen algunos valores y configuraciones importantes en asyncio que podríamos considerar similares a variables, 
como las configuraciones globales, los parámetros"""

#1. asyncio.all_tasks(loop=None). Devuelve un conjunto de todas las tareas activas para el bucle de eventos proporcionado (loop). Si no se pasa un bucle de eventos, usa el bucle de eventos actual.
async def tarea():
    await asyncio.sleep(1) 

async def main(): 
    t = asyncio.create_task(tarea()) 
    await asyncio.sleep(0.5) 
    tasks = asyncio.all_tasks() 
    print(tasks) # Muestra las tareas activas 
    asyncio.run(main()) 

#2. asyncio.current_task(loop=None). Devuelve la tarea actualmente en ejecución. Si no se pasa un bucle de eventos, usa el bucle de eventos actual.
async def tarea(): 
    print(f"Tarea actual: {asyncio.current_task()}") 

async def main():
    await asyncio.create_task(tarea()) 
    asyncio.run(main()) 

#3. asyncio.get_event_loop(). Devuelve el bucle de eventos actual. Si no existe, crea uno nuevo. Obsoleto en versiones recientes, se recomienda usar asyncio.run().
loop = asyncio.get_event_loop() # Obtiene el bucle de eventos 
print(loop) 

#4. asyncio.run(). Esta función ejecuta una corutina, crea un bucle de eventos, lo ejecuta y cierra el bucle una vez que la corutina termina. Es la forma recomendada de ejecutar programas asyncio.
async def tarea():
    print("Ejecutando tarea") 
    asyncio.run(tarea()) 

#5. asyncio.Task.all_tasks(loop=None). Método de la clase Task que devuelve un conjunto de todas las tareas activas en el bucle de eventos.
async def tarea(): 
    await asyncio.sleep(1)

async def main():
    t = asyncio.create_task(tarea()) 
    await asyncio.sleep(0.5)
    tasks = asyncio.Task.all_tasks() 
    print(tasks) # Muestra las tareas activas asyncio.run(main()) 

#6. asyncio.get_event_loop_policy(). Devuelve la política actual para obtener el bucle de eventos. La política es responsable de decidir qué implementación de bucle de eventos se debe usar (esto puede cambiar dependiendo del sistema operativo).
policy = asyncio.get_event_loop_policy() 
print(policy) 

#7. asyncio.set_event_loop_policy(policy). Establece la política para obtener el bucle de eventos. Esto te permite controlar qué tipo de bucle se usará en el programa.
policy = asyncio.get_event_loop_policy() 
asyncio.set_event_loop_policy(policy) 

#8. asyncio.ensure_future(coro, loop=None). Convierte una corutina en una tarea. Esta función es una forma más flexible de programar tareas asíncronas en el bucle de eventos.
async def tarea(): 
    await asyncio.sleep(1) 
    print("Tarea completada") 

async def main(): 
    asyncio.ensure_future(tarea()) # Asegura que la tarea se ejecute 
    await asyncio.sleep(1) 
    asyncio.run(main()) 

#9. asyncio.CancelledError. Es una excepción que se lanza cuando una tarea asíncrona es cancelada.
async def tarea(): 
    await asyncio.sleep(2) 
    print("Tarea completada") 

async def main():
    t = asyncio.create_task(tarea())
    t.cancel() # Cancela la tarea
    try: 
        await t 
    except asyncio.CancelledError:
        print("La tarea fue cancelada") 
    asyncio.run(main()) 



"""Ahora las constantes del modulo asyncio"""

#1. asyncio.ALL_COMPLETED. Esta constante es utilizada con el método asyncio.wait() para esperar a que todas las tareas se completen.
async def tarea(): 
    await asyncio.sleep(1) 

async def main(): 
    tasks = [asyncio.create_task(tarea()) for _ in range(3)] 
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED) 
    print("Todas las tareas están completadas") 
    asyncio.run(main()) 

2. asyncio.FIRST_COMPLETED. Es utilizada con el método asyncio.wait() para esperar a que al menos una tarea se complete.
async def tarea(): 
    await asyncio.sleep(1) 

async def main(): 
    tasks = [asyncio.create_task(tarea()) for _ in range(3)] 
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED) 
    print("Al menos una tarea está completada") asyncio.run(main()) 

3. asyncio.FIRST_EXCEPTION. Se usa con asyncio.wait() para esperar a que la primera tarea que lance una excepción sea completada.
async def tarea(exception=False):
    if exception: 
        raise ValueError("Error en la tarea") 
    await asyncio.sleep(1) 

async def main(): 
    tasks = [asyncio.create_task(tarea()) for _ in range(2)] + [asyncio.create_task(tarea(exception=True))] 
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION) 
    print("Se encontró una excepción") 
    asyncio.run(main()) 

#4. asyncio.CancelledError. Es una constante que representa el tipo de excepción que se lanza cuando una tarea asíncrona es cancelada.
async def tarea(): 
    await asyncio.sleep(2) 
    print("Tarea completada") 

async def main(): 
    task = asyncio.create_task(tarea()) 
    task.cancel() # Cancela la tarea
    try: 
        await task
    except asyncio.CancelledError: 
        print("La tarea fue cancelada") 
        asyncio.run(main()) 

#5. asyncio.DEFAULT. Es un valor predeterminado que se utiliza en la configuración de ciertos métodos, como en asyncio.get_event_loop_policy().
policy = asyncio.get_event_loop_policy() 
print(policy) 

6. asyncio.Event. No es estrictamente una constante, pero asyncio.Event representa un objeto que puede ser utilizado para bloquear o sincronizar tareas. Se puede usar para coordinar actividades entre corutinas.
async def tarea(evento): 
    print("Esperando evento...") 
    await evento.wait()
    print("Evento recibido") 

async def main(): 
    evento = asyncio.Event() 
    await asyncio.gather(tarea(evento), asyncio.sleep(2), evento.set()) 
    asyncio.run(main()) 






"""El módulo asyncio incluye varias excepciones"""

#1. asyncio.CancelledError. Es una excepción que se lanza cuando una tarea asíncrona es cancelada explícitamente. Esto es útil cuando se interrumpe una tarea pendiente.
async def tarea(): 
    await asyncio.sleep(2) 
    print("Tarea completada") 

async def main(): 
    task = asyncio.create_task(tarea()) 
    task.cancel() # Cancela la tarea 
    try: 
        await task 
    except asyncio.CancelledError:
        print("La tarea fue cancelada") asyncio.run(main()) 

#2. asyncio.TimeoutError. Es una excepción que se lanza cuando una operación asíncrona no termina dentro del tiempo especificado. Por ejemplo, si usas asyncio.wait_for() para esperar una tarea con un límite de tiempo, esta excepción será lanzada si el tiempo de espera se excede.
async def tarea():
    await asyncio.sleep(3) 

async def main(): 
    try: 
        await asyncio.wait_for(tarea(), timeout=2) # Espera 2 segundos 
    except asyncio.TimeoutError:
        print("Tiempo de espera excedido") 
        asyncio.run(main()) 

#3. asyncio.InvalidStateError. Se lanza cuando intentas cambiar el estado de una tarea o un objeto Future de manera incorrecta. Por ejemplo, intentar cambiar el estado de una tarea que ya ha sido completada.
async def tarea(): 
    return "Resultado"

async def main(): 
    future = asyncio.Future() 
    await asyncio.gather(future) 
    try:
        future.set_result("Nuevo resultado") # Esto causará un error porque el estado ya está establecido 
    except asyncio.InvalidStateError: 
        print("Intento de modificar un estado inválido") 
        asyncio.run(main()) 

#4. asyncio.QueueEmpty. Es lanzada cuando intentas obtener un elemento de una asyncio.Queue y la cola está vacía. Esta excepción se lanza con el método get() si la cola está vacía y el parámetro block es False.
async def consumidor(queue):
    try:
        item = await queue.get_nowait() # No espera, obtiene el primer elemento disponible
        print(f"Elemento consumido: {item}") 
    except asyncio.QueueEmpty:
        print("La cola está vacía")

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(consumidor(queue)) 
    asyncio.run(main()) 

#5. asyncio.QueueFull. Se lanza cuando intentas añadir un elemento a una asyncio.Queue que ya está llena, si el parámetro block de put() es False.
async def productor(queue): 
    try: 
        await queue.put_nowait("Elemento") # Intenta poner un elemento sin esperar
    except asyncio.QueueFull: 
        print("La cola está llena") 

async def main(): 
    queue = asyncio.Queue(maxsize=1) 
    await asyncio.gather(productor(queue), productor(queue)) 
    asyncio.run(main()) 

#6. asyncio.CancelledError. Es lanzada cuando una tarea es cancelada explícitamente utilizando el método cancel() de una tarea, y se puede capturar para realizar limpieza si es necesario.
async def tarea(): 
    await asyncio.sleep(3) 
        print("Tarea completada")

async def main(): 
    task = asyncio.create_task(tarea()) task.cancel() # Cancela la tarea 
    try:
        await task 
    except asyncio.CancelledError: 
        print("La tarea fue cancelada antes de completarse") 
        asyncio.run(main()) 

#CancelledError: Para manejar la cancelación de tareas.
#TimeoutError: Para manejar los tiempos de espera superados en tareas.
#InvalidStateError: Para controlar cambios de estado incorrectos en tareas o Future.
#QueueEmpty y QueueFull: Para manejar situaciones de lectura o escritura en colas cuando están vacías o llenas.




"""El módulo asyncio no tiene submódulos de forma convencional como algunos otros módulos en Python"""

#Subcomponentes (submódulos) de asyncio:

#1. asyncio.subprocess: Este submódulo permite la creación y gestión de procesos en segundo plano (subprocesos) de manera asíncrona. Proporciona funciones para ejecutar comandos del sistema y manejar su entrada/salida de manera asíncrona.
import asyncio.subprocess
async def ejecutar_comando(): 
    process = await asyncio.subprocess.create_subprocess_exec( 'echo', 'Hola Mundo!', stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE )
    stdout, stderr = await process.communicate() 
    print(stdout.decode()) 
    asyncio.run(ejecutar_comando()) 

#2. asyncio.locks. Este submódulo proporciona herramientas para trabajar con primitivas de sincronización como bloqueos (locks), eventos, semáforos y condiciones de manera asíncrona, lo que es útil para proteger recursos compartidos en programas concurrentes.
import asyncio.locks 
lock = asyncio.locks.Lock() 

async def tarea_con_lock(): 
    async with lock: 
        print("Recurso protegido") 

async def main(): 
    await asyncio.gather(tarea_con_lock(), tarea_con_lock()) 
    asyncio.run(main()) 

#3. asyncio.sslproto. Este submódulo proporciona herramientas para trabajar con protocolos de red seguros (SSL/TLS) de manera asíncrona. Es útil cuando se combinan operaciones asíncronas con conexiones de red seguras. Este submódulo generalmente se usa detrás de escenas y no se utiliza tanto directamente en el código de usuario común. Su uso principal es para trabajar con asyncio y conexiones SSL.

#4. asyncio.streams. Este submódulo proporciona soporte para streams asíncronos (lectura y escritura de datos) de sockets y otras conexiones de red de manera no bloqueante.
import asyncio.streams 
async def main(): 
    reader, writer = await asyncio.streams.open_unix_connection('/tmp/socket') 
    writer.write(b'Hola') 
    await writer.drain() 
    data = await reader.read(100) 
    print(f"Recibido: {data}") 
    asyncio.run(main()) 

#5. asyncio.selector_events. Este submódulo es usado internamente en asyncio y proporciona una implementación basada en el selector de eventos para manejar las operaciones de entrada/salida de archivos y redes de manera eficiente y no bloqueante.

#6. asyncio.protocols. Este submódulo se utiliza para implementar protocolos de comunicación de bajo nivel sobre sockets y otros transportes. Se emplea cuando se necesita un control más detallado sobre cómo se manejan los datos de entrada y salida en aplicaciones asíncronas.


