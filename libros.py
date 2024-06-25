import json

def cargar_datos():
    with open('biblioteca.json', 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
    return datos

def guardar_datos(datos):
    with open('biblioteca.json', 'w', encoding='utf-8') as archivo:
        json.dump(datos, archivo, indent=4)

def reporte_categorias():
    datos = cargar_datos()
    categorias = {categoria['Nombre']: 0 for categoria in datos['Categoria']}  
        categoria_nombre = next(cat['Nombre'] for cat in datos['Categoria'] if cat['CategoriaID'] == libro['CategoriaID'])
        categorias[categoria_nombre] += 1  
    for categoria, count in categorias.items():
        print(f"{categoria}: {count}")

def mostrar_menu_libros():
    while True:
        print("\nMenú de Libros y Reportes:")
        print("1 - Reporte de Categorías de Libros")
        print("2 - Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            reporte_categorias()
        elif opcion == '2':
            break
        else:
            print("Opción no válida.")