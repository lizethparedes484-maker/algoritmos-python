# problema 8/20
"""
Rendimiento de un vehículo por trayecto: En un viaje de 8 etapas, se registra la distancia recorrida (en km) y el combustible consumido (en litros) de cada etapa.
Calcula el consumo promedio (km/l) de cada etapa, el total de km recorridos y el rendimiento promedio total del viaje.
"""

#se inician todos los acumuladores en cero
media = km = rendimientotal = 0

#ciclo que se va a repetir 8 veces 
for i in range (1,9,1):
    #pregunta la distancia recorrida (km) en cada etapa mediante un input
    distancia = float(input(f"¿Cual es la distacia recorrida (kilometros) en la etapa {i}?: "))
    #pregunta el combustible (litros) consumido en cada etapa mediante un input
    combustible = float(input(f"¿Cual es el combustible consumido (litros) en la etapa {i}?: "))
    #calculo del consumo promedio
    consumoprom = distancia/combustible
    km += distancia                 # se acumula la distancia en km
    rendimientotal += consumoprom   # se acumula el consumo promedio en redimiento
    #se imprime el consumo promedio en cada etapa
    print (f"El consumo promedio (km/l)  de la etapa {i} es: {consumoprom}")a
prom = rendimientotal/8             # se calcula el promedio total del viaje

#se imprimen los resultados
print (f"El total de kilometros recorridos es: {km}")
print (f"El rendimiento promedio total del vieje es: {prom} ")
