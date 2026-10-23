#problema 16 ciclos

n = int(input("Total de ventas: "))  #pide el total de ventas

#inician los contadores en cero
menores_iguales500 = 0 
acumuladom500 = 0
mayores500 = 0
acumuladom = 0
mayores1000 = 0
acumuladomi = 0
total = 0

for i in range(n):   #el ciclo se repite las cantidad de veces ingresadas en n
    num = int(input(f"venta {i+1}: "))  #pide el valor de la venta  actual
    total += num                        #se suma cada venta al contador total
    if num <= 500:
        menores_iguales500 += 1         #si el numero es menor o igual a 500 este contador suma 1
        acumuladom500 += num            # en este cumulador  se suma el numero
    elif num > 500 and num <= 1000:     
        mayores500 += 1                 #si el numero es mayor que 500 pero menor o igual a 1000 este contador suma 1
        acumuladom += num               # en este acumulador se suma el numero
    else:
        mayores1000 += 1                #si ninguna de las dos condiciones anteriores se cumple  este contador suma 1
        acumuladomi += num              #este otro acumulador suma el numero
        
        
#se imprimen los resultados
print(f"cantidades menores o iguales a 500: {menores_iguales500}")
print(f"el acumulado en esta categoria es: {acumuladom500}")
print(f"cantidades mayores a 500 pero menores o iguales a 1000: {mayores500}")
print(f"el acumulado en esta categoria es: {acumuladom}")
print(f"cantidades mayores a 1000: {mayores1000}")
print(f"el acumulado en esta categoria es: {acumuladomi}")
print(f"el monto total de forma global es: {total}")