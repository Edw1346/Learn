import fractions

"""El módulo fractions de Python proporciona soporte para trabajar con fracciones (números racionales), representándolos 
como objetos de la clase Fraction. Esta clase permite realizar operaciones aritméticas con fracciones de manera precisa."""



"""Ahora todas, todas las Funciones del modulo fractions"""

#1. Fraction La principal función del módulo, que crea fracciones a partir de números enteros, cadenas o de otras fracciones. Ejemplo:
from fractions import Fraction # Crear una fracción a partir de enteros
frac1 = Fraction(3, 4) # Crear una fracción a partir de una cadena 
frac2 = Fraction("2/5") 
print(frac1) # 3/4 print(frac2) # 2/5 

#2. gcd(a, b) Calcula el máximo común divisor de dos números. Aunque no es directamente parte de la clase Fraction, se puede usar para obtener el GCD de los numeradores y denominadores de las fracciones. Ejemplo:
from fractions import gcd 
print(gcd(12, 15)) # 3 

#3. limit_denominator(max_denominator=1000000) Devuelve una fracción equivalente con el denominador más pequeño posible, no mayor que max_denominator. Este método se utiliza para aproximar una fracción a una forma más simple. Ejemplo:
frac = Fraction(355, 113) 
frac_aprox = frac.limit_denominator(10) 
print(frac_aprox) # 22/7 

#4. from_float(f) Convierte un número de punto flotante en una fracción. Ejemplo:
frac = Fraction.from_float(0.75)
print(frac) # 3/4 

#5. from_decimal(d) Convierte un número decimal (Decimal) en una fracción. Ejemplo:
from decimal import Decimal 
from fractions import Fraction 
d = Decimal('0.5') 
frac = Fraction.from_decimal(d) 
print(frac) # 1/2 

#6. as_integer_ratio() Devuelve una fracción equivalente a un número de punto flotante como una tupla de dos enteros (numerador, denominador). Ejemplo:
frac = Fraction(3, 4) 
print(frac.as_integer_ratio()) # (3, 4) 

#7. __abs__() Devuelve el valor absoluto de la fracción. Ejemplo:
frac = Fraction(-3, 4) 
print(abs(frac)) # 3/4 

#8. __add__() Realiza la suma entre fracciones o entre una fracción y un número (entero o flotante). Ejemplo:
frac1 = Fraction(1, 2) 
frac2 = Fraction(2, 3) 
print(frac1 + frac2) # 7/6 

#9. __sub__() Realiza la resta entre fracciones o entre una fracción y un número (entero o flotante). Ejemplo:
frac1 = Fraction(5, 6) 
frac2 = Fraction(1, 3) 
print(frac1 - frac2) # 1/2 

#10. __mul__() Realiza la multiplicación entre fracciones o entre una fracción y un número (entero o flotante). Ejemplo:
frac1 = Fraction(1, 2) 
frac2 = Fraction(2, 3)
print(frac1 * frac2) # 1/3 

#11. __truediv__() Realiza la división entre fracciones o entre una fracción y un número (entero o flotante). Ejemplo:
frac1 = Fraction(1, 2) 
frac2 = Fraction(3, 4) 
print(frac1 / frac2) # 2/3 

#12. __floordiv__() Realiza la división entera entre fracciones. Ejemplo:
frac1 = Fraction(5, 2) 
frac2 = Fraction(3, 4) 
print(frac1 // frac2) # 3 

#13. __mod__() Devuelve el residuo de la división entre fracciones. Ejemplo:
frac1 = Fraction(5, 2)
frac2 = Fraction(3, 4) 
print(frac1 % frac2) # 1/4 

#14. __pow__()
#Realiza la potenciación entre fracciones. Ejemplo:
frac = Fraction(2, 3) 
print(frac ** 2) # 4/9 

#15. __neg__()
#Devuelve el negativo de la fracción. Ejemplo:
frac = Fraction(1, 2) 
print(-frac) # -1/2 

#16. __pos__() Devuelve la misma fracción (pero explícitamente positiva). Ejemplo:
frac = Fraction(-1, 2)
print(+frac) # -1/2 

#17. __eq__() Compara si dos fracciones son iguales. Ejemplo:
frac1 = Fraction(1, 2)
frac2 = Fraction(2, 4) 
print(frac1 == frac2) # True 

#18. __lt__() Compara si una fracción es menor que otra. Ejemplo:
frac1 = Fraction(1, 2)
frac2 = Fraction(2, 3) 
print(frac1 < frac2) # True 

#19. __le__() Compara si una fracción es menor o igual que otra. Ejemplo: 
frac1 = Fraction(1, 2) 
frac2 = Fraction(2, 3)
print(frac1 <= frac2) # True 

#20. __gt__() Compara si una fracción es mayor que otra. Ejemplo:
frac1 = Fraction(3, 4) 
frac2 = Fraction(1, 2) 
print(frac1 > frac2) # True 

#21. __ge__() Compara si una fracción es mayor o igual que otra. Ejemplo:
frac1 = Fraction(3, 4) 
frac2 = Fraction(1, 2) 
print(frac1 >= frac2) # True 




"""El módulo fractions de Python tiene principalmente una clase:"""

#1. Fraction
#La clase Fraction es la principal clase del módulo y se utiliza para representar números racionales como fracciones exactas (numerador/denominador). Permite realizar operaciones matemáticas, como suma, resta, multiplicación, y división, con fracciones y obtener resultados exactos sin pérdida de precisión.

#Métodos y atributos clave de la clase Fraction:
#numerator: Retorna el numerador de la fracción.
#denominator: Retorna el denominador de la fracción.
#__numerator__ y __denominator__: Métodos para acceder al numerador y denominador internamente.
#limit_denominator(max_denominator=1000000): Devuelve una fracción equivalente con el denominador más pequeño posible (no mayor que max_denominator).
#from_float(f): Convierte un número de punto flotante en una fracción.
#from_decimal(d): Convierte un número decimal (Decimal) en una fracción.
#as_integer_ratio(): Devuelve la fracción como una tupla de enteros (numerador, denominador). Ejemplo de uso de la clase Fraction:
from fractions import Fraction # Crear una fracción a partir de dos números enteros
frac1 = Fraction(3, 4) 
print(frac1) # 3/4 # Crear una fracción a partir de una cadena
frac2 = Fraction("2/3") 
print(frac2) # 2/3 # Operaciones con fracciones
result = frac1 + frac2 
print(result) # 17/12 # Limitar el denominador de una fracción 
frac = Fraction(22, 7) 
frac_limited = frac.limit_denominator(10)
print(frac_limited) # 22/7 (ya es el límite más cercano con denominador <= 10) # Convertir un flotante a fracción 
frac_from_float = Fraction.from_float(0.75) 
print(frac_from_float) # 3/4 # Obtener el numerador y denominador 
print(frac1.numerator) # 3 
print(frac1.denominator) # 4 

#Atributos importantes de la clase Fraction:
#numerator: Accede al numerador de la fracción.
#denominator: Accede al denominador de la fracción.
#limit_denominator(): Permite aproximar la fracción con un denominador más pequeño.

#2. gcd(a, b) (función no estática) Aunque no es una clase como tal, el gcd (máximo común divisor) es una función dentro del módulo fractions que es útil para trabajar con fracciones, ya que se utiliza para calcular el GCD de los numeradores y denominadores. Ejemplo:
from fractions import gcd
print(gcd(12, 15)) # 3 






"""El módulo fractions no tiene variables globales predefinidas como tal. Sin embargo, hay algunos valores y constantes que 
puedes encontrar útiles cuando trabajas con fracciones."""

#1. gcd
#La función gcd(a, b) es otra "entidad" del módulo fractions, que se utiliza para calcular el máximo común divisor de dos números, y aunque no es una variable, puede ser útil para ciertos cálculos relacionados con fracciones. Ejemplo:
from fractions import gcd 
print(gcd(12, 15)) # 3 

#Variables importantes dentro del módulo fractions:
#No existen variables globales predefinidas (como PI o E en otros módulos), ya que el módulo fractions se enfoca en las operaciones de fracciones, y su funcionamiento depende principalmente de la clase Fraction y las funciones asociadas.





"""Ahora las constantes del modulo fractions"""
#El módulo fractions de Python no contiene constantes predefinidas como otros módulos (por ejemplo, math.pi o math.e). Sin embargo, hay algunos comportamientos y valores que puedes considerar constantes en el contexto de trabajar con fracciones. 

#1. Fraction(0)
#Una fracción representando el número cero. Aunque no es una constante predefinida, puedes usar esta fracción en tu código como una forma de representar el cero de manera precisa. Ejemplo:
from fractions import Fraction 
zero = Fraction(0) 
print(zero) # 0 

#2. Fraction(1) Similar al caso de Fraction(0), Fraction(1) representa el número uno de manera exacta como una fracción. Ejemplo:
one = Fraction(1) 
print(one) # 1 

#3. Fracciones como "Constantes"
#Cuando trabajas con fracciones, las fracciones que representan valores comunes (como Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), etc.) pueden ser usadas como constantes en tus programas. Ejemplo:
half = Fraction(1, 2)
third = Fraction(1, 3) 
quarter = Fraction(1, 4) 
print(half, third, quarter) # 1/2 1/3 1/4 



"""El módulo fractions de Python maneja algunas excepciones relacionadas con las operaciones que involucran fracciones. """

#1. ZeroDivisionError
#Esta excepción se lanza cuando intentas crear una fracción con un denominador igual a cero, lo que no es matemáticamente válido. Ejemplo:
from fractions import Fraction 
try:
    frac = Fraction(1, 0) # Intentar crear una fracción con denominador 0 
except ZeroDivisionError as e: 
    print(f"Error: {e}") # Error: Fraction(1, 0) is undefined 

#2. ValueError
#Esta excepción se lanza cuando intentas crear una fracción a partir de un valor que no puede ser interpretado como un número entero o una cadena en formato válido de fracción. Ejemplo:
from fractions import Fraction
try:
    frac = Fraction("1/abc") # Cadena no válida 
except ValueError as e: 
    print(f"Error: {e}") # Error: invalid literal for int() with base 10: 'abc' 

#3. TypeError
#Esta excepción se lanza cuando intentas realizar operaciones entre tipos de datos que no son compatibles con las fracciones. Por ejemplo, intentar sumar una fracción con un tipo de dato no numérico. Ejemplo:
from fractions import Fraction
try: 
    frac = Fraction(1, 2) + "string" # Intentando sumar una fracción con una cadena 
except TypeError as e: 
    print(f"Error: {e}") # Error: unsupported operand type(s) for +: 'Fraction' and 'str' 


""""El módulo fractions en Python no tiene submódulos específicos. Es un módulo autónomo y no contiene módulos internos 
"adicionales como submódulos que se carguen por separado."""
