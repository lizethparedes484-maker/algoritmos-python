import math
minutos_estancia = int(input("¿cuanto tiempo tiene de estancia?(minutos)"))
precio_hora = 20
redondeo = math.ceil (minutos_estancia/60)
cobro = precio_hora*redondeo
print(f"su pago es de: {cobro}")