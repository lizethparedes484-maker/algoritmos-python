#Determina cuánto se debe pagar por equis cantidad de lápices considerando que si son 1000 o más el costo es de $0.85; de lo contrario, el precio es de $0.90

cantidad_lapices = int(input("ingresa la cantidad de lapices:"))
if cantidad_lapices >= 1000:
    costo = 0.85
    total = costo* cantidad_lapices
else:
    costo = 0.90
    total = costo*cantidad_lapices
print("Costo por lapiz: $", costo)
print("total a pagar por los lapices:", total)
