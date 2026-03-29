"""
app.py
Punto de entrada al sistema del inventario
Menu principal conn opciones 1-9 para CRUD, estadisticas y persistencias CSV
"""
from servicios import (
    agregar_producto,
    mostrar_inventario,
    buscar_producto,
    buscar_productos,
    actualizar_producto,
    eliminar_producto,
    calcular_estadisticas, 
)
from archivos import guardar_csv, cargar_csv

# inventario en memoriia: lista de diccionarios
inventario = []

opcion = ""

while opcion != "9":

    print("\n==== MENU ====")
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Estadísticas")
    print("7. Guardar csv")
    print("8. Cargar csv")
    print("9. Salir")

    try:
        opcion = input("Seleccione una opción: ")
    except: 
        print("Error en la opcion seleccionada")
        continue    

    #  Opcion1: agregar producto
    if opcion == "1":
        nombre = input("Nombre del producto: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío")
            continue

        valido_precio = False
        while not valido_precio:
            try:
                precio = float(input("Ingrese el precio a agregar: "))
                if precio >= 0:
                    valido_precio = True
                else:
                    print("Error: no puede ser un número negativo")
            except:
                print("Error: número inválido")

        valido_cantidad = False
        while not valido_cantidad:
            try:
                cantidad = int(input("Ingrese cantidad a agregar: "))
                if cantidad >= 0:
                    valido_cantidad = True
                else:
                    print("Error: no puede ser un número negativo")
            except:
                print("Error: número inválido")

        agregar_producto(inventario, nombre, precio, cantidad)
        print("\nProducto agregado")
    
    # opción 2: mostrar producto
    elif opcion == "2":
        mostrar_inventario(inventario)
    
    # opcion 3: Buscar producto
    elif opcion == "3":
        nombre = input("Nombre a buscar: ").strip()   
        resultados = buscar_productos(inventario, nombre)

        if len(resultados) < 1:
            print(f"Producto {nombre} no encontrado.")
        else:
            for producto in resultados:
                print(f"\nProducto encontrado:")
                print(f" Nombre: {producto['nombre']}")
                print(f" Precio: ${producto['precio']:.2f}")
                print(f"Cantidad: {producto['cantidad']}")


    elif opcion == "4":
        nombre = input("Producto exitente: ")

        precio = input("Ingrese nuevo precio (Enter para omitir): ")
        cantidad = input("Ingrese nueva cantidad (Enter para omitir): ")

        precio = float(precio) if precio else None
        cantidad = int(cantidad) if cantidad else None 

        actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None)
        print("\nProducto actualizado")

    elif opcion == "5":
        nombre = input("Ingrese nombre a eliminar: ")
        eliminar_producto(inventario, nombre)
        print("\nProducto elimminado exitosamente")

    elif opcion == "6":
        stats = calcular_estadisticas(inventario)

        if stats:
            print(stats)
        else:
            print("Inventario vacío")

    elif opcion == "7":
        ruta = input("Ruta: ")
        guardar_csv(inventario, ruta, incluir_header=True)
        print("Archivo  guardado")

    elif opcion == "8":
        ruta = input("Ruta: ")
        nuevo =  cargar_csv(ruta)

        if nuevo:
            decision = input("¿Sobrescribir? (S/N): ").lower()

            if decision == "s":
                inventario = nuevo 
            else:
                for p in nuevo:
                    existente = buscar_producto(inventario, p["nombrre"])
                    if existente:
                        existente["cantidad"] += p["cantidad"]
                        existente["precio "] = p["precio"]
                    else:
                        inventario.append(p)

        print("Datos guardados")

    elif opcion != "9":
        print("opcion invalida") 

print("\nPrograma finalizado")                        