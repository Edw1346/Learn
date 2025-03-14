import random

"""El módulo random en Python proporciona funciones para generar números aleatorios y realizar selecciones aleatorias. 
Es útil cuando necesitas simular eventos aleatorios, como generar números aleatorios en un rango, mezclar elementos 
de una lista, o elegir un valor al azar de una secuencia. El módulo utiliza un generador de números pseudoaleatorios, 
lo que significa que los números son generados de manera que parecen aleatorios, pero en realidad son determinísticos 
y dependen de una semilla inicial."""




"""Funciones del módulo random"""

#random.random() Devuelve un número flotante aleatorio en el intervalo [0.0, 1.0). Ejemplo:
print(random.random()) # Ejemplo de número aleatorio entre 0 y 1 

#random.randint(a, b) Devuelve un número entero aleatorio en el rango [a, b], ambos inclusive. Ejemplo:
print(random.randint(1, 10)) # Número aleatorio entre 1 y 10 

#random.choice(sequence) Elige un elemento aleatorio de una secuencia (lista, tupla, cadena, etc.). Ejemplo:
items = ['apple', 'banana', 'cherry'] 
print(random.choice(items)) # Elige un elemento aleatorio de la lista 

#random.shuffle(sequence) Mezcla los elementos de una lista de manera aleatoria (modifica la lista en el lugar). Ejemplo:
items = [1, 2, 3, 4, 5]
random.shuffle(items) 
print(items) # Los elementos serán mezclados aleatoriamente 

#random.sample(population, k) Devuelve una lista de k elementos seleccionados aleatoriamente de la población, sin repetición. Ejemplo:
items = [1, 2, 3, 4, 5] 
print(random.sample(items, 3)) # 3 elementos aleatorios de la lista 

#random.uniform(a, b) Devuelve un número flotante aleatorio en el intervalo [a, b]. Ejemplo:
print(random.uniform(1, 10)) # Número flotante aleatorio entre 1 y 10 

#random.triangular(low, high, mode) Devuelve un número flotante aleatorio de una distribución triangular entre low y high, con el valor más probable en mode. Ejemplo:
print(random.triangular(1, 10, 5)) # Número aleatorio triangular 

#random.betavariate(alpha, beta) Devuelve un número flotante aleatorio de una distribución beta, que está definida por los parámetros alpha y beta. Ejemplo:
print(random.betavariate(2, 5)) # Distribución beta con parámetros 2 y 5 

#random.expovariate(lambd) Devuelve un número flotante aleatorio de una distribución exponencial con la tasa de lambda lambd. Ejemplo:
print(random.expovariate(1.5)) # Distribución exponencial con lambda=1.5 

#random.gammavariate(alpha, beta) Devuelve un número flotante aleatorio de una distribución gamma con parámetros alpha y beta. Ejemplo:
print(random.gammavariate(2, 2)) # Distribución gamma con parámetros 2 y 2 

#random.gauss(mu, sigma) Devuelve un número flotante aleatorio de una distribución normal (gaussiana) con media mu y desviación estándar sigma. Ejemplo:
print(random.gauss(0, 1)) # Distribución normal con media 0 y desviación 1 

#random.lognormvariate(mu, sigma) Devuelve un número flotante aleatorio de una distribución log-normal con parámetros mu (media) y sigma (desviación estándar). Ejemplo:
print(random.lognormvariate(0, 1)) # Distribución log-normal con media 0 y desviación 1 

#random.normalvariate(mu, sigma) Devuelve un número flotante aleatorio de una distribución normal con parámetros mu (media) y sigma (desviación estándar). Ejemplo:
print(random.normalvariate(0, 1)) # Distribución normal con media 0 y desviación 1 

#random.vonmisesvariate(mu, kappa) Devuelve un número flotante aleatorio de una distribución von Mises, que es una distribución circular (como la normal para ángulos). Ejemplo:
print(random.vonmisesvariate(0, 1)) # Distribución von Mises con parámetros 0 y 1 

#random.paretovariate(alpha) Devuelve un número flotante aleatorio de una distribución Pareto con el parámetro alpha. Ejemplo:
print(random.paretovariate(2)) # Distribución Pareto con parámetro alpha=2 

#random.weibullvariate(alpha, beta) Devuelve un número flotante aleatorio de una distribución Weibull con parámetros alpha y beta. Ejemplo:
print(random.weibullvariate(1, 1)) # Distribución Weibull con parámetros 1 y 1 




"""El módulo random de Python no tiene clases definidas, ya que se centra principalmente en proporcionar funciones 
"para la generación de números aleatorios y manipulación de secuencias. A diferencia de otros módulos más complejos, 
"como datetime, que sí tienen clases, el módulo random no se organiza en torno a clases, sino a funciones que puedes 
"utilizar de manera directa."""


"""El módulo random en Python no tiene variables específicas que estén definidas globalmente. Sin embargo, puede 
"haber algunos valores internos que el módulo utiliza para generar números aleatorios, pero no se exponen directamente 
"como variables accesibles para el usuario."""


"""El módulo random de Python no tiene constantes definidas de manera explícita. Sin embargo, se pueden encontrar algunos 
parámetros predefinidos y valores que son utilizados internamente en las funciones, como los parámetros de las 
distribuciones o los valores por defecto en ciertos métodos, pero no están explícitamente etiquetados como "constantes."""




"""El módulo random de Python no define excepciones específicas propias, pero las funciones del módulo pueden generar 
excepciones estándar de Python si los parámetros proporcionados no son válidos o si ocurre algún otro tipo de error 
durante su ejecución. Algunas de las excepciones comunes que puedes encontrar al usar el módulo random incluyen:"""

#ValueError Se lanza cuando un argumento no válido se pasa a una función. Por ejemplo, al usar random.sample() con un valor de k mayor que la longitud de la población, o al pasar un tipo incorrecto en funciones como randrange(). Ejemplo:
try: 
    random.sample([1, 2, 3], 5) # k es mayor que el tamaño de la población
except ValueError as e: 
    print(f"Error: {e}") # 'Sample larger than population' 

#TypeError Ocurre si se pasa un tipo incorrecto de argumento a una función. Por ejemplo, si pasas un objeto no iterable a funciones como random.choice() o random.sample(). Ejemplo:
try: 
    random.choice(12345) # No se puede elegir de un número entero 
except TypeError as e: 
    print(f"Error: {e}") # 'argument must be a sequence' 

#IndexError Puede ocurrir si se intenta acceder a un índice fuera de los límites de una secuencia cuando se usa una función como random.choice(). Ejemplo:
try: 
    empty_list = [] 
    random.choice(empty_list) # Intentando elegir un elemento de una lista vacía 
except IndexError as e: 
    print(f"Error: {e}") # 'Cannot choose from an empty sequence' 



"""El módulo random en Python no tiene submódulos. Todo lo que ofrece está contenido dentro del propio módulo, sin 
dividirse en submódulos adicionales."""
