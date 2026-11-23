#problema 20/20
"""
Procesamiento de facturas vencidas: Un departamento de cobranza procesa N facturas. 
Por cada una se lee el monto original y los días de retraso. 
Si los días de retraso son mayores a 30, se le aplica un recargo del 5%; si son mayores a 60 días, el recargo es del 12%.
Muestra el importe corregido de cada factura y el monto acumulado por penalizaciones.
"""
#inician los acumuladores
penalizacion = 0
penalizacion2 = 0
facturas = int(input("¿Cual es el numero de facturas?: ")) #pregunta el numero de facturas mediante un input
for i in range (1,facturas+1):                          #inicia el ciclo
    monto = float(input(f"¿Cual es el monto original: de la factura {i}?: ")) 
    dias_retraso = int(input("¿Cuantos son los dias de retraso?: "))

    #si los dias de retraso son mayores a 30 la penalizacion  sera del 5% y se va acumulando en penalizacion2
    if (dias_retraso>30 and dias_retraso<60): 
        monto1=0
        monto1 += monto*1.05
        penalizacion = monto*0.05
        penalizacion2 += penalizacion
        
    #si los dias de retraso son menores a 30 nio hay penalizacion
    elif (dias_retraso>1 and dias_retraso<30): 
        monto1 = monto

     # si los dias de retraso son mayores a 60 la penalizacion es del 12% y se acumula
    elif (dias_retraso>60):                   
        monto1=0
        monto1 += monto*1.12
        penalizacion = monto*0.12
        penalizacion2 += penalizacion
        
    # se imprime cada monto y su penalizacion
    print(f"La penalizacion de la factura es {i} es de {penalizacion}")
    print(f"El monto original de la factura {i} {monto} y el monto final es: {monto1}")

# imprime la penalizacion acumulada
print (f"La penalizacion total {penalizacion2}")
