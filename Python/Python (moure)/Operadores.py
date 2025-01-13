a = 1
b = 2
print("Dadas las variables a=1 y b=2:\n")

"""---------------------------------    Operadores aritméticos    ---------------------------------""" 

# Operadores aritméticos:
numero1 = 20
numero2 = 30
print("Suma", numero1 + numero2)        # 50
print("Resta", numero1 - numero2)       # -10
print("Multiplicación", numero1 * numero2)  # 600
print("División", numero1 / numero2)    # 0.6666666666666666
print("División entera", numero1 // numero2)  # 0
print("Módulo", numero1 % numero2)     # 20
print("Potenciación", numero1 ** numero2)  # 107374182400

# Operadores lógicos
y = a and b
o = a or b
no = not a
print(f"""Las operaciones lógicas básicas realizables son:
      AND: {y}
      OR: {o}
      NOT: {no}\n""")

print(True and True)        # devuelve True
print(True and False)       # devuelve False
print(True or False)        # devuelve True
print(False or True)        # devuelve True
print(not True)             # devuelve False
print(not False)            # devuelve True



"""---------------------------------    Operadores comparacion    ---------------------------------""" 

# Operadores de comparacion
mayor_que = a>b
mayor_o_igual = a>=b
menor_que = a<b
menor_o_igual = a<=b
igualdad = a==b
desigualdad = a!=b
print(f"""Las operaciones de comparacion realizables son:
Mayor que: {mayor_que}
Mayor o igual que: {mayor_o_igual}
Menor que: {menor_que}
Menor o igual que: {menor_o_igual}
Igualdad: {igualdad}
Desigualdad: {desigualdad}\n""")



"""---------------------------------    Operadores asignacion    ---------------------------------""" 

# Operadores de asignación ( is, is not) -> comprobar si dos variables emplean la misma ubicacion en memoria
asignacion = "simbolo ="
a += b
a -= b
a *= b
print(f"""En principio la asignación se hace con {asignacion}
    Es posible agregar cualquier operación aritmética a la vez que se asigna valor de manera que se asignará a la variable su propio valor con la operación realizada""")

# Operadores de identidad
es = a is b
no_es = a is not b
print(f"""Las operaciones de identidad realizables son:
Es: {es}
No es: {no_es}""")
a = 1
b = 2
c = 2

a is b # False
b is c # True
b is not c # False
a is not c # True

# Operadores de pertenencia ( in, not it) -> para indicar pertenencia a alguna secuencia (listas, tuplas, strings)
a = "gato"
b = "perro"
en = a in b
no_en = a not in b
print(f"""Las operaciones de pertenencia son para elementos iterables, tenemos que cambiar las variables a a="gato" y b="perro":
    En: {en}
    No en: {no_en}""")

"""Saber si 2 variables apuntan al mismo objeto en memoria, es útil cuando trabajas con tipos de datos mutables o cuando necesitas un control fino sobre la gestión de la memoria en tu programa."""

#1. Evitar Cambios Inesperados (Comportamiento de Objetos Mutables). Optimizar memoria. Ejemplo:
a = [1, 2, 3]
b = a  # b y a apuntan al mismo objeto
b[0] = 100  # Modificamos b
print(a)  # [100, 2, 3], también se modifica a
print(b)  # [100, 2, 3]
#El hecho de que a y b apunten al mismo objeto lleva a cambios no esperados si no somos conscientes de esto.

#2. Controlar la Memoria y Evitar Copias Innecesarias. Ejemplos:
a = [1, 2, 3]
b = a  # b apunta al mismo objeto
# No necesitamos copiar a 'a' para usarlo en otro lugar
b.append(4)
print(a)  # [1, 2, 3, 4], b y a comparten el mismo objeto

#3. Asegurarte de que las Variables Están Independientes (Evitar Referencias No Deseadas). Copia profunda Ejemplo copia:
a = [1, 2, 3]
b = a.copy()  # Creamos una copia de a, no solo una referencia
b[0] = 100
print(a)  # [1, 2, 3], a no se ve afectada
print(b)  # [100, 2, 3], b tiene la modificación

#4. Comparaciones Rápidas y Optimización. Ejemplo:
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # True, a y b apuntan al mismo objeto
print(a is c)  # False, a y c son objetos diferentes

#5. Comportamiento con Tipos Inmutables. Si asignas un valor de uno a otro, se crea un nuevo objeto. Ejemplo:
a = (1, 2, 3)
b = a  # b y a apuntan al mismo objeto
b = (4, 5, 6)  # Asignamos un nuevo objeto a b, no afecta a a
print(a)  # (1, 2, 3)
print(b)  # (4, 5, 6)

#6. Aplicación en Programación Orientada a Objetos. Ejemplo con objetos:
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
a = Persona("Juan")
b = a  # b y a apuntan al mismo objeto
b.nombre = "Carlos"
print(a.nombre)  # Carlos, ya que a y b apuntan al mismo objeto



"""---------------------------------    Operadores pertenencia    ---------------------------------""" 

#in Está en
#not in No está en

lista = [1, 2, 3, 4, 5, 12]
print(9 in lista) # False
print(9 not in lista) # True
print(12 in lista) # True
print(12 not in lista) # False

"""El operador in se usa para comprobar si un elemento está presente dentro de una colección (como listas, cadenas, diccionarios, etc.). Devuelve True si el elemento está presente y False en caso contrario.

1. Con cadenas: Verifica si una subcadena está dentro de otra."""
texto = "Hola, mundo"
print("Hola" in texto)  # Salida: True
print("Adiós" in texto)  # Salida: False

#2. Con listas: Comprueba si un valor existe en una lista.
numeros = [1, 2, 3, 4, 5]
print(3 in numeros)  # Salida: True
print(6 in numeros)  # Salida: False

"""3. Con diccionarios: Busca si una clave específica está presente (no valores)."""

diccionario = {"nombre": "Juan", "edad": 30}
print("nombre" in diccionario)  # Salida: True
print("apellido" in diccionario)  # Salida: False

"""4. Con conjuntos (set): Comprueba si un elemento pertenece al conjunto."""
conjunto = {10, 20, 30}
print(20 in conjunto)  # Salida: True
print(25 in conjunto)  # Salida: False




"""---------------------------------    Operadores de bit    ---------------------------------""" 

# Operadores bitwise
num1 = 23 # 10111
num2 = 10 # 01010
print(f"La operación AND entre {num1} y {num2} es: {num1 & num2}") #Operador de bits AND (00010) (2)
print(f"La operación OR entre {num1} y {num2} es: {num1 | num2}") #Operador de bits OR (11111) (31)
print(f"La operación XOR entre {num1} y {num2} es: {num1 ^ num2}") #Operador de bits XOR (11101) (29)
print(f"La operación NOT de {num1} es: {~num1}") #Operador de bits NOT (11111111111111111111111111101000) (-24)
print(f"La operación de corrimiento a la izquierda de {num1} es: {num1 << num2}") #Operador de bits de desplazamiernto a la izquierda (101110000000000000000) (23552)
print(f"La operación de corrimiento a la derecha de {num1} es: {num1 >> num2}") #Operador de bits de desplazamiernto a la derecha (0) (0)

print(bin(5))

print(bin(3))
print(bin(5&3))
print(bin(5|3))
print(bin(5>>2))
print(bin(5<<2))

#Los operadores bit a bit (bitwise operators) en Python sirven para trabajar directamente con los bits que componen un número.

"""Usos: Encriptar con bits y operadores bit a bit
La encriptación con bits utiliza principalmente el operador XOR (^) para codificar y decodificar datos. Esto funciona porque XOR tiene una propiedad única: Si aplicas XOR dos veces con el mismo número (clave), recuperas el dato original. Es decir:
Ejemplo de encriptación con XOR
1. Codificar un mensaje: Usamos un número como clave. Realizamos XOR entre el mensaje y la clave.
2. Decodificar el mensaje: Aplicamos XOR nuevamente con la misma clave al mensaje codificado. Código:"""
# Mensaje y clave
mensaje = 123  # Número a encriptar
clave = 42     # Clave secreta

# Encriptar
mensaje_codificado = mensaje ^ clave
print(f"Mensaje codificado: {mensaje_codificado}")

# Desencriptar
mensaje_original = mensaje_codificado ^ clave
print(f"Mensaje desencriptado: {mensaje_original}")

"""Salida:
Mensaje codificado: 81
Mensaje desencriptado: 123
¿Por qué funciona? Porque XOR cancela el efecto de la clave al aplicarla dos veces: 

Puedes convertir letras (caracteres) en su representación binaria usando sus códigos ASCII (mediante ord()) y luego aplicar operadores de bits. Para volver a convertir, usarías chr().

Ejemplo: Encriptar y desencriptar letras con XOR"""
letra = 'A'  # Letra que queremos codificar
clave = 42    # Clave secreta

# Convertimos la letra a su valor ASCII
ascii_letra = ord(letra)  # 65 para 'A'

# Encriptamos
ascii_codificado = ascii_letra ^ clave

# Convertimos a letra encriptada (puede no ser legible directamente)
letra_codificada = chr(ascii_codificado)
print(f"Letra codificada: {letra_codificada}")

# Desencriptamos
ascii_desencriptado = ascii_codificado ^ clave
letra_original = chr(ascii_desencriptado)
print(f"Letra original: {letra_original}")

"""Salida: 
Letra codificada: k
Letra original: A"""

"""Máscaras de bits
Cuando trabajas con máscaras de bits, cada bit en un número binario puede representar un estado o configuración 

(encendido/apagado, verdadero/falso, habilitado/deshabilitado). "Activar" o "desactivar" bits se refiere a cambiar estos estados:

Activar un bit: Cambiar un bit específico a 1.
Desactivar un bit: Cambiar un bit específico a 0.

Activar un bit con OR |:"""
numero = 0b0100  # 4 en binario
mascara = 0b0010  # Máscara para activar el segundo bit
resultado = numero | mascara
print(bin(resultado))  # Salida: 0b0110
#Aquí, el segundo bit de numero pasa de 0 a 1.

#Desactivar un bit con AND & y NOT ~:
numero = 0b0110  # 6 en binario
mascara = ~0b0010  # Máscara para desactivar el segundo bit
resultado = numero & mascara
print(bin(resultado))  # Salida: 0b0100
#Aquí, el segundo bit de numero pasa de 1 a 0.

"""No existe un único estándar universal para los patrones de bits usados en máscaras; puedes diseñar tus propios patrones según lo que necesites controlar. Sin embargo, en muchos contextos (especialmente en sistemas operativos, programación y hardware), hay convenciones comunes que organizan los bits de forma estructurada para representar permisos o configuraciones.

Patrones personalizados para máscaras de bits
Puedes definir tus propios patrones para representar estados o permisos. Por ejemplo:
Cada bit puede representar un permiso específico.
Puedes activar (1) o desactivar (0) bits para personalizar configuraciones.

Ejemplo: Máscara para permisos personalizados
Supongamos que diseñamos un sistema donde cada bit tiene un significado:
Bit 0: Permiso de lectura.
Bit 1: Permiso de escritura.
Bit 2: Permiso de ejecución.

Un número en binario como 0b011 significaría:
Lectura: Sí (1).
Escritura: Sí (1).
Ejecución: No (0).
Con esto, puedes crear patrones para manejar tus propios permisos."""


"""*****------------------------------    Estructuras de control    ----------------------------*****""" 



"""---------------------------------    Condicionales    ---------------------------------""" 

# Condicionales: If, elif, else ( controlar si se cumple 1 o varias condiciones -> utilizar operadores de comparacion y logicos)
if a<b:
    print("a es menor que b")
elif a>b:
    print("a es mayor que b")
else:
    print("deben ser iguales porque no se cumple ninguna condicion...")

#1. Condicionales, técnicas y prácticas 

"""1. Escribir condiciones claras y específicas. Evitar condiciones innecesariamente complejas:"""
if (x > 0 and x < 10) and (y > 5 or z != 0):  # Difícil de leer
# Usar condiciones claras:
if 0 < x < 10 and (y > 5 or z != 0):  # Más limpio y conciso
#Usa comparaciones encadenadas (como 0 < x < 10) siempre que sea posible.

"""2. Ordenar las condiciones de mayor probabilidad, ahorrando tiempo de procesamiento. En Python, valores como 0, None, ' ', y listas vacías [] son evaluados como False. Ejemplo:"""
# Simplifica
if lista:     print("Lista no está vacía")
#3. Usar valores predeterminados para simplificar Cuando necesitas evaluar múltiples opciones con un valor predeterminado, organiza el flujo lógico con claridad.

"""4. Evitar anidamientos profundos
5. Usar expresiones ternarias para asignaciones simples
6. Usar estructuras de datos (lista, conjunto, Tuplas) para simplificar múltiples condiciones"""
colores_validos = ["rojo", "verde", "azul"]
if color in colores_validos:    print("Color válido")
"""7. Comentar condiciones complejas
8. Reducir dependencias en variables globales."""
# Usar parámetros o variables locales
def verificar(valor):     
    if valor > 10:
#9. Aprovechar match-case (Python 3.10+) como una alternativa más clara y escalable para múltiples condiciones.
match color:
    case "rojo":   print("Es rojo")
    case "verde":        print("Es verde")
    case "azul":        print("Es azul")
    case _:        print("Color no reconocido")

#if-else: Agrega una acción alternativa si la condición es falsa.
if x > 0:     print("Positivo")
else:     print("No es positivo")

#if-elif-else: Evalúa múltiples condiciones en orden.
if x > 0:     print("Positivo")
elif x == 0:     print("Cero")
else:     print("Negativo")

"""1. Usar elif en lugar de múltiples if independientes
2. Evitar lógica redundante o ineficiente"""
# Redundante: if x > 10:     
if x % 2 == 0:         
    print("x es mayor que 10 y par")
# Optimizado: 
if x > 10 and x % 2 == 0:     
    print("x es mayor que 10 y par")





"""---------------------------------    Bucles For   ---------------------------------""" 

# Bucle for: permite iterar sobre una variable compleja - Listas o Tuplas)
for i in range(1,4):
    print(f"Esta es la vez {i} de este bucle for")

#bucles, técnicas y prácticas 

#2. Bucles. Permiten repetir un bloque de código varias veces.
#for: Itera sobre una secuencia (lista, cadena, rango, etc.).
for i in range(5):
    print(i)
#1. Iterar directamente sobre elementos
for nombre in nombres:
    print(nombre)

#2. Usar enumerate para obtener índice y valor
nombres = ["Ana", "Luis", "Pedro"]
for index, nombre in enumerate(nombres):
    print(f"Índice {index}: {nombre}")

#3. Usar zip para iterar sobre múltiples secuencias
nombres = ["Ana", "Luis", "Pedro"]
edades = [25, 30, 35]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

#4. Usar comprensiones de listas (list comprehensions)
# Con list comprehension
cuadrados = [x**2 for x in range(10)]

#5. Usar bucles anidados con cuidado
# Matriz bidimensional
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")

#6. Romper y continuar con break y continue
for numero in range(10):
    if numero == 5:
        break  # Detener el bucle cuando llega a 5
    if numero % 2 == 0:
        continue  # Saltar los números pares
    print(numero)

#7. Usar else con for
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    if numero == 6:  # No está en la lista
        print("Número encontrado")
        break
else:
    print("El número no está en la lista")

#8. Evitar modificar la secuencia durante la iteración. A menos que desees cambiarlos para manipularlos
# Buena práctica: trabajar sobre una copia
numeros = [1, 2, 3, 4, 5]
for numero in numeros[:]:
    if numero % 2 == 0:
        numeros.remove(numero)

#9. Usar generadores para grandes secuencias
# Generador para números pares
pares = (x for x in range(1000000) if x % 2 == 0)
# Iterar sobre el generador
for numero in pares:
    print(numero)

#10. Iterar sobre diccionarios
diccionario = {"a": 1, "b": 2, "c": 3}
# Iterar sobre claves y valores
for clave, valor in diccionario.items():

    print(f"Clave: {clave}, Valor: {valor}")

#11. Manejar excepciones dentro de un bucle
valores = [10, 20, 0, 30]
for valor in valores:
    try:
        resultado = 100 / valor
        print(f"100 / {valor} = {resultado}")
    except ZeroDivisionError:
        print("Error: división entre cero")

#12. Evitar bucles innecesarios
# Suma de elementos (ineficiente)
numeros = [1, 2, 3, 4, 5]
suma = 0
for numero in numeros:
    suma += numero

# Más eficiente
suma = sum(numeros)



"""---------------------------------    Bucle while    ---------------------------------""" 

# Bucle while: ejecuta una misma accion mientras una condicion se cumpla. Dejara de ejecutarse cuando la condicion se incumpla
i=0
while i<5:
    print(f"Esta es la vez {i} del bucle while")
    i+=1

#While, técnicas y prácticas 

#3. while: Repite un bloque de código mientras una condición sea verdadera.
i = 0
while i < 5:
    print(i)
    i += 1

#1. Establecer condiciones claras
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1

#2. Usar break para salir del bucle
while True:
    dato = input("Ingresa 'salir' para terminar: ")
    if dato == "salir":
        break
    print(f"Ingresaste: {dato}")

#3. Usar continue para saltar a la siguiente iteración
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue  # Saltar los números pares
    print(f"Número impar: {contador}")

#4. Usar else con while
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("Bucle terminado correctamente")

#5. Validar entradas del usuario

while True:
    edad = input("Ingresa tu edad (número positivo): ")
    if edad.isdigit() and int(edad) > 0:
        print(f"Edad válida: {edad}")
        break
    print("Entrada inválida, inténtalo de nuevo.")

#6. Crear bucles dependientes de estados
estado = "inicio"
while estado != "fin":
    if estado == "inicio":
        print("Juego iniciado")
        estado = "jugando"
    elif estado == "jugando":
        print("Estás jugando...")
        comando = input("Escribe 'fin' para salir: ")
        if comando == "fin":
            estado = "fin"

#7. Evitar bucles infinitos no controlados. Hacer bucle infinito controlado:
import time
tiempo = True
while tiempo:
    print("Procesando...")
    time.sleep(1)
    False

# Usa señales o condiciones externas para detener este tipo de bucles.
#8. Usar contadores como límite adicional
contador = 0
max_intentos = 5
while contador < max_intentos:
    print(f"Intento {contador + 1}")
    contador += 1

#9. Iterar sobre secuencias con índices
nombres = ["Ana", "Luis", "Pedro"]
indice = 0
while indice < len(nombres):
    print(nombres[indice])
    indice += 1

#10. Usar generadores o funciones dentro del bucle
def generador_numeros():
    num = 0
    while True:
        yield num
        num += 1
gen = generador_numeros()
while True:
    numero = next(gen)
    if numero > 10:
        break
    print(numero)

#11. Evitar cálculos costosos en la condición, realiza esos cálculos antes del bucle o una vez por iteración.
# Más eficiente
longitud = len(lista_grande)
while longitud > 1000:
    lista_grande.pop()
    longitud -= 1

#12. Controlar múltiples condiciones
a, b = 0, 10
while a < b and b > 5:
    print(f"a: {a}, b: {b}")
    a += 1
    b -= 1

#13. Usar el bucle while con estructuras de datos dinámicas
cola = [1, 2, 3, 4, 5]
while cola:
    elemento = cola.pop(0)  # Eliminar el primer elemento
    print(f"Procesando: {elemento}")




"""---------------------------------    control de bucles    ---------------------------------""" 

#Control de bucles técnicas y prácticas 

#4. Control de bucles. Permiten modificar el flujo dentro de un bucle.
#break: Termina un bucle antes de completarlo.
for i in range(10):
    if i == 5:
        break
    print(i)

#continue: Salta el resto del código en una iteración y pasa a la siguiente.
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

#else en bucles: Ejecuta un bloque de código cuando el bucle termina normalmente (sin un break).
for i in range(5):
    print(i)
else:
    print("Bucle completado")




"""---------------------------------    #Conceptos avanzados relacionados    ---------------------------------""" 

#1. Operadores ternarios: Un if resumido en una sola línea.
resultado = "Positivo" if x > 0 else "Negativo"

"""valor_si_condicion_verdadera if condicion else valor_si_condicion_falsa
Explicación:
condicion: Una expresión booleana que se evalúa como True o False.
valor_si_condicion_verdadera: Lo que se retorna si la condición es verdadera.
valor_si_condicion_falsa: Lo que se retorna si la condición es falsa."""

# Variable para ejemplo
edad = 18

# Usando el operador ternario para verificar si la persona es mayor de edad
estado = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(estado)  # Salida: "Mayor de edad"

"""1. Utilizar cuando la lógica es simple
2. Evitar ternarios anidados, que pueden hacer el código difícil de leer.
3. Usar ternarios para asignaciones dentro de expresiones
def obtener_descuento(precio):"""
#return precio * 0.9 if precio > 100 else precio

"""4. No usarlos para efectos secundarios (como imprimir, modificar estados).
5. Comprimir múltiples condiciones"""
# Asegúrate de que la condición sea fácilmente comprensible
resultado = "Aprobado" if 50 <= nota <= 100 else "Reprobado"
"""6. Evitar el uso excesivo de ternarios en funciones complejas con operadores lógico.
7. Usar ternarios para cambiar el flujo de control de manera directa"""
# Condicional simple para cambiar el flujo de control
accion = "Venta" if tipo == "producto" else "Alquiler"



"""---------------------------------    List comprehensions    ---------------------------------""" 

#2. List comprehensions: Sintaxis compacta para crear listas con bucles y condiciones.
cuadrados = [x**2 for x in range(10) if x % 2 == 0]

"""[expresión for item in iterable]
expresión: La operación que deseas realizar con cada item.
item: El elemento individual del iterable.
iterable: La secuencia sobre la que iteramos (como una lista, tupla o rango)."""

# Supongamos que necesitamos filtrar solo los números mayores a 5
# y luego obtener el cuadrado de esos números
numeros = [1, 2, 3, 6, 7, 8, 10]
resultados = [x**2 for x in numeros if x > 5]
print(resultados)  # Salida: [36, 49, 64, 100]

# Generar una lista de números al cuadrado
cuadrados = [x**2 for x in range(10)]
print(cuadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#2. Añadir condiciones con if.Puedes filtrar elementos añadiendo una condición if.
# Generar una lista de números pares
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]

#3. Usar if-else dentro de la expresión, como una condición ternaria para transformar elementos según una regla.
# Reemplazar números impares con 'Impar' y pares con su valor
resultado = [x if x % 2 == 0 else "Impar" for x in range(10)]
print(resultado)  # [0, 'Impar', 2, 'Impar', 4, 'Impar', 6, 'Impar', 8, 'Impar']

#4. Anidar bucles, como para trabajar con listas bidimensionales o generar combinaciones.
# Generar todas las combinaciones de dos listas
combinaciones = [(x, y) for x in range(3) for y in range(3)]
print(combinaciones)
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]: se ejecuta el primer for se ejecuta al principio y cuando acaba el segundo for

#5. Trabajar con estructuras bidimensionales, ideales para transformar o filtrar matrices.
# Transponer una matriz

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
print(transpuesta)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

#6. Aplicar funciones en cada elemento. Puedes usar funciones dentro de la expresión para transformar elementos.
# Convertir todos los nombres a mayúsculas
nombres = ["ana", "luis", "pedro"]
mayusculas = [nombre.upper() for nombre in nombres]
print(mayusculas)  # ['ANA', 'LUIS', 'PEDRO']

#7. Manejar entradas dinámicas, como manejar entradas del usuario o datos dinámicos.
# Filtrar números positivos ingresados por el usuario
datos = input("Ingresa números separados por espacios: ").split()
positivos = [int(x) for x in datos if int(x) > 0]
print(positivos)

#8. Trabajar con diccionarios y conjuntos, puedes usarlas para construir diccionarios y conjuntos.
# Crear un diccionario de números y sus cuadrados
cuadrados_dict = {x: x**2 for x in range(5)}
print(cuadrados_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Crear un conjunto de números pares
pares_set = {x for x in range(10) if x % 2 == 0}
print(pares_set)  # {0, 2, 4, 6, 8}

#9. Evitar comprensiones de listas excesivamente complejas
# Demasiado complejo (mala práctica)
resultados = [x**2 for x in range(10) if x % 2 == 0 if x > 2]
print(resultados)

# Alternativa más legible
resultados = []
for x in range(10):
    if x % 2 == 0 and x > 2:
        resultados.append(x**2)
print(resultados)

#10. Usar con generadores, si no necesitas almacenar todos los elementos generados en memoria
# Generador para números pares
pares = (x for x in range(10) if x % 2 == 0)
for par in pares:
    print(par)

#11. Combinarlas con otras funciones como map y filter
# Filtrar y transformar elementos
numeros = [-1, -2, 0, 1, 2]
positivos_cuadrados = [x**2 for x in filter(lambda x: x > 0, numeros)]
print(positivos_cuadrados)  # [1, 4]

#12. Procesar datos en una línea
# Normalizar cadenas
cadenas = ["  Python  ", "  es  ", "   genial "]
normalizadas = [cadena.strip().capitalize() for cadena in cadenas]
print(normalizadas)  # ['Python', 'Es', 'Genial']




"""---------------------------------    Expresiones generadora    ---------------------------------""" 

#Expresiones generadoras técnicas y practicas

"""3. Expresiones generadoras: Similar a las comprensiones de listas, pero generan valores uno a uno.
Sintaxis básica

generador = (expresión for elemento in iterable [if condición])"""

# Ejemplo básico: Crear un generador que produce números pares
pares = (x for x in range(10) if x % 2 == 0)
for numero in pares:
    print(numero)
# Salida: 0, 2, 4, 6, 8

#1. Usar expresiones generadoras para ahorro de memoria, si ocupas grandes colecciones de datos
# Generar números al cuadrado hasta 1 millón
cuadrados = (x**2 for x in range(1_000_000))
# Procesar solo los primeros 10
for _ in range(10):
    print(next(cuadrados))

#2. Trabajar con cadenas grandes, pueden procesar línea por línea sin cargar todo el archivo en memoria.
# Leer líneas de un archivo grande
lineas = (linea.strip() for linea in open("archivo_grande.txt"))
for linea in lineas:
    print(linea)  # Procesar cada línea

#3. Encadenar generadores para construir flujos de datos más complejos.
# Filtrar números pares y luego calcular sus cuadrados
pares = (x for x in range(20) if x % 2 == 0)
cuadrados = (x**2 for x in pares)
for cuadrado in cuadrados:
    print(cuadrado)

#4. Funciones, pueden pasarse directamente a funciones que esperan iterables, como sum, min, max, any, o all.
# Calcular la suma de números pares
suma_pares = sum(x for x in range(100) if x % 2 == 0)
print(suma_pares)

#5. Crear secuencias infinitas o flujos de datos que no tienen fin.
# Generar números impares infinitos
def numeros_impares():
    numero = 1
    while True:
        yield numero
        numero += 2
generador_impares = numeros_impares()
for _ in range(5):
    print(next(generador_impares))  # 1, 3, 5, 7, 9

#6. Usar con funciones como zip, enumerate, o itertools herramientas avanzadas de iteración.
import itertools
# Generar combinaciones de números
combinaciones = ((x, y) for x, y in itertools.product(range(3), range(3)) if x != y)
for combinacion in combinaciones:
    print(combinacion)

#7. Mezclar con expresiones condicionales. Puedes añadir condiciones complejas para filtrar elementos en los generadores.
# Generar solo números primos
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True
primos = (x for x in range(100) if es_primo(x))
print(list(primos))

#8. Optimizar pipelines de datos
# Procesar datos de un archivo y calcular estadísticas
valores = (float(linea) for linea in open("datos.txt") if linea.strip())
promedio = sum(valores) / 1_000_000  # Solo procesamos un millón de elementos
print(promedio)

#9. Controlar el flujo con islice, puedes tomar partes específicas del generador sin consumirlo completamente.
from itertools import islice
# Generar solo los primeros 5 elementos
pares = (x for x in range(100) if x % 2 == 0)
primeros_cinco = list(islice(pares, 5))
print(primeros_cinco)  # [0, 2, 4, 6, 8]

#10. Usar generadores en paralelo al mismo tiempo utilizando zip.
numeros = (x for x in range(5))
cuadrados = (x**2 for x in range(5))
for numero, cuadrado in zip(numeros, cuadrados):
    print(f"{numero} al cuadrado es {cuadrado}")

#11. Evitar sobreprocesamiento, evita usar operaciones que los consuman varias veces, agotan después de una iteración.
generador = (x**2 for x in range(10))

# Mala práctica: agota el generador
print(list(generador))  # [0, 1, 4, ..., 81]
print(list(generador))  # [] (el generador ya está vacío)



"""---------------------------------    Desempaquetado    ---------------------------------""" 

#Desempaquetado múltiple técnicas y prácticas 

"""4. Desempaquetado múltiple: Asignar múltiples valores de un iterable (lista, tupla o conjunto) a múltiples variables de una sola vez.    a, b, c = 1, 2, 3

1. Desempaquetado múltiple 
Sintaxis básica"""
a, b, c = [1, 2, 3]
print(a, b, c)  # Salida: 1 2 3 En este ejemplo: La lista [1, 2, 3] se desempaqueta en tres variables: a, b y c.

#2. Usar el operador * para capturar valores restantes en una sola variable.
a, *b, c = [1, 2, 3, 4, 5]
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

#3. Intercambio de valores sin variables temporales
a, b = 5, 10
a, b = b, a
print(a, b)  # Salida: 10 5

#4. Retornos múltiples de funciones como tupla, puedes desempaquetarlos directamente.
def calcular(a, b):
    return a + b, a * b
suma, producto = calcular(3, 4)
print(suma, producto)  # Salida: 7 12

#5. Desempaquetado de datos en bucles

# Lista de tuplas
pares = [(1, 'a'), (2, 'b'), (3, 'c')]
for numero, letra in pares:
    print(f"Número: {numero}, Letra: {letra}")

#6. Usar con diccionarios, desempaquetar las claves o valores de un diccionario.
diccionario = {'a': 1, 'b': 2, 'c': 3}
# Desempaquetar claves
for clave in diccionario:
    print(clave)
# Desempaquetar claves y valores
for clave, valor in diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")

#7. Desempaquetar anidado
datos = [(1, (2, 3)), (4, (5, 6))]
for a, (b, c) in datos:
    print(a, b, c) # Salida:  
# 1 2 3
# 4 5 6

#8. Validar tamaños al desempaquetar, para validar el número de elementos en una estructura.
numeros = [1, 2, 3]
if len(numeros) == 3:
    a, b, c = numeros
else:    print("La lista no tiene el tamaño correcto.")

#9. Ignorar valores con _: Cuando no necesitas usar ciertos valores, _ se usa como una convención para ignorarlos.
numeros = [10, 20, 30]
_, segundo, _ = numeros
print(segundo)  # Salida: 20

#10. Desempaquetar y reasignar valores. Puedes combinar el desempaquetado con reasignaciones.
a, b, c = 1, 2, 3
# Incrementar los valores
a, b, c = a + 1, b + 2, c + 3
print(a, b, c)  # Salida: 2 4 6

#11. Desempaquetar con zip para manejar listas paralelas.
nombres = ['Ana', 'Luis', 'Pedro']
edades = [25, 30, 35]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años.")

#12. Uso avanzado con listas dinámicas. Puedes usar desempaquetado con listas dinámicas de entrada.
entrada = input("Ingresa tres valores separados por espacio: ").split()
a, b, c = map(int, entrada)
print(f"Valores: {a}, {b}, {c}")

#13. Desempaquetar con * en asignaciones múltiples para combinar desempaquetado y reasignaciones de valores.
primero, *intermedios, ultimo = range(10)
print(primero, intermedios, ultimo) # Salida: 0 [1, 2, 3, 4, 5, 6, 7, 8] 9

#14. Manejar excepciones con desempaquetado. Usar desempaquetado en combinaciones con try para manejar datos con estructuras variables. Ejemplo:
datos = [1, 2]
try:
    a, b, c = datos
except ValueError:
    print("Error: La estructura no tiene suficientes elementos.")


#15. Desempaquetar con funciones lambda. Simplificar retornos complejos en funciones pequeñas.
# Lambda que retorna múltiples valores
f = lambda x: (x, x**2, x**3)
a, b, c = f(2)
print(a, b, c)  # Salida: 2 4 8




"""---------------------------------    Operadores combinados    ---------------------------------""" 

#Operadores combinados con estructuras: Usar operadores como in o not in dentro de bucles o condicionales."""
if "a" in "abc":
    print("Está presente")

#1. Operadores Lógicos. Combinar condiciones. Usa paréntesis para mayor claridad en condiciones complejas.
if (edad > 18 and ingresos > 30000) or (edad > 60 and ingresos > 20000):
    print("Cumple algún requisito.")

#2. Operadores Comparativos y Encadenamiento, evitar escribir varias condiciones repetitivas y condiciones redundantes 
x = 10
if 5 < x <= 20:
    print("El valor está en el rango.")

#3. Operador Asignación y combinados (+=, *=, etc.) útiles a actualizar valores dentro de estructuras bucles. Acumuladores
numeros = [1, 2, 3, 4, 5]
suma = 0
for numero in numeros:
    suma += numero  # Uso de operador combinado
print(suma)  # Salida: 15

#4. Uso del Operador Ternario con Condicionales: (condición ? valor_si_verdadero : valor_si_falso) 
edad = 17
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)

#5. Operadores de Pertenencia (in, not in), verificar si un elemento pertenece a una estructura (listas, tuplas o diccionarios).
usuarios_permitidos = ["admin", "editor", "viewer"]
usuario = "editor"
if usuario in usuarios_permitidos:
    print("Acceso concedido.")

#6. Operadores Bit a Bit en Condiciones Avanzadas para optimizacion de bajo nivel o procesamiento específico. Procesar permisos
PERMISO_LECTURA = 0b001
PERMISO_ESCRITURA = 0b010
PERMISO_EJECUCION = 0b100
usuario_permisos = 0b101  # Lectura y ejecución
if usuario_permisos & PERMISO_LECTURA:
    print("Tiene permiso de lectura.")

#7. Combinación de Bucles con Operadores de Pertenencia. Buscar elementos específicos
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero} es par.")

#8. Listas por Compresión con Operadores permiten integrar operadores dentro de bucles de forma compacta.
numeros = range(10)
pares = [x for x in numeros if x % 2 == 0]
print(pares)  # Salida: [0, 2, 4, 6, 8]


#9. Uso del Operador is para Comparaciones de Identidad para verificar si 2 variables apuntan al mismo objeto en memoria.
valor = None
if valor is None:
    print("El valor no está definido.")

#10. Combinar try-except con Operadores Lógicos. Manejar errores de forma limpia
try:
    numero = int(input("Ingresa un número: "))
    if numero > 0 and numero % 2 == 0:
        print("Número positivo y par.")
except ValueError:
    print("No ingresaste un número válido.")

#11. Operadores con Diccionarios para combinar operadores y estructuras como for o if. Verificar existencia de claves
config = {"modo": "oscuro", "idioma": "es"}
if "idioma" in config:
    print(f"Idioma configurado: {config['idioma']}")

#12. Optimizaciones con Generadores y Expresiones Lambda. Filtrar valores
numeros = range(10)
pares = (x for x in numeros if x % 2 == 0)
for par in pares:
    print(par)


"""---------------------------------    Rangos y secuencias    ---------------------------------""" 

#6. Uso avanzado de rangos y secuencias:
for i in range(5):
    print(i)  # Salida: 0, 1, 2, 3, 4

#1. El objeto range genera secuencias de números enteros, ideal para iteraciones. Usa range(start, stop, step) para personalizar el inicio, fin y el paso.
for i in range(1, 10, 2):
    print(i)  # Salida: 1, 3, 5, 7, 9

#2. Generar Listas o Tuplas con Rangos. Convertir rangos a listas para inicializar estructuras de datos rápidamente.
numeros = list(range(5))
print(numeros)  # Salida: [0, 1, 2, 3, 4]

#3. Iterar de Forma Inversa. El rango permite iterar en reversa fácilmente.
for i in range(10, 0, -1):
    print(i)  # Salida: 10, 9, 8, ..., 1

#4. Trabajar con Indices y Rangos. Combinar range con índices
frutas = ["manzana", "pera", "uva"]
for i in range(len(frutas)):
    print(f"{i}: {frutas[i]}")

# Es preferible usar enumerate para mayor claridad:
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")

#5. Crear Subrangos. Generar divisiones con pasos personalizados
for i in range(0, 100, 20):
    print(f"Procesando grupo desde {i} hasta {i+19}")

#6. Usar Rangos para Validar Secuencias. Los rangos pueden verificar si un valor pertenece a una secuencia.

if 7 in range(10):
    print("7 está dentro del rango.")  # Úsalo para simplificar condiciones.

#7. Crear Estructuras con Comprensiones de Listas
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # Salida: [0, 2, 4, 6, 8]

#8. Manejar Secuencias de Caracteres, puedes combinarlo con chr() y ord() para secuencias de caracteres.
for letra in range(ord('a'), ord('f') + 1):
    print(chr(letra))  # Salida: a, b, c, d, e, f Útil para alfabetos o validaciones específicas.

#9. Trabajar con Rangos Grandes. Iterar sin gastar memoria
for i in range(10**8, 10**8 + 5):
    print(i)  # Itera sin cargar toda la secuencia en memoria.

#10. Mezclar Rangos con Funciones Avanzadas. Usar zip para pares
rangos1 = range(5)
rangos2 = range(10, 15)
for a, b in zip(rangos1, rangos2):
    print(a, b)  # Salida: (0, 10), (1, 11), ...

#11. Filtrar Rangos. Usa funciones como filter para seleccionar elementos específicos.
impares = filter(lambda x: x % 2 != 0, range(10))
print(list(impares))  # Salida: [1, 3, 5, 7, 9]

#12. Números Aleatorios dentro de Rangos. Usar random con rangos
import random
print(random.choice(range(1, 101)))  # Número aleatorio entre 1 y 100

#13. Rellenar con Rangos
secuencia = [x % 3 for x in range(10)]
print(secuencia)  # Salida: [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]

#14. Usar Rangos con Formato Personalizado. Generar salidas formateadas
for i in range(1, 6):
    print(f"Producto {i}: precio ${(i * 10):.2f}")

#15. Rangos Multidimensionales. Trabajar con matrices
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()



# EXCEPCION
while True:
    # control de la excepcion
    try:
        number = int(input('Inserta un numero: '))
        break # si introduce un valor valido termina la ejecucion
    
    # si no introduce un valor valido, devuelve el error controlado
    except ValueError:
        print('Error! No ha insertado un valor valido. Intentelo de nuevo')


""" DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3."""

"""
conteo = 0
for i in range(56):
    if i % 2 ==0 and i % 3 ==0:
        print(f"Es multiplo de 2 y 3: {i}")
    elif i == 16:
        print("Este es el 16")
    elif i % 2 ==0:
        print(f"Es multiplo de 2: {i}")
    elif i % 3 == 0:
        print(f"Es Multiplo de 3: {i}")
    elif i == 16:
        print("Este es el 16")
    else: conteo += 1
print(f"Faltantes {conteo}")
"""
