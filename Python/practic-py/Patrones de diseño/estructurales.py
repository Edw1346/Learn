"""Estructurales (7)"""

"""6. Adapter. Contexto
Supongamos que estamos construyendo una aplicación de procesamiento de pagos, que originalmente trabaja con pagos en dólares, pero ahora necesitamos integrarnos con un servicio de pagos en euros.
Nuestro código cliente espera un método pay_usd(amount) para procesar pagos.
El servicio nuevo tiene un método pay_euro(amount) incompatible.
Aquí entra el Adapter, que convierte la interfaz de un servicio en otra esperada por el cliente, sin cambiar ni el cliente ni el servicio externo. Código en Python """
# adapter_payment.py

# --- Servicio existente (clase cliente espera este método) ---
class USDPaymentProcessor:
    def pay_usd(self, amount):
        print(f"Procesando pago de ${amount} USD")

# --- Servicio nuevo (interfaz incompatible) ---
class EuroPaymentProcessor:
    def pay_euro(self, amount):
        print(f"Procesando pago de €{amount} EUR")

# --- Adaptador ---
class EuroToUSDAdapter:
    def __init__(self, euro_processor: EuroPaymentProcessor, conversion_rate: float):
        self.euro_processor = euro_processor
        self.conversion_rate = conversion_rate  # ej: 1 USD = 0.95 EUR

    # Método esperado por el cliente
    def pay_usd(self, amount):
        # Convertimos USD a EUR antes de llamar al servicio nuevo
        amount_eur = amount * self.conversion_rate
        self.euro_processor.pay_euro(amount_eur)

# --- Uso del Adapter ---
usd_processor = USDPaymentProcessor()
usd_processor.pay_usd(100)  # funciona directo

# Ahora queremos usar el procesador de euros pero la app espera pay_usd
euro_processor = EuroPaymentProcessor()
adapter = EuroToUSDAdapter(euro_processor, conversion_rate=0.95)
adapter.pay_usd(100)  # llama internamente a pay_euro con conversión










"""7. Bridge. Contexto
Supongamos que estamos construyendo un sistema de notificaciones que puede enviar mensajes por distintos canales: Email y SMS. Además, los mensajes pueden tener distintos formatos: Simple o Enriquecido.
Queremos que los canales y los formatos puedan variar de forma independiente sin generar una combinación de clases para cada caso.
Aquí entra Bridge, que separa la abstracción (mensaje) de su implementación (canal de envío), permitiendo combinaciones independientes. Código en Python"""
# bridge_notification.py

from abc import ABC, abstractmethod

# --- Implementador (interface de envío) ---
class MessageSender(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# --- Implementaciones concretas ---
class EmailSender(MessageSender):
    def send(self, message: str):
        print(f"Enviando por Email: {message}")

class SMSSender(MessageSender):
    def send(self, message: str):
        print(f"Enviando por SMS: {message}")

# --- Abstracción ---
class Notification(ABC):
    def __init__(self, sender: MessageSender):
        self.sender = sender

    @abstractmethod
    def send(self, content: str):
        pass

# --- Refined Abstractions ---
class SimpleNotification(Notification):
    def send(self, content: str):
        message = f"[Simple] {content}"
        self.sender.send(message)

class RichNotification(Notification):
    def send(self, content: str):
        message = f"[Enriquecido] *** {content} ***"
        self.sender.send(message)

# --- Uso del Bridge ---

# Simple notification por Email
email_sender = EmailSender()
simple_email = SimpleNotification(email_sender)
simple_email.send("Hola usuario")

# Rich notification por SMS
sms_sender = SMSSender()
rich_sms = RichNotification(sms_sender)
rich_sms.send("¡Alerta importante!")






"""8. Composite. Contexto
Supongamos que estamos construyendo un sistema de archivos:
Tenemos archivos individuales y carpetas que pueden contener archivos o más carpetas.
Queremos que tanto archivos como carpetas puedan ser tratados de manera uniforme al mostrar su contenido, calcular tamaño, etc. Aquí entra Composite, que permite tratar objetos individuales y compuestos de manera uniforme. Código:"""
# composite_filesystem.py

from abc import ABC, abstractmethod

# --- Componente abstracto ---
class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass

# --- Hoja: archivo individual ---
class File(FileSystemComponent):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def display(self, indent=0):
        print('  ' * indent + f"Archivo: {self.name} ({self.size}KB)")

# --- Compuesto: carpeta ---
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def display(self, indent=0):
        print('  ' * indent + f"Carpeta: {self.name}")
        for child in self.children:
            child.display(indent + 1)

# --- Uso del Composite ---
# Creamos archivos
file1 = File("documento.txt", 10)
file2 = File("imagen.png", 50)

# Creamos carpetas
folder1 = Folder("Mis Documentos")
folder2 = Folder("Fotos")

# Construimos la jerarquía
folder1.add(file1)
folder2.add(file2)
folder1.add(folder2)  # Carpeta dentro de carpeta

# Mostramos la estructura
folder1.display()

#Salida esperada:
#Carpeta: Mis Documentos
#Archivo: documento.txt (10KB)
#Carpeta: Fotos
#Archivo: imagen.png (50KB)













"""9. Decorator. Contexto
Imagina que estamos construyendo un sistema de pedidos de café:
Tenemos un café básico.
Podemos agregar adicionales como leche, chocolate, o espuma.
Queremos agregar funcionalidades dinámicamente sin modificar la clase base de café.
Aquí entra Decorator, que permite envolver objetos con funcionalidades adicionales de manera flexible. Código en Python"""
# decorator_coffee.py

from abc import ABC, abstractmethod

# --- Componente base ---
class Coffee(ABC):
    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

# --- Componente concreto ---
class SimpleCoffee(Coffee):
    def get_cost(self) -> float:
        return 2.0

    def get_description(self) -> str:
        return "Café simple"

# --- Decorador abstracto ---
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    @abstractmethod
    def get_cost(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

# --- Decoradores concretos ---
class MilkDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 0.5

    def get_description(self) -> str:
        return self._coffee.get_description() + ", con leche"

class ChocolateDecorator(CoffeeDecorator):
    def get_cost(self) -> float:
        return self._coffee.get_cost() + 1.0

    def get_description(self) -> str:
        return self._coffee.get_description() + ", con chocolate"

# --- Uso del Decorator ---
# Café simple
coffee = SimpleCoffee()
print(coffee.get_description(), "-", coffee.get_cost(), "USD")

# Café con leche
coffee_with_milk = MilkDecorator(coffee)
print(coffee_with_milk.get_description(), "-", coffee_with_milk.get_cost(), "USD")

# Café con leche y chocolate
coffee_with_milk_chocolate = ChocolateDecorator(coffee_with_milk)
print(coffee_with_milk_chocolate.get_description(), "-", coffee_with_milk_chocolate.get_cost(), "USD")

#Salida esperada:
#Café simple - 2.0 USD
#Café simple, con leche - 2.5 USD
#Café simple, con leche, con chocolate - 3.5 USD















"""10. Facade. Contexto:
Imagina que estamos construyendo un sistema de compra en línea.
El proceso de compra involucra múltiples subsistemas: 
Inventario (InventorySystem)
Procesamiento de pagos (PaymentSystem)
Envíos (ShippingSystem)
Queremos que el cliente del sistema pueda realizar una compra con una sola llamada, sin conocer los detalles internos de cada subsistema. Aquí entra Facade, que proporciona una interfaz unificada y simple para interactuar con un sistema complejo. Código en Python"""
# facade_online_store.py

# --- Subsistema 1: Inventario ---
class InventorySystem:
    def check_stock(self, product):
        print(f"Verificando stock de {product}")
        return True

# --- Subsistema 2: Pagos ---
class PaymentSystem:
    def process_payment(self, product, amount):
        print(f"Procesando pago de ${amount} por {product}")
        return True

# --- Subsistema 3: Envíos ---
class ShippingSystem:
    def ship_product(self, product):
        print(f"Enviando {product} al cliente")
        return True

# --- Fachada ---
class OnlineStoreFacade:
    def __init__(self):
        self.inventory = InventorySystem()
        self.payment = PaymentSystem()
        self.shipping = ShippingSystem()

    def purchase_product(self, product, amount):
        if self.inventory.check_stock(product):
            if self.payment.process_payment(product, amount):
                if self.shipping.ship_product(product):
                    print(f"Compra de {product} completada exitosamente.\n")
                else:
                    print("Error en el envío.")
            else:
                print("Error en el pago.")
        else:
            print("Producto agotado.")

# --- Uso del Facade ---
store = OnlineStoreFacade()
store.purchase_product("Laptop", 1200)
store.purchase_product("Auriculares", 100)

#Salida esperada:
#Verificando stock de Laptop
#Procesando pago de $1200 por Laptop
#Enviando Laptop al cliente
#Compra de Laptop completada exitosamente.

#Verificando stock de Auriculares
#Procesando pago de $100 por Auriculares
#Enviando Auriculares al cliente
#Compra de Auriculares completada exitosamente.







"""11. Flyweight. Contexto:
Imagina que estamos creando un editor de texto muy grande que puede tener millones de caracteres en pantalla.
Cada carácter tiene información intrínseca (letra, fuente) y extrínseca (posición en el documento).
Crear un objeto completo para cada carácter consumiría mucha memoria.
Aquí entra Flyweight, que permite compartir objetos comunes (intrínsecos) y mantener separados los datos extrínsecos, optimizando el uso de memoria. Código en Python"""
# flyweight_text_editor.py

from abc import ABC, abstractmethod

# --- Flyweight: carácter compartido ---
class CharacterFlyweight(ABC):
    @abstractmethod
    def display(self, position):
        pass

# --- Flyweight concreto ---
class Character(CharacterFlyweight):
    def __init__(self, char, font):
        self.char = char       # intrínseco
        self.font = font       # intrínseco

    def display(self, position):
        # position es extrínseco
        print(f"Caracter '{self.char}' con fuente '{self.font}' en posición {position}")

# --- Flyweight Factory: administra objetos compartidos ---
class CharacterFactory:
    def __init__(self):
        self._characters = {}

    def get_character(self, char, font):
        key = (char, font)
        if key not in self._characters:
            self._characters[key] = Character(char, font)
        return self._characters[key]

# --- Uso del Flyweight ---
factory = CharacterFactory()

document = [
    ('H', 'Arial', 0),
    ('e', 'Arial', 1),
    ('l', 'Arial', 2),
    ('l', 'Arial', 3),
    ('o', 'Arial', 4),
    ('H', 'Arial', 5),  # se reutiliza el mismo objeto 'H'
]

for char, font, position in document:
    c = factory.get_character(char, font)
    c.display(position)

#Salida esperada:
#Caracter 'H' con fuente 'Arial' en posición 0
#Caracter 'e' con fuente 'Arial' en posición 1
#Caracter 'l' con fuente 'Arial' en posición 2
#Caracter 'l' con fuente 'Arial' en posición 3
#Caracter 'o' con fuente 'Arial' en posición 4
#Caracter 'H' con fuente 'Arial' en posición 5
#Nota: El objeto 'H' con fuente 'Arial' se reutiliza, en lugar de crear uno nuevo.













"""12. Proxy. Contexto:
Imagina que estamos construyendo un sistema de visualización de imágenes de alta resolución:
Cargar imágenes grandes consume mucho tiempo y memoria.
Queremos mostrar una imagen cuando sea necesario, pero no cargarla inmediatamente. Aquí entra el Proxy, que actúa como representante del objeto real, cargándolo solo cuando es necesario (lazy loading). Código en Python"""
# proxy_image_viewer.py

from abc import ABC, abstractmethod

# --- Interfaz ---
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# --- Objeto real ---
class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_image_from_disk()

    def load_image_from_disk(self):
        print(f"Cargando imagen de {self.filename} desde disco...")

    def display(self):
        print(f"Mostrando imagen {self.filename}")

# --- Proxy ---
class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

# --- Uso del Proxy ---
print("Cliente crea proxy de imagen:")
image1 = ProxyImage("foto1.png")
image2 = ProxyImage("foto2.png")

print("\nCliente solicita mostrar la primera imagen:")
image1.display()  # se carga y muestra

print("\nCliente solicita mostrar la primera imagen otra vez:")
image1.display()  # ya está cargada, solo muestra

print("\nCliente solicita mostrar la segunda imagen:")
image2.display()  # se carga y muestra

#Salida esperada:
#Cliente crea proxy de imagen:

#Cliente solicita mostrar la primera imagen:
#Cargando imagen de foto1.png desde disco...
#Mostrando imagen foto1.png

#Cliente solicita mostrar la primera imagen otra vez:
#Mostrando imagen foto1.png

#Cliente solicita mostrar la segunda imagen:
#Cargando imagen de foto2.png desde disco...
#Mostrando imagen foto2.png
#Nota: La imagen se carga solo cuando se necesita, gracias al Proxy.