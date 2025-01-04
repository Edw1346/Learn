#importar el modulo csv para leerlo

"""
import csv

with open('Python\\art_cvs.cvs') as archivo:
    #se usa el metodo de csv reader(), y se coloca el archivo
    #si en archivo hay saltos
    leer = csv.reader(archivo)
    #se recibe un objeto que se puede iterar
    for i in leer:
        for l in i:
            print(l)
"""

#importar el modulo de pandas, pero el modulo se debe de descargar
#se puede hcaer por el cmd del sistema, primero instalar pip y despues pandas


import pandas as pd

print(type(pd))
##leer con pandas
df = pd.read_csv("Python\\art_cvs.cvs")
df2 = pd.read_csv("Python\\art_cvs.cvs")
print(df)
#acceder a encabezados 
encabezado = df['Nombre']
print(encabezado)

#cambiar en nombre de encabezado
cambio_encabezado = df = pd.read_csv("Python\\art_cvs.cvs",names=['name', 'lastname', 'age'])
print(cambio_encabezado)

#ordenar ascendente, se coloca la colunma de referencia 
df_ascendente = df.sort_values("Edades")

#ordenar desendente, se coloca la solumna de refencia y el desendente
df_desendente = df.sort_values("Edades",ascending=False)

#concatenar 2 archivos
concatenar = pd.concat([df, df2])
print(concatenar)

#accdeder a las primeras filas, se coloca el # de filas a visualizar
primeras_filas = df.head(3)
print(primeras_filas)

#acceder a las ultimas filas, se coloca el # de filas a visualizar
ultimas_filas = df.tail(3)
print(ultimas_filas)

#acceder a las columnas y filas, se recibe un conjunto del numero de filas y columnas
filas_y_colmnas  = df.shape
print(filas_y_colmnas)

#obtener numeros estadisticos del dataframe
infomacion  = df.describe()
print(infomacion)

#acceder a un elemento especificion del datafrema, 1 par: filas. 2 par: columnas
elemento_especifico = df.loc[2, "Edades"]
print(elemento_especifico)

#acceder a un elemento especifico de forma de indice, 1 par: filas. 2 par: columnas
elemento_especifico_indice = df.iloc[2,2]
#para accer a el todo de las filas o columnas se coloca el : = [:,1] o [1,:]

#acceder a datos con una condicion
condicion  = df.loc[df["Edades"]>30,:]
print(condicion)
#pasarlos a string, ya que son de tipo numpy.int
df['Edades'] = df['Edades'].astype(str)

#cambiar datos. 1 par: dato a remplazar. 2 par: dato para remplazar. 3 par: comfirmar remplazo
df['Apellidos'].replace("Edwin", "Adrina", inplace=True)

#eliminar filas (axis=0) o columnas(axis=1) que no tiene todos los datos
df.dropna()

#eliminar filas duplicadas
df.drop_duplicates()

#guardar los datos de una tabla (limpia). 1 par: path o direccion
df.to_csv("Python\\tabla_limpia.csv")