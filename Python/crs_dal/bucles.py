animal = ["gato", "perro", "loro", "cocodrilo", "leon"]
numeros = [2, 4, 6, 8, 10, 12]

#recorrer la lista, imprime cada elemento
for animales in animal:
    print(animales)

#recorrer una lista y manipulos los datos
for num in numeros:
    resulta = num * 2
    print(resulta)

#recorres 2 lista, en cada interacion recorre el mismo indice de cada lista
cont = 0
for numu, anim in zip(numeros, animal):
    cont +=1
    print(f"soy el elemento: {numu} de numeros, estamos en la interacion numero {cont}")
    print(f"soy el elemento: {anim} de animales, estamos en la interacion numero {cont}")


#recorrer con un rango con 1 parametro, inicia de 0 hasta el parametro
for i in range(5):
    print(i)

#recorrer con un rango con 1 parametro, numero de inicio, 2 parametro, limite de numero
for a in range(0, 6):
    print(a)

#recorrer por el indice de una lista o estructura, enumerate recibe 2 valores en cada iteracion
#1° valor: el indice, 2° valor: el valor de ese indice
for e in enumerate(numeros):
    indice = e[0]
    valor = e[1]
    print(f"El inidce {indice}, y el valor {valor} de la lista numero")

#usando un else, este se ejecuta al finalizar el for
for o in numeros:
    print(o)
else:
    print("finaliza el bucle")

#forma de añadir datos a otra estructura
numeros1 = [2, 4, 6, 8, 10, 12]
numeros_duplicados = []

for num in numeros1:
    numeros_duplicados.append(num*2)
    print("se add el numero duplicado a numeros_duplicados")
print(numeros_duplicados)


#forma simplificar de añadir datos en otra estructura en una sola linea
numeros_duplicados1 = [x*2 for x in numeros1]
print(numeros_duplicados1)

#para hacer for de una linea, hay que hacern en parenteisis como lista []
#se coloca la condicion primero y despues la estructura del for
[print(f"Hola {i} eres el {u}") for i, u in zip(numeros, animales)]


#todas esta formas funciona en listas, conjuntos y tuplas

#diccionarios
diccionario1 = {'nombre': "edwin", 'apellido': "lopez", 'edad': 20}
print(diccionario1)

#recorrer claves, cuando se usa un forma solo da los key
for key in diccionario1:
    print(key)

#recorrer valores, para hacer se usa item y recibe 2 valores en cada iteracion
#1° valor: el indice, 2° valor: el valor de ese indice
for val in diccionario1.items():
    indice = val[0]
    valor = val[1]
    print(f"el indice {indice} y el valor es {valor}")

    
#herramientas para los bucles
comida = ["manzana", "pera", "coco", "banano", "naranja"]

#iteracion normal
for com in comida:
    print(com)

#iterar con continue, hace un salo en el codigo para que vuelva a iterar con el siguiente elemento
for com in comida:
    if com == 'coco':
        print(f"voy a saltarme con un continue el elemento {com}")
        continue
    print(com)

#iterar con break, lo que hace es que corta el codigo, se sale de los bucles y condicionales
#con el break se sale de los bucles y condicionales incluido sus elses
for com in comida:
    if com == 'coco':
        print(f"voy a salir del for con un break el elemento {com}")
        break
    print(com)


#recorrer cadenas
cadena = "Hola Edwin"

#recorre una cadena, ir leta por letra
for caracter in cadena:
    print(caracter)


#Bucle white

contador = 0

while contador < 10:
    contador +=1
    print(contador)


