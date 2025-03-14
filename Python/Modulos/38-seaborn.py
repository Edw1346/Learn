import seaborn

"""Seaborn es una biblioteca de visualización de datos basada en Matplotlib que facilita la creación de gráficos estadísticos "
atractivos y complejos con un código más sencillo y más opciones de personalización. Está diseñada para trabajar con datos "
"estructurados, como pandas DataFrames, y proporciona funciones para crear gráficos estadísticos de manera rápida."""

#Ejemplo básico:
import seaborn as sns
import matplotlib.pyplot as plt # Cargar un conjunto de datos incorporado de seaborn 
tips = sns.load_dataset("tips") 
# Crear un gráfico de barras con seaborn 
sns.barplot(x="day", y="total_bill", data=tips) 
# Mostrar el gráfico 
plt.show() 


"""Funciones del módulo Seaborn"""

#seaborn.set() Configura el estilo de los gráficos.
import seaborn as sns 
sns.set(style="whitegrid") 

#seaborn.set_context() Ajusta el contexto de los gráficos (por ejemplo, para presentaciones, publicaciones, etc.).
sns.set_context("talk") 

#seaborn.set_palette() Establece la paleta de colores utilizada en los gráficos.
sns.set_palette("husl") 

#seaborn.load_dataset() Carga conjuntos de datos de ejemplo que están integrados en Seaborn.
tips = sns.load_dataset("tips") 

#seaborn.pairplot() Crea una matriz de gráficos de dispersión entre todas las variables de un DataFrame.
sns.pairplot(tips) 

#seaborn.corrplot() (deprecated) Crea una matriz de correlación visualmente atractiva.
sns.heatmap(tips.corr(), annot=True) 

#seaborn.heatmap() Crea un mapa de calor de datos 2D.
sns.heatmap(data) 

#seaborn.boxplot() Crea un diagrama de caja para representar la distribución de los datos.
sns.boxplot(x="day", y="total_bill", data=tips) 

#seaborn.violinplot() Crea un gráfico de violín para mostrar la distribución y la densidad de los datos.
sns.violinplot(x="day", y="total_bill", data=tips) 

#seaborn.barplot() Crea un gráfico de barras para comparar valores entre diferentes categorías.
sns.barplot(x="day", y="total_bill", data=tips) 

#seaborn.countplot() Crea un gráfico de barras para contar las observaciones de categorías.
sns.countplot(x="day", data=tips) 

#seaborn.distplot() (deprecated, ahora histplot) Crea un histograma o gráfico de densidad para visualizar distribuciones.
sns.histplot(tips["total_bill"], kde=True) 

#seaborn.histplot() Crea un histograma de los datos con la opción de agregar la función de densidad.
sns.histplot(tips["total_bill"], kde=True) 

#seaborn.kdeplot() Crea un gráfico de estimación de densidad kernel (KDE) para representar la distribución de una variable.
sns.kdeplot(tips["total_bill"]) 

#seaborn.stripplot() Crea un gráfico de dispersión para visualizar los datos categóricos.
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True) 

#seaborn.regplot() Crea un gráfico de dispersión con una línea de regresión ajustada.
sns.regplot(x="total_bill", y="tip", data=tips) 

#seaborn.lmplot() Crea un gráfico de regresión lineal con más flexibilidad y para múltiples variables.
sns.lmplot(x="total_bill", y="tip", data=tips) 

#seaborn.factorplot() (deprecated, ahora catplot) Crea gráficos de categorías, como boxplots, violin plots o scatter plots.
sns.catplot(x="day", y="total_bill", data=tips, kind="box") 

#seaborn.catplot() Función flexible para crear gráficos categóricos, como boxplots, violinplots, stripplots, etc.
sns.catplot(x="day", y="total_bill", data=tips, kind="violin") 

#seaborn.jointplot() Crea un gráfico de dispersión con los histogramas marginales.
sns.jointplot(x="total_bill", y="tip", data=tips) 

#seaborn.pairgrid() Crea una malla de gráficos para visualizar relaciones entre varias variables.
g = sns.PairGrid(tips) 
g.map_lower(sns.kdeplot) 
g.map_diag(sns.histplot) 

#seaborn.FacetGrid() Facilita la visualización de gráficos faceteados, es decir, gráficos separados por categorías.
g = sns.FacetGrid(tips, col="sex", row="time") 
g.map(sns.scatterplot, "total_bill", "tip") 

#seaborn.despine() Elimina los bordes del gráfico para una visualización más limpia.
sns.despine() 

#seaborn.set_style() Cambia el estilo visual de los gráficos (blanco, oscuro, etc.).
sns.set_style("darkgrid") 

#seaborn.set_palette() Cambia la paleta de colores que se usa en los gráficos.
sns.set_palette("Blues") 

#seaborn.set_context() Ajusta el contexto para gráficos (puede ser para publicaciones, conferencias, etc.).
sns.set_context("talk") 

#seaborn.load_dataset() Carga datasets incorporados en Seaborn para realizar ejemplos.
df = sns.load_dataset("titanic") 

#seaborn.color_palette() Devuelve una lista de colores que se usan en Seaborn.
sns.color_palette("Set1", as_cmap=True) 

#seaborn.palplot() Muestra una paleta de colores visualmente.
sns.palplot(sns.color_palette("husl")) 

#Funciones para visualización estadística: pairplot(), heatmap(), boxplot(), violinplot(), barplot(), countplot(), histplot(), kdeplot(), regplot(), lmplot(), catplot().
#Funciones de manipulación de estilo: set(), set_context(), set_palette(), set_style().
#Funciones de personalización: despine(), color_palette(), palplot().


"""Clases del módulo Seaborn"""

#seaborn.AxesSubplot
#Es la clase principal para manejar los subgráficos dentro de una figura. Cuando se crea un gráfico en Seaborn, la mayoría de las veces se utiliza una instancia de esta clase. Uso: No se utiliza directamente, pero es la clase subyacente para muchos gráficos.
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips") 
ax = sns.barplot(x="day", y="total_bill", data=tips)
plt.show() 

#seaborn.PairGrid
#Esta clase permite crear una cuadrícula de gráficos de pares, es decir, gráficos de todas las combinaciones posibles entre las variables de un conjunto de datos. Uso: Usado para crear una malla de gráficos. Puedes mapear funciones de visualización a las diferentes partes de la cuadrícula.
tips = sns.load_dataset("tips")
g = sns.PairGrid(tips) 
g.map_lower(sns.kdeplot) 
g.map_diag(sns.histplot) 
plt.show() 

#seaborn.FacetGrid
#Permite crear una cuadrícula de gráficos para visualizar los datos de forma segmentada por una o más variables. Uso: Se usa para crear gráficos "facetados", que se organizan por categorías (por ejemplo, por diferentes valores de una columna).
tips = sns.load_dataset("tips")
g = sns.FacetGrid(tips, col="sex", row="time") 
g.map(sns.scatterplot, "total_bill", "tip") 
plt.show() 

#seaborn.ColorPalette
#Representa una paleta de colores en Seaborn. Se puede usar para aplicar colores consistentes a los gráficos. Uso: Sirve para seleccionar y utilizar colores dentro de los gráficos.
palette = sns.color_palette("husl", 8) 
sns.palplot(palette) 
plt.show() 

#seaborn.Palette (no tan común, es una versión más flexible de ColorPalette)
#Es una clase para trabajar con paletas de colores de manera más avanzada y flexible.
palette = sns.dark_palette("purple", reverse=True) 
sns.palplot(palette) 
plt.show() 

#AxesSubplot: Clase subyacente de los gráficos en Seaborn.
#PairGrid: Crea una cuadrícula de gráficos de pares (relaciones entre múltiples variables).
#FacetGrid: Crea una cuadrícula de gráficos faceteados (visualización segmentada por categorías).
#ColorPalette: Clase que representa y maneja paletas de colores para los gráficos.
#Palette: Una versión más avanzada para trabajar con colores.


"""Variables importantes en Seaborn"""

#seaborn.color_palette()
#Esta función devuelve una lista de colores que se utilizan en los gráficos. Puedes especificar el nombre de una paleta o una secuencia de colores.
palette = sns.color_palette("husl", 8) 

#seaborn.palettes
#Es un módulo que contiene varias paletas de colores predefinidas en Seaborn, como deep, muted, pastel, dark, entre otras. Estas son paletas de colores que se pueden utilizar directamente.
sns.palettes.color_palette("dark:#5A9_r") 

#seaborn.axes_style()
#Esta función devuelve los estilos predeterminados para los ejes de los gráficos (por ejemplo, el color de fondo, las líneas de los ejes, etc.). Esta variable se puede utilizar para aplicar un estilo global en los gráficos.
sns.axes_style("darkgrid") 

#seaborn.plotting_context()
#Esta función permite definir el contexto de los gráficos, ajustando elementos visuales como el tamaño de las fuentes o los anchos de las líneas para diferentes propósitos (por ejemplo, "paper", "talk", "poster").
sns.plotting_context("talk") 

#seaborn.despine()
#Aunque no es una variable per se, esta función puede modificar la apariencia del gráfico, eliminando los bordes del gráfico para hacer que los gráficos se vean más limpios y estéticos.
sns.despine() 

#seaborn.xkcd_palette()
#Devuelve una paleta de colores basada en el estilo de los cómics XKCD. Es una forma divertida de cambiar los colores en un gráfico.
xkcd_colors = sns.xkcd_palette(["blue", "orange", "green"]) 
sns.palplot(xkcd_colors) 


"""Constantes principales en Seaborn"""

#seaborn.dark_palette()
#Constante de paleta: Utiliza una paleta de colores oscuros, ideal para gráficos con un esquema de colores más oscuro.
sns.dark_palette("purple") 

#seaborn.light_palette()
#Constante de paleta: Utiliza una paleta de colores claros, generalmente útil para gráficos con un estilo más sutil y suave.
sns.light_palette("blue") 

#seaborn.color_palette()
#Constante de paleta: Devuelve las paletas de colores predefinidas, como deep, muted, pastel, dark, etc.
sns.color_palette("deep") 

#seaborn.desaturate()
#Constante de color: Esta función reduce la saturación de un color para hacerlo más suave.
sns.desaturate("red", 0.5) 

#seaborn.palplot()
#Constante de paleta: Aunque es una función, esta permite visualizar las paletas de colores disponibles, lo que puede considerarse una "constante" al ser un valor que se puede usar repetidamente.
sns.palplot(sns.color_palette("pastel")) 

#seaborn.set_context()
#Constante de contexto: Define las opciones de contexto predeterminadas, como "paper", "talk", "poster", "notebook", que cambian el tamaño y otros detalles visuales de los gráficos.
sns.set_context("talk") 

#seaborn.axes_style()
#Constante de estilo de ejes: Define el estilo global para los ejes de los gráficos (por ejemplo, "white", "darkgrid", "ticks", etc.).
sns.set_style("darkgrid") 

#seaborn.__version__
#Constante de versión: Retorna la versión de Seaborn instalada.
print(sns.__version__) 


"""Excepciones comunes en Seaborn"""

#ValueError
#Esta es probablemente la excepción más común que se lanza en Seaborn cuando los parámetros proporcionados no son válidos. Puede ocurrir si se pasan datos incorrectos, como un tipo de datos no esperado o un número incorrecto de argumentos a una función. Ejemplo: 
import matplotlib.pyplot as plt
# Causa ValueError: No hay suficientes datos para mapear a la variable 'x'
tips = sns.load_dataset("tips") 
sns.barplot(x="non_existent_column", y="total_bill", data=tips)
plt.show() 

#TypeError
#Esta excepción ocurre cuando un tipo de dato no es el esperado, como pasar un tipo incorrecto de datos para un gráfico, por ejemplo, pasando un objeto que no es un DataFrame a una función de Seaborn. Ejemplo: 
import matplotlib.pyplot as plt 
# Causa TypeError porque 'None' no es un tipo de datos válido 
sns.barplot(x="day", y="total_bill", data=None) 
plt.show() 

#KeyError
#Esta excepción se lanza cuando el nombre de la columna proporcionado no existe en el DataFrame de entrada. Suele ocurrir si se hace referencia a una columna inexistente. Ejemplo: 
import matplotlib.pyplot as plt 
# Causa KeyError: La columna 'non_existent_column' no está en el DataFrame 
tips = sns.load_dataset("tips") 
sns.barplot(x="non_existent_column", y="total_bill", data=tips) 
plt.show() 

#AttributeError
#Ocurre cuando se intenta acceder a un atributo o método que no está disponible en el objeto. En Seaborn, esto puede ocurrir si intentas utilizar un atributo que no es válido para el objeto que has creado. Ejemplo: 
# Causa AttributeError porque 'FacetGrid' no tiene el atributo 'invalid_method' 
tips = sns.load_dataset("tips") 
g = sns.FacetGrid(tips) 
g.invalid_method() 

#IndexError
#Puede ocurrir si intentas acceder a un índice fuera de rango en una estructura de datos o al intentar usar un índice en un gráfico que no existe. Ejemplo:
tips = sns.load_dataset("tips")
sns.barplot(x="day", y="total_bill", data=tips[1000:])
# Índice fuera de rango 


"""Submódulos de Seaborn"""

#seaborn.algorithms
#Contiene funciones de bajo nivel que se utilizan para calcular y ajustar aspectos de los gráficos antes de que se tracen, como el ajuste de curvas o la generación de modelos estadísticos. Uso:
import seaborn.algorithms as sns_alg 

#seaborn.axisgrid
#Contiene las clases y funciones relacionadas con la creación de grids (cuadrículas) y la disposición de subgráficos (como FacetGrid y PairGrid). Uso: 
import seaborn.axisgrid as sns_grid 

#seaborn.categorical
#Este submódulo incluye funciones para crear gráficos categóricos, como barplot, boxplot, violinplot, entre otros. Uso: 
import seaborn.categorical as sns_cat 

#seaborn.colors
#Contiene herramientas para trabajar con colores, como la creación de paletas de colores y la manipulación de los mismos. Uso: 
import seaborn.colors as sns_colors 

#seaborn.distributions
#Proporciona funciones para crear gráficos de distribución como distplot, kdeplot y otros gráficos relacionados con la visualización de distribuciones de datos. Uso: 
import seaborn.distributions as sns_dist 

#seaborn.external
#Contiene funciones que permiten integrar o trabajar con bibliotecas externas o formatos de datos  adicionales, como herramientas de visualización avanzadas. Uso:
import seaborn.external as sns_ext 

#seaborn.matrix
#Contiene funciones para crear gráficos de matrices, como heatmap y otros gráficos donde las relaciones entre variables pueden mostrarse en formato matricial. Uso:
import seaborn.matrix as sns_matrix 

#seaborn.rcmod
#Este submódulo se usa para configurar y personalizar los parámetros de Matplotlib. Es útil para ajustar el estilo global de todos los gráficos creados con Seaborn. Uso: 
import seaborn.rcmod as sns_rc 

#seaborn.regression
#Contiene herramientas específicas para la creación de gráficos de regresión, como regplot y lmplot. Uso: 
import seaborn.regression as sns_reg 

#seaborn.timeseries
#Proporciona herramientas para trabajar con datos de series temporales y crear gráficos relacionados con series temporales. Uso:
import seaborn.timeseries as sns_ts 

#algorithms: Funciones de bajo nivel para cálculos.
#axisgrid: Herramientas para trabajar con cuadrículas de subgráficos.
#categorical: Funciones para gráficos categóricos.
#colors: Manipulación y creación de paletas de colores.
#distributions: Herramientas para gráficos de distribución de datos.
#external: Integración con bibliotecas externas.
#matrix: Gráficos matriciales.
#rcmod: Configuración global de estilo.
#regression: Funciones para gráficos de regresión.
#timeseries: Funciones para trabajar con series temporales.

