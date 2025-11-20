#El módulo statistics sirve para hacer cálculos estadísticos básicos como media, mediana y moda.

import statistics

datos = [1, 2, 3, 4, 5] 
datos1 = [7, 3, 1, 9, 5] 
datos2 = [2, 3, 3, 5, 3, 7]
datos3 = [1, 3, 5, 7, 9, 11] 
datos4 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5] 
datos5 = [10, 12, 23, 23, 16, 23, 21, 16] 
datos6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
datos7 = [40, 60, 80] 
datos8 = [1, 3, 9, 27, 81] 
datos9 = [1, 2, 2, 3, 3, 4] 

x = [1, 2, 3, 4, 5] 
y = [2, 4, 6, 8, 10] 

#Medidas de tendencia central
#mean(data) – Calcula la media (promedio)
print(statistics.mean(datos)) # (1+2+3+4+5) / 5 = 3.0 

#median(data) – Calcula la mediana (valor central de una lista ordenada)
print(statistics.median(datos1)) # Ordenado: [1, 3, 5, 7, 9] → 5 

#mode(data) – Encuentra el valor más repetido
print(statistics.mode(datos2)) # El número 3 aparece más veces 

#median_low(data) – Devuelve la mitad inferior en caso de una mediana par
print(statistics.median_low(datos3)) # Ordenado: [1, 3, 5, 7, 9, 11] → 5 

#median_high(data) – Devuelve la mitad superior en caso de una mediana par
print(statistics.median_high(datos3)) # Ordenado: [1, 3, 5, 7, 9, 11] → 7 

#median_grouped(data, interval=1) – Estima la mediana en datos agrupados
print(statistics.median_grouped(datos4)) # Aproximación a la mediana usando intervalos 


#2. Medidas de dispersión
#pstdev(data, mu=None) – Desviación estándar de la población
print(statistics.pstdev(datos5)) # Desviación estándar de toda la población 

#pvariance(data, mu=None) – Varianza de la población
print(statistics.pvariance(datos5)) # Varianza de la población 

#stdev(data, xbar=None) – Desviación estándar de una muestra
print(statistics.stdev(datos5)) # Desviación estándar muestral 

#variance(data, xbar=None) – Varianza de una muestra
print(statistics.variance(datos5)) # Varianza de la muestra 

#3. Medidas de posición
#quantiles(data, n=4, method='exclusive') – Divide los datos en partes iguales
print(statistics.quantiles(datos6, n=4)) # Cuartiles de los datos 

#4. Funciones avanzadas de promedio
#harmonic_mean(data) – Media armónica (para tasas y proporciones)
print(statistics.harmonic_mean(datos7)) # Aproximadamente 57.14 

#geometric_mean(data) – Media geométrica (útil en crecimiento exponencial)
print(statistics.geometric_mean(datos8)) # Aproximadamente 9.0 

#fmean(data) – Media rápida en punto flotante
print(statistics.fmean(datos)) # Más eficiente que `mean` 

#multimode(data) – Encuentra todos los valores más repetidos
print(statistics.multimode(datos9)) # [2, 3] porque ambos se repiten más 

#5. Correlación y regresión
#covariance(x, y) – Covarianza entre dos listas
print(statistics.covariance(x, y)) # Relación entre los datos 

#correlation(x, y) – Correlación de Pearson entre dos listas
print(statistics.correlation(x, y)) # Debe ser 1.0 (relación perfecta) 

#linear_regression(x, y) – Calcula regresión lineal (pendiente e intersección)
modelo = statistics.linear_regression(x, y) 
print(f"Pendiente: {modelo.slope}, Intersección: {modelo.intercept}") 




#El módulo statistics en Python tiene solo una clase importante:

#Clase statistics.NormalDist: Esta clase representa una distribución normal (Gaussiana) y permite calcular probabilidades, valores Z y generar distribuciones.

#Crear una distribución normal
from statistics import NormalDist 
dist = NormalDist(mu=50, sigma=10)  # Media = 50, Desviación estándar = 10 
print(dist.mean) # 50.0 
print(dist.stdev) # 10.0 

#Calcular la probabilidad acumulada (CDF). Esta función devuelve la probabilidad de que un valor sea menor o igual a un número dado.
print(dist.cdf(60)) # Probabilidad de que un número sea menor o igual a 60 

#Obtener un valor a partir de una probabilidad (ICDF). La inversa de cdf(), devuelve el valor de X que corresponde a una probabilidad dada.
print(dist.inv_cdf(0.95)) # Valor donde la probabilidad acumulada es 95% 

#Multiplicación por un escalar. Podemos escalar la distribución para modificar su media y desviación estándar.
nueva_dist = dist * 2 
print(nueva_dist.mean) # 100.0 print(nueva_dist.stdev) # 20.0 

#Sumar dos distribuciones normales
dist2 = NormalDist(mu=30, sigma=5) 
suma = dist + dist2 
print(suma.mean) # 80.0 (50+30) 
print(suma.stdev) # 11.18 (√(10² + 5²)) 

#Generar una distribución a partir de datos. Podemos calcular una distribución normal basada en una lista de datos.
datos = [10, 20, 30, 40, 50] 
dist_datos = NormalDist.from_samples(datos) 
print(dist_datos.mean) # 30.0
print(dist_datos.stdev) # 15.81 


#El módulo statistics no tiene submódulos. Es un módulo estándar en Python que solo contiene funciones, una clase (NormalDist) y excepciones (StatisticsError).


