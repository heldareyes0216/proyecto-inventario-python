"""
archivos.py
Modulo para persistencia del inventario en archivos CSV
Formato esperado: nombre, precio, cantidad (con encabezado)
"""

import csv


def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV

    Parametros: 
        inventario(list): lista de productos en memoria
        ruta (str): ruta del archivo destino
        incluir_header (bool): si True, escribe la fila del encabezado
    """
    # validar que el inventario no esté vacío antes de guardar    
    if not inventario:
        print("invenatrio vacío, no es posible guardar")
        return
    
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)

            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print(f"invenatrio guardado en: {ruta}")

    except PermissionError:
        print("Error: sin permisos para escribir en esa ruta.")
    except OSError as e:
        print(f"Error al guarar el archivo: {e}")
    except Exception as e:        
        print(f"Error inesperado al guardar. {e}")

def cargar_csv(ruta):
    """
    Carga productos desde un archivo CSV al inventario

    Valida encabezado, número de colmnas, tipos de dato y valores no negativos
    Las filas invalidas se omiten y se contablizan

    Parametros:
        list: lista de prodcutos cargados correctamente
              Retorna [] si el archivo no existe, está corrupto o el encabezado es invalido
    """          
 
    inventario = []
    errores = 0

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)

            # validar encabezado
            encabezado = next(reader)
            if encabezado != ["nombre", "precio", "cantidad"]:
                print("Error: encabezado invádo. Se esperaba: nombre, precio, cantidad")
                
                return [] 
            
            # Procesar cada fila
            for fila in reader:
                #validar número de columnas
                if len(fila) != 3:
                    errores += 1
                    continue 

                try:
                    nombre = fila[0].strip()
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    # validar que no sean negativos
                    if precio < 0 or cantidad < 0:
                        raise ValueError("Valores negativos no permitidos.")
                    
                    inventario.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
                    
                except (ValueError, IndexError):
                    # fila con dato invalido: se omite y se cuenta
                    errores += 1

        print(f"Productos cargados: {len(inventario)}")
        if errores > 0:
            print(f"{errores} filas invalidas omitidas.")

        return inventario

    except FileNotFoundError:
            print("Archivo no encontrado")
    except UnicodeDecodeError:
            print("Error de codificación")
    except ValueError as e:
        print(f"Error inesperado {e}")

    return []        


