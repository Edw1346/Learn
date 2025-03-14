import decimal 

"""El módulo decimal en Python se usa para realizar cálculos con números decimales de alta precisión, evitando errores 
de redondeo que ocurren con los float."""



"""Ahora todas, todas las Funciones del modulo decimal"""

#1. Creación y configuración
#getcontext() – Obtiene el contexto actual
from decimal import getcontext 
contexto = getcontext() 
print(contexto.prec) # Muestra la precisión actual (por defecto 28) 

#setcontext(context) – Establece un contexto personalizado
from decimal import setcontext, Context 
nuevo_contexto = Context(prec=10) # Configura 10 dígitos de precisión 

setcontext(nuevo_contexto) 
print(getcontext().prec) # 10 

#localcontext([context]) – Crea un contexto temporal
from decimal import localcontext, Decimal 
with localcontext() as ctx:
    ctx.prec = 5 
    print(Decimal("1.123456") + Decimal("2.654321")) # 3.7778 (5 dígitos de precisión) 


#2. Creación de números decimales
#Decimal(value) – Crea un número decimal
from decimal import Decimal
num = Decimal("1.1") # Evita errores de precisión de float 
print(num) # 1.1 


#3. Operaciones matemáticas
#decimal.getcontext().power(x, y) – Potencia exacta
from decimal import Decimal, getcontext 
getcontext().prec = 6 
print(Decimal("2").__pow__(3)) # 2³ = 8 

#decimal.getcontext().sqrt(x) – Raíz cuadrada exacta
print(Decimal("16").sqrt()) # 4.0 

#decimal.getcontext().exp(x) – Exponencial (e^x)
print(Decimal("1").exp()) # e^1 ≈ 2.71828 

#decimal.getcontext().ln(x) – Logaritmo natural (base e)
print(Decimal("10").ln()) # ln(10) ≈ 2.30258 

#decimal.getcontext().log10(x) – Logaritmo base 10
print(Decimal("100").log10()) # log10(100) = 2 

#decimal.getcontext().logb(x) – Logaritmo base 2 (binario)
print(Decimal("8").logb()) # log2(8) = 3 

#decimal.getcontext().fma(a, b, c) – Multiplicación y suma en un solo paso
print(Decimal("2").fma(Decimal("3"), Decimal("4"))) # (2×3) + 4 = 10 


#4. Comparaciones y redondeo
#decimal.getcontext().max(x, y) – Máximo de dos decimales
print(Decimal("2.5").max(Decimal("3.1"))) # 3.1 

#decimal.getcontext().min(x, y) – Mínimo de dos decimales
print(Decimal("2.5").min(Decimal("3.1"))) # 2.5 

#decimal.getcontext().max_mag(x, y) – Mayor en valor absoluto
print(Decimal("-5").max_mag(Decimal("3"))) # -5 porque | -5 | > | 3 | 

#decimal.getcontext().min_mag(x, y) – Menor en valor absoluto
print(Decimal("-5").min_mag(Decimal("3"))) # 3 porque | 3 | < | -5 | 

#decimal.getcontext().abs(x) – Valor absoluto
print(Decimal("-10").abs()) # 10 

#decimal.getcontext().copy_abs(x) – Copia con valor absoluto
print(Decimal("-7.2").copy_abs()) # 7.2 

#decimal.getcontext().copy_negate(x) – Invierte el signo
print(Decimal("5.5").copy_negate()) # -5.5 


#5. Conversión y formato
#decimal.getcontext().to_integral_value(x) – Redondea a entero
print(Decimal("4.9").to_integral_value()) # 5 

#decimal.getcontext().to_integral_exact(x) – Redondeo exacto a entero
print(Decimal("3.7").to_integral_exact()) # 4 


#6. Otras funciones útiles
#decimal.getcontext().quantize(x, y) – Ajusta la precisión de un número
num = Decimal("3.14159") 
print(num.quantize(Decimal("0.01"))) # 3.14 (redondeado a 2 decimales) 

#decimal.getcontext().remainder_near(x, y) – Resto con menor distancia
print(Decimal("10.5").remainder_near(Decimal("3"))) # 1.5 (porque 10.5 ≈ 3×3 + 1.5) 

#decimal.getcontext().scaleb(x, n) – Escala el número (x * 10^n)
print(Decimal("2.5").scaleb(3)) # 2500 (2.5 × 10³) 





"""El módulo decimal en Python tiene una clase principal llamada Decimal, que se utiliza para representar y trabajar con 
números decimales de alta precisión. También incluye una clase para definir el contexto de los cálculos, que es Context, 
y BasicContext. A continuación te explico cada una con ejemplos:"""

#1. Decimal
#La clase Decimal es la más utilizada y representa números decimales. Proporciona métodos para realizar operaciones 
# aritméticas con una alta precisión y exactitud. Ejemplo de uso básico de Decimal
from decimal import Decimal # Crear un número Decimal 
num = Decimal("10.123")
print(num) # 10.123 

#Métodos comunes de Decimal
Decimal.is_zero(): #Devuelve True si el número es cero.
num = Decimal("0.0") 
print(num.is_zero()) # True 

Decimal.sqrt(): #Calcula la raíz cuadrada.
num = Decimal("16") 
print(num.sqrt()) # 4.0 

Decimal.quantize(): #Redondea el número a una cantidad específica de decimales.
num = Decimal("3.14159") 
print(num.quantize(Decimal("0.01"))) # 3.14 


#2. Context
#La clase Context se usa para definir el contexto en el que se hacen las operaciones decimales, como la precisión y el redondeo. Ejemplo de uso de Context
from decimal import Context # Crear un contexto con 5 dígitos de precisión 
contexto = Context(prec=5) 
print(contexto.prec) # 5 

#Context.prec: Define la precisión (número de dígitos significativos).
#Context.Emax: Define el exponente máximo permitido.
#Context.Emin: Define el exponente mínimo permitido.


#3. BasicContext
#BasicContext es una subclase de Context que tiene valores predeterminados para realizar operaciones con números decimales. Ejemplo de uso de BasicContext
from decimal import BasicContext 
contexto_basico = BasicContext() 
print(contexto_basico.prec) # 28 (precisión predeterminada) 

#Decimal: Usado para representar números decimales y realizar operaciones con alta precisión.
#Context: Define el contexto de cálculos decimales (precisión, redondeo, etc.).
#BasicContext: Subclase que proporciona un contexto con configuraciones predeterminadas.



"""El módulo decimal no tiene variables predefinidas en el sentido tradicional de variables globales o constantes. Sin 
"embargo, contiene algunas configuraciones que afectan cómo se manejan los cálculos dentro del módulo, que se pueden "
considerar "variables" de configuración o propiedades del contexto decimal."""

#Aquí están las configuraciones clave del contexto y las variables relacionadas:

#1. decimal.getcontext()
#La función getcontext() devuelve el contexto actual, que incluye varias variables o configuraciones relacionadas con la precisión y el redondeo de los cálculos decimales.
#Propiedades del contexto (Context)
#prec: La precisión (número de dígitos significativos) que se usa en las operaciones decimales. Ejemplo:
from decimal import getcontext 
contexto = getcontext() 
print(contexto.prec) # Muestra la precisión actual 

#Emax: El exponente máximo que se permite en una operación decimal. Ejemplo: 
print(getcontext().Emax) # Muestra el valor máximo de exponente 

#Emin: El exponente mínimo que se permite en una operación decimal. Ejemplo: 
print(getcontext().Emin) # Muestra el valor mínimo de exponente 

#rounding: El método de redondeo utilizado en los cálculos decimales. Los valores posibles incluyen ROUND_HALF_UP, ROUND_DOWN, etc. Ejemplo: 
print(getcontext().rounding) # Muestra el tipo de redondeo utilizado 

#flags: Un diccionario que almacena información sobre el estado de las excepciones de cálculo (por ejemplo, si ocurrió un desbordamiento o una división por cero). Ejemplo: 
print(getcontext().flags) # Muestra el estado de las banderas de excepciones 

#traps: Un diccionario que define qué excepciones deben atraparse en los cálculos decimales. Ejemplo: 
print(getcontext().traps) # Muestra las excepciones que serán atrapadas 


#2. Variables de contexto globales
#Aunque no son variables por sí mismas, el contexto también puede ser configurado a nivel global con el uso de setcontext() para establecer un nuevo contexto para los cálculos decimales.
#setcontext(context): Establece un nuevo contexto global, donde context es una instancia de Context o BasicContext.  Ejemplo: 
from decimal import Context, setcontext 
nuevo_contexto = Context(prec=10, Emax=999, Emin=-999) 
setcontext(nuevo_contexto) 




"""El módulo decimal en Python no tiene constantes predefinidas como tal (en el sentido de valores fijos como π o e). 
Sin embargo, puedes crear y usar números constantes con precisión decimales si lo deseas. Por ejemplo, puedes crear 
constantes como π (pi) o e de manera precisa utilizando el módulo decimal:"""

#Ejemplos de constantes de precisión decimal
#π (pi): Puedes usar el valor de pi de manera precisa con Decimal.
from decimal import Decimal, getcontext 
getcontext().prec = 50 # Establecer una precisión alta 

pi = Decimal('3.141592653589793238462643383279502884197169399375105820974944') 
print(pi) # 3.141592653589793238462643383279502884197169399375105820974944 

#e (número de Euler): Puedes crear una constante para e con la misma precisión.
from decimal import Decimal, getcontext 
getcontext().prec = 50 # Establecer una precisión alta 
e = Decimal('2.718281828459045235360287471352662497757247093699959574966967') 
print(e) # 2.718281828459045235360287471352662497757247093699959574966967 




"""El módulo decimal en Python define algunas excepciones que se utilizan para manejar errores relacionados con cálculos 
decimales. Estas excepciones son específicas de las operaciones realizadas con el tipo Decimal y están relacionadas 
principalmente con situaciones de precisión, redondeo y cálculo inválido."""

#1. DecimalException
#Es la excepción base para todas las excepciones relacionadas con el módulo decimal. La mayoría de las otras excepciones heredan de esta Ejemplo:
from decimal import Decimal, DecimalException 
try: 
    raise DecimalException("Error en operación decimal") 
except DecimalException as e: 
    print(f"Se produjo un error: {e}") 

#2. DivisionByZero
#Se lanza cuando hay una división por cero en una operación decimal. Ejemplo: 
from decimal import Decimal, DivisionByZero 
try: 
    result = Decimal('10') / Decimal('0') 
except DivisionByZero as e: 
    print("Error: División por cero") 

#3. InvalidOperation
#Se lanza cuando una operación no es válida, como por ejemplo, dividir un número decimal por cero, o hacer una operación inválida como tomar la raíz cuadrada de un número negativo. Ejemplo:
from decimal import Decimal, InvalidOperation 
try: 
    result = Decimal("1.23") / Decimal("0") 
except InvalidOperation as e:
    print("Operación inválida") 

#4. Overflow
#Se lanza cuando una operación produce un resultado que excede el límite de la precisión que el contexto puede manejar. Ejemplo:
from decimal import Decimal, Overflow
try: 
    result = Decimal('1e1000') * Decimal('1e1000') 
except Overflow as e: 
    print("Error: Desbordamiento (Overflow)") 

#5. Underflow
#Se lanza cuando una operación produce un resultado demasiado pequeño para ser representado, es decir, debajo del límite mínimo de precisión en el contexto decimal. Ejemplo:
from decimal import Decimal, Underflow
try: 
    result = Decimal('1e-1000') 
except Underflow as e: 
    print("Error: Subdesbordamiento (Underflow)") 

#6. Clamped
#Se lanza cuando un valor se ajusta debido a que no puede representarse con la precisión establecida, es decir, se recorta para cumplir con el límite de precisión. Ejemplo:
from decimal import Decimal, Clamped
try:
    result = Decimal("123.4567890123456789") # Dependiendo de la precisión del contexto, puede ser "clamp" 
except Clamped as e: 
    print("Error: El valor fue recortado por precisión") 

#7. Rounded
#Se lanza cuando una operación produce un resultado que ha sido redondeado para ajustarse a la precisión definida. Ejemplo:
from decimal import Decimal, Rounded
getcontext().prec = 5 # Redondear a 5 dígitos 
try: 
    result = Decimal("1.1234567").sqrt() # La raíz cuadrada será redondeada
except Rounded as e: 
    print("Error: El valor fue redondeado") 

#DecimalException: Excepción base para todas las excepciones decimales.
#DivisionByZero: Error de división por cero.
#InvalidOperation: Operación inválida, como dividir entre cero o raíces cuadradas de números negativos.
#Overflow: Exceso en los valores que superan la capacidad de la precisión decimal.
#Underflow: Valores demasiado pequeños para ser representados correctamente.
#Clamped: Los valores se ajustan o recortan debido a la falta de suficiente precisión.
#Rounded: Los valores se redondean debido a la precisión configurada.



"""El módulo decimal no contiene submódulos. Todo el contenido de este módulo, como las clases (Decimal, Context), las 
excepciones, y las funciones, se encuentra directamente en el propio módulo. No está dividido en submódulos adicionales. 
Sin embargo, algunas funcionalidades del módulo pueden ser configuradas o extendidas a través de objetos como Context, 
y hay funciones que permiten modificar el comportamiento global del módulo, como getcontext() y setcontext(). Pero no 
existen submódulos dentro de decimal."""
