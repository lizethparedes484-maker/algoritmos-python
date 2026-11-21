# problema 17/20
prestamo = float(input("¿De cuanto es el prestamo?: "))
meses = int(input("¿A cuantos meses se va a pagar?: "))

capitalmensual = prestamo / meses
saldorestante = prestamo
interes = 0.015

for i in range(1, meses+1):
    interes_mes = saldorestante * interes
    cuota = capitalmensual + interes_mes
    saldorestante = saldorestante - capitalmensual

    print(f"En en el mes {i} la cuota a pagar es: ${cuota} y el saldo que queda pendiente es: ${saldorestante}")
