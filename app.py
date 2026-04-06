from funciones import *
opcion="x"
inventario={}
<<<<<<< HEAD
while opcion!="11":
    print("--------------------------------------------------")
=======
while opcion!="9":
>>>>>>> c4844fc8f169f85d6ff007e50cfbd059f1ff78ee
    print("==MENÚ PRINCIPAL==")
    opcion=input("1. Agregar"+
             "\n2. Mostrar"+
             "\n3. Buscar"+
             "\n4. Actualizar"+
             "\n5. Eliminar"+
             "\n6. Estadisticas"+
<<<<<<< HEAD
             "\n7. Guardar JSON"+
             "\n8. Cargar JSON"+
             "\n9. Guardar CSV"+
             "\n10. Cargar CSV"+
             "\n11. Salir"+
=======
             "\n7. Guardar CSV"+
             "\n8. Cargar CSV"+
             "\n9. Salir"+
>>>>>>> c4844fc8f169f85d6ff007e50cfbd059f1ff78ee
             "\n Por favor ingrese la opción a elegir: "
             )
    match opcion:
        case "1":
<<<<<<< HEAD
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
=======
            print("Entró en agregar")
            clave=len(inventario)
            inventario=(create(inventario,clave))
            print(inventario)
            
        case "2":
            print("Entró en Mostrar")
            read(inventario)
        case "3":
            print("Entró en Buscar")
            buscar_producto(inventario)
        case "4":
            print("Entró en Actualizar")
        case "5":
            print("Entró en Eliminar")
            delete(inventario)
        case "6":
            print("Entró en Estadisticas")
            estadisticas(inventario)
        case "7":
            print("Guardar CSV")
        case "8":
            print("Cargar CSV")
        case "9":
            print("Muchas gracias por utilizar nuestro programa") 
        case _:
            print("Opcion invalida, por favor solo digite números del 1 al 9")
>>>>>>> c4844fc8f169f85d6ff007e50cfbd059f1ff78ee
