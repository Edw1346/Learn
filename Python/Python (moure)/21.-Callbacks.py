"""Callbacks 
Son funciones que se pasan como argumento a otras funciones y que se ejecutan en un momento posterior, generalmente cuando ocurre un evento específico o cuando se completa una tarea. Son muy utilizados en escenarios como la programación asíncrona, el manejo de eventos y el diseño de arquitecturas basadas en eventos.

1. Callback Básico en Funciones
Técnica: Usar una función como argumento y llamarla dentro de otra función.

Ejemplo: Callback simple"""
def operacion_suma(a, b, callback): 
    resultado = a + b 
    callback(resultado) 

# Llamamos al callback con el resultado 
def mostrar_resultado(resultado):
    print(f"El resultado de la suma es: {resultado}") 

# Usamos el callback 
operacion_suma(5, 3, mostrar_resultado) 

#En este caso, la función mostrar_resultado se pasa como callback a operacion_suma y se ejecuta cuando la operación de suma se completa.

"""2. Usar Callbacks en Funciones Asíncronas
Los callbacks son fundamentales cuando trabajas con código asíncrono en Python. Puedes usar asyncio o threading para invocar una función cuando una tarea se complete.

Ejemplo: Callback en funciones asíncronas"""
import asyncio 
async def tarea_larga(callback): 
    print("Iniciando tarea larga...") 
    await asyncio.sleep(3) 
    # Simula una tarea asíncrona que tarda 3 segundos 
    print("Tarea completada.") 
    callback("Tarea completada exitosamente.")

def notificar(resultado): 
    print(f"Notificación: {resultado}") 

# Ejecutar la tarea asíncrona con un callback 
asyncio.run(tarea_larga(notificar)) 

#Aquí, el callback notificar se pasa a la tarea asíncrona tarea_larga para ser ejecutado cuando la tarea termine.

"""3. Callbacks con Excepciones
Puedes utilizar callbacks en funciones que manejan excepciones, para invocar una acción específica si ocurre un error.

Ejemplo: Callback con manejo de excepciones"""
def dividir(a, b, callback_error): 
    try: 
        resultado = a / b
        print(f"Resultado de la división: {resultado}")
    except ZeroDivisionError: 
        callback_error("Error: División por cero.") 

def manejar_error(error):
        print(error) # Llamada con error 

dividir(10, 0, manejar_error) 

#En este ejemplo, el callback manejar_error se llama cuando ocurre una excepción de división por cero.

"""4. Callbacks en Bibliotecas de Eventos
Algunas bibliotecas, como Tkinter o Flask, usan callbacks para manejar eventos, como hacer clic en un botón o recibir una solicitud HTTP.

Ejemplo: Callback en un evento de Tkinter"""
import tkinter as tk 
def mostrar_mensaje():
    print("¡Botón presionado!") # Crear la ventana 
    ventana = tk.Tk() 
    ventana.title("Ejemplo de Callback") # Crear un botón y asignar un callback 

boton = tk.Button(ventana, text="Haz clic aquí", command=mostrar_mensaje) 
boton.pack() # Ejecutar la ventana 
ventana.mainloop() 

#En este caso, el callback mostrar_mensaje se ejecuta cuando el usuario hace clic en el botón.

"""5. Callbacks con functools.partial

Si quieres pasar un callback con parámetros adicionales, puedes usar functools.partial para fijar algunos de los argumentos del callback.

Ejemplo: Usar partial con un callback"""
import functools
def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!") # Crear un callback con un saludo fijo 

saludar_maria = functools.partial(saludar, nombre="María", saludo="Buenas tardes") # Llamar al callback 
saludar_maria() # Imprime: Buenas tardes, María! 

#El uso de partial permite crear una versión preconfigurada de la función saludar, donde se fijan ciertos argumentos para su uso posterior.

"""6. Callbacks con el módulo threading
Cuando realizas tareas en hilos (threads), puedes usar callbacks para manejar los resultados de esas tareas cuando terminen.
Ejemplo: Callback con threading"""
import threading 
def tarea_larga(callback): 
    print("Iniciando tarea en el hilo...") # Simulando una tarea de 3 segundos 
    import time
    time.sleep(3) 
    callback("Tarea completada en el hilo.") 

def resultado_en_hilo(resultado): 
    print(f"Resultado recibido: {resultado}") # Crear y empezar un hilo 

hilo = threading.Thread(target=tarea_larga, args=(resultado_en_hilo,)) 
hilo.start() # Continuar con el hilo principal 
print("Esperando a que termine el hilo...")
hilo.join() 

#Aquí, el callback resultado_en_hilo se ejecutará cuando el hilo termine su tarea.

"""7. Callbacks con flask y Rutas

En frameworks web como Flask, los callbacks se utilizan para manejar las respuestas a las rutas HTTP.

Ejemplo: Callback en Flask"""
from flask import Flask
app = Flask(__name__) 

def bienvenida(): 
    return "¡Bienvenido a la página de inicio!" 
@app.route('/') 
def inicio(): 
    return bienvenida() # Llamar al callback 

if __name__ == '__main__': 
    app.run(debug=True) 

#En este ejemplo, la función bienvenida actúa como un callback para la ruta principal de la aplicación web.

"""8. Callbacks en Funciones de Orden Superior
Puedes pasar funciones como parámetros de una función principal, haciendo que la función principal actúe como un wrapper que modifica el comportamiento del callback.

Ejemplo: Función de orden superior con callback"""
def operaciones(a, b, callback):
    resultado = callback(a, b) 
    print(f"Resultado de la operación: {resultado}") 

def suma(x, y): 
    return x + y 

def resta(x, y): 
    return x - y # Usar la función de orden superior con diferentes callbacks 

operaciones(10, 5, suma) # Resultado de la operación: 15 
operaciones(10, 5, resta) # Resultado de la operación: 5 

#En este caso, operaciones actúa como una función de orden superior que acepta una función de callback y la ejecuta.


"""Prácticas con Callbacks"""

"""1. Usar Callbacks para Separar Lógica
Una buena práctica es utilizar callbacks para separar la lógica de negocio de las tareas de control de flujo. Esto hace que tu código sea más modular y fácil de mantener.

Práctica: Separar la lógica de negocio"""
def operacion(a, b, operacion_callback): 
    """Realiza una operación pasando un callback para realizar la lógica específica"""
    return operacion_callback(a, b)

def sumar(x, y): 
    return x + y 

def restar(x, y): 
    return x - y 

print(operacion(5, 3, sumar)) # 8 
print(operacion(5, 3, restar)) # 2 

#
"""2. Evitar la Sobrecarga de Callbacks
Si un callback es llamado con mucha frecuencia (por ejemplo, en eventos de interfaz gráfica o cuando se interactúa con la red), puede llevar a un rendimiento bajo. Evitar sobrecargar las llamadas al callback es crucial.

Práctica: Limitación de la frecuencia de los callbacks"""
import time 
def callback():
    print("Callback ejecutado.") 

def ejecutar_con_restriccion(callback, intervalo): 
    """Ejecuta un callback, pero lo limita a una vez cada `intervalo` segundos""" 
    last_call = time.time() 
    while True: 
        if time.time() - last_call > intervalo:
            callback() 
            last_call = time.time()
        time.sleep(1) # Ejecutar el callback con una restricción de tiempo 

ejecutar_con_restriccion(callback, 5) # Ejecuta el callback una vez cada 5 segundos 

#
"""3. Usar Callbacks para Controlar el Flujo Asíncrono
Cuando trabajes con código asíncrono, es una buena práctica usar callbacks para ejecutar acciones cuando las tareas asíncronas finalicen, evitando bloquear el hilo principal.

Práctica: Callback en código asíncrono"""
import asyncio 
async def tarea_asincrona(callback):
    await asyncio.sleep(2) # Simular una tarea que toma 2 segundos 
    callback("Tarea finalizada.") 

def notificar(resultado): 
    print(resultado) # Ejecutar la tarea asincrona con callback 

asyncio.run(tarea_asincrona(notificar)) 

#
"""4. Evitar Dependencias Circulares en Callbacks
Es importante evitar dependencias circulares donde un callback depende de otro que lo invoca nuevamente, ya que esto puede llevar a problemas de recursión infinita o a un flujo incontrolado.

Práctica: Evitar dependencias circulares"""
def tarea_1(callback): 
    print("Realizando tarea 1...") 
    callback() 

def tarea_2(callback):
    print("Realizando tarea 2...") 
    callback() # Evitar pasar tareas que se llaman recursivamente entre sí. 
# Define una estructura de control clara en tu flujo de callbacks. 
tarea_1(tarea_2) # Correcto si es necesario, pero evitar ciclos innecesarios. 

#
"""5. Usar functools.partial para Callbacks Parametrizados
En algunos casos, puede ser necesario pasar parámetros adicionales al callback. Puedes usar functools.partial para crear callbacks parametrizados sin modificar las funciones originales.

Práctica: Usar functools.partial"""
import functools

def saludar(nombre, saludo="Hola"):
    print(f"{saludo}, {nombre}!") 
# Crear un callback con un saludo específico 

saludar_maria = functools.partial(saludar, nombre="María", saludo="Buenas tardes") # Usar el callback 
saludar_maria() # "Buenas tardes, María!" 

#

"""Técnicas con Callbacks"""

"""1. Callbacks para Mejorar la Reusabilidad
Una técnica clave es usar callbacks como estrategias de extensión en funciones o clases para mejorar la reutilización de código. Permite que la lógica de procesamiento pueda ser cambiada sin modificar el flujo principal.

Técnica: Mejora de la reutilización usando callbacks"""
def procesar_datos(datos, preprocesar_callback, postprocesar_callback): 
    """Procesa datos usando callbacks para preprocesar y postprocesar""" 
    datos = preprocesar_callback(datos) 
    print(f"Datos procesados: {datos}") 
    datos = postprocesar_callback(datos) 
    return datos 

def preprocesar(datos): 
    return [x*2 for x in datos] 

def postprocesar(datos):
    return [x-1 for x in datos] 

# Uso de callbacks para diferentes etapas del procesamiento
datos = [1, 2, 3]
resultado = procesar_datos(datos, preprocesar, postprocesar) 
print("Resultado final:", resultado) 

#

"""3. Llamar a un Callback Después de un Intervalo de Tiempo
Puedes usar time.sleep o librerías como sched para llamar a un callback después de un intervalo de tiempo. Es útil para manejar tareas que deben ejecutarse periódicamente o con retraso.

Técnica: Ejecutar un callback después de un intervalo"""
import time 
def callback_con_retraso(): 
    print("Callback ejecutado después de 2 segundos.") 
# Llamar al callback después de 2 segundos 
    time.sleep(2) 
    callback_con_retraso() 

#

"""4. Callbacks en Interfaces de Usuario (UI)
En las interfaces gráficas como Tkinter o PyQt, los callbacks se utilizan para manejar eventos de usuario como clics, cambios de valor, entre otros. Aquí la técnica principal es asociar un callback a un evento de interfaz.

Técnica: Callback en un botón de Tkinter"""
import tkinter as tk
def saludar(): 
    print("¡Hola, mundo!") # Crear la ventana de Tkinter 
    ventana = tk.Tk() 

boton = tk.Button(ventana, text="Presiona aquí", command=saludar) 
boton.pack() ventana.mainloop() 