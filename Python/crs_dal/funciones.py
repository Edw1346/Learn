#ver el numero mas alto
v1 = {1,3,5,8}
valto1 = max(v1)    #lanza el numero mas alto
vbajo1 = min(v1)    #lanza el numero mas bajo
print(f"De {v1} el maximo es {valto1} y el menor es {vbajo1}")

#redordear un numero float, con round
v2 = 12.3456
vred2 = round(v2, 2)   #recibe 2 parametros: 1 parametro el numero a redondear, 2 parametro los decimos a redondear
print(vred2)

#El bool, deveulve false si es 0, vacio, none 
v3 = bool(0)
print(v3)

#retorna true si todos los valores son verdadero pero si hay un 0, vacio o none, dara false
v4 = [234, True, [334.25]] 
vall4 = all(v4)
print(vall4)

#suma todos los numeros
v5 = [1,45,67,32,45] 
vsum5 = sum(v5)
print(vsum5)


#Crear funciones, Built out

#Crea un funcion es con def

#crae un funcion simple, se usa def el nombre de la funcion y parentesis para los parametros
def saludar():
    print("Hola como estas")
saludar()   #se llama a la funciom

#crear una funcion con parametro
def saludo(nombre:str, sexo:str)->str:
    sexo = sexo.lower()
    if(sexo == 'mujer'):
        print(f"Hola {nombre}, mi reina como estas ?")
    elif(sexo == 'hombre'):
        print(f"Hola {nombre}, mi guapo como estas ?")
    else:
        print(f"Hola {nombre}, como estas ?")
saludo("Edwin","Hombre")


#funcion de contraseña aleatoria
def dar_contrase_aleatoria(contraseña, num):
    print(f"El numero introducido es {num}. Tu contraseña aleatoria es {contraseña}, no se la des a nadie")

def contrase_aleatoria(num:int)->str:
    num_com = num
    char1 = 'abcdefghij'
    char2 = 'klmnopqrst'
    char3 = 'uvwxyzabcd'
    char4 = '!#$%&/¡*^+'
    num_str = str(num)
    num = int(num_str[0])
    c1 = num * 3 
    c2 = num * 1 
    c3 = num * 2 
    c4 = num * 8
    c5 = num * 5
    c6 = c1 + c3 
    c7 = c4 - c5
    c1 = str(c1) 
    c2 = str(c2) 
    c3 = str(c3) 
    c4 = str(c4) 
    c5 = str(c5) 
    c6 = str(c6)
    c7 = str(c7)
    c1 = int(c1[0])
    c2 = int(c2[0])
    c3 = int(c3[0])
    c4 = int(c4[0])
    c5 = int(c5[0])
    c6 = int(c6[0])
    c7 = int(c7[0])
    contraseña = f"{char1[c1]}{char4[c3]}{char3[c2]}{c1*8}{char4[c4]}{char1[c4]}{c4*4}{char3[c4]}{char4[c3]}{c2**2}{char2[c1]}{char4[c5]}{char1[c6]}{num**3}"
    dar_contrase_aleatoria(contraseña, num_com)
    #ch1 = c1 c3 c4, ch2 = c1 c3 c4, ch3 = c2 c4 ultimo c5 y c6

contrase_aleatoria(61)

#funcion de lamda, es una fomra de simplificar funciones, pero lamda tiene limitacion, son usadas para funciones simples

#funionan con una variable, requiere 2 cosas
#1, los parametros, despues 2 puntos :. 2, la funcion que necesita hacer
funclamda = lambda x, y: x**y
print(funclamda(2, 5))


#Filter es una funcion para traer valores que concidere true, filtara valores
#Filter recorre o itera una estructura ejecutando una funcion
#para usarla hace falta tener una funcion, asignar el filter en una variable
num = [2,3,4,5,6,7,8,9]

def fun_filter(n):
    if n%2==0:
        return True

#Filter recibe parametros: 1, la funcion. 2, los parametros
var_filter1 = filter(fun_filter,num)
print(list(var_filter1))

#tambien se puede usar una funcion lambda, pero se usa en el mismo filter
var_filter2 = filter(lambda nu: nu%2==0,num)
print(list(var_filter2))
