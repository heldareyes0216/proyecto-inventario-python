#lista donde se almacenarän todos los prodcutos
inventario = []

#funcion agregrar productos
def agregar_productos():
    print("\n---- Agregar prodcuto ----")

    #pedimos nombre del producto
    nombre = input("Ingrese el nombre del producto: ")

    #validamos que el precio sea un numero valido
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("EL precio no puede ser negativo")
            else:
                break
        except:
            print("Error: Ingrese un numero valido.")

    #validamos que la cantidad sea un numero entero valido
    while True:
        try:
            cantidad = int(input("ingrese la cantidad del producto: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                break
        except:
            print("Ingrese un numero valido")

    #creamos el producto como diccionario 
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    #lo que agregamos a la lista de inventario
    inventario.append(producto)

    print("producto agregado correctamente")

#funcion para mostrar el inventario
def mostrar_inventario():
    print("\n---- Inventario----")

    #validamos si el inventario está vacio 
    if len(inventario) == 0:
        print("El inventario está vacio.")

    else:
        #aqui se recorre la lista con un for
        for producto in inventario:
            print("Producto:", producto["nombre"],
                  "precio:", producto["precio"],
                  "cantidad:", producto["cantidad"])

#funcion para calcular estadisticas
def calcular_estadisticas():
    print("\n=== ESTADISTICAS ===")

    if len(inventario) == 0:
        print("no hay movimientos para calcular estadisticas")

        for producto in inventario:
            valor_total += producto["precio"] * producto["cantidad"]
            total_productos += producto["cantidad"]

            print("total del valor del inventario:", round(valor_total))
            print("total cantidad de productos:", total_productos)

while True:
    print("\n=== MENÚ ===")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_productos()

    elif opcion == "2":
        mostrar_inventario()

    elif opcion == "3":
        calcular_estadisticas()

    elif opcion == "4":
        print("Saliendo del programa...")
        break  # Termina el bucle

    else:
        print("Opción inválida. Intente nuevamente.")                        

        



