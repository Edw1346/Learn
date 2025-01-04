#abrir una archivo
archivo = open("Python\\art_txt.txt", encoding="UTF-8")

#leer un archivo completo
leer_archivo = archivo.read()
#print(leer_archivo)

#leer una linea, si quieres leer cierta parate del texto, solo coloca los caracteres a leer en los parentesis ()
linea = archivo.readline(100)
print(linea)

#leer linea por lineas, 
lineas = archivo.readlines()
print(lineas)

#cerrar una archivo
cerrar = archivo.close()

#Esta forma es un poco defiiemte ya que hay que abrir y cerar el archivo



#Hay otra forma mas eficiente, usar with
#Con with no hay que cerrar el archivo, with lo cierra automaticamente
with open("Python\\art_txt1.txt", encoding="UTF-8") as archivo:
    contenido = archivo.read()  #leer su contenido
    print(contenido)

#Ahora con permisos w (write) este lo que hace es que siempre sobreescribe, no agrega
with open('Python\\art_txt2.txt','w',encoding='UTF-8') as archivo:
    #Escribir en el archivo, pero este solo sobreescribe no añade, se puede hacer varios write
    escribir = archivo.write("Hola macho estoy escribiendo")
    
    #Este sobreescribe varias lineas, debe de ser una lista []
    escribir_lineas = archivo.writelines(["Hola guapo\n", "Como estas?"])


#Ahora con permisos a (apen) este lo que hace es que añade, no sobreescribe
with open('Python\\art_txt2.txt','a',encoding='UTF-8') as archivo:
    #Escribir en el archivo, pero este solo sobreescribe no añade, se puede hacer varios write
    escribir = archivo.write("Hola macho estas escribiendo:\n")
    
    for i in range(5):
        escribir_lineas = archivo.writelines([f"Hola guapo {i}, como estas?", " Eres el mejor\n"])