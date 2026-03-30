#Validar numeros
def validar_numeros(mensaje):
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
#Crear diccionario de diccionario
def create(inventario,clave):
    mensaje="¿Cuantos productos quieres añadir en el inventario?"
    n=validar_numeros(mensaje)
    i=1
    while i<=n:
        clave = clave+1
        nombre=input("Introduce el nombre del producto: ")
        mensaje="Introduce el precio del producto"
        precio=validar_numeros(mensaje)
        mensaje="Introduce la cantidad del producto: "
        cantidad=validar_numeros(mensaje)
        inventario[clave] = {"nombre_producto":nombre,"precio_producto":precio, "cantidad_producto":cantidad}
        i=i+1
    print(inventario)
    return inventario
#Mostrar diccionario de diccionario
def read(inventario):
    clave=len(inventario)
    if clave == 0:
        print("Inventario vacio")
    else:
        print("==INVENTARIO==\n")
        for clave, datos in inventario.items():
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
def buscar_producto(inventario):
    clave=len(inventario)
    if clave == 0:
        print("Inventario vacio")
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
                    print("Busqueda por ID: ")
                    mensaje="Ingrese el id a buscar"
                    id_buscado=validar_numeros(mensaje)
                    valid=inventario.get(id_buscado, "No se encontró el dato proporcionado")
                    print(valid)
                    if valid!="No se encontró el dato proporcionado":
                        valid=id_buscado
                    return valid
                case "2":
                    print("Busqueda por nombre del producto: ")
                    nombre_buscado=input("Ingrese el nombre del producto a buscar: ")
                    valid = "No se encontró el dato proporcionado"
                    nombre=""

                    for clave, producto in inventario.items():
                        if producto["nombre_producto"] == nombre_buscado:
                            nombre=producto["nombre_producto"]
                            precio=producto["precio_producto"]
                            cantidad=producto["cantidad_producto"]
                            valid=clave
                    if nombre==nombre_buscado:
                        print("Nombre del producto: ", nombre,
                            "\nPrecio: ", precio,
                            "\nCantidad: ", cantidad,
                            "\n")
                        print("-----------------------------------------")
                        return valid
                    else:
                        print(valid)
                        return valid
                case "3":
                    continue
                case _:
                    print("Opcion invalida, por favor solo digite números del 1 al 9")
#Eliminar campos
def delete(inventario):
    print("Eliminación por ID: ")
    print("Por favor, primero busque el Id o nombre a eliminar... ")
    id_eliminado=buscar_producto(inventario)
    print(id_eliminado)
    if id_eliminado!="No se encontró el dato proporcionado":
        print("Se borrarán los todos los campos del ID: ", id_eliminado)
        op="x"
        while op!="S".upper() and op!="N".upper():
                    op = input("¿Desea eliminarlos? (S/N): ").upper()
                    if op != "S".upper() and op!="N".upper():
                        print("Dato ingresado erronéo, por favor solo coloca 'S' o 'N'")
                    if op=="S".upper():
                        del inventario[id_eliminado]
                        print("Campos eliminados")
                    elif op=="N".upper():
                        print("Campos no eliminados")
                        continue
#Estadisticas
def estadisticas(inventario):
    unidades_totales=0
    valor_total=0
    producto_mayor_stock=""
    cantidad_mayor_stock=0
    producto_mas_caro=""
    precio_mas_caro=0
    clave=len(inventario)
    if clave == 0:
        print("Inventario vacio")
    else:
        print("==ESTADISTICAS==\n")
        for clave, datos in inventario.items():
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
