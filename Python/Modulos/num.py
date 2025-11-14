import numpy as np

"""Matrices"""
arr1 = np.array([1,2,3,4,5,6])
arr1m = np.append(arr1,[2.3434,5.454,6.45654]) 
arr2 = np.array([0,1,2,3])
arr3 = np.array([1,2,3])
arr4 = np.array([1,2,3])
arr5 = np.array([arr3,arr4])
arr6 = np.array([1,2])
arr7 = np.array([1,3])
arr8 = np.array([5,6])
arr9 = np.array([arr6,arr7])

print("Matrices (m)")
print(f"m1 {arr1}")
print(f"m1m {arr1}")
print(f"m2 {arr2}")
print(f"m3 {arr3}")
print(f"m4 {arr4}")
print(f"m5 {arr5}")
print(f"m6 {arr6}")
print(f"m7 {arr7}")
print(f"m8 {arr8}")
print(f"m9 {arr9}\n")


"""Operaciones"""
print("Operaciones (arr3 y arr4)")
print(f"sumar {np.add(arr3,arr4)}")
print(f"restar {np.subtract(arr3,arr4)}")
print(f"multiplicar {np.multiply(arr3,arr4)}") #Para multiplicacion entera es np-floor_power
print(f"dividir {np.divide(arr3,arr4)}") #Para division entera es np-floor_divide
print(f"potencia {np.power(arr3, arr4)}") 
print(f"modulo {np.mod(arr3, arr4)}") #Resto de la division
print(f"modulo2 {np.remainder(arr3, arr4)}") #Similar a mod pero respeta signo
print(f"raiz (solo arr3) {np.sqrt(arr3)}\n")

"""Estadistica"""
print("Estadisticas (solo arr1)")
print(f"sumatoria {np.sum(arr1)}") #suma de todos los valores
print(f"media {np.mean(arr1)}") #Promedio de todos los valores
print(f"Desviacion {np.std(arr1)}") #desviacion estandar (raiz)
print(f"Varianza {np.var(arr1)}") #varianza de los elementos (Al cuadrado)
print(f"Mediana {np.median(arr1)}") #mediana de los elementos
print(f"Minimo {np.min(arr1)}") #minimos de los elementos
print(f"Maximo {np.max(arr1)}\n") #maximo de los elementos

"""Algebra lineal"""
print("Algabra lineal (varias)")
print(f"producto punto (arr3 y arr4) {np.dot(arr3,arr4)}") #Producto punto
print(f"Matriz-matriz (2 de arr1) {np.matmul(arr1, arr1)}") #
print(f"Transparencia (arr1) {arr1.T}")
print(f"inversa de matriz (arr9) {np.linalg.inv(arr9)}") #se necita una matrix cuadrada 2x2
print(f"Determinante (arr9) {np.linalg.det(arr9)}") #se necita una matrix cuadrada 2x2
print(f"Valores y vectores propios (arr9) {np.linalg.eig(arr9)}") #se necita una matrix cuadrada 2x2
print(f"Rango de una matriz (arr1) {np.linalg.matrix_rank(arr1)}") #
print(f"Magnitud de un vector o matrix (arr1) {np.linalg.norm(arr1)}") #
print(f"Resolver ecuaciones lineales (arr9 y arr8) {np.linalg.solve(arr9, arr8)}")
val, vec = np.linalg.eig(arr9) #valores y vectores propios
print(f"(arr9) Valores: {val} y vectores propios {vec}")
u, s, vt = np.linalg.svd(arr9) #Descomposicion SDV (Singular, value, descomposition)
print(f"(arr9) U: {u}, S= {s}, Vt={vt}")
print(f"Pseudoinversa (arr9) {np.linalg.pinv(arr9)}") #Pseudoinversa (Matriz de moore-Penrose)
print(f"Condicion numerica (arr9) {np.linalg.cond(arr9)}") #Estabilidad numerica
print(f"Traza (arr9) {np.trace(arr9)}") #Suma de la diagonal principal
print(f"Singular (arr9) {np.allclose(arr9, arr9.T)}") #Si es simetrica, identidad
print(f"Simetrica (arr9) {np.isclose(np.linalg.det(arr9), 0)}\n") #Si es singular (Determinante 0) 

"""Ordenar, combinar y dividir"""
print("Ordenar, combinar y dividir")
print(f"sort (arr1) {np.sort(arr1)}") #copia y ordena
print(f"split (arr1) {np.split(arr1, 3)}") #divide en partes (segun se coloque)
print(f"append (arr1) {np.append(arr1,[2.3434,5.454,6.45654])}") #agregar valores al array
print(f"concatenate (arr3 y arr4) {np.concatenate([arr3, arr4])}") #une arrays
print(f"hstack (arr3 y arr4) {np.hstack([arr3, arr4])}") #apila array horizontalmente
print(f"vstack (arr3 y arr4) {np.vstack([arr3, arr4])}") #apila array verticalmente
print(f"copia (arr4) {np.copy(arr4)}") #copia arreglo
print(f"unique (arr1) {np.unique(arr1)}") #copia sin valores repetidos
print(f"espand_dims (nueva) {np.expand_dims(arr3, axis=0)}") #Añada una dimencion
print(f"squeeze (nueva) {np.squeeze(np.array([[1,2,3]]))}") #quita dimenciones vacias
print(f"reshape (arr1) {np.reshape(arr1, (3,2))}") #rearma array: 2 (arrays) 3 (Valores en esos array)
print(f"ravel (arr5) {np.ravel(arr5)}") #convierte un array multidimencional en un unimencional

"""Trigonometria, exponentes, logaritmos, etc"""
print("Trigonometria, exponentes, logaritmos, etc (solo arr3)")
print(f"seno (arr3) {np.sin(arr3)}") #
print(f"coseno (arr3) {np.cos(arr3)}") #
print(f"tangente (arr3) {np.tan(arr3)}") #
print(f"exponente (arr3) {np.exp(arr3)}") #
print(f"logaritmos (arr3) {np.log(arr3)}") #
print(f"logaritmo base 10 (arr3) {np.log10(arr3)}") #
print(f"abs (arr3) {np.abs(arr3)}\n") #valores absolutos de los elementos del array
#Tambien se puede el arco(seno, coseno, tangente): np.arcsin, coccos, arctan, arctan2 (tangemte inversa)(array) -- 
#COnvertir grados a radianes: np.deg2rad(array)
#COnvertir radianes a grados: np.rad2ded(array)
#hiperbolicos np.sinh cosh tanh(array)
#inverso hiperbolicos np.arcsinh arccosh arctanh(array)

"""Aleotorio"""
print("Aleotorio")
print(f"(nueva) aleatorio (0 o 1) {np.random.rand(2,3)}") #Entre 0 a 1
print(f"Enteros (nueva) {np.random.randint(0,10,(3,3))})") #
print(f"distribucion (nueva) {np.random.normal(0,1,100)}\n") #

"""Funcionalidades"""
print("Funcionalidades")
print(f"where (arr1) {np.where(arr1 <4)}") #indice los valores que cumplen la condicion
print(f"clip (arr1) {np.clip(arr1, 2,5)}") #Recorta valores del rango
print(f"all (arr3) {np.all(arr3)}") #True si todo no son 0
print(f"any (arr2) {np.any(arr2)}") #True si al menos 1 no es 0
print(f"aruond (arr1m) {np.around(arr1m,1)}") #redondear entero cercano
print(f"floor (arr1m){np.floor(arr1m)}") #redondear abajo
print(f"ceil (arr1m){np.ceil(arr1m)}") #redondear arriba
print(f"trunc (arr1m){np.trunc(arr1m)}") #redondear arriba
print(f"argmax (arr1) {np.argmax(arr1)}") #Numero mayor
print(f"argmin (arr3) {np.argmin(arr3)}") #NUmero menor
print(f"arange (nueva) {np.arange(0, 10, 2)}") #crea array rango: 0 (inicio) 10 (final) 2 (secuencia)
print(f"linspace (nueva) {np.linspace(0, 10, 5)}") #crea array rango en un equidistantes (porcion equitativa): 0 (inicio) 10 (final) 2 (las partes cuales cuales divide)
print(f"transpose (arr5) {np.transpose(arr5)}\n") #transpuesta de un arreglo multidimencional

#print(f" {np.}") #
#print(f" {}") #