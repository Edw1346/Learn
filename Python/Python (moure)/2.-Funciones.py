"""Funciones y su alcance"""

"""1. Definición de funciones: Una función es un bloque reutilizable de código que realiza una tarea específica. Se define con la palabra clave def. Ejemplo:"""
def saludar(nombre): 
    return f"Hola, {nombre}!" 

"""2. Llamada a funciones: Para ejecutar una función, se utiliza su nombre seguido de paréntesis. Si la función acepta argumentos, se pasan dentro de los paréntesis. Ejemplo:"""
resultado = saludar("Carlos") 
print(resultado) # Salida: Hola, Carlos! 

"""3. Parámetros y argumentos
Parámetros: Son variables definidas en la declaración de la función.
Argumentos: Son los valores que se pasan a la función al llamarla. Ejemplo:"""
def sumar(a, b): # 'a' y 'b' son parámetros 
    return a + b 

print(sumar(3, 5)) # 3 y 5 son argumentos 

"""4. Tipos de parámetros
Parámetros posicionales: Se pasan en el orden en que están definidos.
Parámetros con valor predeterminado: Tienen valores predeterminados si no se proporciona un argumento.
Parámetros arbitrarios:  *args: Recoge múltiples argumentos posicionales.
**kwargs: Recoge múltiples argumentos con nombre. Ejemplo:"""
def ejemplo(a, b=10, *args, **kwargs): 
    print(f"a={a}, b={b}, args={args}, kwargs={kwargs}") 

ejemplo(1, 20, 30, 40, opcion="extra") # Salida: a=1, b=20, args=(30, 40), kwargs={'opcion': 'extra'} 

"""5. Retorno de valores. Una función puede devolver un valor usando la palabra clave return. Si no se incluye return, devuelve None por defecto. Ejemplo:"""
def cuadrado(x): 
    return x ** 2 

print(cuadrado(4)) # Salida: 16 

"""6. Alcance de las variables (Scope)
El alcance determina dónde se puede acceder a una variable:
Local: Definidas dentro de una función. Solo son accesibles dentro de ella.
Global: Definidas fuera de cualquier función. Son accesibles en todo el programa.
No local (nonlocal): Usadas en funciones anidadas para referirse a variables de la función externa. Ejemplo:"""
x = 10 # Variable global 
def funcion(): 
    y = 5 # Variable local 
    print(x) # Se puede acceder a 'x' 
    print(y) # Accesible solo dentro de la función 

funcion() 
x = "global" 

def externa(): 
    x = "enclosing" 

def interna(): 
    x = "local" 

print(x) # Salida: local 
interna() 

externa() 

"""8. Modificación de variables globales: Para modificar variables globales dentro de una función, usa la palabra clave global. Esto no es una práctica recomendada en general. Ejemplo:"""
contador = 0 
def incrementar(): 
    global contador 
    contador += 1 
    
incrementar() 
print(contador) # Salida: 1 

"""9. Funciones anidadas: Son funciones definidas dentro de otras funciones. Pueden acceder al alcance de su función externa. Ejemplo:"""
def externa(): 
    x = "enclosing" 

def interna(): 
    print(x) # Accede a 'x' de la función externa 

interna() 

externa() 

"""10. Decoradores: Son funciones que modifican el comportamiento de otras funciones. Ejemplo:"""
def decorador(func): 
    def envoltura(): 
        print("Antes de la función") 
    func() 
    print("Después de la función") 
    return envoltura 

@decorador 
def saludo(): 
    print("Hola!") 

saludo() 

"""12. Funciones como objetos de primera clase: En Python, las funciones pueden ser asignadas a variables, pasadas como argumentos y devueltas como resultados. Ejemplo:"""
def saludar(): 
    print("Hola!") 
    
accion = saludar 

accion() # Salida: Hola! 

"""13. Generadores: Funciones que producen una secuencia de valores de manera perezosa usando yield. Ejemplo:"""
def contador(): 
    for i in range(5): 
        yield i 
        for numero in contador(): 
            print(numero) 

"""14. Closures: Son funciones anidadas que recuerdan el estado de las variables de su entorno, incluso después de que la función externa haya terminado. Ejemplo:"""
def multiplicador(factor): 
    def multiplica(n): 
        return n * factor 
    return multiplica 

doble = multiplicador(2) 
print(doble(5)) # Salida: 10 

"""15. Tipado de funciones: Python permite anotar los tipos de los parámetros y del retorno de una función, aunque no son obligatorios. Ejemplo:"""
def sumar(a: int, b: int) -> int: 
    return a + b 


"""16. Manejo de excepciones en funciones. Las funciones pueden incluir manejo de errores con try-except. Ejemplo:"""
def dividir(a, b): 
    try: 
        return a / b 
    except ZeroDivisionError: 
        return "Error: División por cero" 

print(dividir(10, 2)) # Salida: 5.0 
print(dividir(10, 0)) # Salida: Error: División por cero 

# Func sin parametros ni retorno
def sin_param_retorno():
    print('Funcion no devuelve nada ni tiene parametros')

# Func con varios parametros con retorno
def suma(num1:int , num2:int):
    return num1 + num2

# Funciones dentro de funciones
def fun_dentro(param1:int,param2:int):
    def suma(n1,n2):
        return n1 + n2
    return suma(param1,param2)

# Funcion con parametros por defecto
def fun_param_defecto(nombre = 'Abel', apellido = 'Perez'):
    return f'Bienvenido, {nombre} {apellido}' 


#Funciones integradas en el lenguaje:
print("El print es una funcion de Python")

a="El len() también lo es"
print(len(a))

#Existen tambien las funciones lambda, que son funciones anónimas pequeñas
multiplicacion=lambda a,b,c : a*b*c
print(multiplicacion(10,3,5))
#Tambien se pueden declarar y llamar en la misma linea
print((lambda var1,var2 : var1**var2)(2,3))

#EXTRA
def ej_extra(a,b):
    for i in range(1,101):
        if not i%3 and not i%5:
            print(a,b)
        elif not i%3:
            print(a)
        elif not i%5:
            print(b)
        else:
            print(i)

ej_extra("pen","pineapple")

#Funcion lambda es una función anónima que se puede usar para hacer una función en una sola linea
#Funcion lambda con un parametro
suma = lambda x: x + 10
print(suma(5))

#Funcion lambda con varios parametros
nombre_completo = lambda nombre, apellido: f"{nombre} {apellido}"
print(nombre_completo("Laura", "Gonzalez"))

#Funcion lambda con varios parametros y operaciones
resta = lambda x,y,z,w: x - y + z / w
print(resta(10,2,3,2))

#Funcion recursiva es una función que se llama a si misma
def factorial(numero = 4):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

print(factorial())

#Funcion con argumentos es una función que recibe un número indeterminado de argumentos
def suma_con_args(*args):
    return sum(args)

print(suma_con_args(1,2,3,4,5))

# Función con diccionarios de argumentos variables 
def estadisticas_temperaturas(*temps, **kwargs):
    media = sum(temps)/len(temps)
    suma = sum((i - media)**2 for i in temps)
    devstd = (suma/(len(temps)-1))**0.5
    if kwargs.get('promedio'):
        print(f"El promedio de las temperaturas es {media} grados")
    if kwargs.get('desviacion'):
        print(f"El desviación estándar de las temperaturas es {round(devstd,3)} grados")

estadisticas_temperaturas(1,2,3,4,5,6,promedio=True,desviacion=True)


## Variables locales y globales en funciones

def variable_locall():
    variable_local = "Valor variable local"
    print(variable_local)
    
variable_locall()

variable_global = "Valor variable global"

def variable_globall():
    global variable_global
    variable_global = "Nuevo valor variable global"
    print(variable_global)
    
variable_globall()

"""------------ Funciones y alcances: Practicas y tecnicas -------------"""

"""1. Definición de Funciones: Las funciones son bloques de código que realizan una tarea específica. Se definen usando la palabra clave def, seguida del nombre de la función y paréntesis con los parámetros, si los hay. """
def saludo():
    print("¡Hola, mundo!")

#2. Parámetros y Argumentos: Las funciones pueden aceptar parámetros (entradas) y devolver valores (salidas). Los parámetros se definen en la firma de la función.

def suma(a, b):
    return a + b

#3. Alcance (Scope): El alcance determina la visibilidad de las variables dentro de una función. Las variables definidas dentro de una función son locales a esa función y no pueden ser accedidas fuera de ella.
def ejemplo():
    x = 10  # Variable local
    print(x)

#4. Funciones Anónimas (Lambda): Las funciones lambda son pequeñas funciones anónimas definidas con la palabra clave lambda.
suma = lambda x, y: x + y




#1. Nombres Descriptivos: Usa nombres que describan claramente lo qué hace, evitar nombres genéricos como func1 o doSomething. Ejemplo:
# Correcto
def calcular_area_rectangulo(base, altura):
    return base * altura
#Consejo: Si una función realiza algo complejo, usa un nombre más detallado.

#2. Mantén Funciones Pequeñas y Simples. Cada función debe hacer una sola cosa.nDivide tareas complejas en varias funciones pequeñas. Ejemplo:
# Correcto: Una función por tarea
def leer_datos():
    # Lógica para leer datos
    pass

def procesar_datos(datos):
    # Lógica para procesar datos
    pass

def guardar_resultados(resultados):
    # Lógica para guardar resultados
    pass

#3. Usa Parámetros en Lugar de Variables Globales. Evitar: Modificar variables globales dentro de una función. Ejemplo:
# Correcto
def aumentar_porcentaje(valor, porcentaje):
    return valor * (1 + porcentaje / 100)

#4. Documenta tus Funciones. Usa docstrings para explicar qué hace la función, sus parámetros y su retorno. Ejemplo:
def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    
    Args:
        numeros (list): Una lista de números enteros o flotantes.
    
    Returns:
        float: El promedio de los números.
    """
    return sum(numeros) / len(numeros)

#5. Usa Valores Predeterminados para los Parámetros. Ayuda a que las funciones sean más flexibles y fáciles de usar. Ejemplo:
def saludar(nombre, mensaje="¡Hola!"):
    return f"{mensaje} {nombre}"


print(saludar("Carlos"))  # Salida: ¡Hola! Carlos
print(saludar("Ana", "Buenos días"))  # Salida: Buenos días Ana

#6. Maneja los Errores. Utiliza try-except para capturar errores y proporcionar mensajes claros. Ejemplo:
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero"

#7. Evita los "Code Smells". Si una funcionalidad aparece en varios lugares, conviértela en una función reutilizable. Pasa solo los argumentos que necesitas. Ejemplo:
# Correcto
def calcular_impuestos(salario):
    return salario * 0.15

#8. Funciones Puramente Funcionales. Una función pura: No tiene efectos secundarios (no modifica variables fuera de su alcance). Siempre produce el mismo resultado para las mismas entradas. Ejemplo:
# Correcto
def sumar(a, b):
    return a + b

# Incorrecto: Modifica un estado global
resultado = 0
def sumar_y_guardar(a, b):
    global resultado
    resultado = a + b
    return resultado

#9. Usa Anotaciones de Tipos: Añade tipos de datos para que sea más claro cómo usar la función. Ejemplo:
def calcular_descuento(precio: float, descuento: float) -> float:
    """
    Calcula el precio después de aplicar un descuento.
    """
    return precio - (precio * descuento / 100)


#10. Pruebas Unitarias: Escribe pruebas para validar que tus funciones funcionan como se espera. Usa módulos como unittest o pytest. Ejemplo con unittest:

import unittest
def sumar(a, b):
    return a + b

class TestFunciones(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)
if __name__ == "__main__":
    unittest.main()





"""Técnicas para el Uso de Funciones en Python"""

# Paso de Argumentos y Retorno. Pasar datos a las funciones mediante parámetros y devolver valores con return. Ejemplo:
def sumar(a, b):

    return a + b
resultado = sumar(3, 5)
print(resultado)  # Salida: 8

#3. Evitar Código "Hardcoded". Usa parámetros en lugar de escribir datos directamente dentro de la función.
def sumar(a, b):
    return a + b

#4. Valores Predeterminados. Facilitan el uso de funciones al establecer valores por defecto para parámetros opcionales. Ejemplo:
def calcular_total(precio, impuesto=0.15):
    return precio * (1 + impuesto)
print(calcular_total(100))  # Usa el impuesto predeterminado (15%)
print(calcular_total(100, 0.20))  # Usa un impuesto del 20%

#5. Argumentos por Nombre y por Posición. Python permite pasar argumentos por posición (orden) o por nombre (clave-valor). Ejemplo:
def presentar(nombre, edad):
    return f"Soy {nombre} y tengo {edad} años."

# Llamada por posición
print(presentar("Ana", 25))
# Llamada por nombre
print(presentar(edad=25, nombre="Ana"))

"""6. Argumentos Variables (*args y **kwargs)
*args: Agrupa argumentos posicionales en una tupla.
**kwargs: Agrupa argumentos nombrados en un diccionario. Ejemplo:"""
def sumar_todos(*numeros):
    return sum(numeros)
print(sumar_todos(1, 2, 3, 4))  # Salida: 10

def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")
mostrar_info(nombre="Carlos", edad=30, profesion="Ingeniero")


#8. Funciones Anidadas. Definir funciones dentro de otras funciones, lo que permite encapsular lógica interna. Ejemplo:
def exterior(mensaje):
    def interior():
        return mensaje.upper()
    return interior()
print(exterior("hola"))  # Salida: HOLA

#9. Clausuras (Closures). Una clausura es una función anidada que recuerda las variables del ámbito donde fue creada. Ejemplo:
def multiplicador(n):
    def multiplicar(x):
        return x * n
    return multiplicar

doble = multiplicador(2)
triple = multiplicador(3)

print(doble(5))  # Salida: 10
print(triple(5))  # Salida: 15


#10. Funciones de Orden Superior. Funciones aceptan otras funciones como parámetros o devuelven funciones. Ejemplo:

def aplicar_operacion(funcion, valor):
    return funcion(valor)
resultado = aplicar_operacion(lambda x: x ** 2, 4)
print(resultado)  # Salida: 16

#11. Decoradores. Son funciones que modifican el comportamiento de otras funciones. Ejemplo:
def decorador(func):
    def envoltura():
        print("Antes de la función")
        func()
        print("Después de la función")
    return envoltura

@decorador
def saludar():
    print("Hola")
saludar()
# Salida:
# Antes de la función
# Hola
# Después de la función

#12. Funciones Lambda: Ideal para escribir funciones pequeñas de manera rápidas. Ejemplo:
doblar = lambda x: x * 2
print(doblar(4))  # Salida: 8

#13. Tipado Estático con Anotaciones: Agrega información de tipos para documentar mejor tus funciones. Ejemplo:
def sumar(a: int, b: int) -> int:
    return a + b

#14. Programación Funcional (Map, Filter, Reduce): Aprovecha funciones de orden superior para operar sobre colecciones. Ejemplo:
numeros = [1, 2, 3, 4, 5]

# Map
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]

# Filter
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4]

# Reduce
from functools import reduce
suma = reduce(lambda x, y: x + y, numeros)
print(suma)  # Salida: 15







"""Funciones Lambda en Python
Son funciones anónimas que no requieren un nombre explícito al ser definidas. Se utilizan para realizar operaciones simples en una sola línea de código.

Sintaxis
lambda argumentos: expresión
1. lambda: Es la palabra clave para definir una función lambda.

2. argumentos: Uno o más parámetros separados por comas (pueden ser opcionales).
3. expresión: La operación o valor que será devuelto.
Las funciones lambda siempre devuelven el resultado de la expresión, sin necesidad de usar return.

Ejemplos Prácticos"""

#1. Suma de dos números:
suma = lambda x, y: x + y
print(suma(5, 3))  # Salida: 8

#2. Usar en una lista: Filtrar números pares en una lista:
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4, 6]

#3. Ordenar por un criterio: Ordenar una lista de tuplas por el segundo elemento:
personas = [("Ana", 25), ("Luis", 20), ("Sofía", 30)]
personas_ordenadas = sorted(personas, key=lambda x: x[1])
print(personas_ordenadas)
# Salida: [('Luis', 20), ('Ana', 25), ('Sofía', 30)]

#4. Aplicar operaciones matemáticas: Elevar un número al cuadrado:
cuadrado = lambda x: x**2
print(cuadrado(4))  # Salida: 16


"""Buenas Prácticas para el Uso de Funciones Lambda en Python"""

#1. Usa Lambda para Operaciones Simples. No usar lambda para lógica compleja
# Usar lambda para una operación simple
doblar = lambda x: x * 2
print(doblar(5))  # Salida: 10

#2. Usa Lambda para Funciones Temporales o Anónimas o si no necesitas reutilizar una función, útiles en situaciones donde no deseas definir una función completa con def.
# Usar lambda directamente en una operación
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]

#3. Evita Lambdas Complejas con Múltiples Expresiones. Si una operación es compleja, usa una función normal con def.
# Simple lambda con una sola operación
suma = lambda x, y: x + y
print(suma(3, 4))  # Salida: 7

#4. Usa Lambda en Funciones de Orden Superior, usadas como argumentos de funciones con map(), filter(), sorted(), etc.
# Usar lambda con filter()
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4, 6]
#Aunque ambas formas son válidas, usar una lambda aquí es menos claro y no tiene tanto beneficio en cuanto a legibilidad.

#5. Usa Nombres de Variables Claros. Pueden ser asignadas una variable, asegúrate de usar nombres descriptivos.
# Usar nombre descriptivo
es_par = lambda x: x % 2 == 0
print(es_par(4))  # Salida: True

#7. Usa Lambda para Expresiones Funcionales Simples en Librerías de Terceros como pandas, numpy o funciones de bibliotecas de manejo de colecciones.
#Correcto:

import pandas as pd
data = {'nombre': ['Ana', 'Luis', 'Carlos'], 'edad': [28, 22, 35]}
df = pd.DataFrame(data)
# Usar lambda para aplicar funciones en columnas
df['edad_doble'] = df['edad'].apply(lambda x: x * 2)
print(df)

#8. No Confundir Lambda con Funciones Anónimas en Otros Lenguajes. Las lambdas son solo funciones anónimas y se deben utilizar principalmente para tareas simples.




#Técnicas para Usar Funciones Lambda en Python

#1. Uso con Condicionales: Define funciones lambda con expresiones condicionales para operaciones más dinámicas.
# Retornar "Par" o "Impar"
es_par = lambda x: "Par" if x % 2 == 0 else "Impar"
print(es_par(4))  # Salida: Par
print(es_par(5))  # Salida: Impar

#2. Lambdas con Argumentos Variables (*args y **kwargs): Usa lambdas para manejar un número variable de argumentos.
# Sumar todos los argumentos
suma_total = lambda *args: sum(args)
print(suma_total(1, 2, 3, 4))  # Salida: 10

#3. Composición de Funciones Lambda: Combina lambdas para crear funciones complejas reutilizando funciones simples.
# Dos lambdas combinadas: multiplicar y sumar
multiplicar = lambda x: x * 2
sumar = lambda x: x + 3
composicion = lambda x: sumar(multiplicar(x))
print(composicion(4))  # Salida: 11

#4. Uso con reduce(): Combina lambdas con reduce() para realizar operaciones acumulativas.
from functools import reduce
# Multiplicar todos los números de una lista
numeros = [1, 2, 3, 4]
producto = reduce(lambda x, y: x * y, numeros)
print(producto)  # Salida: 24

#5. Lambdas en Decoradores: Usa lambdas como decoradores simples.
# Decorador con lambda
decorador = lambda funcion: lambda x: f"Resultado: {funcion(x)}"
@decorador
def cuadrado(x):
    return x ** 2
print(cuadrado(5))  # Salida: Resultado: 25

#6. Lambdas para Expresiones Complejas con Operadores Lógicos: Para manejar múltiples condiciones.
# Clasificar números según su valor
clasificar = lambda x: "Negativo" if x < 0 else "Cero" if x == 0 else "Positivo"
print(clasificar(-5))  # Salida: Negativo
print(clasificar(0))   # Salida: Cero
print(clasificar(7))   # Salida: Positivo

#7. Lambdas con Generadores: Integra lambdas con generadores para manipular datos grandes.
# Generador con una lambda para filtrar números pares
numeros = range(10)
pares = (x for x in numeros if (lambda x: x % 2 == 0)(x))
print(list(pares))  # Salida: [0, 2, 4, 6, 8]


#8. Uso con Configuraciones Dinámicas: Usa lambdas para definir funciones personalizables sobre la marcha.
# Crear una función personalizada con parámetros
crear_funcion = lambda n: lambda x: x * n
doblar = crear_funcion(2)
triplicar = crear_funcion(3)
print(doblar(4))  # Salida: 8
print(triplicar(4))  # Salida: 12




"""Buenas Prácticas y Técnicas en el Alcance de una Función en Python (Scope)"""

#1. Define Variables en el Alcance Más Reducido Posible. Mantén las variables en el alcance más limitado posible para evitar conflictos y confusiones. Evita modificar variables globales desde dentro de una función.
def calcular_area(base, altura):
    area = base * altura
    return area

# La variable `area` solo existe dentro de la función
print(calcular_area(5, 3))  # Salida: 15

#2. Usa Variables Globales Solo Cuando Sea Necesario. Evita usar variables globales a menos que sea absolutamente necesario, ya que pueden causar problemas de mantenimiento y errores en proyectos grandes.
CONSTANTE_GRAVEDAD = 9.8  # Correcto para valores constantes
def calcular_peso(masa):
    return masa * CONSTANTE_GRAVEDAD
print(calcular_peso(70))  # Salida: 686.0

#3. Evita Sobrescribir Variables en el Alcance Global. Si necesitas trabajar con una variable global, úsala como referencia, pero no la sobrescribas directamente.
#Incorrecto:
contador = 0
def incrementar():
    contador += 1  # Error: UnboundLocalError
    return contador

#Correcto:
contador = 0
def incrementar():
    global contador
    contador += 1
    return contador

#4. Usa nonlocal para Modificar Variables en Alcances Externos. En funciones anidadas, usa la palabra clave nonlocal para modificar una variable en un alcance externo pero no global.
def generar_contador():
    contador = 0

    def incrementar():
        nonlocal contador
        contador += 1
        return contador

    return incrementar
contador = generar_contador()
print(contador())  # Salida: 1
print(contador())  # Salida: 2

#5. Evita Nombrar Variables con Mismo Nombre Alcances Diferentes. Puede causar confusión y errores difíciles de depurar.
#Incorrecto:
x = 10
def funcion():
    x = 5  # Confusión: ¿a cuál `x` nos referimos?
    print(x)
funcion()
print(x)

#Correcto:
variable_global = 10
def funcion():
    variable_local = 5
    print(variable_local)
funcion()
print(variable_global)



"""Técnicas en el Manejo del Alcance"""

"""1. Comprender los Niveles de Alcance: LEGB
Python sigue la regla LEGB para buscar variables:
1. Local: Dentro de la función actual.
2. Enclosing: En funciones anidadas.
3. Global: Variables definidas en el nivel global del módulo.
4. Built-in: Funciones y nombres integrados de Python.
Ejemplo:"""

x = "global"  # Alcance global
def funcion_externa():
    x = "enclosing"  # Alcance de cierre
    def funcion_interna():
        x = "local"  # Alcance local
        print(x)
    funcion_interna()
funcion_externa()  # Salida: local
print(x)           # Salida: global

#2. Usa Variables Globales Manera Controlada. Si necesitas trabajar con variables globales, centraliza definición y acceso.
configuracion = {"modo": "producción"}
def obtener_modo():
    return configuracion["modo"]

def cambiar_modo(nuevo_modo):
    configuracion["modo"] = nuevo_modo
print(obtener_modo())  # Salida: producción
cambiar_modo("desarrollo")
print(obtener_modo())  # Salida: desarrollo


#3. Usa Funciones Anidadas para Modularidad. Las funciones anidadas pueden usar variables de alcances externos, lo que permite encapsular lógica sin contaminar el alcance global.
def fabrica_mensajes(prefijo):
    def mensaje(nombre):
        return f"{prefijo} {nombre}"
    return mensaje

saludo = fabrica_mensajes("Hola")

despedida = fabrica_mensajes("Adiós")
print(saludo("Juan"))     # Salida: Hola Juan
print(despedida("María")) # Salida: Adiós María

#4. Usa Closures para Persistir Estado. Un closure es una función que "recuerda" el alcance en el que fue creada.
def contador():
    cuenta = 0
    def incrementar():
        nonlocal cuenta
        cuenta += 1
        return cuenta
    return incrementar
mi_contador = contador()
print(mi_contador())  # Salida: 1
print(mi_contador())  # Salida: 2

#5. Usa globals() y locals() con Precaución. Estas funciones permiten acceder a las variables globales o locales, pero deben usarse con cuidado para evitar efectos secundarios inesperados.
x = 10

# Acceder a variables globales
print(globals()["x"])  # Salida: 10

# Crear dinámicamente una variable local
def crear_variable():
    locals()["y"] = 20
    print(locals().get("y"))  # Salida: None (no afecta realmente el alcance local)
crear_variable()

#6. Usa Decoradores para Extender el Alcance. Los decoradores pueden ayudar a gestionar el alcance modificando o extendiendo el comportamiento de funciones.
def decorador(funcion):
    contador = 0

    def envoltura(*args, **kwargs):
        nonlocal contador
        contador += 1
        print(f"Llamada número: {contador}")
        return funcion(*args, **kwargs)
    return envoltura

@decorador
def saludar(nombre):
    print(f"Hola, {nombre}")
saludar("Juan")
saludar("María")

#7. Usa Contextos Globales con Clases (Alternativa). En lugar de variables globales puras, encapsula los datos globales en clases.
class Configuracion:
    modo = "producción"

def obtener_modo():
    return Configuracion.modo

def cambiar_modo(nuevo_modo):
    Configuracion.modo = nuevo_modo
print(obtener_modo())  # Salida: producción
cambiar_modo("desarrollo")
print(obtener_modo())  # Salida: desarrollo


"""
Resumen de Buenas Prácticas y Técnicas
1. Minimiza el uso de variables globales.
2. Usa closures y nonlocal para persistir estado.
3. Aplica funciones anidadas para modularidad.
4. Sigue la regla LEGB para comprender el alcance.
5. Evita conflictos de nombres entre variables locales y globales.
6. Encapsula datos globales en clases o estructuras.
"""


"""Usos Combinados de Lambda y Scope"""

#1. Lambda con variable global:
multiplicador = 2
doble = lambda x: x * multiplicador
print(doble(5))  # Salida: 10

#2. Cuidado con el alcance en lambdas anidadas:
def crear_multiplicador(n):
    return lambda x: x * n
por_tres = crear_multiplicador(3)
print(por_tres(4))  # Salida: 12



"""Usos Combinados de Lambda y Scope"""

#1. Lambda con variable global:
multiplicador = 2
doble = lambda x: x * multiplicador
print(doble(5))  # Salida: 10

#2. Cuidado con el alcance en lambdas anidadas:
def crear_multiplicador(n):
    return lambda x: x * n
por_tres = crear_multiplicador(3)
print(por_tres(4))  # Salida: 12




"""
1. Variables Locales: Se define dentro de una función. Estas variables solo existen y son accesibles dentro del ámbito de esa función y no afectan ni son afectadas por variables con el mismo nombre en otros ámbitos.
Características: Solo existen dentro de la función donde se definen. No son accesibles fuera de esa función. Se destruyen una vez que la función termina su ejecución. Ejemplo:"""
def ejemplo_local(): 
    x = 10 # Variable local 
    print(f"Variable local dentro de la función: {x}") 

ejemplo_local() # print(x) # Error: NameError, 'x' no está definido fuera de la función 

"""2. Variables Globales: Se define fuera de todas las funciones. Estas variables están disponibles en todo el programa, incluyendo dentro de funciones, siempre que no se cree una variable local con el mismo nombre.
Características: Son accesibles desde cualquier parte del código. Se pueden leer dentro de funciones, pero para modificarlas dentro de una función, debes usar la palabra clave global. Pueden ser sobrescritas accidentalmente, por lo que deben usarse con cuidado. Ejemplo:"""
x = 20 # Variable global def ejemplo_global(): 

global x # Indica que queremos modificar la variable global 
x = 30 
print(f"Variable global modificada dentro de la función: {x}") 
print(f"Variable global antes de la función: {x}") 

def ejemplo_global():
    print(f"Variable global después de la función: {x}") 

"""3. Variables Nonlocal: Se utiliza en funciones anidadas (closures). Permite acceder y modificar una variable de un ámbito intermedio, es decir, una variable definida en la función contenedora, pero que no es ni local ni global. Características: Permite modificar variables de un ámbito externo inmediato, pero no global. Es útil para closures, donde una función interna necesita modificar una variable de su función contenedora. Ejemplo:"""
def ejemplo_nonlocal(): 
    x = 10 # Variable del ámbito externo inmediato
    def interna(): 
        nonlocal x # Modifica la variable del ámbito externo inmediato 
        x = 20
        print(f"Variable nonlocal dentro de la función interna: {x}") 
        interna() 
        print(f"Variable nonlocal modificada dentro de la función principal: {x}") 

ejemplo_nonlocal() 

#Closure: retonar referencia de funcion. Desempaquetar los return y acceder a las funciones internas
def funcion_principal(): 
    def funcion_interna(): 
        return "Hola desde la función interna" 
    return funcion_interna # Retornamos la referencia 

# Guardamos la referencia en una variable 
ref_funcion = funcion_principal() # Ahora ejecutamos la función interna 

print(ref_funcion()) # Salida: Hola desde la función interna 

"""Desempaquetar múltiples retornos
Puedes retornar varias funciones internas como referencias, empaquetarlas en una estructura como una tupla o lista, y luego desempaquetarlas para usarlas por separado. Ejemplo: Retornar y desempaquetar funciones internas"""

def funcion_principal(): 
    def suma(a, b): 
        return a + b
    
    def resta(a, b): 
        return a - b 

    def multiplicacion(a, b): 
        return a * b # Retornamos las referencias de las funciones internas en una tupla 
    return suma, resta, multiplicacion 

# Desempaquetamos las funciones 
suma_func, resta_func, multiplicacion_func = funcion_principal() # Ahora usamos las funciones internas
print(suma_func(5, 3)) # Salida: 8 
print(resta_func(10, 4)) # Salida: 6 
print(multiplicacion_func(2, 3)) # Salida: 6 


#Acceder a las funciones internas dinámicamente, por un diccionario 

def calculadora(): 
    def suma(a, b): 
        return a + b
    def resta(a, b): 
        return a - b 
    def multiplicacion(a, b): 
        return a * b 
    # Retornamos las referencias como un diccionario 
    return { "sumar": suma, "restar": resta, "multiplicar": multiplicacion } 
# Obtenemos el diccionario de funciones 
operaciones = calculadora() # Accedemos a las funciones internas por nombre 
print(operaciones["sumar"](10, 5)) # Salida: 15 
print(operaciones["restar"](20, 7)) # Salida: 13 
print(operaciones["multiplicar"](4, 3)) # Salida: 12 



#Ejecutar la función interna y con un print o un return dentro de la función principal
def saludo(nombre):
    def mensaje():
        print(f"Hola, {nombre}!")  # Usamos print en la función interna
    return mensaje  # Retornamos la referencia a la función interna

# Obtenemos la referencia a la función interna
saludar = saludo("Juan")

# Llamamos a la función interna
saludar()  # Salida: Hola, Juan!
saludar()  # Salida: Hola, Juan!


#En la función principal retornar la función interna con paréntesis con parámetros

def calcular_area_circulo():
    def area(radio):
        return 3.1416 * (radio ** 2)
    
    # Ejecutamos la función interna y retornamos su resultado
    return area(5)

# Llamamos a la función principal
resultado = calcular_area_circulo()
print(resultado)  # Salida: 78.54

#En la función principal Retornar el resultado de una función interna en una variable

def funcion_principal():
    def funcion_interna():
        return "Hola desde la función interna"
    
    # Ejecutamos la función interna y usamos print
    resultado = funcion_interna()
    print("Desde la función principal:", resultado)


# Llamamos a la función principal
funcion_principal()

#En la funcion principal Retornar la función interna (con paréntesis) que está asu vez retorna un valor

def funcion_principal():
    def funcion_interna():
        return "Retorno de la función interna"
    
    # Ejecutamos la función interna y retornamos su resultado
    return funcion_interna()

# Obtenemos el valor retornado por la función principal
resultado = funcion_principal()
print(resultado)  # Salida: Retorno de la función interna