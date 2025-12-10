"""Comportamentales (11)"""

"""13. Chain of Responsibility. Contexto
Imagina que estamos construyendo un sistema de soporte técnico:
Tenemos distintos niveles de soporte: Soporte Básico, Soporte Avanzado y Soporte Experto.
Cada solicitud de ayuda puede ser resuelta por distintos niveles, dependiendo de su complejidad.
No queremos que cada nivel conozca a todos los otros niveles, ni tener condicionales enormes.
Aquí entra Chain of Responsibility, que permite pasar la solicitud a lo largo de una cadena de objetos hasta que alguien la maneje. Código en Python"""
# chain_of_responsibility_support.py

from abc import ABC, abstractmethod

# --- Handler abstracto ---
class SupportHandler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abstractmethod
    def handle_request(self, issue_level: int):
        pass

# --- Handlers concretos ---
class BasicSupport(SupportHandler):
    def handle_request(self, issue_level: int):
        if issue_level == 1:
            print("Soporte Básico: Resuelto el problema simple.")
        elif self.next_handler:
            self.next_handler.handle_request(issue_level)

class AdvancedSupport(SupportHandler):
    def handle_request(self, issue_level: int):
        if issue_level == 2:
            print("Soporte Avanzado: Resuelto el problema intermedio.")
        elif self.next_handler:
            self.next_handler.handle_request(issue_level)

class ExpertSupport(SupportHandler):
    def handle_request(self, issue_level: int):
        if issue_level == 3:
            print("Soporte Experto: Resuelto el problema complejo.")
        elif self.next_handler:
            print("No se pudo resolver el problema.")

# --- Uso de la cadena ---
# Creamos la cadena de responsabilidad
chain = BasicSupport(AdvancedSupport(ExpertSupport()))

# Diferentes solicitudes
chain.handle_request(1)  # manejado por BasicSupport
chain.handle_request(2)  # manejado por AdvancedSupport
chain.handle_request(3)  # manejado por ExpertSupport
chain.handle_request(4)  # no se puede resolver

#Salida esperada:
#Soporte Básico: Resuelto el problema simple.
#Soporte Avanzado: Resuelto el problema intermedio.
#Soporte Experto: Resuelto el problema complejo.
#No se pudo resolver el problema.









"""14. Command. Contexto
Imagina que estamos construyendo un sistema de control remoto para una casa inteligente:
Podemos encender o apagar distintos dispositivos: luz, ventilador, televisión.
Queremos separar el objeto que invoca la acción (control remoto) del objeto que realiza la acción (dispositivos).
Aquí entra Command, que encapsula una solicitud como un objeto, permitiendo ejecutar, deshacer o almacenar acciones fácilmente. Código en Python"""
# command_home_automation.py

from abc import ABC, abstractmethod

# --- Command abstracto ---
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# --- Receptores (objetos que realizan la acción) ---
class Light:
    def turn_on(self):
        print("Luz encendida")

    def turn_off(self):
        print("Luz apagada")

class Fan:
    def turn_on(self):
        print("Ventilador encendido")

    def turn_off(self):
        print("Ventilador apagado")

# --- Comandos concretos ---
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_off()

class FanOnCommand(Command):
    def __init__(self, fan: Fan):
        self.fan = fan

    def execute(self):
        self.fan.turn_on()

class FanOffCommand(Command):
    def __init__(self, fan: Fan):
        self.fan = fan

    def execute(self):
        self.fan.turn_off()

# --- Invocador ---
class RemoteControl:
    def __init__(self):
        self.commands = []

    def set_command(self, command: Command):
        self.commands.append(command)

    def press_button(self):
        for command in self.commands:
            command.execute()
        self.commands.clear()  # ejecutadas, limpiamos la lista

# --- Uso del Command ---
light = Light()
fan = Fan()

# Creamos comandos
light_on = LightOnCommand(light)
fan_on = FanOnCommand(fan)
light_off = LightOffCommand(light)

# Configuramos el control remoto
remote = RemoteControl()
remote.set_command(light_on)
remote.set_command(fan_on)
remote.press_button()  # ejecuta todos los comandos

remote.set_command(light_off)
remote.press_button()  # apaga la luz

#Salida esperada:
#Luz encendida
#Ventilador encendido
#Luz apagada










"""15. Interpreter. Contexto
Imagina que estamos construyendo un sistema de validación de expresiones matemáticas simples (como 5 + 3 - 2) o instrucciones de lenguaje mini DSL (Domain Specific Language).
Queremos interpretar expresiones de texto y obtener un resultado.
Cada operación (suma, resta, número) se puede representar como un objeto que sabe cómo interpretarse.
Aquí entra Interpreter, que define una gramática para interpretar expresiones y permite extender fácilmente nuevas operaciones. Código en Python"""
# interpreter_calculator.py

from abc import ABC, abstractmethod

# --- Expresión abstracta ---
class Expression(ABC):
    @abstractmethod
    def interpret(self):
        pass

# --- Expresiones terminales ---
class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self):
        return self.value

# --- Expresiones no terminales ---
class Add(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

class Subtract(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

# --- Uso del Interpreter ---
# Expresión: 5 + 3 - 2
expression = Subtract(Add(Number(5), Number(3)), Number(2))
result = expression.interpret()
print("Resultado de 5 + 3 - 2 =", result)

#Salida esperada: 
#Resultado de 5 + 3 - 2 = 6 
#Nota: Cada operación sabe cómo interpretar su resultado y combina otros elementos, formando un árbol de expresión.














"""16. Iterator. Contexto
Imagina que estamos construyendo un sistema de gestión de playlists de música:
Una playlist contiene canciones que pueden almacenarse en diferentes estructuras internas (lista, diccionario, etc.).
Queremos recorrer todas las canciones sin exponer cómo se almacenan internamente.
Aquí entra Iterator, que permite recorrer los elementos de una colección sin conocer su estructura interna. Código Python"""
# iterator_playlist.py

from abc import ABC, abstractmethod

# --- Iterator abstracto ---
class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self):
        pass

# --- Colección abstracta ---
class Playlist(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass

# --- Colección concreta ---
class SongPlaylist(Playlist):
    def __init__(self):
        self.songs = []

    def add_song(self, song: str):
        self.songs.append(song)

    def create_iterator(self) -> Iterator:
        return SongIterator(self.songs)

# --- Iterator concreto ---
class SongIterator(Iterator):
    def __init__(self, songs):
        self._songs = songs
        self._position = 0

    def has_next(self) -> bool:
        return self._position < len(self._songs)

    def next(self):
        song = self._songs[self._position]
        self._position += 1
        return song

# --- Uso del Iterator ---
playlist = SongPlaylist()
playlist.add_song("Song A")
playlist.add_song("Song B")
playlist.add_song("Song C")

iterator = playlist.create_iterator()

print("Reproduciendo playlist:")
while iterator.has_next():
    print(" -", iterator.next())

#Salida esperada:
#Reproduciendo playlist:
# - Song A
# - Song B
# - Song C
#Nota: El cliente no sabe ni le importa cómo se almacenan las canciones, solo usa el iterator.







"""17. Mediator. Contexto
Imagina que estamos construyendo un chat de grupo:
Tenemos varios usuarios que pueden enviarse mensajes.
No queremos que cada usuario conozca directamente a todos los demás.
Aquí entra Mediator, que actúa como intermediario central: los usuarios envían mensajes al mediator, y este se encarga de distribuirlos a los demás. Código en Python"""
# mediator_chat.py

from abc import ABC, abstractmethod

# --- Mediator abstracto ---
class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, message: str, user):
        pass

# --- Usuario ---
class User:
    def __init__(self, name: str, mediator: ChatMediator):
        self.name = name
        self.mediator = mediator

    def send(self, message: str):
        print(f"{self.name} envía: {message}")
        self.mediator.send_message(message, self)

    def receive(self, message: str):
        print(f"{self.name} recibe: {message}")

# --- Mediator concreto ---
class ChatRoom(ChatMediator):
    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)

    def send_message(self, message: str, sender: User):
        for user in self.users:
            if user != sender:
                user.receive(message)

# --- Uso del Mediator ---
chat_room = ChatRoom()

alice = User("Alice", chat_room)
bob = User("Bob", chat_room)
charlie = User("Charlie", chat_room)

chat_room.add_user(alice)
chat_room.add_user(bob)
chat_room.add_user(charlie)

alice.send("Hola a todos!")
bob.send("Hola Alice!")

#Salida esperada:
#Alice envía: Hola a todos!
#Bob recibe: Hola a todos!
#Charlie recibe: Hola a todos!
#Bob envía: Hola Alice!
#Alice recibe: Hola Alice!
#Charlie recibe: Hola Alice!
#Nota: Cada usuario no conoce a los demás usuarios directamente, solo interactúa con el Mediator.









"""18. Memento. Contexto
Imagina que estamos construyendo un editor de texto:
El usuario puede escribir y modificar el contenido.
Queremos poder deshacer cambios y restaurar versiones anteriores sin exponer la estructura interna del documento.
Aquí entra Memento, que permite guardar snapshots del estado y restaurarlos cuando sea necesario. Código en Python"""
# memento_editor.py

from copy import deepcopy

# --- Memento: guarda el estado ---
class Memento:
    def __init__(self, content: str):
        self._content = content

    def get_content(self):
        return self._content

# --- Originador: objeto cuyo estado queremos guardar ---
class TextEditor:
    def __init__(self):
        self.content = ""

    def write(self, text: str):
        self.content += text

    def save(self) -> Memento:
        # Crea un memento con el estado actual
        return Memento(self.content)

    def restore(self, memento: Memento):
        # Restaura el estado desde el memento
        self.content = memento.get_content()

# --- Caretaker: guarda mementos ---
class History:
    def __init__(self):
        self._history = []

    def push(self, memento: Memento):
        self._history.append(memento)

    def pop(self) -> Memento:
        if not self._history:
            return None
        return self._history.pop()

# --- Uso del Memento ---
editor = TextEditor()
history = History()

editor.write("Hola")
history.push(editor.save())

editor.write(", mundo")
history.push(editor.save())

editor.write("!!!")

print("Contenido actual:", editor.content)

# Deshacer cambios
editor.restore(history.pop())
print("Después de deshacer 1:", editor.content)

editor.restore(history.pop())
print("Después de deshacer 2:", editor.content)

#Salida esperada:
#Contenido actual: Hola, mundo!!!
#Después de deshacer 1: Hola, mundo
#Después de deshacer 2: Hola
#Nota: Cada Memento guarda un snapshot del contenido, y el editor puede restaurarlo cuando quiera.







"""19. Observer. Contexto
Imagina que estamos construyendo un sistema de monitoreo de temperatura:
Hay un sensor de temperatura que cambia su valor constantemente.
Queremos que varios dispositivos o componentes se enteren automáticamente cuando la temperatura cambie, por ejemplo: pantalla de temperatura, alarma, registro de datos.
Aquí entra Observer, donde los objetos observan a un sujeto y reciben notificaciones cuando cambia su estado. Código:"""
# observer_temperature.py

from abc import ABC, abstractmethod

# --- Subject ---
class TemperatureSensor:
    def __init__(self):
        self._observers = []
        self._temperature = 0

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature):
        print(f"\nSensor: temperatura cambiada a {temperature}°C")
        self._temperature = temperature
        self.notify()

# --- Observer abstracto ---
class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

# --- Observers concretos ---
class Display(Observer):
    def update(self, temperature):
        print(f"Display: mostrando {temperature}°C")

class Alarm(Observer):
    def update(self, temperature):
        if temperature > 30:
            print("Alarm: temperatura demasiado alta! Activando alarma.")

class Logger(Observer):
    def update(self, temperature):
        print(f"Logger: registrando temperatura {temperature}°C")

# --- Uso del Observer ---
sensor = TemperatureSensor()

display = Display()
alarm = Alarm()
logger = Logger()

# Registramos observadores
sensor.attach(display)
sensor.attach(alarm)
sensor.attach(logger)

# Cambios de temperatura
sensor.set_temperature(25)
sensor.set_temperature(35)

#Salida esperada:
#Sensor: temperatura cambiada a 25°C
#Display: mostrando 25°C
#Logger: registrando temperatura 25°C

#Sensor: temperatura cambiada a 35°C
#Display: mostrando 35°C
#Alarm: temperatura demasiado alta! Activando alarma.
#Logger: registrando temperatura 35°C
#Nota: Cada observador recibe automáticamente la actualización sin que el sensor conozca los detalles de cada uno.




"""20. State. Contexto
Imagina que estamos construyendo un reproductor de música:
El reproductor tiene distintos estados: Detenido, Reproduciendo, Pausado.
Cada acción (play, pause, stop) se comporta diferente según el estado actual.
Aquí entra State, que permite cambiar el comportamiento de un objeto cuando cambia su estado interno, evitando condicionales gigantes. Código en Python"""
# state_music_player.py

from abc import ABC, abstractmethod

# --- Estado abstracto ---
class State(ABC):
    @abstractmethod
    def play(self, player):
        pass

    @abstractmethod
    def pause(self, player):
        pass

    @abstractmethod
    def stop(self, player):
        pass

# --- Estados concretos ---
class Stopped(State):
    def play(self, player):
        print("Reproductor: Iniciando reproducción")
        player.state = Playing()

    def pause(self, player):
        print("Reproductor: No se puede pausar, está detenido")

    def stop(self, player):
        print("Reproductor: Ya está detenido")

class Playing(State):
    def play(self, player):
        print("Reproductor: Ya está reproduciendo")

    def pause(self, player):
        print("Reproductor: Pausando reproducción")
        player.state = Paused()

    def stop(self, player):
        print("Reproductor: Deteniendo reproducción")
        player.state = Stopped()

class Paused(State):
    def play(self, player):
        print("Reproductor: Reanudando reproducción")
        player.state = Playing()

    def pause(self, player):
        print("Reproductor: Ya está pausado")

    def stop(self, player):
        print("Reproductor: Deteniendo desde pausa")
        player.state = Stopped()

# --- Contexto ---
class MusicPlayer:
    def __init__(self):
        self.state: State = Stopped()

    def play(self):
        self.state.play(self)

    def pause(self):
        self.state.pause(self)

    def stop(self):
        self.state.stop(self)

# --- Uso del State ---
player = MusicPlayer()

player.play()   # Detenido -> Reproduciendo
player.pause()  # Reproduciendo -> Pausado
player.play()   # Pausado -> Reproduciendo
player.stop()   # Reproduciendo -> Detenido
player.pause()  # Detenido -> No se puede pausar

#Salida esperada:
#Reproductor: Iniciando reproducción
#Reproductor: Pausando reproducción
#Reproductor: Reanudando reproducción
#Reproductor: Deteniendo reproducción
#Reproductor: No se puede pausar, está detenido
#Nota: Cada estado define cómo responde a las acciones, y el contexto cambia su estado dinámicamente.





"""21. Strategy. Contexto
Imagina que estamos construyendo un sistema de envío de pedidos:
Los pedidos se pueden enviar mediante diferentes métodos: correo, mensajería exprés, drone, etc.
Queremos cambiar la estrategia de envío dinámicamente sin modificar el objeto Pedido.
Aquí entra Strategy, que permite definir familias de algoritmos intercambiables y seleccionar cuál usar en tiempo de ejecución. Código en Python"""
# strategy_shipping.py

from abc import ABC, abstractmethod

# --- Estrategia abstracta ---
class ShippingStrategy(ABC):
    @abstractmethod
    def ship(self, order_id: str):
        pass

# --- Estrategias concretas ---
class PostalShipping(ShippingStrategy):
    def ship(self, order_id: str):
        print(f"Pedido {order_id} enviado por correo postal")

class ExpressShipping(ShippingStrategy):
    def ship(self, order_id: str):
        print(f"Pedido {order_id} enviado por mensajería exprés")

class DroneShipping(ShippingStrategy):
    def ship(self, order_id: str):
        print(f"Pedido {order_id} enviado por drone")

# --- Contexto ---
class Order:
    def __init__(self, order_id: str, strategy: ShippingStrategy):
        self.order_id = order_id
        self.strategy = strategy

    def set_strategy(self, strategy: ShippingStrategy):
        self.strategy = strategy

    def ship_order(self):
        self.strategy.ship(self.order_id)

# --- Uso del Strategy ---
order1 = Order("001", PostalShipping())
order1.ship_order()  # Pedido 001 enviado por correo postal

# Cambiamos la estrategia dinámicamente
order1.set_strategy(ExpressShipping())
order1.ship_order()  # Pedido 001 enviado por mensajería exprés

order1.set_strategy(DroneShipping())
order1.ship_order()  # Pedido 001 enviado por drone

#Salida esperada:
#Pedido 001 enviado por correo postal
#Pedido 001 enviado por mensajería exprés
#Pedido 001 enviado por drone
#Nota: El objeto Order delegó la acción de envío a una estrategia, que puede cambiar dinámicamente.






"""22. Template Method. Contexto
Imagina que estamos construyendo un sistema de preparación de bebidas:
Tenemos distintos tipos de bebidas como café y té.
Cada bebida sigue un proceso similar: hervir agua, preparar la bebida, servir.
Algunas etapas son comunes y otras varían según la bebida.
Aquí entra Template Method, que permite definir la estructura de un algoritmo en una clase base y dejar que las subclases implementen los pasos específicos. Código en Python"""
# template_method_beverage.py

from abc import ABC, abstractmethod

# --- Clase abstracta (Template) ---
class Beverage(ABC):
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Hirviendo agua")

    @abstractmethod
    def brew(self):
        pass

    def pour_in_cup(self):
        print("Vertiendo en la taza")

    @abstractmethod
    def add_condiments(self):
        pass

# --- Subclases concretas ---
class Tea(Beverage):
    def brew(self):
        print("Infusionando té")

    def add_condiments(self):
        print("Agregando limón")

class Coffee(Beverage):
    def brew(self):
        print("Preparando café")

    def add_condiments(self):
        print("Agregando azúcar y leche")

# --- Uso del Template Method ---
print("Preparando té:")
tea = Tea()
tea.prepare()

print("\nPreparando café:")
coffee = Coffee()
coffee.prepare()

#Salida esperada:
#Preparando té:
#Hirviendo agua
#Infusionando té
#Vertiendo en la taza
#Agregando limón

#Preparando café:
#Hirviendo agua
#Preparando café
#Vertiendo en la taza
#Agregando azúcar y leche
#Nota: El método prepare define la estructura del algoritmo, mientras que las subclases implementan los pasos específicos.







"""23. Visitor. Contexto
Imagina que estamos construyendo un sistema de compras:
Tenemos diferentes tipos de productos: Libro, DVD.
Queremos aplicar operaciones distintas sobre los productos, como calcular impuestos o imprimir detalles, sin modificar las clases de los productos. Aquí entra Visitor, que permite definir nuevas operaciones sobre una estructura de objetos sin cambiar las clases de esos objetos. Código en Python"""
# visitor_shopping.py

from abc import ABC, abstractmethod

# --- Elementos ---
class Product(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Book(Product):
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def accept(self, visitor):
        visitor.visit_book(self)

class DVD(Product):
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def accept(self, visitor):
        visitor.visit_dvd(self)

# --- Visitor abstracto ---
class Visitor(ABC):
    @abstractmethod
    def visit_book(self, book: Book):
        pass

    @abstractmethod
    def visit_dvd(self, dvd: DVD):
        pass

# --- Visitor concretos ---
class TaxVisitor(Visitor):
    def visit_book(self, book: Book):
        print(f"Book '{book.title}' impuesto: {book.price * 0.1}")

    def visit_dvd(self, dvd: DVD):
        print(f"DVD '{dvd.title}' impuesto: {dvd.price * 0.2}")

class PrintVisitor(Visitor):
    def visit_book(self, book: Book):
        print(f"Book: {book.title}, Price: {book.price}")

    def visit_dvd(self, dvd: DVD):
        print(f"DVD: {dvd.title}, Price: {dvd.price}")

# --- Uso del Visitor ---
products = [
    Book("Python 101", 50),
    DVD("Matrix", 100)
]

tax_visitor = TaxVisitor()
print_visitor = PrintVisitor()

print("Calculando impuestos:")
for product in products:
    product.accept(tax_visitor)

print("\nImprimiendo detalles:")
for product in products:
    product.accept(print_visitor)

#Salida esperada:
#Calculando impuestos:
#Book 'Python 101' impuesto: 5.0
#DVD 'Matrix' impuesto: 20.0

#Imprimiendo detalles:
#Book: Python 101, Price: 50
#DVD: Matrix, Price: 100
#Nota: Cada Product delega la operación al visitor correspondiente. Se pueden agregar nuevas operaciones sin modificar los productos.

