#El módulo xml.etree.ElementTree para procesar y manejar archivos XML. Ofrece herramientas para analizar (parsear), crear y manipular documentos XML de forma eficiente.

import xml.etree.ElementTree as ET # Crear un elemento XML 

#Element(tag, attrib={}, **extra) Crea un nuevo elemento XML con una etiqueta y atributos opcionales: 
root = ET.Element("root") 

#SubElement(parent, tag, attrib={}, **extra). Crea un nuevo elemento XML como subelemento de un elemento parent: 
child1 = ET.SubElement(root, "child", {"id": "2"}) 

#tostring(element, encoding='utf-8', method='xml'). Convierte un elemento XML a una cadena de texto: 
xml_string = ET.tostring(child1) 

child1.text = "Este es un hijo" # Contenido del hijo
child2 = ET.SubElement(root, "child2")
child21 = ET.SubElement(child2, "child21")
child21.text = "Soy el nieto"
child3 = ET.SubElement(root, "child3")
child31 = ET.SubElement(child3, "child31")
child311 = ET.SubElement(child31, "child311")
child311.text = "Soy el bizñieto" 

#ElementTree(element). Crea un objeto ElementTree a partir de un Element (raíz del árbol XML). Ejemplo: 
tree = ET.ElementTree(root) 

#fromstring(text). Analiza una cadena de texto XML y devuelve un objeto Element: 
root = ET.fromstring("<root><child>data</child></root>") 

#parse(source). Analiza un archivo o un objeto tipo archivo y devuelve un objeto ElementTree. Ejemplo: 
tree.write("output.xml") # Parsear un archivo XML 
tree = ET.parse("output.xml") 
root = tree.getroot() 

print(root)
print(root.tag) # 'root' 
print(root[0].tag) # 'child' 
print(root.attrib)
print(root[0].text) # 'Este es un hijo' 
print(root.tail)

#find(xpath). Encuentra el primer subelemento que coincide con el camino XPath. Ejemplo: 
child = root.find(".//child") 

#findall(xpath). Encuentra todos los subelementos que coinciden con el camino XPath. Ejemplo: 
children = root.findall(".//child") 

#findtext(xpath, default=None). Encuentra el texto de un subelemento que coincide con el camino XPath: 
text = root.findtext(".//child") 

#getroot(). Devuelve la raíz del árbol XML: 
root = tree.getroot() 

#write(file, encoding="utf-8", xml_declaration=None, default_namespace=None, method="xml"). Escribe el árbol XML a un archivo: 
tree.write("output.xml") 

#close(). Cierra el archivo de origen (en caso de que haya sido abierto durante un análisis):
tree.close() 

#register_namespace(prefix, uri). Registra un espacio de nombres XML para que pueda ser utilizado al generar documentos XML: 
ET.register_namespace("ns", "http://www.example.com") 

#parse(source). Analiza un archivo XML o un objeto archivo y devuelve un objeto ElementTree que puede ser manipulado: 
tree = ET.parse("example.xml") 



#Clases del Módulo xml.etree.ElementTree

#Element. Representa un único elemento XML. Cada Element tiene un nombre (etiqueta), atributos y una lista de subelementos (hijos): 
element = ET.Element("item", {"id": "1"}) 
print(element.tag) # 'item' 
print(element.attrib) # {'id': '1'} 

#ElementTree. Representa un árbol XML completo. Un objeto ElementTree encapsula un elemento raíz y proporciona métodos para manipular y escribir el árbol completo. Ejemplo: 
tree = ET.ElementTree(element) 
tree.write("output.xml") 

#XMLParser. Esta clase se usa para controlar el análisis de un documento XML. Aunque no es tan común para usuarios básicos, se usa para personalizar cómo se analiza el XML. Ejemplo:
from xml.etree.ElementTree import XMLParser 
parser = XMLParser(target=ET.TreeBuilder()) 

#TreeBuilder. Esta clase se usa internamente para construir un árbol de elementos XML mientras se analiza un archivo o cadena XML. Generalmente no se utiliza directamente en tareas comunes. Ejemplo: 
from xml.etree.ElementTree import TreeBuilder 
builder = TreeBuilder() 

#XML. Analiza un documento XML a partir de una cadena de texto. Esta función es fundamental en la creación de objetos Element desde una cadena XML: 
root = ET.XML("<root><child>data</child></root>") 
