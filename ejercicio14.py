#La política de la compañía telefónica “chimefón” es: “Chismea + x -”. Cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan $1.00 peso c/u, los siguientes tres, 80¢ centavos de peso c/u, los siguientes dos minutos, 70¢ centavos de peso c/u, y a partir deldécimo minuto, 50¢ centavos de peso c/u. Además, se carga un impuesto de 3 % cuando es domingo, y si es día hábil, en turno matutino, 15 %, y en turno vespertino, 10 %. Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada en moneda nacional mexicana (MXN).
# Pedimos la duración de la llamada en minutos
duracion = int(input("Ingresa la duración de la llamada (minutos): "))
# Preguntamos el tipo de día
dia = input("¿Es día 'domingo' o 'habil'?: ")

# Si es domingo, la tarifa del impuesto es del 3%
if dia == "domingo":
    porcentaje_impuesto = 0.03
    
 # Pedimos el turno en el que se hizo la llamada   
turno = input("Ingresa el turno ('matutino' , 'vespertino' , 'ninguno'): ")
    
# Si fue en la mañana, aplica 15% de impuesto    
if turno == "matutino":
    porcentaje_impuesto = 0.15

# Si fue en la tarde, aplica 10% de impuesto
elif turno == "vespertino":
    porcentaje_impuesto = 0.10

# Si no aplica turno o es domingo, se mantiene el 3% de impuesto
elif turno == "ninguno":
    porcentaje_impuesto=0.03

# Si se ingresó un turno no válido, no se cobra impuesto
else:
    print("Turno no reconocido, se aplicará 0 de impuesto.")
    porcentaje_impuesto = 0.0


# Calculamos el subtotal acumulado 
# duracion 1: Hasta 5 minutos a $1.00 por minuto
if duracion <= 5:
    subtotal = duracion * 1.00

# duracion 2: Los primeros 5 min a $1.00 + los minutos restantes a $0.80
elif duracion <= 8:
    subtotal = (5 * 1.00) + ((duracion - 5) * 0.80)

# duracion 3: 5 min a $1.00 + 3 min a $0.80 + los minutos restantes  a $0.70
elif duracion <= 10:
    subtotal = (5 * 1.00) + (3 * 0.80) + ((duracion - 8) * 0.70)
    
# duracion 4: 5 min a $1.00 + 3 min a $0.80 + 2 min a $0.70 + el resto a $0.50
else:
    subtotal = (5 * 1.00) + (3 * 0.80) + (2 * 0.70) + ((duracion - 10) * 0.50)

# Sacamos el monto del impuesto sobre el subtotal y obtenemos el total    
impuesto = subtotal * porcentaje_impuesto
total = subtotal + impuesto

#imprimimos los resultados
print("\n--- DESGLOSE DE COBRO (MXN) ---")
print(f"Subtotal por tiempo de llamada: ${subtotal} MXN")
print(f"Impuesto aplicado ({int(porcentaje_impuesto * 100)}%): ${impuesto} MXN")
print(f"Total a pagar: ${total:} MXN")



    
