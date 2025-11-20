
import pytest 
import warnings

"""El módulo pytest es una herramienta de testing en Python que facilita la escritura y ejecución de pruebas unitarias. Es conocido por su simplicidad, flexibilidad y potencia, ofreciendo una sintaxis más sencilla y una ejecución de pruebas más eficiente que el módulo estándar unittest

Características principales de pytest:
Sintaxis sencilla: Las pruebas se escriben como funciones que comienzan con test_, y se usan afirmaciones estándar de Python (assert).
Detección automática de pruebas: pytest busca automáticamente en los archivos que comienzan con test_ o terminan en _test.py y ejecuta las funciones que empiezan con test_.
Informes detallados: Ofrece salidas detalladas y coloridas para facilitar la comprensión de los resultados de las pruebas.
Manejo de fixtures: Los "fixtures" son objetos o configuraciones reutilizables que se pueden usar para inicializar el entorno de las pruebas.
Compatibilidad con unittest: pytest puede ejecutar pruebas escritas en unittest y mejorar la salida con su propia interfaz."""

#Ejemplo básico de una prueba con pytest:
# test_example.py 
def test_suma(): assert 1 + 1 == 2 
# Esta prueba pasará 

def test_resta():assert 2 - 1 == 1 
# Esta prueba también pasará 

"""Para ejecutar las pruebas, simplemente usa el comando: pytest 
Ventajas:;No requiere clases: No necesitas definir clases de prueba como en unittest.
Simplicidad: Es fácil de aprender y usar para tareas de testing simples.
Ampliable: Soporta extensiones y plugins que permiten agregar más funcionalidades."""


#Funciones principales de pytest:


#pytest.main() Ejecuta el marco de pruebas de pytest de manera programática. Puedes usarlo para ejecutar pruebas en lugar de usar la línea de comandos. Ejemplo: 
pytest.main() 

#pytest.mark.parametrize() Permite ejecutar una prueba con diferentes valores de entrada. Es útil cuando quieres probar una función con varios conjuntos de datos: 
@pytest.mark.parametrize("a, b, resultado", [ (1, 1, 2), (2, 2, 4), (3, 3, 6) ])
def test_suma(a, b, resultado): assert a + b == resultado 

#pytest.fixture() Permite crear configuraciones reutilizables que pueden ser utilizadas en múltiples pruebas. Las "fixtures" se definen usando este decorador:  
@pytest.fixture 
def setup_data(): return {'a': 1, 'b': 2} 

def test_suma(setup_data): assert setup_data['a'] + setup_data['b'] == 3 

#pytest.mark.skip() Marca una prueba para que sea omitida. Útil cuando no quieres ejecutar una prueba específica: 
@pytest.mark.skip(reason="Prueba omitida") 
def test_omitida(): assert False 

#pytest.mark.xfail() Marca una prueba como que se espera que falle. Si la prueba falla, se considera como "pasada":  
@pytest.mark.xfail
def test_esperado_fallo(): assert 1 + 1 == 3 # Esto fallará, pero se considerará como un éxito 

#pytest.fail() Lanza una excepción de fallo en medio de una prueba, lo que permite fallar explícitamente una prueba:  
def test_falla_explicita(): pytest.fail("Fallando de manera explícita") 

#pytest.set_trace() Activa el depurador de pdb en el punto donde se llama. Útil para la depuración durante las pruebas: 
def test_con_debugger():
  pytest.set_trace() # Inicia el depurador aquí
  assert 2 + 2 == 4 

#pytest.raises() Permite comprobar si una excepción específica se lanza durante la ejecución de una prueba. Se usa como un contexto: 
def test_errores(): 
  with pytest.raises(ZeroDivisionError): 1 / 0 

#pytest.mark.usefixtures() Se utiliza para asociar una o más "fixtures" a un test o clase de tests sin necesidad de pasar los objetos directamente: 
@pytest.fixture 
def fixture_de_datos(): return {"clave": "valor"} 

@pytest.mark.usefixtures("fixture_de_datos")
def test_uso_de_fixture(): assert True 
# El test usará 'fixture_de_datos' sin tener que pasarlo como parámetro 

#pytest.warns() Permite verificar que se lanza una advertencia durante la ejecución de la prueba: 
def test_warning(): 
  with pytest.warns(Warning): warnings.warn("Este es un aviso") 

#pytest.mark.parametrize() Se utiliza para parametrizar pruebas y ejecutar la misma prueba con múltiples conjuntos 
@pytest.mark.parametrize("x, y, resultado", [(2, 3, 5), (1, 1, 2), (4, 5, 9)]) 
def test_suma(x, y, resultado):assert x + y == resultado 

#pytest.mark.timeout() Se utiliza para establecer un límite de tiempo para la ejecución de una prueba. Si una prueba excede el tiempo asignado, se marca como fallida:  @pytest.mark.timeout(2) 
def test_larga_ejecucion(): 
  import time
  time.sleep(3) # Esto fallará porque supera el tiempo de espera 

#Clases principales del módulo pytest:

#pytest.TestCase Esta es una clase que emula la funcionalidad de las pruebas de unittest.TestCase. Aunque pytest no requiere clases de prueba como unittest, puedes usar esta clase si prefieres escribir las pruebas con una estructura de clase: 
class TestOperaciones: 
  def test_suma(self): assert 1 + 1 == 2 
  def test_resta(self): assert 3 - 1 == 2 

#pytest.FixtureDef Esta clase es parte del sistema de fixtures de pytest. Representa una "fixture" que se usa para proporcionar datos o recursos necesarios para las pruebas. Ejemplo: 
@pytest.fixture 
def recurso(): return "un recurso" 

#pytest.raises() (Función que actúa como clase en contextos de excepciones)
#Aunque se usa principalmente como una función, pytest.raises() se comporta de manera similar a una clase en el sentido de que actúa como un contexto dentro del cual se verifica si una excepción es lanzada. Ejemplo:
def test_errores(): 
  with pytest.raises(ZeroDivisionError): 1 / 0 

#pytest.mark pytest.mark no es exactamente una clase, pero se utiliza para aplicar marcas a las pruebas, como skip, parametrize, xfail, etc. Se usa para añadir metadatos a las pruebas. Ejemplo:
@pytest.mark.parametrize("a, b, resultado", [(1, 1, 2), (2, 2, 4)]) 
def test_suma(a, b, resultado): assert a + b == resultado 

#pytest.Session Pytest.Session se refiere a la sesión completa de pruebas que se está ejecutando. Puedes interactuar con esta clase a través de hooks para personalizar el comportamiento de pytest a nivel global. Ejemplo: 
def pytest_sessionstart(session): print("La sesión de pruebas ha comenzado.") 

#pytest.Config Esta clase representa la configuración global de pytest, la cual puedes utilizar para acceder a los valores de configuración personalizados definidos a través de la línea de comandos o de archivos de configuración. Ejemplo: 
def pytest_configure(config):print(f"Configuración de pytest: {config}") 



"""En el módulo pytest, no existen variables globales específicas como en otros módulos, pero hay algunos componentes que puedes considerar variables o elementos con características similares, especialmente en relación con configuraciones o comportamientos dentro de las pruebas. A continuación, se detallan algunas de estas "variables" o componentes clave:

#Componentes similares a variables en pytest:"""

#pytest.config (Global Configuración de pytest)

#Permite acceder a la configuración global de pytest. No es exactamente una variable, pero actúa como una fuente de información sobre la configuración actual de las pruebas, como los argumentos pasados en la línea de comandos, configuraciones en el archivo pytest.ini, etc. Ejemplo: 
def pytest_configure(config): print(f"Configuración de pytest: {config}") 

#pytest.__version__ Esta "variable" devuelve la versión actual de pytest instalada. Es útil para asegurarse de que se está utilizando la versión correcta del módulo. Ejemplo: 
print(pytest.__version__) 

#pytest.durations (Dentro de configuraciones)
#Puede usarse para configurar el tiempo máximo de ejecución de las pruebas, lo que afecta a la duración de la sesión. No es una variable per se, pero puedes configurarla a través de la línea de comandos o en archivos de configuración. Ejemplo:
#pytest --maxfail=1 
#--disable-warnings 

#pytest.exit() Esta función se comporta como una variable que te permite salir de la ejecución de pruebas con un código de estado específico, lo cual detendría todas las pruebas si se invoca de manera programática. Ejemplo: 
pytest.exit("Error en las pruebas", returncode=1) 

#pytest.fail() Similar a exit(), pero esta función marca la prueba como fallida de manera programática en lugar de finalizar todas las pruebas. A veces se usa en el lugar de variables de control para finalizar una prueba. Ejemplo:
pytest.fail("Falló la prueba de manera explícita") 

#pytest.mark Aunque pytest.mark no es una variable en sí, puedes usarlo como una especie de "variable" para marcar pruebas con distintas configuraciones, como skip, xfail, parametrize, etc. Ejemplo:
@pytest.mark.parametrize("x", [1, 2, 3]) 
def test_multiplicacion(x): assert x * 2 == x + x 


#Principales constantes de pytest:

#pytest.SKIP Esta constante se usa cuando una prueba está marcada para ser omitida, por ejemplo, usando la marca @pytest.mark.skip. La constante se devuelve cuando una prueba es omitida. Ejemplo:
@pytest.mark.skip(reason="No disponible por el momento") 
def test_skipped(): assert False 

#pytest.xfail Aunque no es exactamente una constante, se usa como un marcador para indicar que una prueba se espera que falle. Se considera una "constante" en el sentido de que su comportamiento es predecible y controlado. Si la prueba pasa cuando está marcada con xfail, se marca como un "paso falso". Ejemplo: 
@pytest.mark.xfail 
def test_esperado_fallido(): assert 1 + 1 == 3 # Se espera que falle 

#pytest.FAIL Esta constante representa el estado de una prueba fallida. Se usa cuando se requiere comprobar si una prueba ha fallado explícitamente dentro de una sesión de prueba. Ejemplo: 
def test_fallo(): pytest.fail("La prueba ha fallado explícitamente") 

#pytest.PASS Esta constante representa el estado de una prueba exitosa. Similar a pytest.FAIL, es útil para realizar pruebas o verificaciones en función del estado de las pruebas. Ejemplo:
def test_exito(): assert 2 + 2 == 4 # La prueba pasa 

#pytest.mark.parametrize Aunque pytest.mark.parametrize no es una constante per se, es un marcador utilizado con frecuencia que permite parametrizar pruebas, lo que permite la ejecución de la misma prueba con diferentes entradas.: 
@pytest.mark.parametrize("a, b, resultado", [(1, 2, 3), (2, 3, 5), (4, 5, 9)]) 
def test_suma(a, b, resultado): assert a + b == resultado 




#Excepciones principales del módulo pytest:

#pytest.fail() Aunque pytest.fail() no es una excepción en sí misma, se usa para marcar una prueba como fallida de manera programática. Lanza una excepción Failed para señalar que la prueba ha fallado explícitamente. Ejemplo: 
def test_falla_explicita(): pytest.fail("Fallo de prueba explícito") 

#pytest.exit() Esta función se utiliza para salir de la ejecución de las pruebas de manera anticipada, indicando un error con un código de retorno específico. Lanza una excepción Exit para terminar la sesión de pruebas. Ejemplo: 
def test_salida_anticipada(): pytest.exit("Terminando la ejecución de las pruebas") 

#pytest.raises() pytest.raises() se usa en forma de contexto para comprobar que se lanza una excepción durante la ejecución de una prueba. Aunque no es una excepción directamente, permite capturar excepciones y verificar que se lanzan en el contexto adecuado. Ejemplo: 
def test_division_por_cero(): 
  with pytest.raises(ZeroDivisionError): 1 / 0 

#pytest.skip() Esta función permite omitir una prueba. Al llamarla dentro de una prueba, la marca como "skip" y se informa de que fue omitida. No lanza una excepción directamente, pero genera un mensaje de advertencia. Ejemplo: 
def test_omitido():pytest.skip("Esta prueba está omitida por razones específicas") 

#pytest.mark.xfail() xfail es un marcador que se usa para indicar que una prueba se espera que falle. Si la prueba pasa cuando está marcada con xfail, se considera un "paso falso". En términos de excepciones, se comporta de manera similar a una expectativa de fallo. Ejemplo: 
@pytest.mark.xfail 
def test_falla_esperada(): assert 1 + 1 == 3 # Se espera que falle 

#pytest.UnexpectedException Es una clase de excepción generada cuando ocurre un error inesperado durante la ejecución de pruebas. No se lanza comúnmente directamente, pero puede ser utilizada en contextos donde se quiera detectar excepciones no previstas. Ejemplo: 
def test_error_inesperado(): raise pytest.UnexpectedException("Se produjo un error inesperado") 



"""El módulo pytest no tiene submódulos en el sentido estricto de la palabra (es decir, módulos dentro de pytest que funcionen como submódulos separados con su propio propósito). Sin embargo, pytest proporciona varios componentes que puedes importar para extender o configurar las pruebas de diversas maneras."""

#Componentes del módulo pytest que funcionan como "submódulos":

#pytest.mark pytest.mark permite marcar pruebas con decoradores para modificar su comportamiento. Puedes usarlo para aplicar configuraciones como skip, xfail, parametrize, entre otros. Ejemplo:
@pytest.mark.parametrize("x, y", [(1, 2), (3, 4)]) 
def test_suma(x, y): assert x + y == 3 

#pytest.fixture Aunque no es un submódulo en sí, pytest.fixture es una función fundamental que se utiliza para crear recursos que se comparten entre varias pruebas. Las fixtures permiten organizar configuraciones y recursos que se necesitan antes o después de cada prueba. Ejemplo: 
@pytest.fixture 
def ejemplo(): return 42 
def test_uso_fixture(ejemplo): assert ejemplo == 42 

#pytest.plugins pytest.plugins es el mecanismo para acceder a los complementos de pytest. Esto te permite interactuar con cualquier complemento o extensión que puedas haber instalado para extender las capacidades de pytest. Ejemplo:
pytest_plugins = ["pytest_cov", "pytest_django"] 

#pytest.config pytest.config es una interfaz de configuración de pytest. Aunque en versiones modernas de pytest se utiliza el archivo de configuración como pytest.ini o pyproject.toml, también se puede acceder a la configuración a través del módulo pytest.config en versiones anteriores. Ejemplo: 
# Aunque ya no es tan común en las últimas versiones de pytest, aún se encuentra disponible en ciertas configuraciones. 
def pytest_configure(config): config.option.some_option = "value" 

#pytest.templating pytest.templating se usa para crear y renderizar plantillas dentro del marco de pruebas. Es útil para pruebas de plantillas en aplicaciones web. Ejemplo:
def test_plantilla():
# Código para prueba de plantillas web assert True 

#pytest.raises Este es un método que se usa como submódulo para capturar excepciones durante las pruebas. Se utiliza en un contexto with para verificar si se lanza una excepción esperada. Ejemplo:
def test_errores():
  with pytest.raises(ZeroDivisionError): 1 / 0 