productos = []


def añadir_producto():
    # Lógica para añadir un producto
    producto = {}
    claves = ["Nombre", "Precio", "Cantidad"]
    
    for clave in claves:
        valor = input(f"Introduce el valor para {clave} : ")
        producto[clave] = valor
        
    return productos.append(producto)

def ver_productos():
    print(productos)

def actualizar_producto():
    producto_nombre = input("Introduce el nombre del producto ha actualizar: ")
    
    for producto in productos:
        if producto["Nombre"] == producto_nombre:
            nuevo_nombre = input("Ingresa el nuevo nombre: ")
            nuevo_precio = input("Ingresa el nuevo precio: ")
            nueva_cantidad = input("Ingresa la nueva cantidad: ")
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
            
menu()
