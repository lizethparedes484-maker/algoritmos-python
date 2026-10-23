#problema 5 ciclos
#Crea un programa que recorra los números del 1 al 20 e imprima únicamente aquellos que sean pares, indicando al final cuántos números pares se encontraron en total.
contador = 0 #contara si el numero es par o no
for i in range (1,21,1):
    numero = i % 2   
    if (numero == 0): #si el residuo es cero
        print (i) 
        contador += 1 #el contador suma 1 porque el numero es par
   
    
print (f"los numeros pares son : {contador}")  #imprime el resultado