"""Creacionales (5)"""
# singleton_logger.py

class LoggerSingleton:
    _instance = None  # variable de clase para almacenar la instancia única

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # Si no existe la instancia, crearla
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, file_name="app.log"):
        # Evitar que __init__ se ejecute múltiples veces
        if self._initialized:
            return
        self.file_name = file_name
        self._initialized = True

    def log(self, message):
        with open(self.file_name, "a") as f:
            f.write(message + "\n")
        print(f"Logged: {message}")  # también mostrar en consola para pruebas

# --- Uso del Singleton ---

logger1 = LoggerSingleton()
logger2 = LoggerSingleton()

logger1.log("Iniciando la aplicación")
logger2.log("Usuario inició sesión")

# Verificamos que logger1 y logger2 son la misma instancia
print(logger1 is logger2)  # True

















#2. Factory Method
# factory_method_notifications.py

from abc import ABC, abstractmethod

# --- Producto abstracto ---
class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# --- Productos concretos ---
class EmailNotification(Notification):
    def send(self, message: str):
        print(f"Enviando email: {message}")

class SMSNotification(Notification):
    def send(self, message: str):
        print(f"Enviando SMS: {message}")

# --- Creador abstracto ---
class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass

# --- Creadores concretos ---
class EmailNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return EmailNotification()

class SMSNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return SMSNotification()

# --- Uso del Factory Method ---
def send_alert(factory: NotificationFactory, message: str):
    notification = factory.create_notification()
    notification.send(message)

# Elegimos el tipo de notificación en tiempo de ejecución
config = "email"  # podría venir de un archivo de config o base de datos

if config == "email":
    factory = EmailNotificationFactory()
else:
    factory = SMSNotificationFactory()

send_alert(factory, "¡Se ha detectado un problema en el sistema!")













#3. Abstract Factory
# abstract_factory_ui.py

from abc import ABC, abstractmethod

# --- Productos abstractos ---
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class TextBox(ABC):
    @abstractmethod
    def render(self):
        pass

# --- Productos concretos para Windows ---
class WindowsButton(Button):
    def render(self):
        print("Renderizando un botón estilo Windows.")

class WindowsTextBox(TextBox):
    def render(self):
        print("Renderizando un cuadro de texto estilo Windows.")

# --- Productos concretos para Mac ---
class MacButton(Button):
    def render(self):
        print("Renderizando un botón estilo Mac.")

class MacTextBox(TextBox):
    def render(self):
        print("Renderizando un cuadro de texto estilo Mac.")

# --- Fábrica abstracta ---
class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_textbox(self) -> TextBox:
        pass

# --- Fábricas concretas ---
class WindowsUIFactory(UIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_textbox(self) -> TextBox:
        return WindowsTextBox()

class MacUIFactory(UIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_textbox(self) -> TextBox:
        return MacTextBox()

# --- Uso del Abstract Factory ---
def render_ui(factory: UIFactory):
    button = factory.create_button()
    textbox = factory.create_textbox()
    button.render()
    textbox.render()

# Elegimos la fábrica según la plataforma
platform = "Mac"  # podría venir de sistema o configuración

if platform == "Windows":
    factory = WindowsUIFactory()
else:
    factory = MacUIFactory()

render_ui(factory)












#4. Builder
# builder_report.py

from abc import ABC, abstractmethod

# --- Producto: Reporte ---
class Report:
    def __init__(self):
        self.title = ""
        self.header = ""
        self.body = ""
        self.footer = ""
        self.charts = []

    def display(self):
        print("=== Reporte ===")
        print(f"Título: {self.title}")
        print(f"Header: {self.header}")
        print(f"Body: {self.body}")
        if self.charts:
            print("Charts:")
            for chart in self.charts:
                print(f" - {chart}")
        print(f"Footer: {self.footer}")
        print("================\n")

# --- Builder abstracto ---
class ReportBuilder(ABC):
    @abstractmethod
    def build_title(self, title): pass

    @abstractmethod
    def build_header(self, header): pass

    @abstractmethod
    def build_body(self, body): pass

    @abstractmethod
    def build_footer(self, footer): pass

    @abstractmethod
    def build_chart(self, chart): pass

    @abstractmethod
    def get_report(self): pass

# --- Builder concreto ---
class ConcreteReportBuilder(ReportBuilder):
    def __init__(self):
        self.report = Report()

    def build_title(self, title):
        self.report.title = title

    def build_header(self, header):
        self.report.header = header

    def build_body(self, body):
        self.report.body = body

    def build_footer(self, footer):
        self.report.footer = footer

    def build_chart(self, chart):
        self.report.charts.append(chart)

    def get_report(self):
        return self.report

# --- Director: define el orden de construcción ---
class ReportDirector:
    def __init__(self, builder: ReportBuilder):
        self.builder = builder

    def construct_financial_report(self):
        self.builder.build_title("Reporte Financiero Q4")
        self.builder.build_header("Resumen Financiero")
        self.builder.build_body("Ingresos: $50000\nGastos: $30000")
        self.builder.build_chart("Gráfico de Ingresos vs Gastos")
        self.builder.build_footer("Confidencial")

    def construct_simple_report(self):
        self.builder.build_title("Reporte Simple")
        self.builder.build_body("Contenido mínimo")

# --- Uso del Builder ---
builder = ConcreteReportBuilder()
director = ReportDirector(builder)

# Construimos un reporte financiero completo
director.construct_financial_report()
report1 = builder.get_report()
report1.display()

# Construimos un reporte simple
builder = ConcreteReportBuilder()  # nuevo builder para no mezclar
director = ReportDirector(builder)
director.construct_simple_report()
report2 = builder.get_report()
report2.display()


















#5. Prototype
# prototype_enemy.py
import copy

# --- Producto: Enemigo ---
class Enemy:
    def __init__(self, type_enemy, health, attack, abilities):
        self.type_enemy = type_enemy
        self.health = health
        self.attack = attack
        self.abilities = abilities

    def display(self):
        print(f"Enemigo: {self.type_enemy}")
        print(f"Vida: {self.health}, Ataque: {self.attack}")
        print(f"Habilidades: {self.abilities}")
        print("------------------------")

    def clone(self):
        # Retorna una copia profunda del objeto
        return copy.deepcopy(self)

# --- Uso del Prototype ---
# Creamos un "prototipo" de enemigo
orc_prototype = Enemy("Orc", 100, 15, ["Golpe fuerte", "Embiste"])

# Clonamos varios enemigos a partir del prototipo
orc1 = orc_prototype.clone()
orc2 = orc_prototype.clone()

# Modificamos algunos atributos sin afectar el prototipo
orc2.health = 120
orc2.abilities.append("Rugido aterrador")

# Mostramos todos los enemigos
orc_prototype.display()
orc1.display()
orc2.display()