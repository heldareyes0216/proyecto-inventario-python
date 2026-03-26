from servicios import *
from archivos import *

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

    opcion = int(input("Seleccione una opción: "))

    if opcion == "1":
        nombre = input("ingrese nombre a agregar: " )

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
        while not valido_precio:
            try:
                cantidad = int(input("Ingrese cantidad a agregar: "))
                if cantidad >= 0:
                    valido_cantidad = True
                else:
                    print("Error: no puede ser un número negativo")
            except:
                print("Error: número inválido")

        agregar_producto()

    elif opcion == "2":
        mostrar_inventario()

    elif opcion == "3":
        buscar = input("Buscar: ")   
        print(buscar_producto(inventario, nombre, precio, cantidad or "No encontrado"))

    elif opcion == "4":
        nombre = input("Producto exitente: ")
        precio = input("Ingrese nuevo precio: ")
        cantidad = input("Agregar nueva cantida: ")

        precio = float(precio) if precio else None
        cantidad = int(cantidad) if cantidad else None 

        actualizar_producto()

    elif opcion == "5":
        nombre = input("Ingrese nombre a eliminar: ")

        eliminar_producto()

    elif opcion == "6":
        stats = calcular_estadistica()

        if stats:
            print(stats)
        else:
            print("Inventario vacío")

    elif opcion == "7":
        ruta = input("Ruta: ")
        guardar_csv()

    elif opcion == "8":
          ruta = input("Ruta: ")
          nuevo =  cargar_csv()

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
                            

                  
             











            