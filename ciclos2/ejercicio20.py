#problema 20/20
#inician los contadores 
penalizacion = 0
penalizacion2 = 0
facturas = int(input("¿Cual es el numero de facturas?: ")) #pregunta el numero de facturas 
for i in range (1,facturas+1):                          #inicia el ciclo
    monto = float(input(f"¿Cual es el monto original: de la factura {i}?: ")) 
    dias_retraso = int(input("¿Cuantos son los dias de retraso?: "))
    if (dias_retraso>30 and dias_retraso<60): #si los dias de retraso son mayores a 30 la penalizacion  sera del 5% y se va acumulando en penalizacion2
        monto1=0
        monto1 += monto*1.05
        penalizacion = monto*0.05
        penalizacion2 += penalizacion
    elif (dias_retraso>1 and dias_retraso<30): #si los dias de retraso son menores a 30 nio hay penalizacion
        monto1 = monto
    elif (dias_retraso>60):                    # si los dias de retraso son mayores a 60 la penalizacion es del 12% y se acumula
        monto1=0
        monto1 += monto*1.12
        penalizacion = monto*0.12
        penalizacion2 += penalizacion
    # se imprime cada monto y su penalizacion
    print(f"La penalizacion de la factura es {i} es de {penalizacion}")
    print(f"El monto original de la factura {i} {monto} y el monto final es: {monto1}")
print (f"La penalizacion total {penalizacion2}")  # imprime la penalizacion acumulada
