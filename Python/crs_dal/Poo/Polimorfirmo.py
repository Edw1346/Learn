"""Polimorfismo"""
#El polimorfismo es la capacidad de un objeto de tomar diferentes formas. 
#En Python, el polimorfismo se logra mediante el uso de métodos con el mismo nombre en diferentes clases.


"""Polimorfismo con clases"""
#Cuando se llama a un método en un objeto y se ejecuta un método diferente dependiendo del objeto.

class Gato:
    def sonido(self): # Método de sonido de gato
        return "Miau"

class Perro:
    def sonido(self): # Método de sonido de perro
        return "Guau"
    
Gato = Gato()
Perro = Perro()

print(Gato.sonido())
print(Perro.sonido())


"""Polimorfismo con funciones"""
#Cuando se pasa un objeto como argumento a una función y se llama a un método en ese objeto.

def sonido(animal):
    return animal.sonido()

"""Polimorfismo con herencia (inclusion, sobreescritura)"""
#Cuando una clase hereda de otra clase y reemplaza un método de la clase base con un método diferente.

class Animal: # Clase base
    def sonido(self): # Método de sonido de animal
        pass # Método abstracto, para ser reemplazado en las subclases

class Gato1(Animal): # Clase derivada
    def sonido(self): # Método de sonido de gato
        return "Miau" # Reemplaza el método de la clase base
    
class Perro2(Animal): # Clase derivada
    def sonido(self): # Método de sonido de perro
        return "Guau" # Reemplaza el método de la clase base
    

"""Polimorfismo de sobrecarga"""
#Cuando se define un método con el mismo nombre pero con diferentes parámetros.

class Calculadora:
    def suma(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            return a + b + c
        elif a != None and b != None:
            return a + b
        else:
            return a
        
calculadora = Calculadora()
print(calculadora.suma(1, 2))

#En Python, el polimorfismo de sobrecarga no es muy común, ya que Python no admite la sobrecarga de métodos.

"""Poliformismo de coersión"""
#Cuando se convierte un objeto de una clase en un objeto de otra clase.

class Gato3:
    def sonido(self): # Método de sonido de gato
        return "Miau"
    
class Perro3:
    def sonido(self): # Método de sonido de perro
        return "Guau"
    
class GatoPerro:
    def sonido(self, animal): # Método de sonido de gato o perro
        return animal.sonido()
    
gato = Gato3()
perro = Perro3()
gato_perro = GatoPerro()

print(gato_perro.sonido(gato))
print(gato_perro.sonido(perro))

"""Conceptos importantes"""
#Duck typing: "Si suena como un pato y camina como un pat, entonces es un pato", es decir, Python no se preocupa por el tipo de objeto, sino por los métodos y atributos que tiene.
#Enlaces dinámicos: Python enlaza los métodos en tiempo de ejecución, lo que permite el polimorfismo, es decir, que un objeto pueda tomar diferentes formas.
#Enlaces estáticos: En otros lenguajes, como C++, los métodos se enlazan en tiempo de compilación, lo que limita el polimorfismo, es decir, que un objeto pueda tomar diferentes formas.

#Tipo real: El tipo de objeto real en tiempo de ejecución, es decir, el tipo de objeto al que se refiere una variable.
#Tipo declarado: El tipo de objeto declarado en tiempo de compilación, es decir, el tipo de variable, es decir, el tipo de variable.

#Sobrecarga de operadores: Permite definir el comportamiento de los operadores en clases personalizadas.

