"""El Patrón Singleton es un patrón de diseño que restringe la instanciación de una clase a un solo objeto. Este patrón es útil cuando necesitas garantizar que una clase tenga una única instancia a lo largo de toda la ejecución de un programa, y que esta instancia sea accesible globalmente.

Características principales:
Una sola instancia: La clase controla su propia creación y asegura que solo se cree una instancia.
Acceso global: Proporciona un punto de acceso global a esa única instancia.
Retraso en la creación (Lazy instantiation): La instancia de la clase se crea solo cuando es necesaria, no en el momento de la definición."""

"""Implementación del Patrón Singleton en Python:"""
#1. Usando un atributo de clase para almacenar la instancia:

class Singleton: 
    _instancia = None
    def __new__(cls): 
        if cls._instancia is None: 
            cls._instancia = super(Singleton, cls).__new__(cls) 
            return cls._instancia 
        
# Prueba del patrón Singleton 
obj1 = Singleton() 
obj2 = Singleton() 
print(obj1 is obj2) # True, ambas son la misma instancia 

"""Explicación:
El método __new__ es sobreescrito para controlar la creación de la instancia.
Si la instancia no ha sido creada previamente, se crea una nueva instancia usando super().
Si ya existe una instancia, se devuelve la instancia ya creada."""

"""2. Usando un decorador:
Otra forma de implementar el patrón Singleton es utilizando un decorador que modifique el comportamiento de la clase."""
def singleton(cls):
    instances = {} 

def get_instance(*args, **kwargs):
    if cls not in instances:
        instances[cls] = cls(*args, **kwargs) 
        return instances[cls] 
    return get_instance

@singleton 
class Singleton: 
    def __init__(self): 
        self.value = "Singleton instance" 
# Prueba del patrón Singleton 
obj1 = Singleton() 
obj2 = Singleton() 
print(obj1 is obj2) 
# True, ambas son la misma instancia 

"""Explicación:
El decorador singleton guarda una instancia de la clase en un diccionario.
La primera vez que se llama a la clase, se crea la instancia y se guarda.
En las siguientes llamadas, se devuelve la misma instancia almacenada."""

"""3. Usando un módulo como Singleton:
Los módulos en Python son instanciados una sola vez por el importador, lo que los convierte en una forma sencilla de 
crear un Singleton."""
# singleton.py
class Singleton:
    def __init__(self):
        self.value = "Singleton instance" 
# test.py 
from singleton import Singleton 
obj1 = Singleton() 
obj2 = Singleton()
print(obj1 is obj2) # True, ambas son la misma instancia 

"""Explicación:
El módulo se ejecuta solo una vez y, por lo tanto, solo se crea una instancia de la clase dentro del módulo.
Esto hace que el módulo se comporte como un Singleton."""

"""Uso práctico del Singleton

Este patrón se utiliza comúnmente en escenarios donde se necesita una única instancia de una clase para manejar recursos compartidos, como conexiones a bases de datos, registros de configuración, gestores de sesión, etc.

Ejemplo práctico:
Supongamos que estamos creando una clase para gestionar una conexión a una base de datos. No queremos crear múltiples instancias de la clase, ya que cada conexión es costosa. Aquí es donde el patrón Singleton puede ser útil:"""
class DatabaseConnection:
    _instancia = None 
    def __new__(cls): 
        if cls._instancia is None: 
            cls._instancia = super(DatabaseConnection, cls).__new__(cls) 
            cls._instancia.connection = "Conexión a la base de datos" 
        return cls._instancia 
    
    def get_connection(self): 
        return self.connection 
# Uso del Singleton 
db1 = DatabaseConnection() 
db2 = DatabaseConnection() 
print(db1.get_connection()) # "Conexión a la base de datos"
print(db1 is db2) # True, ambas son la misma instancia 
#En este ejemplo, la clase DatabaseConnection se asegura de que solo haya una conexión a la base de datos en toda la aplicación.


"""Conceptos relacionados """

"""1. Patrón de Diseño
El Patrón Singleton es uno de los 23 patrones de diseño de software descritos en el libro Design Patterns: Elements of Reusable Object-Oriented Software de Erich Gamma, Richard Helm, Ralph Johnson y John Vlissides (conocidos como la "Gang of Four"). Los patrones de diseño son soluciones reutilizables para problemas comunes en el desarrollo de software. El Singleton es uno de los patrones creacionales, que se enfoca en cómo se crean los objetos.

2. Patrón de Diseño Creacional
El Singleton pertenece a los patrones creacionales, que son patrones que se utilizan para crear objetos de manera controlada, asegurando que el proceso de instanciación sea adecuado a las necesidades de la aplicación. Otros patrones creacionales incluyen:
Factory Method
Abstract Factory
Builder
Prototype

3. Estado Global
El uso de un Singleton puede introducir un estado global dentro de una aplicación, ya que garantiza que una única instancia del objeto esté disponible en todo el programa. El estado global puede ser problemático en aplicaciones grandes, ya que introduce dependencias implícitas entre diferentes partes del sistema.

4. Acoplamiento Débil
En programación, el acoplamiento se refiere a cómo dependen unas clases de otras. El Singleton puede incrementar el acoplamiento entre las clases que dependen de la instancia única, ya que estas clases no tienen acceso directo a su propia instancia, sino que dependen de la clase Singleton.

5. Instanciación Perezosa (Lazy Instantiation)
El patrón Singleton puede implementarse mediante instanciación perezosa, lo que significa que la instancia de la clase no se crea hasta que se necesite por primera vez. Esto ayuda a optimizar los recursos y el tiempo de ejecución si la creación de la instancia es costosa.

6. Sincronización (Thread-Safety)
Cuando trabajas con hilos (threads) en un entorno multihilo, el Singleton debe ser implementado de manera que garantice 

que solo se cree una instancia, incluso cuando varios hilos acceden a la clase simultáneamente. Esto generalmente se maneja mediante bloqueos (locks) o utilizando mecanismos de sincronización como threading.Lock en Python.

7. Factory Method
El Factory Method es otro patrón creacional que puede ser utilizado para crear instancias de objetos. A diferencia del Singleton, el Factory Method permite crear múltiples instancias de objetos, pero lo hace a través de un método común para facilitar su creación.

8. Dependencia de Inyección
La inyección de dependencias es un patrón de diseño que permite gestionar las dependencias de una clase de forma explícita, en lugar de que las clases creen sus propias instancias. Aunque el Singleton garantiza una única instancia, la inyección de dependencias puede ser preferible cuando se necesita más flexibilidad para gestionar las instancias de los objetos.

9. Patrón de Diseño Eager Initialization
En el contexto del Singleton, la inicialización ágil (o "eager initialization") se refiere a crear la instancia del Singleton tan pronto como la clase se cargue, a diferencia de la instanciación perezosa ("lazy initialization"), que crea la instancia solo cuando es necesaria.

10. Proxy
El patrón Proxy es otro patrón estructural que permite crear un objeto sustituto (proxy) que controla el acceso a otro objeto. En algunos casos, un Proxy puede usarse para asegurar que solo haya una instancia de un objeto y controlar su acceso, de una manera similar a cómo el Singleton asegura que solo haya una instancia de la clase.

11. Global Variable (Variable Global)
Un Singleton puede ser considerado una variable global que está encapsulada en una clase. Aunque no se recomienda abusar de las variables globales en la programación, los Singletons son, en cierto sentido, una forma controlada de gestionar un estado global, proporcionando un punto único de acceso a una instancia.

12. Event Bus
Un Event Bus es un sistema de gestión de eventos que puede ser implementado utilizando un Singleton. Si tu aplicación tiene un sistema de eventos que debe ser accesible globalmente (por ejemplo, un bus de mensajes o de notificaciones), el patrón Singleton es una forma efectiva de asegurar que solo haya una instancia del bus.

13. Thread-Safety
La seguridad en hilos (thread-safety) en el contexto del patrón Singleton implica asegurarse de que el acceso y la creación de la instancia sea seguro cuando varias hebras (threads) acceden al Singleton simultáneamente. Esto puede involucrar el uso de mecanismos de sincronización para evitar condiciones de carrera (race conditions)."""





"""Prácticas recomendadas """

"""1. Evitar el abuso del Singleton
Aunque el patrón Singleton puede ser útil en ciertas situaciones, no debe ser utilizado en exceso. El abuso del Singleton puede llevar a un diseño desacoplado y difícil de probar. Es mejor usarlo solo cuando realmente sea necesario que haya una única instancia de una clase (por ejemplo, en la gestión de conexiones a bases de datos o en la configuración global).

2. Implementación perezosa (Lazy Instantiation)
Usar instanciación perezosa es una buena práctica. Esto significa que la instancia del Singleton no se crea hasta que sea necesaria. Esto ayuda a optimizar el rendimiento al evitar la creación de objetos innecesarios si no se utilizan."""
class Singleton: 
    instancia = None 
    def __new__(cls): 
        if cls._instancia is None: 
            cls._instancia = super(Singleton, cls).__new__(cls) 
        return cls._instancia 

#

"""3. Sincronización en entornos multihilo
Si tu aplicación es multihilo, asegúrate de que la instancia Singleton se cree de forma segura. Puedes utilizar mecanismos de sincronización como bloqueos (locks) para garantizar que solo un hilo cree la instancia.
import threading """
class Singleton:
    _instancia = None 
    _lock = threading.Lock() 

    def __new__(cls): 
        with cls._lock:
            if cls._instancia is None:
                cls._instancia = super(Singleton, cls).__new__(cls) 
            return cls._instancia 

#

"""4. Evitar la instanciación en el momento de la definición
Evita crear la instancia del Singleton cuando el módulo o la clase es cargada, a menos que realmente lo necesites. La instanciación perezosa mejora la eficiencia y hace el código más flexible."""
class Singleton:
    _instancia = None

    def __new__(cls): 
        if cls._instancia is None: 
            cls._instancia = super(Singleton, cls).__new__(cls)
        return cls._instancia 

#

"""5. Uso de un Singleton como un servicio global
Cuando implementes un Singleton para manejar servicios globales (como la conexión a una base de datos o un sistema de registro), asegúrate de que su interfaz sea clara y esté bien documentada. El acceso al Singleton debe ser sencillo y comprensible."""
class DatabaseConnection: 
    _instancia =  None 

    def __new__(cls):
        if cls._instancia is None: 
            cls._instancia = super(DatabaseConnection, cls).__new__(cls)
            cls._instancia.connection = "Conexión a la base de datos"
        return cls._instancia 

#

"""6. Evitar la dependencia de estado global
Si bien el Singleton puede proporcionar una instancia única, ten cuidado de no convertirlo en una fuente de estado global. El acceso global a una instancia puede generar dependencia entre componentes y dificultar las pruebas. Mantén el Singleton enfocado en una tarea concreta y bien definida.

7. Documentar la clase Singleton
Debido a que el Singleton es un patrón de diseño que puede ser confuso para quienes no están familiarizados con él, es importante documentar su propósito y uso. Explica por qué necesitas una instancia única y cómo debe usarse."""
class Singleton:
    """Clase que implementa el patrón Singleton. Se asegura de que solo haya una instancia de la clase.""" 
    _instancia = None 
#

"""8. Pruebas unitarias
El patrón Singleton puede dificultar las pruebas unitarias, especialmente si el Singleton es utilizado de forma global. Usa técnicas como inversión de dependencias o mocks para controlar la instancia en las pruebas."""
import unittest from unittest.mock
import patch
class TestSingleton(unittest.TestCase): 
    @patch('path_to.Singleton') 
    def test_singleton(self, MockSingleton): 
        MockSingleton.return_value = MockSingleton()
        
        
instance1 = Singleton()
instance2 = Singleton() 
self.assertIs(instance1, instance2) # Ambas instancias deben ser iguales 

#

"""9. Evitar la creación de instancias dentro del constructor
Si estás utilizando el patrón Singleton, asegúrate de no crear instancias adicionales dentro del constructor o en otros lugares donde no sea necesario. La creación de instancias debe ser controlada de manera centralizada.

10. Considerar el uso de alternativas
En lugar de usar un Singleton, evalúa si el uso de una fábrica de objetos o inyección de dependencias podría ser una mejor opción para evitar los problemas de acoplamiento y estado global."""

"""Técnicas recomendadas para implementar y trabajar con el Patrón Singleton:"""

"""2. Uso de un Lock (Bloqueo) en Entornos Multihilo
En un entorno multihilo, cuando múltiples hilos intentan acceder a la instancia del Singleton simultáneamente, es posible que se creen múltiples instancias. Para evitar esto, puedes usar un bloqueo (lock) para sincronizar el acceso a la instancia y asegurar que solo un hilo cree la instancia del Singleton.

Ejemplo con lock:"""
import threading

class Singleton:
    _instancia = None
    lock = threading.Lock() 

    def __new__(cls):
        with cls._lock: # Asegura que solo un hilo pueda crear la instancia 
            if cls._instancia is None: 
                cls._instancia = super(Singleton, cls).__new__(cls) 
            return cls._instancia 

#

"""3. Uso de Decoradores para Simplificar el Código
Si deseas evitar tener que manejar el bloqueo y la instancia manualmente, puedes usar un decorador para asegurarte de que solo se crea una instancia. Esta es una técnica más elegante y reduce la complejidad del código.

Ejemplo con decorador:"""
def singleton(cls):
    instances = {}

def get_instance():
    if cls not in instances: 
        instances[cls] = cls()
        return instances[cls] 
    return get_instance 

@singleton 
class Singleton:
    def __init__(self): self.value = "Soy único" 

#

"""4. Singleton usando Módulos
Una técnica comúnmente usada en Python es aprovechar las propiedades de los módulos para implementar un Singleton, ya que en Python los módulos se cargan una sola vez, lo que asegura que haya una única instancia del módulo a lo largo de la ejecución de la aplicación.

Ejemplo usando un módulo:"""
# singleton.py 
class Singleton: 
    def __init__(self):
        self.value = "Soy único" 

singleton_instance = Singleton() # En otro archivo import singleton 
instance = singleton.singleton_instance 

#

"""5. Singleton con Métodos Estáticos
Otra técnica es usar un método estático para devolver la instancia única. Esto asegura que no se cree la instancia de forma inadvertida.

Ejemplo con método estático:"""
class Singleton:
    _instancia = None 

@staticmethod 
def get_instance(): 
    if Singleton._instancia is None: 
        Singleton._instancia = Singleton() 
    return Singleton._instancia 

#

"""6. Uso de una Variable de Clase para la Instancia
En lugar de crear una instancia en el método __new__, puedes usar una variable de clase para almacenar la instancia. Esta técnica simplifica el código y también puede ayudar a mantener la claridad del patrón Singleton.

Ejemplo con variable de clase:"""
class Singleton:
    _instancia = None 
    def __init__(self):
        if Singleton._instancia is not None: 
            raise Exception("Ya existe una instancia")
        Singleton._instancia = self 

    @classmethod 
    def get_instance(cls): 
        if cls._instancia is None:
            cls._instancia = Singleton() 
        return cls._instancia 


#

"""7. Singleton con Métodos de Clases (Class Methods)
Puedes usar un método de clase para la creación de la instancia del Singleton. Esto es útil si la lógica de creación necesita ser más flexible.

Ejemplo con método de clase:"""
class Singleton:
    _instancia = None 

    @classmethod 
    def get_instance(cls):
        if cls._instancia is None:
            cls._instancia = Singleton() 
        return cls._instancia 

#

"""8. Instanciación Eager (Inicialización ágil)
En algunos casos, puede ser preferible crear la instancia del Singleton tan pronto como se cargue el módulo o la clase, sin esperar a que se necesite.

Ejemplo de instanciación eager:"""
class Singleton:
    _instancia = Singleton() 

    def __init__(self): 
        self.value = "Soy único" # La instancia está disponible desde el inicio

instance = Singleton._instancia 

#

"""9. Clonación de Objetos (Deshabilitar la Clonación)
En el patrón Singleton, puede que quieras evitar que otros intenten clonar la instancia o crear copias del Singleton. Esto se puede lograr anulando el método __copy__ y __deepcopy__.

Ejemplo de deshabilitación de clonación:"""
import copy 
class Singleton: 
    _instancia = None
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Singleton, cls).__new__(cls)
        return cls._instancia 

    def __copy__(self): 
        raise Exception("No se puede clonar una instancia de Singleton") 

    def __deepcopy__(self, memo):
        raise Exception("No se puede clonar una instancia de Singleton") 
