#problema 11 ciclos
#Revisa en un ciclo el peso registrado de 10 maletas y cuenta cuántas superan el límite de 23 kg.

contador = 0 #el contador inicia en cero
pesos_maletas =[12, 12, 12,85,43,23,87,23, 45,23]  #los pesos a evaluar son las que estan dentro de la lista

for i in range(10):    #se va a repetir 10 veces porque es la cantidad de valores dentro de la lista
    if(pesos_maletas[i] > 23):   #si el peso de la maleta es mayor a 23
        contador += 1            #el contador sumara 1
        print(f"el peso de maleta supera el limite ,{pesos_maletas[i]} kg") #imprime que maleta no puede pasar por exceso de peso
        
        
print(f"el total de las maletas mayor a 23kg son, {contador}")  #imprime el resultado
