#problema 19/20
"""
Sensor de nivel de depósito con alerta: Un tanque de agua de 1,000 litros recibe descargas periódicas de agua.
En cada ciclo se ingresa el volumen en litros de cada descarga hasta que el tanque alcance o supere el 95% de su capacidad total.
Reporta cuántas descargas se necesitaron y el volumen total almacenado.
"""
# definimos la capacidad total del tanque en litros y del límite operativo al 95 porciento
capacidad_total = 1000
limite = capacidad_total*0.95

# se inicia el contador y acumulador en cero
suma = suma2 = 0

# ciclo con rango un máximo de intentos de 1000 para registrar descargas este inicia en 1
for i in range (1, 1000 + 1):
    # se pide la descarga en litros mediante un input
    volumendescarga = float(input(f"Ingrese los litros de la descarga {i}:"))

    # contador que suma de 1 en 1 el número de descargas realizadas
    suma2 += 1 
    # acumulador que suma los litros de cada descarga al volumen total almacenado
    suma += volumendescarga

    # condicional que verifica si el volumen acumulado alcanzó o superó el límite del 95%
    if suma >= limite :
        print(f"El tanque ha llegado a su limite")
        # interrumpe el ciclo anticipadamente al alcanzarse el límite del tanque con un break
        break

#se imprimen los resultados
print(f"Se necesitaron {suma2} descargas para llegar al limite del tanque")
print(f"El volumen total almacenado es de {suma} litros")
