"""Herencia"""
#Herencia es la capacidad de crear una nueva clase a partir de una clase existente

#Clase padre es la clase que posee los atributos y metodos que se van a heredar
#Clase hija es la clase que hereda los atributos y metodos de la clase padre

#La superclase es la clase que se hereda
#La subclase es la clase que hereda

class Padre:
    #Metodo __init__ es un metodo especial que se ejecuta al instanciar la clase
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    #Metodo de la clase, que es una funcion que se ejecuta al llamar al metodo en el objeto
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años y soy {self.nacionalidad}.")

padre1 = Padre("Carlos", 50, "Chileno") #Instanciar la clase padre a un objeto
print(padre1.nombre) #Imprimir el atributo nombre de la clase padre
print(padre1.saludar()) #Llamar al metodo saludar de la clase padre

class Madre:
    #Metodo __init__ es un metodo especial que se ejecuta al instanciar la clase
    def __init__(self, nombre, edad, nacionalidad, cualidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.cualidad = cualidad

    #Metodo de la clase, que es una funcion que se ejecuta al llamar al metodo en el objeto
    def Hablar(self):
        print(f"Estoy hablando")

madre1 = Madre("Ana", 45, "Peruana", "Responsable") #Instanciar la clase madre a un objeto
print(madre1.nombre) #Imprimir el atributo nombre de la clase madre
print(madre1.Hablar()) #Llamar al metodo trabajar de la clase madre

#hijo
class Hijos(Padre): #Clase hijo2 hereda los atributos y metodos de la clase Padre
    #Este __init__ sobreescribe el metodo __init__ de la clase Padre para agregar un nuevo atributo
    #Cada atributos de la clase Padre y el atributo hijo se tienen que pasar como parametros
    def __init__(self, nombre, edad, nacionalidad, hijo, cualidades): 
    
    #super() es una funcion que llama a la clase padre y hereda los atributos especificados de la clase padre
        super().__init__(nombre, edad, nacionalidad) 
    #Despues de super() se pueden agregar los atributos personalizados de la clase hijo
        self.hijo = hijo
        self.cualidades = cualidades

    def saludar(self): #Se puede sobreescribir los metodos de la clase padre
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

hijo1 = Hijos("Pedro", 30, "Boliviano", "Primogenito", "Responsable") #Instanciar la clase hijo2 a un objeto
print(hijo1.nombre) #Imprimir el atributo nombre de la clase hijo2
print(hijo1.saludar()) #Llamar al metodo trabajar de la clase hijo2 heredado de la clase padre

#Dependencia jerarjica, es cuando una clase hereda de otra clase



"""Herencia multiple"""

#Herencia multiple, es cuando una clase hereda de mas de una clase
class Nietos(Padre, Madre): #Clase nieto hereda los atributos y metodos de la clase Padre y clase Madre
    def __init__(self, nombre, edad, nacionalidad, cualidad, jerarquia, caracteristicas):
    #En ves de super, se llama a la clase que se quiere heredar y los atributos a heredar
        Padre.__init__(self, nombre, edad, nacionalidad) #Se heredan los atributos
        Madre.__init__(self, nombre, edad, nacionalidad, cualidad) #Se heredan los atributos de la clase hijo
        self.jerarquia = jerarquia
        self.caracteristicas = caracteristicas
    
    def estudiar(self): #Se puede agregar metodos personalizados a la clase nieto
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
        
nieto1 = Nietos("Juan", 30, "Peruano", "Responsable", "Primogenito", "Inteligente") #Instanciar la clase nieto a un objeto
print(nieto1.nombre) #Imprimir el atributo nombre de la clase nieto
print(nieto1.saludar()) #Llamar al metodo presentar de la clase nieto

herencia = issubclass(Hijos, Padre) #issubclass es una funcion que verifica si una clase hereda de otra clase
print("Hijos hereda de Padre: ", herencia)

herencia2 = issubclass(Nietos, Padre) #issubclass es una funcion que verifica si una clase hereda de otra clase
print("Nietos hereda de Padre: ", herencia2)


"""Metodo MRO"""
#MRO es el orden en que se ejecutan los metodos de las clases en la herencia multiple

class A():
    def habla(self):
        print("Llamo de la clase A")

class B(A):
    def habla(self):
        print("Llamo de la clase B")

class C(A):
    def habla(self):
        print("Llamo de la clase C")

class D(B,C):
    def habla(self):
        print("Llamo de la clase D")

class E:
    def habla(self):
        print("Llamo de la clase E")

d = D()
d.habla()

print("MRO de E: ", D.mro()) #MRO es una funcion que muestra el orden

#Se puede llamar a un metodo de una clase especifica
C.habla(d) #Se llama al metodo habla de la clase C del objeto d