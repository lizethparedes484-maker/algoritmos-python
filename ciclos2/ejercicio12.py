# problema 12/20
"""
Cálculo de comisión decreciente para vendedores: Un vendedor realiza N ventas. Por cada venta mayor a $1,500 obtiene una comisión del 10%; para ventas entre
$500 y $1,500 la comisión es del 5%, y para ventas menores a $500 no recibe comisión. Determina el total percibido por comisiones y el monto de la mayor venta realizada.
"""
# se inicia el acumulador total comision en cero y la variable mayor para ir comparando cada dato y obtener el mayor de estos
totalcomision = mayor = 0

num = int( input("¿Cuantas ventas se realizaron?"))          # se pregunta las ventas realizadas mediante un input
# inicia el ciclo en uno y termina en el numero de ventas realizadas mas uno
for i in range ( 1, num +1):
    cantidad = float(input(f"¿De cuanto es la venta {i} ?")) #pregunta de cunato es la venta mediante un input
    if cantidad > mayor:
        #si la venta es mayor que la variable mayor iniciada en cero, mayor cera igual a esa vemta
        mayor = cantidad
    if cantidad > 1500:
        # si la venta es mayor a 1500 la comision sera de su diez porciento
        comision = cantidad * 0.1
    elif cantidad >= 500:
        # si la venta es mayor o igual a 500 la comision sera de su cinco porciento
        comision = cantidad*0.05
    else:
        # si la venta no cumple con ninguna de las anteriores quiere decir que es menor a 500 por lo tanto no hay comision
        comision = 0
    #se cumulan todas las comisiones a totalcomision
    totalcomision += comision
#se muestran los resultados
print(f"La total de comisiones es de: ${totalcomision}")
print (f"La venta mas grande es de: ${mayor}")
