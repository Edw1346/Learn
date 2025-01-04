"""#crear una estructura
tuplapr = ("Edwin","Lopez","Miranda", 20, 20.2004)

#desempaquetar datos, se selecionan un nombre
nombre, apellidopri, apellidosed, edad, añonaci = tuplapr
print(apellidopri)

#cada elemento se le asigna un nombre y se trata de un solo paquete, de manera que cada elemento es una variable



#crear una tupla
#tupla con el tuple
tuplanormal = tuple(["hol1", "hol2"]) 

#tupla sin parentesis con multiple datos
tuplamult = "hol3", "hol4"

#tupla con un solo valor sin parentesis
tuplauni = "hol5",

print(type(tuplauni))




#conjuntos
conjunto = set(["dat1","dat2"])

#meter un conjunto dentro de otro, solo una manera con frozenset
conjunto1 = frozenset(["dat1", "dat2"])
conjunto2 = {conjunto1, "dat3", "dat4"}

print(conjunto2)
#teoria de conjunto, que hay datos de un conjunto dentro de otro conjunto

conjunto3 = {1,3,5,7} #el conjunto que tiene datos de otros se llama superconjunto
conjunto4 = {3,5,7} #el conjunto que sus datos estan en otro es subconjunto

#da true si es un subconjunto 
resultasubconj = conjunto4.issubset(conjunto3) 
resultasubconjot = conjunto4 <= conjunto3 #otra manera de saber si es un subconjunto
print(resultasubconj)

#da true si es un superconjunto
resultasupconjot = conjunto3 > conjunto4
print(resultasupconj)

#saber si hay un dato en comun en conjuntos
conjunto5 = {1,2,3,4}
conjunto6 = {1,5,6,7}

#da true si no hay dato en comun, tiene que ser todos diferentes
datoencomun = conjunto5.isdisjoint(conjunto6)
print(datoencomun)
"""
#crear un diccionario con dict, solo se coloca la clave (como variables) y valor
diccionario = dict(nombre = "edwin", apellido = "lopez")
print(diccionario)

#crear un diccionario con parentesis {}, se colocar la clave en comillas, 2 puntos :, y el valor segun su tipo
diccionario1 = {'nombre': "edwin", 'apellido': "lopez"}
print(diccionario1)

#crear un diccionario, que contenga un conjunto, con frozenset, el cual sera la key
diccionario3 = {frozenset([" edwin", "Lopez"]):"miranda"}
print(diccionario3)

#crear un diccionario con fromkeys, con 2 parametros: 
#1 parametro, las key (el tamaño del dict depende de este parametro de key, que sera cada letra de este parametro)
#2 parametro, los valores que estaras en cada key
diccionario4 = {'nombre': "edwin", 'apellido': "lopez"}
diccionario4 = diccionario4.fromkeys("nombre","value")
print(diccionario4)

#crear un diccionario con fromkeys, con 1 parametros, una lista []: 
#1 parametro, las key (el tamaño del dict depende de este parametro de key, que sera cada elemento)
#las values son none
diccionario5 = {'nombre': "edwin", 'apellido': "lopez"}
diccionario5 = diccionario5.fromkeys(["nombre","apellido"])
print(diccionario5)

#crear un diccionario con fromkeys, con 2 parametros: 
#1 parametro, las key (el tamaño del dic depende de este parametro de key, que sera cada letra de este parametro)
#las values son none
diccionario6 = {'nombre': "edwin", 'apellido': "lopez"}
diccionario6 = diccionario6.fromkeys("ABCDE")
print(diccionario6)