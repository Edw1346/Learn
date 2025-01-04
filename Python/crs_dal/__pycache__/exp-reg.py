#importar una libreria de expresiones regulares
import re
#Un parametro de findall, flag, hacer cambios en la busqueda
#re.IGNORECAS=FALSE, ignora las mayusculas y minusculas
#(r"") es para decir que son expresiones regulares

cadena = """Hola maestro como estas? 12
Espero que estes bien necesito una ayuda con 4 expresiones regulares 6
Ocupo aprender a usarlas para poder hacer un programa que me ayude a buscar
"""
#search busca la primera coincidencia, manda un objeto match
resultado = re.search("Hola", cadena) #buscar la palabra Hola con search
print(resultado)

#findall busca todas las coincidencias, manda una lista con todas las coincidencias
resultado = re.findall("Hola", cadena) #buscar la palabra Hola con findall
print(resultado)

"""En la expresiones cada letra es una regla de busqueda y cada una tiene un significado
Se puede negar la expresion con el \, ejemplo \d busca todo menos digitos numericos"""

#\d busca digito numerico del 0 al 9
resultado = re.findall(r"\d", cadena) #buscar digitos numericos
print(resultado)

#\D busca todo menos digito numerico del 0 al 9
resultado = re.findall("", cadena) #buscar todo menos digitos numericos
print(resultado)

#\w busca cualquier caracter alfanumerico [a-zA-Z0-9_]
resultado = re.findall(r"\w", cadena) #buscar alfanumericos
print(resultado)

#\W busca todo menos caracter alfanumerico [ , . ? \n]
resultado = re.findall(r"\W", cadena) #buscar todo menos alfanumericos
print(resultado)

#\s busca cualquier espacio en blanco, tabs, saltos y demas [ \t\n\r\f\v]
resultado = re.findall(r"\s", cadena) #b|
print(resultado) 

#\S busca todo menos espacio en blanco, alfanumericos y demas
resultado = re.findall(r"\S", cadena) #buscar todo menos espacios en blanco
print(resultado) 

#. busca cualquier caracter excepto nueva linea
resultado = re.findall(r".", cadena) #buscar cualquier caracter
print(resultado) 

#\n busca nueva linea
resultado = re.findall(r"\n", cadena) #buscar nueva linea
print(resultado) 

#\ cancela el significado de la expresion o caracteres especiales
resultado = re.findall(r"\d", cadena) #buscar digitos numericos
print(resultado)

#^ busca el inicio de la cadena	
resultado = re.findall(r"^", cadena) #el parameto flag re.MULTILINE busca el inicio de cada linea
print(resultado)

#$ busca el final de la cadena
resultado = re.findall(r"$", cadena) #busca el final de la cadena
print(resultado)

#{n} busca n cantidad de caracteres, como buscar 3 digitos numericos
resultado = re.findall(r"\s{3}", cadena) #buscar 3 espacios en blanco
print(resultado)

#{n, m} busca de n a m cantidad de caracteres como un rango, como buscar de 3 a 5 digitos numericos
resultado = re.findall(r"\d{1,4}", cadena) #buscar de 1 a 4 digitos numericos
print(resultado)

#busca sin () grupo de caracteres
resultado = re.findall(r"ab{2,4}", cadena) #buscar la letra a seguida de la letra b de 2 a 4 veces
print(resultado)

#() busca un grupo de caracteres, como buscar una palabra
resultado = re.findall(r"(ab){2,4}", cadena) #buscar la palabra ab de 2 a 4 veces
print(resultado)

#[ab] busca cualquier caracter dentro de los corchetes
resultado = re.findall(r"[ab]{2}", cadena) #buscar la letra a o b de 2 veces
print(resultado)

#| busca una o otra expresion, como un else o sino
resultado = re.findall(r"(ab){2}|Hola", cadena) #buscar la palabra ab de 2 veces o la palabra Hola, 
# envia la primera coincidencia que encuentre
print(resultado)

""" * busca 0 o mas repeticiones de un caracter, opera sobre el caracter anterior"""
resultado = re.findall(r"\d*", cadena) #buscar 0 o mas digitos numericos
print(resultado)

#+ busca 1 o mas repeticiones de un caracter, opera sobre el caracter anterior, se usa para validar si un caracter esta o no
resultado = re.findall(r"[ab]+", cadena) #buscar 1 o mas letras a o b
print(resultado)

#- busca 0 o 1 repeticion de un caracter, opera sobre el caracter anterior, se usa para validar si un caracter esta o no
resultado = re.findall(r"[ab]-", cadena) #buscar 0 o 1 letras a o b
print(resultado)

#% comodin, valida la expresion anterior y la siguiente, se usa para buscar cualquier caracter
resultado = re.findall(r"[a-z%+]", cadena) #buscar cualquier caracter de la a a la z, % o +
print(resultado)

#[-] separa un rango de caracteres, como buscar de la a a la z
resultado = re.findall(r"[a-zA-Z0-9._+-]", cadena) #buscar cualquier caracter alfanumerico
print(resultado)

"""? busca 0 o 1 repeticion de un caracter, se usa para validar si un caracter esta o no"""
resultado = re.findall(r"", cadena) #
print(resultado)

#Hacer busquedas de palabras especificas, combinando expresiones regulares, devulve el resultado con ese patron
resultado = re.findall(r"\d.\s", cadena) #buscar un numero seguido de un punto y un espacio
print(resultado)

"""Resumen de expresiones regulares"""
#\d busca digito numerico del 0 al 9
#\D busca todo menos digito numerico del 0 al 9
#\w busca cualquier caracter alfanumerico [a-zA-Z0-9_]
#\W busca todo menos caracter alfanumerico [ , . ? \n]
#\s busca cualquier espacio en blanco, tabs, saltos y demas [ \t\n\r\f\v]
#\S busca todo menos espacio en blanco, alfanumericos y demas
#. busca cualquier caracter excepto nueva linea
#\n busca nueva linea
#\ cancela el significado de la expresion o caracteres especiales
#^ busca el inicio de la cadena	
#$ busca el final de la cadena
#{n} busca n cantidad de caracteres, como buscar 3 digitos numericos
#{n, m} busca de n a m cantidad de caracteres como un rango, como buscar de 3 a 5 digitos numericos
#() busca un grupo de caracteres, como buscar una palabra
#[ab] busca cualquier caracter dentro de los corchetes
#| busca una o otra expresion, como un else o sino
"""* busca 0 o mas repeticiones de un caracter, opera sobre el caracter anterior"""
#+ busca 1 o mas repeticiones de un caracter, opera sobre el caracter anterior, se usa para validar si un caracter esta o no
#- busca 0 o 1 repeticion de un caracter, opera sobre el caracter anterior, se usa para validar si un caracter esta o no
#% comodin, valida la expresion anterior y la siguiente, se usa para buscar cualquier caracter
#[-] separa un rango de caracteres, como buscar de la a a la z
"""? busca 0 o 1 repeticion de un caracter, se usa para validar si un caracter esta o no"""
#Hacer busquedas de palabras especificas, combinando expresiones regulares, devulve el resultado con ese patron. re.findall(r"\d.\s", cadena)

#cadena = re.sub(valor_a_remplazar, remplazo, cadena_de_caracteres) remplaza un valor por otro en una cadena
#cadena = re.match(valor_a_buscar, cadena_de_caracteres) busca el valor al inicio de la cadena o que sea igual

