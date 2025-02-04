"""Enumeraciones en Python (Enumerations o enum)"""

"""1. Características principales de las enumeraciones
Legibilidad: Los valores son identificados por nombres, no por números.
Inmutabilidad: Los valores en una enumeración no cambian.
Orden: Las enumeraciones tienen un orden definido y pueden compararse.
Nombres únicos: Cada nombre dentro de una enumeración es único.
Enumeraciones personalizadas: Puedes definir métodos y comportamientos para las enumeraciones.

2. Crear una enumeración
Para definir una enumeración, se utiliza el módulo enum y la clase Enum.

Ejemplo básico:"""
from enum import Enum 
class DiasSemana(Enum): 
    LUNES = 1
    MARTES = 2 
    MIERCOLES = 3 
    JUEVES = 4 
    VIERNES = 5 

"""3. Acceder a valores de una enumeración
Puedes acceder a los miembros de una enumeración mediante su nombre o valor."""
print(DiasSemana.LUNES) # Output: DiasSemana.LUNES 
print(DiasSemana.LUNES.name) # Output: LUNES
print(DiasSemana.LUNES.value) # Output: 1 

"""4. Iterar sobre una enumeración
Las enumeraciones son iterables, por lo que puedes recorrer todos sus miembros."""
for dia in DiasSemana:
    print(dia) 

"""Salida:
DiasSemana.LUNES 
DiasSemana.MARTES 
DiasSemana.MIERCOLES
DiasSemana.JUEVES 
DiasSemana.VIERNES"""

"""5. Métodos principales
Verificar la pertenencia:
Puedes comprobar si un valor pertenece a una enumeración."""
print(DiasSemana(1)) # Output: DiasSemana.LUNES 
print(1 in DiasSemana.__members__.values()) # Output: True 

#Comparación: Los miembros de una enumeración son únicos y pueden compararse.
print(DiasSemana.LUNES == DiasSemana.MARTES) # Output: False 

#Listar nombres y valores:
print(list(DiasSemana)) # Lista todos los miembros. 

"""6. Subclases de Enum
Python permite trabajar con otras clases derivadas de Enum, como IntEnum, Flag y IntFlag.

6.1 IntEnum
Extiende Enum, pero asegura que los valores sean enteros."""
from enum import IntEnum
class Nivel(IntEnum): 
    BAJO = 1 
    MEDIO = 2 
    ALTO = 3 

"""6.2 Flag e IntFlag
Estas variantes permiten realizar operaciones binarias (AND, OR) entre los miembros."""
from enum import Flag 
class Permisos(Flag): 
    LEER = 1 
    ESCRIBIR = 2
    EJECUTAR = 4 

"""7. Enumeraciones con métodos personalizados

Puedes agregar métodos dentro de tus enumeraciones."""
class Colores(Enum): 
    ROJO = "#FF0000" 
    VERDE = "#00FF00"
    AZUL = "#0000FF" 
    def hex(self):
        return f"Color en hexadecimal: {self.value}" 

print(Colores.ROJO.hex()) # Output: Color en hexadecimal: #FF0000 

"""8. Buenas prácticas con enumeraciones
Usar nombres claros: Los nombres de las enumeraciones deben ser descriptivos y consistentes.
Evitar cambios posteriores: Los valores de las enumeraciones son constantes; no deberían modificarse.
Iterar con cuidado: Iterar sobre enumeraciones grandes puede afectar el rendimiento.
Mantener valores únicos: Evitar usar valores repetidos dentro de una misma enumeración."""


"""El módulo enum"""
"""El módulo enum introduce un tipo de datos especial llamado Enum que permite definir conjuntos de valores simbólicos asociados a constantes. Es útil para definir opciones, estados, o categorías con nombres significativos. Por ejemplo:"""
from enum import Enum 
class Color(Enum):
    ROJO = 1 
    VERDE = 2 
    AZUL = 3 
#Aquí, Color es una enumeración con tres miembros: ROJO, VERDE y AZUL.

"""2. Clases principales del módulo enum
2.1 Enum
Es la clase base para definir enumeraciones estándar con nombres simbólicos y valores constantes."""
from enum import Enum
class Dias(Enum): 
    LUNES = 1 
    MARTES = 2
    MIERCOLES = 3 

"""2.2 IntEnum
Es una subclase de Enum que asegura que los valores de los miembros sean enteros y permite operaciones aritméticas."""
from enum import IntEnum 
class Nivel(IntEnum): 
    BAJO = 1 
    MEDIO = 2 
    ALTO = 3 

"""2.3 Flag
Permite definir banderas (flags) binarias que pueden combinarse usando operadores bit a bit (|, &, etc.)."""
from enum import Flag 
class Permisos(Flag):
    LEER = 1 
    ESCRIBIR = 2 
    EJECUTAR = 4 

"""2.4 IntFlag
Es similar a Flag, pero garantiza que los valores sean enteros.

3. Crear enumeraciones
3.1 Enumeraciones básicas"""
from enum import Enum 
class Estado(Enum): 
    ACTIVO = "activo" 
    INACTIVO = "inactivo" 
    PENDIENTE = "pendiente" 

"""3.2 Enumeraciones con valores automáticos
Usa la función auto() para asignar valores automáticamente."""
from enum import Enum, auto 
class Dias(Enum): 
    LUNES = auto() 
    MARTES = auto() 
    MIERCOLES = auto() 

"""4. Acceder a los miembros de una enumeración
4.1 Por nombre"""
print(Dias.LUNES) # Output: Dias.LUNES 
print(Dias.LUNES.name) # Output: LUNES 

#4.2 Por valor
print(Dias(1)) # Output: Dias.LUNES 

#5. Iterar y listar miembros
for dia in Dias: 
    print(dia.name, dia.value) # Output: # LUNES 1 # MARTES 2 # MIERCOLES 3 

"""6. Métodos principales
6.1 name y value
Accede al nombre y al valor del miembro."""
print(Dias.LUNES.name) # Output: LUNES 
print(Dias.LUNES.value) # Output: 1 

"""6.2 __members__
Devuelve un diccionario de todos los miembros de la enumeración."""
print(Dias.__members__) # Output: {'LUNES': Dias.LUNES, 'MARTES': Dias.MARTES, 'MIERCOLES': Dias.MIERCOLES} 

"""6.3 Enum()
Convierte un valor en su miembro de enumeración correspondiente."""
print(Dias(1)) # Output: Dias.LUNES 

"""7. Comparación de miembros
Los miembros de una enumeración son únicos y pueden compararse:"""
print(Dias.LUNES == Dias.MARTES) # Output: False print(Dias.LUNES == Dias.LUNES) # Output: True 

"""8. Enumeraciones avanzadas
8.1 Métodos personalizados
Las enumeraciones pueden incluir métodos personalizados."""

class Color(Enum): 
    ROJO = "#FF0000" 
    VERDE = "#00FF00"
    AZUL = "#0000FF" 
    def hex(self): 
        return f"Color hexadecimal: {self.value}" 

print(Color.ROJO.hex()) # Output: Color hexadecimal: #FF0000 

"""8.2 Enumeraciones con valores repetidos
Puedes usar el decorador @enum.unique para garantizar que los valores sean únicos."""
from enum import Enum, unique 

@unique
class Estado(Enum): 
    ACTIVO = 1 
    INACTIVO = 2 
    ENDIENTE = 1 
# Lanza un error porque los valores no son únicos 

"""9. Usos comunes del módulo enum
Definir estados de un sistema:"""
class Estado(Enum): 
    INICIO = 0 
    PROCESANDO = 1 
    FINALIZADO = 2 

#Definir constantes:
class Meses(Enum): 
    ENERO = 1 
    FEBRERO = 2 
    MARZO = 3 

#Flags y permisos:
from enum import Flag
class Permisos(Flag): 
    LEER = 1
    ESCRIBIR = 2
    EJECUTAR = 4 
    permiso = Permisos.LEER | Permisos.EJECUTAR 
    print(permiso) # Output: Permisos.LEER|EJECUTAR 

#Asignación automática de valores:
class DiasAuto(Enum):
    LUNES = auto() 
    MARTES = auto() 

"""10. Buenas prácticas con enum
Nombres claros: Usa nombres significativos para cada miembro.
Evita modificar valores: Los miembros de las enumeraciones son inmutables.
Agrupa constantes relacionadas: Usa enumeraciones para colecciones lógicas de constantes.
Documentación: Documenta tus enumeraciones para mejorar la comprensión del código.
"""

