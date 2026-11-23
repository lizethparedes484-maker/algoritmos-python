# problema 17/20
"""
Tabla de amortización simplificada: Para un préstamo de valor P diferido a M meses, calcula el pago de capital constante más un interés mensual fijo del 1.5% sobre el saldo insoluto. 
Muestra la tabla mes a mes con la cuota a pagar y el saldo restante.
"""
#pregunta la  cantidad del prestamo y los mese en que pagara mediante un input
prestamo = float(input("¿De cuanto es el prestamo?: ")) 
meses = int(input("¿A cuantos meses se va a pagar?: "))

capitalmensual = prestamo / meses  # calcula la cantidad mensual que se  dara
saldorestante = prestamo           # el saldo restante es pretamo
interes = 0.015                    # interes fijo del 1.5 porciento

# ciclo  que recorre desde el mes 1 hasta el total de meses 
for i in range(1, meses+1):
    # calculo del interés correspondiente al mes actual sobre el saldo pendiente
    interes_mes = saldorestante * interes
    # calculo de la cuota mensual sumando el abono a capital y el interés del mes
    cuota = capitalmensual + interes_mes
    # actualizacion del saldo restante restando el abono a capital realizado en el mes
    saldorestante = saldorestante - capitalmensual

    # Impresión de la cuota a pagar y del saldo pendiente al cierre del mes actual
    print(f"En en el mes {i} la cuota a pagar es: ${cuota} y el saldo que queda pendiente es: ${saldorestante}")

