duracion = int(input("Ingresa la duración de la llamada (minutos): "))
dia = input("¿Es día 'domingo' o 'habil'?: ")


if dia == "domingo":
    porcentaje_impuesto = 0.03
    
    
turno = input("Ingresa el turno ('matutino' , 'vespertino' , 'ninguno'): ")
    
    
if turno == "matutino":
    porcentaje_impuesto = 0.15
elif turno == "vespertino":
    porcentaje_impuesto = 0.10
elif turno == "ninguno":
    porcentaje_impuesto=0.03
else:
    print("Turno no reconocido, se aplicará 0 de impuesto.")
    porcentaje_impuesto = 0.0



if duracion <= 5:
    subtotal = duracion * 1.00
elif duracion <= 8:
    subtotal = (5 * 1.00) + ((duracion - 5) * 0.80)
elif duracion <= 10:
    subtotal = (5 * 1.00) + (3 * 0.80) + ((duracion - 8) * 0.70)
else:
    subtotal = (5 * 1.00) + (3 * 0.80) + (2 * 0.70) + ((duracion - 10) * 0.50)

    
impuesto = subtotal * porcentaje_impuesto
total = subtotal + impuesto

print("\n--- DESGLOSE DE COBRO (MXN) ---")
print(f"Subtotal por tiempo de llamada: ${subtotal} MXN")
print(f"Impuesto aplicado ({int(porcentaje_impuesto * 100)}%): ${impuesto} MXN")
print(f"Total a pagar: ${total:} MXN")



    