cantidad_lapices = int(input("ingresa la cantidad de lapices:"))
if cantidad_lapices >= 1000:
    costo = 0.85
    total = costo* cantidad_lapices
else:
    costo = 0.90
    total = costo*cantidad_lapices
print("Costo por lapiz: $", costo)
print("total a pagar por los lapices:", total)