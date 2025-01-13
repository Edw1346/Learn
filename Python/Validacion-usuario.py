Registro_Usuario = []

def sistema_usuarios():
    Registro_Usuario = []
    Registro_acciones = []

def verifica_roles(dato):
    if dato in ["admin","devoloper","user"]:
        return True, dato
    else: return False

def verificar_ids():
    sistema_usuarios

def acciones(dato):
    if dato in ["create", "read", "update", "delete"]:
        return True, dato
    else: return False

def busqueda_datos(dato, registro):
    for d in registro.values():
        if d["Usuario"] == dato:
            return True, len(d-1)

def verificar_datos(user, contraseña, indice, registro):
    if registro[indice] != user:
        return False, f"El Usuario es incorrecto"
    elif registro[indice] != contraseña:
        return False, f"La contraseña es incorrecta"
    elif registro[indice] == user and registro[indice] == contraseña:
        return True, f"Credenciales correctas"

def registrar_usuario(user, contraseña, role):
    id = sistema_usuarios()
    role = verifica_roles()
    Usuario = {"Usuario":user,"Contraseña":contraseña, "role":role[1]}

    Registro_Usuario.append(Usuario)

def Iniciar_seccion(user, contraseña):
    busqueda = busqueda_datos(user, Registro_Usuario)
    if busqueda[0]:
        verificacion = verificar_datos(user, contraseña, busqueda[1], Registro_Usuario)
        if verificacion[0]:
            print("Felicidades, inicio seccion")
        else:
            print(verificacion[1])