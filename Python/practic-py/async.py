#El módulo asyncio para manejar programación asíncrona y concurrencia. Te permite escribir programas que pueden ejecutar múltiples tareas de manera concurrente sin bloquear el flujo de ejecución. 

#Corutinas: Funciones especiales que se pueden pausar y reanudar usando async y await.
#Bucle de eventos (Event Loop): Es el encargado de gestionar las tareas asíncronas.
#Tareas (Tasks): Son las unidades de trabajo que el bucle de eventos ejecuta.

import asyncio

#1. asyncio.run(main(), debug=False). Ejecuta una corutina, estableciendo el bucle de eventos y gestionando su cierre. Esta es la forma más común de iniciar programas asyncio.
async def tar(): print("Tarea terminada")
asyncio.run(tar())

##2. asyncio.create_task(coro, name=None). Crea una tarea asíncrona a partir de una corutina y la ejecuta en el bucle de eventos. Devuelve un objeto Task.
async def tarea(): print("Tarea ejecutada") 

async def main(): 
    tarea1 = asyncio.create_task(tarea()) 
    await tarea1
asyncio.run(main()) 

#3. asyncio.sleep(delay, result=None). Suspende la ejecución de la corutina actual durante el número de segundos especificado en delay. Es útil para simular operaciones de I/O.
async def tarea(): 
    print("Esperando...") 
    await asyncio.sleep(2) 
    print("Ya pasó el tiempo") 
asyncio.run(tarea()) 

#4. asyncio.gather(*tasks, return_exceptions=False). Ejecuta múltiples corutinas simultáneamente y espera a que todas terminen. Devuelve una lista de resultados.
async def tarea_1(): 
    await asyncio.sleep(1) 
    return "Tarea 1 terminada" 
async def tarea_2(): 
    await asyncio.sleep(2) 
    return "Tarea 2 terminada"

async def main(): 
    resultados = await asyncio.gather(tarea_1(), tarea_2())  #Se emvia hasta que se complete todas las tareas
    print(resultados) 
asyncio.run(main()) 

#5. asyncio.wait(futures, *, timeout=None, return_when=ALL_COMPLETED). Espera hasta que se completen algunas o todas las tareas dadas en futures. Puedes especificar un tiempo de espera.
async def tarea(id): 
    await asyncio.sleep(id) 
    return f"Tarea {id} terminada"

async def main(): 
    tareas = [asyncio.gather(tarea(1), tarea(2), tarea(3))]  #La forma en como quiere que se complete las tareas
    done, pending = await asyncio.wait(tareas) #Permite tener control de las tareas que se completan
    for t in done:
        print(t.result()) 
asyncio.run(main()) 

#6. asyncio.as_completed(futures, *, timeout=None). Devuelve un generador que produce los resultados de las tareas conforme se completan.
async def tarea(id): 
    await asyncio.sleep(id) 
    return f"Tarea {id} terminada" 

async def main(): 
    tareas = [tarea(5), tarea(3), tarea(2)] 
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
#loop = asyncio.get_event_loop()
#print(loop) 

#9. asyncio.set_event_loop(loop). Establece el bucle de eventos actual.
loop = asyncio.new_event_loop() 
asyncio.set_event_loop(loop) 
print(loop) 

#10. asyncio.Event(). Devuelve un objeto de evento que permite a las tareas sincronizarse entre sí.
async def tarea(event): #La funcion que espera pausar y reanudar, se manda el objeto event para controlarlo desde adentro
    print("Esperando el evento...") 
    await event.wait()      #Este wait hace una pausa
    print("Evento recibido!") 

async def main(): 
    event = asyncio.Event()  #EL set reauda la pausa del wait
asyncio.run(main()) 

#. asyncio.Future(). Representa un resultado que aún no está disponible. Las corutinas pueden esperar en un Future.
async def tarea(futuro): #Se envia el objeto furute para hacerlo desde adentro
    await asyncio.sleep(2)  
    await futuro #Se bloequea, lo pausa
    print("TErminado")

async def tare(futuro):
    futuro.set_result("Resultado listo")  #El resultado que se envia del future

async def main(): 
    futuro = asyncio.Future() 
    await asyncio.gather(tarea(futuro), tare(futuro)) #Primero se envia el que pausa y d
    print(futuro.result()) 
asyncio.run(main()) 

#asyncio.Queue(maxsize=0)  Proporciona una cola asincrónica para la comunicación entre corutinas.
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



# asyncio.Loop (Event Loop). El bucle de eventos maneja la ejecución de tareas asíncronas. Aunque es más común usar asyncio.run(), puedes acceder al bucle de eventos directamente con get_event_loop().
async def tarea(): 
    print("Tarea ejecutada")
    loop = asyncio.get_event_loop() # Obtener el bucle de eventos
    loop.run_until_complete(tarea()) # Ejecutar la tarea hasta su finalización 

# asyncio.Semaphore. Una clase de sincronización que limita el número de tareas que pueden ejecutarse de manera concurrente. Es útil para controlar el acceso a recursos compartidos.
async def tarea(sem): 
    async with sem: # Asegura que solo un número limitado de tareas accedan al recurso 
        await asyncio.sleep(1) 
        print("Tarea ejecutada") 

async def main(): 
    sem = asyncio.Semaphore(2) # Limitar a 2 tareas concurrentes 
    await asyncio.gather(tarea(sem), tarea(sem), tarea(sem)) 
asyncio.run(main()) 

# asyncio.Lock. Un bloqueo que puede ser utilizado para garantizar que solo una corutina pueda acceder a un recurso en un momento dado, previniendo condiciones de carrera.
async def tarea(lock): 
    async with lock: 
        await asyncio.sleep(1) 
        print("Tarea ejecutada") 

async def main(): 
    lock = asyncio.Lock() # Crear un bloqueo 
    await asyncio.gather(tarea(lock), tarea(lock)) 
asyncio.run(main()) 

#asyncio.Condition. Una clase de sincronización que permite que las corutinas esperen hasta que se cumpla una condición.
async def tarea(condicion): 
    print("Esperando a que se cumpla la condición...") 
    async with condicion: 
        await condicion.wait() # Espera hasta que se active la condición 
    print("Condición cumplida") 

async def main(): 
    condicion = asyncio.Condition() # Crear una condición 
    await asyncio.gather(tarea(condicion), asyncio.sleep(2), condicion.notify()) 
asyncio.run(main()) 

#asyncio.PriorityQueue. Una variante de Queue donde los elementos tienen una prioridad y se recuperan en el orden de menor a mayor prioridad.
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

"""Task: Representa una tarea asíncrona.
Future: Representa un resultado eventual de una operación asíncrona.
Event: Permite sincronizar tareas con un evento.
Queue: Una cola asincrónica para la comunicación entre tareas.
Semaphore: Limita la concurrencia de tareas.
Lock: Un mecanismo para evitar el acceso concurrente a un recurso.
Condition: Permite a las tareas esperar hasta que se cumpla una condición.
PriorityQueue: Una cola con prioridades."""




"""Subcomponentes (submódulos) de asyncio:


1. asyncio.subprocess. Este submódulo permite la creación y gestión de procesos en segundo plano (subprocesos) de manera asíncrona. Proporciona funciones para ejecutar comandos del sistema y manejar su entrada/salida de manera asíncrona.

2. asyncio.locks. Este submódulo proporciona herramientas para trabajar con primitivas de sincronización como bloqueos (locks), eventos, semáforos y condiciones de manera asíncrona, lo que es útil para proteger recursos compartidos en programas concurrentes.

3. asyncio.sslproto. Este submódulo proporciona herramientas para trabajar con protocolos de red seguros (SSL/TLS) de manera asíncrona. Es útil cuando se combinan operaciones asíncronas con conexiones de red seguras. Este submódulo generalmente se usa detrás de escenas y no se utiliza tanto directamente en el código de usuario común. Uso principal para trabajar con asyncio y conexiones SSL.

7. asyncio.streams. Este submódulo proporciona soporte para streams asíncronos (lectura y escritura de datos) de sockets y otras conexiones de red de manera no bloqueante.

8. asyncio.selector_events. Este submódulo es usado internamente en asyncio y proporciona una implementación basada en el selector de eventos para manejar las operaciones de entrada/salida de archivos y redes de manera eficiente y no bloqueante.

9. asyncio.protocols. Este submódulo se utiliza para implementar protocolos de comunicación de bajo nivel sobre sockets y otros transportes. Se emplea cuando se necesita un control más detallado sobre cómo se manejan los datos de entrada y salida en aplicaciones asíncronas."""


