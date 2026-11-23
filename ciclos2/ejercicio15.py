# problema 15/20
"""
Consumo de energía eléctrica y tarifas por escalón: Se registra el consumo de luz en kWh durante 6 bimestres.
Si el consumo en un bimestre es menor o igual a 250 kWh, la tarifa es de $1.5 por kWh; si supera los 250 kWh, el exceso se cobra a $2.8 por kWh. 
Muestra el importe a pagar en cada bimestre y el gasto anual total.
"""
# inicialización del acumulador del costo anual total en cero
total = 0

# ciclo for que recorre los 6 bimestres del año este inicio en 1 y termino  en 7 
for i in range (1,7):
    # se solicitud el consumo eléctrico en kWh correspondiente al bimestre actual mediante un input
    bimestre = float(input(f"¿Cual es el consumo en kWh del bimestre {i}?"))

    # condicionales que determinan la clasificaion según el consumo
    if bimestre < 250:
        #  si el consumo es menor a 250 kWh la tarifa unitaria es de 1.5 
        costouni = 1.5
        # se calcula el costo bimestral multiplicando consumo por tarifa unitaria
        costobi = bimestre * costouni
    else:
        # si no cumple con la primera condicion la tarifa unitaria de 2.5 
        costouni = 2.5
        # se calcula el costo bimestral multiplicando y aplicando el ajuste
        costobi = (bimestre*costouni) - 249

    # el acumuladorsuma el costo de cada bimestre para obtener el costo anual total
    total += costobi

    # se imprime el importe correspondiente al bimestre actual
    print(f"El importe a  pagar en el bimestre {i}, es de {costobi}")

# se imprime el acumulado anual 
print (f"El costo anual es de {total}")
