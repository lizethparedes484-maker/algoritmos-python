#Un estacionamiento requiere determinar el cobro que debe aplicar a las personas que lo utilizan. Considere que el cobro es con base en las horas que lo disponen y que las fracciones de hora se toman como completas
#imortamos la funcion math para poder usar la funcion de redondeo
import math

#le pedimos al usuario que ingrese al cantidad de minutos que estuvo estacionado
minutos_estancia = int(input("¿cuanto tiempo tiene de estancia?(minutos)"))

#definimos el precio fijo por hora
precio_hora = 20

# Convertimos los minutos a horas y redondeamos hacia arriba para cobrar cualquier fracción como una hora completa
redondeo = math.ceil (minutos_estancia/60)

#sacamos el total multiplicando las horas por la tarifa fija
cobro = precio_hora*redondeo

#mostramos el total
print(f"su pago es de: {cobro}")
