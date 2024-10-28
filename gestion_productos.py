import os

# Lista para almacenar los productos
productos = []

# Función para cargar datos desde un archivo al inicio del programa
def cargar_datos():
    if os.path.exists('productos.txt'):
        with open('productos.txt', 'r') as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(',')
                productos.append({
                    'nombre': nombre,
                    'precio': float(precio),
                    'cantidad': int(cantidad)
                })
        print("Datos cargados correctamente.")
    else:
        print("Archivo de datos no encontrado. Se creará uno nuevo.")

# Función para guardar los datos en un archivo
def guardar_datos():
    with open('productos.txt', 'w') as archivo:
        for producto in productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
    print("Datos guardados correctamente.")

# Función para añadir un producto
def añadir_producto():
    nombre = input("Nombre del producto: ")
    try:
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad del producto: "))
        productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
        print("Producto añadido correctamente.")
    except ValueError:
        print("Error: Precio y cantidad deben ser números.")

# Función para ver todos los productos
def ver_productos():
    if productos:
        print("\nLista de productos:")
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print("No hay productos para mostrar.")

# Función para actualizar un producto
def actualizar_producto():
    nombre = input("Nombre del producto a actualizar: ")
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            try:
                producto['nombre'] = input("Nuevo nombre (deja vacío para no cambiar): ") or producto['nombre']
                nuevo_precio = input("Nuevo precio (deja vacío para no cambiar): ")
                producto['precio'] = float(nuevo_precio) if nuevo_precio else producto['precio']
                nueva_cantidad = input("Nueva cantidad (deja vacío para no cambiar): ")
                producto['cantidad'] = int(nueva_cantidad) if nueva_cantidad else producto['cantidad']
                print("Producto actualizado correctamente.")
            except ValueError:
                print("Error: Precio y cantidad deben ser números.")
            return
    print("Producto no encontrado.")

# Función para eliminar un producto
def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            productos.remove(producto)
            print("Producto eliminado correctamente.")
            return
    print("Producto no encontrado.")

# Función para mostrar el menú principal
def menu():
    cargar_datos()  # Cargar datos al inicio del programa
    while True:
        print("\nSistema de Gestión de Productos")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

# Ejecutar el menú
menu()
