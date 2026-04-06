<<<<<<< HEAD
# Sistema de Gestión de Inventario - Python

## Descripción General

**Sistema completo de gestión de inventario** implementado en Python 3.x que utiliza un **diccionario de diccionarios** como base de datos en memoria. Soporta operaciones **CRUD** completas (Crear, Leer, Actualizar, Eliminar) y **persistencia bidireccional** en formatos **JSON** y **CSV**.

## Arquitectura del Sistema
app.py ← Controlador Principal (Menú + Lógica de Flujo)
↓
funciones.py ← Módulo de Negocio (CRUD + Validaciones + Persistencia)
↓
inventario{} ← Base de datos en memoria (Diccionario de Diccionarios)
↓
datos.json ← Persistencia JSON
datos.csv ← Persistencia CSV


## Estructura de Datos

```python
inventario = {
    1: {
        "nombre_producto": "Martillo", 
        "precio_producto": 15000, 
        "cantidad_producto": 25
    },
    2: {
        "nombre_producto": "Destornillador", 
        "precio_producto": 8000, 
        "cantidad_producto": 50
    }
}
```

| **Campo** | **Tipo** | **Descripción** |
|-----------|----------|-----------------|
| `clave` | `int` | ID autoincremental |
| `nombre_producto` | `str` | Nombre del producto (solo letras) |
| `precio_producto` | `int` | Precio unitario (≥ 0) |
| `cantidad_producto` | `int` | Stock disponible (≥ 0) |

## Funcionalidades Implementadas

### **1. Menú Principal (app.py)**
Agregar productos
Mostrar inventario
Buscar productos
Actualizar productos
Eliminar productos
Estadísticas
Guardar JSON
Cargar JSON
Guardar CSV
Cargar CSV
Salir


### **2. Operaciones CRUD (funciones.py)**

| **Operación** | **Función** | **Características** |
|---------------|-------------|-------------------|
| **Crear** | `create(inventario, clave)` | Agrega múltiples productos con ID autoincremental |
| **Leer** | `read(inventario)` | Muestra inventario completo formateado |
| **Buscar** | `search_product(inventario)` | Submenú: ID o nombre (insensible a mayúsculas) |
| **Actualizar** | `update(inventario)` | Busca → submenú para modificar campo(s) específico(s) |
| **Eliminar** | `delete(inventario)` | Busca → confirma eliminación por ID |

### **3. Validaciones de Entrada**
- **`validate_numbers()`**: Solo números enteros ≥ 0
- **`validate_field()`**: Solo letras (alfabético), sin números ni espacios vacíos

### **4. Análisis y Estadísticas**
Producto más caro (precio máximo)
Producto con mayor stock (cantidad máxima)
Total de unidades en inventario
Valor total por producto (precio × cantidad)

### **5. Persistencia Completa**
| **Formato** | **Guardar** | **Cargar** | **Estructura** |
|-------------|-------------|------------|----------------|
| **JSON** | `save_json(inventario)` | `upload_json()` | Diccionario completo |
| **CSV** | `save_CSV(inventario)` | `upload_CSV()` | `nombre,precio,cantidad` |

## Características Técnicas

### **Manejo de Errores**
CSV Guardar: PermissionError, OSError
CSV Cargar: FileNotFoundError, KeyError, ValueError, Exception genérica
Validaciones: ValueError (entrada inválida)


### **Módulos Utilizados**
```python
import json    # Persistencia JSON
import csv     # Persistencia CSV
```

## Flujo de Ejecución



## Ejemplo de Uso
INICIO → Menú Principal → [Opción]
↓
├─ 1: create() → Menú
├─ 2: read() → Menú
├─ 3: search_product() → Menú
├─ 4: update() → Menú
├─ 5: delete() → Menú
├─ 6: estadisticas() → Menú
├─ 7: save_json() → Menú
├─ 8: upload_json() → Menú
├─ 9: save_CSV() → Menú
├─ 10: upload_CSV() → Menú
└─ 11: SALIR ← Fin

```bash
# 1. Agregar productos
$ python app.py
Opción 1 → Agregar 2 productos → ID:1 "Martillo", ID:2 "Destornillador"

# 2. Ver inventario
Opción 2 → Muestra ambos productos formateados

# 3. Guardar datos
Opción 7 → datos.json creado
Opción 9 → datos.csv creado

# 4. Salir y reiniciar
$ python app.py
Opción 8 → Carga datos.json
Opción 10 → Carga datos.csv
```

## Estado de Funcionalidades

| **Módulo** | **Estado** | **Notas** |
|------------|------------|-----------|
| CRUD | ✅ Completo | Validaciones robustas |
| JSON | ✅ 100% | Guardar/Cargar perfectos |
| CSV | ✅ Corregido | Compatible bidireccional |
| Estadísticas | ✅ Funcional | Análisis completo |
| UI/UX | ✅ Excelente | Menús intuitivos |

## Archivos Generados
├── app.py # Controlador principal
├── funciones.py # Lógica de negocio
├── datos.json # Persistencia JSON
├── datos.csv # Persistencia CSV
└── README.md # Documentación del proyecto

## Casos de Uso

- **Gestión de inventario pequeña/mediada**
- **Laboratorio académico de estructuras de datos**
- **Prototipo de sistema de inventario**
- **Aprendizaje de manejo de archivos (JSON/CSV)**

## Autor

**Alejandro Villanueva**  
*Desarrollador Junior | Ingeniero de Sistemas*

---
=======
# historia_de_usuario_M1S3
Inventario avanzado con colecciones y persistencia en archivos
>>>>>>> c4844fc8f169f85d6ff007e50cfbd059f1ff78ee
