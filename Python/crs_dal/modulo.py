#para asignarle un nombre al modulo es con as:
import submodulo as submodulosaludo

modulo = submodulosaludo.saludar("Edwin","super guapo")
print(modulo)


#para solo importar metodos o funciones 
from submodulo import sumar as sumastotal

print(sumastotal(2,4,5,6,7))

#para ver las propiedades de los modulos 
print(dir(submodulosaludo))

#para ver los modulos de python es 
import sys
print(sys.builtin_module_names)

#para ver los modulo en el equipo
print(sys.path)

#para acceder modulos fuera del directorio de modulos, es agregar el pach, se agrega el enlace absoluta
sys.path.append("c:\\user\\...")

#despues puedes acceder a ese modulo: import .. as ...
#paquetes, es un directorio de modulos
#para tener paquetes en pytho, necesita que el directorio tenga una arhivo
#el archivo se debe de llamar __int__.py