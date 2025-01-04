"""Ejercicio 1"""


"""class Estudiante():
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f"{self.nombre} está estudiando")

nombre = input("Ingrese el nombre del estudiante: ")
edad = input("Ingrese la edad del estudiante: ")    
grado = input("Ingrese el grado del estudiante: ")
Estudiante1 = Estudiante(nombre,edad,grado)

while True:
    accion = input("¿Qué desea hacer? estudiar/salir: ")
    if accion.lower() == 'estatus':
        print(f"Nombre: {Estudiante1.nombre}, Edad: {Estudiante1.edad}, Grado: {Estudiante1.grado}")
    elif accion.lower() == 'estudiar':
        Estudiante1.estudiar()
    elif accion.lower() == 'salir':
        break
    else: pass"""

"""Ejercicio 2"""
"""
class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

class Estudiante(Persona):
    def __init__(self, nombre, edad,grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mos_grado(self):
        return f"Soy estudiante de {self.grado}"

while True:
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = input("Ingrese la edad del estudiante: ")
    grado = input("Ingrese el grado del estudiante: ")
    Estudiante1 = Estudiante(nombre, edad, grado)
    resultado = Estudiante1.saludar()
    print(f"Saludar de la clase padre Persona  {resultado}")
    print(f"Grado de la clase Estudiante {Estudiante1.mos_grado()}")
    break

class Animal:
    def comer(self):
        print("Estoy comiendo")

class Mamifero(Animal):
    def amamantar(self):
        print("Estoy amamantando")

class Ave(Animal):
    def volar(self):
        print("Estoy volando")

class Murcielago(Mamifero, Ave):
    pass


murcielago = Murcielago()

murcielago.amamantar()
murcielago.volar()
print(f"El MRO de la clase Murcielago es: {Murcielago.mro()}")


class Murcielago(Mamifero, Animal):
    def __init__(self, nombre):
        self.nombre = nombre

murcielago = Murcielago("Murcielago")
print(murcielago.amamantar())
print(murcielago.comer())
print(f"El MRO de la clase Murcielago es: {Murcielago.mro()}")"""

"""
class Murcielago(Ave, Animal):
    def __init__(self, nombre):
        self.nombre = nombre

murcielago = Murcielago("Murcielago")
print(murcielago.volar())
print(murcielago.comer())
print(f"El MRO de la clase Murcielago es: {Murcielago.mro()}")"""

"""
class Murcielago(Animal ,Mamifero):
    def __init__(self, nombre):
        self.nombre = nombre

murcielago = Murcielago("Murcielago")
print(murcielago.comer())
print(murcielago.amamantar())
print(f"El MRO de la clase Murcielago es: {Murcielago.mro()}")"""



"""Ejercicio 3"""


class Personajes():
    def __init__ (self, nombre, habilidades, poder):
        self.nombre = nombre
        self.habilidades = habilidades
        self.poder = poder

    def presentarse(self):
        print(f"Hola me llamo {self.nombre}, tengo {self.habilidades} habilidades y {self.poder} de poder")

    def __repr__(self):
        return f'Nombre={self.nombre}, habilidades= {self.habilidades} y poder= {self.poder}'

    def __add__(self, otros):
        habilidad_nueva = ((self.habilidades + otros.habilidades) / 2)
        nombre_nuevo = self.nombre + " " + otros.nombre
        poder_nuevo = self.poder + otros.poder
        return Personajes(nombre_nuevo, habilidad_nueva, poder_nuevo)


Goku = Personajes("Goku", 200, 1050)
print(Goku)
Vegeta = Personajes("Vegeta", 150, 1100)
print(Vegeta)

Fusion = Goku + Vegeta
print(Fusion)

"""Ejercicio 4"""




"""Ejercicio 5"""
