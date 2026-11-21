# problema 15/20

total = 0
for i in range (1,7):
    
    bimestre = float(input(f"¿Cual es el consumo en kWh del bimestre {i}?"))
    if bimestre < 250:
        costouni = 1.5
        costobi = bimestre * costouni
    else:
        costouni = 2.5
        costobi = (bimestre*costouni) - 249
    total += costobi
    print(f"El importe a  pagar en el bimestre {i}, es de {costobi}")
print (f"El costo anual es de {total}")
