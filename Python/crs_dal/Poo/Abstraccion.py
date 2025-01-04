"""Abstraccion"""
#Manejar la complegidad ocultando todo lo innecesario y brindarle todo las funcionalidades esencial
#Ocultar la complejidad de un sistema

class Auto():
    def __init__(self):
        self._conductor = 'apagado'

    def encender(self):
        if self._conductor == 'apagado':
            self._conductor = 'encendido'
            self.conducir()

    def Apagar(self):
        if self._conductor == 'apagado':
            print("Estoy parqueado")
        elif self._conductor == 'encendido':
            self._conductor = 'apagado'
            self.Apagar()
    
    def conducir(self):
        if self._conductor == 'apagado':
            self._conductor = 'encendido'
            self.conducir()
        elif self._conductor == 'encendido':
            print("Estoy conduciendo")

Toyota = Auto()
Toyota.encender() #Al llamar a este metodo, se ejecuta algo, pero el usuaria no sabe todo el proceso que hay detras
Toyota.Apagar() #Al llamar a este metodo, se ejecuta algo, pero el usuaria no sabe todo el proceso que hay detras


"""Clases abstractas"""
#Clase que pertime tener abstractacion
#Es como tener un plantilla que sirve para formas otras clases mas complejas, pero estas tiene son una base para formar otras
#Estas clases no son para formar objetos sino para hacer otras clases

#Metodos abstractos, son funcionalidad que tiene la base para otras bases la adapten


from abc import ABC, abstractmethod   #Se tiene que importar los mudulos de abstraccion

class Persona(ABC): #Tiene que heredad el modulo de abstraccion, esta es una clase abstracta
    @abstractmethod #Para decir que este metodo es abstracto
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    
    @abstractmethod
    def hacer_actividad(self):
        pass

    def saludo(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años")

#Edwin = Persona("Edwin", 20, "Masculino", "Programador")  Esto daria un error

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)  #Mientras se hereda los atributos no es necesarios inicializarlos
    
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)  #Mientras se hereda los atributos no es necesarios inicializarlos
    
    def hacer_actividad(self):
        print(f"Estoy trabajando en: {self.actividad}")

Lucas = Estudiante("Lucas", 22, "Masculino", "Desarrollador")  #Esto si funciona, ya que es hizo con una clase abstracta
Lucas.saludo()
Lucas.hacer_actividad()

Edwin = Trabajador("Edwin", 20, "Masculino", "Programador")  #Esto si funciona, ya que es hizo con una clase abstracta
Edwin.saludo()
Edwin.hacer_actividad()


#La diferencia de la abstraccion y la herencias es 
#La abstracion hace que las clases hijas tenga que poser las miscas caracteristicas o metods, dependiendo de el tipo de abstraccion
#La herencia es mas flexible

"""RESUMEN DE FORMAS DE ABSTRACION Y DIFERENCIAS"""

"""
¿Puedo usar abstracción en el constructor (__init__)?
Sí, pero no con @abstractclassmethod ni con @abstractstaticmethod. Si quieres que todas las clases hijas definan su propia lógica de inicialización, lo haces usando @abstractmethod en el constructor.
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def __init__(self, nombre):
        "El constructor debe ser implementado por las clases hijas."
        pass
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Llama al constructor abstracto
        self.nombre = nombre
        self.raza = raza
En este caso: La clase abstracta obliga a las hijas a implementar su propio __init__.
No puedes crear una instancia de Animal, porque su constructor es abstracto.
Si el constructor de la clase base no debe ser abstracto, simplemente no lo decoras y 
puedes definirlo como un constructor común.

Diferencias entre cada tipo de abstracción

A. @abstractmethod
Qué es: Un método de instancia.
Qué trabaja: Con instancias de la clase (es decir, objetos creados de la clase).
Cuándo usarlo: Cuando quieres forzar a las clases hijas a implementar un comportamiento específico para cada instancia.
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass
class Perro(Animal):
    def sonido(self):
        return "Guau"
Diferencia: sonido() requiere una instancia (mi_perro.sonido()).

B. @abstractclassmethod
Qué es: Un método de clase.
Qué trabaja: Con la clase en sí misma, no con instancias (recibe cls en lugar de self).
Cuándo usarlo: Cuando el método aplica a toda la clase y no necesita datos de una instancia.
from abc import ABC, abstractclassmethod
class Forma(ABC):
    @abstractclassmethod
    def descripcion(cls):
        pass
class Circulo(Forma):
    @classmethod
    def descripcion(cls):
        return "Esto es un círculo"
Diferencia: descripcion() trabaja con la clase (Circulo.descripcion()), no con una instancia.

C. @abstractstaticmethod
Qué es: Un método estático.
Qué trabaja: No necesita acceder ni a la instancia ni a la clase.
Cuándo usarlo: Para métodos independientes que no dependen de atributos de la clase o instancia.
from abc import ABC, abstractstaticmethod
class Calculadora(ABC):
    @abstractstaticmethod
    def sumar(a, b):
        pass
class MiCalculadora(Calculadora):
    @staticmethod
    def sumar(a, b):
        return a + b
Diferencia: sumar() es como una función normal, pero está definida dentro de la clase (MiCalculadora.sumar(3, 4)).

D. @abstractproperty
Qué es: Una propiedad abstracta.
Qué trabaja: Obliga a las clases hijas a implementar un atributo accesible como propiedad (objeto.propiedad).
Cuándo usarlo: Cuando quieres forzar a las clases hijas a definir atributos calculados o con lógica personalizada.
from abc import ABC, abstractproperty
class Vehiculo(ABC):
    @abstractproperty
    def tipo(self):
        pass
class Coche(Vehiculo):
    @property
    def tipo(self):
        return "Coche"
Diferencia: tipo se accede como atributo (mi_coche.tipo), no como método.

¿Cómo elegir cuál usar?
Usa @abstractmethod para comportamientos que cada instancia debe tener.
Usa @abstractclassmethod cuando el método aplica a la clase en sí, no a instancias específicas.
Usa @abstractstaticmethod para métodos que son completamente independientes.
Usa @abstractproperty cuando quieres forzar a las clases hijas a tener atributos calculados o dinámicos. """