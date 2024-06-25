from usuarios import mostrar_menu_usuarios
from libros import mostrar_menu_libros

def mostrar_menu_principal():
    while True:
        print("\nMenú Principal:")
        print("1 - Mantenedor de usuarios")
        print("2 - Mantenedor de libros y reportes")
        print("3 - Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrar_menu_usuarios()
        elif opcion == '2':
            mostrar_menu_libros()
        elif opcion == '3':
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    mostrar_menu_principal()