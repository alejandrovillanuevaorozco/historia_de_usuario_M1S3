from funciones import *
opcion="x"
inventario={}
while opcion!="9":
    print("==MENÚ PRINCIPAL==")
    opcion=input("1. Agregar"+
             "\n2. Mostrar"+
             "\n3. Buscar"+
             "\n4. Actualizar"+
             "\n5. Eliminar"+
             "\n6. Estadisticas"+
             "\n7. Guardar CSV"+
             "\n8. Cargar CSV"+
             "\n9. Salir"+
             "\n Por favor ingrese la opción a elegir: "
             )
    match opcion:
        case "1":
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
