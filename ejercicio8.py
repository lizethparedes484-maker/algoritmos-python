#Almacenes “El harapiento distinguido” tiene una promoción: a todos los trajes que tienen un precio superior a $2500.00 se les aplicará un descuento de 15 %, a todos los demás se les aplicará sólo 8 %. Realice un algoritmo para determinar el precio final que debe pagar una persona por comprar un traje y de cuánto es el descuento que obtendrá.
# Pedimos el costo original del traje
precio_original = float(input("Ingrese el precio del traje ($): "))

# nos aseguramos que el usuario no ingrese un precio de cero o negativo
if precio_original <= 0:
    print("El precio debe ser mayor a cero.")
else:
    # Determinamos el porcentaje de descuento según el monto de la compra:
    # Si cuesta más de $2500, le aplicamos el 15% (0.15)
    if precio_original > 2500.00:
        porcentaje_descuento = 0.15
    # Si cuesta $2500 o menos, le aplicamos solo el 8% (0.08)
    else:
        porcentaje_descuento = 0.08
    # Calculamos cuánto dinero representa ese porcentaje
    monto_descuento = precio_original * porcentaje_descuento
    # Le restamos el descuento al valor original para obtener el total
    precio_final = precio_original - monto_descuento
#imprimimos y mostramos el resultado
    print("\n--- RESUMEN DE LA COMPRA ---")
    print(f"Precio original: ${precio_original:.2f}")
    print(f"Descuento aplicado ({int(porcentaje_descuento * 100)}%): ${monto_descuento:.2f}")
    print(f"Precio final a pagar: ${precio_final:.2f}")
