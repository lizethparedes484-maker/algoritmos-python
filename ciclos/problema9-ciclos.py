#problema 9 ciclos
#Revisa la entrada de peso de 10 maletas en un ciclo y cuenta cuántas superan el límite de 23 kg.
contador = 0 #el contador inicia en cero

for i in range(1,11,1): #se repite 10 veces iniciando en 1 y de  uno en uno
    pesos_maletas = int(input(f"cual es el peso de la maleta {i}, ")) #se pide el peso de la maleta(10 veces)
    if(pesos_maletas > 23):  #si el peso de la maleta es mayor a 23
        contador += 1        #contador suma 1
     
                
print(f"el total de las maletas mayor a 23kg son, {contador}") #imprime el resultado