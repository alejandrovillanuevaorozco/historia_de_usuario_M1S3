from funciones import *
inventario={}
clave=0
mensaje="¿Cuantos productos quieres añadir en el inventario?"
n=validar_numeros(mensaje)

valido = False
i=1
while i<=n:
    clave = clave+1
    nombre=input("Introduce el nombre del producto: ")
    valido = False
    while not valido:
        try:
            precio=int(input("Introduce el precio del producto: "))
            if precio >= 0:
                valido = True
            else:
                print("El precio no puede ser negativo.")
        except ValueError:
            print("Debe ingresar un número válido.")
    valido = False
    while not valido:
        try:
            cantidad=int(input("Introduce la cantidad del producto: "))
            if cantidad >= 0:
                valido = True
            else:
                print("El precio no puede ser negativo.")
        except ValueError:
            print("Debe ingresar un número válido.")
    inventario[clave] = {"nombre_producto":nombre,"precio_producto":precio, "cantidad_producto":cantidad}
    i=i+1
print(inventario)
#unidades_totales = suma de cantidad
#valor_total = suma de precio * cantidad
#producto_mas_caro (nombre y precio)
#producto_mayor_stock (nombre y cantidad)
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
