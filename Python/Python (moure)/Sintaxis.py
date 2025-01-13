"""SINTAXIS, VARIABLES, TIPOS DE DATOS, HOLA MUNDO"""

#Comentario de linea

"""
Esto es un comentario multilinea
Puede escribirse en diferentes lineas
Se abre con tres comillas simples ( ' ) o con tres comillas dobles (Como este comentario)
"""

# Tipos de datos primitivos
CONSTANTE = "esta es sólo la manera de escribir su nombre por convencion, Python no tiene constantes"
cadena = "esto es una string"
entero = 5
flotante = 4.2
complejo = 2, 4j   #z = a, bj a= real, b=imaginario (J) 
booleano = False
lista = [1, "dos", 3]
tupla = ("uno", 2, 3.4)
diccionario = {"valor1":1,"valor2":"dos"}
#Es importante recalcar que una cosa son las funciones primitivas de python y otras son tipos de datos integrados para almacenar y manipular colecciones de elementos. 

#Imprimiendo el nombre del lenguaje
print("¡Hola, Python!")


#variables validas
#Empezas con leta [a-zA-z] o guin bajo, nunca con numeros, aunque puede tenerlo en el cuerpo de la variable
Variable = 0
_Variable = 0
variable_val = 0
variable1_valida = 0

#formas
#snake_case: minuscayua y se separa con guion bajo _ el mas usado
variable_valida = 0

#camelCase: inica con minuscula y para simular un espacio se poner la 1° letra de la palabra que sigue en mayuscula 
variableValida = 0

#UPEERCASE: toda la variable en mayuscula, pero es una convencion para CONSTANTES
CONSTANTES = 0

"""VARIABLES, TIPOS DE DATOS: EJERCICIOS"""

"""
#conversion de temperatura: celsus a fareigeit

grados = int(input("Celsius: "))

def conversion_grados(gradoss:int):
    resultado = (gradoss * 9.5) + 32
    print(f"La conversion a Farenheit es {resultado}")

conversion_grados(grados)

edad = int(input("Tu edad: "))

def conversion_a_dias(edadd:int):
    conte = 0
    anos = 365
    resultado_dia = (edadd/1)*anos
    for i in range(edadd):
        if i % 4 ==0:
            conte += 1
    resultado_dias = resultado_dia + conte
    print(f"Los {edad} en dias es: {resultado_dias}")

conversion_a_dias(edad)

dinero = int(input("Dinero sin IVA: "))

def Iva(dineroo:int, iva:int):
    monto_iva = round((dineroo * iva) / 100,3)
    print(f"El dinero {dinero} con IVA es: {monto_iva+dineroo}")

Iva(dinero, 19)

#Conversiones

num = 4
num_cero = 0
flo = 3.4
stre = 'Hola'
booo = True

int_flo = int(flo)
flo_int = float(num)
str_num = str(num)
str_flo = str(flo)
str_bool = str(booo)
boo_int1 = bool(num)
boo_int2 = bool(num_cero)
boo_str = bool(stre)


#conversion implicita

suma = num + flo
print(f"La suma de {num} y {flo} da = {suma} y es de tipo {type(suma)} en ves de ser {type(num)}: Conversion impliciota")
#Convierte el resultado: si se suma un int con un float el resultado se convierte a float

#Ambitos

variable_global = "Soy globla" #acceseble en toda el codigo

def variabl_local():
    variable_local ="Soy local" #accesible en solo esta parte del codigo
"""

"""Ejercicio avanzado"""

producto1 = {'nombre': 'Papas', 'precio': 500, 'cantidad': 6, 'categoria': 'verduras'}
producto2 = {'nombre': 'Rabanos', 'precio': 800, 'cantidad': 8, 'categoria': 'verduras'}

inventario = [producto1, producto2]
#print(f"1 producto {inventario[1]} y 2 producto {inventario[2]}")

def agregar_productos():
    diccionario = {'nombre': '',
    'precio': '',
    'cantidad': '',
    'categoria': ''}
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        categoria = input("Ingrese la categoria del producto: ")
        for dicc in diccionario.keys():
            diccionario["nombre"] = nombre
            diccionario["precio"] = precio
            diccionario["cantidad"] = cantidad
            diccionario["categoria"] = categoria
        inventario.append(diccionario)
        print("Agregado")
        break

def actualizar_producto():
    while True:
        ind = -1
        producto_a_actualizar = input("Ingrese el nombre del producto a actualizar o salir: ")
        print(producto_a_actualizar)
        if producto_a_actualizar.lower() != 'salir':
            for i in inventario:
                ind += 1
                for p in enumerate(i.items()):
                    if p[1][1] == producto_a_actualizar:
                        cambio_especifico = True
                        while cambio_especifico:
                            pregunta1 = input(f"{producto_a_actualizar} fue encontrado, que desea actualizar: Precio (1) o cantidad (2):")
                            if pregunta1 == '1' or pregunta1.lower() == 'precio':
                                if pregunta1 == '1':
                                    pregunta1 = 'precio'
                                nuevo_precio = int(input("Ingrese el nuevo precio: "))
                                inventario[ind][pregunta1] = nuevo_precio                                
                                print(f"El cambio fue exitoso: {inventario[ind]}\n")          
                                del(producto_a_actualizar)
                                actualizar_producto()
                            elif pregunta1 == '2' or pregunta1.lower() == 'cantidad':
                                if pregunta1 == '2':
                                    pregunta1 = 'cantidad'
                                nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                                inventario[ind][pregunta1] = nueva_cantidad
                                print(f"El cambio fue exitoso: De {inventario[ind]}\n")
                                del(producto_a_actualizar)
                                actualizar_producto()
                            elif pregunta1.lower() == 'atras':
                                actualizar_producto()
                            else:
                                print("Vuelva a intentarlo")
                                continue
            else:
                print(f"No fue encontrado {producto_a_actualizar}, intentelo de nuevo\n")    
        else: return


while True:
    Control = input("1. Introducir un nuevo producto 2. Actualizar inventario 3. Mostrar inventario 4. Eliminar producto: ")

    if Control == '1':
        agregar_productos()
        continue

    elif Control == '2':
        actualizar_producto()
        continue

    elif Control == '3':
        continue

    elif Control == '4':
        continue