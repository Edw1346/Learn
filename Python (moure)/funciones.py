# Func sin parametros ni retorno
def sin_param_retorno():
    print('Funcion no devuelve nada ni tiene parametros')

# Func con varios parametros con retorno
def suma(num1:int , num2:int):
    return num1 + num2

# Funciones dentro de funciones
def fun_dentro(param1:int,param2:int):
    def suma(n1,n2):
        return n1 + n2
    return suma(param1,param2)

# Funcion con parametros por defecto
def fun_param_defecto(nombre = 'Abel', apellido = 'Perez'):
    return f'Bienvenido, {nombre} {apellido}' 


#Funciones integradas en el lenguaje:
print("El print es una funcion de Python")

a="El len() también lo es"
print(len(a))

#Existen tambien las funciones lambda, que son funciones anónimas pequeñas
multiplicacion=lambda a,b,c : a*b*c
print(multiplicacion(10,3,5))
#Tambien se pueden declarar y llamar en la misma linea
print((lambda var1,var2 : var1**var2)(2,3))

#EXTRA
def ej_extra(a,b):
    for i in range(1,101):
        if not i%3 and not i%5:
            print(a,b)
        elif not i%3:
            print(a)
        elif not i%5:
            print(b)
        else:
            print(i)

ej_extra("pen","pineapple")

#Funcion lambda es una función anónima que se puede usar para hacer una función en una sola linea
#Funcion lambda con un parametro
suma = lambda x: x + 10
print(suma(5))

#Funcion lambda con varios parametros
nombre_completo = lambda nombre, apellido: f"{nombre} {apellido}"
print(nombre_completo("Laura", "Gonzalez"))

#Funcion lambda con varios parametros y operaciones
resta = lambda x,y,z,w: x - y + z / w
print(resta(10,2,3,2))

#Funcion recursiva es una función que se llama a si misma
def factorial(numero = 4):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

print(factorial())

#Funcion con argumentos es una función que recibe un número indeterminado de argumentos
def suma_con_args(*args):
    return sum(args)

print(suma_con_args(1,2,3,4,5))

# Función con diccionarios de argumentos variables 
def estadisticas_temperaturas(*temps, **kwargs):
    media = sum(temps)/len(temps)
    suma = sum((i - media)**2 for i in temps)
    devstd = (suma/(len(temps)-1))**0.5
    if kwargs.get('promedio'):
        print(f"El promedio de las temperaturas es {media} grados")
    if kwargs.get('desviacion'):
        print(f"El desviación estándar de las temperaturas es {round(devstd,3)} grados")

estadisticas_temperaturas(1,2,3,4,5,6,promedio=True,desviacion=True)


## Variables locales y globales en funciones

def variable_locall():
    variable_local = "Valor variable local"
    print(variable_local)
    
variable_locall()

variable_global = "Valor variable global"

def variable_globall():
    global variable_global
    variable_global = "Nuevo valor variable global"
    print(variable_global)
    
variable_globall()