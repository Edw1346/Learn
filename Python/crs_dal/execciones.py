#accione cuando ocurre un error o interrupcion del programa

#crear execciones
class MiExeccion(Exception):
    def __init__(self, err):
        print("Hola tonto cometiste un erro {err}")


def suma():
    while True:
        try:
            a = int(input("Numero 1: "))
            b = int(input("Numero 2: "))
        #Este simepre se ejeuta como parte del codigo normal, es para realizar exepciones
            resultado = a / b
        #Es para manejar las execciones
        except ValueError :
            print("Ingrese un numero")
            continue
        except ZeroDivisionError :
            print("No puedes dividir por 0")
            continue
        #se ejecuta si el try es true, o si no hay execciones
        else:
            break
        finally:
            print("Finalizado")
        print(resultado)

print(suma())

#Execciones:
#ValueError
#ZeroDivisionError

try:
    raise MiExeccion("Eres un crak")