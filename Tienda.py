# Carrito de compras

# Productos y precios
productos = {"1": {"nombre": "Manzanas", "precio": 0.5},
             "2": {"nombre": "Leche", "precio": 1.0},
             "3": {"nombre": "Pan", "precio": 1.5},
             "4": {"nombre": "Huevos", "precio": 0.2}}

# Mostrar productos disponibles
print("Productos Disponibles:")
for clave, valor in productos.items():
    print(f"{clave}. {valor['nombre']} - ${valor['precio']} cada uno")

# Carrito de compras como cadena de texto
carrito = ""

# Proceso de selección de productos
while True:
    eleccion = input("Elige un producto (1-4) o escribe 'fin' para terminar: ")
    if eleccion in productos:
        cantidad = int(input(f"Cantidad de {productos[eleccion]['nombre']}: "))
        carrito += f"{productos[eleccion]['nombre']} ({cantidad} x ${productos[eleccion]['precio']})\n"
    elif eleccion == 'fin':
        break
    else:
        print("Opción no válida. Por favor, elige un producto válido o escribe 'fin'.")

# Calculando el total
total = 0
print("\nTu carrito:")
for linea in carrito.split('\n'):
    if linea:
        nombre, detalles = linea.split(' (')
        cantidad, precio = detalles.replace(')', '').split(' x $')
        subtotal = int(cantidad) * float(precio)
        print(f"{nombre}: {cantidad} x ${precio} = ${subtotal}")
        total += subtotal

print(f"\nTotal a pagar: ${total}")

# este programa fue desarrollado por Edilson Francisco Guillin 
#primer ciclo  Tecnologías de la informacion
# UEA

