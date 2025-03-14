import PIL

"""El módulo PIL (Python Imaging Library), ahora mantenido como Pillow, es una librería popular en Python para abrir, 
manipular y guardar imágenes en diversos formatos. Proporciona muchas herramientas fáciles de usar para realizar tareas 
comunes de procesamiento de imágenes. El módulo Pillow (PIL) tiene una amplia gama de funciones que permiten realizar diversas operaciones sobre imágenes, como 
abrir, editar, filtrar, manipular colores, y mucho más."""


"""Funciones"""
#1. Funciones de Apertura y Guardado de Imágenes
#Image.open(): Abre una imagen desde un archivo.
img = Image.open("image.jpg") 

#Image.save(): Guarda la imagen en un archivo.
img.save("new_image.png") 

#Image.show(): Muestra la imagen en el visor predeterminado del sistema.
img.show() 


#2. Funciones de Manipulación y Transformación de Imágenes
#Image.resize(): Cambia el tamaño de la imagen a las dimensiones proporcionadas.
img_resized = img.resize((200, 200)) 

#Image.rotate(): Rota la imagen en el ángulo especificado.
img_rotated = img.rotate(90) 

#Image.transpose(): Voltea la imagen.
img_flipped = img.transpose(Image.FLIP_LEFT_RIGHT) 

#Image.crop(): Recorta una imagen con un área definida.
cropped_img = img.crop((0, 0, 100, 100)) 

#Image.paste(): Pega una imagen sobre otra.
img.paste(another_img, (x, y)) 


#3. Funciones de Manipulación de Color
#Image.convert(): Convierte una imagen a otro modo de color.
img_gray = img.convert("L") # Escala de grises 

#Image.getbands(): Obtiene los nombres de los canales de la imagen (como "R", "G", "B").
bands = img.getbands() 

#Image.split(): Divide la imagen en sus canales de color.
r, g, b = img.split() 

#Image.merge(): Combina los canales de color en una imagen.
img_merged = Image.merge("RGB", (r, g, b)) 


#4. Funciones de Filtros
#Image.filter(): Aplica un filtro a la imagen.
img_blurred = img.filter(ImageFilter.BLUR) 

#ImageFilter: Submódulo que contiene filtros predefinidos.
from PIL import ImageFilter
img_filtered = img.filter(ImageFilter.CONTOUR) 


#5. Funciones de Información sobre la Imagen
#Image.size: Obtiene las dimensiones de la imagen (ancho, alto).
width, height = img.size 

#Image.mode: Obtiene el modo de color de la imagen (por ejemplo, "RGB", "L" para escala de grises).
#mode = img.mode 

#Image.info: Obtiene información adicional sobre la imagen (metadatos).
info = img.info 


#6. Funciones de Dibujo en Imágenes
#ImageDraw.Draw(): Permite dibujar sobre la imagen (líneas, texto, etc.). 
from PIL import ImageDraw
draw = ImageDraw.Draw(img) 
draw.text((10, 10), "Texto", fill="red") 


#7. Funciones de Efectos y Mejoras
#ImageEnhance.Enhance(): Mejora la calidad de la imagen (brillo, contraste, etc.). 
from PIL import ImageEnhance 
enhancer = ImageEnhance.Contrast(img) 
img_enhanced = enhancer.enhance(2.0) 


#8. Funciones de Cálculos y Estadísticas
#Image.histogram(): Devuelve un histograma de la imagen.
histogram = img.histogram() 

#Image.getextrema(): Devuelve el valor mínimo y máximo de cada banda.
extrema = img.getextrema() 


#9. Funciones de Formatos de Imagen
#Image.getformat(): Obtiene el formato de la imagen (por ejemplo, JPEG, PNG).
format = img.format 

#Image.getim(): Obtiene el objeto de imagen subyacente en el caso de imágenes en ciertos formatos como GIF o TIFF.
im = img.getim() 


#10. Funciones Avanzadas
#Image.eval(): Aplica una función a cada píxel de la imagen.
img_new = img.eval(lambda px: px * 2) 

#Image.alpha_composite(): Combina dos imágenes con un canal alfa.
composite_img = Image.alpha_composite(img1, img2) 


#11. Funciones de Carga de Imágenes
#ImageSequence.all_frames(): Devuelve todos los cuadros de una imagen animada. 
from PIL import ImageSequence 
frames = ImageSequence.all_frames(img) 


#12. Funciones para Soporte de Formatos de Archivos
#Image.register_open(): Registra un nuevo formato de archivo de imagen.
Image.register_open("JPEG", custom_open_function) 

#Image.register_save(): Registra una función de guardado personalizada para un formato de archivo.
Image.register_save("JPEG", custom_save_function) 


"""El módulo Pillow (PIL) contiene varias clases"""

#1. Image
#Es la clase principal en Pillow, utilizada para representar y manipular imágenes.
#Métodos principales: 
#Image.open(): Abre una imagen desde un archivo.
#Image.save(): Guarda una imagen.
#Image.show(): Muestra una imagen.
#Image.resize(): Cambia el tamaño de una imagen.
#Image.rotate(): Rota una imagen. Ejemplo: 
from PIL import Image 
img = Image.open("image.jpg") 
img.show() 

#2. ImageDraw
#Esta clase permite dibujar sobre una imagen, como agregar texto, líneas, y otras formas.
#Métodos principales: 
#ImageDraw.Draw(): Crea un objeto para dibujar sobre la imagen.
#draw.line(), draw.text(), draw.rectangle(): Métodos para dibujar sobre la imagen. Ejemplo: 
from PIL import Image, ImageDraw
img = Image.open("image.jpg") 
draw = ImageDraw.Draw(img) 
draw.text((10, 10), "Hola Mundo", fill="white") 
img.show() 

#3. ImageFilter
#Este módulo contiene filtros predefinidos que se pueden aplicar a una imagen, como desenfoque, contorno, etc.
#Filtros comunes: 
#ImageFilter.BLUR: Desenfoque básico.
#ImageFilter.CONTOUR: Filtro de contorno.
#ImageFilter.SHARPEN: Filtro de agudización. Ejemplo: 
from PIL import Image, ImageFilter 
img = Image.open("image.jpg") 
img_blurred = img.filter(ImageFilter.BLUR)
img_blurred.show() 

#4. ImageEnhance
#Esta clase se usa para ajustar la calidad de la imagen, como el brillo, el contraste o la saturación.
#Métodos principales: 
#ImageEnhance.Contrast(): Ajusta el contraste de la imagen.
#ImageEnhance.Brightness(): Ajusta el brillo de la imagen.
#ImageEnhance.Color(): Ajusta la saturación de la imagen. Ejemplo: 
from PIL import Image, ImageEnhance
img = Image.open("image.jpg") 
enhancer = ImageEnhance.Contrast(img) 
img_enhanced = enhancer.enhance(2.0) 
img_enhanced.show() 

#5. ImageSequence
#Esta clase proporciona herramientas para trabajar con secuencias de imágenes, como las que contienen animaciones GIF.
#Métodos principales: 
#ImageSequence.all_frames(): Extrae todos los cuadros de una imagen animada. Ejemplo: 
from PIL import Image, ImageSequence 
img = Image.open("animated.gif") 
for frame in ImageSequence.all_frames(img): 
    frame.show() 

#6. ImageTk
#Esta clase proporciona métodos para integrar imágenes en aplicaciones gráficas que usan Tkinter.
#Métodos principales: 
#ImageTk.PhotoImage(): Convierte una imagen Pillow en un objeto que puede ser usado en widgets de Tkinter. Ejemplo: 
from PIL import Image, ImageTk
import tkinter as tk
root = tk.Tk() 
img = Image.open("image.jpg") 
img_tk = ImageTk.PhotoImage(img) 
label = tk.Label(root, image=img_tk) 
label.pack() 
root.mainloop() 

#7. PIL.TiffTags
#Esta clase es útil para trabajar con etiquetas en imágenes TIFF, proporcionando acceso a información metadatos.
#Métodos principales: 
#TiffTags.TIFFTAG_*: Constantes que representan las etiquetas TIFF. Ejemplo: 
from PIL import TiffTags 
print(TiffTags.TIFFTAG_ARTIST) # Muestra la etiqueta TIFF correspondiente. 

#8. PIL.ImageFont
#Esta clase se usa para cargar y manejar fuentes tipográficas cuando se agregan texto a imágenes.
#Métodos principales: 
#ImageFont.truetype(): Carga una fuente TrueType para dibujar texto. Ejemplo: 
from PIL import Image, ImageDraw, ImageFont 
img = Image.open("image.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", 24) 
draw.text((10, 10), "Texto", font=font, fill="white")
img.show() 

#Image: Clase principal para manejar imágenes.
#ImageDraw: Clase para dibujar sobre imágenes (líneas, texto, etc.).
#ImageFilter: Filtros predefinidos para modificar imágenes.
#ImageEnhance: Ajustes para mejorar el contraste, brillo, etc.
#ImageSequence: Trabaja con secuencias de imágenes, como GIFs animados.
#ImageTk: Facilita el uso de imágenes en aplicaciones de Tkinter.
#TiffTags: Utiliza etiquetas en imágenes TIFF.
#ImageFont: Carga y maneja fuentes tipográficas.


"""Variables"""

#1. Image.Modes
#Es un diccionario que contiene los diferentes modos de color disponibles en Pillow (por ejemplo, "RGB", "L" para escala de grises, etc.). Ejemplo:
from PIL import Image
print(Image.Modes) # {'1': '1-bit pixels, black and white', 'L': '8-bit pixels, grayscale', ...} 

#2. Image.Transpose
#Contiene las constantes que se usan para especificar cómo se debe transponer (voltear) una imagen. Algunos valores comunes incluyen: 
#Image.Transpose.ROTATE_90: Rota la imagen 90 grados.
#Image.Transpose.FLIP_LEFT_RIGHT: Voltea la imagen horizontalmente.
#Image.Transpose.FLIP_TOP_BOTTOM: Voltea la imagen verticalmente. Ejemplo:
from PIL import Image
img = Image.open("image.jpg")
img_rotated = img.transpose(Image.Transpose.ROTATE_90) 
img_rotated.show() 

#3. Image.ANTIALIAS
#Es una constante que se usa para especificar un filtro de alta calidad para redimensionar imágenes, particularmente cuando se utiliza el método resize(). En versiones recientes de Pillow, se ha renombrado como Image.Resampling.LANCZOS. Ejemplo: 
from PIL import Image
img = Image.open("image.jpg")
img_resized = img.resize((200, 200), Image.Resampling.LANCZOS) 
img_resized.show() 

#4. Image.PILLOW_VERSION (obsoleta en versiones recientes)
#Esta variable se usaba para verificar la versión de Pillow instalada. En versiones recientes de Pillow, esta variable ha sido reemplazada por el uso del comando pip show Pillow o la propiedad __version__. Ejemplo: 
from PIL import Image 
print(Image.__version__) # En lugar de Image.PILLOW_VERSION 

#5. ImageFilter.FIND_EDGES
#Es una constante que se encuentra en el submódulo ImageFilter. Se utiliza para detectar bordes en una imagen, aplicando un filtro de detección de bordes. Ejemplo: 
from PIL import Image, ImageFilter 
img = Image.open("image.jpg") 
img_edges = img.filter(ImageFilter.FIND_EDGES) 
img_edges.show() 

#6. ImageFilter.BLUR
#Es una constante de ImageFilter que aplica un desenfoque básico a la imagen. Ejemplo:
from PIL import Image, ImageFilter 
img = Image.open("image.jpg")
img_blurred = img.filter(ImageFilter.BLUR) 
img_blurred.show() 

#7. ImageFilter.SHARPEN
#Es una constante que se utiliza en el submódulo ImageFilter para aplicar un filtro de agudización (sharpness) a la imagen. Ejemplo: 
from PIL import Image, ImageFilter 
img = Image.open("image.jpg")
img_sharpened = img.filter(ImageFilter.SHARPEN)
img_sharpened.show() 

#8. ImageFilter.CONTOUR
#Es una constante en ImageFilter que aplica un filtro de contornos a la imagen, lo que resalta las fronteras de los objetos. Ejemplo: 
from PIL import Image, ImageFilter
img = Image.open("image.jpg") 
img_contour = img.filter(ImageFilter.CONTOUR) 
img_contour.show() 

#9. ImageFilter.SMOOTH
#Es una constante en ImageFilter que aplica un filtro de suavizado a la imagen. Ejemplo: 
from PIL import Image, ImageFilter 
img = Image.open("image.jpg") 
img_smooth = img.filter(ImageFilter.SMOOTH)
img_smooth.show() 

#10. ImageFilter.SMOOTH_MORE
#Es una constante en ImageFilter que aplica un suavizado más fuerte que el filtro SMOOTH. Ejemplo: 
from PIL import Image, ImageFilter 
img = Image.open("image.jpg") 
img_smooth_more = img.filter(ImageFilter.SMOOTH_MORE) 
img_smooth_more.show() 

#Image.Modes: Diccionario con los modos de color disponibles.
#Image.Transpose: Contiene constantes para transponer imágenes (rotar, voltear).
#Image.ANTIALIAS: Filtro de alta calidad para redimensionar imágenes (ahora Image.Resampling.LANCZOS).
#Image.PILLOW_VERSION: Versión de Pillow instalada (ahora reemplazada por Image.__version__).
#ImageFilter.FIND_EDGES: Filtro para detectar bordes.
#ImageFilter.BLUR: Filtro para aplicar desenfoque.
#ImageFilter.SHARPEN: Filtro para agudizar la imagen.
#ImageFilter.CONTOUR: Filtro para aplicar un contorno.
#ImageFilter.SMOOTH: Filtro para suavizar la imagen.
#ImageFilter.SMOOTH_MORE: Filtro para un suavizado más fuerte.



"""Constantes"""

#1. Image.ANTIALIAS (renombrado a Image.Resampling.LANCZOS en versiones recientes)
#Esta constante se utilizaba para aplicar un filtro de alta calidad al redimensionar imágenes. Ahora se recomienda usar Image.Resampling.LANCZOS. Ejemplo: 
from PIL import Image 
img = Image.open("image.jpg") 
img_resized = img.resize((200, 200), Image.Resampling.LANCZOS) 
img_resized.show() 

#2. Image.NONE
#Representa un modo sin ningún tipo de filtro de resampling. Se usa cuando no se desea aplicar ningún filtro durante una operación de redimensionamiento. Ejemplo:
from PIL import Image 
img = Image.open("image.jpg")
img_resized = img.resize((200, 200), Image.NONE)
img_resized.show() 

#3. Image.NEAREST
#Esta constante se utiliza para el resampling de una imagen usando el método más cercano (sin suavizado). Es un método rápido pero menos preciso. Ejemplo: 
from PIL import Image
img = Image.open("image.jpg")
img_resized = img.resize((200, 200), Image.NEAREST) 
img_resized.show() 

#4. Image.BOX
#Esta constante se usa en el resampling de imágenes para aplicar un filtro de "cuadro" (box filter). Es más preciso que NEAREST. Ejemplo:
from PIL import Image 
img = Image.open("image.jpg")
img_resized = img.resize((200, 200), Image.BOX) 
img_resized.show() 

#5. Image.BILINEAR
#Se utiliza en el resampling para aplicar el filtro bilineal, que es más suave que el filtro de caja o el filtro de vecino más cercano. Ejemplo:
from PIL import Image 
img = Image.open("image.jpg")
img_resized = img.resize((200, 200), Image.BILINEAR)
img_resized.show() 

#6. Image.HAMMING
#Una constante utilizada para el resampling, aplicando un filtro Hamming, que suaviza la imagen de manera eficiente. Ejemplo: 
from PIL import Image 
img = Image.open("image.jpg")
img_resized = img.resize((200, 200), Image.HAMMING)
img_resized.show() 

#7. Image.BICUBIC
#Utiliza un algoritmo de interpolación bicúbica para redimensionar imágenes, lo cual proporciona mejores resultados que el método bilineal. Ejemplo: 
from PIL import Image 
img = Image.open("image.jpg")
img_resized = img.resize((200, 200), Image.BICUBIC) 
img_resized.show() 

#8. Image.LANCZOS
#Es una constante de resampling de alta calidad, que utiliza el filtro sinc, ideal para reducir el tamaño de las imágenes. Ejemplo:
from PIL import Image
img = Image.open("image.jpg")
img_resized = img.resize((200, 200), Image.LANCZOS) 
img_resized.show() 

#9. Image.FLIP_LEFT_RIGHT
#Esta constante se utiliza para voltear una imagen horizontalmente (de izquierda a derecha). Ejemplo: 
from PIL import Image 
img = Image.open("image.jpg") 
img_flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
img_flipped.show() 

#10. Image.FLIP_TOP_BOTTOM
#Esta constante se usa para voltear una imagen verticalmente (de arriba a abajo). Ejemplo: 
from PIL import Image 
img = Image.open("image.jpg") 
img_flipped = img.transpose(Image.FLIP_TOP_BOTTOM)
img_flipped.show() 

#11. Image.RGB
#Define el modo de color "RGB" (Red, Green, Blue) para una imagen. Ejemplo: 
from PIL import Image
img = Image.new("RGB", (100, 100), (255, 0, 0)) # Imagen de 100x100, color rojo 
img.show() 

#12. Image.L
#Define el modo de color "L" (escala de grises de 8 bits). Ejemplo: 
from PIL import Image 
img = Image.open("image.jpg").convert("L")
img.show() # Convierte la imagen a escala de grises 

#13. Image.P
#Define el modo de color "P" (paleta de 256 colores). Ejemplo: 
from PIL import Image
img = Image.open("image.jpg").convert("P")
img.show() # Convierte la imagen a un modo de paleta de colores 

#14. Image.TIFF
#Especifica que la imagen es de tipo TIFF. Ejemplo:
from PIL import Image 
img = Image.open("image.tiff") 
img.show() # Abre una imagen TIFF 

#Image.ANTIALIAS: Usado para filtros de alta calidad (ahora Image.Resampling.LANCZOS).
#Image.NONE: Modo sin filtro de resampling.
#Image.NEAREST: Filtro de vecino más cercano para redimensionar.
#Image.BOX: Filtro de caja para resampling.
#Image.BILINEAR: Filtro bilineal para redimensionar.
#Image.HAMMING: Filtro Hamming para suavizado.
#Image.BICUBIC: Filtro bicúbico para redimensionar.
#Image.LANCZOS: Filtro sinc para redimensionar con alta calidad.
#Image.FLIP_LEFT_RIGHT: Voltea la imagen horizontalmente.
#Image.FLIP_TOP_BOTTOM: Voltea la imagen verticalmente.
#Image.RGB: Modo de color RGB.
#Image.L: Modo de color en escala de grises.
#Image.P: Modo de paleta de colores.
#Image.TIFF: Tipo de archivo TIFF.


"""El módulo Pillow (PIL) maneja varias excepciones"""

#1. Image.DecompressionBombError
#Esta excepción se lanza cuando una imagen es muy grande para descomprimirla de manera segura, lo que puede indicar una posible "bomba de descompresión", un tipo de ataque de DoS (Denial of Service) mediante imágenes grandes. Ejemplo: 
from PIL import Image
try: 
    img = Image.open("large_image.jpg") 
    img.show() 
except Image.DecompressionBombError:
    print("¡Imagen demasiado grande para procesar!") 

#2. Image.UnidentifiedImageError
#Esta excepción se lanza cuando el archivo que intentas abrir no es una imagen válida o no es reconocido como un formato de imagen soportado. Ejemplo:
from PIL import Image
try:
   img = Image.open("non_image_file.txt")
except Image.UnidentifiedImageError: 
    print("El archivo no es una imagen válida.") 

#3. Image.FileIOError
#Esta excepción se lanza cuando hay un error al intentar leer o escribir en un archivo de imagen, generalmente cuando el archivo está dañado o no se puede acceder. Ejemplo: 
from PIL import Image
try: 
    img = Image.open("corrupt_image.jpg")
except Image.FileIOError: 
    print("Hubo un error al intentar leer el archivo de imagen.") 

#4. Image.ResamplingError
#Esta excepción se lanza cuando ocurre un error al intentar aplicar un filtro de resampling durante operaciones como resize(). Esto puede ocurrir si se pasa un valor incorrecto para el filtro. Ejemplo: 
from PIL import Image 
try: 
    img = Image.open("image.jpg") 
    img_resized = img.resize((200, 200), "invalid_filter") # Filtro incorrecto 
except Image.ResamplingError: 
    print("Error en el filtro de resampling.") 

#5. Image.ModelError
#Esta excepción se lanza cuando se intenta convertir una imagen a un modo no válido o incompatible. Ejemplo: 
from PIL import Image 
try: 
    img = Image.open("image.jpg") 
    img_converted = img.convert("INVALID_MODE") # Modo no válido 
except Image.ModelError: 
    print("Modo de imagen no válido.") 

#6. Image.ImageSequence
#Esta excepción se lanza cuando se trabaja con secuencias de imágenes (como animaciones GIF) y no se pueden manejar correctamente. Ejemplo: 
from PIL import Image
try: 
    img = Image.open("animated_image.gif") 
    for frame in ImageSequence.Iterator(img): 
        frame.show() 
except Image.ImageSequence: 
    print("No se pudo manejar la secuencia de imágenes.") 

#7. Image.OSError
#Esta es una excepción general que puede ser lanzada si ocurre un error relacionado con la apertura, lectura, o escritura de una imagen. Por ejemplo, si se intenta abrir un archivo que no existe o que no es un formato de imagen reconocido. Ejemplo: 
from PIL import Image
try:
    img = Image.open("image_not_found.jpg") 
except OSError: 
    print("Hubo un error con la apertura o lectura de la imagen.") 

#8. Image.TiffTagsError
#Se lanza cuando hay un problema con las etiquetas de metadatos en una imagen TIFF. Ejemplo: 
from PIL import Image
try: 
    img = Image.open("image.tiff") 
    img.verify() # Verifica si la imagen TIFF tiene etiquetas incorrectas
except Image.TiffTagsError: 
    print("Problema con las etiquetas TIFF.") 

#Image.DecompressionBombError: Imagen demasiado grande para descomprimir de forma segura.
#Image.UnidentifiedImageError: Archivo no reconocido como imagen válida.
#Image.FileIOError: Error al leer o escribir en el archivo de imagen.
#Image.ResamplingError: Error al aplicar un filtro de resampling.
#Image.ModelError: Error al convertir la imagen a un modo no válido.
#Image.ImageSequence: Error al manejar secuencias de imágenes (animaciones GIF).
#Image.OSError: Error general al abrir, leer o escribir una imagen.
#Image.TiffTagsError: Problema con las etiquetas de metadatos en imágenes TIFF.


"""El módulo Pillow (PIL) tiene varios submódulos"""

#1. ImageDraw
#Proporciona herramientas para dibujar sobre una imagen, como líneas, texto y figuras geométricas. Ejemplo: 
from PIL import Image, ImageDraw 
img = Image.new("RGB", (200, 200), (255, 255, 255)) 
draw = ImageDraw.Draw(img) 
draw.line((0, 0, 200, 200), fill="black", width=5) 
img.show() 

#2. ImageFilter
#Contiene una serie de filtros para aplicar a las imágenes, como difuminado, contornos y otros efectos. Ejemplo: 
from PIL import Image, ImageFilter
img = Image.open("image.jpg") 
img_filtered = img.filter(ImageFilter.BLUR) 
img_filtered.show() 

#3. ImageOps
#Proporciona operaciones adicionales de transformación y manipulación de imágenes, como invertir colores, voltear imágenes y aplicar márgenes. Ejemplo: 
from PIL import Image, ImageOps 
img = Image.open("image.jpg") 
img_inverted = ImageOps.invert(img.convert("RGB")) 
img_inverted.show() 

#4. ImageEnhance
#Permite ajustar la calidad de la imagen, como el contraste, brillo, color y nitidez. Ejemplo: 
from PIL import Image, ImageEnhance 
img = Image.open("image.jpg") 
enhancer = ImageEnhance.Contrast(img) 
img_enhanced = enhancer.enhance(2) 
# Aumenta el contraste 
img_enhanced.show() 

#5. ImageFont
#Proporciona herramientas para trabajar con fuentes al agregar texto a las imágenes. Puedes cargar fuentes y especificar estilos y tamaños. Ejemplo: 
from PIL import Image, ImageDraw, ImageFont 
img = Image.new("RGB", (200, 100), (255, 255, 255)) 
draw = ImageDraw.Draw(img)
font = ImageFont.load_default() 
draw.text((10, 10), "Texto aquí", font=font, fill="black") 
img.show() 

#6. ImageSequence
#Permite iterar sobre secuencias de imágenes, como los fotogramas de un GIF animado. Ejemplo: 
from PIL import Image, ImageSequence
img = Image.open("animated.gif") 
for frame in ImageSequence.Iterator(img): 
    frame.show() 

#7. ImageTk
#Permite integrar imágenes de Pillow en aplicaciones de Tkinter para crear interfaces gráficas. Ejemplo: 
from PIL import Image, ImageTk
import tkinter as tk 
img = Image.open("image.jpg") 
root = tk.Tk() 
tk_img = ImageTk.PhotoImage(img) 
label = tk.Label(root, image=tk_img) 
label.pack() 
root.mainloop() 

#8. PIL.ImageCms
#Proporciona soporte para la gestión de color mediante perfiles de color ICC, permitiendo realizar conversiones de color precisas entre diferentes espacios de color. Ejemplo:
from PIL import Image, ImageCms
img = Image.open("image.jpg")
img_with_profile = ImageCms.profileToProfile(img, "sRGB.icm", "AdobeRGB.icm") 
img_with_profile.show() 

#9. PIL.PpmImagePlugin
#Proporciona soporte para leer y escribir imágenes en formato PPM (Portable Pixmap). Ejemplo: 
from PIL import Image 
img = Image.open("image.ppm") 
img.show() 

#10. PIL.JpegImagePlugin
#from PIL import Image 
img = Image.open("image.jpg") 
img.show() 

#ImageDraw: Para dibujar en imágenes.
#ImageFilter: Filtros para modificar imágenes (difuminado, bordes, etc.).
#ImageOps: Operaciones como invertir colores, agregar márgenes, etc.
#ImageEnhance: Mejora de atributos como brillo, contraste y nitidez.
#ImageFont: Trabaja con fuentes al agregar texto a las imágenes.
#ImageSequence: Manejo de secuencias de imágenes (GIFs animados).
#ImageTk: Para usar imágenes en aplicaciones de Tkinter.
#PIL.ImageCms: Gestión de perfiles de color ICC.
#PIL.PpmImagePlugin: Soporte para imágenes en formato PPM.
#PIL.JpegImagePlugin: Soporte específico para imágenes JPEG.

