import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    if not inventario:
        print("invenatrio vacío, no es posible guardar")
        return
    try:
        with open(ruta, "w", newline="") as archivo:
            writer = csv.writer(archivo)

            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print(f"invenatrio guardado en: {ruta}")

    except Exception as e:
        print("Error al guardad:", e)

def cargar_csv(ruta):
    inventario = []
    errores = 0

    try:
        with open(ruta, "r") as archivo:
            reader = csv.reader(archivo)

            encabezado = next(reader)

            if encabezado != ["nombre", "precio", "cantidad"]:
                print("Encabezado invádo")
                return [] 
            
            for fila in reader:
                if len(fila) != 3:
                    errores += 1
                    continue 
                try:
                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    if precio < 0 or cantidad < 0:
                        raise ValueError
                    
                    inventario.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
                    
                except:
                    errores += 1

        print(f"Productos cargados: {len(inventario)}")
        print(f"Filas invalidas: {errores}")

        return inventario

    except FileNotFoundError:
            print("Archivo no encontrado")
    except UnicodeDecodeError:
            print("Error de codificación")
    except Exception as e:
        print(f"Error inesperado {e}")

    return []        


