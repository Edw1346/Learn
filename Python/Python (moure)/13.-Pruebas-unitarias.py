"""Pruebas Unitarias"""

"""¿Qué son las pruebas unitarias?
Las pruebas unitarias son un tipo de prueba de software cuyo objetivo es verificar que las unidades individuales de código (generalmente funciones o métodos) funcionan correctamente de forma aislada. En otras palabras, las pruebas unitarias ayudan a asegurarse de que cada parte del código cumpla con su propósito, lo que facilita la detección temprana de errores y mejora la calidad general del software.

Características clave de las pruebas unitarias:
Aisladas: Cada prueba unitaria debe enfocarse en una sola parte del sistema.
Automatizadas: Las pruebas unitarias se suelen ejecutar automáticamente cada vez que se realizan cambios en el código, asegurando que todo siga funcionando correctamente.
Rápidas: Son rápidas de ejecutar y no deben depender de recursos externos como bases de datos o servicios externos.
Repetibles: Deben proporcionar los mismos resultados cuando se ejecutan en diferentes momentos o entornos.

Importancia de las pruebas unitarias
Detección temprana de errores:
Las pruebas unitarias permiten identificar errores y fallos en el código de forma temprana, lo que reduce la complejidad de la corrección y facilita la depuración.

Refactorización segura:
Tener un conjunto robusto de pruebas unitarias permite refactorizar el código con confianza, ya que las pruebas ayudan a garantizar que los cambios no introduzcan nuevos errores.

Documentación viviente:
Las pruebas unitarias sirven como documentación sobre cómo se debe comportar el sistema. Al leer las pruebas, otros desarrolladores pueden entender la lógica y el propósito de una función o módulo.

Mejora en la calidad del software:
Las pruebas unitarias contribuyen a una mayor calidad del código al forzar la escritura de funciones más pequeñas, modulares y fáciles de mantener.

Cómo escribir pruebas unitarias en Python
En Python, el módulo unittest es la herramienta estándar para escribir y ejecutar pruebas unitarias. También existen otros frameworks como pytest, que ofrece una sintaxis más sencilla, pero unittest es ampliamente utilizado.

Estructura básica de una prueba unitaria

Importación del módulo unittest:
Para comenzar, debes importar el módulo unittest y escribir una clase que herede de unittest.TestCase.

Definir métodos de prueba:
Dentro de esta clase, defines métodos que representen casos de prueba. Estos métodos deben comenzar con la palabra "test" para que el framework los reconozca como pruebas.

Usar afirmaciones:
Para verificar que el código se comporta como se espera, puedes usar métodos de afirmación como assertEqual(), assertTrue(), assertFalse(), entre otros.

Ejemplo básico:"""
import unittest # Función a probar 
def suma(a, b): 
    return a + b # Clase de prueba class 

TestFunciones(unittest.TestCase): # Método de prueba 
def test_suma(self): 
    self.assertEqual(suma(2, 3), 5) # Verifica que 2 + 3 sea igual a 5 
    self.assertEqual(suma(-1, 1), 0) # Verifica que -1 + 1 sea igual a 0 
    self.assertEqual(suma(0, 0), 0) # Verifica que 0 + 0 sea igual a 0 
    if __name__ == '__main__': 
        unittest.main() 
        #Comandos comunes en unittest:
        assertEqual(a, b): #Verifica que a sea igual a b.
        assertNotEqual(a, b): #Verifica que a no sea igual a b.
        assertTrue(x): #Verifica que x sea True.
        assertFalse(x): #Verifica que x sea False.
        assertRaises(ErrorType): #Verifica que una excepción específica sea lanzada.

"""Buenas Prácticas para las pruebas unitarias
Aislar las pruebas: Cada prueba unitaria debe ser independiente. No debe depender del estado de otras pruebas ni del orden en que se ejecutan.

Nombrado claro de las pruebas: Los nombres de los métodos de prueba deben ser descriptivos. Un buen nombre indica qué comportamiento está siendo probado.

Pruebas pequeñas y simples: Cada prueba debe verificar una única cosa. Mantén las pruebas simples para que sean fáciles de mantener y depurar.

Evitar dependencias externas: Si la función que se está probando depende de recursos externos como bases de datos o APIs, es recomendable usar mocks o stubs para simular esos recursos y evitar efectos secundarios en las pruebas.

Usar aserciones para verificar el comportamiento esperado: Las aserciones son fundamentales para verificar el comportamiento esperado. No olvides usar varias aserciones si es necesario para validar todos los posibles resultados.

Cobertura de pruebas: Intenta cubrir todas las rutas posibles del código, incluyendo los casos límite y de borde. Las herramientas de cobertura de pruebas, como coverage.py, pueden ayudarte a asegurarte de que todas las funciones y ramas del código están siendo probadas.

Automatización de las pruebas: Integra las pruebas unitarias en tu flujo de trabajo mediante herramientas de integración continua (CI) como Jenkins, Travis CI o GitHub Actions. Esto asegurará que las pruebas se ejecuten automáticamente en cada cambio."""

"""Técnicas Avanzadas en Pruebas Unitarias"""

"""Mocking: El mocking es una técnica que se utiliza para simular el comportamiento de dependencias externas de una 

unidad de código (como bases de datos o servicios web). En Python, puedes usar la librería unittest.mock para crear objetos simulados que imiten el comportamiento de dependencias externas. Ejemplo con mock:"""
from unittest.mock import MagicMock 

def obtener_datos(url): 
# Simula obtener datos desde una API 
    pass 

class TestAPI(unittest.TestCase): 
    def test_obtener_datos(self): 
        mock_api = MagicMock() 
        mock_api.obtener_datos.return_value = {"status": "OK"} 
        self.assertEqual(mock_api.obtener_datos("https://api.com"), {"status": "OK"}) 

"""Pruebas Parametrizadas:
A veces, necesitas probar el mismo código con diferentes entradas. Las pruebas parametrizadas te permiten ejecutar un conjunto de pruebas con varias combinaciones de datos. Ejemplo con unittest:"""
import unittest from parameterized
import parameterized 

class TestSuma(unittest.TestCase):
    @parameterized.expand([ (2, 3, 5), (-1, 1, 0), (0, 0, 0) ]) 
    def test_suma(self, a, b, resultado): 
        self.assertEqual(suma(a, b), resultado) 


"""Conceptos Relacionados con Pruebas Unitarias"""

"""1. Testing (Pruebas de Software)
Pruebas de Software: El proceso de ejecutar un programa con el objetivo de encontrar errores. Existen diferentes tipos de pruebas, y las pruebas unitarias son solo uno de ellos, aunque son fundamentales en el ciclo de vida del desarrollo.

2. Tipos de Pruebas
Pruebas Unitarias: Se enfocan en probar unidades individuales de código, como funciones o métodos.
Pruebas de Integración: Aseguran que diferentes módulos o componentes de un sistema funcionen bien juntos.
Pruebas Funcionales: Validan que el sistema funcione de acuerdo con los requisitos especificados.
Pruebas de Regresión: Se ejecutan para garantizar que nuevas modificaciones no afecten funcionalidades previamente desarrolladas.
Pruebas de Sistema: Verifican que el sistema completo funcione correctamente.
Pruebas de Aceptación: Validan que el sistema cumpla con las expectativas del cliente o del usuario final.

3. Frameworks de Pruebas
unittest: El módulo estándar de Python para realizar pruebas unitarias, que proporciona herramientas para crear y ejecutar pruebas.
pytest: Un framework más flexible y sencillo para realizar pruebas en Python, compatible con unittest y otras bibliotecas.
nose2: Otro framework de pruebas para Python, diseñado como sucesor de nose, ofreciendo características adicionales.
mock: Parte del módulo estándar de Python para simular (mock) objetos o comportamientos en pruebas unitarias, lo que permite testear en aislamiento sin depender de recursos externos.

4. Aserciones (Assertions)
Aserciones: Son las comprobaciones que se hacen durante las pruebas para verificar que los resultados sean los esperados. Por ejemplo, assertEqual(), assertTrue(), assertRaises().

5. Cobertura de Pruebas (Test Coverage)
Cobertura de Pruebas: Mide qué tan bien las pruebas cubren el código fuente. Se puede usar herramientas como coverage.py para analizar qué líneas de código están siendo ejecutadas durante las pruebas. La cobertura completa no garantiza que el código esté libre de errores, pero ayuda a asegurarse de que no se omitan partes críticas del sistema.


6. Mocks y Stubs
Mocks: Son objetos simulados que imitan el comportamiento de objetos reales para probar interacciones. Por ejemplo, se usan para simular el comportamiento de una base de datos o de una API externa sin necesidad de usar esos servicios reales.
Stubs: Son versiones simplificadas de objetos o funciones utilizadas para devolver valores predefinidos durante las pruebas. Ayudan a evitar la necesidad de acceder a recursos externos como bases de datos o servicios en red.

7. TDD (Test-Driven Development)
Desarrollo Dirigido por Pruebas (TDD): Es una metodología de desarrollo de software en la que las pruebas unitarias se escriben antes de escribir el código que las va a pasar. El ciclo básico de TDD sigue estos pasos: 
Escribir una prueba que falle. Escribir el código mínimo necesario para hacer que la prueba pase. Refactorizar el código.

8. BDD (Behavior-Driven Development)
Desarrollo Dirigido por Comportamiento (BDD): Similar a TDD, pero en lugar de centrarse en las pruebas de las funciones, se enfoca en los comportamientos y en la descripción de los mismos en un lenguaje natural. Se usan herramientas como Behave para Python.

9. CI/CD (Integración Continua y Despliegue Continuo)
Integración Continua (CI): Es la práctica de fusionar cambios de código frecuentemente (varias veces al día) para asegurar que el código funcione de manera conjunta. Las pruebas unitarias suelen formar parte del proceso de CI para detectar errores lo antes posible.
Despliegue Continuo (CD): Va un paso más allá, al automatizar el proceso de despliegue del código en producción, asegurándose de que todas las pruebas hayan pasado antes de hacer el despliegue.

10. Pruebas de Caja Negra vs. Caja Blanca
Caja Negra: El tester no conoce la estructura interna del código, solo valida la salida en función de las entradas proporcionadas.
Caja Blanca: El tester tiene acceso al código fuente y verifica su funcionamiento interno, asegurándose de que todas las rutas del código se ejecuten correctamente.

11. Revisión de Código (Code Review)
Revisión de Código: Aunque no es estrictamente una prueba unitaria, las revisiones de código ayudan a encontrar posibles errores antes de que el código se fusione en la base principal del proyecto. Las pruebas unitarias facilitan este proceso al asegurar que las nuevas modificaciones no rompan funcionalidades existentes.

12. Mocking y Dependency Injection
Dependency Injection (DI): Es un patrón de diseño en el que las dependencias de una clase o función se inyectan en lugar de ser creadas internamente. Es útil cuando se combinan con mocks para simular dependencias durante las pruebas.
Mocking: Es el proceso de crear un objeto simulado que imita el comportamiento de objetos reales de una manera controlada y repetible. En pruebas unitarias, el uso de mocks permite probar componentes de manera aislada."""



"""Buenas Prácticas en Pruebas Unitarias"""

"""Mantén las pruebas pequeñas y enfocadas:
Cada prueba unitaria debe centrarse en una única funcionalidad de la unidad de código que estás probando. Esto hace que las pruebas sean más fáciles de entender y depurar. No mezcles múltiples casos de prueba en un solo método. Si es necesario verificar múltiples comportamientos, divídelos en pruebas separadas.

Usa nombres descriptivos para las pruebas:
Los nombres de las pruebas deben ser claros y reflejar lo que están probando. Por ejemplo, test_suma_dos_numeros_positivos es más descriptivo que test_suma. Sigue una convención de nombres consistente, como test_<función>_<comportamiento>.

Asegúrate de que las pruebas sean independientes:

Cada prueba debe ser autónoma, lo que significa que no debe depender del estado de otras pruebas. Si una prueba falla, no debería afectar a las demás.
Evita los efectos secundarios entre pruebas, como el uso de variables globales o de recursos compartidos.

Mantén tus pruebas rápidas:
Las pruebas unitarias deben ser rápidas para poder ejecutarse con frecuencia. Si las pruebas son lentas, es más probable que los desarrolladores las omitan.
Usa mocks y stubs para evitar la dependencia de recursos externos lentos, como bases de datos o servicios web.

Utiliza aserciones claras:
Las aserciones verifican que el resultado de la ejecución sea el esperado. Usa las aserciones apropiadas para el caso que estás verificando, como assertEqual(), assertTrue(), assertFalse(), etc.
Si es necesario, utiliza múltiples aserciones en una sola prueba para verificar diferentes aspectos del comportamiento.

Asegura la cobertura de pruebas:
Asegúrate de que todas las rutas importantes del código estén cubiertas por pruebas. Esto incluye las condiciones de borde y los casos especiales.
Herramientas de cobertura como coverage.py pueden ayudarte a medir qué partes del código están siendo cubiertas por las pruebas.

Haz pruebas para casos límite y excepciones:
No te limites a probar solo los casos comunes. Los casos límite (como 0, valores negativos, o cadenas vacías) y las excepciones son fundamentales para garantizar que tu código maneje todas las situaciones correctamente.
Asegúrate de que las funciones que deben lanzar excepciones realmente lo hagan cuando corresponda."""


"""Técnicas Avanzadas en Pruebas Unitarias"""

"""Mocking y Stubbing:
El mocking y el stubbing son técnicas avanzadas que permiten simular comportamientos de objetos o servicios externos que no son el foco de la prueba.
En Python, puedes usar la librería unittest.mock para crear mock objects y simular interacciones con objetos que dependen de APIs, bases de datos u otros servicios externos. Ejemplo de Mocking:"""
from unittest.mock import Mock

# Simulamos una función que interactúa con una API externa
api_mock = Mock() 
api_mock.obtener_datos.return_value = {"status": "OK"} # Usamos el mock en lugar de la función real
resultado = api_mock.obtener_datos("https://api.com") 
assert resultado == {"status": "OK"} 

"""Test-Driven Development (TDD):
El Desarrollo Guiado por Pruebas (TDD) es una metodología donde primero se escriben las pruebas y luego el código para hacer que esas pruebas pasen. El ciclo básico de TDD es: 
Escribir una prueba que falle. Escribir el código necesario para pasar la prueba. Refactorizar el código y asegurarse de que la prueba siga pasando. Ejemplo de TDD:"""
# Paso 1: Escribir una prueba que falle 
def test_suma(): 
    assert suma(2, 3) == 5 # Aquí la prueba falla porque la función no existe. 
# Paso 2: Escribir el código para pasar la prueba 
def suma(a, b): 
    return a + b 
# Paso 3: Refactorizar (si es necesario) 

"""Pruebas Parametrizadas:
Las pruebas parametrizadas son útiles cuando deseas ejecutar el mismo conjunto de pruebas con diferentes entradas. Esto evita la duplicación de código y asegura que el comportamiento del código sea correcto con diferentes conjuntos de datos. Puedes usar la librería parameterized para realizar pruebas con múltiples parámetros. Ejemplo de pruebas parametrizadas con unittest:"""

from parameterized import parameterized 
import unittest

class TestSuma(unittest.TestCase): 
    @parameterized.expand([ (2, 3, 5), (-1, 1, 0), (0, 0, 0) ])
    def test_suma(self, a, b, resultado): 
        self.assertEqual(suma(a, b), resultado) 
        if __name__ == "__main__": unittest.main() 

"""Uso de Fixtures para Configuración y Limpieza:
Las fixtures son objetos o configuraciones que se crean antes de ejecutar las pruebas y se limpian después. Son útiles para la configuración de recursos que se reutilizan en varias pruebas, como bases de datos o archivos. En unittest, puedes usar los métodos setUp() y tearDown() para definir las fixtures. Ejemplo de Fixture con setUp y tearDown:"""
import unittest 

class TestBaseDeDatos(unittest.TestCase): 
    def setUp(self): 
    # Configuración previa a las pruebas 
        self.db = conectar_a_base_de_datos() 
    def tearDown(self): 
    # Limpieza después de las pruebas 
        self.db.cerrar_conexion() 

    def test_consultar_usuario(self):
        resultado = self.db.consultar_usuario(1) 
        self.assertEqual(resultado["nombre"], "Juan") 
    if __name__ == "__main__": unittest.main() 

"""Cobertura de Código:
Asegúrate de que todas las partes críticas del código estén cubiertas por pruebas unitarias. Las herramientas de cobertura de código permiten visualizar qué porciones del código no están siendo probadas. Usa herramientas como coverage.py para medir la cobertura de tus pruebas. Ejemplo de uso de coverage.py:"""
#coverage run -m unittest discover # Ejecutar las pruebas con cobertura 
#coverage report # Ver el reporte de cobertura 