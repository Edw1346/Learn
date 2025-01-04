"""Ejercicio 1"""
"""Curso min: 2.5h, prom: 4h, max: 7h. El que se llava es : 1.5h"""

"""
#diferencias en porcentaje

cur_min = 2.5
cur_prom = 4
cur_max = 7
cur_act = 1.5
tiem_crud_otr = 5
tiem_crud_act = 3.5

def con_hor_min(hora) -> int:
    minu = hora *(60/1)
    return minu
    

por_curMin_y_curAct = 100 - (con_hor_min(cur_act) * 100 / con_hor_min(cur_min))
por_curmax_y_curAct = 100 - (con_hor_min(cur_act) * 100 / con_hor_min(cur_max)) 
por_curprom_y_curAct = 100 - (con_hor_min(cur_act) * 100 / con_hor_min(cur_prom)) 

print(f"la diferencias entre el mas rapido y el actual es de: {por_curMin_y_curAct}%")
print(f"la diferencias entre el lento y el actual es de: {por_curmax_y_curAct}%")
print(f"la diferencias entre el promedio y el actual es de: {por_curprom_y_curAct}$")


por_tieCrud_prom = 100 - (con_hor_min(cur_prom) * 100 / con_hor_min(tiem_crud_otr))
por_tieCrud_act = 100 - (con_hor_min(cur_act) * 100 / con_hor_min(tiem_crud_act))

print(f"la diferencias tiempo, material inservible del promedio es de: {por_tieCrud_prom}%")
print(f"la diferencias tiempo, material inservible del actual es de: {por_tieCrud_act}%")

print(f"El curso actual con el curso minimo, se puede ver un: {cur_min / cur_act} de veces")
print(f"El curso actual con el curso promedio, se puede ver un: {cur_prom / cur_act} de veces")
print(f"El curso actual con el curso maximo, se puede ver un: {cur_max / cur_act} de veces")
"""










"""Ejercicio 2"""

"""
def most_resultados(maestro, asistente, asistencia):
    print(f"El maestro es {maestro} y el asistente {asistente}, la asistencia de la clase es de {asistencia}")

def mayor_edades(limite):
    edades_alumnos = []
    for i in range(limite):
        nombre = input("introduzca su nombre : ")
        edad = int(input("introduzca su edad : "))
        compañero = (nombre, edad)
        edades_alumnos.append(compañero)
        edades_alumnos.sort(key=lambda x: x[1])
        asistente = edades_alumnos[0][0]
        maestro = edades_alumnos[-1][0]
        asistencia = len(edades_alumnos)
    most_resultados(maestro, asistente, asistencia)
print(mayor_edades(2))"""

"""def llevar_al_primo(primo):
    if primo == 2:
        for i in range(primo):
            if primo/numero ==1 and numero/1 == numero and numero%2== 0:
    else:
        print("2")"""

"""
def repite_primos():
    num = int(input("Escalera de primo: "))
    if type(num) != int:
        print("Escribe un numero")
    ind_primo(num)

def llevar_primo(primo):
    escala_numero = []
    for u in range(2, primo+1):
        conteo = 0
        for e in range(1, u+1):
            if u % e == 0:
                conteo += 1
            else:
                pass
        if conteo < 3:
            escala_numero.append(u)
    else:
        return list(escala_numero)

#print(f"La escalera de primos hasta el {numer}: {list(escala_numero)}")

def ind_primo(numero:int):
    conoprimo = 0
    if numero == 1:
        print("El 1 no es numero primo")
        repite_primos()
    elif numero < 1: 
        print("Tiene que ser un numero positivo")
        repite_primos()
    elif numero >= 2:
        for i in range(1, numero+1):
            if numero % i == 0:
                conoprimo += 1
            else:
                pass
        if conoprimo == 2:
            print(f"El {numero} es primo, escalera: {llevar_primo(numero)}")
            llevar_primo(numero)
            repite_primos()
        else:
            print(f"El {numero} no es un numero primo")
    elif type(numero) != int: 
        print("Ingrese un numero")
        repite_primos()
    else:
        print("Hubo un error")
        repite_primos()

repite_primos()"""

"""def ide_primo(num:int):
    for i in range(2, num-1):
        if num % i==0:
            return False
    return True

def sec_primos():
    num = int(input("Ingrese un numero primo: "))
    secuencia_primos = []
    for u in range(num):
        resultado = ide_primo(u)
        if resultado == True:
            secuencia_primos.append(u)
        elif resultado == False:
            print(f"El numero {u}, no es primo")
            break
        else:
            pass
    return print(f"La escalera de primos es {list(secuencia_primos)}")

sec_primos()"""
"""
def figonacci(): 
    figonaci = []
    a = 1
    b = 1
    num = int(input("Ingrese un numero limite: "))
    while a+b < num :
        a, b = b, a+b
        figonaci.append(a)
    print(f"El figonacci de {num} es: {list(figonaci)}")

figonacci()
"""


"""Ejercicio 3"""
"""
nombre = ["Edwin", "Casey", "Efren", "Yuri", "Elena"]
apellido = ["Lopez","Lopez","Lorente","Miranda","Lorente"]
indice = len(nombre)

with open('Python\\eje_3.txt', 'a',encoding='UTF-8') as archivo:
    archivo.write("Los nombres son:\n")
    for i, l, m in zip(nombre, apellido, range(1, indice+1)):
        archivo.write(f"El {m}: {i} {l}\n")
    else:
        print("Finalizado")"""

"""Ejercicio 4"""


import re

def verificar_tel():
    while True:
        try:
            numero = str(input("Ingrese un numero de telefono: "))
            if numero == "":
                print("No ingreso ningun numero")
                continue
            elif numero.isalpha():
                print("No se permiten letras")
                continue
            elif re.search(r"\d", numero) and re.search(r"[a-zA-Z]", numero):
                print("Tiene que ser solo numeros")
                continue
            elif len(numero) < 8 or len(numero) > 8:
                print("Se necesita un numero de 8 digitos")
                continue
            elif len(numero) == 8:
                numero = numero[:4] + " " + numero[4:]
                print(numero)   
            else:
                pass
            cadena = f'El numero es: +506 {numero}'
            print(cadena)
            condicion = r'^[0-9]{4}+.[0-9]{4}$'
            revision = re.findall(condicion, numero)
            print(revision)

            if revision:
                resultado = re.sub(condicion,'oculto', cadena)
                print(resultado)
                print(f"Valido: {resultado}")
                break
            else:
                print(f"Invalido: {numero}")
                continue
        except Exception as e:
            print(f"Error vuelve a intentarlo: {e}")
            continue

verificar_tel()