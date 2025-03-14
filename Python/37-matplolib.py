import matplotlib

"""El módulo matplotlib es una librería en Python utilizada para crear gráficos y visualizaciones de datos. Es especialmente 
útil para representar datos numéricos de manera visual mediante gráficos como líneas, barras, dispersión, histogramas, entre otros."""

#Instalación. Para instalarlo, puedes usar pip:
#pip install matplotlib 

#Uso básico
#Importar matplotlib: Se importa generalmente pyplot, una sublibrería que proporciona una interfaz para crear gráficos de 
#manera sencilla.

#import matplotlib.pyplot as plt 
#Crear un gráfico simple: Un gráfico de líneas básico con datos de ejemplo.
#import matplotlib.pyplot as plt 
# Datos 
x = [1, 2, 3, 4, 5] 
y = [1, 4, 9, 16, 25] 
# Crear gráfico 
plt.plot(x, y) 
plt.title("Gráfico de ejemplo") 
plt.xlabel("Eje X") 
plt.ylabel("Eje Y") 
# Mostrar gráfico 
plt.show() 
#Este código crea un gráfico de líneas donde el eje X tiene los valores [1, 2, 3, 4, 5] y el eje Y tiene los valores [1, 4, 9, 16, 25].



"""Funciones del módulo matplotlib.pyplot"""

#1. Gráficos básicos
#plot(): Dibuja un gráfico de líneas.
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25] 
plt.plot(x, y) 
plt.show() 

#scatter(): Dibuja un gráfico de dispersión.
x = [1, 2, 3, 4, 5] 
y = [5, 4, 3, 2, 1] 
plt.scatter(x, y) 
plt.show() 

#bar(): Dibuja un gráfico de barras.
x = ['A', 'B', 'C'] 
y = [10, 15, 7] 
plt.bar(x, y) 
plt.show() 

#barh(): Dibuja un gráfico de barras horizontales.
y = ['A', 'B', 'C'] 
x = [10, 15, 7] 
plt.barh(y, x) 
plt.show() 

#hist(): Dibuja un histograma.
data = [1, 2, 2, 3, 3, 3, 4, 4, 5] 
plt.hist(data, bins=5) 
plt.show() 

#pie(): Dibuja un gráfico de pastel.
labels = ['A', 'B', 'C'] 
sizes = [25, 35, 40] 
plt.pie(sizes, labels=labels, autopct='%1.1f%%') 
plt.show() 

#2. Configuración de gráficos
#title(): Establece el título del gráfico.
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.title("Gráfico de ejemplo") 
plt.show() 

#xlabel() y ylabel(): Establecen las etiquetas de los ejes.
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.xlabel("Eje X") 
plt.ylabel("Eje Y") 
plt.show() 

#xlim() y ylim(): Establecen los límites de los ejes X y Y.
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.xlim(0, 4) 
plt.ylim(0, 10) 
plt.show() 

#axis(): Establece las propiedades de los ejes.
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.axis('equal') 
plt.show() 

#3. Personalización de gráficos
#legend(): Muestra la leyenda del gráfico.
plt.plot([1, 2, 3], [1, 4, 9], label="Línea 1") 
plt.plot([1, 2, 3], [9, 4, 1], label="Línea 2") 
plt.legend() 
plt.show() 


#grid(): Activa o desactiva la cuadrícula.
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.grid(True) 
plt.show() 

#xticks() y yticks(): Establecen las ubicaciones de las marcas en los ejes X y Y.
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.xticks([1, 2, 3]) 
plt.yticks([1, 4, 9]) 
plt.show() 

#tick_params(): Personaliza las marcas de los ejes.
plt.plot([1, 2, 3], [1, 4, 9])
plt.tick_params(axis='x', which='both', bottom=False, top=False)
plt.show() 

#text(): Añade texto en una ubicación específica dentro del gráfico.
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.text(2, 5, "Texto de ejemplo") 
plt.show() 

#annotate(): Añade anotaciones a un gráfico.
plt.plot([1, 2, 3], [1, 4, 9])
plt.annotate('Punto 2', xy=(2, 4), xytext=(2.5, 5), arrowprops=dict(facecolor='blue', arrowstyle='->')) 
plt.show() 

#4. Subgráficos
#subplot(): Crea subgráficos dentro de una figura.
plt.subplot(1, 2, 1) 
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.subplot(1, 2, 2) 
plt.plot([1, 2, 3], [9, 4, 1])
plt.show() 

#subplots(): Crea una figura con una cuadrícula de subgráficos.
fig, axs = plt.subplots(1, 2) 
axs[0].plot([1, 2, 3], [1, 4, 9]) 
axs[1].plot([1, 2, 3], [9, 4, 1]) 
plt.show() 

#add_subplot(): Añade un subgráfico a una figura existente.
fig = plt.figure() 
ax = fig.add_subplot(111) 
ax.plot([1, 2, 3], [1, 4, 9]) 
plt.show() 

#5. Guardado y visualización
#show(): Muestra el gráfico.
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.show() 

#savefig(): Guarda el gráfico como un archivo.
plt.plot([1, 2, 3], [1, 4, 9])
plt.savefig('grafico.png') 

#close(): Cierra la figura actual.
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.close() 

#6. Configuración avanzada
#figure(): Crea una nueva figura.
plt.figure(figsize=(8, 6)) 
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.show() 

#clf(): Limpia la figura actual.
plt.plot([1, 2, 3], [1, 4, 9])
plt.clf() 

#gca(): Obtiene el eje actual.
ax = plt.gca() 
ax.plot([1, 2, 3], [1, 4, 9]) 
plt.show() 

#gcf(): Obtiene la figura actual.
fig = plt.gcf() 
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.show() 

#tight_layout(): Ajusta el espaciado de los subgráficos.
fig, axs = plt.subplots(1, 2) 
axs[0].plot([1, 2, 3], [1, 4, 9]) 
axs[1].plot([1, 2, 3], [9, 4, 1]) 
plt.tight_layout() 
plt.show() 


#7. Gráficos en 3D (requiere mpl_toolkits.mplot3d)
#Axes3D(): Crea un gráfico en 3D.
from mpl_toolkits.mplot3d import Axes3D 
fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d') 
ax.plot([1, 2, 3], [1, 2, 3], [1, 4, 9]) 
plt.show() 

#plot_surface(): Dibuja una superficie 3D.
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-5, 5, 100) 
y = np.linspace(-5, 5, 100) 
X, Y = np.meshgrid(x, y) 
Z = X**2 + Y**2 
fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z) 
plt.show() 


"""El módulo matplotlib tiene varias clases"""
#1. Clase Figure (del módulo matplotlib.figure)
#La clase Figure es la contenedora principal de todos los elementos gráficos de Matplotlib. Representa la figura completa, que puede contener uno o más subgráficos (Axes), y proporciona métodos para personalizar la visualización y el tamaño. Ejemplo de uso:
import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(8, 6)) # Crea una figura 
plt.plot([1, 2, 3], [1, 4, 9]) 
fig.suptitle('Título de la figura') 
plt.show() 

#2. Clase Axes (del módulo matplotlib.axes)
#La clase Axes es responsable de manejar el área de los gráficos dentro de una figura. Los ejes de los gráficos (x e y) y todo lo relacionado con la visualización de los datos se maneja mediante esta clase. En términos simples, representa un gráfico dentro de la figura. Ejemplo de uso:
import matplotlib.pyplot as plt 
fig, ax = plt.subplots() 
# Crea una figura y un conjunto de ejes (subgráfico)
ax.plot([1, 2, 3], [1, 4, 9]) 
ax.set_title("Gráfico dentro de la figura") 
plt.show() 

#3. Clase Axes3D (del módulo mpl_toolkits.mplot3d)
#Esta clase se utiliza para crear gráficos en 3D. Para trabajar con gráficos 3D, se debe importar desde mpl_toolkits.mplot3d. Ejemplo de uso:
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d') 
x = np.linspace(-5, 5, 100) 
y = np.linspace(-5, 5, 100) 
X, Y = np.meshgrid(x, y) 
Z = X**2 + Y**2 
ax.plot_surface(X, Y, Z) 
plt.show() 

#4. Clase Subplot (del módulo matplotlib.axes)
#Aunque no se usa directamente a menudo como una clase explícita, subplot() crea instancias de la clase Axes en la figura. Para tener un control más fino, se puede trabajar directamente con subgráficos utilizando add_subplot(). Ejemplo de uso:
fig = plt.figure() 
ax1 = fig.add_subplot(121) 
# Primer subgráfico (de 2) 
ax1.plot([1, 2, 3], [1, 4, 9]) 
ax2 = fig.add_subplot(122) 
# Segundo subgráfico (de 2) 
ax2.plot([1, 2, 3], [9, 4, 1]) 
plt.show() 

#5. Clase Artist (del módulo matplotlib.artist)
#La clase Artist es la clase base para todos los objetos visuales en Matplotlib. Todo en Matplotlib, como las líneas, los ejes, las leyendas, los textos, etc., son artistas. Puedes extender esta clase para crear objetos personalizados. Ejemplo de uso:
import matplotlib.pyplot as plt 
from matplotlib.artist import Artist 
class MyCustomArtist(Artist): 
    def __init__(self): 
        super().__init__() 

    def draw(self, renderer):
    # Lógica de dibujo personalizada 
    # pass
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9]) 
plt.show() 
#(Nota: Este ejemplo es una base, ya que la creación de artistas personalizados es un tema avanzado.)

#6. Clase Text (del módulo matplotlib.text)
#La clase Text se utiliza para representar texto en el gráfico. Es un tipo de artista que se coloca en los ejes y permite manipular el estilo y la posición del texto. Ejemplo de uso:
fig, ax = plt.subplots() 
ax.plot([1, 2, 3], [1, 4, 9]) 
text = ax.text(2, 5, 'Texto de ejemplo', fontsize=12) 
plt.show() 

#7. Clase Line2D (del módulo matplotlib.lines)
#La clase Line2D representa una línea en un gráfico. Esta clase se utiliza internamente cuando se usa plot(), pero también puedes instanciarla directamente para crear líneas personalizadas. Ejemplo de uso:
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt 
fig, ax = plt.subplots() 
line = Line2D([1, 2, 3], [1, 4, 9], color='blue') 
ax.add_line(line) 
plt.show() 

#8. Clase Rectangle (del módulo matplotlib.patches)
#Esta clase representa un rectángulo en un gráfico, que puede ser utilizado para diversas visualizaciones, como barras en un histograma o para resaltar áreas en el gráfico. Ejemplo de uso:
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt 
fig, ax = plt.subplots() 
rect = Rectangle((0.2, 0.2), 0.5, 0.3, linewidth=1, edgecolor='r', facecolor='b') 
ax.add_patch(rect) 
plt.show() 

#9. Clase Circle (del módulo matplotlib.patches)
#Esta clase permite agregar círculos a los gráficos, los cuales también son objetos tipo Artist. Ejemplo de uso:
from matplotlib.patches import Circle
import matplotlib.pyplot as plt 
fig, ax = plt.subplots() 
circle = Circle((0.5, 0.5), 0.2, color='r') 
ax.add_patch(circle) 
plt.show() 

#10. Clase Colormap (del módulo matplotlib.cm)
#La clase Colormap se usa para mapear valores a colores. Puedes obtener una instancia de un mapa de colores a través de plt.cm. Ejemplo de uso:
import matplotlib.pyplot as plt
import numpy as np 
data = np.random.rand(10, 10) 
plt.imshow(data, cmap='viridis') 
plt.colorbar() 
plt.show() 

#Figure: Representa la figura que contiene los ejes y gráficos.
#Axes: Maneja los ejes y las visualizaciones de datos.
#Axes3D: Usado para gráficos en 3D.
#Artist: Clase base para los elementos gráficos, como líneas, textos, y rectángulos.
#Line2D: Representa líneas.
#Rectangle: Permite agregar rectángulos.
#Circle: Permite agregar círculos.
#Text: Para agregar texto al gráfico.
#Colormap: Para asignar colores en gráficos.


"""El módulo matplotlib no define muchas variables globales como tal, pero sí utiliza una serie de configuraciones y parámetros 
que afectan el comportamiento de los gráficos y su apariencia. Estas "variables" suelen ser configuraciones globales, 
propiedades de la figura, los ejes o los estilos de los gráficos."""

#1. matplotlib.rcParams
#rcParams es un diccionario que almacena las configuraciones globales de Matplotlib. Puedes cambiar estos parámetros para modificar la apariencia de tus gráficos sin necesidad de ajustar cada uno manualmente. Ejemplo de uso:
import matplotlib.pyplot as plt 
# Cambiar el estilo global para los gráficos 
plt.rcParams['lines.linewidth'] = 2 
# Establecer el grosor de las líneas 
plt.rcParams['axes.titlesize'] = 20  # Establecer tamaño de título de los ejes 
# Crear un gráfico con la configuración modificada 
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.title("Gráfico con configuración global") 
plt.show() 
#En este ejemplo, la configuración del grosor de las líneas y el tamaño del título de los ejes se modificó a través de rcParams.

#2. matplotlib.pyplot.style.use()
#Matplotlib permite usar diferentes estilos para los gráficos. Estos estilos son colecciones de configuraciones predefinidas (como el color de fondo, tipo de línea, etc.). Puedes cambiar el estilo de tus gráficos usando style.use(). Ejemplo de uso:
import matplotlib.pyplot as plt 
# Aplicar un estilo predefinido 
plt.style.use('ggplot') # Estilo similar al de ggplot2 en R 
# Crear un gráfico con el nuevo estilo 
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.title("Gráfico con estilo ggplot") 
plt.show() 
#Al usar plt.style.use('ggplot'), el gráfico adoptará automáticamente un conjunto de configuraciones visuales predefinidas.

#3. matplotlib.pyplot.rc()
#La función rc() es un método para establecer temporalmente los parámetros de configuración de rcParams para una sección del código. Es útil si deseas cambiar configuraciones solo para una parte específica del gráfico sin afectar toda la configuración global. Ejemplo de uso:
import matplotlib.pyplot as plt 
# Establecer temporalmente un parámetro para el gráfico 
plt.rc('axes', titlesize=15, labelsize=10) # Cambiar tamaño de título y etiquetas de los ejes 
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.title("Gráfico con parámetros temporales") 
plt.show() 
# Restablecer a la configuración original (opcional)
plt.rcdefaults() 
#Con plt.rc(), puedes modificar los parámetros solo para la duración del bloque de código.

#4. matplotlib.colors (variables de colores)
#Matplotlib tiene varias variables relacionadas con colores, como los mapas de colores (colormaps) y las constantes de colores. Ejemplo de uso:
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import cm 
# Usar un mapa de colores para la visualización 
data = np.random.rand(10, 10) 
plt.imshow(data, cmap=cm.viridis) # Usar el colormap 'viridis' 
plt.colorbar() 
plt.show() 
#Aquí cm.viridis es un mapa de colores predefinido que Matplotlib proporciona.

#5. matplotlib.cm (variables de colormap)
#cm es un módulo dentro de matplotlib que proporciona varios mapas de colores predefinidos. Los mapas de colores pueden usarse para personalizar cómo los valores de los datos son representados visualmente. Ejemplo de uso:
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import cm 
# Crear datos aleatorios 
data = np.random.rand(10, 10) 
# Usar un colormap personalizado 
plt.imshow(data, cmap=cm.plasma) 
# Colormap 'plasma' 
plt.colorbar() 
plt.show() 
#Puedes cambiar el mapa de colores usando diferentes variables dentro de cm, como cm.inferno, cm.magma, cm.cividis, entre otros.

#6. matplotlib._api (variables internas)
#Aunque no se utiliza generalmente en código de usuario, algunas variables internas pueden usarse en ciertos contextos avanzados, como la validación de entradas o la manipulación de errores. Ejemplo:
import matplotlib._api # Ejemplo del uso de variables internas para validación (bajo casos específicos) 
#Este tipo de variables es más para usuarios avanzados o para modificar el comportamiento interno de Matplotlib, y generalmente no es necesario en la mayoría de los casos.

#7. matplotlib.backends.backend_*
#Matplotlib utiliza diferentes "backends" para renderizar gráficos. Los valores de estas variables definen cómo se muestra el gráfico (por ejemplo, en una ventana emergente o en un archivo de imagen). Ejemplo:
import matplotlib.pyplot as plt 
# Establecer el backend para generar gráficos 
plt.switch_backend('Agg') 
# Para crear gráficos sin mostrar la ventana interactiva 

#rcParams: Diccionario global que guarda la configuración de los gráficos.
#style.use(): Permite usar estilos predefinidos para los gráficos.
#rc(): Establece temporalmente configuraciones de rcParams.
#colors: Proporciona colores y paletas de colores.
#cm: Contiene diferentes mapas de colores (colormaps).
#backend_*: Variables relacionadas con el backend de Matplotlib para renderizado.



"""El módulo matplotlib tiene varias constantes"""

#1. matplotlib.rcParams (constantes de configuración global)
#rcParams contiene muchas constantes que permiten controlar el aspecto global de los gráficos, como el tamaño de la figura, el tipo de línea, el color de fondo, etc. Estas constantes pueden ser modificadas para cambiar el comportamiento y estilo de los gráficos en general. Ejemplo de uso:
import matplotlib.pyplot as plt # Cambiar el tamaño de la figura por defecto 
plt.rcParams['figure.figsize'] = [8, 6] # Establecer el estilo de las líneas por defecto 
plt.rcParams['lines.linewidth'] = 2 # Crear un gráfico con los parámetros modificados 
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.title("Gráfico con rcParams personalizados") 
plt.show() 
#En este ejemplo, cambiamos el tamaño por defecto de la figura y el grosor de las líneas en todos los gráficos.

#2. matplotlib.colors (constantes de color)
#Matplotlib define varias constantes de color que se pueden usar directamente para configurar el color de elementos gráficos. Estas constantes están dentro del módulo matplotlib.colors y pueden representarse por nombre, valores RGB o hexadecimal. Ejemplo de uso:
import matplotlib.pyplot as plt 
from matplotlib import colors # Usar constantes de color para personalizar un gráfico 
plt.plot([1, 2, 3], [1, 4, 9], color=colors.CSS4['darkblue']) # Usando color CSS4 
plt.show() 
#En este caso, colors.CSS4['darkblue'] es una constante que representa un color predefinido.

#3. matplotlib.pyplot (constantes de estilo)
#Dentro de matplotlib.pyplot, se encuentran constantes para estilos de gráficos, como los estilos predefinidos, el tipo de gráfico y las configuraciones por defecto. Ejemplo de uso:
import matplotlib.pyplot as plt # Usar un estilo predefinido 
plt.style.use('seaborn-darkgrid') # Crear un gráfico con ese estilo 
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.title("Gráfico con estilo seaborn-darkgrid") 
plt.show() 
#seaborn-darkgrid es un estilo predefinido dentro de los estilos de matplotlib que cambia el diseño del gráfico (como el color de fondo y las cuadrículas).

#4. matplotlib.cm (constantes de colormap)
#matplotlib.cm define varios colormaps predefinidos (mapas de colores) que se pueden usar para colorear datos, como en imágenes o gráficos de superficie. Algunos ejemplos de colormaps son viridis, plasma, inferno, etc. Ejemplo de uso:
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import cm # Crear un conjunto de datos aleatorios 
data = np.random.rand(10, 10) # Usar un colormap predefinido para visualizar los datos 
plt.imshow(data, cmap=cm.viridis) # Usando el colormap 'viridis' 
plt.colorbar() 
plt.show() 
#cm.viridis es un colormap que representa colores en una gama de tonos de amarillo-verde-púrpura.

#5. matplotlib.backends.backend_* (constantes de backend)
#Matplotlib tiene varios backends para mostrar los gráficos en diferentes entornos (interactivos o sin interfaz gráfica). Estas constantes permiten seleccionar el backend adecuado según el entorno en el que se esté ejecutando el código. Ejemplo de uso:
import matplotlib.pyplot as plt # Cambiar el backend (por ejemplo, para usar 'Agg', que es sin GUI) 
plt.switch_backend('Agg') # Backend sin interfaz gráfica 
# Crear un gráfico sin que se muestre la ventana de la GUI 
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.savefig('grafico_sin_interfaz.png') 
#Agg es un backend que permite generar gráficos sin mostrar una ventana gráfica, útil para entornos de servidor.

#6. matplotlib.lines.Line2D (constantes para líneas)
#Las constantes de matplotlib.lines.Line2D permiten controlar la apariencia de las líneas en un gráfico, como el estilo de la línea (sólida, discontinua) y el marcador. Ejemplo de uso:
import matplotlib.pyplot as plt 
from matplotlib.lines import Line2D # Crear una línea personalizada con una constante de estilo 
line = Line2D([0, 1], [0, 1], linestyle='--', color='red') # Línea discontinua roja 
plt.gca().add_line(line) 
plt.xlim(-1, 2) 
plt.ylim(-1, 2) 
plt.show() 
#Aquí, linestyle='--' es una constante que indica una línea discontinua.

#7. matplotlib.text.Text (constantes de texto)
#En matplotlib.text.Text, puedes configurar la apariencia del texto, como el tamaño de la fuente, la alineación, etc., utilizando constantes como fontsize, verticalalignment, horizontalalignment, entre otros. Ejemplo de uso:
import matplotlib.pyplot as plt # Crear un gráfico y añadir texto con constantes de formato 
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.text(1.5, 5, 'Texto en gráfico', fontsize=12, color='green', horizontalalignment='center') 
plt.show() 
#ontsize es una constante que determina el tamaño del texto en el gráfico.

#8. matplotlib.patches (constantes para formas geométricas)
#El módulo matplotlib.patches contiene constantes para dibujar formas como círculos, rectángulos y polígonos. Ejemplo de uso:
import matplotlib.pyplot as plt 
from matplotlib.patches import Rectangle # Crear una figura con un rectángulo 
fig, ax = plt.subplots() 
rect = Rectangle((0.1, 0.1), 0.6, 0.3, linewidth=2, edgecolor='blue', facecolor='orange') 
ax.add_patch(rect) 
plt.show() 
#Rectangle se utiliza para dibujar rectángulos en la figura.

#rcParams: Contiene muchas constantes de configuración global, como el tamaño de las figuras y el grosor de las líneas.
#colors: Contiene constantes de colores predefinidos como darkblue, red, green, etc.
#style.use(): Permite aplicar estilos predefinidos a los gráficos.
#cm: Contiene constantes de mapas de colores, como viridis, plasma, inferno, etc.
#backend_*: Constantes para definir el backend de renderizado de gráficos (por ejemplo, Agg).
#Line2D: Contiene constantes para las configuraciones de líneas, como el estilo ('--' para líneas discontinuas).
#Text: Contiene constantes para la personalización del texto en los gráficos (como el tamaño de la fuente).
#patches: Contiene constantes para las formas geométricas, como Rectangle y Circle.


"""Matplotlib define varias excepciones"""

#1. matplotlib.MatplotlibDeprecationWarning
#Esta excepción es un advertencia, no un error, y se utiliza para notificar a los desarrolladores cuando se utiliza una función o característica obsoleta que se eliminará en versiones futuras. Ejemplo de uso:
import matplotlib.pyplot as plt # Usar una función obsoleta generará una advertencia
plt.set_cmap('gray') # Función obsoleta, puede generar un MatplotlibDeprecationWarning 
#Este tipo de advertencia se puede capturar mediante un bloque try-except si se desea.

#2. matplotlib.backends.BackendError
#Se lanza cuando hay un problema con el backend de Matplotlib, como un error al intentar cambiar o inicializar un backend incompatible. Ejemplo de uso:
import matplotlib.pyplot as plt # Intentar usar un backend incompatible puede lanzar una excepción 
try: 
    plt.switch_backend('nonexistent_backend') # Intentar usar un backend inexistente 
except matplotlib.backends.BackendError as e: 
    print(f"Error con el backend: {e}") 
#BackendError se puede capturar para manejar situaciones en las que el backend no está disponible.

#3. matplotlib.AxisError
#Esta excepción se lanza cuando ocurre un error relacionado con los ejes de la figura, como cuando intentas modificar un eje que no existe. Ejemplo de uso:
import matplotlib.pyplot as plt # Crear una figura con un solo eje 
fig, ax = plt.subplots() # Intentar modificar un eje inexistente causará un AxisError 
try: 
    ax2 = fig.add_subplot(111) # El eje ya existe, intentar agregarlo de nuevo genera un error 
except matplotlib.AxisError as e:
    print(f"Error con el eje: {e}") 
#Este error es útil cuando intentas hacer algo inválido con los ejes, como agregar un eje que ya está presente.

#4. matplotlib.RecursionError
#Se lanza cuando hay una llamada recursiva infinita en el código que involucra operaciones gráficas, como cuando se genera un gráfico dentro de otro sin una condición de salida. Ejemplo de uso:
import matplotlib.pyplot as plt # Función recursiva que puede causar un RecursionError 
def plot_recursive(): 
    fig, ax = plt.subplots() 
    ax.plot([1, 2, 3], [1, 4, 9]) 
    plot_recursive() # Llamada recursiva infinita 
    try: 
        plot_recursive() 
    except RecursionError as e: 
        print(f"Error de recursión: {e}") 
#Este tipo de error no es común, pero puede ocurrir en situaciones complejas de recursión en la creación de gráficos.

#5. matplotlib.TightLayoutError
#Se lanza cuando tight_layout() no puede ajustar adecuadamente los elementos del gráfico, como los títulos, etiquetas y márgenes. Esto puede ocurrir cuando hay demasiados elementos en la figura o cuando la figura tiene un tamaño inapropiado. Ejemplo de uso:
import matplotlib.pyplot as plt # Crear una figura con muchos subgráficos 
fig, axs = plt.subplots(3, 3) # Intentar aplicar tight_layout() en una figura con muchos elementos puede generar un error 
try: 
    plt.tight_layout() 
except matplotlib.TightLayoutError as e: 
    print(f"Error de layout ajustado: {e}") 
#Este error es útil cuando estás tratando de ajustar automáticamente el diseño de la figura pero algo impide el ajuste adecuado.

#6. matplotlib.font_manager.FontManagerError
#Se lanza cuando hay un error relacionado con la gestión de fuentes, como cuando no se puede cargar una fuente requerida. Ejemplo de uso:
import matplotlib.pyplot as plt 
from matplotlib import font_manager # Intentar usar una fuente inexistente puede lanzar un error 
try: 
    plt.title("Título con fuente inexistente", fontname="FuenteInexistente") 
except font_manager.FontManagerError as e: 
    print(f"Error de fuente: {e}") 
#Este error se puede capturar cuando se especifica una fuente que no está disponible en el sistema.

#7. matplotlib.cbook.MatplotlibDeprecationWarning
#Al igual que MatplotlibDeprecationWarning, esta es una advertencia que se lanza cuando se utiliza una característica obsoleta de Matplotlib. Aunque no detendrá el programa, es útil para mantenerse al día con las futuras actualizaciones de Matplotlib. Ejemplo de uso:
import matplotlib.pyplot as plt
import warnings # Generar una advertencia de deprecación 
with warnings.catch_warnings(): 
    warnings.simplefilter("always", category=UserWarning) 
    plt.set_cmap('gray') # Usar una función obsoleta 
#Este tipo de advertencia es muy común cuando usas funciones que serán eliminadas en futuras versiones de la librería.

#8. matplotlib.colorbar.ColorbarBase (Excepciones personalizadas)
#Cuando se crea una barra de color personalizada, pueden ocurrir errores si no se proporcionan los parámetros correctos. Ejemplo de uso:
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.colorbar import ColorbarBase 
from matplotlib import cm 
# Intentar crear una barra de color sin los datos correctos 
data = np.random.rand(10, 10) 
try: 
    ColorbarBase(plt.gca(), cmap=cm.viridis) 
# Falta el valor para el parámetro 'mappable' 
except TypeError as e: 
    print(f"Error de tipo: {e}") 
#Este tipo de excepción puede ocurrir si no se pasan los parámetros correctos a las funciones de creación de barras de color.

#MatplotlibDeprecationWarning: Advertencia de uso de características obsoletas.
#BackendError: Error relacionado con el backend de Matplotlib.
#AxisError: Error relacionado con los ejes de la figura.
#RecursionError: Error de recursión infinita en gráficos.
#TightLayoutError: Error cuando tight_layout() no puede ajustar adecuadamente los elementos.
#FontManagerError: Error al gestionar fuentes, como cuando no se puede encontrar la fuente.
#MatplotlibDeprecationWarning (en el módulo cbook): Advertencia de deprecación de características.



"""El módulo matplotlib tiene varios submódulos"""

#1. matplotlib.pyplot
#Este es uno de los submódulos más utilizados y proporciona una interfaz orientada a los gráficos tipo MATLAB para la creación y visualización de gráficos. Es el módulo básico para generar gráficos de líneas, barras, histogramas, etc. Ejemplo de uso:
import matplotlib.pyplot as plt 
# Crear un gráfico de línea simple
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.title('Gráfico de línea') 
plt.show() 

#2. matplotlib.axes
#El submódulo axes proporciona clases y funciones para trabajar con los ejes de los gráficos. Es donde se definen las gráficas específicas, como los gráficos de líneas, barras y dispersión, dentro de la figura. Ejemplo de uso:
import matplotlib.pyplot as plt 
# Crear una figura y un conjunto de ejes 
fig, ax = plt.subplots() 
# Dibujar una línea sobre los ejes
ax.plot([1, 2, 3], [1, 4, 9]) 
ax.set_title('Gráfico con ejes personalizados')
plt.show() 

#3. matplotlib.lines
#Este submódulo se encarga de crear y gestionar objetos de línea dentro de los gráficos. Proporciona la clase Line2D para crear y personalizar líneas en los gráficos. Ejemplo de uso:
import matplotlib.pyplot as plt 
from matplotlib.lines import Line2D 
# Crear un gráfico y agregar una línea personalizada 
fig, ax = plt.subplots() 
line = Line2D([0, 1], [0, 1], color='green', linewidth=2, linestyle='--') 
ax.add_line(line) 
plt.show() 

#4. matplotlib.patches
#Este submódulo se utiliza para trabajar con formas geométricas como rectángulos, círculos, elipses, polígonos, etc., que se pueden agregar a la figura para enriquecer los gráficos. Ejemplo de uso:
import matplotlib.pyplot as plt 
from matplotlib.patches import Rectangle # Crear una figura y agregar un rectángulo 
fig, ax = plt.subplots() 
rect = Rectangle((0.2, 0.2), 0.5, 0.5, edgecolor='red', facecolor='blue') 
ax.add_patch(rect) 
plt.show() 

#5. matplotlib.cm
#Este submódulo contiene los mapas de colores (colormaps) que se utilizan para asignar colores a los datos en gráficos como imágenes o superficies 3D. Los colormaps permiten representar visualmente los valores de los datos mediante colores. Ejemplo de uso:
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import cm 
# Crear datos aleatorios y usar un colormap para visualizarlos 
data = np.random.rand(10, 10) 
plt.imshow(data, cmap=cm.viridis) 
plt.colorbar() 
plt.show() 

#6. matplotlib.colors
#Este submódulo ofrece funcionalidades para la manipulación y creación de colores. Se puede utilizar para definir colores a partir de valores RGB, HSL, o nombres de colores. Ejemplo de uso:
import matplotlib.pyplot as plt 
from matplotlib.colors import to_rgba 
# Convertir un color a formato RGBA 
color = to_rgba('blue', alpha=0.5) 
plt.plot([1, 2, 3], [1, 4, 9], color=color) 
plt.show() 

#7. matplotlib.font_manager
#Este submódulo maneja las fuentes que se utilizan para renderizar texto dentro de los gráficos, permitiendo controlar las propiedades tipográficas, como la familia de la fuente, el estilo y el tamaño. Ejemplo de uso:
import matplotlib.pyplot as plt 
from matplotlib import font_manager 
# Establecer una fuente específica para el título 
plt.title("Gráfico con fuente personalizada", fontname="Comic Sans MS") 
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.show() 

#8. matplotlib.animation
#Este submódulo se utiliza para crear animaciones en los gráficos. Permite actualizar los gráficos de forma dinámica en cada fotograma de la animación. Ejemplo de uso:
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation 
# Crear una figura y un conjunto de ejes 
fig, ax = plt.subplots() # Datos para la animación 
x = np.linspace(0, 2 * np.pi, 100) 
y = np.sin(x) 
# Función de actualización para la animación 
def update(frame): 
ax.clear() 
ax.plot(x, np.sin(x + frame)) 
# Crear la animación
ani = FuncAnimation(fig, update, frames=np.arange(0, 2 * np.pi, 0.1), interval=50) 
plt.show() 

#9. matplotlib.ticker
#Este submódulo permite controlar los valores de las marcas de los ejes en los gráficos, como el formato de los números, la frecuencia de las marcas, etc Ejemplo de uso:
import matplotlib.pyplot as plt 
from matplotlib.ticker import MaxNLocator 
# Crear un gráfico
fig, ax = plt.subplots() 
ax.plot([1, 2, 3], [1, 4, 9]) 
# Configurar el formato de las marcas en el eje Y 
ax.yaxis.set_major_locator(MaxNLocator(integer=True)) 
plt.show() 

#10. matplotlib.backends
#Este submódulo se ocupa de la interacción con los backends de Matplotlib. Controla cómo se renderizan los gráficos, ya sea en una ventana emergente, en una imagen guardada, o en un entorno sin interfaz gráfica (como en servidores). Ejemplo de uso:
import matplotlib.pyplot as plt 
# Cambiar el backend a uno sin interfaz gráfica (útil en servidores) 
plt.switch_backend('Agg') 
# Crear un gráfico y guardarlo como imagen 
plt.plot([1, 2, 3], [1, 4, 9]) 
plt.savefig('grafico_sin_gui.png') 

#matplotlib.pyplot: Interfaz para la creación de gráficos.
#matplotlib.axes: Manejo de ejes en los gráficos.
#matplotlib.lines: Manejo de líneas gráficas.
#matplotlib.patches: Trabajo con formas geométricas.
#matplotlib.cm: Mapa de colores (colormaps).
#matplotlib.colors: Manipulación de colores.
#matplotlib.font_manager: Manejo de fuentes tipográficas.
#matplotlib.animation: Creación de animaciones en gráficos.
#matplotlib.ticker: Configuración de marcas y formatos de ejes.
#matplotlib.backends: Manejo de backends gráficos para diferentes entornos.

