import numpy

"""El módulo numpy es una biblioteca de Python que proporciona soporte para trabajar con arreglos (arrays) multidimensionales 
y matrices, junto con una amplia colección de funciones matemáticas para operar sobre estos arreglos. Es esencial para la 
computación científica en Python y se utiliza en tareas de álgebra lineal, estadísticas, procesamiento de señales, etc."""

#Características principales de numpy:
#Arreglos multidimensionales (ndarray): numpy introduce un tipo de objeto llamado ndarray que permite almacenar y manipular datos en forma de arreglos multidimensionales (listas anidadas). Es mucho más eficiente que las listas estándar de Python.
#Funciones matemáticas y estadísticas: numpy tiene muchas funciones optimizadas para realizar operaciones sobre arreglos, como suma, resta, multiplicación, estadísticas, álgebra lineal, transformaciones, entre otras.
#Operaciones vectorizadas: Puedes realizar operaciones sobre arreglos sin necesidad de escribir bucles, ya que numpy optimiza las operaciones internamente.
#Compatibilidad con otros paquetes: numpy se integra bien con otras bibliotecas de Python como pandas, matplotlib y scipy.

#Ejemplo básico de uso:
import numpy as n
p # Crear un arreglo unidimensional 
arr = np.array([1, 2, 3, 4]) # Realizar una operación sobre el arreglo
arr_sum = arr + 10 
print(arr_sum) # [11 12 13 14] 
# Crear un arreglo bidimensional (matriz) 
matrix = np.array([[1, 2], [3, 4]]) 
print(matrix) # Operación con matrices
matrix_sum = matrix + 5 
print(matrix_sum) # [[6 7] [8 9]] 




"""Funciones que abarcan diversas áreas de matemáticas, álgebra lineal, estadísticas, operaciones sobre arreglos, y más. """

#1. numpy.abs() Devuelve el valor absoluto de cada elemento del arreglo. Ejemplo:
arr = np.array([-1, -2, 3]) 
print(np.abs(arr)) # [1 2 3] 

#2. numpy.add() Realiza la suma de dos arreglos o valores. Ejemplo:
arr1 = np.array([1, 2, 3]) 
arr2 = np.array([4, 5, 6]) 
print(np.add(arr1, arr2)) # [5 7 9] 

#3. numpy.all() Devuelve True si todos los elementos del arreglo son verdaderos (no cero). También puede usarse en una dimensión específica. Ejemplo:
arr = np.array([1, 1, 1])
print(np.all(arr)) # True 

#4. numpy.any() Devuelve True si al menos uno de los elementos del arreglo es verdadero (no cero). Ejemplo:
arr = np.array([0, 1, 0]) 
print(np.any(arr)) # True 

#5. numpy.append() Añade valores al final de un arreglo. Ejemplo:
arr = np.array([1, 2, 3])
print(np.append(arr, [4, 5])) # [1 2 3 4 5] 

#6. numpy.around() Redondea los valores de un arreglo al número de decimales especificado. Ejemplo:
arr = np.array([1.234, 5.678, 9.012]) 
print(np.around(arr, 1)) # [1.2 5.7 9.0] 

#7. numpy.argmax() Devuelve el índice del valor máximo en un arreglo. Ejemplo:
arr = np.array([1, 5, 3])
print(np.argmax(arr)) # 1 (índice del valor 5) 

#8. numpy.argmin() Devuelve el índice del valor mínimo en un arreglo. Ejemplo:
arr = np.array([1, 5, 3]) 
print(np.argmin(arr)) # 0 (índice del valor 1) 

#9. numpy.array() Crea un arreglo ndarray a partir de una lista o una lista anidada. Ejemplo:
arr = np.array([1, 2, 3]) 
print(arr) # [1 2 3] 

#10. numpy.zeros() Crea un arreglo lleno de ceros. Ejemplo:
arr = np.zeros((2, 3))
print(arr) # [[0. 0. 0.] [0. 0. 0.]] 

#11. numpy.ones() Crea un arreglo lleno de unos. Ejemplo:
arr = np.ones((2, 3))
print(arr) # [[1. 1. 1.] [1. 1. 1.]] 

#12. numpy.arange() Devuelve un arreglo con valores en un rango específico. Ejemplo:
arr = np.arange(0, 10, 2) 
print(arr) # [0 2 4 6 8] 

#13. numpy.linspace() Devuelve valores equidistantes entre dos números, de acuerdo con un número de puntos especificado. Ejemplo:
arr = np.linspace(0, 10, 5) 
print(arr) # [ 0. 2.5 5. 7.5 10. ] 

#14. numpy.reshape() Cambia la forma de un arreglo sin cambiar sus datos. Ejemplo:
arr = np.array([1, 2, 3, 4, 5, 6]) 
print(np.reshape(arr, (2, 3))) # [[1 2 3] [4 5 6]] 

#15. numpy.ravel() Convierte un arreglo multidimensional en un arreglo unidimensional. Ejemplo:
arr = np.array([[1, 2], [3, 4]])
print(np.ravel(arr)) # [1 2 3 4] 

#16. numpy.transpose() Devuelve la transpuesta de un arreglo multidimensional. Ejemplo:
arr = np.array([[1, 2], [3, 4]])
print(np.transpose(arr)) # [[1 3] [2 4]] 

#17. numpy.dot() Realiza el producto punto entre dos arreglos. Ejemplo:
arr1 = np.array([1, 2]) 
arr2 = np.array([3, 4]) 
print(np.dot(arr1, arr2)) # 11 (1*3 + 2*4) 

#18. numpy.sum() Devuelve la suma de todos los elementos en un arreglo. Ejemplo:
arr = np.array([1, 2, 3])
print(np.sum(arr)) # 6 

#19. numpy.mean() Devuelve el valor medio (promedio) de los elementos en un arreglo. Ejemplo:
arr = np.array([1, 2, 3, 4]) 
print(np.mean(arr)) # 2.5 

#20. numpy.std() Devuelve la desviación estándar de los elementos en un arreglo. Ejemplo:
arr = np.array([1, 2, 3, 4]) 
print(np.std(arr)) # 1.118 

#21. numpy.median() Devuelve la mediana de los elementos en un arreglo. Ejemplo:
arr = np.array([1, 3, 2]) 
print(np.median(arr)) # 2.0 

#22. numpy.min() Devuelve el valor mínimo de un arreglo. Ejemplo:
arr = np.array([1, 2, 3])
print(np.min(arr)) # 1 

#23. numpy.max() Devuelve el valor máximo de un arreglo. Ejemplo:
arr = np.array([1, 2, 3]) 
print(np.max(arr)) # 3 

#24. numpy.sort() Devuelve una copia ordenada del arreglo. Ejemplo:
arr = np.array([3, 1, 2]) 
print(np.sort(arr)) # [1 2 3] 

#25. numpy.copy() Crea una copia de un arreglo. Ejemplo:
arr = np.array([1, 2, 3]) 
arr_copy = np.copy(arr) 
print(arr_copy) # [1 2 3] 

#26. numpy.unique() Devuelve los elementos únicos de un arreglo. Ejemplo:
arr = np.array([1, 2, 2, 3, 3, 3])
print(np.unique(arr)) # [1 2 3] 

#27. numpy.concatenate() Concatena varios arreglos a lo largo de un eje especificado. Ejemplo:
arr1 = np.array([1, 2]) 
arr2 = np.array([3, 4]) 
print(np.concatenate([arr1, arr2])) # [1 2 3 4] 

#28. numpy.vstack() Apila arreglos verticalmente (por filas). Ejemplo:
arr1 = np.array([1, 2]) 
arr2 = np.array([3, 4]) 
print(np.vstack([arr1, arr2])) # [[1 2] [3 4]] 

#29. numpy.hstack() Apila arreglos horizontalmente (por columnas). Ejemplo:
arr1 = np.array([1, 2]) 
arr2 = np.array([3, 4]) 
print(np.hstack([arr1, arr2])) # [1 2 3 4] 

#30. numpy.linspace() Genera un arreglo con valores igualmente espaciados entre dos valores especificados. Ejemplo:
arr = np.linspace(0, 10, 5) 
print(arr) # [ 0. 2.5 5. 7.5 10. ] 


"""El módulo numpy tiene algunas clases clave que son fundamentales para trabajar con arreglos y operaciones científicas. """

#1. numpy.ndarray
#Esta es la clase principal de numpy. Un ndarray (N-dimensional array) es un arreglo multidimensional que permite almacenar elementos de tipo homogéneo (todos los elementos deben ser del mismo tipo de datos). Ejemplo:
# Crear un ndarray de una dimensión
arr = np.array([1, 2, 3, 4]) 
print(type(arr)) # <class 'numpy.ndarray'> 
# Crear un ndarray de dos dimensiones (matriz)
matrix = np.array([[1, 2], [3, 4]]) 
print(matrix) # [[1 2] [3 4]] 

#2. numpy.matrix
#La clase matrix es una subclase de ndarray que representa una matriz bidimensional. Aunque numpy recomienda usar ndarray para operaciones generales, matrix se sigue usando en algunos contextos donde se desea trabajar explícitamente con matrices. Ejemplo:
# Crear una matriz 2x2 
m = np.matrix([[1, 2], [3, 4]]) 
print(type(m)) # <class 'numpy.matrix'> 
# Operaciones con matrices 
m2 = np.matrix([[5, 6], [7, 8]]) 
print(m * m2) # Multiplicación de matrices 

#3. numpy.generic
#Es la clase base para todos los tipos de datos de numpy, como int32, float64, etc. Representa un objeto de tipo numpy que no tiene una estructura de arreglo (como los números de punto flotante o enteros). Ejemplo:
# Crear un número flotante de numpy 
num = np.float64(5.7) 
print(type(num)) # <class 'numpy.float64'> 

#4. numpy.ufunc
#Esta clase representa una función universal en numpy. Las funciones universales son operaciones elementales de bajo nivel que operan sobre datos de ndarray de manera rápida.Ejemplo:
# Crear una ufunc 
ufunc = np.add 
result = ufunc(5, 3) 
print(result) # 8 

#5. numpy.dtype
#La clase dtype representa el tipo de datos de los elementos dentro de un arreglo ndarray. Permite especificar el tipo de datos de los elementos y manipularlos de forma eficiente. Ejemplo:
# Definir un arreglo con un tipo de dato específico 
arr = np.array([1, 2, 3], dtype=np.float64)
print(arr) # [1. 2. 3.] 
print(arr.dtype) # float64 

#6. numpy.random.RandomState
#Esta clase se utiliza para generar números aleatorios. Aunque numpy tiene muchas funciones aleatorias, RandomState es una forma más flexible de crear generadores de números aleatorios. Ejemplo:
# Crear un generador de números aleatorios 
rs = np.random.RandomState(42) # Generar un número aleatorio
print(rs.rand()) # Valor aleatorio entre 0 y 1 

#7. numpy.recarray
#recarray es una subclase de ndarray que permite acceder a los campos de un arreglo mediante atributos (como si fueran campos de un objeto), en lugar de índices. Es útil para trabajar con datos estructurados de manera más amigable. Ejemplo:
# Crear un recarray 
rec_arr = np.recarray(3, dtype=[('x', 'i4'), ('y', 'f4')]) 
rec_arr[0] = (1, 2.5) 
rec_arr[1] = (2, 3.5) 
rec_arr[2] = (3, 4.5) # Acceder a los campos por atributos 
print(rec_arr.x) # [1 2 3] 



"""El módulo numpy tiene varias variables importantes que se utilizan en diversas operaciones"""

#1. numpy.e
#Esta es una constante que representa el número de Euler (aproximadamente 2.718281828459045). Es útil en operaciones matemáticas, especialmente en cálculos de crecimiento exponencial y logaritmos naturales. Ejemplo:
print(np.e) # 2.718281828459045 

#2. numpy.pi
#Esta constante representa el valor de pi (aproximadamente 3.141592653589793). Es comúnmente utilizada en cálculos relacionados con círculos y geometría. Ejemplo:
print(np.pi) # 3.141592653589793 

#3. numpy.inf
#Representa el infinito positivo en numpy. Puede ser útil cuando se desea definir valores que exceden los límites de representaciones numéricas. Ejemplo:
print(np.inf) # inf 

#4. numpy.NAN
#Representa "Not a Number" (NaN). Es utilizado para representar valores no definidos o no representables, como el resultado de una división por cero o valores faltantes. Ejemplo:
print(np.NAN) # nan 

#5. numpy.PINF
#Representa el infinito positivo, similar a numpy.inf, pero está específicamente reservado para los valores positivos infinitos dentro de un contexto de tipos de datos de punto flotante. Ejemplo:
print(np.PINF) # inf 

#6. numpy.NINF
#Representa el infinito negativo, similar a numpy.inf, pero específicamente para valores negativos infinitos. Ejemplo:
print(np.NINF) # -inf 

#7. numpy.bool_
#Representa un tipo de dato de booleano en numpy. Es usado para almacenar valores booleanos de manera más eficiente en arreglos. Ejemplo:
arr = np.array([True, False, True], dtype=np.bool_)
print(arr) # [ True False True ] 

#8. numpy.float_
#Es el tipo de dato que representa números de punto flotante. Dependiendo del sistema, puede ser float32 o float64, pero se usa generalmente para mantener la precisión de los cálculos. Ejemplo:
arr = np.array([1.1, 2.2, 3.3], dtype=np.float_)
print(arr) # [1.1 2.2 3.3] 

#9. numpy.int_
#Es el tipo de dato que representa enteros. Similar a float_, depende de la plataforma, pero generalmente es int32 o int64. Ejemplo:
arr = np.array([1, 2, 3], dtype=np.int_) 
print(arr) # [1 2 3] 

#10. numpy.complex_
#Es el tipo de dato que representa números complejos en numpy. El tipo complejo se utiliza para operaciones que involucran números imaginarios. Ejemplo:
arr = np.array([1 + 2j, 3 + 4j], dtype=np.complex_) 
print(arr) # [1.+2.j 3.+4.j] 

#11. numpy.intc
#Representa el tipo de dato entero estándar, equivalente a int32 en muchas plataformas. Se usa cuando se desea asegurar que el tipo de datos sea compatible con los enteros de 32 bits. Ejemplo:
arr = np.array([1, 2, 3], dtype=np.intc) 
print(arr) # [1 2 3] 

#12. numpy.intp
#Es el tipo de dato entero que tiene el tamaño de un puntero. Es útil cuando se trabaja con índices en arreglos. Ejemplo:
arr = np.array([1, 2, 3], dtype=np.intp) 
print(arr) # [1 2 3] 

#13. numpy.longlong
#Representa un tipo de dato entero largo. Es el equivalente a int64 en muchas plataformas. Ejemplo:
arr = np.array([1, 2, 3], dtype=np.longlong) 
print(arr) # [1 2 3] 

#14. numpy.uint8, numpy.uint16, numpy.uint32, numpy.uint64
#Estos son tipos de datos enteros sin signo que representan 8, 16, 32 o 64 bits respectivamente. Ejemplo:
arr = np.array([1, 2, 3], dtype=np.uint8) 
print(arr) # [1 2 3] 

#15. numpy.datetime64
#Esta variable se utiliza para manejar fechas y tiempos en numpy. Es especialmente útil cuando se trabaja con series temporales. Ejemplo:
date = np.datetime64('2023-01-01') 
print(date) # 2023-01-01 

#16. numpy.timedelta64
#Representa una diferencia de tiempo o duración, como días, meses, años, etc. Ejemplo:
delta = np.timedelta64(5, 'D') # 5 días
print(delta) # 5 days 

#17. numpy.finfo
#Proporciona información sobre el tipo de datos de punto flotante (como el rango y la precisión de float32 o float64). Ejemplo:
print(np.finfo(np.float32)) # Rango y precisión para float32 

#18. numpy.iinfo
#Proporciona información sobre el tipo de datos entero (como el rango para enteros de 32 o 64 bits). Ejemplo:
print(np.iinfo(np.int32)) # Rango para int32 

#19. numpy.seterr()
#Esta variable se utiliza para configurar las reglas de manejo de errores en numpy (como las excepciones de división por cero o los valores inválidos). Ejemplo:
np.seterr(divide='ignore') # Ignorar errores de división por cero 



"""El módulo numpy tiene varias constantes que son útile"""

#1. numpy.RTLD_GLOBAL, numpy.RTLD_LOCAL
#Constantes utilizadas al cargar bibliotecas compartidas en numpy y especificar su visibilidad. Usadas en funciones de carga de bibliotecas dinámicas como numpy.ctypeslib.load_library. Ejemplo:
print(np.RTLD_GLOBAL) 
print(np.RTLD_LOCAL) 

#2. numpy.int8, numpy.int16, numpy.int32, numpy.int64
#Son constantes que representan enteros con diferentes tamaños de bits (8, 16, 32 y 64 bits respectivamente). Ejemplo:
arr = np.array([1, 2, 3], dtype=np.int32) 
print(arr) # [1 2 3] 

#3. numpy.uint8, numpy.uint16, numpy.uint32, numpy.uint64
#Son constantes que representan enteros sin signo de diferentes tamaños de bits. Ejemplo:
arr = np.array([1, 2, 3], dtype=np.uint8) 
print(arr) # [1 2 3] 

#4. numpy.float32, numpy.float64
#Representan los tipos de datos de punto flotante con precisión simple y doble. Ejemplo:
arr = np.array([1.0, 2.0, 3.0], dtype=np.float64) 
print(arr) # [1. 2. 3.] 

#5. numpy.complex64, numpy.complex128
#Representan números complejos con diferentes precisiones. Ejemplo:
arr = np.array([1 + 2j, 3 + 4j], dtype=np.complex128)
print(arr) # [1.+2.j 3.+4.j] 



"""El módulo numpy tiene varias excepciones"""

#1. numpy.AxisError
#Esta excepción se lanza cuando una operación sobre un arreglo de numpy intenta acceder a un eje que no existe o no es válido. Ejemplo:
arr = np.array([[1, 2], [3, 4]]) 
try: 
    arr.sum(axis=3) # Intentando sumar a un eje que no existe 
except np.AxisError as e: 
    print(f"Error: {e}") 

#2. numpy.ValueError
#Se lanza cuando se pasan argumentos incorrectos a una operación, como un número de dimensiones incorrecto o una incompatibilidad de forma de arreglos. Ejemplo:
arr = np.array([1, 2, 3]) 
try: 
    arr.reshape((2, 3)) # Incompatible con el número de elementos 
except np.ValueError as e: 
    print(f"Error: {e}") 

#3. numpy.TypeError
#Se lanza cuando el tipo de dato de un arreglo es incompatible con una operación, como intentar realizar una operación matemática con datos no numéricos. Ejemplo:
arr = np.array(['a', 'b', 'c']) 
try:
    arr + 1 # Intentando sumar un número a un arreglo de cadenas
except np.TypeError as e:
    print(f"Error: {e}") 

#4. numpy.MemoryError
#Esta excepción ocurre cuando no hay suficiente memoria para realizar una operación en el arreglo o cuando se intenta crear un arreglo de tamaño demasiado grande. Ejemplo:
try:
    arr = np.zeros((10**9, 10**9)) # Intentando crear un arreglo demasiado grande 
except np.MemoryError as e: 
    print(f"Error: {e}") 

#5. numpy.linalg.LinAlgError
#Se lanza en operaciones de álgebra lineal cuando hay un problema, como una matriz no invertible o problemas con la descomposición. Ejemplo:
from numpy.linalg import LinAlgError 
arr = np.array([[1, 2], [2, 4]])
try: 
    np.linalg.inv(arr) # Intentando invertir una matriz singular 
except LinAlgError as e: 
    print(f"Error: {e}") 

#6. numpy.matlib.MatlibError
#Se lanza cuando se produce un error relacionado con las funciones de la subbiblioteca matlib de numpy. Ejemplo:
from numpy.matlib import mat 
try: 
    m = mat([[1, 2], [3, 4]]) # Intentando crear una matriz 
    print(m + "string") # Suma inválida con una cadena 
except np.matlib.MatlibError as e:
    print(f"Error: {e}") 

#7. numpy.UFuncTypeError
#Se lanza cuando una operación de función universal (ufunc) recibe argumentos de tipo incorrecto. Ejemplo:
arr = np.array([1, 2, 3])
try: 
    np.add(arr, "string") # Intentando sumar una cadena a un arreglo 
except np.UFuncTypeError as e:
    print(f"Error: {e}") 

#8. numpy.PandasError
#Aunque no es tan común, algunas operaciones pueden generar excepciones si se integran con la biblioteca pandas y no se usan correctamente. Ejemplo:
import pandas as pd 
try: 
    df = pd.DataFrame([1, 2, 3])
    arr = np.array(df) 
except np.PandasError as e: 
    print(f"Error: {e}") 



"""El módulo numpy tiene varios submódulos"""

#1. numpy.fft
#Submódulo utilizado para trabajar con la Transformada Rápida de Fourier (FFT, por sus siglas en inglés), que se utiliza para realizar transformadas de Fourier discretas y sus variantes. Ejemplo:
from numpy.fft import fft 
arr = np.array([1, 2, 3, 4]) 
result = fft(arr) # Calcula la Transformada Rápida de Fourier
print(result) 

#2. numpy.linalg
#Este submódulo contiene funciones de álgebra lineal, como el cálculo de determinantes, la inversión de matrices, la factorización de matrices y más. Ejemplo:
from numpy.linalg import inv
arr = np.array([[1, 2], [3, 4]])
result = inv(arr) # Calcula la inversa de una matriz 
print(result) 

#3. numpy.random
#Submódulo que ofrece funciones para generar números aleatorios de diferentes distribuciones y realizar muestreos. Ejemplo:
from numpy.random import rand 
arr = rand(3, 2) # Genera una matriz 3x2 de números aleatorios entre 0 y 1 
print(arr) 

#4. numpy.ma
#Submódulo para trabajar con arreglos enmascarados, que son arreglos que permiten tener valores "faltantes" o "enmascarados". Ideal para manejar datos incompletos. Ejemplo:
from numpy.ma import masked_array 
arr = np.array([1, 2, 3, 4]) 
masked_arr = masked_array(arr, mask=[0, 1, 0, 0]) # Enmascara el segundo valor 
print(masked_arr) 

#5. numpy.polynomial
#Submódulo para trabajar con polinomios, que ofrece funciones para evaluar, derivar, integrar y ajustar polinomios. Ejemplo:
from numpy.polynomial.polynomial import Polynomial
p = Polynomial([1, -3, 2]) # Representa el polinomio x^2 - 3x + 2 
print(p(1)) # Evalúa el polinomio en x = 1 

#6. numpy.core
#Este submódulo contiene las funciones principales del núcleo de numpy y define la funcionalidad básica de arrays. Es más bajo nivel y menos accesible directamente, pero contiene elementos clave de la infraestructura de numpy. Ejemplo:
print(np.core.numeric) 

#7. numpy.ctypeslib
#Submódulo que permite trabajar con bibliotecas compartidas mediante la interfaz ctypes. Se usa para integrar numpy con bibliotecas C. Ejemplo:
from numpy.ctypeslib import load_library 
lib = load_library('libm.so', '/usr/lib') # Carga una biblioteca compartida 

#8. numpy.testing
#Submódulo utilizado para realizar pruebas y verificar la corrección de las operaciones y funciones de numpy. Proporciona herramientas para comparar arreglos numéricos de manera eficiente. Ejemplo:
from numpy.testing import assert_array_equal 
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3]) 
assert_array_equal(arr1, arr2) # Verifica si los arreglos son iguales 

#9. numpy.lib
#Este submódulo proporciona varias utilidades y funciones adicionales que no caen directamente en los otros submódulos. Contiene herramientas útiles para manipulaciones de arreglos, operaciones matemáticas, funciones estadísticas y más. Ejemplo:
from numpy.lib import stride_tricks
arr = np.array([1, 2, 3, 4, 5]) 
subarr = stride_tricks.as_strided(arr, shape=(3, 2), strides=(arr.strides[0], arr.strides[0])) 
print(subarr) 

#10. numpy.distutils
#Submódulo que proporciona herramientas para la construcción y compilación de bibliotecas de numpy y extensiones de C, incluyendo la compilación de módulos de Python en C. Ejemplo:
import numpy.distutils 
# Este submódulo generalmente se usa para tareas de instalación y compilación en entornos específicos 

#11. numpy.version
#Submódulo que proporciona información sobre la versión de numpy instalada en el entorno. Ejemplo:
print(np.__version__) # Muestra la versión de numpy 

