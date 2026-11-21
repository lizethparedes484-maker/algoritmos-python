# problema 13/20
masproductivo = totalmañana = totalnoche = totaltarde = 0

for i in range(1,8):
    
    mañana = int(input(f"¿Cual fue la cantidad de piezas producidas en el turno de la mañana en el dia {i}?"))
    tarde = int(input(f"¿Cual fue la cantidad de piezas producidas en el turno de la tarde en el dia {i}?"))
    noche = int(input(f"¿Cual fue la cantidad de piezas producidas en el turno de la noche en el dia {i}?"))
  
    totalmañana += mañana
    totaltarde += tarde
    totalnoche += noche

if totalmañana > masproductivo:
    masproductivo = totalmañana
    turno = "mañana"
if totaltarde > masproductivo:
    masproductivo = totaltarde
    turno = "tarde"
if totalnoche > masproductivo:
    masproductivo = totalnoche
    turno = "noche"

print(f"la cantidad de produccion acumulada en el turno de la mañana es de {totalmañana}")
print(f"la cantidad de produccion acumulada en el turno de la tarde es de {totaltarde}")
print(f"la cantidad de produccion acumulada en el turno de la noche es de {totalnoche}")
print (f"El turno mas productivo fue el turno de la {turno} con una produccion acumulada de {masproductivo} piezas a la semana")
