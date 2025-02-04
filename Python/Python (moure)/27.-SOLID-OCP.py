"""El Principio de Abierto/Cerrado (OCP). Este principio establece que una clase debe ser abierta para su extensión pero cerrada para su modificación. Esto significa que deberíamos poder agregar nuevas funcionalidades a una clase sin necesidad de modificar su código existente, minimizando el riesgo de introducir errores en el sistema, en lugar de modificar el código existente cuando queremos cambiar o agregar comportamientos, deberíamos ser capaces de extender el comportamiento de las clases mediante la adición de nuevas clases o módulos sin modificar las clases originales. Esto se puede lograr mediante la herencia, la composición o el uso de interfaces/abstract classes, lo que permite añadir funcionalidades sin alterar el código base que ya está probado y funcionando.

Cómo aplicar el OCP
Uso de interfaces y clases abstractas
Las interfaces y clases abstractas permiten definir un conjunto de operaciones comunes sin imponer detalles de implementación, lo que facilita la extensión sin modificar el código base. Ejemplo: Si tienes una clase ProcesadorDePago, puedes crear diferentes clases concretas como PagoConTarjeta o PagoConPaypal que implementen una interfaz común como IPago sin modificar la clase ProcesadorDePago original.

Patrón de diseño Strategy
El patrón Strategy permite cambiar el comportamiento de una clase en tiempo de ejecución, encapsulando los algoritmos en clases separadas que implementan una interfaz común. Ejemplo: Si tienes una clase Calculadora que realiza distintas operaciones, puedes implementar diferentes estrategias de cálculo (como sumar, restar, multiplicar) y luego asignarlas a la calculadora sin modificar la clase base.

Patrón de diseño Decorator
El patrón Decorator permite agregar comportamientos adicionales a un objeto de manera dinámica sin modificar la clase original. Esto se logra envolviendo el objeto original en una clase decoradora que agrega funcionalidad. Ejemplo: Si tienes una clase Pizza y quieres añadir diferentes ingredientes como QuesoExtra o Aceitunas, puedes hacerlo sin modificar la clase Pizza usando decoradores.

Composición sobre herencia
La composición permite extender las funcionalidades de una clase sin tener que usar la herencia, lo que hace que las clases sean más flexibles y fáciles de modificar sin afectar la base. Ejemplo: Si tienes una clase Empleado, en lugar de crear clases hijas para cada tipo de empleado, puedes usar un objeto de clase TipoDeEmpleado que contenga la lógica específica para cada tipo.

Uso de eventos o delegación
En lugar de modificar el comportamiento de una clase directamente, puedes usar eventos o delegación para extenderla. Esto permite que la clase original delegue el comportamiento a otras clases, manteniendo su código cerrado pero permitiendo la extensión. Ejemplo: En un sistema de pagos, puedes usar un sistema de eventos donde la clase Pago delega las diferentes operaciones de procesamiento a los manejadores de eventos según el tipo de pago.

Ejemplo de OCP
Antes de aplicar OCP (código sin OCP):"""
class Calculadora: 
    def calcular(self, tipo, a, b): 
        if tipo == "suma": 
            return a + b 
        elif tipo == "resta": 
            return a - b
        else: 
            raise ValueError("Operación no soportada") 

"""En este ejemplo, la clase Calculadora tiene un método calcular que cambia cada vez que se necesita agregar una nueva operación. Si queremos agregar una nueva operación (como multiplicación o división), tendríamos que modificar la clase Calculadora, lo cual viola el principio OCP.
Después de aplicar OCP (con OCP):"""
class Operacion: 
    def calcular(self, a, b): 
        pass 

class Suma(Operacion): 
    def calcular(self, a, b): 
        return a + b 

class Resta(Operacion): 
    def calcular(self, a, b): 
        return a - b

class Calculadora: 
    def __init__(self, operacion: Operacion):
        self.operacion = operacion

    def calcular(self, a, b): 
        return self.operacion.calcular(a, b) 

"""En este caso, las clases Suma y Resta implementan la interfaz Operacion. Si queremos agregar una nueva operación, no es necesario modificar la clase Calculadora; simplemente agregamos una nueva clase que implemente Operacion, como Multiplicacion, y la pasamos como parámetro al constructor de Calculadora. De esta forma, la clase Calculadora sigue siendo "cerrada para modificaciones" pero "abierta para extensiones".

conceptos relacionados con el Principio de Abierto/Cerrado (OCP) que te ayudarán a entender mejor cómo aplicarlo en tus proyectos y cómo se conecta con otros principios y patrones de diseño:"""

"""1. Composición sobre Herencia
Descripción: Composición es una forma de construir clases que incorporan instancias de otras clases. En lugar de extender una clase base mediante herencia, la composición permite que una clase mantenga su flexibilidad y su capacidad de ser extendida sin tener que modificarse. Ejemplo: Si tienes una clase Empleado, en lugar de heredar de una clase base Persona, puedes componerla con objetos como Direccion o Telefono que contengan la lógica adicional sin modificar Empleado.


2. Inyección de Dependencias
Descripción: La inyección de dependencias es un patrón que permite pasar las dependencias a una clase en lugar de crearla dentro de ella. Esto facilita la extensión de las funcionalidades de una clase sin cambiar su código. Ejemplo: Si tienes una clase Pedido que necesita un servicio de pago, puedes inyectar la dependencia de un servicio de pago como PagoConTarjeta o PagoConPaypal sin tener que modificar la clase Pedido.

3. Acoplamiento Bajo y Cohesión Alta
Descripción: Acoplamiento bajo significa que las clases tienen pocas dependencias entre sí, mientras que cohesión alta significa que las clases están bien centradas en una única responsabilidad. El principio OCP promueve el acoplamiento bajo, ya que la extensión de una clase no debe afectar a las clases existentes. Ejemplo: Si tienes una clase Factura que solo se encarga de crear facturas y no depende de otras clases que implementan comportamientos adicionales (como pagos o notificaciones), entonces la clase está bien diseñada con acoplamiento bajo y es fácil de extender.

4. Principio de Responsabilidad Única (SRP)
Descripción: Aunque SRP y OCP son principios distintos, están estrechamente relacionados. El SRP dice que una clase debe tener solo una razón para cambiar. Si una clase tiene más de una responsabilidad, se vuelve difícil de extender sin modificarla, lo que entra en conflicto con OCP. Ejemplo: Si tienes una clase que maneja tanto el procesamiento de pagos como el envío de correos electrónicos, sería más difícil de extender sin modificarla. Sin embargo, si separas estas responsabilidades en clases diferentes (una para el pago y otra para el correo electrónico), cada clase puede extenderse de forma independiente sin afectar a la otra.

9. Diseño Modular
Descripción: El diseño modular es una forma de dividir el sistema en módulos que pueden ser extendidos sin modificar los módulos existentes. Esto es crucial para aplicar el principio OCP, ya que cada módulo puede ser extendido de manera independiente. Ejemplo: Si tienes un sistema de ventas, puedes tener módulos independientes para la gestión de productos, pagos y usuarios. Cada módulo puede ser ampliado o modificado sin afectar a los demás.

10. Abstracción
Descripción: La abstracción es el proceso de ocultar los detalles de implementación y mostrar solo lo necesario. Esto se aplica al principio OCP mediante el uso de clases abstractas e interfaces que proporcionan una capa de abstracción sobre los detalles específicos, permitiendo extender el comportamiento sin modificar el código base. Ejemplo: Una clase Vehiculo puede tener métodos abstractos como arrancar(), y luego diferentes implementaciones como Coche o Bicicleta proporcionan la implementación específica. El código que utiliza Vehiculo no necesita conocer las clases concretas.

11. Código Limpio (Clean Code)
Descripción: El principio OCP es fundamental para escribir código limpio, ya que permite que el código se mantenga flexible y fácil de entender a medida que evoluciona, sin introducir complejidad innecesaria al modificar clases existentes. Ejemplo: Si sigues el principio OCP, puedes agregar nuevas funcionalidades o requisitos sin que el código se vuelva más complejo o difícil de entender."""




"""El módulo abc (Abstract Base Classes) proporciona una forma de definir clases abstractas y métodos abstractos, lo que permite definir un contrato para las clases hijas sin necesidad de crear una implementación completa. Para asegurar que las clases que heredan de una clase base implementen ciertos métodos, pero no quieres proporcionar una implementación específica en la clase base.

Una clase abstracta es una clase que no puede ser instanciada directamente, y que generalmente contiene métodos abstractos. Los métodos abstractos son métodos que no tienen implementación en la clase base, pero que deben ser implementados por las clases hijas. El módulo abc facilita la creación de clases abstractas y la definición de métodos abstractos mediante el uso de la metaclase ABC y el decorador @abstractmethod.

Elementos principales del módulo abc:

1. ABC (Abstract Base Class)

La metaclase ABC se usa para declarar que una clase es abstracta.
Las clases que heredan de ABC se consideran clases abstractas, y no pueden ser instanciadas directamente.

2. @abstractmethod (Método abstracto)
Es un decorador utilizado para marcar los métodos que deben ser implementados por las clases hijas.
Si una clase tiene métodos abstractos, no se podrá instanciar, a menos que todos los métodos abstractos sean implementados en las clases hijas."""

"""Cómo utilizar el módulo abc"""

"""Paso 1: Importar el módulo abc
Necesitamos importar ABC y abstractmethod para poder definir clases y métodos abstractos."""
from abc import ABC, abstractmethod 

"""Paso 2: Crear una clase abstracta
Se define una clase que hereda de ABC y se usa @abstractmethod en los métodos que deben ser implementados por las clases hijas."""
class Animal(ABC): 
    @abstractmethod 
    def hacer_sonido(self): 
        pass 

#En este ejemplo, la clase Animal es abstracta y tiene el método abstracto hacer_sonido. Cualquier clase que herede de Animal debe proporcionar una implementación para este método.

"""Paso 3: Crear clases hijas
Las clases hijas deben proporcionar una implementación de los métodos abstractos definidos en la clase base abstracta."""
class Perro(Animal): 
    def hacer_sonido(self): 
        return "Guau!"

class Gato(Animal): 
    def hacer_sonido(self): 
        return "Miau!" 

#Ahora las clases Perro y Gato implementan el método hacer_sonido, por lo que son instanciables.

#Paso 4: Instanciar las clases hijas
perro = Perro() 
print(perro.hacer_sonido()) # Output: Guau! 

gato = Gato() 
print(gato.hacer_sonido()) # Output: Miau! 

#Explicación detallada de conceptos importantes:

"""1. Métodos abstractos
Un método abstracto es un método que está definido en la clase base pero sin implementación. Las clases hijas deben sobrescribir este método y proporcionar una implementación concreta.
Los métodos abstractos se definen mediante el decorador @abstractmethod.

2. ABC (Abstract Base Class)
ABC es una metaclase que, al ser heredada por una clase, convierte a esa clase en abstracta. Las clases abstractas no pueden ser instanciadas directamente. Se debe crear una subclase que implemente los métodos abstractos.

3. Instanciación de clases abstractas
No se puede instanciar directamente una clase abstracta. Si intentas instanciarla, obtendrás un error TypeError.
animal = Animal() # Error: TypeError: Can't instantiate abstract class Animal with abstract methods hacer_sonido 

Sí se pueden instanciar las subclases que implementan los métodos abstractos:"""
perro = Perro() # Correcto 

"""4. Comportamiento obligatorio de las subclases
Las subclases de una clase abstracta deben implementar todos los métodos abstractos. Si una subclase no implementa un método abstracto, no podrá ser instanciada y se generará un error."""
class Pez(Animal): 
    pass 

pez = Pez() # Error: TypeError: Can't instantiate abstract class Pez with abstract methods hacer_sonido 

"""5. Clases con implementación parcial
Las clases abstractas pueden tener métodos con implementación parcial. Las subclases pueden sobrescribir estos métodos si lo desean, pero no es obligatorio."""
class Animal(ABC): 
    @abstractmethod 
    def hacer_sonido(self): 
        pass

    def moverse(self):
        return "Se mueve" 

class Gato(Animal): 
    def hacer_sonido(self):
        return "Miau!" 

gato = Gato() 
print(gato.moverse()) # Output: Se mueve 

"""6. Verificación de implementación de métodos abstractos
Si deseas verificar si una clase concreta ha implementado todos los métodos abstractos, puedes usar la función issubclass() y el método register()."""
from abc import ABCMeta
class Animal(ABC): 
    @abstractmethod 
    def hacer_sonido(self): 
        pass

class Perro(Animal): 
    def hacer_sonido(self): 
        return "Guau!" 

print(issubclass(Perro, Animal)) # Output: True 

#Ejemplo completo con varios métodos abstractos:
from abc import ABC, abstractmethod
# Clase abstracta 
class Vehiculo(ABC): 
    @abstractmethod 
    def acelerar(self): 
        pass 

    @abstractmethod 
    def frenar(self):
        pass 

# Subclases concretas
class Coche(Vehiculo): 
    def acelerar(self): 
        return "El coche acelera" 

    def frenar(self): 
        return "El coche frena"

class Bicicleta(Vehiculo): 
    def acelerar(self): 
        return "La bicicleta acelera" 

    def frenar(self): 
        return "La bicicleta frena"

# Instanciando objetos 
coche = Coche() 
bicicleta = Bicicleta() 
print(coche.acelerar()) # Output: El coche acelera 
print(bicicleta.frenar()) # Output: La bicicleta frena 


"""1. ABC (Abstract Base Class)

La clase ABC es la clase base de la cual las clases abstractas deben heredar. Utilizando esta clase metaclase, podemos convertir una clase en una clase abstracta, lo que significa que no puede ser instanciada directamente.
Uso:  Una clase que hereda de ABC se convierte en abstracta y no puede ser instanciada directamente.
Las clases abstractas pueden contener métodos abstractos, pero también pueden tener implementaciones concretas."""
from abc import ABC 

class Animal(ABC):
    pass 
#En este ejemplo, Animal es una clase abstracta porque hereda de ABC.

"""2. @abstractmethod
El decorador @abstractmethod se usa para marcar un método como abstracto. Esto significa que cualquier clase hija de una clase abstracta debe implementar este método para poder ser instanciada.
Uso: Un método marcado con @abstractmethod no tiene implementación en la clase base y obliga a las subclases a implementarlo.
Si la subclase no implementa el método, no se puede instanciar la subclase."""
from abc import ABC, abstractmethod 

class Animal(ABC): 
    @abstractmethod 
    def hacer_sonido(self): 
        pass 

# No implementación 
class Perro(Animal): 
    def hacer_sonido(self): 
        return "Guau!" 
# animal = Animal() 
# Esto dará error, porque Animal tiene un método abstracto 
perro = Perro() # Esto es válido porque Perro implementa el método abstracto
print(perro.hacer_sonido()) # Output: Guau! 
#En este caso, el método hacer_sonido es obligatorio para cualquier clase que herede de Animal, como Perro.

"""3. @abstractmethod en métodos con implementación
Aunque generalmente se usa @abstractmethod para definir métodos sin implementación, es posible utilizarlo en métodos que sí tengan una implementación parcial en la clase base.
Uso: El decorador puede ser utilizado en métodos con implementación, lo que permite que las subclases sobreescriban estos métodos si lo desean."""
from abc import ABC, abstractmethod
class Vehiculo(ABC): 
    @abstractmethod
    def acelerar(self):
        pass
    def frenar(self):
        return "Frenando el vehículo" 

class Coche(Vehiculo): 
    def acelerar(self): 
        return "Acelerando el coche" 

coche = Coche() 
print(coche.acelerar()) # Output: Acelerando el coche 
print(coche.frenar()) # Output: Frenando el vehículo 

#En este ejemplo, frenar tiene una implementación por defecto en la clase base Vehiculo, pero acelerar sigue siendo abstracto y debe ser implementado por las subclases.

"""4. register()
El método register() se utiliza para registrar una clase como una subclase de una clase abstracta sin necesidad de heredar de ella directamente. Este método es útil cuando tienes una clase que no hereda de una clase abstracta pero deseas que sea tratada como si lo hiciera.
Uso: Registra una clase como subclase de una clase base abstracta, lo que le otorga el comportamiento de ser una subclase de dicha clase abstracta."""
from abc import ABC, abstractmethod 
class Animal(ABC): 
    @abstractmethod 
    def hacer_sonido(self): 
        pass 

class Perro: 
    def hacer_sonido(self):
        return "Guau!"
# Registrar Perro como una subclase de Animal
Animal.register(Perro)
perro = Perro() 
print(isinstance(perro, Animal)) # Output: True 

#Aquí, a pesar de que Perro no hereda directamente de Animal, al registrarlo como subclase de Animal, Python trata a Perro como si fuera una subclase de Animal.

"""5. __subclasshook__()

El método __subclasshook__() es un método especial que puede ser sobrescrito en una clase abstracta para personalizar el comportamiento de issubclass() y isinstance(). Este método permite controlar cómo Python determina si una clase es o no una subclase de una clase abstracta.
Uso: Se puede sobrescribir para implementar lógica personalizada al verificar si una clase es una subclase de otra.
from abc import ABC, abstractmethod """
class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self): 
        pass

    @classmethod 
    def __subclasshook__(cls, C): 
        if any("hacer_sonido" in B.__dict__ for B in C.__mro__): 
            return True
        return NotImplemented 

class Perro: 
    def hacer_sonido(self):
        return "Guau!" 
# Ahora se considera a Perro como subclase de Animal 
print(issubclass(Perro, Animal)) # Output: True 

"""6. ABCMeta
ABCMeta es la metaclase usada por ABC para definir las clases abstractas. Aunque la mayoría de las veces no es necesario usarla directamente, se puede utilizar para crear clases abstractas de forma más programática.
Uso: Puedes crear clases abstractas dinámicamente al usar ABCMeta como metaclase."""
from abc import ABCMeta, abstractmethod 
class Animal(metaclass=ABCMeta):
    @abstractmethod 
    def hacer_sonido(self):
        pass 



#Los decoradores @abstractmethod, @abstractclassmethod, @abstractstaticmethod y @abstractproperty son todos decoradores que se utilizan en el contexto de clases abstractas en Python, y son proporcionados por el módulo abc. 

"""A. @abstractmethod
El decorador @abstractmethod es el más común y se usa para marcar un método como abstracto en una clase abstracta. Un método abstracto es aquel que no tiene implementación en la clase base (abstracta) y debe ser implementado por cualquier subclase no abstracta.
Uso: Se utiliza para definir métodos que las subclases deben implementar.
Es aplicable a métodos normales dentro de una clase abstracta."""
from abc import ABC, abstractmethod 
class Animal(ABC): 
    @abstractmethod 
    def hacer_sonido(self): 
        pass 

class Perro(Animal): 
    def hacer_sonido(self):
        return "Guau!"
# animal = Animal() 
# Esto da error, ya que Animal tiene un método abstracto. 
perro = Perro() 
print(perro.hacer_sonido()) # Output: Guau! 

"""B. @abstractclassmethod
El decorador @abstractclassmethod es utilizado para marcar un método de clase como abstracto. Es similar a @abstractmethod, pero se aplica a métodos de clase, los cuales son definidos con @classmethod y suelen tener al menos un parámetro, típicamente cls, que hace referencia a la clase misma.
Uso: Se aplica a métodos de clase que no tienen implementación en la clase base.
Las subclases deben implementar este método de clase."""
from abc import ABC, abstractclassmethod
class Vehiculo(ABC): 
    @abstractclassmethod 
    def obtener_tipo(cls):
        pass 
    
class Coche(Vehiculo):
    @classmethod
    def obtener_tipo(cls): 
        return "Coche"

# vehiculo = Vehiculo() # Error: no se puede instanciar una clase abstracta. 
coche = Coche() 
print(coche.obtener_tipo()) # Output: Coche 


"""C. @abstractstaticmethod
El decorador @abstractstaticmethod marca un método estático como abstracto en una clase abstracta. Similar a los otros decoradores, pero aplicable a métodos estáticos, que son métodos que no requieren un objeto o una clase para ser invocados, es decir, no toman self ni cls como primer argumento.
Uso: Se aplica a métodos estáticos que no tienen implementación en la clase base.
Las subclases deben implementar este método estático."""
from abc import ABC, abstractstaticmethod 
class Figura(ABC): 
    @abstractstaticmethod 
    def area(): 
        pass 

class Cuadrado(Figura): 
    @staticmethod 
    def area(): 
        return 25

# figura = Figura() # Error: no se puede instanciar una clase abstracta. 
cuadrado = Cuadrado() 
print(cuadrado.area()) # Output: 25 

"""D. @abstractproperty
El decorador @abstractproperty se utilizaba anteriormente para marcar propiedades de la clase como abstractas. Sin embargo, desde Python 3.3, el uso de @abstractproperty ha quedado obsoleto, y se recomienda usar @property en combinación con @abstractmethod para definir propiedades abstractas.
Uso: Se aplica a propiedades que las subclases deben implementar. Aunque ha quedado obsoleto, el uso más actualizado es usar @property junto con @abstractmethod."""
from abc import ABC, abstractmethod 
class Animal(ABC): 
    @property 

    @abstractmethod 
    def sonido(self): 
        pass 

class Perro(Animal): 
    @property 
    def sonido(self): 
        return "Guau!"

perro = Perro() 
print(perro.sonido) # Output: Guau! 
#En este ejemplo, sonido se define como una propiedad abstracta utilizando @property junto con @abstractmethod, que es la forma recomendada actualmente.

"""Diferencias Clave:
@abstractmethod:
Se usa para marcar un método normal (no estático, no de clase) como abstracto.
Debe ser implementado por las subclases.

@abstractclassmethod:
Se usa para marcar un método de clase como abstracto.
El método debe ser definido como @classmethod y debe ser implementado por las subclases.

@abstractstaticmethod:
Se usa para marcar un método estático como abstracto.
El método debe ser definido como @staticmethod y debe ser implementado por las subclases.

@abstractproperty:
Estaba diseñado para marcar una propiedad como abstracta, pero ha sido obsoleto a partir de Python 3.3.
Actualmente, se utiliza @property en combinación con @abstractmethod para lograr el mismo propósito."""




"""Buenas prácticas para aplicar el OCP """

"""1. Usar Polimorfismo para Extender Funcionalidad
Una forma común de aplicar el OCP es utilizando el polimorfismo. Al definir clases base o interfaces con métodos que pueden ser implementados o sobrecargados por las subclases, puedes extender su comportamiento sin modificar las clases base.
Práctica: Define una clase o interfaz base con un comportamiento común.
Crea subclases que extiendan ese comportamiento según sea necesario.
No cambies el código de la clase base; agrega nuevas clases que implementen el comportamiento extendido."""
class Shape: 
    def draw(self): 
        pass 

class Circle(Shape): 
    def draw(self): 
        return "Drawing a Circle" 

class Rectangle(Shape): 
    def draw(self): 
        return "Drawing a Rectangle" 
# Agregar una nueva forma sin modificar las clases existentes 

class Triangle(Shape): 
    def draw(self): 
        return "Drawing a Triangle"
# Uso
shapes = [Circle(), Rectangle(), Triangle()]
for shape in shapes: 
    print(shape.draw()) 

"""2. Implementar Interfaces o Clases Abstractas
Usar interfaces o clases abstractas también es una excelente manera de aplicar OCP. Esto permite a las subclases implementar comportamientos específicos sin necesidad de modificar el código de la clase base.
Práctica: Define una interfaz o clase abstracta con métodos abstractos.
Las subclases implementan esos métodos de acuerdo a sus necesidades.
Si deseas agregar nuevos comportamientos, crea nuevas subclases en lugar de modificar la base."""
from abc import ABC, abstractmethod 
class PaymentMethod(ABC): 
    @abstractmethod 
    def process_payment(self, amount): 
        pass

class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        return f"Processing credit card payment of {amount}" 

class PayPal(PaymentMethod): 
    def process_payment(self, amount): 
        return f"Processing PayPal payment of {amount}" 
# Uso
payments = [CreditCard(), PayPal()] 
for payment in payments:
    print(payment.process_payment(100)) 

"""3. Preferir la Composición sobre la Herencia
La composición permite que las clases sean fácilmente extendidas al incluir nuevas funcionalidades a través de objetos en lugar de heredar de una clase base. Esta técnica ayuda a mantener el código cerrado para modificaciones directas pero abierto a nuevas funcionalidades.
Práctica: Si tienes varias clases con comportamientos similares, en lugar de hacer que una clase herede de otra, crea objetos que se componen entre sí.
Usa la composición para combinar funcionalidades de forma flexible sin modificar las clases originales."""
class Printer: 
    def print(self, document):
        return f"Printing {document}" 

class Scanner: 
    def scan(self, document): 
        return f"Scanning {document}" 

class MultiFunctionMachine:
    def __init__(self): 
        self.printer = Printer() 
        self.scanner = Scanner() 

    def print(self, document): 
        return self.printer.print(document) 

    def scan(self, document): 
        return self.scanner.scan(document) 

# Uso mfm = MultiFunctionMachine() 
print(mfm.print("Report")) 
print(mfm.scan("Report")) 

"""4. Usar Patrones de Diseño como el Strategy o Decorator
Los patrones de diseño como Strategy y Decorator ayudan a extender el comportamiento de una clase sin necesidad de modificarla, lo cual es la esencia del OCP.

Patrón Strategy:
Práctica: Puedes aplicar el patrón Strategy para encapsular diferentes comportamientos y seleccionarlos dinámicamente, sin cambiar el código de la clase principal."""
class PaymentMethod: 
    def pay(self, amount): 
        raise NotImplementedError 
        
class CreditCardPayment(PaymentMethod): 
    def pay(self, amount): 
        return f"Paid {amount} using Credit Card"

class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid {amount} using PayPal" 

class Order:
    def __init__(self, payment_method: PaymentMethod): 
        self.payment_method = payment_method 

    def complete_order(self, amount): 
        return self.payment_method.pay(amount) 
# Uso 

order = Order(CreditCardPayment())
print(order.complete_order(100)) 
order = Order(PayPalPayment()) 

print(order.complete_order(200)) 

"""Patrón Decorator:
Práctica: El patrón Decorator se utiliza para extender el comportamiento de un objeto sin modificar su estructura."""
class Coffee: 
    def cost(self): 
        return 5 
    
class MilkDecorator: 
    def __init__(self, coffee): 
        self._coffee = coffee 
        
    def cost(self):
        return self._coffee.cost() + 2 

class SugarDecorator: 
    def __init__(self, coffee): 
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 1 
# Uso
coffee = Coffee() 

print(coffee.cost()) # Output: 5 
coffee_with_milk = MilkDecorator(coffee) 
print(coffee_with_milk.cost()) # Output: 7 
coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk) 
print(coffee_with_milk_and_sugar.cost()) # Output: 8 

"""5. Evitar Modificar el Código Existente
El principio OCP subraya la importancia de evitar cambios en el código existente. Cuando se detecta la necesidad de nuevas funcionalidades, la solución debe ser agregar nuevas clases o módulos que extiendan el comportamiento, en lugar de modificar las clases ya existentes.
Práctica: Mantén el código base inmutable y crea nuevas implementaciones que agreguen nuevas funcionalidades.
Esto es especialmente útil cuando el código ya está en producción y evitar la modificación directa puede prevenir errores."""



"""Las técnicas"""

"""1. No Modificar Código Existente
Una técnica crucial para seguir el principio OCP es evitar modificar el código ya escrito. Cuando se desea agregar una nueva funcionalidad, en lugar de modificar el código existente, se debe agregar nueva lógica, creando nuevas clases o métodos.
Técnica: Cuando se necesita nueva funcionalidad, extiende el comportamiento sin modificar el código original. Añadir nuevas clases o métodos, manteniendo el código existente inmutable."""

# Definimos una clase que existe ya 
class ExistingClass: 
    def method_to_be_extended(self): 
        return "Existing Method"
# Agregamos funcionalidad extendida en una nueva clase 
class ExtendedClass(ExistingClass): 
    def new_method(self): 
        return "New Method Added" 
# Uso
existing = ExistingClass() 
print(existing.method_to_be_extended()) # Output: Existing Method 
extended = ExtendedClass() 
print(extended.method_to_be_extended()) # Output: Existing Method
print(extended.new_method()) # Output: New Method Added 

"""5. Use Dependencias Invertidas (Dependency Injection)
El principio de inversión de dependencias (parte de SOLID) se complementa muy bien con OCP. En lugar de depender de implementaciones concretas, puedes inyectar dependencias a tus clases, lo que facilita la extensión del comportamiento sin modificar el código existente.
Técnica: Usa inyección de dependencias para que las clases dependan de abstracciones en lugar de implementaciones concretas. Esto permite cambiar o extender el comportamiento sin modificar las clases existentes."""
class Database:
    def connect(self):
        return "Connecting to database" 

class Application: 
    def __init__(self, database: Database): 
        self.database = database 
        
    def start(self):         
        return self.database.connect() 
# Uso 
database = Database() 
app = Application(database) 
print(app.start()) # Output: Connecting to database 