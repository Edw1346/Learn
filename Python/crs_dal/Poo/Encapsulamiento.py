"""Encapsulamiento"""
# Es la capacidad de un objeto de ocultar sus atributos y métodos internos del mundo exterior.

class CuentaBancaria1:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo  # Atributo privado, estos siempre llevan un guin bajo _


#Atributo muy privado

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo muy privado, estos siempre llevan 2 guin bajo __

    def depositar(self, cantidad):
        self.__saldo += cantidad #Atributo muy privado

    def retirar(self, cantidad):
        if cantidad <= self.__saldo: #Atributo muy privado
            self.__saldo -= cantidad
        else:
            print("Saldo insuficiente")

    def mostrar_saldo(self):
        print(f"Saldo: {self.__saldo}")

#convencion: los privados en python son los protegidos(__), los muy privados son los privados

"""Getters y Setter"""
#Getters, Funcion para acceder a atributos privados o muy privados
#Setter, Funcion para usa para modificar o establecer el valor de un atributos privados o muy privados

class Persona1():
    def __init__(self, __nombre, __edad):
        self.__nombre = __nombre
        self.__edad = __edad
    
    def get_nombre(self): #Accede a los atributos privados porque las funciones estan dentro de la clase
        return self.__nombre
    

    def set_nombre(self, new_nombre): #Modifica a los atributos privados porque las funciones estan dentro de la clase
        self.__nombre = new_nombre

Persona12 = Persona1("Edwin", 20)
nombre = Persona12.get_nombre()
print(nombre)

Nombre1 = input("Introduzca un nuevo nombre: ")

Persona12.set_nombre(Nombre1)
Nombre1 = Persona12.get_nombre()
print(Nombre1)


"""Decorador"""

#Es una funcion que decora otra funcion, agrega funcionalidad y devuele 
#la funcion modificada pero no cambia la funcion original

#Crear un decorador
def decorador(funcion):
    def funcion_modificada(*arg, **kwargs): #Crea la funcion para añadir, y el parametro es la funcion principal
        print("Hacer algo, 1") #Agregar algo al inicio, antes de la principal
        resultado1 = funcion(*arg, **kwargs) #Ejecutar la funcion principal, es la misma que se pone en el parametro
        print("Hacer algo, 2") #Agregar algo al final, despues de la principal
        return resultado1
    return funcion_modificada #retornar para que sea agarrable de una variable


#Llamar al decorador con la funcion principal, pero  esta forma no estan optimo
def saludar(): #Crear la funcion principal
    return "Hola soy tu" 

saludo_modificado = decorador(saludar) #Variable para guardar la funcion decorador con la funcion principal
print(saludo_modificado()) #llamar a la funcion de decoracion 


#Forma optima

print("Forma optima")
@decorador #Con el @ asignamos la funcion decorador a la funcion principal, esta debe de estar debajo de ella 
def saludo(): #Crear la funcion principal
    print("Hola soy tu") 

saludo() #Esta funcion ya tiene el decorador y la funcion


#Hay otros tipos de decoradores: con argumentos, multiple, de clases y otros mas 




#Property en Getters
#Atributy en Setters

class Persona2():
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    @property #Hace que esta funcion sea una metodo en vez de una funcion, muestra el atributo privado
    def nombre(self): #Accede a los atributos privados porque las funciones estan dentro de la clase
        return self.__nombre #Debe de tener el nombre del atributo que deseas mostrar
    
    @nombre.setter #tiene que tener el atributo donde se hace el setter
    def nombre(self, new_nombre): #Debe de tener el nombre del atributo que deseas mostrar
        self.__nombre = new_nombre #Modifica a los atributos privados porque las funciones estan dentro de la clase

    @nombre.deleter #Elimina el atributo privado
    def nombre(self): #Accede a los atributos privados porque las funciones estan dentro de la clase
        del self.__nombre #Debe de tener el nombre del atributo que deseas eliminar

Persona21 = Persona2("Adrian", 30)
nombre21 = Persona21.nombre #Es un metodo no ocupa parentesis ()
print(nombre21)

Nombre2 = input("Introduzca un nuevo nombre: ")

Persona21.nombre = Nombre2 #con el setter solo se reescribe no necesita los parentesis ()
nombre21 = Persona21.nombre
print(nombre21)

del Persona21.nombre #Solo se puede eliminar si la clase tiene el decorador de deleter


#Este es la mejor forma de encapsularlos, se llama Python ways, usar los atributos directamente
