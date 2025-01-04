# Ejemplo de Clases y Objetos
class Persona:
    # Atributos de la clase Persona
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método de la clase Persona
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear un objeto de la clase Persona
persona1 = Persona("Juan", 30)
# Usar el método del objeto
persona1.saludar()

# Ejemplo de Encapsulamiento
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Saldo insuficiente")

    def mostrar_saldo(self):
        print(f"Saldo: {self.__saldo}")

# Crear un objeto de la clase CuentaBancaria
cuenta = CuentaBancaria("Ana", 1000)
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.mostrar_saldo()

# Ejemplo de Herencia
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")

# Crear objetos de las clases derivadas
perro = Perro("Firulais")
gato = Gato("Misu")
perro.hacer_sonido()
gato.hacer_sonido()

# Ejemplo de Polimorfismo
def hacer_sonido_animal(animal):
    animal.hacer_sonido()

hacer_sonido_animal(perro)
hacer_sonido_animal(gato)

# Ejemplo de Abstracción
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * (self.radio ** 2)

class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

# Crear objetos de las clases derivadas
circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)
print(f"Área del círculo: {circulo.area()}")
print(f"Área del rectángulo: {rectangulo.area()}")

# Ejemplo de Modularidad
# Supongamos que tenemos un archivo llamado modulo.py con la siguiente clase:
# class ModuloEjemplo:
#     def __init__(self, dato):
#         self.dato = dato
# 
#     def mostrar_dato(self):
#         print(f"El dato es: {self.dato}")

# Ahora, en otro archivo, podemos importar y usar esta clase:
# from modulo import ModuloEjemplo
# 
# modulo_ejemplo = ModuloEjemplo("Ejemplo de modularidad")
# modulo_ejemplo.mostrar_dato()