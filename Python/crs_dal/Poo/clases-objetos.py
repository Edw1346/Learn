"""Conceptos"""

"""POO: Pogramacion orientada a objetos, es un paradigma de programacion que usa objetos que representan 
entidades del mundo real o cosas y sus interacciones para modelar y resolver problemas"""

"""La POO se basa en 4 conceptos fundamentales:
Clases: son los modelos que se utilizan para crear objetos que representan una entidad con propiedades (atributos) y comportamientos (metodos) especificas
Objetos: son las instancias de una clase
Atributos: son las caracteristicas de un objeto
Metodos: son las acciones que un objeto puede realizar"""

"""La Poo se centra en el encapsulamiento, la herencia, el polimorfismo y el abstraccion y modularidad
Encapsulamiento: es la capacidad de ocultar los detalles de implementacion de un objeto y mostrar solo los detalles necesarios para interactuar con el
Herencia: es la capacidad de crear una nueva clase a partir de una clase existente
Polimorfismo: es la capacidad de una clase de comportarse como otra clase
Abstraccion: es la capacidad de modelar entidades del mundo real como objetos
Modularidad: es la capacidad de dividir un programa en modulos o clases que pueden"""



"""Crear un clase y un objeto"""
#Podemos colocar el nombre de las clase con pascales case, ejemplo: MiClase
class PrimeraClase:
    propiedad1 = "Hola"     #Propiedades estaticas, caracteristicas de la clase
    propiedad2 = "Mundo"
    propiedad3 = 2024

clase1 = PrimeraClase() #Instanciar la clase a un objeto, llmada clase1
print(clase1.propiedad1) #Imprimir la propiedad1 de la clase1

clase2 = PrimeraClase() #Instanciar la clase a un objeto, llmada clase2
print(clase2.propiedad3) #Imprimir la propiedad3 de la clase2

#atributos estaticos, son caracteristicas de la clase, por lo que se pueden acceder sin instanciar la clase
#instanciar una clase es al momento de crear un objeto de la clase
#Cada vez que sea haga un objeto de la clase, los atributos son fijos, no se pueden modificar

"""Atributos de la clase"""
#Darle atributos personalizados: atributos de instancia
#Atributos de instancia son caracteristicas de un objeto, que se pueden modificar al instanciar la clase

#Metodos son funciones dentro de una clase
class SegundaClase:
    #Metodo __init__ es un metodo especial que se ejecuta al instanciar la clase    
    def __init__(self, nombre, edad, ciudad): 
    #parametros de la clase: self es un parametro obligatorio que signfica que se refiere a la instancia de la clase
    #Luego se pueden agregar parametros personalizados, que sean los atributos de la clase
        self.nombre = nombre 
        self.edad = edad
        self.ciudad = ciudad
    #Lo que va despes del self. es el nombre del atributo de la clase y no de la clase 
    #lo que va despues del = es el parametro de la clase

#Instanciar la clase a un objeto, llmada clase3 con atributos personalizados
Clase3 = SegundaClase("Juan", 30, "Lima") 
print(Clase3.nombre) #Imprimir el atributo nombre de la clase3
print(Clase3.ciudad) #Imprimir el atributo ciudad de la clase3

Clase4 = SegundaClase("Carlos", 25, "Buenos Aires") 
print(Clase4.nombre) #Imprimir el atributo nombre de la clase4
print(Clase4.ciudad) #Imprimir el atributo ciudad de la clase4 


"""Metodos de la clase"""

#Metodos son funciones dentro de una clase, acciones que un objeto puede realizar
class TerceraClase:
    #Funcion __init__ es un metodo especial que se ejecuta al instanciar la clase
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    #Metodo de la clase, que es una funcion que se ejecuta al llamar al metodo en el objeto
    def saludar(self): #parametro self es obligatorio porque se refiere a la instancia de la clase
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años. Vivo en {self.ciudad}")

clase5 = TerceraClase("Ana", 18, "Bogota")
print(clase5.nombre) #Imprimir el atributo nombre de la clase5
clase5.saludar() #Llamar al metodo saludar de la clase5

#El parametro self es obligatorio en los metodos de la clase, porque se refiere a la instancia de la clase
#Ya que los metodos de la clase se ejecutan en los objetos de la clase, se tiene que referiarse a la clase
