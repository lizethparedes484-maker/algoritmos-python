#Almacenes “El harapiento distinguido” tiene una promoción: a todos los trajes que tienen un precio superior a $2500.00 se les aplicará un descuento de 15 %, a todos los demás se les aplicará sólo 8 %. Realice un algoritmo para determinar el precio final que debe pagar una persona por comprar un traje y de cuánto es el descuento que obtendrá.

precio_original = float(input("Ingrese el precio del traje ($): "))

if precio_original <= 0:
    print("El precio debe ser mayor a cero.")
else:
    if precio_original > 2500.00:
        porcentaje_descuento = 0.15
    else:
        porcentaje_descuento = 0.08

    monto_descuento = precio_original * porcentaje_descuento
    precio_final = precio_original - monto_descuento

    print("\n--- RESUMEN DE LA COMPRA ---")
    print(f"Precio original: ${precio_original:.2f}")
    print(f"Descuento aplicado ({int(porcentaje_descuento * 100)}%): ${monto_descuento:.2f}")
    print(f"Precio final a pagar: ${precio_final:.2f}")
