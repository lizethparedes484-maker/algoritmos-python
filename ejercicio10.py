#Determina cuánto se debe pagar por equis cantidad de lápices considerando que si son 1000 o más el costo es de $0.85; de lo contrario, el precio es de $0.90
# Pedimos al usuario la cantidad de lápices que desea comprar
cantidad_lapices = int(input("ingresa la cantidad de lapices:"))

# Evaluamos si la compra es de 1000 lápices o más
if cantidad_lapices >= 1000:
    #si es verdad, aplicamos el costo con descuento 
    costo = 0.85
    total = costo* cantidad_lapices
#si la compra es menor a 1000 lapices
else:
    # Aplicamos el costo unitario normal
    costo = 0.90
    total = costo*cantidad_lapices
#imrimimos y mostramos el precio de cada lapiz y el acumulado
print("Costo por lapiz: $", costo)
print("total a pagar por los lapices:", total)
