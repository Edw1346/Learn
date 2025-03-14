import collections

"""El módulo collections en Python proporciona implementaciones de tipos de datos que ofrecen funcionalidades adicionales 
sobre los tipos básicos de Python, como listas, diccionarios y tuplas. Estos tipos de datos están optimizados para tareas
 específicas y permiten manejar colecciones de manera más eficiente y flexible.

Tipos de datos comunes en collections:

Counter: Una subclase de dict que cuenta la frecuencia de elementos en una colección.
defaultdict: Similar a un diccionario, pero proporciona un valor predeterminado cuando se accede a una clave que no existe
OrderedDict: Un diccionario que recuerda el orden en el que se insertaron los elementos.
namedtuple: Crea tuplas con campos nombrados, lo que las hace más legibles y accesibles por nombre en lugar de por índice.
deque: Una lista optimizada para agregar y eliminar elementos de ambos extremos con eficiencia (cola y pila)."""



"""Funciones del módulo collections:"""

#collections.Counter([iterable-or-mapping]) Crea un contador, que es una subclase de dict diseñada para contar elementos en un iterable o mapeo. Ejemplo:
from collections import Counter 
counter = Counter('abracadabra') 
print(counter) # Contará la frecuencia de cada letra 

#collections.defaultdict(default_factory) Devuelve un diccionario con un valor predeterminado si la clave no existe. El default_factory es una función que define el valor predeterminado (por ejemplo, list, int). Ejemplo:
from collections import defaultdict 
dd = defaultdict(int) 
dd['a'] += 1 
print(dd) # {'a': 1} 

#collections.OrderedDict() Crea un diccionario que recuerda el orden de inserción de las claves. Ejemplo:
from collections import OrderedDict 
ordered_dict = OrderedDict([('a', 1), ('b', 2)])
print(ordered_dict) # {'a': 1, 'b': 2} 

#collections.namedtuple(typename, field_names, ...) Crea una subclase de tupla con campos nombrados, proporcionando acceso a los elementos por nombre en lugar de por índice. Ejemplo:
from collections import namedtuple 
Point = namedtuple('Point', 'x y') 
p = Point(1, 2)
print(p.x, p.y) # 1 2 

#collections.deque([iterable[, maxlen]]) Devuelve una lista doblemente enlazada, más eficiente para agregar y eliminar elementos desde ambos extremos. Ejemplo:
from collections import deque 
d = deque([1, 2, 3])
d.append(4) # Agregar al final 
d.appendleft(0) # Agregar al principio 
print(d) # deque([0, 1, 2, 3, 4]) 

#collections.ChainMap(*maps) Combina varios diccionarios en una sola vista, buscando en cada uno en orden. Ejemplo:
from collections import ChainMap 
dict1 = {'a': 1}
dict2 = {'b': 2} 
cm = ChainMap(dict1, dict2) 
print(cm) # ChainMap({'a': 1}, {'b': 2}) 

#collections.UserDict Una clase base para crear diccionarios personalizados. Permite modificar o extender la funcionalidad de un diccionario. Ejemplo:
from collections import UserDict 
class MyDict(UserDict): 
    def __setitem__(self, key, value): 
        self.data[key] = value * 2 # Almacena el valor duplicado 
        my_dict = MyDict(a=1) 
        print(my_dict['a']) # 2 

#collections.UserList Una clase base para crear listas personalizadas. Permite extender la funcionalidad de una lista. Ejemplo:
from collections import UserList 
class MyList(UserList): 
    def append(self, value): 
        self.data.append(value * 2) 
        my_list = MyList([1, 2]) 
        my_list.append(3)
        print(my_list) # [1, 2, 6] 

#collections.UserString Una clase base para crear cadenas personalizadas. Permite extender la funcionalidad de una cadena. Ejemplo:
from collections import UserString 
class MyString(UserString): 
    def reverse(self): 
        return self.data[::-1] 

my_string = MyString('hello') 
print(my_string.reverse()) # 'olleh' 





"""Clases del módulo collections:"""

#Counter
#Subclase de dict que cuenta la frecuencia de elementos en un iterable. Es útil para contar elementos en listas o cadenas de texto. Ejemplo:
from collections import Counter 
counter = Counter('abracadabra') 
print(counter) # Counter({'a': 5, 'r': 2, 'b': 2, 'c': 1, 'd': 1}) 

#defaultdict
#Subclase de dict que proporciona un valor predeterminado cuando se accede a una clave inexistente, usando una función default_factory.Ejemplo:
from collections import defaultdict 
dd = defaultdict(int) # El valor por defecto será 0 
dd['a'] += 1 
print(dd) # defaultdict(<class 'int'>, {'a': 1}) 

#OrderedDict
#Un diccionario que recuerda el orden de inserción de las claves. A diferencia de un dict normal (que no garantiza el orden de inserción hasta Python 3.7), un OrderedDict conserva el orden en el que se añadieron los elementos. Ejemplo:
from collections import OrderedDict 
ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)]) 
print(ordered_dict) # OrderedDict([('a', 1), ('b', 2), ('c', 3)]) 

#namedtuple
#Crea tuplas con campos nombrados. Es útil cuando necesitas tuplas, pero con nombres para los elementos, lo que mejora la legibilidad del código. Ejemplo:
from collections import namedtuple 
Point = namedtuple('Point', 'x y') 
p = Point(1, 2) 
print(p.x, p.y) # 1 2 

#deque
#Una lista optimizada para agregar y eliminar elementos desde ambos extremos (cola y pila). Es más eficiente que usar listas cuando se realizan muchas operaciones de inserción o eliminación en los extremos. Ejemplo:
from collections import deque 
d = deque([1, 2, 3]) 
d.append(4) # Agrega al final 
d.appendleft(0) # Agrega al principio 
print(d) # deque([0, 1, 2, 3, 4]) 

#ChainMap
#Una clase que combina varios diccionarios en una sola vista. Busca las claves en los diccionarios de izquierda a derecha. Es útil para manejar múltiples contextos (por ejemplo, variables de entorno). Ejemplo:
from collections import ChainMap
dict1 = {'a': 1}
dict2 = {'b': 2}
chain = ChainMap(dict1, dict2) 
print(chain) # ChainMap({'a': 1}, {'b': 2}) 

#UserDict
#Una clase base para crear diccionarios personalizados. Puedes extender esta clase para crear tus propias implementaciones de diccionarios. Ejemplo:
from collections import UserDict 
class MyDict(UserDict):
    def __setitem__(self, key, value): 
        self.data[key] = value * 2 

d = MyDict(a=1) 
print(d['a']) # 2 

#UserList
#Una clase base para crear listas personalizadas. Permite extender la funcionalidad de las listas de Python. Ejemplo:
from collections import UserList 
class MyList(UserList): 
    def append(self, item): 
        self.data.append(item * 2) 

l = MyList([1, 2, 3]) 
l.append(4) 
print(l) # [1, 2, 3, 8] 

#UserString
#Una clase base para crear cadenas personalizadas. Permite extender la funcionalidad de las cadenas de texto. Ejemplo:
from collections import UserString 
class MyString(UserString):
    def reverse(self):
        return self.data[::-1] 
    
s = MyString('hello') 
print(s.reverse()) # 'olleh' 




"""El módulo collections en Python no tiene variables específicas definidas como parte de su API pública. Sin embargo, 
proporciona clases, funciones y tipos de datos especializados que puedes usar para trabajar con colecciones de datos."""



"""El módulo collections no define constantes específicas. Sin embargo, tiene tipos de datos y clases predefinidas que 
permiten manejar colecciones de manera más eficiente. Aunque no hay constantes como tal, algunas clases y estructuras 
de datos del módulo podrían tener comportamientos que puedes considerar "constantes" en su naturaleza, como el valor 
predeterminado de las funciones de defaultdict o los métodos en ciertas clases."""



"""El módulo collections no define excepciones específicas, pero algunas de sus clases pueden generar excepciones 
estándar de Python en ciertas situaciones. Por ejemplo:

KeyError: Puede ser levantada por clases como defaultdict o Counter si intentas acceder a una clave inexistente sin un valor predeterminado.
TypeError: Puede ocurrir si se utilizan tipos incompatibles con las clases de collections, como cuando se intenta modificar un namedtuple.
AttributeError: Puede surgir si se intenta acceder a un atributo que no existe en un tipo de colección, como al intentar acceder a un atributo inexistente en un namedtuple."""



"""El módulo collections no contiene submódulos oficiales. Sin embargo, ofrece una variedad de clases y funciones que 
proporcionan estructuras de datos especializadas."""

