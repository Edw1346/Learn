import xml.etree.ElementTree

"""El módulo xml.etree.ElementTree es una biblioteca estándar de Python para procesar y manejar archivos XML. Ofrece 
herramientas para analizar (parsear), crear y manipular documentos XML de forma eficiente."""

import xml.etree.ElementTree as ET # Crear un elemento XML 
root = ET.Element("root") 
child = ET.SubElement(root, "child") 
child.text = "Este es un hijo" # Crear el árbol y convertirlo a cadena 
tree = ET.ElementTree(root) 
tree.write("output.xml") # Parsear un archivo XML 
tree = ET.parse("output.xml") 
root = tree.getroot() # Acceder a los elementos 
print(root.tag) # 'root' 
print(root[0].tag) # 'child' 
print(root[0].text) # 'Este es un hijo' 



"""Funciones del Módulo xml.etree.ElementTree"""
#Element(tag, attrib={}, **extra) Crea un nuevo elemento XML con una etiqueta y atributos opcionales. Ejemplo: 
import xml.etree.ElementTree as ET 
element = ET.Element("item", {"id": "1"}) 

#SubElement(parent, tag, attrib={}, **extra) Crea un nuevo elemento XML como subelemento de un elemento parent. Ejemplo: 
child = ET.SubElement(parent, "child", {"id": "2"}) 

#tostring(element, encoding='utf-8', method='xml') Convierte un elemento XML a una cadena de texto. Ejemplo: 
xml_string = ET.tostring(element) 
fromstring(text)

#Analiza una cadena de texto XML y devuelve un objeto Element. Ejemplo: 
root = ET.fromstring("<root><child>data</child></root>") 

#parse(source) Analiza un archivo o un objeto tipo archivo y devuelve un objeto ElementTree. Ejemplo: 
tree = ET.parse("file.xml") 
root = tree.getroot() 

#ElementTree(element) Crea un objeto ElementTree a partir de un Element (raíz del árbol XML). Ejemplo: 
tree = ET.ElementTree(element) 

#find(xpath) Encuentra el primer subelemento que coincide con el camino XPath. Ejemplo: 
child = root.find(".//child") 

#findall(xpath) Encuentra todos los subelementos que coinciden con el camino XPath. Ejemplo: 
children = root.findall(".//child") 

#findtext(xpath, default=None) Encuentra el texto de un subelemento que coincide con el camino XPath. Ejemplo: 
text = root.findtext(".//child") 

#getroot() Devuelve la raíz del árbol XML. Ejemplo: 
root = tree.getroot() 

#write(file, encoding="utf-8", xml_declaration=None, default_namespace=None, method="xml") Escribe el árbol XML a un archivo. Ejemplo: 
tree.write("output.xml") 

#close() Cierra el archivo de origen (en caso de que haya sido abierto durante un análisis). Ejemplo:
tree.close() 

#register_namespace(prefix, uri) Registra un espacio de nombres XML para que pueda ser utilizado al generar documentos XML. Ejemplo: 
ET.register_namespace("ns", "http://www.example.com") 

#parse(source) Analiza un archivo XML o un objeto archivo y devuelve un objeto ElementTree que puede ser manipulado. Ejemplo: 
tree = ET.parse("example.xml") 



"""Clases del Módulo xml.etree.ElementTree"""

#Element: Representa un único elemento XML. Cada Element tiene un nombre (etiqueta), atributos y una lista de subelementos (hijos). Ejemplo: 
import xml.etree.ElementTree as ET 
element = ET.Element("item", {"id": "1"}) 
print(element.tag) # 'item' 
print(element.attrib) # {'id': '1'} 

#ElementTree: Representa un árbol XML completo. Un objeto ElementTree encapsula un elemento raíz y proporciona métodos para manipular y escribir el árbol completo. Ejemplo: 
tree = ET.ElementTree(element) 
tree.write("output.xml") 

#XMLParser. Esta clase se usa para controlar el análisis de un documento XML. Aunque no es tan común para usuarios básicos, se usa para personalizar cómo se analiza el XML. Ejemplo:
from xml.etree.ElementTree import XMLParser 
parser = XMLParser(target=ET.TreeBuilder()) 

#TreeBuilder: Esta clase se usa internamente para construir un árbol de elementos XML mientras se analiza un archivo o cadena XML. Generalmente no se utiliza directamente en tareas comunes. Ejemplo: 
from xml.etree.ElementTree import TreeBuilder 
builder = TreeBuilder() 

#XML: Analiza un documento XML a partir de una cadena de texto. Esta función es fundamental en la creación de objetos Element desde una cadena XML.Ejemplo: 
root = ET.XML("<root><child>data</child></root>") 



"""Variables en xml.etree.ElementTree"""

#_namespace_map: Es un diccionario utilizado internamente por ElementTree para gestionar los espacios de nombres XML registrados. Generalmente, no se interactúa con esta variable directamente, pero es crucial para la correcta creación y análisis de XML con espacios de nombres.
#_namespace: Al igual que _namespace_map, esta es una variable interna que administra los espacios de nombres en el contexto de XML, ayudando a resolver y asignar prefijos a los espacios de nombres durante la manipulación de los documentos XML.



"""Constantes en xml.etree.ElementTree"""

#XML_NAMESPACE: Es una constante utilizada para representar el espacio de nombres XML estándar (por ejemplo, el prefijo "xml" que se usa en muchos documentos XML). Sin embargo, no es común que los usuarios interactúen directamente con esta constante.
from xml.etree.ElementTree import XML_NAMESPACE 
print(XML_NAMESPACE) # Muestra el espacio de nombres XML 

#TREE_IMPLEMENTATION: Esta es una constante interna que define la implementación de la estructura de árbol que usa ElementTree. No es comúnmente usada directamente por los usuarios del módulo.

#DOCTYPE: Esta constante se utiliza internamente para verificar el tipo de documento en el proceso de análisis, como en la validación de declaraciones DOCTYPE en los documentos XML. También es más relevante para el funcionamiento interno.



"""Excepciones en xml.etree.ElementTree"""

#ElementTree.ParseError
#Se lanza cuando hay un error durante el análisis (parsing) de un documento XML. Es una subclase de SyntaxError y se utiliza cuando el documento XML no está bien formado. Ejemplo: 
try: 
    tree = ET.parse("archivo_incorrecto.xml") 
except ET.ParseError as e: 
    print(f"Error de análisis XML: {e}") 

#ElementTree.Element
#No es realmente una excepción, sino una clase principal. No obstante, en algunos casos puede generar errores al intentar usar elementos de manera incorrecta.

#TypeError
#Puede ser lanzada en casos donde los tipos de datos no son compatibles, como al pasar un objeto incorrecto a funciones que esperan un tipo específico (por ejemplo, un archivo, cadena de texto o un objeto Element). Ejemplo: 
try:
    tree = ET.fromstring(123) # Pasar un número en lugar de una cadena 
except TypeError as e: 
    print(f"Error de tipo: {e}") 

#OverflowError
#Se lanza si hay un problema de desbordamiento al intentar analizar un XML muy grande. Ejemplo: 
try: 
    tree = ET.parse("archivo_muy_grande.xml") 
except OverflowError as e: 
    print(f"Error de desbordamiento: {e}") 



"""El módulo xml.etree.ElementTree en Python no tiene submódulos explícitos, pero sí contiene varios componentes importantes. 
Dentro de xml.etree, los principales elementos son:"""
#xml.etree.ElementTree – La clase principal para manejar árboles XML.
#xml.etree.ElementPath – Proporciona soporte para consultas XPath simples en elementos XML.

