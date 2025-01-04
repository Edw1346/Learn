def validaciones_datos(role:str, action:str, hour:str):
    if role not in ["admin", "editor", "viewer"]:
        return False, f"El rol {role} no es valido\n"
    elif action not in ["delete", "update", "create", "read"]:
        return False, f"La acción {action} no es valida\n"
    elif hour < 0 or hour > 24:
        return False, f"La hora {hour} no puede ser mayor a 24 o menor a 0\n"
    else:
        if 0 < hour < 13:
            form_hour = f"{str(hour)} a.m"
        elif hour > 12:
            form_hour = f"{str(hour-12)} p.m"
        elif hour == 12:
            form_hour = f"12 p.m"
        elif hour == 24:
            form_hour = f"0 a.m"
    return True, form_hour

def validacion_permisos(role:str, action:str, hour:int, validacion_hora:str):
    if role == "admin" and (action in ["delete", "update", "create", "read"]):
        return f"Acción permitida {role}. Verifico sus permisos de {role}, accion de {action} a las {validacion_hora}\n"
    elif role == "editor":
        if (action not in ["read", "update"]):
            return f"{role} no posee el permiso {action}\n"
        elif hour not in range(8, 21):
            return f"El rol {role} no tiene permisos para realizar acciónes a las {validacion_hora}\n"
        else: return f"Acción permitida {role}. Verifico sus permisos de {role}, accion de {action} a las {validacion_hora}\n"
    if role == "viewer":
        if action not in "read":
            return f"{role} no posee el permiso {action}\n"
        elif hour not in range(9,18):
            return f"El rol {role} no tiene permisos para realizar acciónes a las {validacion_hora}\n"
        return f"Acción permitida {role}. Verifico sus permisos de {role}, accion de {action} a las {validacion_hora}\n"
    else: return f"Error vuelva a intentarlo\n"

def validacion_usuario(role:str, action:str, hour:int):
    validacion = validaciones_datos(role.lower(), action.lower(), hour)
    if validacion[0]:
        permisos = validacion_permisos(role, action, hour, validacion[1])
        print(permisos)
    else: print(validacion[1])

while True:
    try:
        rol = input("Que rol posee: ")
        actio = input("Que accion tiene: ")
        hou = int(input("Que horas es: "))
        validacion_usuario(rol, actio, hou)
    except ValueError:
        print("Error! No ha insertado un valor valido. Intentelo de nuevo")