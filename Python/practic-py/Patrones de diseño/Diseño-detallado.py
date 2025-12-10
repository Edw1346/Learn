"""Diseño Detallado Basado en Interfaz
Cómo se usa en la práctica
Definir la interfaz"""
from abc import ABC, abstractmethod

class IPaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

#Crear implementaciones concretas
class PayPalProcessor(IPaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Procesando pago de {amount} con PayPal")

class StripeProcessor(IPaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Procesando pago de {amount} con Stripe")

#Consumir la interfaz
class OrderService:
    def __init__(self, payment_processor: IPaymentProcessor):
        self.payment_processor = payment_processor

    def checkout(self, amount: float):
        self.payment_processor.process_payment(amount)

# Uso
paypal = PayPalProcessor()
order = OrderService(paypal)
order.checkout(100)  # Procesando pago de 100 con PayPal
#Nota: OrderService no conoce la implementación concreta, solo usa la interfaz.









"""Diseño Basado en Flujos de Datos (Data Flow Design)
Cómo se usa en la práctica
Definir fuentes y destinos de datos Ejemplo: leer datos de un CSV, procesarlos y guardarlos en base de datos.
Diseñar pipeline de procesamiento Dividir en pasos: limpieza → normalización → cálculo de métricas → almacenamiento.
Implementar cada etapa"""
# Ejemplo sencillo de pipeline
data = [1, 2, 3, 4, 5]

# Transformaciones
def multiply_by_two(numbers):
    return [x*2 for x in numbers]

def filter_even(numbers):
    return [x for x in numbers if x % 2 == 0]

# Flujo de datos
processed = multiply_by_two(data)
processed = filter_even(processed)

print(processed)  # [4, 8]

#Agregar nuevas etapas sin modificar las existentes Modularidad permite cambiar el flujo sin romper otras etapas.
#Escalar o paralelizar Cada función o etapa puede ejecutarse en threads, procesos o nodos distribuidos.









"""Beneficios del diseño basado en flujo de datos
Mantenibilidad → cada etapa es independiente y reemplazable.
Flexibilidad → agregar nuevas transformaciones o fuentes es sencillo.
Escalabilidad → permite paralelismo y distribución.
Claridad y trazabilidad → fácil entender cómo los datos se transforman y se mueven.
Profesionalidad → usado en sistemas de Big Data, ETL, procesamiento de eventos y pipelines modernos.
Diseño Basado en Estados (State-Based Design)
Cómo se usa en la práctica. Ejemplo sencillo: máquina expendedora"""
from abc import ABC, abstractmethod

# Interfaz del estado
class VendingState(ABC):
    @abstractmethod
    def insert_coin(self, context):
        pass
    
    @abstractmethod
    def select_item(self, context):
        pass

# Estado bloqueado
class LockedState(VendingState):
    def insert_coin(self, context):
        print("Moneda insertada. La máquina ahora está desbloqueada.")
        context.state = UnlockedState()
    
    def select_item(self, context):
        print("Inserta una moneda primero.")

# Estado desbloqueado
class UnlockedState(VendingState):
    def insert_coin(self, context):
        print("Ya hay moneda insertada.")
    
    def select_item(self, context):
        print("Producto entregado. Máquina bloqueada nuevamente.")
        context.state = LockedState()

# Contexto de la máquina
class VendingMachine:
    def __init__(self):
        self.state = LockedState()
    
    def insert_coin(self):
        self.state.insert_coin(self)
    
    def select_item(self):
        self.state.select_item(self)

# Uso
machine = VendingMachine()
machine.select_item()   # Inserta una moneda primero.
machine.insert_coin()   # Moneda insertada. La máquina ahora está desbloqueada.
machine.select_item()   # Producto entregado. Máquina bloqueada nuevamente.
#Nota: Aquí cada estado encapsula su comportamiento, y la máquina (context) solo delega.










"""Diseño Basado en Eventos (Event-Driven Design)
Cómo se usa en la práctica. Ejemplo sencillo: notificación de usuarios registrados"""
# Definición de eventos y listeners
class EventBus:
    def __init__(self):
        self.listeners = {}
    
    def subscribe(self, event_type, listener):
        self.listeners.setdefault(event_type, []).append(listener)
    
    def publish(self, event_type, data):
        if event_type in self.listeners:
            for listener in self.listeners[event_type]:
                listener(data)

# Handlers de eventos
def send_welcome_email(user):
    print(f"Enviando email de bienvenida a {user}")

def add_to_marketing_list(user):
    print(f"Agregando {user} a la lista de marketing")

# Uso del bus de eventos
bus = EventBus()
bus.subscribe("UserRegistered", send_welcome_email)
bus.subscribe("UserRegistered", add_to_marketing_list)

# Emisor de eventos
def register_user(user):
    print(f"Usuario registrado: {user}")
    bus.publish("UserRegistered", user)

# Registrar un usuario
register_user("alice@example.com")

#Salida:
#Usuario registrado: alice@example.com
#Enviando email de bienvenida a alice@example.com
#Agregando alice@example.com a la lista de marketing
#Nota: register_user no conoce los listeners, solo emite un evento. Cada listener puede reaccionar de forma independiente.




"""Qué es el diseño basado en protocolos
Cómo se usa en la práctica. Ejemplo sencillo: comunicación basada en protocolo REST"""
# Definimos un "protocolo" usando una interfaz abstracta
from abc import ABC, abstractmethod

class PaymentProtocol(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Implementación de protocolo para PayPal
class PayPalPayment(PaymentProtocol):
    def process_payment(self, amount):
        print(f"Procesando {amount} con PayPal")

# Implementación de protocolo para Stripe
class StripePayment(PaymentProtocol):
    def process_payment(self, amount):
        print(f"Procesando {amount} con Stripe")

# Cliente que usa protocolo sin importar implementación concreta
def pay(amount, processor: PaymentProtocol):
    processor.process_payment(amount)

# Uso
paypal = PayPalPayment()
stripe = StripePayment()
pay(100, paypal)   # Procesando 100 con PayPal
pay(200, stripe)   # Procesando 200 con Stripe
#Nota: pay solo conoce el protocolo, no la implementación concreta, lo que permite cambiar o agregar procesadores sin modificar el cliente.






"""Diseño Basado en Reglas (Rule-Based Design)
Cómo se usa en la práctica. Ejemplo sencillo: validación de descuentos"""
# Definimos reglas como funciones
def discount_rule_1(order):
    if order['amount'] > 100:
        order['discount'] = 10
        print("Aplicando 10% de descuento por pedido mayor a 100")

def discount_rule_2(order):
    if order['customer_type'] == 'VIP':
        order['discount'] = 20
        print("Aplicando 20% de descuento para cliente VIP")

# Motor de reglas
def apply_rules(order, rules):
    for rule in rules:
        rule(order)

# Datos de entrada
order = {'amount': 120, 'customer_type': 'VIP', 'discount': 0}

# Aplicación de reglas
rules = [discount_rule_1, discount_rule_2]
apply_rules(order, rules)

print(order)  # {'amount': 120, 'customer_type': 'VIP', 'discount': 20}
#Nota: Las reglas se aplican de forma independiente y pueden modificarse sin tocar el motor.