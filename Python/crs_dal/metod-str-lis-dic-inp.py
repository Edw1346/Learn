""""
'capitalize', 'casefold', 'center',
count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index',
'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 
'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 
'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 
'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 
'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill"""

"""
strig = "edwin"
print(strig)

print(f"capitalize: primera letra mayuscula {strig.capitalize()}")
print(strig.casefold())
print(f"cuenta las coincidencias {strig.count('edw')}")
print(f"termina con {strig.endswith('e')}")
print(strig.startswith('edwin'))
print(f"encuentra una cadena, sino lanzar un error {strig.find('i')}")
print(strig.format(True))
print(strig.index('in'))
print(f"Si numerico, solo numero {strig.isnumeric()}")
print(f"si una cadena de caracteres de a-z {strig.isalpha()}")
print(f"cambia a minusculas {strig.lower}")
print(f"cambia a mayusculas {strig.upper()}")
print(f"cambia cadenas {strig.replace('n','n alexander')}")
print(f"separa cadenas y la vuerle una lista: {strig.split('i')}")


#Metodo de lista
lista = list([1, 2, 3, 4]) #crea una lista, tiene que ir con parentesis cuadrados []
len(lista) #cuantos elementos hay en la lista
lista.append(5) #agrega un elemento
lista.insert(5, 6)  #agrega un elemento a un indice: 1p, indice y 2p, elemento
lista.extend([7, 8, 9])   #agrega varios elementos, tiene que tener los parentice cuadrados []
lista.pop(0)    #elimina un elemento segun el indice: 1p indice
lista.remove(1) #busca un elemento y lo elimina, sino lo encuentra genera un error: 1p elemento a buscar
lista.clear()   # elimina todos los elementos
lista.sort()    #ordena la lista ascendente jerarquia: bool, int, floot, tiene que ser solo bool y numeros
"""

"""
dict = {
    "one": 'im firts',
    "segund": 'im segund',
    "three": 'im third'
}

print(dict)

kys = dict.keys() #devuelve las claves
print(kys)

ver = dict.get("three") #ver los valores de las claves
print(ver)

ite = dict.items() #crea un objeto que se pueda iterar
print(ite)

lim = dict.clear() #eliminar todas las claves y valores
print(lim)"""


#input

intpu = input("esbribe algo: ")
print(intpu)

