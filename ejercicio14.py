#La política de la compañía telefónica “chimefón” es: “Chismea + x -”. Cuando se realiza una llamada, el cobroes por el tiempo que ésta dura, de tal forma que losprimeros cinco minutos cuestan $1.00 peso c/u, lossiguientes tres, 80¢ centavos de peso c/u, los siguientesdos minutos, 70¢ centavos de peso c/u, y a partir deldécimo minuto, 50¢ centavos de peso c/u.Además, se carga un impuesto de 3 % cuando esdomingo, y si es día hábil, en turno matutino, 15 %, y enturno vespertino, 10 %. Realice un algoritmo paradeterminar cuánto debe pagar por cada concepto unapersona que realiza una llamada en moneda nacional mexicana (MXN).

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



    
