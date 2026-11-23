# problema 6/20
"""
Control de peso y sobrepeso en envíos: Se recibe un lote de N paquetes. Se debe registrar el peso de cada uno en kg. Si un paquete pesa más de 15 kg, se le aplica
un recargo de $50 de transporte. Muestra cuántos paquetes tenían sobrepeso, el total pagado en recargos y el peso medio de todo el lote.
"""
#inician los contadores y acumuladores en cero
contador  = total = media = 0

paquetes = int(input("¿Cual es el numero de paquetes?: "))  # se pregunta los paquetes a ingresar 
print ("Se debe registrar el peso de cada uno en kg")       # imprime que el peso debe de ser en kg

#ciclo que se repite el numero de veces ingresado
for i in range ( paquetes):
    peso = float(input("¿Cual es el peso del paquete ? (kg) ")) #pregunta el peso de cada paquete cuantas veces dure el ciclo
    #condional: en caso de que le paquete exceda el limte de 15 kg
    if peso > 15:
        #si este condicional se cumple 
        total += 50   # a total se le acumula 50
        contador += 1 # a contador se le summa 1
        media += peso # a media  se le acumula el peso ingresado
    #si no se cumple le anterior condicional
    else:
        media += peso # a media se le acumula el peso

#calculo del peso promedio
pesom = media/paquetes

#se imprimen los resultados 
print (f"Numero de paquetes que tiene sobrepeso: {contador}")
print (f"Cantidad pagado en recargos: ${ total}")
print (f"Peso medio de todo el lote: {pesom}kg ")
