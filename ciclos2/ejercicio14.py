#problema 14/20
"""
Actualización de precios por inflación: Una lista de N productos tiene sus precios actuales.
La empresa aplicará un aumento del 5% a los productos que cuesten menos de $100, un 8% a los que cuesten entre $100 y $500, y un 12% a los mayores de $500. 
Imprime el costo anterior, el nuevo costo de cada producto y la diferencia total sumada del ajuste.
"""
#se inicia el acumulador en cero
diftotal = 0

#pregunta la cantidad de productos a ingresar mediante un input
cantidadp = int(input("¿Cual sera la cantidad de productos a ingresar?"))
#ciclo que empieza en uno y recorre hasta terminar en cantidadp mas uno
for i in range (1,cantidadp + 1):
    precios = float(input(f"¿Cual es el precio del producto {i}?")) # pregunta el precio de cada producto mediante un input

    #inician los condicionales para clasificar cada precio ingresado
    if precios > 500:
        #si el precio es mayor a 500 el aumento sera del 12 porciento del mismo precio
        aumento = precios * 0.12
       
    elif precios >= 100 and precios < 500:
        #si el precio es mayor o igual a 100 pero menor a 500 el aumento sera de 8 porciento
        aumento =precios * 0.08
        
    else:
        # sino cumple ninguno de los condicionales anteriores el aumento solo es del 5 porciento
        aumento = precios * 0.05
    
    now = precios + aumento     #calculo del precio actualizado sumandole a precio el aumento
    diferencia = now - precios  #calcula la diferencia entre el precio actual y el anterior
    diftotal += diferencia      #suma esa diferencia a el acumulador diftotal
    #imprime el precio anterior y el actualizado 
    print (f"El precio anterior del producto {i} es de {precios}, y el  actual es de {now} ")
    
#imprime la diferencia total
print(f"La diferencia total es de {diftotal}")
