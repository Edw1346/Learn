import unittest # Función a probar 

#El módulo unittest herramienta para realizar pruebas automatizadas (test-driven development). Permite crear, ejecutar y organizar pruebas de unidades de código (funciones, métodos, etc.) de manera estructurada

"""Características clave: Pruebas unitarias: Es utilizado para probar unidades individuales de código de forma aislada.
Asserts: Proporciona métodos para verificar si los resultados de las pruebas son correctos, como assertEqual(), assertTrue(), etc.
Organización de pruebas: Puedes agrupar las pruebas en clases y ejecutar todas las pruebas de forma ordenada."""

#Ejemplo básico:
def suma(a, b): return a + b # Clase de pruebas 

class TestSuma(unittest.TestCase): 
    def test_suma(self): 
        self.assertEqual(suma(2, 3), 5) # Verifica que la suma de 2 + 3 sea 5 
        self.assertEqual(suma(-1, 1), 0) # Verifica que -1 + 1 sea 0 
        
        # Ejecutar las pruebas 
        if __name__ == "__main__": unittest.main() 

        #assertEqual(a, b): Verifica que a sea igual a b. Ejemplo: 
        self.assertEqual(2 + 2, 4)  # Verifica que 2 + 2 sea igual a 4 
        self.assertEqual('hello', 'hello') # Verifica que las cadenas sean iguales 

        #. assertNotEqual(a, b): Verifica que a no sea igual a b. Ejemplo:
        self.assertNotEqual(2 + 2, 5) # Verifica que 2 + 2 no sea igual a 5 
        self.assertNotEqual('hello', 'world') # Verifica que las cadenas no sean iguales 

        #. assertTrue(x): Verifica que la expresión x sea True. Ejemplo:
        self.assertTrue(1 == 1) # Verifica que 1 sea igual a 1 
        self.assertTrue('a' in 'apple') # Verifica que 'a' esté en 'apple' 

        #. assertFalse(x): Verifica que la expresión x sea False. Ejemplo:
        self.assertFalse(1 == 2) # Verifica que 1 no sea igual a 2 
        self.assertFalse('b' in 'apple') # Verifica que 'b' no esté en 'apple' 

        #. assertIs(a, b): Verifica que a y b sean el mismo objeto (es decir, que a es b). Ejemplo:
        a = [1, 2, 3] 
        b = a 
        self.assertIs(a, b) # Verifica que 'a' y 'b' sean el mismo objeto 

        #. assertIsNot(a, b): Verifica que a y b no sean el mismo objeto. Ejemplo:
        a = [1, 2, 3] 
        b = [1, 2, 3] 
        self.assertIsNot(a, b) # Verifica que 'a' y 'b' no sean el mismo objeto 

        #. assertIsNone(x): Verifica que x sea None. Ejemplo:
        my_var = None
        self.assertIsNone(None) # Verifica que la variable sea None
        self.assertIsNone(my_var) # Verifica que 'my_var' sea None 

        #. assertIsNotNone(x): Verifica que x no sea None. Ejemplo:
        my_var = 3
        self.assertIsNotNone(5) # Verifica que 5 no sea 
        self.assertIsNotNone(my_var) # Verifica que 'my_var' no sea None 

        #. assertIn(a, b): Verifica que a esté en b (se usa en secuencias o colecciones). Ejemplo:
        self.assertIn(2, [1, 2, 3]) # Verifica que 2 esté en la lista 
        self.assertIn('apple', 'apple pie') # Verifica que 'apple' esté en la cadena 

        #. assertNotIn(a, b): Verifica que a no esté en b. Ejemplo:
        self.assertNotIn(4, [1, 2, 3]) # Verifica que 4 no esté en la lista 
        self.assertNotIn('banana', 'apple pie') # Verifica que 'banana' no esté en la cadena 

        #. assertIsInstance(a, b): Verifica que a sea una instancia de b (una clase o tipo). Ejemplo:
        self.assertIsInstance(5, int) # Verifica que 5 sea una instancia de 'int' 
        self.assertIsInstance("hello", str) # Verifica que "hello" sea una instancia de 'str' 

        #. assertNotIsInstance(a, b): Verifica que a no sea una instancia de b. Ejemplo:
        self.assertNotIsInstance("hello", int) # Verifica que "hello" no sea una instancia de 'int' 
        self.assertNotIsInstance(5, str) # Verifica que 5 no sea una instancia de 'str' 

        #. assertAlmostEqual(a, b, places=7): Verifica que a y b sean casi iguales, permitiendo una diferencia pequeña. Puedes especificar la cantidad de decimales permitidos con places. Ejemplo:
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=2) # Verifica que 0.1 + 0.2 sea igual a 0.3 con 2 decimales 
        self.assertAlmostEqual(1.3333, 1.3334, places=3) # Verifica que los dos valores sean casi iguales 

        #. assertNotAlmostEqual(a, b, places=7): Verifica que a y b no sean casi iguales, permitiendo una diferencia pequeña:
        self.assertNotAlmostEqual(0.1 + 0.2, 0.4, places=2) # Verifica que 0.1 + 0.2 no sea igual a 0.4 

        #. assertGreater(a, b): Verifica que a sea mayor que b. Ejemplo:
        self.assertGreater(3, 2) # Verifica que 3 sea mayor que 2 
        self.assertGreater(10, 5) # Verifica que 10 sea mayor que 5 

        #. assertGreaterEqual(a, b): Verifica que a sea mayor o igual a b. Ejemplo:
        self.assertGreaterEqual(3, 2) # Verifica que 3 sea mayor o igual a 2 
        self.assertGreaterEqual(5, 5) # Verifica que 5 sea mayor o igual a 5 

        #. assertLess(a, b): Verifica que a sea menor que b. Ejemplo:
        self.assertLess(2, 3) # Verifica que 2 sea menor que 3 
        self.assertLess(4, 5) # Verifica que 4 sea menor que 5 

        #. assertLessEqual(a, b): Verifica que a sea menor o igual a b. Ejemplo:
        self.assertLessEqual(2, 3) # Verifica que 2 sea menor o igual a 3 
        self.assertLessEqual(5, 5) # Verifica que 5 sea menor o igual a 5 

        #. assertRegex(text, regex): Verifica que el texto coincida con el patrón regular regex. Ejemplo:
        self.assertRegex("hello", r"^h") # Verifica que "hello" comience con 'h' 
        self.assertRegex("apple", r"pp") # Verifica que "apple" contenga 'pp' 

        #. assertNotRegex(text, regex): Verifica que el texto no coincida con el patrón regular regex. Ejemplo:
        self.assertNotRegex("hello", r"^a") # Verifica que "hello" no comience con 'a' 
        self.assertNotRegex("apple", r"xx") # Verifica que "apple" no contenga 'xx' 

        #. assertCountEqual(a, b): Verifica que a y b tengan los mismos elementos, independientemente del orden. Ejemplo:
        self.assertCountEqual([1, 2, 3], [3, 2, 1]) # Verifica que ambas listas tengan los mismos elementos 
        self.assertCountEqual("apple", "leppa") # Verifica que las cadenas tengan los mismos caracteres 

        #. assertLogs(logger, level): Verifica que se hayan registrado mensajes de log en el nivel especificado. Ejemplo:
        import logging 
        logger = logging.getLogger('mylogger') 
        with self.assertLogs('mylogger', level='ERROR'): logger.error('Error!') 


#Lista completa de las clases del módulo unittest con ejemplos detallados para cada una de ellas:

# unittest.TestCase: La clase base para todos los casos de prueba. Todas las pruebas deben derivar de esta clase para ser reconocidas como casos de prueba. Ejemplo:
class MyTestCase(unittest.TestCase): 
    def test_addition(self): self.assertEqual(2 + 2, 4) 
    if __name__ == '__main__': unittest.main() 

# unittest.TestResult: Contiene los resultados de la ejecución de las pruebas, incluyendo información sobre las pruebas que pasaron, fallaron o fueron ignoradas. Ejemplo:
result = unittest.TestResult() 
result.addSuccess('test1') # Agrega un caso de prueba exitoso 
result.addFailure('test2', 'assertEqual failed') # Agrega un caso de prueba fallido 
print(result.testsRun) # Imprime el número total de pruebas ejecutadas 

#. unittest.TextTestRunner: Ejecuta las pruebas y genera una salida de texto. Esta es la clase que normalmente usas para ejecutar las pruebas desde la línea de comandos. Ejemplo:
suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase) 
runner = unittest.TextTestRunner() 
runner.run(suite) 

#. unittest.TextTestResult: Utilizada por TextTestRunner para generar los resultados de las pruebas en un formato de texto. Muestra detalles sobre las pruebas pasadas y fallidas. Ejemplo:
result = unittest.TextTestResult(None, True, 0) 
result.addSuccess('test1') # Agrega un caso de prueba exitoso 
result.addFailure('test2', 'assertEqual failed') # Agrega un caso de prueba fallido 

#. unittest.TestLoader: Carga y descubre casos de prueba desde archivos, clases o métodos. Proporciona una manera sencilla de cargar y organizar las pruebas. Ejemplo:
loader = unittest.TestLoader() 
suite = loader.loadTestsFromTestCase(MyTestCase) 

#. unittest.SkipTest: Excepción que se lanza cuando un caso de prueba es marcado para ser ignorado. Esto permite que ciertas pruebas se salten si no son relevantes para la ejecución actual. Ejemplo:
import unittest 
class MyTestCase(unittest.TestCase): 
    def test_addition(self): 
        raise unittest.SkipTest("Skipping this test") 
    if __name__ == '__main__': unittest.main() 
        #. unittest.result._TextTestResult: Internamente utilizada por TextTestRunner para almacenar resultados de las pruebas:
        # Usada internamente en combinación con TextTestRunner 
    result = unittest.result._TextTestResult(None, True, 0) 
    #. unittest.mock.Mock: No es estrictamente parte del núcleo de unittest, pero es comúnmente utilizada junto con unittest para hacer pruebas unitarias. Permite crear objetos de prueba que imitan el comportamiento de objetos reales. Ejemplo:
    from unittest.mock import Mock 
    mock = Mock() 
    mock.method.return_value = 'Mocked response' 
    self.assertEqual(mock.method(), 'Mocked response') 
    #. unittest.mock.MagicMock: Similar a Mock, pero con métodos predefinidos como __getitem__, __setitem__, __iter__, etc., para una mayor flexibilidad en las pruebas. Ejemplo:
    from unittest.mock import MagicMock 
    magic_mock = MagicMock() 
    magic_mock.__getitem__.return_value = 'MagicMocked response' 
    self.assertEqual(magic_mock['key'], 'MagicMocked response') 




#El módulo unittest no tiene muchas variables definidas como tal, pero hay algunas constantes y variables que se utilizan para manejar la configuración y resultados de las pruebas. 

#unittest.main(): Esta es una función que se utiliza comúnmente para ejecutar las pruebas automáticamente cuando el archivo de pruebas es ejecutado como script. Se configura para buscar automáticamente instancias de unittest.TestCase y ejecutarlas:
class MyTestCase(unittest.TestCase): 
    def test_addition(self): self.assertEqual(2 + 2, 4)
    if __name__ == '__main__': unittest.main() # Ejecuta las pruebas cuando el script es ejecutado 

#unittest.__version__: Esta variable contiene la versión del módulo unittest que está instalada. No es comúnmente utilizada en pruebas, pero puede ser útil para verificar la versión del módulo en uso. Ejemplo:
print(unittest.__version__) # Imprime la versión de unittest 

#unittest.TestCase.id: Esta variable permite configurar cómo se identifican los métodos de prueba cuando se presentan los resultados. Puede ser útil si deseas modificar cómo se nombran o muestran las pruebas en los informes. Ejemplo:
class MyTestCase(unittest.TestCase): 
    def id(self): return "MyCustomTestName" 
    def test_example(self): self.assertEqual(2 + 2, 4) 
    if __name__ == '__main__': unittest.main() 




#El módulo unittest incluye algunas constantes que se utilizan para facilitar la configuración y ejecución de las pruebas. 

#unittest.TestCase.failfast: Esta es una variable de configuración que determina si el proceso de ejecución de pruebas debe detenerse tan pronto como se detecte un error. El valor predeterminado es False:
class MyTestCase(unittest.TestCase): 
    failfast = True # Detiene la ejecución tras el primer error
    def test_example(self): self.assertEqual(2 + 2, 4)
    if __name__ == '__main__': unittest.main() 

#unittest.TestResult.failfast: Similar al anterior, esta constante está relacionada con la clase TestResult. Si está activada (con un valor True), el proceso de pruebas se detendrá en cuanto falle la primera prueba. Ejemplo:
class MyTestCase(unittest.TestCase): 
    def test_example(self):  self.assertEqual(2 + 2, 4) 
    if __name__ == '__main__': 
        result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(MyTestCase)) 
        print("Test result:", result.failfast) # Imprime si se detuvo por un fallo 

# unittest.TestCase.maxDiff: Esta es una variable de configuración que se puede utilizar para especificar cuántas diferencias se deben mostrar en los informes cuando una prueba falla debido a una diferencia en el resultado esperado. Por defecto es None, lo que significa que no hay un límite. Ejemplo:
class MyTestCase(unittest.TestCase): 
    maxDiff = 50 # Limita el número de diferencias a mostrar
    def test_long_string_comparison(self): self.assertEqual("A" * 100, "B" * 100)   
    if __name__ == '__main__':  unittest.main() 

#unittest.result._WritelnDecorator: Esta constante es utilizada internamente por unittest.TextTestResult para escribir los resultados de las pruebas en la salida estándar, con el fin de que sea más legible. Es parte de la infraestructura interna de unittest, por lo que rara vez interactúas con ella directamente.

# unittest.TestResult.wasSuccessful(): Esta constante es un método de la clase TestResult, pero se incluye aquí porque es comúnmente usado para verificar si todas las pruebas se han ejecutado con éxito. Devuelve True si todas las pruebas pasaron, o False si alguna falló. Ejemplo:
class MyTestCase(unittest.TestCase): 
    def test_addition(self): self.assertEqual(2 + 2, 4) 
    if __name__ == '__main__': result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(MyTestCase)) 
    print("Tests passed:", result.wasSuccessful()) # Imprime si todas las pruebas fueron exitosas 



#Unittest tiene varias excepciones que se utilizan para manejar situaciones de error durante la ejecución de las pruebas. 

#unittest.TestCase.failureException: Es la excepción que se lanza cuando una afirmación (assert) en una prueba falla. Esta es la excepción básica que indica que la prueba no pasó. Uso: Generalmente no la usas directamente, ya que se lanza automáticamente cuando una afirmación falla. Ejemplo:
class MyTestCase(unittest.TestCase): 
    def test_example(self): 
        with self.assertRaises(unittest.TestCase.failureException): self.assertEqual(1, 2) # Esto lanzará una excepción failureException 
    if __name__ == '__main__': unittest.main() 

#. unittest.SkipTest: Esta excepción se utiliza para indicar que una prueba debe ser omitida. Puede ser útil cuando una prueba no es relevante en un entorno específico o si depende de factores externos no disponibles. Uso: Se lanza dentro de un método de prueba para omitir esa prueba específica. Ejemplo:
class MyTestCase(unittest.TestCase): 
    def test_skip_example(self):raise unittest.SkipTest("Esta prueba debe ser omitida") 
    if __name__ == '__main__': unittest.main() 

#. unittest.expectedFailure: Esta no es una excepción que se lance explícitamente, sino una forma de marcar una prueba como esperada para fallar. Si la prueba falla, se marca como esperada y no se cuenta como error. Uso: Se utiliza como un decorador sobre los métodos de prueba para indicar que se espera que fallen. Ejemplo:
class MyTestCase(unittest.TestCase):
    @unittest.expectedFailure 
    def test_expected_failure(self): self.assertEqual(1, 2) # Esta prueba está marcada como esperada para fallar 
    if __name__ == '__main__': unittest.main() 

#. unittest.TestCase.assertRaises (Excepción para probar excepciones): Esta no es una excepción directa, sino una función útil que se utiliza para comprobar que se lanza una excepción específica durante la ejecución de una prueba. Uso: Se utiliza dentro de las pruebas para verificar que una operación lance una excepción esperada. Ejemplo:
class MyTestCase(unittest.TestCase): 
    def test_divide_by_zero(self): 
        with self.assertRaises(ZeroDivisionError):
            x = 1 / 0 # Esto debería lanzar una excepción ZeroDivisionError 
    if __name__ == '__main__': unittest.main() 

#unittest.TestCase.assertWarns: Al igual que assertRaises, esta función se usa para verificar que se lance una advertencia (warning) durante la ejecución de la prueba. Uso: Permite comprobar si una función genera una advertencia:
import warnings
class MyTestCase(unittest.TestCase):
    def test_warning(self):
        with self.assertWarns(Warning): warnings.warn("Esta es una advertencia")
    if __name__ == '__main__': unittest.main() 



#El módulo unittest no tiene submódulos como tal. Sin embargo, el módulo en sí mismo está estructurado de manera que incluye diferentes clases, funciones y métodos que se utilizan para escribir, organizar y ejecutar pruebas unitarias.

"""Dentro de unittest, los principales elementos que puedes encontrar son:
unittest.TestCase: La clase base que se usa para crear las pruebas.
unittest.main(): Una función para ejecutar todas las pruebas cuando el archivo de pruebas se ejecuta como un script.
unittest.TextTestRunner: Un corredor de pruebas que se utiliza para ejecutar las pruebas y mostrar los resultados en la consola.
unittest.TextTestResult: Una clase que contiene los resultados de la ejecución de las pruebas.
unittest.TestLoader: Una clase que se usa para cargar pruebas automáticamente.
unittest.result: Un submódulo que contiene clases relacionadas con los resultados de las pruebas.

Aunque unittest no tiene "submódulos" adicionales en su estructura interna, los elementos como TextTestRunner, TextTestResult, y TestLoader pueden ser considerados subcomponentes que trabajan juntos para facilitar la escritura y ejecución de pruebas unitarias en Python"""



