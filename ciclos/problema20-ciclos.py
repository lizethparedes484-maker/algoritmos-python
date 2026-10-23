#problema 20 ciclos

#se inician los tres contadores uqe se van a utilizar
verde =  0
rojo = 0
blanco = 0

numerofoco = int(input("cual es la cantidad de focos")) #pide la cantidad de focos a contar

for i in range (numerofoco): #el ciclo se va a repetir la cantidad de veces ingresada en numerofoco
    color = input("cual es el color del foco(verde, rojo, blanco): ") #pregunta el color de cada foco
    if (color == "verde"):  
        verde += 1          #si el color es verde este contador suma 1
    elif (color == "rojo"):
        rojo +=1            #si es rojo este contador suma 1
    else:
        blanco += 1         #si no es ninguno de los anteriores el contador blanco suma 1

#se imprimen los resultados
print(f"el numero de focos verdes es:{verde}")
print(f"el numero de focos rojos es:{rojo}")
print(f"el numero de focos blancos es:{blanco}")
