# problema 8/20
media = km = rendimientotal = 0

for i in range (1,9,1):
    distancia = float(input(f"¿Cual es la distacia recorrida (kilometros) en la etapa {i}?: "))
    combustible = float(input(f"¿Cual es el combustible consumido (litros) en la etapa {i}?: "))
    consumoprom = distancia/combustible
    km += distancia
    rendimientotal += consumoprom
    print (f"El consumo promedio (km/l)  de la etapa {i} es: {consumoprom}")
prom = rendimientotal/8

print (f"El total de kilometros recorridos es: {km}")
print (f"El rendimiento promedio total del vieje es: {prom} ")
