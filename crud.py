productos = []


def añadir_producto():
    # Lógica para añadir un producto
    producto = {}
    claves = ["Nombre", "Precio", "Cantidad"]
    
    producto["Nombre"] = input("Ingrese el nombre: ")

    while True:
        try:
            producto["Precio"] = float(input("Ingrese el precio: "))
            break
        except ValueError:
            print("Error: Ingrese solamente numeros.")
    
    while True:
        try:
            producto["Cantidad"] = int(input("Ingrese la cantidad: "))
            break
        except ValueError:
            print("Error: Ingrese solamente numeros enteros.")

        
    productos.append(producto)
    print("Producto añadido")

def ver_productos():
    print(productos)

def actualizar_producto():
    producto_nombre = input("Introduce el nombre del producto ha actualizar: ")
    
    for producto in productos:
        if producto["Nombre"] == producto_nombre:
            nuevo_nombre = input("Ingresa el nuevo nombre: ")

            while True:
                try:
                    nuevo_precio = float(input("Ingresa el nuevo precio: "))
                    break
                except ValueError:
                    print("Error: Ingrese solamente numeros.")
            
            while True:
                try:
                    nueva_cantidad = int(input("Ingresa la nueva cantidad: "))
                    break
                except ValueError:
                    print("Error: Ingrese solamente numeros enteros.")
            producto["Nombre"] = nuevo_nombre
            producto["Precio"] = nuevo_precio
            producto["Cantidad"] = nueva_cantidad
            print("Producto actualizado")
            return
    print("No se encontro el producto")
    

def eliminar_producto():
    producto_nombre = input("Ingresa el nombre del producto ha eliminar: ")
    
    for indice, producto in enumerate(productos):
        if producto["Nombre"] == producto_nombre:
            productos.pop(indice)
            print("Producto eliminado correctamente")
            return

    print("No se encontro el producto")
        
            

def guardar_datos():
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto['Nombre']},{producto['Precio']},{producto['Cantidad']}\n")
    print("Se guardaron los datos.")

def cargar_datos():
    try:
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(",")
                producto = {"Nombre": nombre, "Precio": precio, "Cantidad": cantidad}
                productos.append(producto) 
        print("Se cargaron los datos")
    except FileNotFoundError:
        print("No se encontro el archivo")
        
def menu():
    cargar_datos()
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")
        if opcion.isdecimal():
            opcion = int(opcion)

            if opcion == 1:
                añadir_producto()
            elif opcion == 2:
                ver_productos()
            elif opcion == 3:
                actualizar_producto()
            elif opcion == 4:
                eliminar_producto()
            elif opcion == 5:
                guardar_datos()
                break
            else:
                print("Por favor, selecciona una opción válida.")
        else:
            print("Introduzca un numero del 1 al 5")
            
menu()
