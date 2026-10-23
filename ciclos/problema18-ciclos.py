#problema 18 ciclos

#ambos contadores inician en cero
total = 0
htotal = 0
horas = int(input("cuantas horas trabaja por dia "))  #pide cuantas horas trabajadas hay
pago = float(input("cuanto gana por hora"))           #pide el salario por hora
for i in range (6):                                   #ciclo que se repite 6 veces
    total += 1                                        #total suma 1
    htotal += 1                                       #htotal suma 1
totalhoras = htotal * horas                           #calcula el total de horas con una multiplicacion
pagototal = totalhoras* pago                          #calcula el pago total
#imprime los resultados
print (f"el total de horas trabajadas son: {totalhoras}")
print(f"el sueldo por esas horas es: {pagototal}")