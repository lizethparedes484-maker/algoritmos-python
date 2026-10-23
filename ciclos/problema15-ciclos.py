#problema 15 ciclos
#Realice un algoritmo para generar e imprimir los números pares que se encuentran entre 0 y 100.
contador = 0  #contador inicia en cero
for i in range(101):  #el ciclo se repite del 0 al 100
    if(i%2 == 0):     #el numero es par si el residuo es cero
        print(f"el numero {i} es par")  #se imprime cual numero es par
        contador += 1  #contador suma 1
print(f"el total de numeros pares son: {contador}") #imprimimos el total de numeros pares
