"""Metodos especiales"""
#Son funcionalidad especiales que son diferente a metodos normales

class Persona():
#Init, inicializa el objeto
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

#Representacion del objeto en una cadena
    def __str__(self):
        return F'Persona (nombre={self.nombre}, edad={self.edad})'

#represntar un objeto
    def __repr__(self):
        return f'Persona ("{self.nombre}", {self.edad}, "{self.sexo}", "{self.actividad}")'

#agregar o sumas objetos de esta clases herada
    def __add__(self, otro):
        valor_nuevo = self.edad + otro.edad #manipular datos (sumar edades)
        return Persona(self.edad+otro.edad,valor_nuevo, self.sexo+otro.sexo, self.actividad+otro.actividad) 
    # deben de colocar tosos los atrubitos de la clase

#El __str__
Edwin = Persona("Edwin", 20, "Masculino", "Programacion")
print(Edwin) #Forma de mostrar el objeto en str, en vez de poner un codigo de memoria object at 0x0000000
print(type(Edwin))

#El __Repr__
Lucas = Persona("Lucas", 35, "Masculino", "Electricista")
repre = repr(Lucas) #Pasa a un str
print(type(repre))
result = eval(repre) #Pasa a un objeto, este trasforma el str del objeto a un objeto
#Debe de respetar los tipos de datos: "str", float 1.2
print(type(result))

#El __add__
Maria = Persona("Maria", 23, "Famenino", "Contador")
Pedro = Persona("Pedro", 30, "Masculino", "Obrero")
Carlos = Persona("Carlos", 43, "Masculino", "Fontanero")

Nueva_persona = Maria + Pedro #Sumar objetos
print(Nueva_persona)
print(type(Nueva_persona))




"""TIPOS DE METODOS ESPECIALES"""

"""
1. __init__(self, ...): Constructor, se llama al crear una nueva instancia de la clase.
2. __new__(cls, ...): Crea una nueva instancia de la clase antes de inicializarla.
3. __del__(self): Destructor, se llama antes de que el objeto sea destruido.
4. __repr__(self): Representación oficial del objeto (para desarrolladores).
5. __str__(self): Representación amigable del objeto (para usuarios).
6. __bytes__(self): Convierte el objeto a una representación de bytes.
7. __format__(self, format_spec): Define cómo formatear el objeto con format().
8. __hash__(self): Devuelve un valor hash del objeto, usado en colecciones como set o dict.
9. __eq__(self, other): Define el comportamiento de igualdad (==).
10. __ne__(self, other): Define el comportamiento de desigualdad (!=).
11. __lt__(self, other): Define el comportamiento de menor que (<).
12. __le__(self, other): Define el comportamiento de menor o igual (<=).
13. __gt__(self, other): Define el comportamiento de mayor que (>).
14. __ge__(self, other): Define el comportamiento de mayor o igual (>=).
15. __bool__(self): Define el valor de verdad del objeto (bool(objeto)).
16. __call__(self, ...): Hace que una instancia de clase sea "llamable" como una función.
17. __getitem__(self, key): Define el comportamiento para acceder con índices (objeto[key]).
18. __setitem__(self, key, value): Define el comportamiento para asignar valores con índices (objeto[key] = valor).
19. __delitem__(self, key): Define el comportamiento para eliminar valores con índices (del objeto[key]).
20. __len__(self): Define el comportamiento de len(objeto).
21. __contains__(self, item): Define el comportamiento de item in objeto.
22. __iter__(self): Devuelve un iterador para el objeto.
23. __next__(self): Devuelve el siguiente elemento en un iterador.
24. __reversed__(self): Define el comportamiento de reversed(objeto).
25. __add__(self, other): Define el comportamiento de la suma (+).
26. __sub__(self, other): Define el comportamiento de la resta (-).
27. __mul__(self, other): Define el comportamiento de la multiplicación (*).
28. __truediv__(self, other): Define el comportamiento de la división (/).
29. __floordiv__(self, other): Define el comportamiento de la división entera (//).
30. __mod__(self, other): Define el comportamiento del módulo (%).
31. __pow__(self, other): Define el comportamiento de la potenciación (**).
32. __lshift__(self, other): Define el comportamiento del desplazamiento a la izquierda (<<).
33. __rshift__(self, other): Define el comportamiento del desplazamiento a la derecha (>>).
34. __and__(self, other): Define el comportamiento del AND bit a bit (&).
35. __or__(self, other): Define el comportamiento del OR bit a bit (|).
36. __xor__(self, other): Define el comportamiento del XOR bit a bit (^).
37. __invert__(self): Define el comportamiento del NOT bit a bit (~).
38. __radd__(self, other): Define el comportamiento de la suma inversa (cuando other + self se evalúa y other no lo soporta).
39. __iadd__(self, other): Define el comportamiento de la suma en asignación (+=).
40. __isub__(self, other): Define el comportamiento de la resta en asignación (-=).
41. __imul__(self, other): Define el comportamiento de la multiplicación en asignación (*=).
42. __itruediv__(self, other): Define el comportamiento de la división en asignación (/=).
43. __ifloordiv__(self, other): Define el comportamiento de la división entera en asignación (//=).
44. __imod__(self, other): Define el comportamiento del módulo en asignación (%=).
45. __ipow__(self, other): Define el comportamiento de la potenciación en asignación (**=).
46. __ilshift__(self, other): Define el comportamiento del desplazamiento a la izquierda en asignación (<<=).
47. __irshift__(self, other): Define el comportamiento del desplazamiento a la derecha en asignación (>>=).
48. __iand__(self, other): Define el comportamiento del AND en asignación (&=).
49. __ior__(self, other): Define el comportamiento del OR en asignación (|=).
50. __ixor__(self, other): Define el comportamiento del XOR en asignación (^=).
51. __enter__(self): Define el comportamiento al entrar en un contexto (with).
52. __exit__(self, exc_type, exc_value, traceback): Define el comportamiento al salir de un contexto (with).
53. __index__(self): Define cómo convertir el objeto en un índice entero (usado en objeto[índice]).
54. __round__(self, n): Define el comportamiento de round(objeto, n).
55. __trunc__(self): Define cómo truncar el objeto (math.trunc(objeto)).
56. __floor__(self): Define cómo redondear hacia abajo (math.floor(objeto)).
57. __ceil__(self): Define cómo redondear hacia arriba (math.ceil(objeto)).


class MiClase:
    # 1. __init__
    def __init__(self, atributo):
        self.atributo = atributo

    # 2. __new__
    def __new__(cls, *args, **kwargs):
        instancia = super().__new__(cls)
        return instancia

    # 3. __del__
    def __del__(self):
        print("El objeto se está destruyendo.")

    # 4. __repr__
    def __repr__(self):
        return f"MiClase({self.atributo})"

    # 5. __str__
    def __str__(self):
        return f"Este es un objeto con atributo: {self.atributo}"

    # 6. __bytes__
    def __bytes__(self):
        return bytes(str(self.atributo), encoding='utf-8')

    # 7. __format__
    def __format__(self, format_spec):
        return f"El atributo es {self.atributo:{format_spec}}"

    # 8. __hash__
    def __hash__(self):
        return hash(self.atributo)

    # 9. __eq__
    def __eq__(self, other):
        return self.atributo == other.atributo

    # 10. __ne__
    def __ne__(self, other):
        return self.atributo != other.atributo

    # 11. __lt__
    def __lt__(self, other):
        return self.atributo < other.atributo

    # 12. __le__
    def __le__(self, other):
        return self.atributo <= other.atributo

    # 13. __gt__
    def __gt__(self, other):
        return self.atributo > other.atributo

    # 14. __ge__
    def __ge__(self, other):

        return self.atributo >= other.atributo

    # 15. __bool__
    def __bool__(self):
        return bool(self.atributo)

    # 16. __call__
    def __call__(self, *args, **kwargs):
        print("Este objeto es llamado como una función.")

    # 17. __getitem__
    def __getitem__(self, key):
        return f"Accediendo al índice {key}"

    # 18. __setitem__
    def __setitem__(self, key, value):
        print(f"Asignando {value} al índice {key}")

    # 19. __delitem__
    def __delitem__(self, key):
        print(f"Eliminando el índice {key}")

    # 20. __len__
    def __len__(self):
        return 42  # Ejemplo de longitud arbitraria

    # 21. __contains__
    def __contains__(self, item):
        return item == "permitido"

    # 22. __iter__
    def __iter__(self):
        return iter([1, 2, 3])  # Ejemplo con una lista

    # 23. __next__
    def __next__(self):
        raise StopIteration  # Ejemplo básico

    # 24. __reversed__
    def __reversed__(self):
        return reversed([1, 2, 3])  # Ejemplo con una lista

    # 25. __add__
    def __add__(self, other):
        return f"Suma entre {self} y {other}"

    # 26. __sub__
    def __sub__(self, other):
        return f"Resta entre {self} y {other}"

    # 27. __mul__
    def __mul__(self, other):
        return f"Multiplicación entre {self} y {other}"

    # 28. __truediv__
    def __truediv__(self, other):
        return f"División entre {self} y {other}"

    # 29. __floordiv__
    def __floordiv__(self, other):
        return f"División entera entre {self} y {other}"

    # 30. __mod__
    def __mod__(self, other):
        return f"Módulo entre {self} y {other}" """