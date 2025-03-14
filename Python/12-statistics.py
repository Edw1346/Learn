import statistics

"""El módulo statistics en Python sirve para hacer cálculos estadísticos básicos como media, mediana y moda."""



"""funciones del módulo statistics con ejemplos explicados:"""

#1. Medidas de tendencia central: mean(data) – Calcula la media (promedio)
datos = [1, 2, 3, 4, 5] 
print(statistics.mean(datos)) # (1+2+3+4+5) / 5 = 3.0 

#median(data)  Calcula la mediana (valor central de una lista ordenada)
datos = [7, 3, 1, 9, 5] 
print(statistics.median(datos)) # Ordenado: [1, 3, 5, 7, 9] → 5 

#mode(data)  Encuentra el valor más repetido
datos = [2, 3, 3, 5, 3, 7]
print(statistics.mode(datos)) # El número 3 aparece más veces 

#median_low(data)  Devuelve la mitad inferior en caso de una mediana par
datos = [1, 3, 5, 7, 9, 11] 
print(statistics.median_low(datos)) # Ordenado: [1, 3, 5, 7, 9, 11] → 5 

#median_high(data)  Devuelve la mitad superior en caso de una mediana par
datos = [1, 3, 5, 7, 9, 11] 
print(statistics.median_high(datos)) # Ordenado: [1, 3, 5, 7, 9, 11] → 7 

#median_grouped(data, interval=1) – Estima la mediana en datos agrupados
datos = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5] 
print(statistics.median_grouped(datos)) # Aproximación a la mediana usando intervalos 

#2. Medidas de dispersión
#pstdev(data, mu=None) – Desviación estándar de la población
datos = [10, 12, 23, 23, 16, 23, 21, 16] 
print(statistics.pstdev(datos)) # Desviación estándar de toda la población 

#pvariance(data, mu=None)  Varianza de la población
datos = [10, 12, 23, 23, 16, 23, 21, 16] 
print(statistics.pvariance(datos)) # Varianza de la población 

#stdev(data, xbar=None) – Desviación estándar de una muestra
datos = [10, 12, 23, 23, 16, 23, 21, 16] 
print(statistics.stdev(datos)) # Desviación estándar muestral 

#variance(data, xbar=None) – Varianza de una muestra
datos = [10, 12, 23, 23, 16, 23, 21, 16] 
print(statistics.variance(datos)) # Varianza de la muestra 


#3. Medidas de posición
#quantiles(data, n=4, method='exclusive') – Divide los datos en partes iguales
datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
print(statistics.quantiles(datos, n=4)) # Cuartiles de los datos 


#4. Funciones avanzadas de promedio
#harmonic_mean(data) – Media armónica (para tasas y proporciones)
datos = [40, 60, 80] 
print(statistics.harmonic_mean(datos)) # Aproximadamente 57.14 

#geometric_mean(data) – Media geométrica (útil en crecimiento exponencial)
datos = [1, 3, 9, 27, 81] 
print(statistics.geometric_mean(datos)) # Aproximadamente 9.0 

#fmean(data) – Media rápida en punto flotante
datos = [1, 2, 3, 4, 5] 
print(statistics.fmean(datos)) # Más eficiente que `mean` 

#multimode(data) – Encuentra todos los valores más repetidos
datos = [1, 2, 2, 3, 3, 4] 
print(statistics.multimode(datos)) # [2, 3] porque ambos se repiten más 

#5. Correlación y regresión
#covariance(x, y) – Covarianza entre dos listas
x = [1, 2, 3, 4, 5] 
y = [2, 4, 6, 8, 10] 
print(statistics.covariance(x, y)) # Relación entre los datos 

#correlation(x, y) – Correlación de Pearson entre dos listas
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10] 
print(statistics.correlation(x, y)) # Debe ser 1.0 (relación perfecta) 

#linear_regression(x, y) – Calcula regresión lineal (pendiente e intersección)
x = [1, 2, 3, 4, 5] 
y = [2, 4, 6, 8, 10] 
modelo = statistics.linear_regression(x, y) 
print(f"Pendiente: {modelo.slope}, Intersección: {modelo.intercept}") 





"""El módulo statistics en Python tiene solo una clase importante:"""

#Clase statistics.NormalDist
#Esta clase representa una distribución normal (Gaussiana) y permite calcular probabilidades, valores Z y generar distribuciones.

#1. Crear una distribución normal
from statistics import NormalDist 
dist = NormalDist(mu=50, sigma=10) 

# Media = 50, Desviación estándar = 10 
print(dist.mean) # 50.0 
print(dist.stdev) # 10.0 


#2. Calcular la probabilidad acumulada (CDF)
#Esta función devuelve la probabilidad de que un valor sea menor o igual a un número dado.
print(dist.cdf(60)) # Probabilidad de que un número sea menor o igual a 60 

#3. Obtener un valor a partir de una probabilidad (ICDF)
#La inversa de cdf(), devuelve el valor de X que corresponde a una probabilidad dada.
print(dist.inv_cdf(0.95)) # Valor donde la probabilidad acumulada es 95% 

#4. Multiplicación por un escalar
#Podemos escalar la distribución para modificar su media y desviación estándar.
nueva_dist = dist * 2 
print(nueva_dist.mean) # 100.0 print(nueva_dist.stdev) # 20.0 

#5. Sumar dos distribuciones normales
dist2 = NormalDist(mu=30, sigma=5) 
suma = dist + dist2 
print(suma.mean) # 80.0 (50+30) 
print(suma.stdev) # 11.18 (√(10² + 5²)) 

#6. Generar una distribución a partir de datos
#Podemos calcular una distribución normal basada en una lista de datos.
datos = [10, 20, 30, 40, 50] 
dist_datos = NormalDist.from_samples(datos) 
print(dist_datos.mean) # 30.0
print(dist_datos.stdev) # 15.81 



"""El módulo statistics no tiene variables predefinidas. Solo contiene funciones y la clase NormalDist. Si buscas valores 
estadísticos predefinidos, tendrías que usar math o scipy.stats para constantes como π o valores críticos de distribuciones."""



"""El módulo statistics no tiene constantes predefinidas. Si necesitas constantes matemáticas como π (pi) o e 
(número de Euler), puedes usar el módulo math"""



"""El módulo statistics en Python tiene dos excepciones específicas:"""

#1. statistics.StatisticsError. Se lanza cuando ocurre un error en los cálculos estadísticos, por ejemplo, cuando 
#intentamos calcular la moda en un conjunto sin un valor más frecuente. Ejemplo: Error al calcular la moda sin un valor dominante
datos = [1, 2, 3, 4] # No hay un número que se repita más veces
try: 
    print(statistics.mode(datos)) 
except statistics.StatisticsError as e: 
    print(f"Error: {e}") # No hay una moda clara 


#Ejemplo: Error con datos vacíos
datos = [] 
try: 
    print(statistics.mean(datos)) # No se puede calcular la media de una lista vacía
except statistics.StatisticsError as e: 
    print(f"Error: {e}") 

#2. ValueError (Excepción general utilizada en statistics). Algunas funciones pueden lanzar ValueError cuando los datos de entrada no son válidos.
#Ejemplo: Intentar calcular una varianza con un solo dato
datos = [5] 
try: 
    print(statistics.variance(datos)) # Se necesita al menos dos datos 
except ValueError as e: 
    print(f"Error: {e}") 

#StatisticsError → Ocurre cuando la estadística no se puede calcular correctamente.
#ValueError → Se lanza cuando los datos de entrada son inválidos.



"""El módulo statistics no tiene submódulos. Es un módulo estándar en Python que solo contiene funciones, una clase 
(NormalDist) y excepciones (StatisticsError)."""
