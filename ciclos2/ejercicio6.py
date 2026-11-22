# problema 6/20
contador  = total = media = 0


paquetes = int(input("¿Cual es el numero de paquetes?: "))
print ("Se debe registrar el peso de cada uno en kg")
for i in range ( paquetes):
    peso = float(input("¿Cual es el peso del paquete ? (kg) "))
    if peso > 15:
        total += 50
        contador += 1
        media += peso
    else:
        media += peso
pesom = media/paquetes

print (f"Numero de paquetes que tiene sobrepeso: {contador}")
print (f"Cantidad pagado en recargos: ${ total}")
print (f"Peso medio de todo el lote: {pesom}kg ")
