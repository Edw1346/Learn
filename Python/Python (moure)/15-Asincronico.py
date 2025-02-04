"""Python asíncrono """
"""Eventos y Bucle de Eventos: El corazón del sistema asíncrono en Python es el bucle de eventos. Este es responsable de gestionar las tareas asíncronas y sus resultados. Cuando un evento (como una operación I/O) se completa, el bucle de eventos reanuda las tareas pendientes.

Coroutines: Una coroutine (o corrutina) es una función especial en Python que puede ser pausada y reanudada. Las coroutines se definen con async def y se ejecutan con await. Estas funciones pueden ser suspendidas en medio de su ejecución, permitiendo que el control se ceda a otras tareas mientras esperan resultados.

asyncio: asyncio es el módulo estándar para escribir programas asíncronos en Python. Este módulo proporciona funciones y clases para trabajar con coroutines, gestionar el bucle de eventos y manejar tareas asíncronas."""

"""Sintaxis Asíncrona"""

"""3.1 Definir Coroutines con async def
Las funciones asíncronas se definen usando async def. Esto marca a la función como una "coroutine", lo que significa que puede ser suspendida y continuada más tarde. Ejemplo:"""
import asyncio 
# Corutina simple async
def saludar(): 
    print("Hola") 
    await asyncio.sleep(1) 
# Simulamos una operación asíncrona 
    print("Mundo") # Ejecutando la corutina
    asyncio.run(saludar()) 
#En este ejemplo, la función saludar es asíncrona, y await asyncio.sleep(1) simula una operación que puede tomar tiempo (como una solicitud de red), permitiendo que otras tareas se ejecuten mientras tanto.

"""3.2 await
El await se utiliza dentro de las coroutines para indicar que el flujo debe esperar a que una operación asíncrona termine antes de continuar. Es importante entender que await solo se puede usar dentro de coroutines. Ejemplo:"""
import asyncio 
# Corutina con espera async 
def tarea_larga(): 
    print("Iniciando tarea...") 
    await asyncio.sleep(2) 
    # Espera 2 segundos sin bloquear el hilo principal 
    print("Tarea completada") 
    # Ejecutando la corutina 
    asyncio.run(tarea_larga()) 

"""3.3 asyncio.run()
La función asyncio.run() se utiliza para ejecutar una coroutine. Es una forma de iniciar el bucle de eventos y ejecutar tareas asíncronas de manera eficiente. Ejemplo:"""
import asyncio 
async def main():
    print("Comienza") 
    await asyncio.sleep(1)
    print("Fin") 
# Ejecutando el bucle de eventos y coroutines 
    asyncio.run(main()) 

"""Conceptos Avanzados"""

"""4.1 Tareas y Futuro (asyncio.create_task())
En lugar de usar await directamente, puedes crear tareas explícitas usando asyncio.create_task(). Esto te permite controlar las tareas concurrentes y gestionarlas por separado. Ejemplo:"""
import asyncio 
async def tarea_1(): 
    await asyncio.sleep(1) 
    print("Tarea 1 completada")
    async def tarea_2():
        await asyncio.sleep(2)
        print("Tarea 2 completada")
    async def main():
    # Crear y ejecutar las tareas
        tarea1 = asyncio.create_task(tarea_1())
        tarea2 = asyncio.create_task(tarea_2()) 
# Esperar que todas las tareas terminen await tarea1 await tarea2 
# Ejecutar el bucle de eventos 
    asyncio.run(main()) 

"""4.2 Ejecutar varias tareas concurrentemente (asyncio.gather())
asyncio.gather() permite ejecutar múltiples coroutines de manera concurrente y esperar a que todas terminen antes de continuar. Es útil cuando deseas ejecutar varias tareas a la vez y esperar los resultados. Ejemplo:"""
import asyncio 
async def tarea_1():
    await asyncio.sleep(1) 
    print("Tarea 1 completada") 
    async def tarea_2(): 
        await asyncio.sleep(2) 
        print("Tarea 2 completada") 
    async def main(): 
# Ejecuta varias tareas a la vez await
        asyncio.gather(tarea_1(), tarea_2())
# Ejecutar el bucle de eventos 
    asyncio.run(main()) 

"""4.3 Manejo de Excepciones en Asíncrono
Cuando trabajas con código asíncrono, también puedes manejar excepciones dentro de coroutines. Es importante asegurarse de que las excepciones en las coroutines sean manejadas adecuadamente, especialmente si estás usando asyncio.gather(). Ejemplo:"""
import asyncio 
async def tarea_exitosa(): 
    await asyncio.sleep(1)
    print("Tarea exitosa") 
    async def tarea_fallida():
        await asyncio.sleep(2) 
        raise Exception("Error en la tarea") 
    async def main(): 
        try: 
            await asyncio.gather(tarea_exitosa(), tarea_fallida()) 
        except Exception as e: 
            print(f"Error: {e}")
    # Ejecutar el bucle de eventos 
    asyncio.run(main()) 

"""Buenas Prácticas y Técnicas con Python Asíncrono"""
"""No bloquees el hilo principal: Utiliza asyncio para manejar tareas que dependen de I/O (como consultas a bases de datos, solicitudes HTTP, etc.) sin bloquear el hilo principal de la aplicación. Esto es esencial en aplicaciones web o en programas que necesiten responder rápidamente a eventos.

Divide el código en tareas pequeñas: Mantén las coroutines pequeñas y manejables. Esto facilitará la depuración y mejorará la eficiencia del código.

Gestiona excepciones adecuadamente: Siempre maneja las excepciones en las coroutines, especialmente cuando usas asyncio.gather(), ya que si una tarea falla, todas las demás tareas pueden verse afectadas.

Usa asyncio.create_task() para tareas concurrentes: Si tienes múltiples tareas que deben ejecutarse concurrentemente, usa asyncio.create_task() para crear y gestionar esas tareas, y luego espera que se completen con await.

Evita usar time.sleep() en código asíncrono: En lugar de usar time.sleep(), que bloquea el hilo de ejecución, usa await asyncio.sleep() para permitir que el hilo principal siga procesando otras tareas mientras espera.

Usa asyncio.gather() para gestionar múltiples tareas: Si necesitas ejecutar varias tareas concurrentemente y esperar que todas terminen, usa asyncio.gather() para agruparlas y esperarlas todas a la vez.

Optimiza las operaciones I/O: Python asíncrono es ideal para mejorar el rendimiento en tareas de I/O (como interactuar con APIs, realizar consultas a bases de datos, o acceder a archivos), ya que puedes manejar múltiples operaciones simultáneamente sin bloquear el flujo del programa."""



"""Módulo de asyncio"""

"""Futuro (Future): Un Future es un objeto que representa el resultado de una operación que no ha terminado aún. A veces se usa para representar una tarea asíncrona en ejecución. En asyncio, las tareas devuelven un Future, que se resuelve cuando la operación asíncrona ha finalizado.

Tareas (Task): Una Task es una subclase de Future que se utiliza para ejecutar coroutines. Es la forma más común de ejecutar una coroutine en asyncio de forma concurrente. Las tareas son gestionadas por el bucle de eventos.

Funciones Principales del Módulo asyncio

asyncio.run(): La función asyncio.run() es la forma más sencilla de ejecutar un programa asíncrono. Se utiliza para ejecutar una coroutine y gestionar el bucle de eventos de forma automática. Ejemplo:"""
import asyncio 
async def hola_mundo():
    print("Hola")
    await asyncio.sleep(1) 
# Simula una operación I/O asíncrona
    print("Mundo") 
    asyncio.run(hola_mundo()) 
# Ejecuta la coroutine 

"""asyncio.create_task(): asyncio.create_task() se utiliza para crear una tarea a partir de una coroutine. Esta función devuelve un objeto Task, que se puede usar para gestionar la ejecución de una coroutine de manera concurrente. La tarea se ejecutará cuando el bucle de eventos esté listo. Ejemplo:"""
import asyncio 
async def tarea_1(): 
    await asyncio.sleep(1)
    print("Tarea 1 completada") 
    async def tarea_2(): 
        await asyncio.sleep(2) 
        print("Tarea 2 completada")
    async def main(): 
    # Crea tareas y ejecuta en paralelo 
        tarea1 = asyncio.create_task(tarea_1())
        tarea2 = asyncio.create_task(tarea_2())
        await tarea1
        await tarea2
    asyncio.run(main()) 

"""asyncio.gather(): asyncio.gather() es una función que se utiliza para ejecutar varias coroutines de manera concurrente y esperar a que todas terminen. Se pasa una lista de coroutines (o tareas) y gather se encargará de esperar todas las tareas simultáneamente. Ejemplo:"""
import asyncio 
async def tarea_1():
    await asyncio.sleep(1)
    print("Tarea 1 completada") 
    async def tarea_2(): 
        await asyncio.sleep(2) 
        print("Tarea 2 completada")
    async def main():
        await asyncio.gather(tarea_1(), tarea_2()) 
# Ejecutar ambas tareas en paralelo 
    asyncio.run(main()) 

"""asyncio.sleep(): asyncio.sleep() es una función que simula una espera asíncrona, lo que significa que no bloquea el hilo mientras espera. A diferencia de time.sleep(), que bloquea el hilo, asyncio.sleep() cede el control al bucle de eventos. Ejemplo:"""
import asyncio 
async def espera(): 
    print("Empezando espera")
    await asyncio.sleep(2) # No bloquea el hilo 
    print("Espera terminada")
    asyncio.run(espera()) 

"""asyncio.Future(): Future() es un objeto que representa un valor que aún no está disponible. Un Future puede estar en uno 

de tres estados: pendiente, resuelto o cancelado. asyncio usa Future para representar el estado de las tareas asíncronas. Ejemplo:"""
import asyncio 
async def ejecutar_future(): 
    futuro = asyncio.Future() 
    await asyncio.sleep(2) 
    futuro.set_result("Resultado de la operación")
 # Completa el futuro
    print(f"El resultado es: {futuro.result()}") 
    asyncio.run(ejecutar_future()) 

"""Flujo de Control y Ejecución

Iniciar el Bucle de Eventos: asyncio.run() es la forma principal de ejecutar una coroutine. Internamente, esta función crea un nuevo bucle de eventos, ejecuta la coroutine proporcionada y luego cierra el bucle al final.

Tareas Concurrentes: Las coroutines se ejecutan de forma concurrente, lo que significa que pueden estar esperando operaciones de I/O sin bloquear el resto del código. Por ejemplo, si una tarea está esperando una respuesta de una red, otras tareas pueden seguir ejecutándose mientras tanto.

Manejo de Excepciones en Tareas Asíncronas: Si una coroutine genera una excepción, puedes capturarlas de manera normal con bloques try/except. Si usas asyncio.gather(), las excepciones se propagarán a la función que espera los resultados. Ejemplo:"""
import asyncio
async def tarea_1():
    await asyncio.sleep(1) 
    raise ValueError("Algo salió mal") 
    async def tarea_2(): 
        await asyncio.sleep(2) 
        print("Tarea 2 completada") 
    async def main(): 
        try:
            await asyncio.gather(tarea_1(), tarea_2())
        except Exception as e: 
            print(f"Error: {e}") 
        asyncio.run(main()) 

"""Ciclo de Vida del Bucle de Eventos: El bucle de eventos de asyncio se ejecuta mientras haya tareas pendientes. Una vez que todas las tareas han sido completadas o canceladas, el bucle de eventos se detiene."""

"""Buenas Prácticas y Técnicas en asyncio"""

"""Evitar time.sleep() en código asíncrono: Usa asyncio.sleep() en lugar de time.sleep() para evitar que tu código bloquee el hilo y pierda la ventaja de la ejecución concurrente.

No crear coroutines sin esperar a su ejecución: Es importante usar await o asyncio.create_task() para ejecutar las coroutines. Si creas coroutines sin ejecutar await, se quedarán pendientes y no se ejecutarán.

Gestiona excepciones en tareas concurrentes: Usa bloques try/except para manejar excepciones dentro de las coroutines. Cuando uses asyncio.gather(), también puedes capturar excepciones de todas las tareas concurrentes en un solo bloque try/except.

Divide el código en tareas pequeñas: Es una buena práctica mantener las coroutines pequeñas y manejables para evitar que el código se vuelva difícil de depurar o entender.

Usa el bucle de eventos con cuidado: Si usas múltiples bucles de eventos o administras tareas manualmente, ten cuidado de no ejecutar más de un bucle de eventos a la vez. La mayoría de las aplicaciones no necesitan múltiples bucles de eventos."""