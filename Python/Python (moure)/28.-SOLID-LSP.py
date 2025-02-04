"""El Principio de Sustitución de Liskov (LSP) es el tercer principio de SOLID y establece que las clases derivadas deben ser sustituibles por sus clases base sin alterar el comportamiento esperado del programa, si una clase B hereda de una clase A, entonces los objetos de tipo B deben poder reemplazar a los objetos de tipo A sin cambiar las propiedades que el programa tiene de esos objetos. Las clases derivadas deben cumplir las expectativas y contratos establecidos por las clases base, garantizando la funcionalidad del sistema no se vea afectada al utilizar la subclase en lugar de la clase base.

¿Por qué es importante LSP?
El LSP asegura que las clases derivadas mantienen el comportamiento de la clase base y no introducen errores o efectos secundarios inesperados.
Permite una extensión de funcionalidades sin causar fallos en el comportamiento original del sistema.
Facilita el uso de polimorfismo, ya que las instancias de las subclases se pueden utilizar de forma intercambiable con las clases base.

Ejemplo Correcto (Cumple LSP)
En este ejemplo, la subclase Bird puede ser reemplazada por su clase base Animal sin alterar el comportamiento del programa."""
class Animal: 
    def speak(self):
        return "Animal sound" 

class Bird(Animal):
    def speak(self): 
        return "Tweet" 
    
    def animal_sound(animal: Animal): 
        print(animal.speak())

# Uso 
bird = Bird() 
animal_sound(bird) # Output: Tweet 
#Aquí, Bird es una subclase de Animal, y puedes usar un objeto de tipo Bird donde se espera un Animal sin cambiar el comportamiento del programa.

"""Ejemplo Incorrecto (No Cumple LSP)
En este ejemplo, la subclase Bird no cumple con el principio de LSP. La clase Bird debería ser capaz de comportarse como 

un Animal, pero lo que sucede es que hemos introducido una restricción en la subclase que cambia el comportamiento de forma inesperada."""
class Animal: 
    def speak(self):
        return "Animal sound"

class Bird(Animal): 
    def speak(self): 
        raise NotImplementedError("Birds can't speak!") 

    def animal_sound(animal: Animal): 
        print(animal.speak()) 

# Uso 
bird = Bird()
animal_sound(bird) # Esto lanzará un error 

"""En este caso, el Bird no puede ser sustituido por un Animal sin alterar el comportamiento esperado. La clase Bird no está cumpliendo con el contrato de la clase base Animal porque speak no es implementado adecuadamente."""

"""Cómo Cumplir el LSP
Usar interfaces claras y bien definidas: Si tienes una jerarquía de clases, asegúrate de que la interfaz proporcionada por la clase base sea completa y clara. Las subclases deben seguir esta interfaz.

Respetar la lógica de negocio de la clase base: Las subclases deben extender la funcionalidad de la clase base de una manera coherente y no deben modificar la lógica fundamental de los métodos heredados.

Evitar sobrecargar el comportamiento de las clases base: Si una subclase necesita cambiar drásticamente el comportamiento de la clase base, es posible que sea más adecuado crear una nueva clase que implemente una funcionalidad diferente en lugar de extender la clase base."""

"""Ejemplo de Correcto Cumplimiento del LSP
Imaginemos que tenemos una clase base Shape que tiene un método area(), y dos subclases: Circle y Rectangle. Ambas subclases cumplen con el contrato de la clase base y pueden ser usadas intercambiablemente."""

class Shape: 
    def area(self): 
        pass 

class Circle(Shape): 
    def __init__(self, radius): 
        self.radius = radius 

    def area(self): 
        return 3.14159 * self.radius ** 2 

class Rectangle(Shape): 
    def __init__(self, width, height): 
        self.width = width 
        self.height = height 

    def area(self): 
        return self.width * self.height 

# Uso 
shapes = [Circle(5), Rectangle(10, 20)] 
for shape in shapes: 
    print(f"Area: {shape.area()}") 


"""Este código cumple con el LSP porque ambas clases Circle y Rectangle implementan el método area() de manera coherente con la clase base Shape, lo que permite que las instancias de Circle y Rectangle sean sustituidas por instancias de Shape sin afectar el comportamiento del programa."""




""" conceptos relacionados con el Principio de Sustitución de Liskov (LSP):"""

"""1. Contratos de Clases
Un contrato de clase se refiere a las expectativas sobre el comportamiento de una clase (por ejemplo, los métodos que debe tener y lo que esos métodos deben hacer). LSP asegura que las clases derivadas respeten el contrato de la clase base. Si un contrato establece que un método debe devolver un valor entero, la subclase no debe alterar ese comportamiento. Ejemplo:"""
class Account: 
    def get_balance(self): 
        raise NotImplementedError 

class SavingsAccount(Account): 
    def get_balance(self):
        return 1000 

"""2. Subtipado
El subtipado se refiere a la relación entre una clase base y sus subclases. En el contexto de LSP, las subclases deben poder sustituir a la clase base sin generar errores o comportamientos inesperados. Es decir, la subclase debe ser un subtipo de la clase base en términos de sus comportamientos y no introducir alteraciones. Ejemplo:"""
class Shape: 
    def area(self): 
        pass 

class Circle(Shape):
    def area(self): 
        return 3.14 * self.radius ** 2 


"""9. Técnicas de Diseño (Design Patterns)
Algunos patrones de diseño ayudan a implementar LSP de manera efectiva:
Patrón de Estrategia: Permite cambiar el comportamiento de un objeto sin modificar el objeto en sí, utilizando composición.
Patrón de Delegación: Similar a la estrategia, pero delega tareas a un objeto diferente. Ejemplo de Estrategia:"""
class PaymentStrategy:
    def pay(self, amount): 
        pass 

class CreditCardPayment(PaymentStrategy): 
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card") 

class PayPalPayment(PaymentStrategy): 
    def pay(self, amount): 
        print(f"Paying {amount} using PayPal") 

class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy): 
        self.strategy = strategy 

    def process_payment(self, amount): 
        self.strategy.pay(amount) 


payment = PaymentProcessor(CreditCardPayment()) 
payment.process_payment(100) 





"""Prácticas recomendadas """


"""1. Seguir los contratos de la clase base
Las clases derivadas deben cumplir con el contrato de la clase base, lo que significa que los métodos de la subclase deben comportarse de manera coherente con la clase base. Si un método de la clase base devuelve un valor, la subclase también debe devolver ese tipo de valor.
Evita cambiar la firma o el tipo de retorno de los métodos heredados de la clase base.
Si la clase base tiene un comportamiento específico, las subclases deben mantener ese comportamiento. Ejemplo:"""
class Animal: 
    def speak(self):
        return "Animal sound" 

class Dog(Animal): 
    def speak(self): 
        return "Woof!"

class Cat(Animal): 
    def speak(self): 
        return "Meow" 

# Uso 
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak()) # Output: Woof! Meow 

"""2. Evitar cambiar el comportamiento esperado de la clase base
Si la clase base define un comportamiento específico, las subclases deben mantener ese comportamiento o extenderlo, pero no deben cambiarlo ni eliminarlo.
Asegúrate de que las subclases no introduzcan cambios inesperados que puedan romper la funcionalidad del sistema. Ejemplo:"""
class Shape:
    def area(self): 
        pass

class Circle(Shape): 
    def __init__(self, radius): 
        self.radius = radius 

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height 

    def area(self): 
        return self.width * self.height 

#Las subclases Circle y Rectangle mantienen la lógica de la clase base Shape y cumplen con su contrato.


"""3. No introducir excepciones inesperadas
Las subclases no deben introducir excepciones que no están definidas en la clase base, a menos que se trate de un comportamiento previsible y documentado.
Si la clase base no lanza una excepción, la subclase no debe hacerlo a menos que sea absolutamente necesario y se haga de manera coherente con el contrato. Ejemplo incorrecto:"""
class Animal: 
    def speak(self): 
        return "Animal sound"

class Dog(Animal): 
    def speak(self): 
        raise NotImplementedError("Dogs can't speak") 
#Aquí, Dog introduce una excepción inesperada que viola el contrato de la clase base Animal, que no especifica ninguna excepción.

"""4. Utilizar el polimorfismo correctamente
Asegúrate de que las subclases puedan ser utilizadas como si fueran instancias de la clase base. Esto significa que deben cumplir con la interfaz y las expectativas establecidas por la clase base.
Las funciones que esperan una clase base deben ser capaces de trabajar correctamente con cualquier subclase de esa clase base. Ejemplo:"""
class Bird: 
    def fly(self):
        return "Flying" 

class Sparrow(Bird): 
    def fly(self): 
        return "Sparrow is flying" 

class Penguin(Bird): 
    def fly(self):
        return "Penguin can't fly" 

birds = [Sparrow(), Penguin()] 
for bird in birds:
    print(bird.fly()) # Output: Sparrow is flying Penguin can't fly 

#En este ejemplo, Sparrow y Penguin son subclases de Bird, y puedes tratarlas como objetos de tipo Bird, aunque cada subclase implementa fly() de forma diferente.

"""5. Usar la herencia con coherencia
La herencia debe ser usada con coherencia, de tal manera que las subclases representen una especialización de la clase base y no una alteración radical de su comportamiento.
Si necesitas cambiar significativamente el comportamiento de la clase base, considera la posibilidad de usar composición en lugar de herencia. Ejemplo incorrecto de herencia incoherente:"""
class Bird: 
    def fly(self): 
        return "Flying" 

class Ostrich(Bird): # No debería heredar de Bird 
    def fly(self): 
        return "Ostriches don't fly" 
#La clase Ostrich no debería heredar de Bird, ya que no puede cumplir con el contrato de la clase base. En su lugar, la composición sería más adecuada.

"""6. Evitar romper la lógica de la clase base
Las subclases no deben romper la lógica que ya está definida en la clase base. Si una subclase debe cambiar el comportamiento, debe hacerlo de forma que extienda la funcionalidad sin eliminar o alterar la funcionalidad existente. 

Ejemplo de extensión:"""
class Employee: 
    def __init__(self, name, salary): 
        self.name = name 
        self.salary = salary 

    def display_salary(self): 
        print(f"Salary: {self.salary}")

class Manager(Employee): 
    def __init__(self, name, salary, bonus): 
        super().__init__(name, salary) 
        self.bonus = bonus 

    def display_salary(self):
        super().display_salary()
        print(f"Bonus: {self.bonus}") 

manager = Manager("John", 5000, 1000) 
manager.display_salary() # Output: Salary: 5000 Bonus: 1000 
#Aquí, Manager extiende la funcionalidad de Employee sin alterar su lógica básica.

"""7. Especificar y documentar el comportamiento
Es importante que tanto las clases base como las derivadas tengan documentación clara que explique cómo se deben usar y qué comportamientos esperar. Esto ayuda a evitar confusión sobre lo que se puede y no se puede hacer con las subclases.

8. Realizar pruebas unitarias
Es fundamental probar las clases base y sus subclases de forma independiente, así como en conjunto, para asegurarse de que la sustitución de clases no rompa el comportamiento esperado. Utiliza pruebas unitarias para verificar que el principio LSP se cumple correctamente. Prueba las funciones que dependen de clases base para asegurarte de que siguen funcionando correctamente cuando se usan subclases. Ejemplo de prueba:"""
import unittest
class TestAnimal(unittest.TestCase): 
    def test_dog(self): 
        dog = Dog() 
        self.assertEqual(dog.speak(), "Woof!")

    def test_cat(self):
        cat = Cat() 
        self.assertEqual(cat.speak(), "Meow") 
        if __name__ == "__main__": 
            unittest.main() 




"""Técnicas útiles para implementar correctamente el Principio de Sustitución de Liskov (LSP) en tu código:"""

"""1. Preferir la composición sobre la herencia
Cuando te enfrentes a una situación donde una subclase no puede extender correctamente el comportamiento de la clase base, usa composición en lugar de herencia. La composición permite combinar comportamientos sin violar el contrato de la clase base.
Técnica: Si una subclase no puede cumplir el contrato de la clase base, crea una clase que contenga un objeto de la clase base y delegue la responsabilidad a este objeto. Ejemplo:"""
class Bird:
    def fly(self): 
        return "Flying" 
    
class Ostrich: 
    def __init__(self): 
        self.bird = Bird() # Composición en lugar de herencia 

    def fly(self): 
        return "Ostriches don't fly, but I can run fast" 
#En este ejemplo, en lugar de hacer que Ostrich herede de Bird (lo cual sería incorrecto por LSP), hemos compuesto la clase con un objeto Bird.

"""2. Uso adecuado de la herencia para especialización
Utiliza la herencia solo cuando las clases derivadas representen una especialización de la clase base. Si las subclases cambian demasiado el comportamiento de la clase base, puede ser un indicio de que no deberían heredar.
Técnica: Asegúrate de que las subclases sean sustituibles por la clase base sin alterar el comportamiento del programa.
Considera que la herencia es apropiada solo si una clase es un tipo de la clase base. Ejemplo:"""
class Animal: 
    def speak(self): 
        raise NotImplementedError

class Dog(Animal): 
    def speak(self): 
        return "Woof!" 

class Cat(Animal):
    def speak(self): 
        return "Meow" # Ambas clases derivadas pueden reemplazar a Animal sin problemas 

animals = [Dog(), Cat()] 
for animal in animals:
    print(animal.speak()) # Output: Woof! Meow 
#Aquí, tanto Dog como Cat son tipos de animales, lo que justifica la herencia y el cumplimiento de LSP.

"""3. Implementar interfaces o clases abstractas para contratos claros
Usa interfaces o clases abstractas para definir contratos claros entre la clase base y sus subclases. Esto asegura que las subclases sigan los mismos principios y comportamientos que la clase base.
Técnica: Define métodos en una clase abstracta o interfaz, y asegúrate de que las subclases implementen esos métodos correctamente.
Esto hace explícito el comportamiento esperado y ayuda a garantizar que las subclases cumplan con LSP. Ejemplo:"""
from abc import ABC, abstractmethod
class Shape(ABC): 
    @abstractmethod 
    def area(self): 
        pass 
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius 
    
    def area(self): 
        return 3.14 * self.radius ** 2 

class Rectangle(Shape): 
    def __init__(self, width, height): 
        self.width = width 
        self.height = height 

    def area(self): 
        return self.width * self.height 

#Aquí, Shape define un contrato que las clases derivadas deben cumplir, garantizando que el comportamiento de area se mantenga consistente.

"""4. Proveer un comportamiento común en la clase base
La clase base debe proporcionar un comportamiento común que las subclases puedan extender o usar tal cual. Si una subclase necesita reemplazar el comportamiento, debe hacerlo de manera coherente.
Técnica: En la clase base, proporciona un comportamiento general, mientras que las subclases pueden especializarse si es necesario sin romper el contrato. Ejemplo:"""
class Vehicle: 
    def start_engine(self): 
        return "Engine started" 

class Car(Vehicle): 
    def start_engine(self): 
        return "Car engine started" 

class Truck(Vehicle):
    def start_engine(self): 
        return "Truck engine started" # Todos los vehículos cumplen con el contrato 

vehicles = [Car(), Truck()]
for vehicle in vehicles: 
    print(vehicle.start_engine()) # Output: Car engine started Truck engine started 

#Aquí, el comportamiento start_engine en Vehicle se mantiene consistente, pero puede ser extendido por las subclases.

"""5. Evitar excepciones inesperadas
Las subclases no deben lanzar excepciones que la clase base no haya previsto, ya que esto puede romper el comportamiento esperado.
Técnica: Las subclases deben mantener la compatibilidad con las excepciones que la clase base maneja, y no deben lanzar nuevas excepciones que no puedan manejar las funciones que usan la clase base. Ejemplo:"""
class Bird: 
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def fly(self): 
        raise NotImplementedError("Penguins can't fly") 

#En este caso, Penguin introduce una excepción inesperada al cambiar el comportamiento de fly. Esto viola LSP porque cualquier función que use un objeto Bird no espera un NotImplementedError.

"""6. Asegurar que las funciones que usan clases base funcionen con las subclases
Asegúrate de que las funciones que trabajan con objetos de la clase base funcionen correctamente con cualquier subclase. Esto garantiza que la substitución de clases no rompa el comportamiento esperado.
Técnica: Las funciones o métodos que aceptan la clase base deben ser capaces de manejar cualquier subclase de manera transparente, sin cambios inesperados. Ejemplo:"""
def print_speak(animal): 
    print(animal.speak()) 

animals = [Dog(), Cat()] 
for animal in animals: 
    print_speak(animal) # Output: Woof! Meow 

#En este caso, print_speak puede aceptar tanto un Dog como un Cat sin problema, ya que ambos cumplen con el contrato de la clase base Animal.

"""7. Testeo y validación de sustituciones
Implementa pruebas unitarias para verificar que el comportamiento de las subclases cumple con el contrato de la clase base. Esto puede ayudarte a detectar violaciones de LSP durante el desarrollo.


Técnica: Realiza pruebas de sustitución para asegurarte de que las clases derivadas se comporten de la misma manera que la clase base y no rompan el flujo del programa. Ejemplo:"""
import unittest
class Animal: 
    def speak(self): 
        pass 

class Dog(Animal): 
    def speak(self): 
        return "Woof!" 

class TestAnimal(unittest.TestCase): 
    def test_speak(self): 
        dog = Dog()
        self.assertEqual(dog.speak(), "Woof!")
        if __name__ == "__main__":
            unittest.main() 

#En este caso, la prueba asegura que la clase Dog cumple con el contrato de la clase Animal al implementar correctamente el método speak.