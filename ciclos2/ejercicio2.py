#problema 2/20
#inician los contadores 
contador1 = contador2 = contador3 = 0
total =  total1 = total2 = total3 = 0
ventan = int(input("¿Cuantas ventas desea ingresar?"))  # se piden las ventas 

for i in range(ventan):
    ventaa = float(input (f"¿De cuanto es la venta {i +1} ?"))
    if (ventaa <= 300 ):
        contador1 += 1
        total1 += ventaa
    elif (ventaa >300 and ventaa <=  800):
        contador2 += 1
        total2 += ventaa
    else:
        contador3 += 1
        total3 += ventaa
t = total1+total2+total3
print (f"La cantidad de ventas menores o iguales a 300 son: {contador1} y el monto recaudado es {total1}")
print (f"La cantidad de ventas entre $301 y $800 son: {contador2} y el monto recaudado es {total2}")
print (f"La cantidad de ventas mayores a $800 son: {contador3} y el monto recaudado es {total3}")
print (f"El acumulado total es: ${t}")
