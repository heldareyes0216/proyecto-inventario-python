import re

"""
servivios.py
módulo con las operacione CRUD y estadísticas del inventario.
El inventaro se mantiene en memoria como lista de diccionarios:
"""

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario.

    Parametros:
        inventario (lista): lista de productos en memoria.
        nombre (str): nombre del producto
        precio (float): agrega el precio unitario (>=0)
        cantidad (int): unidades disponibles (>=0)
    """    
    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad 
    })            

def mostrar_inventario(inventario):
    """"
    Imprime todos los producos del inventario con formato legible

    Parametros:
        inventario(lista): lista de productos
    """    
    if not inventario:
        print("inventario vacío")
    else:
        print("\n{:<20} {:>10} {:>20}".format("nombre", "precio", "cantidad"))
        print("-" * 60)
        for p in inventario:
            print("{:<20} {:>10.2f} {:>20}".format(
            p["nombre"], p["precio"], p["cantidad"]
            ))

def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre 

    Parametros:
        inventario (list): list de productos
        nombre (str): nombre del producto a buscar

    Retorna
        dict: el producto encontrado, o None si no existe
    """  
    for producto in inventario:
        if producto["nombre"] == nombre:
            return producto
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """"
    Actualiza el precio y/o cantidad de un producto existente 

    Parametros:
        inventario (list): lista de productos
        nombre (str): nombre del prodcuto que se va actualizar
        nuevo_precio (float): nuevo precio a asignar
        nueva_cantidad (int): nueva cantidad a asignar
    """    

    producto = buscar_producto(inventario, nombre)              

    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
    else:
        print("Producto no encontrado")


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario por nombre

    Parametros:
    inventario(list): lista de productos 
    nombre(str): nombre del producto a eliminar
    """
    producto = buscar_producto(inventario, nombre) 

    if producto:
        inventario.remove(producto)
    else:
        print("Producto no encontrado")


def calcular_estadisticas(inventario):
    """
    Calcula estadisticas generales del inventario

    Parametros:
        inventario (list): lista de prodcutos del inventario

    Retorna:
        dict con claves:
            unidades_totales (int): suma todas las cantidades
            valor_toatal (float): suma de precio * cantidad de cada producto
            producto_mas_caro (tuple): (nombre, precio) del producto mas caro
            producto_mayor_stock (tuple): (nombre, cantidad) el producto con mas stock

            Retorna None si el inventario está vacio
    """            
    if not inventario:
        return None
    # lambda para calcular el subtotal de cada producto
    subtotal = lambda p: p["precio"] * p["cantidad"]

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_stock_mayor = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidade totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (producto_mas_caro["nombre"], producto_mas_caro["precio"]),
        "producto_stock_mayor": (producto_stock_mayor["nombre"], producto_stock_mayor["cantidad"])
    }

def buscar_productos(inventario, nombre):
    expresion = fr"{nombre}"
    
    return list(filter(lambda p: re.search(expresion, p['nombre']), inventario))