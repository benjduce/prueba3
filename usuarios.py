import json

def cargar_datos():
    with open('biblioteca.json', 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
    return datos

def guardar_datos(datos):
    with open('biblioteca.json', 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4)

def agregar_usuario(nombre, email, fecha_registro):
    datos = cargar_datos()
    nuevo_usuario = {
        "UsuarioID": max([usuario['UsuarioID'] for usuario in datos['Usuario']]) + 1,
        "Nombre": nombre,
        "Email": email,
        "FechaRegistro": fecha_registro
    }
    datos['Usuario'].append(nuevo_usuario)
    guardar_datos(datos)

def editar_usuario(usuario_id, nuevo_nombre, nuevo_email, nueva_fecha_registro):
    datos = cargar_datos()
    for usuario in datos['Usuario']:
        if usuario['UsuarioID'] == usuario_id:
            usuario['Nombre'] = nuevo_nombre
            usuario['Email'] = nuevo_email
            usuario['FechaRegistro'] = nueva_fecha_registro
            break
    guardar_datos(datos)

def eliminar_usuario(usuario_id):
    datos = cargar_datos()
    datos['Usuario'] = [usuario for usuario in datos['Usuario'] if usuario['UsuarioID'] != usuario_id]
    guardar_datos(datos)

def buscar_usuario(usuario_id):
    datos = cargar_datos()
    for usuario in datos['Usuario']:
        if usuario['UsuarioID'] == usuario_id:
            return usuario
    return None

def mostrar_menu_usuarios():
    while True:
        print("\nMenú de Usuarios:")
        print("1 - Agregar usuario")
        print("2 - Editar usuario")
        print("3 - Eliminar usuario")
        print("4 - Buscar usuario")
        print("5 - Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del usuario: ")
            email = input("Ingrese el email del usuario: ")
            fecha_registro = input("Ingrese la fecha de registro (YYYY-MM-DD): ")
            agregar_usuario(nombre, email, fecha_registro)
        elif opcion == '2':
            usuario_id = int(input("Ingrese el ID del usuario a editar: "))
            nuevo_nombre = input("Ingrese el nuevo nombre del usuario: ")
            nuevo_email = input("Ingrese el nuevo email del usuario: ")
            nueva_fecha_registro = input("Ingrese la nueva fecha de registro (YYYY-MM-DD): ")
            editar_usuario(usuario_id, nuevo_nombre, nuevo_email, nueva_fecha_registro)
        elif opcion == '3':
            usuario_id = int(input("Ingrese el ID del usuario a eliminar: "))
            eliminar_usuario(usuario_id)
        elif opcion == '4':
            usuario_id = int(input("Ingrese el ID del usuario a buscar: "))
            usuario = buscar_usuario(usuario_id)
            if usuario:
                print(f"Usuario encontrado: {usuario}")
            else:
                print("Usuario no encontrado.")
        elif opcion == '5':
            break
        else:
            print("Opción no válida.")