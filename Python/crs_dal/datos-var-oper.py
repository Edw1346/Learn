"""num = 12
cad = "Hola"
bol = True
flo = 9.4

lista = ["hola", False, 23, 5.6]
tupla = ("el1", True, 32, 6.5)
conjunto = {3.4, 12, False, "el4"}
diccionario = {
    "inte":2,
    "cade": "el2",
    "boo": True,
    "floo": 4.3
}
lista.append(56)
conjunto.add(33)
conjunto.add(True)

diccionario["nuevo"] = "el5"

print(lista)
print(tupla)
print(conjunto)
print(diccionario)

sum1 = 4 + 8
print(sum1)
res = 5 - 3
print(res)
mul = 6 * 2
print(mul)
div = 66 / 11
print(div)
pot = 3 ** 4
print(pot)
divb = 55 // 4
print(div)

and1 = True and True
print(and1)
or1 = True or False
print(or1)
not1 = not False
print(not1)

igua = 2 == 2
diferent = 2 != 3
menor = 3 < 11
mayor = 5 > 3
ig_meno = 4 <= 3
ig_may = 5 >= 7

if sum1 > 18:
    print("Eres mayor de edad")
elif sum1 < 18 and res < 5:
    print("Eres un malo")
else: 
    print("Pura vida")
print (f"El and: True todas las condiciones debe de ser true: 2+2=4 and 3*3=8 es {2+2==4 and 3*3==8}")
print (f"El or: True una condicion es true: 2+2=4 and 3*3=8 es {2+2==4 or 3*3==8}")
print (f"El not: da la contraria del valor obtenido: !2+2=4 es {not 2+2==4}")"""


"""l1 = 3 
l2 = 3

l3 =3
l4 = l3

print(f"IS: solo compara posion: l1 is l2 es: {l1 is l2}")
print(f"IN: compara valor: l1 in l2 es: {'3' in '223454'}")
print(f"IS: solo compara posion: l3 is l4 es: {l3 is l4}")
print(f"IN: compara valor: l3 in l4 es: {'3' in 'l4'}")"""


lista = [["hola11", "hola12", "hola13"], ["hola21", "hola22", "hola23"], ["hola31", "hola32", "hola33"]]
buscar = "hola22"

if type(lista) == list:
    print("entre en el if")
    for i in range(0, 3):
        print("entre en el for")
        for l in range (i):
            print("entre en el for2")
            if buscar is i:
                print(f"Objeto encontrado: El elemento {buscar} fue encontrado en la lista, en el indice {i}")
            else: 
                print(f"El objeto {buscar} no fue encontrado")        
