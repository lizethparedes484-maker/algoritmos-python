# problema 12/20
totalcomision = mayor = 0

num = int( input("¿Cuantas ventas se realizaron?"))
for i in range ( 1, num +1):
    cantidad = float(input(f"¿De cuanto es la venta {i} ?"))
    if cantidad > mayor:
        mayor = cantidad
    if cantidad > 1500:
        comision = cantidad * 0.1
    elif cantidad >= 500:
        comision = cantidad*0.05
    else:
        comision = 0
    totalcomision += comision
    
print(f"La total de comisiones es de: ${totalcomision}")
print (f"La venta mas grande es de: ${mayor}")
