import scipy

"""El módulo scipy es una biblioteca de Python que se basa en numpy y proporciona herramientas y funciones adicionales para 
realizar cálculos científicos y técnicos avanzados. Es particularmente útil para trabajar en áreas como álgebra lineal, "
"optimización, estadísticas, integración numérica, procesamiento de señales, interpolación y más."""

#Funcionalidades clave de scipy:
#Álgebra Lineal: scipy.linalg ofrece funciones para resolver sistemas de ecuaciones, calcular determinantes, valores propios, etc., de manera eficiente.
#Optimización: scipy.optimize contiene métodos para resolver problemas de optimización y encontrar mínimos de funciones.
#Integración y ecuaciones diferenciales: scipy.integrate ayuda a resolver integrales y ecuaciones diferenciales numéricas.
#Interpolación: scipy.interpolate permite realizar interpolación de datos y ajustar funciones a conjuntos de datos.
#Estadísticas: scipy.stats proporciona una amplia variedad de funciones estadísticas, distribuciones de probabilidad y pruebas estadísticas.
#Procesamiento de señales: scipy.signal contiene funciones para el análisis y procesamiento de señales, como filtros y transformadas.
#Álgebra de matrices dispersas: scipy.sparse ayuda a trabajar con matrices dispersas, lo que es más eficiente en términos de memoria para grandes matrices con muchos ceros.
#Ejemplo de uso:
import scipy.integrate as integrate
import numpy as np 
# Definir una función
def func(x):
    return np.sin(x) # Integrar la función de 0 a pi 
result, error = integrate.quad(func, 0, np.pi) 
print(f"Resultado de la integración: {result}, Error estimado: {error}") 



"""Funciones"""
#1. scipy.integrate.quad: Realiza la integración numérica de una función en un intervalo dado.
import scipy.integrate as integrate 
# Definir la función a integrar 
def f(x): 
    return x**2 # Integrar la función de 0 a 1 
result, error = integrate.quad(f, 0, 1) 
print(f"Resultado de la integración: {result}") 

#2. scipy.optimize.minimize: Realiza la minimización de una función.
import scipy.optimize as opt
# Función a minimizar 
def func(x): 
    return (x - 2)**2 # Minimizamos la función comenzando en 0
result = opt.minimize(func, 0) 
print(f"Resultado de la minimización: {result.x}") 

#3. scipy.interpolate.interp1d: Interpolación unidimensional de funciones.
import scipy.interpolate as interp 
# Datos de ejemplo
x = np.array([0, 1, 2, 3]) 
y = np.array([0, 1, 4, 9]) 
# Crear la función de interpolación
f = interp.interp1d(x, y, kind='linear') 
# Evaluar la interpolación en un nuevo punto 
print(f"Interpolación en 2.5: {f(2.5)}") 

#4. scipy.linalg.solve: Resuelve un sistema de ecuaciones lineales.
import scipy.linalg as linalg 
# Definir la matriz y el vector
A = np.array([[3, 2], [1, 4]])
b = np.array([5, 6]) # Resolver el sistema
x = linalg.solve(A, b) 
print(f"Solución del sistema: {x}") 

#5. scipy.signal.convolve: Realiza la convolución de dos señales.
import scipy.signal as signal 
# Señales de ejemplo
x = np.array([1, 2, 3]) 
h = np.array([0, 1, 0.5]) 
# Convolución de las señales 
y = signal.convolve(x, h, mode='full')
print(f"Resultado de la convolución: {y}") 

#6. scipy.stats.ttest_ind: Realiza una prueba t de Student para dos muestras independientes.
import scipy.stats as stats
# Muestras de ejemplo 
sample1 = np.array([2.3, 2.9, 3.1, 3.3, 2.8]) 
sample2 = np.array([3.4, 3.8, 3.2, 3.0, 3.5]) 
# Realizar la prueba t 
stat, p_value = stats.ttest_ind(sample1, sample2)
print(f"Estadística t: {stat}, Valor p: {p_value}") 

#7. scipy.linalg.eig
#Calcula los valores propios y vectores propios de una matriz cuadrada.
import scipy.linalg as linalg 
# Definir la matriz 
A = np.array([[1, 2], [3, 4]]) 
# Calcular los valores propios y vectores propios 
values, vectors = linalg.eig(A) 
print(f"Valores propios: {values}") 
print(f"Vectores propios: {vectors}") 

#8. scipy.special.gammaln
#Calcula el logaritmo de la función gamma.
import scipy.special as sp 
# Calcular el logaritmo de la función gamma
result = sp.gammaln(5) 
print(f"Logaritmo de Gamma(5): {result}") 

#9. scipy.cluster.hierarchy.linkage: Realiza el algoritmo de agrupamiento jerárquico.
import scipy.cluster.hierarchy as hierarchy 
# Datos de ejemplo 
data = np.array([[1, 2], [3, 4], [5, 6]])
# Calcular el agrupamiento jerárquico 
Z = hierarchy.linkage(data, method='single') 
print(f"Resultado del agrupamiento jerárquico: {Z}") 

#10. scipy.optimize.curve_fit: Ajusta una curva a datos usando mínimos cuadrados no lineales.
import scipy.optimize as opt 
import matplotlib.pyplot as plt
# Datos de ejemplo
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([2.3, 2.9, 3.3, 3.6, 4.0]) 

# Función de ajuste 
def func(x, a, b):
    return a * x + b
# Ajustar la curva 
params, params_covariance = opt.curve_fit(func, x_data, y_data) 
# Graficar el ajuste
plt.scatter(x_data, y_data, label='Datos') 
plt.plot(x_data, func(x_data, *params), label='Ajuste', color='red') 
plt.legend() 
plt.show() 

#11. scipy.integrate.simps
#Calcula la integral de una función usando la regla de Simpson.
import scipy.integrate as integrate 
# Datos de ejemplo
x = np.linspace(0, np.pi, 100)
y = np.sin(x)
#Realizar la integración utilizando la regla de Simpson 
result = integrate.simps(y, x) 
print(f"Resultado de la integración (Simpson): {result}") 

#12. scipy.stats.norm: Trabaja con la distribución normal, incluyendo la generación de variables aleatorias.
import scipy.stats as stats 
# Generar una variable aleatoria de una distribución normal estándar 
random_value = stats.norm.rvs(loc=0, scale=1, size=5) 
print(f"Valores aleatorios de una distribución normal estándar: {random_value}") 

#13. scipy.linalg.det: Calcula el determinante de una matriz.
import scipy.linalg as linalg 
# Definir la matriz 
A = np.array([[1, 2], [3, 4]])
# Calcular el determinante 
determinant = linalg.det(A) 
print(f"Determinante de la matriz: {determinant}") 

#14. scipy.signal.resample: Realiza el cambio de tamaño de una señal.
import scipy.signal as signal 
# Señal de ejemplo 
x = np.sin(np.linspace(0, 10, 100)) 
# Resamplear la señal a 50 puntos 
y_resampled = signal.resample(x, 50) 
print(f"Señal resampleada: {y_resampled}") 

#15. scipy.sparse.csr_matrix: Crea una matriz dispersa en formato CSR (Compressed Sparse Row).
import scipy.sparse as sparse
# Crear una matriz dispersa en formato CSR 
data = np.array([4, 5, 7]) 
row_indices = np.array([0, 2, 3]) 
col_indices = np.array([1, 2, 3]) 
matrix = sparse.csr_matrix((data, (row_indices, col_indices)), shape=(4, 4)) 
print(f"Matriz dispersa CSR:\n{matrix}") 

#16. scipy.optimize.differential_evolution; Realiza optimización mediante el algoritmo de evolución diferencial.
import scipy.optimize as opt
# Función a minimizar 
def func(x): 
    return x**2 + 3 * x + 2
# Realizar la optimización 
result = opt.differential_evolution(func, bounds=[(-10, 10)]) 
print(f"Resultado de la optimización: {result.x}") 

#17. scipy.special.jn: Calcula la función de Bessel de primer tipo.
import scipy.special as sp 
# Calcular la función de Bessel de primer tipo para n=0 y x=3 
result = sp.jn(0, 3) 
print(f"Función de Bessel J0(3): {result}") 




"""El módulo scipy es muy amplio, y cuenta con una variedad de clases"""

#1. scipy.sparse.csr_matrix
#La clase csr_matrix se utiliza para almacenar matrices dispersas en formato Compressed Sparse Row (CSR). Este formato es eficiente para la multiplicación de matrices y otros cálculos. Ejemplo:
import scipy.sparse as sparse
# Crear una matriz dispersa en formato CSR 
data = np.array([4, 5, 7]) 
row_indices = np.array([0, 2, 3]) 
col_indices = np.array([1, 2, 3]) 
matrix = sparse.csr_matrix((data, (row_indices, col_indices)), shape=(4, 4)) 
print(f"Matriz dispersa CSR:\n{matrix}") 

#2. scipy.sparse.csc_matrix
#La clase csc_matrix es otra representación de matrices dispersas, pero en este caso en formato Compressed Sparse Column (CSC). Es más eficiente para la transposición y las operaciones columna por columna. Ejemplo:
import scipy.sparse as sparse 
# Crear una matriz dispersa en formato CSC 
data = np.array([4, 5, 7]) 
row_indices = np.array([0, 2, 3]) 
col_indices = np.array([1, 2, 3]) 
matrix = sparse.csc_matrix((data, (row_indices, col_indices)), shape=(4, 4)) 
print(f"Matriz dispersa CSC:\n{matrix}") 


#3. scipy.optimize.OptimizeResult
#La clase OptimizeResult contiene el resultado de las funciones de optimización, incluyendo el valor de la solución, el éxito de la optimización y otros detalles. Ejemplo:
import scipy.optimize as opt 
# Función a minimizar
def func(x): 
    return (x - 2)**2 
# Minimizamos la función comenzando en 0
result = opt.minimize(func, 0) 
print(f"Resultado de la optimización: {result}") 

#4. scipy.integrate.odeint
#La clase odeint resuelve sistemas de ecuaciones diferenciales ordinarias (ODE). Permite especificar un sistema de ecuaciones y su condición inicial. Ejemplo:
import scipy.integrate as integrate
import matplotlib.pyplot as plt
# Definir la ecuación diferencial 
def model(y, t): 
    dydt = -2 * y 
    return dydt # Condición inicial 
y0 = 1 # Tiempo
t = np.linspace(0, 5, 100) # Resolver la ecuación diferencial 
y = integrate.odeint(model, y0, t) # Graficar el resultado 
plt.plot(t, y) 
plt.xlabel('Tiempo') 
plt.ylabel('y') 
plt.title('Solución de la ecuación diferencial') 
plt.show() 

#5. scipy.spatial.Delaunay
#La clase Delaunay se utiliza para generar una triangulación de Delaunay a partir de un conjunto de puntos en el espacio. Ejemplo:
import scipy.spatial as spatial
points = np.random.rand(10, 2) # Generar la triangulación de Delaunay 
tri = spatial.Delaunay(points) # Ver las celdas trianguladas
print(f"Triangulaciones de Delaunay: {tri.simplices}") 

#6. scipy.stats.rv_continuous
#rv_continuous es una clase base para la creación de distribuciones continuas personalizadas. Permite definir distribuciones estadísticas personalizadas mediante la herencia y sobrescribiendo algunos métodos clave. Ejemplo:
import scipy.stats as stats
# Definir una distribución normal 
class CustomDistribution(stats.rv_continuous):
    def _pdf(self, x): 
        return np.exp(-x**2 / 2) / np.sqrt(2 * np.pi) 
# Crear una instancia de la distribución 
custom_dist = CustomDistribution(name="custom_normal") 
# Calcular el valor de la PDF en
x = 0 
print(f"Valor de la PDF en x=0: {custom_dist.pdf(0)}") 

#7. scipy.signal.TransferFunction
#La clase TransferFunction se utiliza para representar funciones de transferencia en sistemas de control y señales. Ejemplo:
import scipy.signal as signal 
import matplotlib.pyplot as plt 
# Numerador y denominador de la función de transferencia 
num = [1] 
den = [1, 3, 2] # Crear la función de transferencia 
system = signal.TransferFunction(num, den) # Simulación de la respuesta del sistema en el tiempo 
t, y = signal.step(system) 
# Graficar la respuesta 
plt.plot(t, y) 
plt.xlabel('Tiempo') 
plt.ylabel('Respuesta')
plt.title('Respuesta de la función de transferencia') 
plt.show() 

#8. scipy.linalg.LinAlgError
#LinAlgError es una clase que se utiliza para manejar errores relacionados con álgebra lineal, como fallos en la inversión de matrices o en la descomposición de matrices. Ejemplo:
import scipy.linalg as linalg
# Definir una matriz singular (no invertible)
A = np.array([[1, 2], [2, 4]]) 
# Intentar invertir la matriz 
try: 
    inv_A = linalg.inv(A) 
except linalg.LinAlgError as e:
    print(f"Error en la inversión de la matriz: {e}") 

#9. scipy.special.Gamma
#La clase Gamma se utiliza para trabajar con la función gamma. Esta clase permite calcular valores relacionados con la función gamma y sus derivadas. Ejemplo:
import scipy.special as sp 
# Calcular el valor de la función Gamma para 
x=5 
result = sp.gamma(5) 
print(f"Valor de Gamma(5): {result}") 

#10. scipy.interpolate.BarycentricInterpolator
#La clase BarycentricInterpolator realiza interpolación utilizando la interpolación barycéntrica. Es útil cuando se necesita una interpolación de precisión sin una gran sobrecarga computacional. Ejemplo:
import scipy.interpolate as interp 
x = np.array([0, 1, 2, 3]) 
y = np.array([0, 1, 4, 9]) # Crear el interpolador
interpolator = interp.BarycentricInterpolator(x, y)
# Evaluar la interpolación en un nuevo punto
print(f"Interpolación en 1.5: {interpolator(1.5)}") 



"""El módulo scipy no tiene variables predefinidas o constantes, pero hay algunas variables y configuraciones que puedes encontrar 
dentro de los submódulos de scipy, que son utilizadas para controlar el comportamiento de las funciones o como valores predeterminados para ciertos cálculos. """

#1. scipy.integrate._IntegrationWarning
#s una variable utilizada internamente para generar advertencias relacionadas con la integración, como un resultado no convergente. Ejemplo:
import scipy.integrate as integrate
import warnings
# Generar una advertencia de integración 
warnings.warn("Este es un ejemplo de advertencia en integración.", category=integrate._IntegrationWarning) 

#2. scipy.optimize._warn
#Es una variable interna que se utiliza en la optimización para generar advertencias sobre posibles problemas, como la falta de convergencia en un proceso de optimización. Ejemplo:
import scipy.optimize as opt 
import warnings 
# Generar una advertencia en optimización 
warnings.warn("Este es un ejemplo de advertencia en optimización.", category=opt._warn) 

#3. scipy.special._pycache
#Es una variable interna en el submódulo special que almacena información sobre el directorio de caché de Python. Ejemplo:
import scipy.special as sp 
# Verificar si la variable _pycache existe 
print(f"Cache de Python en especial: {hasattr(sp, '_pycache')}") 

#4. scipy.stats._stats
#Es una variable interna en el submódulo stats que se usa para almacenar estadísticas precomputadas y datos relacionados con distribuciones estadísticas. Ejemplo:
import scipy.stats as stats 
# Verificar si la variable _stats existe
print(f"Existe la variable _stats en stats: {hasattr(stats, '_stats')}") 

#5. scipy.sparse._sparsetools
#Es una variable interna del submódulo sparse que contiene herramientas específicas para trabajar con matrices dispersas. Ejemplo:
import scipy.sparse as sparse 
# Verificar si _sparsetools existe 
print(f"Existe _sparsetools en sparse: {hasattr(sparse, '_sparsetools')}") 



"""El módulo scipy tiene un submódulo llamado scipy.constants, que contiene varias constantes físicas y matemáticas"""

#1. scipy.constants.pi: Contiene el valor de pi, que es utilizado en muchas funciones matemáticas dentro de scipy. Ejemplo:
import scipy.constants as const # Usar el valor de pi
print(f"El valor de pi es: {const.pi}") 

#2. scipy.constants.e: Contiene el valor de la constante matemática , la base del logaritmo natural. Ejemplo:
import scipy.constants as const
# Usar el valor de e 
print(f"El valor de e es: {const.e}") 

#3. scipy.constants.g: Es la constante gravitacional de la Tierra, expresada en metros por segundo al cuadrado (). Ejemplo:
import scipy.constants as const
# Usar el valor de la constante gravitacional
print(f"La constante gravitacional es: {const.g} m/s²") 

#4. scipy.constants.c: Es la velocidad de la luz en el vacío, expresada en metros por segundo (). Ejemplo:
import scipy.constants as const 
# Usar el valor de la velocidad de la luz
print(f"La velocidad de la luz es: {const.c} m/s") 

#5. scipy.constants.h: La constante de Planck , que describe la relación entre la energía de una partícula y su frecuencia. Ejemplo:
import scipy.constants as const 
# Usar la constante de Planck
print(f"La constante de Planck es: {const.h} J·s") 

#6. scipy.constants.N_A: El número de Avogadro , que representa el número de unidades (átomos, moléculas, etc.) por mol. Ejemplo:
import scipy.constants as const
# Usar el número de Avogadro 
print(f"El número de Avogadro es: {const.N_A} mol⁻¹") 

#7. scipy.constants.k: La constante de Boltzmann , que relaciona la temperatura con la energía a nivel de partículas. Ejemplo:
import scipy.constants as const
# Usar la constante de Boltzmann 
print(f"La constante de Boltzmann es: {const.k} J/K") 

#8. scipy.constants.R: La constante de los gases ideales , que es utilizada en la ecuación de los gases ideales. Ejemplo:
import scipy.constants as const 
# Usar la constante de los gases ideales 
print(f"La constante de los gases ideales es: {const.R} J/(mol·K)") 

#9. scipy.constants.electron_volt: Es el valor de un electrón volt (eV) expresado en julios. Ejemplo:
import scipy.constants as const 
# Usar el valor de un electrón volt
print(f"Un electrón volt es: {const.electron_volt} julios") 

#10. scipy.constants.sigma: La constante de Stefan-Boltzmann , que aparece en la ley de radiación de cuerpo negro. Ejemplo:
import scipy.constants as const 
# Usar la constante de Stefan-Boltzmann 
print(f"La constante de Stefan-Boltzmann es: {const.sigma} W/m²·K⁴") 

#12. scipy.constants.alpha: La constante de estructura fina , que es una medida de la intensidad de la interacción electromagnética. Ejemplo:
import scipy.constants as const 
# Usar la constante de estructura fina 
print(f"La constante de estructura fina es: {const.alpha}") 

#13. scipy.constants.mu_0: La permeabilidad del vacío , que es utilizada en electromagnetismo para describir la relación entre el campo magnético y la corriente. Ejemplo:
import scipy.constants as const 
# Usar la permeabilidad del vacío
print(f"La permeabilidad del vacío es: {const.mu_0} T·m/A") 

#14. scipy.constants.epsilon_0: La permitividad del vacío , que describe la relación entre el campo eléctrico y la carga en el vacío. Ejemplo:
import scipy.constants as const
# Usar la permitividad del vacío 
print(f"La permitividad del vacío es: {const.epsilon_0} F/m") 

#15. scipy.constants.F: La constante de Faraday , que representa la cantidad de carga eléctrica por mol de electrones. Ejemplo:
import scipy.constants as const 
# Usar la constante de Faraday
print(f"La constante de Faraday es: {const.F} C/mol") 

#16. scipy.constants.m_p: La masa del protón , que es una constante fundamental en física. Ejemplo:
import scipy.constants as const 
# Usar la masa del protón 
print(f"La masa del protón es: {const.m_p} kg") 



"""El módulo scipy tiene varias excepciones"""

#1. scipy.optimize.OptimizeError: Esta excepción se lanza cuando ocurre un error durante un proceso de optimización. Ejemplo:
import scipy.optimize as opt 
def func(x): 
    return x**2
try:
# Intentar una optimización con una función incorrecta
    result = opt.minimize(func, [0]) 
except opt.OptimizeError as e:
    print(f"Error en la optimización: {e}") 

#2. scipy.integrate.IntegrationWarning
#Esta excepción es una advertencia generada cuando ocurre un problema durante la integración, como la falta de convergencia. Ejemplo:
import scipy.integrate as integrate
import warnings
# Función que no se puede integrar correctamente
def func(x):
    return 1 / x # Usar una integración para generar una advertencia
try: 
    result, error = integrate.quad(func, 0, 1)
except Exception as e: 
    print(f"Advertencia en la integración: {e}") 

#3. scipy.sparse.SparseEfficiencyWarning
#Este tipo de advertencia se lanza cuando hay un problema relacionado con la eficiencia en el uso de matrices dispersas. Ejemplo:
import scipy.sparse as sparse
import warnings 
# Crear una matriz dispersa ineficiente 
sparse_matrix = sparse.coo_matrix(([], [], []), shape=(5, 5)) 
# Generar advertencia de eficiencia 
warnings.warn("Advertencia de eficiencia en matrices dispersas", category=sparse.SparseEfficiencyWarning) 

#4. scipy.linalg.LinAlgError
#Es una excepción general que se lanza cuando se produce un error relacionado con la álgebra lineal, como la falta de inversibilidad de una matriz. Ejemplo:
import scipy.linalg as linalg 
try: # Intentar invertir una matriz no invertible 
    matrix = [[1, 2], [2, 4]] 
    result = linalg.inv(matrix) 
except linalg.LinAlgError as e: 
    print(f"Error en álgebra lineal: {e}") 

#5. scipy.stats.PerformanceWarning
#Se lanza cuando hay problemas de rendimiento al realizar ciertos cálculos estadísticos. Ejemplo:
import scipy.stats as stats 
import warnings # Generar advertencia de rendimiento en cálculo de estadísticas 
warnings.warn("Advertencia de rendimiento en estadísticas", category=stats.PerformanceWarning) 

#6. scipy.optimize.NonLinearConstraint
#Aunque no es exactamente una excepción, esta clase se utiliza para definir restricciones no lineales en optimización. Si se usan de manera incorrecta, pueden generar errores que son capturados por otras excepciones. Ejemplo:
import scipy.optimize as opt 
# Intentar usar una restricción no válida 
constraint = opt.NonLinearConstraint(lambda x: x**2 - 1, 0, 10) 

#7. scipy.interpolate.InterpolationError
#Se lanza cuando ocurre un error en un proceso de interpolación, como un índice fuera de rango o un tipo de interpolación no soportado. Ejemplo:
import scipy.interpolate as interp 
try: # Intentar hacer una interpolación con datos no válidos 
    f = interp.interp1d([1, 2, 3], [1, 4, 9]) 
    result = f(4) # Esto genera una advertencia ya que 4 no está en el rango de datos
except interp.InterpolationError as e: 
    print(f"Error en interpolación: {e}") 

#8. scipy.optimize._optimize.OptimizeWarning
#Advertencia que ocurre durante la optimización, particularmente cuando se encuentra un valor no convergente o se llega a un resultado subóptimo. Ejemplo:
import scipy.optimize as opt 
import warnings # Usar una optimización que puede generar advertencia 
def func(x):
    return (x - 2)**2 
warnings.warn("Advertencia en la optimización", category=opt._optimize.OptimizeWarning) 

#9. scipy.signal.SignalError
#Se lanza cuando ocurre un error al trabajar con señales, como en la filtración o el procesamiento de señales. Ejemplo:
import scipy.signal as signal
try: # Usar un filtro con parámetros incorrectos 
    b, a = signal.butter(3, 1.2, 'low', analog=True) 
except signal.SignalError as e:
    print(f"Error en el procesamiento de señales: {e}") 

#10. scipy.special._ufuncs.UFuncTypeError
#Se lanza cuando se pasa un tipo de datos incompatible a una función especial de scipy.special. Ejemplo:
import scipy.special as sp
try:
    # Intentar calcular una función especial con un tipo de dato incorrecto
    result = sp.gamma("a") 
except sp._ufuncs.UFuncTypeError as e: 
    print(f"Error en el cálculo de la función especial: {e}") 



"""El módulo scipy tiene varios submódulos"""

#1. scipy.integrate
#Proporciona funciones para realizar integraciones numéricas, incluyendo integrales simples y ecuaciones diferenciales. Ejemplo de uso:
import scipy.integrate as integrate 
# Función para integrar 
def func(x):
    return x**2 # Realizar una integración definida 
result, error = integrate.quad(func, 0, 1) 
print(f"Resultado de la integración: {result}") 

#2. scipy.optimize
#Contiene algoritmos de optimización para encontrar el mínimo o máximo de funciones, resolver problemas de optimización no lineales, y más. Ejemplo de uso:
import scipy.optimize as opt 
# Función a minimizar 
def func(x): 
    return (x - 2)**2 # Encontrar el mínimo de la función 
result = opt.minimize(func, 0) 
print(f"Resultado de la optimización: {result.x}") 

#3. scipy.linalg
#Proporciona funciones avanzadas de álgebra lineal, como la factorización de matrices, la solución de sistemas de ecuaciones lineales y más. Ejemplo de uso:
import scipy.linalg as linalg
# Crear una matriz 
matrix = np.array([[1, 2], [3, 4]]) 
# Calcular la inversa de la matriz 
inv_matrix = linalg.inv(matrix)
print(f"Inversa de la matriz: \n{inv_matrix}") 

#4. scipy.stats
#Contiene funciones estadísticas, distribuciones de probabilidad y métodos para realizar pruebas estadísticas. Ejemplo de uso:
import scipy.stats as stats 
# Generar datos con una distribución normal
data = stats.norm.rvs(loc=0, scale=1, size=1000) 
# Calcular la media y desviación estándar
mean = stats.tmean(data)
std = stats.tstd(data) 
print(f"Media: {mean}, Desviación estándar: {std}") 

#5. scipy.interpolate
#Proporciona herramientas para la interpolación de datos, como interpolación unidimensional y multidimensional. Ejemplo de uso:
import scipy.interpolate as interp 
x = np.linspace(0, 10, 10) 
y = np.sin(x) # Crear un objeto de interpolación
f = interp.interp1d(x, y, kind='linear') # Interpolar para obtener un valor intermedio 
print(f(5.5)) 

#6. scipy.signal
#Contiene funciones para el procesamiento de señales, como filtrado, análisis espectral y transformación de señales. Ejemplo de uso:
import scipy.signal as signal
# Crear un filtro Butterworth de paso bajo
b, a = signal.butter(3, 0.1) # Aplicar el filtro a una señal
x = np.sin(np.linspace(0, 10, 100)) 
y = signal.filtfilt(b, a, x) 
print(y) 

#7. scipy.sparse
#Proporciona funciones para trabajar con matrices dispersas, que son útiles cuando se tienen matrices grandes y mayoritariamente llenas de ceros. Ejemplo de uso:
import scipy.sparse as sparse
# Crear una matriz dispersa en formato COO 
matrix = sparse.coo_matrix([[1, 0, 0], [0, 0, 3], [0, 0, 0]]) 
# Convertir a formato denso (matriz normal) 
dense_matrix = matrix.toarray() 
print(dense_matrix) 

#8. scipy.constants
#Contiene constantes físicas y matemáticas predefinidas, como , la constante de Planck, y otras constantes utilizadas en física y química. Ejemplo de uso:
import scipy.constants as const 
# Imprimir algunas constantes 
print(f"Valor de pi: {const.pi}") 
print(f"Velocidad de la luz: {const.c} m/s") 

#9. scipy.ndimage
#Proporciona funciones para procesamiento de imágenes, incluyendo filtros, transformaciones y análisis de imágenes multidimensionales. Ejemplo de uso:
import scipy.ndimage as ndimage
# Crear una imagen de ejemplo 
image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) 
# Aplicar un filtro gaussiano 
filtered_image = ndimage.gaussian_filter(image, sigma=1) 
print(filtered_image) 

#10. scipy.special
#Contiene funciones especiales, como las funciones gamma, Bessel y otras utilizadas en diversos campos científicos. Ejemplo de uso:
import scipy.special as sp 
# Calcular la función gamma de un número
result = sp.gamma(5) 
print(f"Gamma(5) = {result}") 

#11. scipy.cluster
#Contiene algoritmos para el análisis de clústeres, como el algoritmo de k-means y otras técnicas de agrupamiento. Ejemplo de uso:
import scipy.cluster.vq as vq 
# Datos de ejemplo 
data = np.random.rand(10, 2) 
# Aplicar el algoritmo de k-means 
centroids, labels = vq.kmeans(data, 2) 
print(f"Centroides: {centroids}") 
print(f"Etiquetas: {labels}") 

#12. scipy.integrate
#Contiene funciones para la resolución de ecuaciones diferenciales y para realizar integración numérica. Ejemplo de uso:
import scipy.integrate as integrate 
# Ecuación diferencial 
def model(t, y): 
    return -y 
# Resolver la ecuación diferencial 
result = integrate.solve_ivp(model, [0, 10], [1]) 
print(f"Solución: {result.y}") 
