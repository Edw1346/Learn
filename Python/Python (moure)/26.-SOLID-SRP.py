"""SRP (Single Responsibility Principle) o Principio de Responsabilidad Única es el primer principio de los principios SOLID
Una clase debe tener una sola razón para cambiar, lo que significa que debe estar enfocada en una única responsabilidad o función dentro del sistema. En otras palabras, cada clase debe encargarse solo de un aspecto específico de la funcionalidad del sistema.

El principal objetivo del SRP es dividir las responsabilidades de manera que cada clase se encargue únicamente de una cosa, lo que facilita el mantenimiento, las pruebas y la evolución del sistema. Si una clase tiene múltiples responsabilidades, cualquier cambio relacionado con una de esas responsabilidades podría requerir modificaciones en esa clase, lo que aumenta el riesgo de introducir errores en otras partes del sistema.

Ejemplo malo (sin SRP)
Supongamos que estamos desarrollando un sistema de gestión de empleados, y tenemos una clase Empleado que tiene múltiples responsabilidades, como el almacenamiento de los datos del empleado y la gestión de la impresión de reportes."""
class Empleado: 
    def __init__(self, nombre, salario):
        self.nombre = nombre 
        self.salario = salario 

    def calcular_salario(self):
        return self.salario 

    def generar_reporte(self):
        return f"Empleado: {self.nombre}, Salario: {self.salario}" 

"""Problemas:
La clase Empleado tiene dos responsabilidades: gestionar los datos del empleado (nombre, salario) y generar reportes.
Si se necesita cambiar la lógica de generación de reportes (por ejemplo, modificar el formato o añadir funcionalidades de exportación), sería necesario modificar la clase Empleado, lo cual es un cambio en su responsabilidad. Esto puede afectar otros aspectos del sistema relacionados con la gestión de empleados."""

"""Refactorización (con SRP)
Siguiendo el SRP, podemos dividir las responsabilidades en diferentes clases, donde cada clase tiene una única razón para cambiar."""
class Empleado:
    def __init__(self, nombre, salario): 
        self.nombre = nombre 
        self.salario = salario

    def calcular_salario(self): 
        return self.salario 

class ReporteEmpleado:
    def generar_reporte(self, empleado): 
        return f"Empleado: {empleado.nombre}, Salario: {empleado.salario}" 




"""Prácticas para el SRP"""
"""Dividir las clases por responsabilidades
Si una clase tiene más de una responsabilidad, divídelas en clases separadas. Cada clase debe ser responsable de una única función o aspecto del sistema. Ejemplo: En lugar de tener una clase Empleado que maneje tanto la lógica de negocio como la generación de reportes, se deberían crear clases separadas: Empleado (para la lógica de negocio) y GeneradorDeReportes (para la generación de reportes).

Evitar la sobrecarga de funciones
Si una función hace más de una cosa (por ejemplo, calcular valores y luego formatearlos), considera dividirla en varias funciones más pequeñas. Cada función debe hacer una sola tarea. Ejemplo: En lugar de tener una función que calcule y formatee un informe en el mismo lugar, usa una función para cada tarea: def calcular_salario(empleado): return empleado.salario def formatear_reporte(empleado): return f"Empleado: {empleado.nombre}, Salario: {empleado.salario}" 

Usar servicios externos para responsabilidades adicionales
Si una clase necesita hacer algo fuera de su dominio, como interactuar con una base de datos o enviar un correo electrónico, esa responsabilidad debe ser movida a otra clase especializada (servicio). Ejemplo: Si tu clase Empleado necesita enviar un correo electrónico con su información, esa lógica debería ser manejada por una clase ServicioEmail.

Mantener las clases pequeñas y enfocadas
Asegúrate de que las clases no sean demasiado grandes ni aborden demasiados temas. Si una clase parece contener varias responsabilidades, probablemente sea una señal de que necesita ser refactorizada en varias clases más pequeñas.

Aplicar principios de "alta cohesión"
Relacionado con el SRP, una clase debe ser cohesiva, es decir, todos los métodos y atributos dentro de la clase deben estar estrechamente relacionados con su responsabilidad principal. Si encuentras que un grupo de métodos no están relacionados entre sí, deberías moverlos a otra clase.

Revisar y refactorizar regularmente
En sistemas más grandes, es fácil que las clases se vuelvan demasiado grandes con el tiempo. Revisa regularmente tu código y busca oportunidades para aplicar SRP. Si una clase comienza a asumir responsabilidades adicionales, refactórala para que siga siendo responsable de una sola tarea.

Diseñar con la extensión en mente
Cuando creas una clase, piensa en su evolución a futuro. Si anticipas que la clase podría adquirir más responsabilidades con el tiempo, planea cómo refactorarla para que las nuevas responsabilidades no violen el SRP.

Usar patrones de diseño apropiados
Algunos patrones de diseño, como Factory Method, Strategy, o Observer, pueden ayudar a organizar responsabilidades en clases separadas, ayudando a cumplir con SRP. Estos patrones ayudan a delegar responsabilidades sin añadir demasiado acoplamiento.

Testeo enfocado
Siguiendo el SRP, cada clase y función tendrá una única responsabilidad, lo que facilita la escritura de pruebas unitarias. Es más sencillo probar clases pequeñas y específicas que aquellas que hacen múltiples cosas. La cobertura de pruebas será más completa.

Ejemplo: Aplicando SRP en un sistema de gestión de pedidos
Supongamos que estás desarrollando un sistema para gestionar pedidos en línea. Tienes una clase llamada Pedido que maneja tanto la lógica de creación de pedidos como el envío de correos electrónicos y la generación de facturas.

Código sin SRP:"""
class Pedido: 
    def __init__(self, cliente, items):
        self.cliente = cliente 
        self.items = items 

    def crear_pedido(self): 
    # Lógica para crear un pedido 
        pass 

    def generar_factura(self): 
        # Lógica para generar una factura 
        pass

    def enviar_email_confirmacion(self): 
        # Lógica para enviar un email
        pass 


"""Problema:
La clase Pedido tiene tres responsabilidades: crear el pedido, generar la factura y enviar un correo electrónico. Esto hace que la clase sea difícil de mantener y modificar.

Código refactorizado (siguiendo SRP):"""
class Pedido:
    def __init__(self, cliente, items):
        self.cliente = cliente 
        self.items = items 

    def crear_pedido(self):
    # Lógica para crear un pedido
        pass

class GeneradorDeFactura:
    def generar_factura(self, pedido): 
    # Lógica para generar una factura 
        pass 

class ServicioEmail: 
    def enviar_email_confirmacion(self, pedido): 
    # Lógica para enviar un email de confirmación
        pass 




"""Técnicas para aplicar SRP de manera efectiva"""
"""Diseño orientado a interfaces
Técnica: Utiliza interfaces o clases abstractas para definir la responsabilidad de la clase de forma más flexible. Ejemplo: Puedes tener una interfaz IGeneradorDeReportes que definirá solo el comportamiento relacionado con la generación de reportes, mientras que clases como Empleado o Factura implementarán esta interfaz según sus necesidades específicas.

Patrón de diseño Strategy (Estrategia)
Técnica: Utiliza el patrón Strategy para delegar responsabilidades que podrían cambiar con frecuencia, como el algoritmo de generación de reportes o el cálculo de precios, fuera de la clase principal. Ejemplo: En un sistema de facturación, puedes usar diferentes estrategias de pago (tarjeta de crédito, PayPal, transferencia bancaria). Cada estrategia se encapsula en su propia clase, y la clase Pedido solo delega el cálculo del precio a la estrategia correspondiente.

Utilizar clases auxiliares y servicios
Técnica: Si una clase tiene muchas responsabilidades, descompón esas responsabilidades en clases auxiliares o servicios especializados. Ejemplo: Una clase de Pedido no debe preocuparse por la base de datos o el envío de correos electrónicos. Estos aspectos pueden ser delegados a clases de servicio como ServicioBaseDeDatos o ServicioEmail.

Refactorización de clases grandes
Técnica: Si encuentras que una clase tiene más de una razón para cambiar (es decir, maneja más de una responsabilidad), refactórala dividiéndola en varias clases más pequeñas. Ejemplo: En lugar de tener una clase Factura que se encargue de la lógica de negocio, la validación de datos y la creación de informes, refactoriza para que cada responsabilidad se maneje en una clase diferente: GeneradorDeFactura, ValidadorDeFactura, y GeneradorDeReporteFactura.

Uso de clases de "valor" para encapsular conceptos
Técnica: Encapsula conceptos del dominio en clases de "valor" que tienen una sola responsabilidad, como un Direccion o un Telefono. Ejemplo: En lugar de almacenar una dirección de correo electrónico como una cadena de texto en una clase Cliente, crea una clase CorreoElectronico que tenga una única responsabilidad: validar y almacenar un correo electrónico.

Uso de contenedores de dependencias
Técnica: Utiliza un contenedor de dependencias para inyectar las clases necesarias en lugar de crear instancias dentro de la clase misma. Ejemplo: Si tienes una clase Factura que necesita acceso a una base de datos y a un servicio de envío de 

correos electrónicos, en lugar de crear estas dependencias dentro de la clase, puedes inyectarlas utilizando un contenedor de dependencias, como Dependency Injector o Flask.

Patrón Observer (Observador) para delegación
Técnica: Usa el patrón Observer para delegar tareas en función de eventos sin comprometer la responsabilidad de la clase. Ejemplo: Si tienes una clase Empleado y deseas que otros servicios, como el de envío de correos electrónicos, reaccionen a un cambio en el salario del empleado, puedes implementar el patrón Observer para notificar a esos servicios cuando ocurra el cambio.

Seguir el principio de Cohesión alta
Técnica: Asegúrate de que los métodos de una clase estén estrechamente relacionados entre sí. Si los métodos no están relacionados, considera moverlos a otra clase que esté más alineada con esos métodos. Ejemplo: Una clase Factura que solo contenga métodos relacionados con la creación, validación y emisión de facturas es más coherente que una clase que también maneje la generación de reportes o el cálculo de impuestos.

Usar módulos para separar responsabilidades
Técnica: En lugar de tener clases grandes, divide las funcionalidades en varios módulos que se enfoquen en tareas específicas. Ejemplo: En lugar de tener una clase Pedido que gestione todo, puedes separar la lógica de pago, facturación, envío y notificación en diferentes módulos (por ejemplo, modulo_pago.py, modulo_factura.py, modulo_envio.py, etc.).

Aplicar principios de "composición sobre herencia"
Técnica: En lugar de usar herencia para modelar comportamientos relacionados con la responsabilidad de una clase, usa la composición para delegar responsabilidades a otras clases. Ejemplo: Si tienes una clase Empleado y necesitas comportamientos diferentes para varios tipos de empleados (por ejemplo, EmpleadoTiempoCompleto y EmpleadoParcial), usa composición para incluir las clases de comportamiento específico en lugar de hacer que una clase derive de otra."""

