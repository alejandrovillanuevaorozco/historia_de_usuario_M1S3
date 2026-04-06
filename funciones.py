import json
import csv
#Validar numeros
def validate_numbers(mensaje):
    valido = False
    while not valido:
        try:
            print(mensaje)
            num=int(input(":"))
            if num >= 0:
                valido = True
            else:
                print("El número no puede ser negativo.")
        except ValueError:
            print("Debe ingresar un número válido.")
    return num
#validar string vacios y sin numeros
def validate_field(message):
    validate=False
    while validate!=True:
        print(message)
        text=input(":")
        validate=text.isalpha()
        if validate==False:
            print("The field must not be empty or contain numbers, please try again")
    return text
#Crear diccionario de diccionario
def create(inventory,clave):
    mensaje="¿Cuantos productos quieres añadir en el inventory?"
    n=validate_numbers(mensaje)
    i=1
    while i<=n:
        clave = clave+1
        print("--------------------------------------------------")
        print("===CREACIÓN DE NUEVO PRODUCTO CON ID: ",clave,"===")
        message="Introduce el nombre del producto"
        nombre=validate_field(message)
        mensaje="Introduce el precio del producto"
        precio=validate_numbers(mensaje)
        mensaje="Introduce la cantidad del producto: "
        cantidad=validate_numbers(mensaje)
        inventory[clave] = {"nombre_producto":nombre,"precio_producto":precio, "cantidad_producto":cantidad}
        i=i+1
    return inventory
#Mostrar diccionario de diccionario
def read(inventory):
    clave=len(inventory)
    if clave == 0:
        print("Inventario vacio, Por favor añade productos al inventario")
    else:
        for clave, datos in inventory.items():
            nombre=datos["nombre_producto"]
            precio=datos["precio_producto"]
            cantidad=datos["cantidad_producto"]
            print("Id del producto:", clave)
            print("Nombre del producto: ", nombre,
                "\nPrecio: ", precio,
                "\nCantidad: ", cantidad,
                "\n")
            print("-----------------------------------------")
#buscar en diccionario de diccionario
def search_product(inventory):
    clave=len(inventory)
    if clave == 0:
        print("Inventario vacio, Por favor añade productos al inventario")
    else:
        opcion="x"
        while opcion!="3":
            print("¿Cómo deseas buscar el producto?")
            opcion=input("1. Por Id: "+
                    "\n2. Por nombre: "+
                    "\n3. Atras"+
                    "\n Por favor ingrese la opción a elegir: "
                    )
            match opcion:
                case "1":
                    print("===Busqueda por ID===")
                    mensaje="Ingrese el id a buscar"
                    id_buscado=validate_numbers(mensaje)
                    valid=inventory.get(id_buscado, "No se encontró el dato proporcionado")
                    print(valid)
                    if valid!="No se encontró el dato proporcionado":
                        valid=id_buscado
                    return valid
                case "2":
                    print("===Busqueda por nombre del producto===")
                    nombre_buscado=input("Ingrese el nombre del producto a buscar: ")
                    valid = "No se encontró el dato proporcionado"
                    nombre=""

                    for clave, producto in inventory.items():
                        if producto["nombre_producto"].upper() == nombre_buscado.upper():
                            nombre=producto["nombre_producto"]
                            precio=producto["precio_producto"]
                            cantidad=producto["cantidad_producto"]
                            valid=clave
                    if nombre.upper()==nombre_buscado.upper():
                        print("Nombre del producto: ", nombre,
                            "\nPrecio: ", precio,
                            "\nCantidad: ", cantidad,
                            "\n")
                        return valid
                    else:
                        print(valid)
                        return valid
                case "3":
                    continue
                case _:
                    print("Opcion invalida, por favor solo digite números del 1 al 9")
#actualizar diccionario
def update(inventory):
    clave=len(inventory)
    if clave == 0:
        print("Inventario vacio, Por favor añade productos al inventario")
    else:
        print("Please first find the ID or name to update...")
        id_actualizado=search_product(inventory)
        if id_actualizado!="No se enc1ontró el dato proporcionado":
            option="x"
            while option!="5":
                print("What do you want to update about the product?")
                option=input("1. Product's name. "+
                        "\n2. Product's price. "+
                        "\n3. Product's quantity. "+
                        "\n4. Update all. "+
                        "\n5. Back"+
                        "\n Please enter the option you wish to choose:")
                print("-----------------------------------------")
                for clave, product in inventory.items():
                    match option:
                        case "1":
                            if clave == id_actualizado:
                                message="Please enter the product's new name"
                                name=validate_field(message)
                                product["nombre_producto"]=name
                                print("-----------------------------------------")
                        case "2":
                            if clave == id_actualizado:
                                message="Please enter the product's new price"
                                precio=validate_numbers(message)
                                product["precio_producto"]=precio
                                print("-----------------------------------------")
                        case "3":
                            if clave == id_actualizado:
                                message="Please enter the product's new quantity"
                                cantidad=validate_numbers(message)
                                product["cantidad_producto"]=cantidad
                                print("-----------------------------------------")
                        case "4":
                            if clave == id_actualizado:
                                message="Please enter the product's new name"
                                name=validate_field(message)
                                message="Please enter the product's new price"
                                precio=validate_numbers(message)
                                message="Please enter the product's new quantity"
                                cantidad=validate_numbers(message)
                                inventory[clave] = {"nombre_producto":name,"precio_producto":precio, "cantidad_producto":cantidad}
                                print("-----------------------------------------")
                        case "5":
                            print("-----------------------------------------")
                            break
                        case _:
                            print("Invalid option, please only enter numbers from 1 to 5")
                            print("-----------------------------------------")
#Eliminar campos
def delete(inventory):
    clave=len(inventory)
    if clave == 0:
        print("Inventario vacio, Por favor añade productos al inventario")
    else:
        print("Eliminación por ID: ")
        print("Por favor, primero busque el Id o nombre a eliminar... ")
        id_eliminado=search_product(inventory)
        print(id_eliminado)
        if id_eliminado!="No se encontró el dato proporcionado":
            print("Se borrarán los todos los campos del ID: ", id_eliminado)
            op="x"
            while op!="S".upper() and op!="N".upper():
                        op = input("¿Desea eliminarlos? (S/N): ").upper()
                        if op != "S".upper() and op!="N".upper():
                            print("Dato ingresado erronéo, por favor solo coloca 'S' o 'N'")
                        if op=="S".upper():
                            del inventory[id_eliminado]
                            print("Campos eliminados")
                        elif op=="N".upper():
                            print("Campos no eliminados")
                            continue
#Estadisticas
def estadisticas(inventory):
    clave=len(inventory)
    if clave == 0:
        print("Inventario vacio, Por favor añade productos al inventario")
    else:    
        unidades_totales=0
        valor_total=0
        producto_mayor_stock=""
        cantidad_mayor_stock=0
        producto_mas_caro=""
        precio_mas_caro=0
        clave=len(inventory)
        if clave == 0:
            print("inventory vacio")
        else:
            print("==ESTADISTICAS==\n")
            for clave, datos in inventory.items():
                nombre=datos["nombre_producto"]
                precio=datos["precio_producto"]
                cantidad=datos["cantidad_producto"]
                unidades_totales=unidades_totales+cantidad
                valor_total=precio*cantidad
                if precio_mas_caro<=precio:
                    precio_mas_caro=precio
                    producto_mas_caro=nombre
                if cantidad_mayor_stock<=cantidad:
                    cantidad_mayor_stock=cantidad
                    producto_mayor_stock=nombre
                
                print("Nombre del producto: ", nombre,
                    "\nValor total: ", valor_total,
                    "\n")
                print("-----------------------------------------")

        print("Producto más caro: ", producto_mas_caro,
            "\nPrecio del producto: ", precio_mas_caro,
            "\nProducto de mayor stock: ", producto_mayor_stock,
            "\nCantidad del producto: ", cantidad_mayor_stock,
            "\nUnidades totales: ", unidades_totales,
            "\n")
        print("-----------------------------------------")

#Guardar en JSON
def save_json(inventory):
    clave=len(inventory)
    if clave == 0:
        print("Inventario vacio, Por favor añade productos al inventario")
    else:   
        with open("datos.json", "w", encoding="utf-8") as laboratorio_3:
            json.dump(inventory, laboratorio_3, indent=4, ensure_ascii=False)

#Cargar JSON
def upload_json():
    with open("datos.json", "r", encoding="utf-8") as laboratorio_3:
        inventory = json.load(laboratorio_3)
    return inventory
#Save_CSV
def save_CSV(inventory,ruta="datos.csv",incluir_header=True):
    clave=len(inventory)
    if clave == 0:
        print("Inventario vacio, Por favor añade productos al inventario")
    else:
        try:
                with open(ruta, "w", encoding="utf-8", newline="") as archivo:
                    writer = csv.writer(archivo, delimiter=",")

                    if incluir_header:
                        writer.writerow(["nombre", "precio", "cantidad"])

                    for producto in inventory.values():
                        writer.writerow([
                            producto["nombre_producto"],
                            producto["precio_producto"],
                            producto["cantidad_producto"]
                        ])

                print(f"Inventario guardado en: {ruta}")

        except PermissionError:
            print("Error: no tienes permisos para escribir en ese archivo.")
        except OSError as e:
            print(f"Error al guardar el archivo: {e}")
#Cargar CSV
def upload_CSV(filename="datos.csv"):
    inventory = {}
    try:
        with open(filename, "r", encoding="utf-8", newline="") as archivo:
            reader = csv.DictReader(archivo)

            clave = 0
            for row in reader:
                clave += 1
                inventory[clave] = {
                    "nombre_producto": row["nombre"],
                    "precio_producto": float(row["precio"]),
                    "cantidad_producto": int(row["cantidad"])
                }

        return inventory

    except FileNotFoundError:
        print("Error: no se encontró el archivo CSV.")
        return {}
    except KeyError:
        print("Error: el archivo CSV no tiene los encabezados correctos.")
        print("Debe tener: nombre,precio,cantidad")
        return {}
    except ValueError:
        print("Error: uno o más datos del CSV no tienen el formato correcto.")
        return {}
    except Exception as e:
        print(f"Error inesperado al cargar el CSV: {e}")
        return {}
