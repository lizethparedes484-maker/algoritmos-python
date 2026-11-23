# problema 13/20
"""
Control de producción por turnos: Una fábrica registra la cantidad de piezas producidas por 3 turnos (Mañana, Tarde y Noche) a lo largo de 7 días.
Acumula la producción total de cada turno al final de la semana e indica cuál fue el turno más productivo.
"""
# inicialización de la variable para el máximo acumulado y de los acumuladores, todos inician en cero
masproductivo = totalmañana = totalnoche = totaltarde = 0

# ciclo que recorre los 7 días de la semana 
for i in range(1,8):
    # pregunta las piezas producidas en cada turno durante el día mediante un input
    mañana = int(input(f"¿Cual fue la cantidad de piezas producidas en el turno de la mañana en el dia {i}?"))
    tarde = int(input(f"¿Cual fue la cantidad de piezas producidas en el turno de la tarde en el dia {i}?"))
    noche = int(input(f"¿Cual fue la cantidad de piezas producidas en el turno de la noche en el dia {i}?"))
  
    # acumuladores que suman las piezas diarias de cada turno para obtener el total semanal por turno
    totalmañana += mañana
    totaltarde += tarde
    totalnoche += noche

# condicionales para determinar cuál turno tuvo la mayor producción acumulada en la semana
if totalmañana > masproductivo:
    masproductivo = totalmañana
    turno = "mañana"
if totaltarde > masproductivo:
    masproductivo = totaltarde
    turno = "tarde"
if totalnoche > masproductivo:
    masproductivo = totalnoche
    turno = "noche"

# se imprimen todos los resultados
print(f"la cantidad de produccion acumulada en el turno de la mañana es de {totalmañana}")
print(f"la cantidad de produccion acumulada en el turno de la tarde es de {totaltarde}")
print(f"la cantidad de produccion acumulada en el turno de la noche es de {totalnoche}")
print (f"El turno mas productivo fue el turno de la {turno} con una produccion acumulada de {masproductivo} piezas a la semana")
