#problema 2/20
"""
Categorización de ventas con montos acumulados: Procesa N ventas realizadas en un negocio. El programa debe determinar cuántas ventas fueron menores o iguales
a $300, cuántas entre $301 y $800, y cuántas mayores a $800. Debe mostrar lacantidad de ventas y el monto total recaudado en cada categoría, además del totalgeneral.
"""
#inician los contadores en cero
contador1 = contador2 = contador3 = 0
total =  total1 = total2 = total3 = 0
ventan = int(input("¿Cuantas ventas desea ingresar?"))  # se piden las ventas mediante un input

#inician los ciclos
for i in range(ventan):
    ventaa = float(input (f"¿De cuanto es la venta {i +1} ?")) #se repite esta pregunta el numero de veces que el usuario ingreso

    #dependiendo que condicional cumpla es a que contador se suma 1 y la venta
    #condicionales: si ventas son menores o iguales que cero
    if (ventaa <= 300 ):
        contador1 += 1
        total1 += ventaa

    #condicionales: para ventas mayores a 300 hasta 800
    elif (ventaa >300 and ventaa <=  800):
        contador2 += 1
        total2 += ventaa
        
    #condicionales: ventas mayores a 800
    else:
        contador3 += 1
        total3 += ventaa
#se suman los montos de las tres categorias
t = total1+total2+total3
#se imprimen los resultados de cada categoria y el total
print (f"La cantidad de ventas menores o iguales a 300 son: {contador1} y el monto recaudado es {total1}")
print (f"La cantidad de ventas entre $301 y $800 son: {contador2} y el monto recaudado es {total2}")
print (f"La cantidad de ventas mayores a $800 son: {contador3} y el monto recaudado es {total3}")
print (f"El acumulado total es: ${t}")
