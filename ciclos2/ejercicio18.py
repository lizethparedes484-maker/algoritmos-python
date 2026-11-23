#problema 18/20
"""
Análisis de velocidad de vehículo (Multas y promedios): Un radar registra la velocidad de 12 vehículos en una carretera donde el límite es 90 km/h. 
Cuenta cuántos vehículos iban dentro del límite y cuántos cometieron infracción.
De los infractores, indica cuántos superaban los 110 km/h (multa grave).
"""
#inician los contadores en cero
dentro = infraccion = multagrave = 0

# un ciclo de 12 que inicia en 1
for i in range (1,13):
    #pregunta la velocidad de cada vehiculo mediante un input
    vehiculo = float(input(f"¿A que velocidad iba el vehiculo {i}?"))
    if vehiculo <= 90:
        #si la velocidad es menor o igual a 90 el contador dentro suma 1
        dentro += 1
    
    elif vehiculo > 110:
        #si la velocidad es mayor a 110 el contador multa grave e infraccion suman ambos 1
        multagrave += 1
        infraccion += 1
    else:
        #si la velocidad no este en ningun condicional anterior el contador infraccion suma 1
        infraccion += 1

#se imprimen los resultados
print(f"La cantidad de vehiculos que iban dentro del limite son {dentro}")
print(f"La cantidad de vehiculos que superaron el limite son: {infraccion} y {multagrave} de ellos tienen multa grave por superar los 110 km/h")
    
