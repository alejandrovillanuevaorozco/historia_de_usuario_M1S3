from funciones import *
opcion="x"
inventario={}
while opcion!="11":
    print("--------------------------------------------------")
    print("==MENÚ PRINCIPAL==")
    opcion=input("1. Agregar"+
             "\n2. Mostrar"+
             "\n3. Buscar"+
             "\n4. Actualizar"+
             "\n5. Eliminar"+
             "\n6. Estadisticas"+
             "\n7. Guardar JSON"+
             "\n8. Cargar JSON"+
             "\n9. Guardar CSV"+
             "\n10. Cargar CSV"+
             "\n11. Salir"+
             "\n Por favor ingrese la opción a elegir: "
             )
    match opcion:
        case "1":
            print("--------------------------------------------------")
            print("===AGREGAR PRODUCTOS AL INVENTARIO===")
            clave=len(inventario)
            inventario=(create(inventario,clave))            
        case "2":
            print("--------------------------------------------------")
            print("===INVENTARIO DE PRODUCTOS===")
            read(inventario)
        case "3":
            print("--------------------------------------------------")
            print("===BUSQUEDA DE PRODUCTOS===")
            search_product(inventario)
        case "4":
            print("--------------------------------------------------")
            print("===ACTUALIZACIÓN DE PRODUCTOS===")
            update(inventario)
        case "5":
            print("--------------------------------------------------")
            print("===ELIMINACIÓN DE PRODUCTOS===")
            delete(inventario)
        case "6":
            print("--------------------------------------------------")
            print("===ESTADISTICAS DE PRODUCTOS===")
            estadisticas(inventario)
        case "7":
            print("--------------------------------------------------")
            print("===GUARDANDO ARCHIVO JSON...===")
            save_json(inventario)
        case "8":
            print("--------------------------------------------------")
            print("===CARGANDO INVENTARIO DEL ARCHIVO JSON...===")
            inventario=upload_json()
        case "9":
            print("--------------------------------------------------")
            print("===GUARDANDO ARCHIVO CSV...===")
            save_CSV(inventario)
        case "10":
            print("--------------------------------------------------")
            print("===CARGANDO INVENTARIO DEL ARCHIVO CSV...===")
            inventario=upload_CSV()

        case "11":
            print("Muchas gracias por utilizar nuestro programa") 
        case _:
            print("Opcion invalida, por favor solo digite números del 1 al 11")