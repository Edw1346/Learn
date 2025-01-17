cabezaras = {'uno': 1, 'dos':'nombre', 'tres': 'precio', 'cuatro': 'cantidad', 'cinco': 'categoria'}
producto1 = {'id':1,'nombre': 'Papas', 'precio': 500, 'cantidad': 6, 'categoria': 'verduras'}
producto2 = {'id': 2,'nombre': 'Rabanos', 'precio': 800, 'cantidad': 8, 'categoria': 'verduras'}

inventario = [producto1, producto2]
#print(f"1 producto {inventario[1]} y 2 producto {inventario[2]}")

def agregar_productos(nombre, precio, cantidad, categoria, observacion):
    num = len(inventario)+1
    producto = {'id':num,'nombre': nombre.capitalize(),'precio': precio,'cantidad': cantidad,'categoria': categoria,'observacion': observacion}
    inventario.append(producto)
    print("Agregado")

def búsqueda_items:(item, registro):
    ind = -1
    for i in registro:
            ind += 1
            if i['nombre'] == item:
                 return True

def actualizar_producto(producto_a_actualizar):
    global inventario 
    nueva_busque = producto_a_actualizar.capitalize()
    if producto_a_actualizar.lower() != 'salir':
        if búsqueda_items(producto_a_actualizar,  ):
                pregunta1 = input(f"{nueva_busque} fue encontrado con exito. Que desea actualizar: (1) Nombre. (2) Precio. (3) Cantidad. (4) Categoria. (5) Observacion: ")
                if pregunta1 == '1' or pregunta1.lower() == 'nombre':
                    nuevo_val = input("Ingrese el nuevo nombre: ")
                    if nuevo_val.lower() == 'salir' or nuevo_val.lower() == 'atras':
                        print("Error, el nombre introducido es una parabra clave, vuelva a intentarlo")
                        return
                    inventario[ind]['nombre'] = nuevo_val.capitalize()
                    del producto_a_actualizar
                    print("Actualizado")
                    return
                elif pregunta1 == '2' or pregunta1.lower() == 'precio':
                    nuevo_val = input("Ingrese el nuevo precio: ")
                    inventario[ind]['precio'] = nuevo_val
                    del producto_a_actualizar
                    print("Actualizado")
                    return
                elif pregunta1 == '3' or pregunta1.lower() == 'cantidad':
                    nuevo_val = input("Ingrese la nueva cantidad: ")
                    inventario[ind]['cantidad'] = nuevo_val
                    del producto_a_actualizar
                    print("Actualizado")
                    return
                elif pregunta1 == '4' or pregunta1.lower() == 'categoria':
                    nuevo_val = input("Ingrese la nueva categoria: ")
                    inventario[ind]['categoria'] = nuevo_val    
                    del producto_a_actualizar
                    print("Actualizado")
                    return
                elif pregunta1 == '5' or pregunta1.lower() == 'observacion':
                    nuevo_val = input("Ingrese el nuevo comentario: ")
                    inventario[ind]['observacion'] = nuevo_val                            
                    del producto_a_actualizar
                    print("Actualizado")
                    return
                elif pregunta1.lower() == 'salir':
                    return
                elif pregunta1.isalpha():
                    print("Error intentelo de nuevo")
                    return
        else:
            print(f"No fue encontrado {producto_a_actualizar}, intentelo de nuevo\n")    
            del producto_a_actualizar
            actualizar2 = input("Ingrese el nombre del producto a actualizar o salir: ")
            actualizar_producto(actualizar2)
    elif producto_a_actualizar.lower() == 'salir' : pass

def mostrar_inventario():
    print(inventario)

def eliminar_producto(producto_a_eliminar):
    ind = -1
    nueva_eli = producto_a_eliminar.capitalize()
    if producto_a_eliminar.lower() != 'salir':
        for i in inventario:
            ind += 1
            if i['nombre'] == nueva_eli:
                print(f"{nueva_eli} fue encontrado y elliminado con exito")
                del(inventario[ind])
                ids = 0
                for i in inventario:
                    ids +=1
                    i['id'] = ids
            else:
                print(f"No fue encontrado {producto_a_eliminar}, intentelo de nuevo")
                eliminar2 = input("\nIngrese el nombre del producto a eliminar o salir: ")
                eliminar_producto(eliminar2)
    elif producto_a_eliminar.lower() == 'salir' : pass

def sistema_Control():
    while True:
        Control = input("\n1. Introducir un nuevo producto 2. Actualizar inventario 3. Mostrar inventario 4. Eliminar producto: ")

        if Control == '1':
            nombre = input("\nIngrese el nombre del producto: ")
            precio = int(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            categoria = input("Ingrese la categoria del producto: ")
            observacion = input("Ingrese un comentario: ")
            agregar_productos(nombre, precio, cantidad, categoria, observacion)
            continue

        elif Control == '2':
            actualizar = input("\nIngrese el nombre del producto a actualizar o salir: ")
            actualizar_producto(actualizar)
            continue

        elif Control == '3':
            print("\nInventario:")
            mostrar_inventario()
            continue

        elif Control == '4':
            eliminar = input("\nIngrese el nombre del producto a eliminar o salir: ")
            eliminar_producto(eliminar)
            continue

sistema_Control()