"""1. Herencia
La herencia permite que una clase hija (subclase) herede atributos y métodos de una clase base (superclase), lo que fomenta la reutilización del código y la creación de jerarquías lógicas entre clases. Mediante la herencia, una clase puede especializarse a partir de una clase más general.

Subclase (clase hija): Una clase que hereda de otra. Puede heredar métodos y atributos de la clase base y puede sobrescribir (override) métodos para darles un comportamiento más específico.

Superclase (clase base): Una clase que proporciona atributos y métodos que pueden ser reutilizados por otras clases. Las subclases heredan estas características.
super(): Se utiliza para llamar a los métodos de la superclase desde la subclase. Es útil cuando queremos extender o modificar el comportamiento heredado. Ejemplo de herencia:"""
class Animal: 
    def __init__(self, nombre): 
        self.nombre = nombre 

    def hablar(self): 
        return "Hace un sonido." 

class Perro(Animal): 
    def __init__(self, nombre, raza): 
        super().__init__(nombre) 
        self.raza = raza 

    def hablar(self): 
        return "Ladra" 

# Crear instancia de la clase Perro 
mi_perro = Perro("Max", "Labrador") 
print(mi_perro.nombre) # Max (heredado de Animal) 
print(mi_perro.hablar()) # Ladra (sobrescrito en Perro) 
#En este ejemplo, Perro hereda de Animal y sobrescribe el método hablar para dar un comportamiento específico.

"""2. Polimorfismo
El polimorfismo permite que las mismas operaciones o métodos se comporten de manera diferente según el tipo de objeto en el que se apliquen. Es decir, los objetos de diferentes clases pueden responder al mismo mensaje de manera distinta.

Existen dos tipos de polimorfismo:
Polimorfismo de tiempo de compilación (estático): Se logra a través de la sobrecarga de métodos (en lenguajes que lo permiten).
Polimorfismo de tiempo de ejecución (dinámico): Se refiere a la sobrescritura de métodos en las clases derivadas. En este caso, la clase base define un método, y las subclases pueden modificar ese método según sus necesidades.

Sobrescritura (overriding): Cuando una subclase proporciona una implementación específica de un método que ya está definido en la superclase. El polimorfismo de tiempo de ejecución depende de esto.
Métodos abstractos y clases abstractas: En algunos casos, el polimorfismo se usa con clases abstractas y métodos abstractos que obligan a las subclases a implementar ciertos métodos.
Interfaces (o protocolos): Aunque no existe el concepto de "interfaces" de manera explícita en Python como en otros lenguajes, se pueden simular con clases abstractas. Ejemplo de polimorfismo:"""
class Animal: 
    def hablar(self): 
        raise NotImplementedError("El método hablar debe ser implementado por las subclases") 

class Perro(Animal): 
    def hablar(self): 
        return "Ladra" 

class Gato(Animal): 
    def hablar(self): 
        return "Mia" # Función que recibe cualquier objeto que herede de Animal 

    def hacer_sonar(animal): 
        print(animal.hablar()) # Usando polimorfismo 

mi_perro = Perro() 
mi_gato = Gato() 
hacer_sonar(mi_perro) # Ladra 

hacer_sonar(mi_gato) # Mia 
#En este ejemplo, la función hacer_sonar puede aceptar cualquier objeto que herede de Animal, pero el comportamiento del método hablar varía dependiendo de si el objeto es un Perro o un Gato, demostrando polimorfismo.

"""Relación entre Herencia y Polimorfismo
Herencia permite que las subclases hereden comportamientos de la superclase, lo que facilita la creación de una jerarquía de clases.
Polimorfismo permite que una función o un método se comporte de manera diferente dependiendo del tipo de objeto que lo invoque, aunque se llame al mismo método. Ejemplo combinado de Herencia y Polimorfismo:"""
class Vehiculo: 
    def mover(self): 
        raise NotImplementedError("El método mover debe ser implementado por las subclases") 

class Coche(Vehiculo): 
    def mover(self): 
        return "El coche se mueve por carretera." 

class Avion(Vehiculo): 
    def mover(self): 
        return "El avión vuela por el aire." # Función que acepta cualquier Vehiculo y llama a mover 

    def realizar_movimiento(vehiculo): 
        print(vehiculo.mover()) 

# Usamos herencia y polimorfismo 
mi_coche = Coche() 
mi_avion = Avion() 
realizar_movimiento(mi_coche) # El coche se mueve por carretera. 
realizar_movimiento(mi_avion) # El avión vuela por el aire. 
#En este ejemplo, Coche y Avion heredan de Vehiculo y sobrescriben el método mover. La función realizar_movimiento es capaz de invocar el método mover de cualquier tipo de Vehiculo, demostrando cómo la herencia y el polimorfismo trabajan juntos.









"""Conceptos Relacionados con la Herencia:"""

"""1. Subclase (Clase Derivada)
Es una clase que hereda atributos y métodos de una clase base (superclase) y puede agregar o modificar funcionalidad.

3. Superclase (Clase Base)
Es una clase que es heredada por otras clases. Proporciona atributos y métodos que pueden ser reutilizados por las subclases.

4. Sobrescritura de Métodos (Method Overriding)
Cuando una subclase redefine un método de la superclase para proporcionar una implementación más específica. Esto permite modificar el comportamiento heredado.

5. Constructor y super()
El constructor de la clase se usa para inicializar los objetos, y super() se utiliza para llamar al constructor de la clase base desde una subclase.

6. Herencia Múltiple
Cuando una clase hereda de más de una clase base. Esto puede ser útil en algunos casos, pero puede introducir complejidad y problemas, como el "diamante de herencia", por lo que debe usarse con cautela.

7. Encapsulamiento y Herencia
El encapsulamiento permite ocultar la implementación de los detalles de la clase. Al usar herencia, las subclases pueden acceder a los métodos públicos y protegidos de las superclases, pero no a los privados.

8. Visibilidad de los Miembros
Los miembros de una clase (atributos y métodos) pueden tener diferentes niveles de acceso: public, protected y private, lo que afecta cómo las subclases pueden interactuar con ellos.

9. Composición vs. Herencia
La composición es un enfoque alternativo a la herencia, donde un objeto contiene instancias de otros objetos para reutilizar funcionalidad en lugar de heredarla. La composición es más flexible y generalmente preferida sobre la herencia en muchas situaciones."""

"""Conceptos Relacionados con el Polimorfismo:"""

"""1. Sobrecarga de Métodos (Method Overloading)
Es la capacidad de definir varios métodos con el mismo nombre pero con diferentes parámetros. A diferencia de la sobrescritura, la sobrecarga ocurre en la misma clase.

3. Polimorfismo de Tiempo de Ejecución (Polimorfismo Dinámico)
Es el tipo de polimorfismo que ocurre cuando un método se resuelve en tiempo de ejecución. Depende de la sobrescritura de métodos en las subclases. El tipo real de objeto determina qué método se ejecuta.

4. Polimorfismo de Tiempo de Compilación (Polimorfismo Estático)
Es el polimorfismo que ocurre en tiempo de compilación y se logra a través de la sobrecarga de métodos o de operadores. En este caso, el compilador determina qué versión del método se ejecutará según el número o tipo de parámetros.

5. Métodos Virtuales
Son métodos definidos en una clase base que pueden ser sobrescritos por las subclases. Esto habilita el polimorfismo de tiempo de ejecución.

6. Enlace Dinámico (Binding)
Es el proceso de vincular un método a una llamada de función en tiempo de ejecución. Es una característica clave del polimorfismo de tiempo de ejecución.

7. Referencias de Clase Base
El polimorfismo se aprovecha cuando una variable de una clase base puede referirse a un objeto de una clase derivada, permitiendo invocar métodos sobrescritos sin conocer el tipo concreto de la subclase.

8. Patrón de Diseño Strategy
Este patrón permite definir una familia de algoritmos y hacerlos intercambiables. Utiliza polimorfismo para cambiar el comportamiento de un objeto de forma flexible en tiempo de ejecución.

9. Delegación
En lugar de heredar directamente de una clase base, una clase puede delegar responsabilidades a otras clases, lo que fomenta la reutilización sin necesidad de herencia.

10. Polimorfismo Paramétrico
Es un tipo de polimorfismo que permite escribir código genérico que funcione con cualquier tipo de dato. En Python, esto puede lograrse mediante tipos dinámicos y funciones que aceptan cualquier tipo de argumento."""






"""Buenas Prácticas en Herencia:"""

"""1. Preferir la Composición sobre la Herencia
Composición es más flexible y permite mayor control sobre las interacciones entre clases. Usar composición en lugar de herencia puede evitar jerarquías demasiado complejas que son difíciles de mantener. Ejemplo: En lugar de tener una jerarquía Coche -> Vehiculo -> Motor, podrías componer un Coche con un Motor como atributo.

2. Usar la Herencia Solo cuando Haya una Relación de Tipo
La herencia debe usarse solo cuando exista una relación lógica de "es un tipo de". Si la relación no es clara, es mejor usar composición. 
Ejemplo correcto: Perro hereda de Animal porque un perro es un tipo de animal.
Ejemplo incorrecto: Si tienes Coche heredando de Motor, la relación no es de "es un tipo de", y sería más apropiado usar composición.

3. Evitar Herencia Múltiple
La herencia múltiple puede ser confusa y propensa a errores, especialmente cuando no se sabe cuál de las superclases debería implementar un método. Si es necesario, usa interfaces o protocolos (si el lenguaje lo permite). En Python, puedes usar el método de resolución de órdenes (MRO) para manejar la herencia múltiple, pero es mejor evitarla en la medida de lo posible.

4. Evitar Sobreescribir Métodos sin Necesidad
No sobrescribas métodos de la clase base si no es estrictamente necesario. Sobreescribir métodos debe ser una decisión consciente para extender o modificar un comportamiento. Ejemplo: Si Vehiculo tiene un método mover(), no lo sobrescribas en Coche a menos que el comportamiento del movimiento de un coche sea realmente diferente al de la superclase Vehiculo.

5. Usar super() para Acceder a Métodos de la Superclase
Al sobrescribir un método en una subclase, usa super() para llamar al método de la superclase y asegurarte de que su funcionalidad se conserve (si es necesario). Esto ayuda a mantener la consistencia entre las clases base y derivadas.
Ejemplo: """
class Animal: 
    def hablar(self): 
        return "Hace un sonido" 

class Perro(Animal): 
    def hablar(self): 
        mensaje_base = super().hablar() 
        return f"{mensaje_base}, pero también ladra" 

"""6. Limitar la Profundidad de la Herencia
Mantén las jerarquías de herencia lo más planas posible. Cuanto más profunda sea la jerarquía, más difícil será entender y mantener el código. La profundidad excesiva puede llevar a una alta dependencia entre clases. 
Mejor práctica: Utiliza composición y agregación para evitar una jerarquía profunda."""

"""Buenas Prácticas en Polimorfismo:"""

"""1. Definir Métodos Abstratos en la Superclase (cuando sea necesario)
Usa clases abstractas y métodos abstractos cuando quieras garantizar que todas las subclases implementen un comportamiento específico. Esto asegura que el polimorfismo sea efectivo y que las subclases no omitan funcionalidades importantes. Ejemplo: """
from abc import ABC, abstractmethod 
class Animal(ABC): 
    @abstractmethod     
    def hablar(self): 
        pass 

class Perro(Animal): 
    def hablar(self): 
        return "Ladra" 

class Gato(Animal): 
    def hablar(self): 
        return "Mia" 

"""2. Sobrescribir Métodos Solo si Es Necesario
Solo sobrescribe métodos en una subclase cuando sea necesario cambiar el comportamiento de la clase base. Si no es necesario, es mejor dejar que la clase base maneje el comportamiento. Ejemplo: Si tienes un método dibujar() en una clase Figura, no es necesario sobrescribirlo en subclases si no cambia su funcionalidad.

3. Implementar el Polimorfismo de Forma Consistente
Asegúrate de que las subclases implementen consistentemente los métodos de la superclase o de las interfaces, ya que el polimorfismo depende de que estos métodos se comporten de manera coherente. Si una clase base define un método como mover(), las subclases deben implementarlo, de lo contrario, el polimorfismo no funcionará correctamente.

4. Evitar Excesiva Sobrecarga de Métodos
En algunos lenguajes, puedes realizar sobrecarga de métodos, donde el mismo nombre de método puede aceptar diferentes parámetros. Sin embargo, este patrón debe usarse con moderación, ya que puede llevar a confusión. En su lugar, considera usar argumentos opcionales o patrones de diseño como Strategy o Factory.

5. Usar Polimorfismo con Interfaces y Clases Abstractas
Cuando sea apropiado, define un contrato común utilizando interfaces o clases abstractas para que las subclases tengan que seguir un conjunto de métodos predefinidos. Esto permite que el polimorfismo sea más robusto y fácil de mantener. Ejemplo: """
class Animal: 
    def hablar(self): 
        pass 

class Perro(Animal): 
    def hablar(self): 
        return "Ladra" 

class Gato(Animal): 
    def hablar(self): 
        return "Mia" 

    def hacer_sonar(animal: Animal): 
        print(animal.hablar()) 

perro = Perro() 
gato = Gato() 

hacer_sonar(perro) # Ladra 
hacer_sonar(gato) # Mia 

"""6. Evitar el Polimorfismo Abusivo
Aunque el polimorfismo puede hacer que tu código sea más flexible, no lo uses en exceso. A veces puede hacer que el código sea difícil de entender si no está bien documentado o si el comportamiento de los métodos cambia inesperadamente. En lugar de abusar del polimorfismo, considera alternativas como el patrón Strategy, que permite variar el comportamiento sin recurrir a un gran número de clases."""



"""Técnicas para Herencia:"""

"""1. Uso de Herencia para Reutilización de Código
La herencia permite a las subclases reutilizar el código de la superclase. Aprovecha la herencia para evitar la duplicación de código común en clases relacionadas. Ejemplo: Si tienes varias clases Perro, Gato y Conejo que comparten métodos comunes como comer(), puedes implementarlo en una clase base Animal.

2. Especialización en Subclases
En lugar de crear grandes jerarquías de clases, especializa las subclases para agregar funcionalidades adicionales. La idea es que las subclases extiendan la funcionalidad de la clase base, pero no modifiquen demasiado su estructura. Ejemplo: Si tienes una clase Empleado, puedes crear subclases como Gerente o Desarrollador que agreguen comportamientos específicos para cada tipo de empleado sin tener que modificar la clase base Empleado.

3. Usar la Herencia para Implementar Patrones de Diseño
La herencia es útil para implementar patrones de diseño como Template Method o Factory Method, donde las clases base definen la estructura de un algoritmo y las subclases implementan detalles específicos. Template Method: La clase base define la estructura general del algoritmo, pero las subclases implementan pasos específicos.

4. Aprovechar las Clases Abstractas para Contratos Comunes
Las clases abstractas definen un conjunto de métodos que las subclases deben implementar, proporcionando un contrato común. Usa este enfoque cuando quieras garantizar que todas las subclases implementen ciertos comportamientos. Ejemplo: Una clase Figura abstracta puede tener un método abstracto calcular_area(), que todas las figuras geométricas deben implementar.

5. Control de Acceso y Encapsulamiento con Herencia
En la herencia, utiliza modificadores de acceso como private, protected, y public para controlar el acceso a los miembros de las clases base y evitar que las subclases accedan a detalles internos que no deberían. Ejemplo: Si tienes una clase Vehiculo, sus detalles internos como el motor (motor) deben ser protected para que las subclases puedan acceder, pero no deberían ser accesibles desde fuera de la jerarquía."""

"""Técnicas para Polimorfismo:"""

"""1. Polimorfismo de Tiempo de Ejecución con Métodos Sobrescritos
Aprovecha el polimorfismo de tiempo de ejecución sobrescribiendo métodos de la clase base en las subclases para modificar el comportamiento. Esto permite que un solo método se comporte de manera diferente según el tipo de objeto que lo invoque. Ejemplo:"""
class Animal: 
    def hablar(self): 
        return "Hace un sonido" 

class Perro(Animal): 
    def hablar(self): 
        return "Ladra" 

class Gato(Animal): 
    def hablar(self): 
        return "Mia" 
    def hacer_sonar(animal: Animal): 
        print(animal.hablar()) 

hacer_sonar(Perro()) # Ladra 
hacer_sonar(Gato()) # Mia 

"""2. Uso de Interfaces o Clases Abstractas para Definir Contratos
Utiliza interfaces o clases abstractas para definir un conjunto de métodos que las subclases deben implementar. Esto promueve un diseño flexible donde el código cliente puede interactuar con diferentes tipos de objetos sin conocer su 

implementación interna. Ejemplo: """
from abc import ABC, abstractmethod 
class Hablador(ABC): 
    @abstractmethod 
    def hablar(self): 
        pass 

class Persona(Hablador): 
    def hablar(self): 
        return "Hola" 

class Perro(Hablador):
    def hablar(self): 
        return "Guau" 

"""3. Implementación de Polimorfismo con Colecciones de Objetos
Puedes almacenar objetos de diferentes clases que comparten una interfaz o clase base en una colección y tratarlos de manera uniforme. Ejemplo:""" 
animales = [Perro(), Gato()] 
for animal in animales: 
    print(animal.hablar()) # Polimorfismo: "Ladra" y "Mia" 

"""4. Uso de Polimorfismo con Patrón de Diseño Strategy
El patrón Strategy utiliza polimorfismo para intercambiar comportamientos de manera dinámica. Se define una interfaz común para diferentes algoritmos o comportamientos, lo que permite cambiarlos de manera flexible sin modificar el código cliente. Ejemplo:"""
class EstrategiaPago: 
    def pagar(self): 
        pass 

class PagoTarjeta(EstrategiaPago): 
    def pagar(self): 
        return "Pago con tarjeta" 

class PagoPaypal(EstrategiaPago): 
    def pagar(self): 
        return "Pago con PayPal" 

class Cliente: 
    def __init__(self, metodo_pago: EstrategiaPago): 
        self.metodo_pago = metodo_pago 

    def pagar(self): 
        print(self.metodo_pago.pagar()) 

cliente1 = Cliente(PagoTarjeta()) 
cliente1.pagar() # Pago con tarjeta 
cliente2 = Cliente(PagoPaypal()) 
cliente2.pagar() # Pago con PayPal 

"""5. Polimorfismo con Delegación
Delegación permite que un objeto delegue la ejecución de ciertas tareas a otros objetos. Este enfoque se usa cuando una clase no quiere heredar comportamientos, pero necesita compartirlos a través de objetos colaboradores. Ejemplo: Una clase Coche puede delegar la tarea de manejar el motor a una clase Motor.

6. Uso de Métodos Genericos para Polimorfismo Paramétrico
El polimorfismo paramétrico permite escribir métodos que operan con cualquier tipo de dato sin tener que especificar el tipo exacto, lo que facilita la creación de funciones y clases genéricas. Este enfoque es común en lenguajes con soporte para generics (como Java o C#), y también puede aplicarse en Python utilizando tipos dinámicos. Ejemplo: """

def imprimir_lista(elementos: list): 
    for elemento in elementos:
        print(elemento) 

imprimir_lista([1, 2, 3]) # Funciona con enteros imprimir_lista(["a", "b", "c"]) # Funciona con cadenas 

