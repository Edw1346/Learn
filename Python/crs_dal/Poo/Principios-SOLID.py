#Practicas y tecnicas para software que sean mantenibles, modificable, escalables:
#Mantenibilidad: facil de maneter y modificable, debe de ser organizado, con un estracutura clara y buenas practica, si se va amodificar sea facil
#Reutilizable = Reusar codigo, que sus componentes debe de volver usarse
#Legibilidad =  Que sea entendible, que este documentado, con variable de nombres logicos, con un codigo de estilo
#Extensibles = Extendenser sin afectar el codigo principal

"""PRINCIPIOS SOLID
S -> SRP: SRP SINGLE, RESPONSABILITY PRINCIPLE: PRINCIPIO DE RESPONSABILIDAD UNICA
O -> OCP: :PRINCIPIO DE ABIERTO/CERRADO
L -> LSP: : PRINCIPIO DE SUSTITUCION DE LISKOV
I -> ISP: : PRINCIPIO DE SEGREGACION DE INTERFAZ
D -> DIP: : PRINCIPIO DE INVERSION DE DEPENDENCIA     """





"""1° Primer principio: SRP SINGLE, RESPONSABILITY PRINCIPLE"""
#Que cada funcion o clase cumpla una funcion, no varias, y solo hacerlo en casos importantes

class Tanque(): #Crear esta clase para colocarla como parametro en el objeto
    def __init__(self, combustible):
        self.combustible = 100 + combustible
    
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= (cantidad/2)

    def poner_combustible(self, cantidad):
        self.combustible += cantidad

class Auto():
    def __init__(self, tanque): #Ingresar la clase como parametro
        self.posicion = 0
        self.tanque = tanque

    def moverse(self, distancia):
        if self.tanque.obtener_combustible() > (distancia /2): # Atributo de la clase.funcion() para funciones de otra clase
            self.tanque.usar_combustible(distancia)
            self.posicion += (distancia) 
            print(f"Te moviste {self.posicion} metros")
        else:
            print("No hay combustible necesario")

    def posicionamiento(self):
        print(self.posicion)

Tanques= Tanque(50)
carro = Auto(Tanques) #colocar el objeto Tanques como parametro en el Objeto Auto y acceder a sus funciones dentro de Auto

print(f"Tanque = {Tanques.obtener_combustible()}")
carro.moverse(10)
carro.posicionamiento()
print(f"Tanque = {Tanques.obtener_combustible()}")
carro.moverse(100)
carro.posicionamiento()
print(f"Tanque = {Tanques.obtener_combustible()}")
carro.moverse(40)
carro.posicionamiento()
print(f"Tanque = {Tanques.obtener_combustible()}")
carro.moverse(140)
print(f"Tanque = {Tanques.obtener_combustible()}")
carro.moverse(10)
print(f"Tanque = {Tanques.obtener_combustible()}")
carro.moverse(10)
print(f"Tanque = {Tanques.obtener_combustible()}")
Tanques.poner_combustible(30)
print(f"Tanque = {Tanques.obtener_combustible()}")

"""Cumplimiento del principio SRP: Usar una clase para una tarea especifica, Auto es una clase con sus metodos 
y aunque se puede añadir los metodos de tanque, es mejor hacer otra clase que lleve esas tareas que son diferentes
a alas de carro"""



"""2° PRINCIPIO: ORP,  OPEN/CLOSE PRINCIPLE"""

#Open for extension: Las entidades de software (clases, metodos, funciones, modulos, etc) tienen que estar abierta para la extension
#Close modify: Pero cerradas para la modificacion
#O sea poder agregar funcionalidad sin teener que modificar el codigo fuente de esta clase


class Usuario():
    def __init__(self, nom_usuario, email, sms, telefono):
        self.nombre = nom_usuario
        self.email = email
        self.sms = sms
        self.telefono = telefono

    def presentarse(self):
        print(f"Soy {self.nombre}")

class Notificacion():
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError  #Esto avisa de que no se debe de modifica (Close modify)

class NotifiEmail(Notificacion): #Que herede la clase que desea copiar sus funcionalidades
    def __init__(self, usuario, mensaje):
        super().__init__(mensaje)
        self.usuario = usuario

    def notificar(self): #Acceder a sus funcionalidad y modificarlas (Open for extension)
        print(f"Mensaje por Email a {self.usuario.nombre}: {self.mensaje}")

class NotifiSms(Notificacion): #Que herede la clase que desea copiar sus funcionalidades
    def __init__(self, usuario, mensaje):
        super().__init__(mensaje)
        self.usuario = usuario

    def notificar(self): #Acceder a sus funcionalidad y modificarlas (Open for extension)
        print(f"Mensaje por SMS a {self.usuario.nombre}: {self.mensaje}")

class NotifiWhasapp(Notificacion): #Que herede la clase que desea copiar sus funcionalidades    
    def __init__(self, usuario, mensaje):
        super().__init__(mensaje)
        self.usuario = usuario
        

    def notificar(self): #Acceder a sus funcionalidad y modificarlas (Open for extension)
        print(f"Mensaje por WhasApp a {self.usuario.nombre}: {self.mensaje}")

Edwin = Usuario("Edwin","edwin@gmail.com","edwin",72892522)
NotEmail = NotifiEmail(Edwin, "Hola")
NotSms = NotifiSms(Edwin, "Hola")
NotWhat = NotifiWhasapp(Edwin, "Hola")

NotEmail.notificar()
NotSms.notificar()
NotWhat.notificar()

"""3° LSP, LISKOV'S SUBTITUTION PRINCIPLE"""
#Las clases derivdas son sustituble por sus clases bases:
#Si clase B essubclase de clase A, entonces clase A puede utilizarse en todos donde clase B tambien se utiliza
#Una subclase debe hacer TODO lo que la clase base tenga (atributos, metodos, etc)
#Si una subclase hace cosas diferente que su clase base, se debe de hacer mas super clase

class Ave(): #Clase base
    def __init__(self, especie):
        self.especie = especie

class AveVoladora(Ave): #Una subclase que herede de la clase base, pero difiera a otros por sus metodos
    def __init__(self, especie): 
        super().__init__(especie) #Hereda de la clase base

    def volar(self): #Funcion de acuedo con la clase
        print("Puedo volar")

class AveNoVoladora(Ave): #Una subclase que herede de la clase base, pero difiera a otros por sus metodos
    def __init__(self, especie):
        super().__init__(especie) #Hereda de la clase base
    
    def volar(self): #Funcion de acuedo con la clase
        print("No puedo volar")

Tucan = AveVoladora("Tucan")
Pinguino = AveNoVoladora("Pinguino")

Pinguino.volar()
Tucan.volar()





"""4° ISP, INTERFACE SEGREGATION PRINCIPLE"""
#Ningun cliente tiene que ser forzado a no depender de interfaces que no utilice o usa
#En Python no hay una interfaz implicita o fija (clases con sus metodos)
#Esto es aplicable en clases abstractas

from abc import ABC, abstractmethod

#Clases abstractas obligar a las hijas a tener las mismos metodos, todos los metodos se tienen que usar
#Pero si van a crear instancias que no necesitan ciertos metodos, se tiene que hacer otras tecnicas

class Comedor(): #Esta clase pasa todos sus metodos
    @abstractmethod
    def comer(self):
        pass

class Trabajador(): #Esta clase pasa todos sus metodos
    @abstractmethod
    def trabajar(self):
        pass
    
class Durmiente(): #Esta clase pasa todos sus metodos
    @abstractmethod
    def dormir(self):
        pass

class Humano(Comedor, Trabajador, Durmiente): #Se agregan todas las clases abstractas con las funcionalidad que Si van a usar
    def comer(self):
        print("Estoy comiendo")

    def trabajar(self):
        print("Estoy trabajando")

    def dormir(self):
        print("Estoy durmiendo")

class Robot(Trabajador): #Se agregan todas las clases abstractas con las funcionalidad que Si van a usar
    def trabajar(self):
        print("Estoy trabajando")

Human = Humano()
Robott = Robot()

Human.comer()
Human.trabajar()
Human.dormir()

Robott.trabajar()

#Se divide las clases segun sus metodos, no se quiere introducir metodos a objetos que no deben de tenerlos
#Ya que las clases abstractas obligar a usar los metodos, aunque no concuerden con el objetivo de la clase hija


"""5° DIP, DEPENDENCY INVERSION PRINCIPLE"""
#1: Las modulos de alto nivle no tiene que depender de los de bajo nivel, sino que los 2 deden de depender de las Abstraciones
#2: Que las abstracciones no depender de los detalles sino que los detalles (implementacion de la clase) depende de las abstraciones
#Sino depender de interfaces mas complejas, que las clase de alto nivel(las que tiene la logica compleja) no dependan de las de bajo (hacen tareas especificas)
#Clase complejas y grandes no debem de depender de clases pequeña, lo muy importante no depende de algo importante

#from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):          #Clase principal, alto nivel
    @abstractmethod
    def verificar_palabra(self, palabra):       
        pass 

class Dicionario(VerificadorOrtografico):   #Clase segundaria
    def verificar_palabra(self, palabra):
        #Logica para verificar palabrasi esta en el diccionario

class CorrectorOrtografico():  #Clase de bajo nivel
    def __init__(self, verificador):
        self.verificador = verificador

    def corregir_texto(self, texto):
        #Usamos el verificador para corregir texto

corrector = CorrectorOrtografico(Dicionario())
#La clase (CorrectorOrtografico) que es de bajo nievl depende de la clase (Diccionario)
#Esta depende de VerificadorOrtografico la principal una clase mas compleja 


"""Recomendaciones: Lo mejor es el equilibrio, lo mas optimo es que en lo mas posible, lo mejor es seguir los 
principios de SOLID, pero en ocasiones talvez hay que saltarse algunos"""