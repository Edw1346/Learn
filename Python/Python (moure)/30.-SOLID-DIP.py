"""El Principio de Inversión de Dependencias (DIP), sugiere que tanto los módulos de alto nivel (que contienen la lógica principal del negocio) como los de bajo nivel (que se encargan de detalles de implementación como bases de datos, interfaces de usuario, servicios de red) deben depender de abstracciones (interfaces o clases abstractas), no de implementaciones concretas. Esto permite que los módulos de alto nivel no se vean afectados por los cambios en los módulos de bajo nivel, promoviendo así un código más flexible y fácil de mantener."""

"""Ejemplo:
Supongamos que tienes una clase Factura que depende directamente de una clase BaseDeDatos para guardar datos. Si deseas cambiar la forma de almacenamiento de datos (por ejemplo, pasar de una base de datos relacional a una base de datos no relacional), necesitarías modificar la clase Factura, lo cual va en contra del DIP.
Para seguir el DIP, puedes crear una interfaz Almacenamiento que declare un método guardar(), y hacer que tanto la clase BaseDeDatos como otros módulos de bajo nivel implementen esta interfaz. La clase Factura ahora dependerá de la interfaz Almacenamiento, no de una implementación concreta, y se podrá cambiar fácilmente el módulo de almacenamiento sin afectar a la clase Factura."""
from abc import ABC, abstractmethod 
# Abstracción 
class Almacenamiento(ABC): 
    @abstractmethod 
    def guardar(self, datos): 
        pass 

# Módulo de bajo nivel
class BaseDeDatos(Almacenamiento): 
    def guardar(self, datos): 
        print(f"Guardando en la base de datos: {datos}") 

# Módulo de alto nivel 
class Factura:
    def __init__(self, almacenamiento: Almacenamiento):
        self.almacenamiento = almacenamiento 

    def procesar_factura(self, datos):
        self.almacenamiento.guardar(datos) 
        print("Factura procesada.") 

# Uso 
almacenamiento_db = BaseDeDatos() 
factura = Factura(almacenamiento_db) 
factura.procesar_factura("Datos de la factura") 

"""En este ejemplo:
La clase Factura depende de la abstracción Almacenamiento.
La clase BaseDeDatos implementa Almacenamiento, pero si más adelante decides cambiar la implementación para almacenar los datos en un archivo en lugar de una base de datos, solo necesitarás crear una nueva clase que implemente Almacenamiento y la clase Factura seguirá funcionando sin necesidad de cambios."""

"""Conceptos Relacionados con el DIP:
Abstracciones vs. Detalles: Los detalles de implementación deben estar separados de la lógica del negocio. Las clases de 

alto nivel deben utilizar interfaces o clases abstractas, y no deben conocer los detalles específicos de las implementaciones.

Interfaces/Clases Abstractas: Las interfaces y clases abstractas son herramientas clave para aplicar el DIP, ya que proporcionan un punto de conexión entre los módulos de alto y bajo nivel sin acoplar directamente sus implementaciones.

Inyección de Dependencias (DI): Este es un patrón de diseño que facilita la implementación del DIP. Consiste en proporcionar las dependencias de una clase (por ejemplo, BaseDeDatos en el ejemplo anterior) desde el exterior, ya sea a través de constructor, método o propiedad. Esto promueve un código más modular y facilita la prueba.

Inversiones de Control (IoC): El DIP es un tipo de Inversión de Control, en la que el control de la creación de objetos y la gestión de las dependencias se delega a un contenedor o framework, en lugar de que las clases de alto nivel creen y gestionen sus propias dependencias."""

"""Prácticas para Aplicar el DIP:
Definir Interfaces Claras: Siempre que sea posible, define interfaces claras para cada módulo de bajo nivel que pueda ser sustituido por otras implementaciones.
Uso de Inyección de Dependencias: Siempre que se requiera una dependencia, inyectala desde el exterior de la clase a través de su constructor, en lugar de crearla directamente dentro de la clase.
Evitar el Acoplamiento Fuerte: No permitas que las clases de alto nivel dependan directamente de implementaciones específicas de clases de bajo nivel. Utiliza abstracciones siempre que puedas.
Utilizar un Contenedor de Dependencias: Si tu aplicación crece en complejidad, considera usar un contenedor de dependencias para gestionar la creación y gestión de objetos. Esto te ayudará a aplicar el DIP de forma automática."""

"""Técnicas para Aplicar el DIP:
Patrón de Diseño de Estrategia: Usa este patrón para permitir que una clase de alto nivel cambie su comportamiento dependiendo de la implementación de la interfaz que se le pase.
Patrón de Diseño de Fábrica: Si el detalle de las dependencias es muy complejo, usa el patrón de diseño de fábrica para centralizar la creación de las dependencias y simplificar la aplicación del DIP.
Uso de Frameworks de Inyección de Dependencias: Si trabajas con frameworks como Spring (Java) o Django (Python), puedes aprovechar la funcionalidad integrada de inyección de dependencias para cumplir automáticamente con el DIP.
Mocking y Pruebas Unitarias: Utiliza mocks y stubs para simular implementaciones de bajo nivel en pruebas unitarias, evitando la necesidad de instanciar implementaciones concretas."""


"""1. Contenedores de Inyección de Dependencias

Definición: Son herramientas o frameworks que gestionan automáticamente la creación y el ciclo de vida de las dependencias en una aplicación.
Relación con DIP: Facilitan la implementación del DIP gestionando la creación de instancias y la inyección de dependencias. Ejemplo: Frameworks como Spring en Java o Django en Python proveen contenedores para gestionar las dependencias.

2. Patrón de Diseño de Fábrica
Definición: Es un patrón que permite crear objetos sin especificar la clase exacta que se va a instanciar. La creación de objetos se delega a una fábrica.

Relación con DIP: La fábrica puede ser utilizada para crear objetos concretos que implementen una interfaz o clase abstracta, garantizando que los módulos de alto nivel sigan dependiendo de abstracciones. Ejemplo: Una Fábrica de Almacenamiento que crea instancias de BaseDeDatos o Archivo según se necesite, sin que la clase Factura dependa de la implementación concreta.

8. Inversión de Control (IoC)
Definición: Se refiere a la transferencia de la gestión de objetos o servicios del código de aplicación al framework o contenedor. Es una técnica donde el flujo de control de la aplicación es invertido.

Relación con DIP: La Inversión de Control es una técnica que implementa el DIP al delegar la responsabilidad de gestionar las dependencias a un contenedor o framework, en lugar de que las clases de alto nivel gestionen directamente sus 

dependencias. Ejemplo: Un framework como Spring o Django gestiona las dependencias y las inyecta en las clases de alto nivel automáticamente.

10. Patrón de Diseño de Estrategia
Definición: Este patrón permite que un objeto cambie su comportamiento en tiempo de ejecución al delegar el comportamiento a un objeto de la estrategia.

Relación con DIP: La estrategia se basa en el uso de abstracciones para cambiar el comportamiento de una clase sin modificar su código. El DIP facilita este patrón, permitiendo que una clase de alto nivel dependa de diferentes estrategias implementadas a través de interfaces. Ejemplo: Un sistema de pago que pueda cambiar entre diferentes estrategias de pago (tarjeta, PayPal, etc.) sin modificar la lógica de procesamiento de pagos, ya que cada estrategia implementa la interfaz común MetodoDePago."""




"""Prácticas recomendadas """

"""1. Utilizar Interfaces y Clases Abstratas para las Dependencias
Descripción: Las clases de alto nivel no deben depender de clases concretas, sino de abstracciones (interfaces o clases abstractas).
Práctica: Define interfaces para los módulos de bajo nivel, y haz que las clases de alto nivel dependan de estas interfaces, en lugar de depender de implementaciones concretas. Ejemplo: """
class Almacenamiento: 
    def guardar(self, datos): 
        pass 

class BaseDeDatos(Almacenamiento): 
    def guardar(self, datos): 
        print("Guardando en la base de datos") 

class Factura: 
    def __init__(self, almacenamiento: Almacenamiento): 
        self.almacenamiento = almacenamiento 

    def procesar(self): 
        self.almacenamiento.guardar("Datos de factura") 

"""2. Inyección de Dependencias
Descripción: Asegúrate de que las dependencias se inyecten desde el exterior en lugar de ser creadas dentro de las clases. Esto puede hacerse a través del constructor, métodos o propiedades.
Práctica: Usa un contenedor de dependencias o un patrón de diseño como Inyección de Dependencias (DI) para proporcionar las dependencias de forma que no sea necesario acoplar las clases de alto nivel con las clases de bajo nivel. Ejemplo: # Inyección de dependencias por constructor """
factura = Factura(BaseDeDatos()) 
factura.procesar() 

"""3. Uso de Fábricas para Crear Objetos
Descripción: Utiliza el patrón Fábrica para crear objetos sin que las clases de alto nivel dependan de las clases concretas.
Práctica: Delega la creación de las instancias a una fábrica que pueda decidir qué tipo de implementación usar según sea necesario. Ejemplo: """
class AlmacenamientoFactory: 
    @staticmethod 
    def crear(tipo): 
        if tipo == "base_datos":
            return BaseDeDatos() 
        elif tipo == "archivo": 
            return Archivo() 

almacenamiento = AlmacenamientoFactory.crear("base_datos") 
factura = Factura(almacenamiento) 
factura.procesar() 

"""4. Implementar Interfaces para Cambiar Comportamientos
Descripción: Cambiar comportamientos en tiempo de ejecución utilizando estrategias que implementen las interfaces. Así, la clase de alto nivel no dependerá de implementaciones específicas.
Práctica: Define diferentes estrategias o comportamientos que pueden ser inyectados según las necesidades sin modificar la clase que los usa. Ejemplo: """
class MetodoPago: 
    def procesar_pago(self, cantidad): 
        pass 

class TarjetaCredito(MetodoPago):
    def procesar_pago(self, cantidad): 
        print(f"Procesando pago de {cantidad} con tarjeta de crédito") 

class PayPal(MetodoPago): 
    def procesar_pago(self, cantidad): 
        print(f"Procesando pago de {cantidad} con PayPal") 

class Factura: 
    def __init__(self, metodo_pago: MetodoPago):
        self.metodo_pago = metodo_pago 
        
        def realizar_pago(self, cantidad): 
            self.metodo_pago.procesar_pago(cantidad) # Se inyecta la estrategia según sea necesario 

factura = Factura(TarjetaCredito())
factura.realizar_pago(100) 

"""5. Preferir la Composición sobre la Herencia
Descripción: En lugar de heredar de clases concretas, usa la composición para delegar comportamientos, lo cual facilita la flexibilidad y mantenibilidad.

Práctica: Utiliza interfaces y clases abstractas para definir roles o comportamientos, y luego compón esos roles en lugar de crear jerarquías complejas de herencia. Ejemplo: """
class Almacenamiento: 
    def guardar(self, datos): 
        pass 

class BaseDeDatos(Almacenamiento): 
    def guardar(self, datos): 
        print("Guardando en base de datos") 

class Factura: 
    def __init__(self, almacenamiento: Almacenamiento): 
        self.almacenamiento = almacenamiento 

    def procesar(self): 
        self.almacenamiento.guardar("Datos de factura") # Composición en lugar de herencia 

factura = Factura(BaseDeDatos()) 
factura.procesar() 

"""6. Evitar Dependencias Directas entre Componentes de Alto y Bajo Nivel
Descripción: Asegúrate de que los módulos de alto nivel no dependan directamente de los de bajo nivel. Ambos deben depender de abstracciones, lo que favorece la flexibilidad del sistema.
Práctica: Utiliza interfaces o clases abstractas para reducir la dependencia entre los módulos. Ejemplo: """
class Envio:
    def realizar_envio(self, paquete): 
        pass 


class EnvioPorCorreo(Envio): 
    def realizar_envio(self, paquete):
        print("Enviando por correo") 

class EnvioPorMensajero(Envio): 
    def realizar_envio(self, paquete): 
        print("Enviando por mensajero") 

class Paquete: 
    def __init__(self, envio: Envio): 
        self.envio = envio 

    def enviar(self): 
        self.envio.realizar_envio(self) # Dependiendo de la estrategia de envío, sin modificar la clase Paquete

paquete = Paquete(EnvioPorCorreo()) 
paquete.enviar() 

"""7. Pruebas Unitarias con Mocking
Descripción: En las pruebas unitarias, utiliza mocking para sustituir las dependencias reales por objetos simulados (mocks). Esto te permitirá probar el comportamiento de las clases de alto nivel sin depender de las clases de bajo nivel concretas.

Práctica: Usa herramientas como unittest.mock para simular las dependencias y aislar el comportamiento que estás probando. Ejemplo: """
from unittest.mock import MagicMock 
# Crear un mock de la clase de bajo nivel 
mock_almacenamiento = MagicMock() 
mock_almacenamiento.guardar.return_value = "Guardado correctamente" 
# Inyecta el mock en la clase de alto nivel 
factura = Factura(mock_almacenamiento) 
factura.procesar() 





"""Técnicas """

"""1. Uso de Interfaces para Abstracciones
Técnica: En lugar de depender de clases concretas, define interfaces o clases abstractas que sirvan como puntos de conexión entre los módulos de alto y bajo nivel. Esto asegura que las clases de alto nivel no estén directamente acopladas a implementaciones específicas: Permite que las implementaciones cambien sin afectar a las clases que las usan.

2. Inyección de Dependencias
Técnica: Utiliza un patrón de inyección de dependencias para pasar las dependencias necesarias a través del constructor, métodos o propiedades, en lugar de que una clase las cree directamente.
Beneficio: Facilita la reutilización de código, pruebas unitarias y facilita el cambio de implementaciones de dependencias sin modificar la clase que las utiliza.

3. Uso de Fábricas para la Creación de Objetos
Técnica: Implementa un patrón de fábrica para la creación de instancias de objetos. Esto permite que las clases de alto nivel no dependan de clases concretas al instanciar dependencias, delegando la responsabilidad a un objeto de fábrica.
Beneficio: Desacopla la creación de objetos de la lógica del negocio y facilita la modificación de las implementaciones sin alterar el código cliente. Ejemplo:"""
class AlmacenamientoFactory:
    @staticmethod 
    def crear(tipo): 
        if tipo == "base_datos": 
            return BaseDeDatos()
        elif tipo == "archivo":
            return Archivo() # ...otros tipos de almacenamiento
# Usando la fábrica para crear dependencias

almacenamiento = AlmacenamientoFactory.crear("base_datos")
factura = Factura(almacenamiento) 
factura.procesar() 

"""4. Uso de Inversión de Control (IoC) con Contenedores de Dependencias
Técnica: Aplica Inversión de Control (IoC) mediante un contenedor de dependencias, el cual gestiona las dependencias entre los objetos. El contenedor decide cómo y cuándo se crean las dependencias y las inyecta en las clases correspondientes. Beneficio: Mejora la flexibilidad y escalabilidad del sistema al centralizar la gestión de dependencias y reducir el acoplamiento. Ejemplo: """
# En lugar de crear el objeto manualmente, un contenedor de dependencias lo gestiona 
class Container: 
    def __init__(self): 
        self.registros = {} 

    def registrar(self, nombre, clase): 
        self.registros[nombre] = clase 

    def obtener(self, nombre):
        return self.registros[nombre]()

container = Container()
container.registrar("factura", Factura) 
factura = container.obtener("factura") 

"""5. Composición sobre Herencia
Técnica: Evita la herencia directa y utiliza la composición para inyectar comportamientos en las clases. Componer objetos permite que se reutilicen comportamientos sin introducir dependencias estrictas. Ejemplo: """
class Factura: 
    def __init__(self, metodo_pago): 
        self.metodo_pago = metodo_pago

    def procesar_pago(self, cantidad): 
        self.metodo_pago.procesar_pago(cantidad) 

class TarjetaCredito: 
    def procesar_pago(self, cantidad):
        print(f"Procesando pago de {cantidad} con tarjeta de crédito") 

tarjeta = TarjetaCredito() 
factura = Factura(tarjeta)
factura.procesar_pago(100) 

"""6. Usar Mocks en Pruebas Unitarias
Técnica: En pruebas unitarias, emplea mocks para simular las dependencias de las clases de bajo nivel. Esto facilita las pruebas de las clases de alto nivel sin necesidad de depender de implementaciones reales. Ejemplo:"""
from unittest.mock import MagicMock 
# Crear un mock para la clase de bajo nivel 
mock_almacenamiento = MagicMock() 
mock_almacenamiento.guardar.return_value = "Guardado correctamente" 
factura = Factura(mock_almacenamiento) 
factura.procesar() 

"""7. Diseñar Sistemas Basados en Estrategias
Técnica: Usa el patrón estrategia para definir comportamientos que pueden ser intercambiados dinámicamente. Las 

clases de alto nivel pueden cambiar el comportamiento de bajo nivel sin necesidad de modificar su código. Ejemplo:"""
class MetodoPago: 
    def procesar(self, cantidad):
        pass

class TarjetaCredito(MetodoPago): 
    def procesar(self, cantidad):
        print(f"Pago procesado con tarjeta de crédito: {cantidad}") 

class PayPal(MetodoPago): 
    def procesar(self, cantidad): 
        print(f"Pago procesado con PayPal: {cantidad}") 

class Factura: 
    def __init__(self, metodo_pago: MetodoPago): 
        self.metodo_pago = metodo_pago 

    def procesar_pago(self, cantidad):
        self.metodo_pago.procesar(cantidad) 

factura = Factura(TarjetaCredito())
factura.procesar_pago(50) 