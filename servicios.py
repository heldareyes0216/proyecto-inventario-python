def agregar_producto(inventario, nombre, precio, cantidad):

    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad 
    })            

def mostrar_inventario(inventario):
    if not inventario:
        print("inventario vacío")

def buscar_producto(inventario, nombre):
    for producto in inventario:
        if producto["nombre"] == nombre:
            return producto
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    producto = buscar_producto(inventario, nombre,)              

    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
    else:
        print("Prodcuto no encontrado")


def eliminar_producto(inventario, nombre):
    producto = buscar_producto(inventario, nombre) 

    if producto:
        inventario.remove (producto)
    else:
        print("Producto no encontrado")


def calcular_estadistica(inventario):
    if not inventario:
        return None

    subtotal = (lambda p:["precio"] * p["cantidad"])
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_stock_mayor = max(inventario, kye=lambda p: p["cantidad"])

    return {
        "unidade totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (producto_mas_caro["nombre"], producto_mas_caro["precio"]),
        "producto_stock_mayor": (producto_stock_mayor["nombre"], producto_stock_mayor["cantidad"])
    }