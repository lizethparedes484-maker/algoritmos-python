#Un estacionamiento requiere determinar el cobro que debe aplicar a las personas que lo utilizan. Considere que el cobro es con base en las horas que lo disponen y que las fracciones de hora se toman como completas

import math
minutos_estancia = int(input("¿cuanto tiempo tiene de estancia?(minutos)"))
precio_hora = 20
redondeo = math.ceil (minutos_estancia/60)
cobro = precio_hora*redondeo
print(f"su pago es de: {cobro}")
