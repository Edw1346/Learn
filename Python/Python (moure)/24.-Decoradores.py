"""Decoradores 
Un decorador es una función que toma otra función como argumento y devuelve una nueva función que generalmente extiende o modifica el comportamiento de la original."""
def decorador(func): 
    def envoltura(): 
        print("Antes de ejecutar la función.") 
    func() 
    print("Después de ejecutar la función.")
    return envoltura 

"""Uso básico de un decorador: Para aplicar un decorador a una función, se utiliza la sintaxis de @decorador encima de la definición de la función a decorar."""
@decorador 
def mi_funcion(): 
    print("Estoy dentro de la función.") 
mi_funcion() 

"""La salida de este código sería:
Antes de ejecutar la función. Estoy dentro de la función. Después de ejecutar la función. 

Decoradores con parámetros: Si deseas que el decorador acepte parámetros adicionales, puedes anidar funciones de manera que los parámetros sean pasados correctamente."""
def decorador_con_parametros(param):
    def decorador(func): 
        def envoltura(*args, **kwargs): 
            print(f"Antes de ejecutar {param}.") 
            result = func(*args, **kwargs) 
            print(f"Después de ejecutar {param}.") 
            return result 
        return envoltura
    return decorador 

#Y su uso sería:
@decorador_con_parametros("mi_funcion")
def mi_funcion():
    print("Ejecutando mi función.") 
mi_funcion() 

#Esto imprimirá: Antes de ejecutar mi_funcion. Ejecutando mi función. Después de ejecutar mi_funcion. 

#Decoradores con retorno de valores: Los decoradores no solo pueden modificar el comportamiento, sino también alterar el valor retornado de la función decorada.
def decorador(func): 
    def envoltura(*args, **kwargs):
        result = func(*args, **kwargs) 
        return f"Resultado modificado: {result}" 
    return envoltura 

@decorador
def suma(a, b): 
    return a + b
print(suma(2, 3)) # Imprimirá: Resultado modificado: 5 

"""Tipos de Decoradores

Decoradores estándar: Los decoradores simples son los que hemos visto en los ejemplos anteriores. A menudo, son útiles para modificar el comportamiento de funciones sin necesidad de cambiar su código fuente.


Decoradores de funciones con parámetros: Los decoradores que toman parámetros adicionales, como hemos visto en el ejemplo de decorador_con_parametros. Estos permiten personalizar aún más la funcionalidad del decorador.

Decoradores para métodos de clases: Los decoradores también se pueden aplicar a métodos dentro de clases, para modificar su comportamiento. Uno de los más comunes es @staticmethod y @classmethod."""

class MiClase: 
    @staticmethod
    def metodo_estatico(): 
        print("Método estático") 

    @classmethod 
    def metodo_clase(cls): 
        print(f"Método de clase: {cls}") 

MiClase.metodo_estatico()
MiClase.metodo_clase() 

"""Decoradores de clases: Los decoradores pueden ser aplicados a clases para modificar su comportamiento. Un decorador de clase generalmente toma una clase como argumento y devuelve una nueva clase modificada."""
def decorador_de_clase(cls): 
    cls.nueva_funcion = lambda self:  
    "Método agregado por decorador" 
    return cls 

@decorador_de_clase 
class MiClase: 
    def metodo(self):
        return "Método original" 

mi_objeto = MiClase() 
print(mi_objeto.metodo()) # Método original 
print(mi_objeto.nueva_funcion()) # Método agregado por decorador 

"""Decoradores Comunes"""

#@staticmethod: Se utiliza para definir un método estático en una clase, que no requiere acceso a la instancia ni a los atributos de la clase.
class MiClase: 
    @staticmethod 
    def metodo_estatico(): 
        print("Método estático") 

#@classmethod: Se utiliza para definir un método de clase, que toma la clase como primer argumento en lugar de una instancia.
class MiClase: 
    @classmethod 
    def metodo_clase(cls): 
        print(f"Clase: {cls}") 

#@property: Es un decorador para definir métodos que se comportan como atributos. Esto es útil cuando quieres controlar el acceso a los atributos de una clase, aplicando lógicas como validaciones antes de asignar un valor.
class MiClase: 
    def __init__(self, valor): 
        self._valor = valor 

@property 
def valor(self):
    return self._valor

@valor.setter 
def valor(self, valor):
    if valor < 0: 
        raise ValueError("El valor no puede ser negativo.")
    self._valor = valor 

#Este decorador permite que valor sea tratado como si fuera un atributo, pero sigue siendo un método.

#@functools.lru_cache: Este decorador sirve para memoización, es decir, guarda los resultados de las funciones que ya se han ejecutado para evitar cálculos redundantes.
from functools import lru_cache

@lru_cache(maxsize=128) 
def fibonacci(n): 
    if n <= 1: 
        return n 
    return fibonacci(n-1) + fibonacci(n-2) 

print(fibonacci(10)) 

#

"""Buenas Prácticas
Utilizar decoradores de manera clara y explícita: Es recomendable usar decoradores cuando el comportamiento adicional que estás agregando es claro y no interfiere con la claridad del código. Si el decorador hace demasiado, puede hacer que el código sea más difícil de entender.

Usar decoradores para código repetido: Si encuentras que varias funciones tienen el mismo comportamiento repetido, un decorador puede ser una forma eficiente de centralizar esa lógica.

No hacer decoradores muy complejos: Los decoradores no deben ser demasiado complejos ni hacer demasiadas cosas a la vez. Esto puede hacer que el código sea más difícil de seguir y depurar.

Documentar el comportamiento del decorador: Como los decoradores modifican el comportamiento de las funciones que decoran, es importante documentarlos bien para que otros desarrolladores entiendan cómo interactúan con las funciones decoradas."""






"""Conceptos relacionados"""

"""1. Funciones de Primera Clase
Las funciones en Python son de primera clase, lo que significa que pueden ser asignadas a variables, pasadas como argumentos y retornadas desde otras funciones. Este es un requisito esencial para los decoradores, ya que un decorador es simplemente una función que toma otra función como argumento y devuelve una nueva función. Ejemplo:"""
def saludo(): 
    return "Hola" # Asignando la función a una variable 
nueva_funcion = saludo 

print(nueva_funcion()) # Imprime "Hola" 

#Relación: Los decoradores dependen de que las funciones sean tratadas como objetos de primera clase.

"""2. Funciones Anidadas (Nested Functions)
Un decorador comúnmente utiliza funciones anidadas. Una función anidada es aquella que está definida dentro de otra función. Los decoradores generalmente definen una función interna (envoltorio o wrapper) que se encarga de modificar o 

extender el comportamiento de la función original. Ejemplo:"""
def decorador(func):
    def envoltura(): 
        print("Antes de la ejecución.")
    func()
    print("Después de la ejecución.") 
    return envoltura 

#Relación: Los decoradores hacen uso de funciones anidadas para envolver la función original y modificar su comportamiento.

"""3. Cierre (Closures)
Los decoradores también dependen del concepto de cierres. Un cierre ocurre cuando una función anidada captura y recuerda el entorno en el que fue creada, incluso después de que la función exterior haya terminado de ejecutarse. Ejemplo:"""
def contador(): 
    count = 0 
    def incrementar(): 
        nonlocal count 
        count += 1 
        return count 
    return incrementar 

contador_func = contador() 
print(contador_func()) # Imprime 1 print(contador_func()) # Imprime 2 

#Relación: Los decoradores aprovechan los cierres para recordar y modificar el comportamiento de las funciones originales.

"""4. Funciones Lambda
Las funciones lambda son funciones anónimas que se pueden definir en una sola línea. A veces se usan como decoradores simples cuando se requiere aplicar una función breve sin necesidad de una definición formal. Ejemplo:"""
# Decorador simple utilizando una función lambda 
decorador = lambda func: lambda: print("Decorado: ", func()) 

@decorador 
def saludo():
    return "Hola"

saludo() # Imprime: Decorado: Hola 

#Relación: Las funciones lambda pueden servir como decoradores cuando la funcionalidad es pequeña y se puede definir en una sola expresión.

"""5. Métodos de Clases
Los decoradores pueden ser utilizados para métodos dentro de una clase. Un decorador aplicado a un método puede modificar su comportamiento o agregar funcionalidades, como verificación de permisos o validación. Ejemplo:"""
class MiClase: 
    def metodo(self): 
        print("Método original") 

    @staticmethod 
    def metodo_estatico(): 
        print("Método estático") 

#Relación: Los decoradores también son comúnmente usados con métodos de clases, como @staticmethod y @classmethod.

"""6. Desempaquetado de Argumentos (*args, **kwargs)
Los decoradores a menudo deben ser capaces de manejar cualquier número de argumentos posicionales y de palabra clave, ya que pueden ser aplicados a funciones con diferentes firmas de parámetros. Para lograr esto, se utilizan las construcciones *args y **kwargs. Ejemplo:"""
def decorador(func): 
    def envoltura(*args, **kwargs): 
        print(f"Arguments: {args}, Keyword Arguments: {kwargs}") 
        return func(*args, **kwargs)
    return envoltura 

@decorador 
def suma(a, b): 
    return a + b

suma(2, 3) # Arguments: (2, 3), Keyword Arguments: {} 

#Relación: Los decoradores deben ser capaces de manejar funciones con diferentes números de argumentos utilizando *args y **kwargs.

"""7. functools.wraps
Cuando aplicas un decorador, la función decorada puede perder información importante como su nombre, documentación (__doc__) y otros atributos que originalmente tenía. Para evitar esto, el módulo functools ofrece el decorador wraps, que ayuda a preservar esos atributos. Ejemplo:"""
from functools import wraps 

def decorador(func):
    @wraps(func) 
    def envoltura(*args, **kwargs): 
        print("Antes de ejecutar la función.") 
        return func(*args, **kwargs) 
    return envoltura

@decorador 
def saludo(): 
    """Esta es la función saludo.""" 
    print("Hola") 

print(saludo.__doc__) # Imprime: Esta es la función saludo. 

#Relación: functools.wraps ayuda a mantener la información de la función original al usar decoradores.

"""8. Clases Decoradoras
Los decoradores también pueden implementarse usando clases. Una clase decoradora debe definir el método __call__, que permite que una instancia de la clase actúe como un decorador. Ejemplo:
class MiDecorador: """
def __init__(self, func): 
    self.func = func 

def __call__(self, *args, **kwargs): 
    print("Antes de ejecutar la función.") 
    result = self.func(*args, **kwargs) 
    print("Después de ejecutar la función.") 
    return result 

@MiDecorador 
def mi_funcion(): 
    print("Ejecutando la función.") 
    
mi_funcion() 

#Relación: Las clases decoradoras permiten un control más detallado sobre cómo se modifican las funciones.

"""9. Memoización
La memoización es una técnica para almacenar los resultados de funciones costosas en términos de tiempo para evitar recalcularlos. Los decoradores como @lru_cache se utilizan para aplicar memoización. Ejemplo:"""

from functools import lru_cache 
@lru_cache(maxsize=128) 
def fibonacci(n): 
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2) 

print(fibonacci(10)) 

#Relación: Los decoradores como lru_cache implementan memoización, mejorando el rendimiento de funciones recursivas.




"""Prácticas """

"""1. Usar Decoradores para Evitar Código Repetitivo
Una de las principales razones para usar decoradores es eliminar la duplicación de código. Si tienes varias funciones que comparten un comportamiento común (como la validación de datos, el registro de logs, el manejo de excepciones, etc.), puedes encapsular ese comportamiento en un decorador y aplicarlo a varias funciones.

Ejemplo:"""
def registrar_log(func): 
    def envoltura(*args, **kwargs): 
        print(f"Ejecutando la función {func.__name__}") 
        return func(*args, **kwargs) 
    return envoltura 

@registrar_log 
def saludar(nombre): 
    print(f"Hola, {nombre}!") 

saludar("Juan") 

#Esto es útil cuando tienes varias funciones que requieren el mismo comportamiento y no deseas repetir el mismo código cada vez.

"""2. Mantener los Decoradores Simples
Asegúrate de que los decoradores sean simples y enfocados en una sola responsabilidad. Si un decorador hace demasiadas cosas, puede complicar la depuración y el mantenimiento del código. Intenta aplicar el principio de responsabilidad única (SRP). """
#Malo:
def decorador_complejo(func): 
    def envoltura(*args, **kwargs): 
        print("Verificación de permisos") 
        print("Log de ejecución")
        print("Enviando correo") 
        return func(*args, **kwargs) 
    return envoltura 

#Bueno:
def verificar_permisos(func): 
    def envoltura(*args, **kwargs): 
        print("Verificando permisos...")
        return func(*args, **kwargs)
    return envoltura

def log_ejecucion(func): 
    def envoltura(*args, **kwargs): 
        print("Registrando log...")
        return func(*args, **kwargs) 
    return envoltura 

#De esta manera, cada decorador tiene un propósito claro y puedes combinarlos como sea necesario.

"""3. Usar functools.wraps para Preservar la Información de la Función Decorada
Cuando un decorador envuelve una función, pierde atributos importantes como su nombre, su documentación (__doc__), entre otros. Usar functools.wraps dentro del decorador es una buena práctica para preservar esta información. Ejemplo:"""
from functools import wraps

def decorador(func): 
    @wraps(func) 
    def envoltura(*args, **kwargs): 
        print("Antes de ejecutar") 
        return func(*args, **kwargs)
    return envoltura 

@decorador 
def saludar(nombre): 
    """Saluda a la persona proporcionada.""" 
    print(f"Hola, {nombre}!") 
    print(saludar.__name__) # saludar 
    print(saludar.__doc__) # Saluda a la persona proporcionada. 

"""4. Usar Decoradores para Manejo de Excepciones
Si tienes varias funciones que requieren manejo de excepciones similar, un decorador puede ser útil para centralizar esa lógica. Ejemplo:"""
def manejar_excepciones(func): 
    def envoltura(*args, **kwargs): 
        try:
            return func(*args, **kwargs)
        except Exception as e: 
            print(f"Ocurrió un error: {e}") 
        return envoltura 

@manejar_excepciones 
def dividir(a, b): 
    return a / b 

dividir(10, 0) # Imprime: Ocurrió un error: division by zero 

"""5. Evitar Decoradores Pesados y Largos
Si un decorador es demasiado complejo o largo, puede volverse difícil de mantener. Si el decorador necesita realizar muchas tareas, considera dividirlo en varios decoradores más pequeños, cada uno con una responsabilidad bien definida.

6. Aplicar Decoradores en Métodos de Clase
Los decoradores no solo son útiles para funciones globales, también se pueden usar en métodos de clase. Esto es particularmente útil para aplicar validaciones o funcionalidades específicas de clase. Ejemplo:"""
class MiClase: 
    @staticmethod 
    def metodo_estatico(): 
        print("Método estático")

    @classmethod 
    def metodo_clase(cls): 
            print(f"Método de clase: {cls}")

# Aplicar decorador para logging en métodos de clase 
def log_metodo(func): 
    def envoltura(self, *args, **kwargs):
        print(f"Ejecutando {func.__name__}...") 
        return func(self, *args, **kwargs) 
    return envoltura 

class MiClaseConLog: 
    @log_metodo
    def metodo_con_log(self): 
        print("Método con log.") 

obj = MiClaseConLog() 
obj.metodo_con_log() 

"""7. Usar Decoradores con Parámetros
Si necesitas que tu decorador sea más flexible y acepte parámetros, puedes anidar funciones. Esto permite personalizar el comportamiento del decorador. Ejemplo:"""
def repetir(n): 
    def decorador(func): 
        def envoltura(*args, **kwargs): 
            for _ in range(n): 
                result = func(*args, **kwargs) 
                return result 
        return envoltura 
    return decorador 

@repetir(3) 
def saludar():
    print("Hola!") 
    
saludar() # Imprime "Hola!" tres veces. 

"""8. Decoradores para Cache o Memoización
Usar un decorador para memoizar los resultados de funciones costosas es una práctica muy común. functools.lru_cache es un decorador incorporado que implementa esta funcionalidad. Ejemplo:"""
from functools import lru_cache 

@lru_cache(maxsize=128) 
def fibonacci(n):
    if n <= 1: 
        return n 
    return fibonacci(n-1) + fibonacci(n-2) 

print(fibonacci(10)) # Imprime 55, pero optimizado por cache. 

"""9. Pruebas de Decoradores
Asegúrate de probar tus decoradores. Los decoradores modifican el comportamiento de las funciones, por lo que es importante garantizar que la función decorada siga funcionando correctamente. Ejemplo:"""
def test_decorador(): 
    @decorador 
    def saludo(): 
        return "Hola" 
    
assert saludo() == "Hola" 

"""10. Cuidado con la Orden de los Decoradores
Si estás aplicando varios decoradores a una función, el orden en que se aplican puede afectar el resultado. Los decoradores se aplican de abajo hacia arriba, es decir, el decorador que aparece más cerca de la función se aplica primero. Ejemplo:"""
def decorador_a(func): 
    def envoltura(): 
        print("Decorador A")
        return func() 
    return envoltura 

def decorador_b(func): 
    def envoltura():
        print("Decorador B") 
        return func() 
    return envoltura 

@decorador_a 
@decorador_b 
def saludar(): 
    print("¡Hola!") 

saludar() # La salida será: 
# Decorador A 
# Decorador B 
# ¡Hola! 




"""Técnicas """


"""6. Decoradores para Validación de Argumentos
Usar decoradores para validar los argumentos de las funciones puede hacer que el código sea más limpio y evitar la repetición de lógica de validación. Puedes crear un decorador que verifique si los parámetros son válidos antes de ejecutar la función.
Técnica: Crear decoradores para validar argumentos de entrada, asegurando que las funciones solo se ejecuten con valores válidos. Ejemplo:"""
def validar_positivo(func):
    def envoltura(*args, **kwargs):
        if args[0] <= 0: 
            raise ValueError("El valor debe ser positivo") 
            return func(*args, **kwargs)
    return envoltura 

@validar_positivo 
def cuadrado(x): 
    return x ** 2 

print(cuadrado(4)) # 16 
print(cuadrado(-2)) # Levanta un ValueError 

"""7. Decoradores como Funciones de Orden Superior
Un decorador es, en esencia, una función de orden superior, es decir, una función que toma otra función como argumento y devuelve una nueva función. Puedes utilizar decoradores en combinación con otras funciones de orden superior, como map(), filter() y reduce().
Técnica: Combinar decoradores con funciones de orden superior para crear funciones más generales o reutilizables. Ejemplo:"""
def multiplicar_por(n): 
    def decorador(func): 
        def envoltura(*args, **kwargs): 
            result = func(*args, **kwargs) 
            return result * n 
        return envoltura 
    return decorador

@multiplicar_por(3) 
def obtener_numero():
    return 5 

print(obtener_numero()) # 15 

"""8. Aplicación de Decoradores para Monitoreo y Performance
Puedes utilizar decoradores para medir el tiempo de ejecución de una función o monitorear el uso de recursos. Esto es útil para realizar análisis de rendimiento sin modificar directamente el código de la función.
Técnica: Utilizar decoradores para medir el tiempo de ejecución y realizar análisis de rendimiento o de uso de recursos. Ejemplo:"""
import time 

def medir_tiempo(func): 
    def envoltura(*args, **kwargs): 
        inicio = time.time() 
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio} segundos") 
        return resultado 
    return envoltura 

@medir_tiempo 
def largo_calculo():
    time.sleep(2) # Simula una tarea pesada 
    return "Cálculo completado" 

largo_calculo() # Salida: Tiempo de ejecución: 2.0005 segundos 