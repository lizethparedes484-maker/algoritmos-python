#problema 14/20
diftotal = 0
cantidadp = int(input("¿Cual sera la cantidad de productos a ingresar?"))
for i in range (1,cantidadp + 1):
    precios = float(input(f"¿Cual es el precio del producto {i}?"))
    if precios > 500:
        aumento = precios * 0.12
       
    elif precios >= 100 and precios < 500:
        aumento =precios * 0.08
        
    else:
        aumento = precios * 0.05
    
    now = precios + aumento
    diferencia = now - precios
    diftotal += diferencia
    print (f"El precio anterior del producto {i} es de {precios}, y el  actual es de {now} ")
print(f"La diferencia total es de {diftotal}")
