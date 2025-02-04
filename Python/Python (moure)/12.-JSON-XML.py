"""JSON (JavaScript Objet Notion)"""

"""¿Qué es JSON?
JSON es un formato ligero de intercambio de datos, fácil de leer y escribir para los humanos, y fácil de analizar y generar para las máquinas.
Se utiliza comúnmente en APIs y aplicaciones web para el intercambio de datos entre un cliente y un servidor. Los datos en JSON son estructurados como pares clave-valor, similares a un diccionario en Python.

Características de JSON:
Soporta tipos de datos simples como cadenas de texto, números, booleanos, y null.
Puede contener estructuras anidadas como listas y objetos.
Se usa comúnmente en APIs web y en almacenamiento de configuraciones.

Ejemplo de JSON:"""
{ "nombre": "Juan", "edad": 30, "es_estudiante": false, "hobbies": ["leer", "correr", "programar"] } 

"""Trabajar con JSON en Python
Python proporciona el módulo json para convertir entre datos en formato JSON y objetos de Python.

Operaciones Comunes:
Convertir un objeto de Python a JSON (json.dumps):
Convierte un objeto Python (como un diccionario) a una cadena JSON. Ejemplo:"""
import json 
persona = {"nombre": "Juan", "edad": 30, "hobbies": ["leer", "correr"]} 
json_data = json.dumps(persona) 
print(json_data) 

"""Convertir JSON a un objeto Python (json.loads):
Convierte una cadena JSON a un objeto Python (como un diccionario). Ejemplo: """
json_data = '{"nombre": "Juan", "edad": 30, "hobbies": ["leer", "correr"]}' 
persona = json.loads(json_data) 
print(persona["nombre"]) # Output: Juan 

"""Leer JSON desde un archivo (json.load):
Lee datos JSON de un archivo y los convierte en un objeto Python. Ejemplo:"""
with open("data.json", "r") as file: 
    data = json.load(file) 
    print(data) 

"""Escribir un objeto Python en un archivo JSON (json.dump):
Convierte un objeto Python en JSON y lo guarda en un archivo. Ejemplo:"""
persona = {"nombre": "Juan", "edad": 30, "hobbies": ["leer", "correr"]} 
with open("data.json", "w") as file: 
    json.dump(persona, file) 

"""XML (eXtensible Markup Language)"""

"""¿Qué es XML?
XML es un lenguaje de marcado que define un conjunto de reglas para la codificación de documentos en un formato legible tanto para los humanos como para las máquinas.

XML es más pesado que JSON, pero es más flexible en cuanto a la estructura y la definición de etiquetas personalizadas.
Es ampliamente utilizado en aplicaciones que necesitan describir documentos de manera jerárquica, como configuraciones o datos complejos.

Ejemplo de XML:"""
"""<persona> 
<nombre>Juan</nombre> 
<edad>30</edad> 
<es_estudiante>false</es_estudiante> 
<hobbies> 
<hobby>leer</hobby>
 <hobby>correr</hobby> 
</hobbies>
 </persona> """

"""Trabajar con XML en Python
Python ofrece varias bibliotecas para trabajar con XML, siendo xml.etree.ElementTree una de las más utilizadas.

Operaciones Comunes:
Parsear XML desde una cadena (ElementTree):
Convierte una cadena XML en un árbol de elementos. Ejemplo:"""
import xml.etree.ElementTree as ET 
xml_data = '''<persona> <nombre>Juan</nombre> <edad>30</edad> <es_estudiante>false</es_estudiante> <hobbies> <hobby>leer</hobby> <hobby>correr</hobby> </hobbies> </persona>''' 
root = ET.fromstring(xml_data)
print(root.find("nombre").text) # Output: Juan 


#Leer un archivo XML (ET.parse): Lee y analiza un archivo XML. Ejemplo:
tree = ET.parse("persona.xml") 
root = tree.getroot() 
print(root.find("nombre").text) 

#Escribir un objeto Python en XML: Convierte un objeto Python a XML y lo guarda en un archivo. Ejemplo:
import xml.etree.ElementTree as ET 
persona = ET.Element("persona") 
nombre = ET.SubElement(persona, "nombre") 
nombre.text = "Juan" 
edad = ET.SubElement(persona, "edad") 
edad.text = "30" 
tree = ET.ElementTree(persona) 
tree.write("persona.xml") 

#Recorrer un árbol XML: Navegar a través de los elementos XML utilizando funciones como find(), findall(), etc. Ejemplo:
for hobby in root.findall(".//hobby"): 
    print(hobby.text) 



"""Buenas Prácticas con JSON y XML"""

"""JSON:

Usa UTF-8 para la codificación, ya que es el estándar más común.

Utiliza la función json.dump() para escribir datos en un archivo de forma eficiente.
Trata de evitar estructuras de datos muy complejas que puedan hacer el archivo JSON difícil de manejar.

XML:
Utiliza nombres de etiquetas significativos y estructurados de manera jerárquica.
Evita archivos XML innecesariamente largos; cuando sea posible, usa alternativas más ligeras como JSON.
Considera usar XML Schema para validar la estructura de los documentos XML.



Conceptos Relacionados con JSON y XML

   JSON
Serialización (JSON Encoding) y Deserialización (JSON Decoding):

La serialización convierte objetos de Python a una cadena JSON (usando json.dumps()), mientras que la deserialización convierte una cadena JSON de vuelta a un objeto de Python (usando json.loads()).

JSON Schema:
Un JSON Schema es una forma de describir la estructura de un documento JSON, especificando los tipos de datos, los valores posibles y las restricciones para los elementos. Esto se utiliza para validar que los datos JSON cumplan con una estructura específica.

Pares clave-valor:
JSON está basado en la estructura de pares clave-valor, similar a un diccionario de Python, donde cada clave es un string y su valor puede ser cualquier tipo de dato compatible con JSON (números, cadenas, listas, booleanos, etc.).

Codificación y Decodificación (UTF-8):
La codificación UTF-8 es un estándar comúnmente usado para representar texto como una secuencia de bytes, especialmente cuando se trabajan con datos JSON. Asegúrate de usar la codificación adecuada al leer o escribir archivos 

JSON.

APIs RESTful:
Muchas APIs RESTful (Representational State Transfer) utilizan JSON como formato de intercambio de datos. Esto se debe a que JSON es ligero, fácil de leer y se adapta bien a las necesidades de comunicación entre el cliente y el servidor.

JSON Web Tokens (JWT):
JWT es un estándar abierto (RFC 7519) que utiliza JSON para representar información que puede ser transferida de manera segura entre dos partes, especialmente útil en sistemas de autenticación.

Pandas (DataFrames):
Pandas es una librería de Python que permite trabajar con grandes cantidades de datos. pd.read_json() es una función que convierte un archivo JSON o una cadena JSON en un DataFrame, que es una estructura de datos tabular.

   XML

Etiquetas y Atributos:
El formato XML está basado en etiquetas (tags) que contienen información. Cada etiqueta puede tener atributos que brindan más contexto o detalles sobre el contenido de la etiqueta.

DOM (Document Object Model):
El DOM es una representación estructural en memoria de un documento XML. Permite manipular, modificar, y acceder a las partes individuales del XML. En Python, bibliotecas como xml.etree.ElementTree implementan una versión del DOM.

XSD (XML Schema Definition):
XSD es un esquema que define la estructura y los tipos de datos válidos dentro de un archivo XML. Es similar al concepto de JSON Schema, pero para documentos XML.

XPath:
XPath es un lenguaje utilizado para navegar a través de elementos y atributos de un documento XML. Se usa comúnmente para extraer información específica de documentos XML. En Python, puedes utilizar la librería lxml para trabajar con XPath.

XSLT (Extensible Stylesheet Language Transformations):
XSLT es un lenguaje para transformar documentos XML en otros formatos, como HTML, texto o incluso otros documentos XML. Es muy útil cuando se necesita transformar datos XML en otro formato para su visualización o procesamiento.

Namespaces en XML:
Los namespaces son una forma de evitar colisiones de nombres en XML, especialmente en documentos grandes que combinan datos de diferentes fuentes. Se usan para identificar de manera única los elementos y atributos dentro de un documento XML.

SOAP (Simple Object Access Protocol):
SOAP es un protocolo de mensajería basado en XML, utilizado para intercambiar información estructurada entre servicios web. A menudo se utiliza en servicios web más antiguos o más estrictos que requieren una estructura más formal que la que ofrece JSON."""

"""Conceptos Comunes entre JSON y XML"""

"""Formato de Datos Estructurados:
Tanto JSON como XML permiten representar datos de forma estructurada y jerárquica, lo que facilita el intercambio de datos complejos entre diferentes sistemas.

Intercambio de Datos entre Sistemas:
Ambos formatos son utilizados para transmitir datos entre sistemas, como en las comunicaciones cliente-servidor o en el consumo de APIs, especialmente cuando se necesitan representar objetos complejos con relaciones jerárquicas.

Parsing y Generación de Datos:
El parsing es el proceso de leer y analizar un archivo o cadena en JSON o XML para convertirlo en un formato que el programa pueda procesar. La generación de datos es el proceso inverso, donde un programa crea una cadena JSON o 

XML a partir de datos estructurados.

Serialización y Deserialización:
Ambos formatos requieren serialización (convertir datos estructurados a una cadena en el formato adecuado) y deserialización (convertir esa cadena de vuelta a un objeto estructurado). Esto se hace mediante funciones como json.dumps() y json.loads() para JSON, y xml.etree.ElementTree para XML.

Interoperabilidad entre Lenguajes:
JSON y XML son formatos independientes del lenguaje de programación, lo que permite que diferentes lenguajes y tecnologías se comuniquen entre sí sin problemas, ya que ambos son fácilmente manipulables desde cualquier lenguaje moderno.

Reducción de Complejidad:
JSON, por su naturaleza más simple, se utiliza cuando se requiere una forma ligera y rápida de almacenar o transmitir datos. XML es más adecuado para estructuras de datos más complejas o cuando se necesita metadatos adicionales."""