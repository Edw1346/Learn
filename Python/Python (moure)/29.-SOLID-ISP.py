"""Principio de Segregación de Interfaces (ISP) - SOLID"""

"""El Principio de Segregación de Interfaces (ISP) establece que una clase no debería ser forzada a depender de interfaces que no utiliza. En otras palabras, es preferible tener muchas interfaces específicas y pequeñas en lugar de una interfaz grande y general. Este principio es crucial para mantener un diseño limpio, flexible y fácil de mantener.

Interfaces específicas: En lugar de crear una interfaz que tenga múltiples responsabilidades y que todas las clases deban implementar (aunque solo necesiten una pequeña parte de la funcionalidad), debemos crear interfaces más pequeñas, cada una enfocada en una tarea específica.

Evitar "interfaces gordas": Cuando una clase implementa una interfaz, debe usar toda la funcionalidad que esa interfaz ofrece. Si la interfaz es demasiado grande o contiene métodos que no son útiles para ciertas clases, esas clases deberían implementarlas solo si realmente las necesitan. De lo contrario, es mejor dividir la interfaz en varias más pequeñas y específicas.

Flexibilidad: La segregación de interfaces aumenta la flexibilidad y hace que el sistema sea más fácil de modificar y extender sin afectar a las clases que ya implementan las interfaces. Si tienes una interfaz grande, cualquier cambio puede afectar a muchas clases; sin embargo, al tener interfaces más específicas, solo las clases que realmente necesitan ese cambio se verán afectadas."""

#Ejemplo en Python:
# Interfaces más pequeñas y específicas: 
class Printable: 
    def print(self): 
        pass 

class Scannable: 
    def scan(self): 
        pass     

class Faxable: 
    def fax(self): 
        pass # Clases específicas que implementan solo lo que necesitan: 

class Printer(Printable): 
    def print(self): 
        print("Printing...") 

class Scanner(Scannable): 
    def scan(self): 
        print("Scanning...") 

class MultiFunctionPrinter(Printable, Scannable, Faxable):
    def print(self): 
        print("Printing...") 

    def scan(self): 
        print("Scanning...") 

    def fax(self): 
        print("Faxing...") # Usando las clases: 

printer = Printer() 
printer.print() 
scanner = Scanner() 
scanner.scan() 
multi_function = MultiFunctionPrinter() 
multi_function.print() 
multi_function.scan() 
multi_function.fax() 

"""En este ejemplo:
Printer solo implementa Printable porque no necesita otras funcionalidades.
MultiFunctionPrinter implementa las tres interfaces (Printable, Scannable, y Faxable) porque es un dispositivo multifuncional que necesita todas esas capacidades.
Si alguna clase no necesita una funcionalidad, simplemente no implementa la interfaz correspondiente, evitando el "forzar" la implementación de métodos innecesarios."""


"""Técnicas para aplicar ISP:
Identificación de responsabilidades: Antes de diseñar una interfaz, asegúrate de que sea específica para un conjunto limitado de responsabilidades. Piensa en lo que debe hacer la clase en lugar de mezclar funcionalidades diferentes.

Diseño orientado a clientes: Si una interfaz es demasiado grande, observa cómo las clases consumidoras de esa interfaz están interactuando con ella. Divídelas de acuerdo con sus necesidades.

Revisión constante: A medida que el sistema crece, revisa las interfaces regularmente. Si descubres que una interfaz está siendo usada por clases no relacionadas, puede ser hora de refactorizarla en varias interfaces más pequeñas.

Evita interfaces grandes: Mantén las interfaces pequeñas y centradas en una sola responsabilidad. Si te encuentras con una interfaz que parece estar cubriendo varias responsabilidades, sepárala en múltiples interfaces más simples.

Documentación clara: Asegúrate de documentar bien las interfaces y las clases que las implementan, para que quede claro qué funcionalidades se esperan de cada clase."""




"""Conceptos relacionados con el Principio de Segregación de Interfaces (ISP) """

"""1. Acoplamiento Bajo (Low Coupling)
El acoplamiento bajo es una característica de diseño que promueve la independencia entre clases. Cuanto menos dependen las clases entre sí, más fácil es mantener, entender y modificar el sistema.
Relación con ISP: ISP reduce el acoplamiento al asegurar que las clases solo dependen de los métodos que realmente utilizan de las interfaces. Esto evita la creación de dependencias innecesarias.

2. Cohesión Alta (High Cohesion)
La cohesión alta significa que los elementos dentro de una clase o módulo están fuertemente relacionados y trabajan juntos para lograr una única tarea. En el contexto de las interfaces, las interfaces cohesionadas contienen solo los métodos que están íntimamente relacionados entre sí.
Relación con ISP: Al dividir interfaces grandes en interfaces más pequeñas, se aumenta la cohesión de esas interfaces, ya que cada una de ellas se especializa en un conjunto concreto de funcionalidades.

3. Interfaz de Cliente (Client Interface)
Una interfaz de cliente define los métodos que los consumidores de la clase deben utilizar. A menudo, se habla de la creación de interfaces desde el punto de vista de lo que el cliente necesita de esa clase.
Relación con ISP: ISP sugiere que las interfaces deben diseñarse en función de las necesidades de los clientes, para que no tengan que implementar métodos que no utilizarán.

4. Patrón de Diseño: Adapter
El patrón Adapter permite que una interfaz existente sea utilizada por otras clases sin modificar la clase original.
Relación con ISP: Si una interfaz es demasiado grande o inadecuada para ciertas clases, puedes usar un adaptador para hacer que las clases trabajen con una versión más pequeña y apropiada de la interfaz.

5. Patrón de Diseño: Façade
El patrón Facade proporciona una interfaz simplificada a un conjunto complejo de interfaces en un subsistema.
Relación con ISP: Un fachada puede ser utilizada para proporcionar un acceso más específico y adecuado a ciertas funcionalidades, ayudando a cumplir con ISP al ofrecer interfaces que solo incluyen lo necesario.
"""





"""Prácticas para aplicar el Principio de Segregación de Interfaces (ISP):"""

"""1. Divide interfaces grandes en interfaces más pequeñas
Descripción: Si tienes una interfaz que tiene demasiados métodos y cubre demasiadas responsabilidades, sepárala en interfaces más pequeñas y específicas. Esto evita que las clases implementen métodos que no necesitan. Ejemplo: Si tienes una interfaz MultifunctionDevice con métodos como print(), scan(), fax(), sepárala en tres interfaces diferentes: Printable, Scannable, y Faxable. De esta manera, las clases solo implementan las interfaces que realmente necesitan.

2. Haz que las interfaces sean específicas y enfocadas
Descripción: Define interfaces que representen un conjunto reducido de operaciones que están fuertemente relacionadas entre sí. No sobrecargues una sola interfaz con funcionalidades que no estén directamente relacionadas. Ejemplo: Si una clase Empleado tiene una interfaz ComportamientoTrabajo con métodos como trabajar(), descansar(), celebrar(), separa las responsabilidades. Crea una interfaz Trabajador con trabajar() y otra Recreativo con celebrar() si esas responsabilidades no siempre coinciden en las mismas clases.

3. Usa interfaces para definir contratos claros
Descripción: Una interfaz debe ser un contrato claro que indique las operaciones que una clase necesita implementar. Asegúrate de que las interfaces representen las capacidades que las clases están dispuestas a proporcionar y no imposiciones que no utilizan. Ejemplo: Si una clase CuentaBancaria solo necesita realizar operaciones de depositar() y consultarSaldo(), pero implementa una interfaz TransaccionesBancarias que incluye métodos como transferir(), consultarHistorial(), etc., deberías separar estas funcionalidades en interfaces más especializadas.

4. Evita interfaces con muchos métodos opcionales
Descripción: Las interfaces no deben tener métodos opcionales (es decir, métodos que no todas las clases deberían implementar). Si una clase no necesita ciertos métodos, esa interfaz probablemente debe ser dividida. Ejemplo: Si tienes una interfaz Dispositivo con métodos como encender(), apagar(), cargar(), enviarMensaje(), y no todos los dispositivos requieren enviarMensaje(), entonces deberías crear una interfaz Mensajeable que sea implementada solo por dispositivos que necesiten ese método.

5. Implementa las interfaces de acuerdo con las necesidades del cliente
Descripción: Cuando diseñes interfaces, siempre piensa en cómo las clases consumidoras las usarán. Si no necesitan toda la funcionalidad, no las hagas implementar todo. Crea interfaces orientadas a los clientes. Ejemplo: Si una aplicación de ventas tiene un sistema de pagos, crea interfaces como Pagable, DescuentoAplicable y FacturaGenerable en lugar de una sola interfaz SistemaDeVentasCompleto que obligue a implementar todos los métodos relacionados con pagos, descuentos, y facturación.

6. Refactoriza cuando una clase implementa métodos innecesarios
Descripción: Si una clase implementa métodos que no necesita (es decir, métodos de una interfaz que no utiliza), es el momento de refactorizar. La refactorización puede implicar separar la interfaz en componentes más pequeños o hacer que la clase implemente solo las interfaces necesarias. Ejemplo: Si tienes una clase CarroDeCompras que implementa una interfaz Producto que incluye un método agregarDescuento(), pero CarroDeCompras no necesita este método, deberías refactorizar creando una interfaz más pequeña, como ProductoDescontable, y hacer que solo las clases que lo necesiten la implementen.

7. Usa el principio de Inversión de Dependencias
Descripción: Asegúrate de que las clases de alto nivel no dependan de detalles de implementación de clases de bajo nivel. Las interfaces pequeñas pueden ayudar a desacoplar el código. Ejemplo: Si una clase CajeroAutomático necesita acceder a una clase CuentaBancaria, usa una interfaz como CuentaBancariaInterface en lugar de que CajeroAutomático dependa directamente de la clase concreta CuentaBancaria. Esto facilita la extensión y el mantenimiento del sistema.

8. Define interfaces orientadas a la acción, no a la estructura
Descripción: Las interfaces deben definirse por lo que hacen las clases, no por cómo están estructuradas. Así las clases pueden implementar la interfaz sin necesidad de tener una estructura común. Ejemplo: En lugar de crear una interfaz Empleado con métodos como nombre(), edad(), direccion(), crea una interfaz Trabajable con un método trabajar(), para que cualquier clase que tenga esa responsabilidad pueda implementarla, independientemente de su estructura interna.

9. Prioriza la reutilización sobre la generalización excesiva
Descripción: En lugar de crear una interfaz genérica que cubra todos los casos posibles, crea interfaces que representen acciones que puedan ser reutilizadas y extendidas de manera flexible. Ejemplo: Si tienes una interfaz Usuario con métodos como registrar(), loguear(), editarPerfil(), pero algunas clases como Administrador y Cliente solo necesitan una parte de estas funcionalidades, divídelas en interfaces como Registrable, Logueable, y EditablePerfil, de forma que cada clase implemente solo lo que necesita.

10. Aprovecha los patrones de diseño adecuados
Descripción: Los patrones de diseño como el Adapter, Façade, o Proxy pueden ayudarte a aplicar ISP de manera más efectiva, ya que permiten que las clases se adapten a interfaces pequeñas sin modificar su comportamiento interno. Ejemplo: Si tienes una interfaz Dispositivo muy compleja y necesitas usarla en una clase Smartphone, puedes usar un Adaptador para proporcionar solo los métodos que el Smartphone necesita sin tener que implementar la interfaz completa."""




"""Técnicas para aplicar el Principio de Segregación de Interfaces (ISP) de manera eficiente en el diseño de software:"""

"""1. Uso de Interfaces Específicas y Especializadas
Técnica: En lugar de crear interfaces amplias que incluyen muchos métodos, crea interfaces más pequeñas y especializadas para grupos de métodos relacionados. Esto permite que las clases implementen solo las interfaces que necesitan. Ejemplo: Si tienes una clase Empleado y una interfaz Funcionario que incluye métodos como trabajar(), 

descansar(), reporte(), en lugar de tener una única interfaz Funcionario, puedes crear interfaces especializadas como Trabajador, Jefe, Reportador y hacer que cada clase implemente solo las que necesita.

2. Implementación de Múltiples Interfaces
Técnica: Permite que las clases implementen varias interfaces pequeñas en lugar de una sola interfaz grande. Esto proporciona flexibilidad y facilita la implementación de solo los métodos relevantes para una clase en particular. Ejemplo: Si tienes una interfaz Vehiculo con métodos como arrancar(), detener(), cargarCombustible(), puedes crear interfaces separadas como Motorizable, Transportable, y Energizable, y permitir que una clase Coche implemente Motorizable y Transportable, mientras que una clase EstaciónDeServicio implemente Energizable.

3. Aplicación de Interfaces con Métodos de Solo Lectura o Solo Escritura
Técnica: Separa las interfaces en aquellas que solo permiten operaciones de lectura (getter) y aquellas que solo permiten operaciones de escritura (setter). Esto puede ayudar a evitar que las clases implementen métodos que no les corresponden. Ejemplo: Si tienes una clase Libro, puedes crear una interfaz Lectura con un método obtenerContenido(), y una interfaz Escritura con un método agregarContenido(). Las clases que solo necesitan leer implementarán Lectura, y aquellas que necesitan escribir implementarán Escritura.

4. Patrón de Diseño de Delegación
Técnica: Usa delegación para mover la responsabilidad de ciertos métodos a otras clases especializadas, en lugar de que la clase principal implemente todos los métodos de una interfaz grande. Esto puede ser útil cuando quieres cumplir con ISP sin llenar una clase de métodos innecesarios. Ejemplo: Si tienes una interfaz Pago con métodos como procesarPago(), verificarPago(), y enviarFactura(), puedes delegar la implementación de verificarPago() y enviarFactura() a clases separadas, dejando que la clase principal solo implemente procesarPago().

5. Uso de Interfaces con Métodos Comunes
Técnica: Cuando tienes múltiples clases que implementan un conjunto similar de métodos pero con ligeras variaciones, crea interfaces con métodos comunes que puedan ser reutilizados por estas clases, evitando duplicación de código. Ejemplo: Si tienes una interfaz Operable con el método operar(), y diversas clases como Robot y Coche que tienen diferentes implementaciones, puedes hacer que ambas clases implementen la interfaz Operable y tengan una implementación específica de operar().

6. Aplicación de Interfaces con Métodos Opcionales
Técnica: Usa interfaces opcionales o técnicas como default methods (en lenguajes como Java) cuando un método no es obligatorio para todas las clases que implementan la interfaz. Esto reduce la necesidad de que las clases implementen métodos que no usan. Ejemplo: En Java, puedes tener una interfaz Notificable con un método enviarNotificacion(). Sin embargo, si no todas las clases necesitan notificar, puedes usar un método por defecto como default void enviarNotificacion() {} para proporcionar una implementación vacía.

7. Estrategia de Interfaces Orientadas a Comportamientos
Técnica: Define interfaces en base a comportamientos específicos en lugar de basarlas en la estructura o clases. Esto permite que las clases implementen interfaces que se alinean mejor con las responsabilidades que tienen. Ejemplo: En lugar de crear una interfaz Vehiculo que combine comportamientos y características de todos los vehículos, crea interfaces como Conducible, Acelerable o Estacionable, que se pueden aplicar a diferentes tipos de vehículos según sus características.

8. Patrón Adapter para Interfaces
Técnica: Si tienes una interfaz grande que no se ajusta a una clase, usa el Patrón Adapter para crear una clase adaptadora que implemente una interfaz más pequeña y adapte la funcionalidad de la clase original para que se ajuste a la interfaz. Ejemplo: Si tienes una clase Vendedor que implementa una interfaz GestorDePedidos con 10 métodos, pero solo necesita 4 de esos métodos, puedes usar un adaptador que implemente una interfaz más pequeña con esos 4 métodos necesarios.

9. Uso de Interfaces Funcionales (para lenguajes que soportan programación funcional)
Técnica: Si trabajas con lenguajes que soportan programación funcional, como Java 8 o Python, puedes definir interfaces funcionales (interfaces con un solo método abstracto) que permiten una mayor flexibilidad en cómo las clases implementan sus comportamientos. Ejemplo: Usar una interfaz funcional OperadorMatematico con el método operar() y luego permitir que varias clases implementen la lógica específica, como Sumador, Restador, etc., de forma modular.

10. Uso de Principios de Inyección de Dependencias
Técnica: Aplica la inyección de dependencias para que las clases dependan de interfaces pequeñas y no de implementaciones grandes. Esto facilita la reutilización de componentes y cumple con ISP. Ejemplo: Si tienes una clase Coche, inyecta una interfaz como Motor en lugar de depender de una implementación concreta de motor, permitiendo que la clase Coche funcione con diferentes tipos de motores sin tener que modificarla."""



