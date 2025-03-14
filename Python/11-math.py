import math

"""El módulo math en Python proporciona funciones matemáticas estándar que permiten realizar operaciones comunes como 
cálculo de trigonometría, logaritmos, estadísticas, y otras funciones matemáticas fundamentales. Las funciones del 
módulo están implementadas en C, por lo que son muy rápidas y eficientes."""


"""Funciones del módulo math:"""

#1. Funciones de Potencias y Logaritmos Permiten trabajar con exponentes y logaritmos.

#math.exp(x) Devuelve , donde es la base de los logaritmos naturales (aproximadamente 2.718).
print(math.exp(2)) # 7.38905609893065 (e^2) 

#math.expm1(x) Devuelve , útil para valores pequeños de con más precisión.
print(math.expm1(0.0001)) # 0.00010000500016667084 

#math.log(x, base) Devuelve el logaritmo de x en la base dada. Si no se proporciona base, usa el logaritmo natural (base ).
print(math.log(100, 10)) # 2.0, porque 10^2 = 100 

#math.log1p(x) Devuelve el logaritmo natural de , útil para valores pequeños de .
print(math.log1p(0.0001)) # 9.999500033329732e-05 

#math.log2(x) Devuelve el logaritmo base 2 de x.
print(math.log2(8)) # 3.0, porque 2^3 = 8 

#math.log10(x) Devuelve el logaritmo base 10 de x.
print(math.log10(1000)) # 3.0, porque 10^3 = 1000 

#math.pow(x, y) Devuelve , similar a x ** y pero siempre devuelve un float.
print(math.pow(2, 3)) # 8.0, porque 2^3 = 8 

#math.sqrt(x) Devuelve la raíz cuadrada de x.
print(math.sqrt(16)) # 4.0 

#2. Funciones Trigonométricas: Trabajan con ángulos en radianes.

#math.sin(x) Devuelve el seno de x en radianes.
print(math.sin(math.pi/2)) # 1.0 

#math.cos(x) Devuelve el coseno de x en radianes.
print(math.cos(0)) # 1.0 

#math.tan(x) Devuelve la tangente de x en radianes.
print(math.tan(math.pi/4)) # 1.0 

#math.asin(x) Devuelve el arcoseno de x.
print(math.asin(1)) # 1.5707963267948966 (π/2) 

#math.acos(x) Devuelve el arcocoseno de x.
print(math.acos(0)) # 1.5707963267948966 (π/2) 

#math.atan(x) Devuelve el arcotangente de x.
print(math.atan(1)) # 0.7853981633974483 (π/4) 

#math.atan2(y, x) Devuelve el arcotangente de considerando cuadrantes.
print(math.atan2(1, 1)) # 0.7853981633974483 (π/4) 

#math.hypot(x, y) Calcula la hipotenusa de un triángulo rectángulo con lados x e y.
print(math.hypot(3, 4)) # 5.0 

#math.degrees(x) Convierte radianes a grados.
print(math.degrees(math.pi)) # 180.0 

#math.radians(x) Convierte grados a radianes.
print(math.radians(180)) # 3.141592653589793 


#3. Funciones de Redondeo y Enteros: math.ceil(x)

#Redondea x hacia arriba.
print(math.ceil(3.2)) # 4 

#math.floor(x) Redondea x hacia abajo.
print(math.floor(3.8)) # 3 

#math.trunc(x) Elimina la parte decimal de x.
print(math.trunc(3.8)) # 3 

#math.fabs(x) Devuelve el valor absoluto de x.
print(math.fabs(-5.3)) # 5.3 

#math.factorial(x) Devuelve el factorial de x.
print(math.factorial(5)) # 120 (5 * 4 * 3 * 2 * 1) 


#4. Funciones Combinatorias y MCD/ MCM

#math.comb(n, k) Devuelve el número de combinaciones de n elementos tomados de k en k.
print(math.comb(5, 2)) # 10 

#math.perm(n, k) Devuelve el número de permutaciones de n elementos tomados de k en k.
print(math.perm(5, 2)) # 20 

#math.gcd(x, y) Devuelve el máximo común divisor de x e y.
print(math.gcd(24, 18)) # 6 

#math.lcm(x, y) Devuelve el mínimo común múltiplo de x e y.
print(math.lcm(4, 6)) # 12 





"""El módulo math de Python no define clases específicas. Su enfoque principal está en las funciones matemáticas y 
constantes, y no en clases que encapsulen comportamientos o estados."""





"""Ahora las variables del modulo math. El módulo math en Python define varias variables son constantes matemáticas y 
valores predefinidos."""




"""Constantes del módulo math:"""

#math.pi. El valor de la constante pi (aproximadamente 3.14159).

#math.e. El valor de la constante e (aproximadamente 2.71828), la base del logaritmo natural.

#math.tau. El valor de la constante tau (aproximadamente 6.28318), que es igual a 2 * pi.

#math.inf. Representa el valor infinito positivo.

#math.nan. Representa "Not a Number" (NaN), que se utiliza para representar valores no definidos o resultados inválidos en operaciones matemáticas.



"""El módulo math en Python no define excepciones propias, pero algunas de sus funciones pueden generar excepciones 
estándar de Python bajo ciertas condiciones. Aquí están las excepciones más comunes que pueden ocurrir al usar el 
módulo math:"""

#ValueError. Puede ocurrir si se pasan argumentos incorrectos a algunas funciones. Por ejemplo:
#Si se intenta calcular la raíz cuadrada de un número negativo usando math.sqrt(), se lanzará un ValueError.
math.sqrt(-1) # ValueError: math domain error 

#DomainError
#Relacionada con funciones como math.log() o math.sqrt(), que no aceptan valores fuera de su dominio matemático (por ejemplo, logaritmo de un número negativo).

#OverflowError. Puede ocurrir si los cálculos en las funciones de math exceden el rango que puede manejar el sistema. Por ejemplo: Intentar calcular un número demasiado grande con math.exp().
math.exp(1000) # OverflowError 



"""El módulo math en Python no contiene submódulos. Es un módulo autónomo que proporciona funciones matemáticas de bajo 
nivel, como trigonometría, logaritmos, y constantes matemáticas, pero no organiza su funcionalidad en submódulos adicionales."""
