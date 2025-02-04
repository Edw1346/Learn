"""Una clase es un molde o plantilla que define la estructura y el comportamiento de un objeto. Es un esquema que describe cómo deberían ser los objetos de esa clase y qué operaciones pueden realizar.

Un objeto es una instancia de una clase. Es una entidad real creada a partir del molde de la clase. Los objetos tienen atributos (datos o propiedades) y métodos (funciones que describen sus comportamientos).

Ejemplo en Python:"""

class Persona: 
# Atributo de clase 
    especie = "Homo sapiens" 
# Método de inicialización (constructor) 
    def __init__(self, nombre, edad): 
        self.nombre = nombre  # Atributo de objeto 
        self.edad = edad # Atributo de objeto
# Método de instancia 
    def hablar(self): 
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.") 
# Crear un objeto de la clase Persona 
persona1 = Persona("Juan", 30) 
persona1.hablar() 


"""Los atributos son las propiedades de una clase que se asocian a los objetos de esa clase. Pueden ser de clase o de instancia: 
Atributos de instancia: Son variables que pertenecen a un objeto específico. Se definen dentro del método __init__ con self.

Atributos de clase: Son variables compartidas por todos los objetos de la clase, y se definen fuera de cualquier método.

Los métodos son funciones que definen el comportamiento de los objetos de la clase. Los métodos pueden acceder y modificar los atributos de la instancia mediante self. 
Métodos de instancia: Son métodos que operan sobre las instancias del objeto.
Métodos de clase: Son métodos que operan sobre la clase misma y no sobre una instancia específica. Se definen con el decorador @classmethod.
Métodos estáticos: Son métodos que no necesitan acceso ni a la instancia ni a la clase. Se definen con el decorador @staticmethod.

Ejemplo de método de clase y estático:"""


class Persona:
    especie = "Homo sapiens" 
    def __init__(self, nombre, edad): 
        self.nombre = nombre 
        self.edad = edad
    @classmethod 
    def obtener_especie(cls): 
        return cls.especie 
    @staticmethod 
    def saludar(): 
        print("¡Hola!") # Llamando al método de clase 

print(Persona.obtener_especie()) # "Homo sapiens" 
# Llamando al método estático 
Persona.saludar() # ¡Hola! 

"""El encapsulamiento es un principio que consiste en ocultar los detalles internos de un objeto y exponer solo lo necesario a través de métodos públicos. En Python, se logra mediante convenciones como el uso de un guion bajo (_) o doble guion bajo (__) para atributos y métodos privados. 

Atributos privados: Aquellos que no deben ser accesibles directamente desde fuera de la clase.

Métodos privados: Aquellos que no deben ser llamados desde fuera de la clase.

Ejemplo de encapsulamiento:"""
class Persona: 
    def __init__(self, nombre, edad): 
        self._nombre = nombre # Atributo protegido 
        self.__edad = edad # Atributo privado 

    def obtener_edad(self): 
        return self.__edad 

persona = Persona("Ana", 25) 
print(persona.__edad) # Error, no es accesible directamente 
print(persona.obtener_edad()) # 25 

"""Herencia es un mecanismo que permite crear una nueva clase basándose en una clase existente. La clase hija hereda los atributos y métodos de la clase padre, y puede añadir o modificar comportamientos. Ejemplo de herencia:"""
class Animal: 
    def __init__(self, nombre): 
        self.nombre = nombre 

    def hacer_sonido(self): 
        print("Sonido genérico") 

class Perro(Animal): 
    def __init__(self, nombre, raza): 
        super().__init__(nombre) # Llamada al constructor de la clase base 
        self.raza = raza 

    def hacer_sonido(self): 
        print(f"{self.nombre} dice: Guau!") 

perro = Perro("Rex", "Labrador") 
perro.hacer_sonido() # Rex dice: Guau! 


"""Polimorfismo permite que diferentes clases puedan ser tratadas a través de la misma interfaz, aunque cada clase puede implementar su propio comportamiento para una misma función. Esto se logra mediante la sobrescritura de métodos (en 

clases hijas) o sobrecarga de métodos. Ejemplo de polimorfismo:"""
class Gato(Animal): 
    def hacer_sonido(self): 
        print(f"{self.nombre} dice: Miau!") 

animales = [Perro("Rex", "Labrador"), Gato("Whiskers")] 
for animal in animales: 
    animal.hacer_sonido() 


"""Abstracción es el proceso de ocultar la complejidad y mostrar solo lo necesario. En OOP, las clases abstractas proporcionan una estructura que otras clases pueden extender, pero no pueden ser instanciadas directamente. Ejemplo de clase abstracta:"""
from abc import ABC, abstractmethod 
class Animal(ABC): 
    @abstractmethod 
    def hacer_sonido(self): 
        pass 

class Perro(Animal): 
    def hacer_sonido(self): 
        print("Guau!") 
# animal = Animal() 
# Error, no se puede instanciar una clase abstracta 
perro = Perro() 
perro.hacer_sonido() # Guau! 


"""El método __init__ es un método especial utilizado para inicializar objetos. Se llama automáticamente cuando se crea una instancia de la clase. Ejemplo:"""
class Persona: 
    def __init__(self, nombre, edad): 
        self.nombre = nombre 
        self.edad = edad 

persona = Persona("Luis", 28) 
print(persona.nombre) # Luis 


"""Python tiene varios métodos especiales, como: 
__str__(): Define cómo representar un objeto como cadena.
__repr__(): Define cómo representar un objeto para depuración.
__del__(): Método destructor llamado al eliminar un objeto."""

#Ejemplo de __str__:
class Persona: 
    def __init__(self, nombre, edad): 
        self.nombre = nombre 
        self.edad = edad 

    def __str__(self): 
        return f"{self.nombre}, {self.edad} años" 

persona = Persona("Carlos", 35) 
print(persona) # Carlos, 35 años 



"""El destructor es un método especial __del__ que se llama cuando un objeto es destruido (cuando se elimina o sale de su ámbito). En algunos lenguajes de programación, se usa para liberar recursos como memoria o conexiones de red.


La composición es un concepto relacionado con la OOP en el que una clase contiene instancias de otras clases como atributos. Es una forma de modelar relaciones de "tiene un" (por ejemplo, un coche tiene un motor).

Las interfaces definen un conjunto de métodos que una clase debe implementar, pero no proporcionan implementación propia. Aunque Python no tiene interfaces como tal (como otros lenguajes como Java), se puede simular el concepto mediante clases abstractas.

Las clases abstractas son clases que no se pueden instanciar directamente y pueden contener métodos abstractos, que son métodos que deben ser implementados por las subclases. Se usan para proporcionar una interfaz común y establecer un contrato para las clases derivadas.

self es una convención en Python que se utiliza para referirse a la instancia actual de una clase dentro de los métodos de instancia. Permite acceder a los atributos y métodos del objeto.

La función super() se utiliza en una subclase para invocar los métodos de la superclase. Es especialmente útil para llamar al constructor de la superclase desde una subclase.

Los modificadores de acceso en OOP controlan la visibilidad de los atributos y métodos: 
Público: Accesible desde cualquier parte del programa.

Protegido: Se indica mediante un solo guion bajo (_). Por convención, significa que el atributo/método debe ser tratado como interno.

Privado: Se indica mediante doble guion bajo (__). No debe ser accedido directamente fuera de la clase.

Las clases anidadas son clases definidas dentro de otra clase. Son útiles cuando se necesita encapsular una clase que solo tiene sentido dentro del contexto de la clase externa.

Los métodos de propiedad (@property) permiten definir atributos que, aunque se accedan como si fueran simples variables, son en realidad el resultado de una función."""


"""Buenas prácticas"""

"""1. Seguir el principio de responsabilidad única (SRP - Single Responsibility Principle)
Cada clase debe tener una única responsabilidad. Esto significa que una clase debe encargarse de una sola tarea o funcionalidad en el sistema. Ejemplo: Si tienes una clase Usuario, su única responsabilidad debería ser gestionar los datos y comportamientos de un usuario, no mezclarla con la lógica de base de datos o procesamiento de datos.

2. Mantener las clases pequeñas y enfocadas
Las clases deben ser compactas y contener solo las funcionalidades necesarias. Si una clase empieza a tener demasiados métodos o atributos, es una señal de que tal vez debas dividirla en varias clases con responsabilidades más enfocadas. Ejemplo: Una clase Factura que tenga tanto métodos para el cálculo de impuestos como métodos para el envío de correos electrónicos puede estar violando esta práctica.

3. Usar nombres descriptivos para las clases
Los nombres de las clases deben ser claros, descriptivos y coherentes con su responsabilidad. Un buen nombre de clase debe reflejar claramente su función o rol. Ejemplo: Utilizar Empleado en lugar de Persona si la clase solo se dedica a gestionar información de empleados.

4. Encapsular los detalles internos
Utiliza el encapsulamiento para ocultar la implementación interna de la clase. Los atributos internos no deben ser accesibles directamente desde fuera de la clase; en lugar de eso, debes proporcionar métodos públicos para acceder o modificar esos atributos de forma controlada. Ejemplo: Si tienes un atributo edad, asegúrate de no permitir acceso directo al mismo, sino usa un método como get_edad() o set_edad().

5. Utilizar métodos de clase y estáticos solo cuando sea necesario

Los métodos de clase (@classmethod) y métodos estáticos (@staticmethod) deben utilizarse solo cuando sea necesario, ya que generalmente indican que una acción no depende de la instancia de la clase.  Ejemplo: Si un método actúa sobre un objeto específico, debe ser un método de instancia. Usa métodos estáticos solo cuando no necesiten modificar los atributos de la instancia ni la clase.

6. Definir métodos __str__ y __repr__
Es recomendable definir el método especial __str__() para proporcionar una representación de cadena legible del objeto. Esto es útil para depuración y para mostrar objetos de manera más comprensible. Ejemplo: Si tienes una clase Coche, el método __str__() podría devolver "Coche {marca} {modelo}", mientras que __repr__() puede devolver una representación más detallada para depuración.

7. Evitar el uso excesivo de clases anidadas
Si bien las clases anidadas pueden ser útiles en algunos casos, deberían usarse con moderación. Evitar anidar clases si no es absolutamente necesario, ya que puede hacer que el código sea más difícil de leer y mantener. Ejemplo: Utiliza clases anidadas solo cuando su existencia tenga sentido en el contexto de la clase principal, por ejemplo, como una clase auxiliar para funciones internas.

8. Usar herencia de forma prudente
La herencia es un poderoso mecanismo, pero debe usarse de forma responsable. Evita la herencia múltiple en exceso y asegúrate de que la relación entre la superclase y la subclase sea lógica y útil. Ejemplo: Utiliza herencia solo si la subclase realmente extiende las funcionalidades de la superclase. No uses herencia si una relación de composición sería más adecuada.

9. Evitar el uso de métodos __del__ para la limpieza
El método __del__ es usado para limpiar recursos cuando un objeto es destruido. Sin embargo, no es fiable, ya que no se llama siempre cuando esperamos, y el recolector de basura de Python no garantiza cuándo se destruirán los objetos. Es mejor usar otras técnicas, como context managers o la gestión explícita de recursos. Ejemplo: Si necesitas liberar recursos como archivos abiertos, utiliza with para gestionar el contexto.

10. Aplicar el principio de "favorecer la composición sobre la herencia"
Aunque la herencia es útil, la composición suele ser preferible cuando sea posible. La composición permite mejor flexibilidad al combinar objetos con diferentes funcionalidades, evitando la jerarquía rígida de clases. Ejemplo: Si un coche tiene un motor y una transmisión, en lugar de hacer que Coche herede de Motor, haz que Coche tenga un atributo motor y otro transmision.

11. Definir interfaces claras
Si usas clases abstractas o interfaces, asegúrate de que sus métodos estén bien definidos y que cada clase que las implemente se adhiera rigurosamente a la interfaz. Esto facilita la extensibilidad del código. Ejemplo: Una clase Vehiculo que tenga un método mover() que sea implementado por todas las subclases como Coche o Bicicleta.

12. Limitar el uso de modificadores de acceso privados
Aunque los modificadores de acceso privados (__atributo) son útiles para ocultar los detalles de implementación, se debe ser consciente de la necesidad real de hacer privados los atributos. No es necesario hacer todos los atributos privados a menos que se esté seguro de que no deben ser modificados directamente. Ejemplo: Usar _atributo para atributos que deban ser protegidos, pero que todavía puedan ser modificados por las clases derivadas si es necesario.

13. Evitar el código duplicado
Asegúrate de que las funcionalidades comunes se encuentren en un lugar centralizado. Si varias clases tienen métodos similares, es una señal de que podrías abstraer ese comportamiento en una clase base o usar clases auxiliares. Ejemplo: Si varias clases tienen métodos para calcular impuestos, extrae esa lógica en una clase común o en un módulo de utilidades.

14. Implementar pruebas unitarias
Las clases deben ser fáciles de probar. Cada método debe ser probado de forma aislada utilizando pruebas unitarias. Esto garantizará que los cambios en el código no rompan funcionalidades existentes. Ejemplo: Si tienes una clase Calculadora, deberías escribir pruebas unitarias para cada operación (suma, resta, multiplicación, etc.).

15. Usar el principio de "no acoplar fuertemente" (loose coupling)
Reducir el acoplamiento entre las clases. Las clases deben interactuar entre sí de manera mínima y controlada. Esto permite cambiar o sustituir clases sin afectar significativamente otras partes del sistema. Ejemplo: Si un Coche depende de un Motor, asegúrate de que el Motor se pase como una dependencia y no se cree dentro de la clase Coche."""








"""Técnicas"""

"""1. Uso de Composición en lugar de Herencia (Favor Composición)
Composición significa que una clase tiene instancias de otras clases como atributos. Es una técnica para lograr una mayor flexibilidad y evitar una jerarquía de clases demasiado rígida que pueda hacer que el sistema sea más difícil de mantener. 
Técnica: Cuando una clase necesita usar las funcionalidades de otra clase, en lugar de heredar de ella, inserta esa clase como atributo. Esto hace que el comportamiento de una clase dependa de sus componentes, lo que favorece un acoplamiento bajo y una extensibilidad más fácil. Ejemplo: En lugar de que Coche herede de Motor, haz que Coche tenga un atributo motor, y cualquier cambio en la implementación de Motor no afectará a las otras clases.

2. Usar Interfaces para Abstraer Comportamientos
Las interfaces permiten definir un contrato de comportamiento que las clases implementan sin necesidad de conocer la implementación específica. Aunque Python no tiene interfaces explícitas como otros lenguajes, puedes simularlas usando clases abstractas. 
Técnica: Usa clases abstractas y métodos abstractos para definir un conjunto de operaciones que cualquier subclase debe implementar. Ejemplo: Si tienes una clase Forma, puedes definir métodos como dibujar() y calcular_area(), y luego hacer que clases como Círculo o Rectángulo implementen esos métodos.

3. Principio de Inyección de Dependencias
La inyección de dependencias es una técnica que implica pasar las dependencias de una clase (otros objetos que necesita para funcionar) a través de su constructor o métodos, en lugar de crear las instancias internamente. Esto mejora la testabilidad y la flexibilidad del código. 
Técnica: Utiliza el constructor para pasar las dependencias necesarias en lugar de crearlas dentro de la clase. Esto permite cambiar comportamientos sin modificar el código de la clase principal. Ejemplo: En lugar de que una clase Usuario cree internamente una instancia de BaseDeDatos, pasa la base de datos como argumento del constructor de Usuario.

4. Uso de Métodos de Clase para Factories
Los métodos de clase son útiles para implementar patrones de diseño como factories, donde el método de clase puede crear instancias de la clase de una manera flexible. 
Técnica: Utiliza un método de clase para proporcionar una forma estándar de crear objetos, especialmente cuando el proceso de instanciación involucra varios pasos o configuraciones. Ejemplo: Si tienes una clase Coche, puedes usar un método de clase crear_de_configuracion(config) que reciba un diccionario de configuraciones y cree una instancia de Coche con los parámetros correspondientes.

5. Aplicar el Principio de Diseño SOLID
SOLID es un acrónimo que representa cinco principios clave de diseño que ayudan a mejorar la calidad del código orientado a objetos: 
S: Single Responsibility Principle (SRP): Cada clase debe tener una única responsabilidad.
O: Open/Closed Principle (OCP): Las clases deben estar abiertas para la extensión pero cerradas para la modificación.
L: Liskov Substitution Principle (LSP): Las subclases deben ser intercambiables por sus superclases sin afectar el funcionamiento del sistema.
I: Interface Segregation Principle (ISP): Los clientes no deben depender de interfaces que no utilizan.
D: Dependency Inversion Principle (DIP): Las clases de alto nivel no deben depender de clases de bajo nivel. Ambas deben depender de abstracciones.
Técnica: Al seguir estos principios, puedes hacer que tu código sea más modular, flexible y fácil de mantener.


6. Usar el Patrón de Diseño Observer
El patrón Observer es útil cuando tienes una clase que necesita notificar a otras clases cuando ocurre un cambio en su estado. Es muy común en interfaces de usuario o sistemas de eventos. 
Técnica: Utiliza una lista de observadores que se suscriben a los eventos de la clase y reaccionan cuando el estado cambia. Ejemplo: Si tienes una clase Temporizador, puedes tener múltiples clases observadoras que reaccionan cuando el temporizador llega a cero.

7. Evitar la Mutabilidad Inesperada (Inmutabilidad)
Evita que los objetos cambien de manera inesperada, especialmente si se pasan a otras clases. Usar objetos inmutables hace que tu código sea más fácil de razonar y menos propenso a errores. 
Técnica: Si una clase tiene atributos que no deben cambiar una vez creados, marca esos atributos como constantes o utiliza patrones que garantizan que los objetos no cambien después de su creación. Ejemplo: Si tienes una clase Fecha, evita que sus atributos día, mes y año cambien después de la creación. Puedes usar la propiedad @property para asegurarte de que no se modifiquen.

8. Implementación de Métodos de Factory para la Creación de Objetos
Los métodos de fábrica son métodos que crean objetos sin exponer el constructor directamente. Esto es útil si la creación del objeto es compleja o si deseas ocultar la complejidad de la construcción. 

Técnica: Usa un método estático o un método de clase para encapsular la lógica de creación de objetos. Ejemplo: Si tienes una clase CuentaBancaria, puedes usar un método de clase crear_cuenta(nombre, saldo) para crear una nueva cuenta, en lugar de llamar al constructor directamente.

9. Delegación de Responsabilidades (Delegation)
Delegar responsabilidades significa que una clase puede delegar ciertas tareas a otras clases para que su código se mantenga limpio y modular. 

Técnica: Usa la delegación para asignar tareas a otras clases que se encargan de una responsabilidad particular, en lugar de abarcar múltiples responsabilidades dentro de una sola clase. Ejemplo: Si tienes una clase Pedido, puedes delegar la responsabilidad de calcular el precio total del pedido a una clase separada CalculadoraDePrecios.

10. Aplicación de Patrones de Diseño Comunes
A medida que adquieras más experiencia con OOP, familiarizarte con patrones de diseño comunes puede mejorar la flexibilidad y reutilización de tu código. Algunos patrones útiles son: 

Singleton: Asegura que una clase tenga una única instancia durante la ejecución.
Factory Method: Proporciona una interfaz para crear objetos, permitiendo que las subclases decidan qué clase instanciar.
Decorator: Permite agregar funcionalidades a un objeto de manera dinámica.
Adapter: Permite que clases con interfaces incompatibles trabajen juntas."""
