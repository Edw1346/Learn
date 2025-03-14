import argparser

"""El módulo argparse de Python se utiliza para manejar los argumentos de la línea de comandos en los programas. Permite 
que los usuarios pasen parámetros al ejecutar el script, y el programa puede procesarlos y usarlos dentro del código"""




"""Funciones principales de argparse:"""

#ArgumentParser() Crea un nuevo objeto ArgumentParser, que es la instancia principal usada para gestionar los argumentos de la línea de comandos. Ejemplo: 
parser = argparse.ArgumentParser(description='Mi script de ejemplo.') 

#add_argument() Añade un nuevo argumento o parámetro que el programa espera recibir. Puedes definir varios tipos de argumentos, como posicionados, opcionales, con valores predeterminados, etc. Ejemplo: 
parser.add_argument('nombre', help='Tu nombre')
parser.add_argument('--edad', type=int, help='Tu edad', default=30) 

#parse_args() Analiza los argumentos pasados por la línea de comandos y los convierte en un objeto que se puede usar dentro del código. Ejemplo: 
args = parser.parse_args() 

#print_help() Muestra el mensaje de ayuda del programa, que incluye la descripción y los argumentos disponibles. Ejemplo:
parser.print_help() 

#exit() Termina el programa inmediatamente después de mostrar un mensaje de error o ayuda. Se puede usar para salir con un código de error específico. Ejemplo:
 parser.exit(1) 

#error() Muestra un mensaje de error personalizado y termina el programa con un código de error 2. Ejemplo: 
parser.error('Este es un mensaje de error.') 

#format_help() Devuelve la cadena que contiene el mensaje de ayuda formateado (en lugar de imprimirlo). Ejemplo: 
help_message = parser.format_help() 
print(help_message) 

#add_mutually_exclusive_group() Crea un grupo de argumentos mutuamente exclusivos. Esto significa que solo uno de los argumentos del grupo puede ser proporcionado a la vez. Ejemplo: 
group = parser.add_mutually_exclusive_group() 
group.add_argument('--verbose', action='store_true', help='Salida detallada') 
group.add_argument('--quiet', action='store_true', help='Salida reducida') 

#set_defaults() Establece valores predeterminados para los argumentos que no se pasan. Se puede usar para configurar valores predeterminados para argumentos complejos. Ejemplo:
 parser.set_defaults(edad=25) 

#parse_known_args() Analiza los argumentos de la línea de comandos, pero permite que algunos argumentos no sean reconocidos sin generar un error. Retorna los argumentos desconocidos. Ejemplo: 
args, unknown = parser.parse_known_args() 

#fromfile_prefix_chars: Permite leer los argumentos de un archivo en lugar de pasarlos por la línea de comandos. Utiliza un prefijo especificado para leer un archivo de texto que contenga los argumentos. Ejemplo: 
parser = argparse.ArgumentParser(fromfile_prefix_chars='@') 




"""El módulo argparse de Python incluye algunas clases que son fundamentales para trabajar con los argumentos de la línea 
de comandos. Aquí están las clases principales que proporciona el módulo:"""

#1. ArgumentParser Es la clase principal de argparse. Se utiliza para crear un objeto que procesa los argumentos de la línea de comandos. Permite definir los argumentos que el programa aceptará, analizarlos, generar mensajes de ayuda y más.
#Métodos importantes: 
#add_argument(): Para añadir nuevos argumentos.
#parse_args(): Para analizar los argumentos pasados desde la línea de comandos.
#print_help(): Para mostrar la ayuda del programa. Ejemplo:
parser = argparse.ArgumentParser(description="Mi programa") 

parser.add_argument('--edad', type=int, help="La edad del usuario")
args = parser.parse_args() 

#2. ArgumentDefaultsHelpFormatter Esta clase se utiliza para mostrar los valores predeterminados de los argumentos en el mensaje de ayuda generado por ArgumentParser. Es un formato de presentación que incluye los valores predeterminados de los argumentos en la salida de ayuda. Ejemplo: 
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter) 

#3. RawDescriptionHelpFormatter Esta clase muestra la descripción del programa sin realizar ningún tipo de formato, es decir, lo que se proporciona en el texto se muestra tal cual. Ejemplo: 
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter) 

#4. RawTextHelpFormatter Similar a RawDescriptionHelpFormatter, pero también respeta el formato de los textos largos en la ayuda. Ideal si necesitas mostrar texto en bruto, sin cambios en los saltos de línea. Ejemplo: 
parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter) 

#5. ArgumentParser - Subclase de HelpFormatter HelpFormatter es la clase base para los formateadores que determinan cómo se presenta la ayuda. Se utiliza para mostrar las opciones de ayuda de una manera determinada, controlando cómo se imprimen las descripciones, los valores predeterminados, etc.

#6. ArgumentGroup (en versiones más recientes de argparse) Esta clase permite agrupar los argumentos de manera lógica en el mensaje de ayuda, mejorando la presentación de los argumentos en la salida. Ejemplo: 
group = parser.add_argument_group('Grupo de opciones') 
group.add_argument('--verbose', help='Salida detallada') 






"""Ahora las variables del modulo argparse"""

"""El módulo argparse no tiene variables globales específicas que sean accesibles directamente como en otros módulos, pero 
tiene algunas configuraciones y constantes que se usan de forma indirecta a través de los métodos y clases."""


#ArgumentParser.prog. Es una variable que guarda el nombre del programa que se utiliza en los mensajes de ayuda. Por defecto, se establece con el nombre del archivo de script, pero puede ser modificada. Ejemplo: 
parser = argparse.ArgumentParser()
print(parser.prog) # Muestra el nombre del programa 

#ArgumentParser.description. Es una variable que guarda la descripción del programa que aparecerá en los mensajes de ayuda. Ejemplo:
parser = argparse.ArgumentParser(description="Este es un programa de ejemplo") 

#ArgumentParser.epilog. Es una variable que se usa para agregar texto adicional al final del mensaje de ayuda. Es útil para proporcionar información extra después de la lista de argumentos. Ejemplo:
parser = argparse.ArgumentParser(epilog="Para más información, visita nuestro sitio web.") 

#ArgumentParser.prefix_chars. Define los caracteres que se usarán para identificar los argumentos. Por defecto es '-' para los argumentos de una sola letra y '--' para los de múltiples letras. Ejemplo: 
parser = argparse.ArgumentParser(prefix_chars='-') 

#ArgumentParser.fromfile_prefix_chars. Esta variable especifica el carácter que debe utilizarse para leer los argumentos desde un archivo. Por ejemplo, si se establece en '@', el archivo que contiene los argumentos debe comenzar con @ para que los lea desde el archivo en vez de pasarlos directamente desde la línea de comandos. Ejemplo: 
parser = argparse.ArgumentParser(fromfile_prefix_chars='@') 

#ArgumentParser.exit_on_error. Determina si el programa debe salir automáticamente cuando se encuentra un error en la línea de comandos. Por defecto es True, lo que significa que el programa terminará si encuentra un error. Ejemplo:
parser.exit_on_error = False # Para no terminar el programa en caso de error 




"""El módulo argparse no define muchas constantes como tal, pero tiene algunas que se utilizan con frecuencia en el manejo 
de argumentos. Estas constantes ayudan a definir el comportamiento del análisis de argumentos y la forma en que los 
resultados son presentados."""

#argparse._UNRECOGNIZED_ARGS. Es una constante que representa un grupo de argumentos no reconocidos por el analizador. Se utiliza internamente cuando se encuentran argumentos desconocidos durante el análisis. Ejemplo: 
parser = argparse.ArgumentParser()
 args = parser.parse_args(['--unknown']) # argparse maneja el error de argumento desconocido internamente 

#argparse.SUPPRESS. Esta constante se usa para suprimir la inclusión de un argumento en el mensaje de ayuda, aunque esté definido en el ArgumentParser. Si se establece un argumento con argparse.SUPPRESS, no aparecerá en la ayuda. Ejemplo:
parser = argparse.ArgumentParser() 
parser.add_argument('--secreto', help="No aparecerá en la ayuda", default=argparse.SUPPRESS) 
parser.print_help() # El argumento '--secreto' no aparecerá 

#argparse.REMAINDER. Esta constante se utiliza para captar todos los argumentos restantes no reconocidos, lo que permite que el resto de los argumentos sean procesados como una lista. Ejemplo:
parser = argparse.ArgumentParser()
parser.add_argument('args', nargs=argparse.REMAINDER) 
args = parser.parse_args() print(args.args) # Captura todos los argumentos restantes 

#argparse.Action. Aunque no es una constante en el sentido clásico, Action es una clase que se utiliza para definir cómo se manejarán los valores de los argumentos. Action tiene subclases como store, store_true, store_false, etc., que se usan para especificar cómo se procesan los valores de los argumentos. Ejemplo: 
parser = argparse.ArgumentParser() 
parser.add_argument('--verbose', action='store_true', help="Mostrar más detalles") 





"""El módulo argparse maneja excepciones principalmente para tratar errores que surgen cuando los argumentos proporcionados 
en la línea de comandos son incorrectos o incompletos. Aquí están las excepciones más relevantes que se pueden encontrar 
al trabajar con argparse:"""

Excepciones en el módulo argparse:

#argparse.ArgumentError. Esta excepción es lanzada cuando hay un error relacionado con un argumento específico, como cuando un argumento no se define correctamente o cuando ocurre un error en los valores de los argumentos. Ejemplo: 
parser = argparse.ArgumentParser() 
parser.add_argument('--edad', type=int) 
try: 
    args = parser.parse_args(['--edad', 'abc'])
except argparse.ArgumentError as e:
    print(f"Error en el argumento: {e}") 

#argparse.ArgumentTypeError. Esta excepción se lanza cuando el tipo de un argumento no es el esperado. Por ejemplo, si un argumento espera un número entero y se pasa un valor no numérico, se genera esta excepción. Ejemplo: 
parser = argparse.ArgumentParser() 
parser.add_argument('--edad', type=int) 
try: 
    args = parser.parse_args(['--edad', 'no_es_un_numero']) 
except argparse.ArgumentTypeError as e:
    print(f"Error de tipo: {e}") 

#argparse.MissingRequiredArgument. Esta excepción es lanzada cuando falta un argumento obligatorio que no ha sido proporcionado en la línea de comandos. Ejemplo: 
parser = argparse.ArgumentParser() 
parser.add_argument('--nombre', required=True) 
try: 
    args = parser.parse_args([]) # No se pasa el argumento obligatorio '--nombre' 
except argparse.MissingRequiredArgument as e: 
    print(f"Falta un argumento obligatorio: {e}") 

#argparse.PyArgumentParserError. Esta es una excepción general que se lanza cuando se produce un error no específicamente relacionado con los argumentos individuales, sino con el análisis general de los mismos. Ejemplo: 
parser = argparse.ArgumentParser() 
try: 
    parser.parse_args(['--nombre', 'Juan', '--edad']) 
except argparse.PyArgumentParserError as e: 
    print(f"Error general al procesar los argumentos: {e}") 

argparse.Error. La excepción base para los errores en argparse. Si un error no está relacionado específicamente con un argumento, puede generar un argparse.Error. Ejemplo: 
parser = argparse.ArgumentParser()
try: 
    parser.parse_args(['--edad']) 
except argparse.Error as e:
    print(f"Se produjo un error al procesar los argumentos: {e}") 



"""El módulo argparse no tiene submódulos en el sentido tradicional, como otros módulos de Python que tienen una jerarquía 
de submódulos. Sin embargo, el módulo se organiza en clases y funciones, como hemos visto anteriormente, y no incluye 
submódulos adicionales. Aún así, es importante mencionar que argparse se puede extender mediante la adición de personalizaciones, 
como la creación de nuevos tipos de argumentos o el manejo de la ayuda, pero esto no se considera un submódulo perse."""


