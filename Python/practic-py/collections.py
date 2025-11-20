import collections

"""El módulo collections proporciona implementaciones de tipos de datos que ofrecen funcionalidades adicionales sobre los tipos básicos de Python, como listas, diccionarios y tuplas."""

"""Tipos de datos comunes en collections:
Counter: Una subclase de dict que cuenta la frecuencia de elementos en una colección.
defaultdict: Similar a un diccionario, pero proporciona un valor predeterminado cuando se accede a una clave que no existe
OrderedDict: Un diccionario que recuerda el orden en el que se insertaron los elementos.
namedtuple: Crea tuplas con campos nombrados, lo que hace más legibles y accesibles por nombre en lugar de por índice.
deque: Una lista optimizada para agregar y eliminar elementos de ambos extremos con eficiencia (cola y pila)."""


"""Funciones del módulo collections"""

##collections.Counter([iterable-or-mapping]) Crea un contador, que es una subclase de dict diseñada para contar elementos en un iterable o mapeo:
counter = collections.Counter("Edwin")
print(counter) # Contará la frecuencia de cada letra: Counter({'a': 5, 'r': 2, 'b': 2, 'c': 1, 'd': 1}) 

#collections.defaultdict(default_factory). Devuelve un diccionario con un valor predeterminado si la clave no existe. El default_factory es una función que define el valor predeterminado (por ejemplo, list, int). Ejemplo:
dd = collections.defaultdict(int) # El valor por defecto será 0 
le = ["Edwin", "Josue","Casey", "Yuri","Leslie", "Diana"]
for let in le:
    dd[let] += 1 
print(dd, dd[8]) # defaultdict(<class 'int'>, {'a': 1})  

#collections.OrderedDict() Crea un diccionario que recuerda el orden de inserción de las claves:
ordered_dict = collections.OrderedDict([('a', 1), ('b', 2)])
print(ordered_dict) # {'a': 1, 'b': 2} 
# OrderedDict([('a', 1), ('b', 2), ('c', 3)]) 

#collections.namedtuple(typename, field_names, ...). Crea una subclase de tupla con campos nombrados, proporcionando acceso a los elementos por nombre en lugar de por índice:
Point = collections.namedtuple('Point', 'x y') 
p = Point(1, 2)
print(p.x, p.y) # 1 2 

#collections.deque([iterable[, maxlen]]) Devuelve una lista doblemente enlazada, más eficiente para agregar y eliminar elementos desde ambos extremos:
d = collections.deque([1, 2, 3])
d.append(4) # Agregar al final 
d.appendleft(0) # Agregar al principio 
print(d, d[3]) # deque([0, 1, 2, 3, 4]) 

#collections.ChainMap(*maps) Combina varios diccionarios en una sola vista, buscando en cada uno en orden:
dict1 = {'a': 1, 'b':3}
dict2 = {'a': 2, 'b':4} 
cm = collections.ChainMap(dict1, dict2) 
print(cm,cm["b"]) # ChainMap({'a': 1}, {'b': 2}) 

#collections.UserDict Una clase base para crear diccionarios personalizados. Modificar o extender funcionalidad de un diccionario. Combina varios diccionarios en una sola vista. Busca las claves en los diccionarios de izquierda a derecha. 
class MyDict(collections.UserDict): 
    def __setitem__(self, key, value): self.data[key] = value * 2 # Almacena el valor duplicado 

my_dict = MyDict(a=1) 
print(my_dict['a']) # 2 

#collections.UserList Una clase base para crear listas personalizadas. Permite extender la funcionalidad de una lista:
class MyList(collections.UserList): 
    def append(self, value): self.data.append(value * 2) 

my_list = MyList([1, 2]) 
my_list.append(3)
print(my_list) # [1, 2, 6] 

#collections.UserString Clase base para crear cadenas personalizadas. Permite extender la funcionalidad de una cadena:
class MyString(collections.UserString): 
    def reverse(self): return self.data[::-1] 

my_string = MyString('hello') 
print(my_string.reverse()) # 'olleh' 


#El módulo collections no contiene submódulos. Ofrece una variedad de clases y funciones que proporcionan estructuras de datos especializadas.