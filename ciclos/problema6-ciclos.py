#problema 6 ciclos
#Diseñe una aplicación que permita ingresar n números y muestre y sume los números pares.
num = int(input("ingrese la cantidad: "))    #se pide un numero que servira como el limite 
contador = 0                                 #se utiliza un contador para ver si seran pares o no y aqui se van a acumular
for i in range (1,num+1,1):                  #se repite el codigo hasta llegar a 0
    num = i % 2                              #se saca el residuo
    if (num == 0):                           # si el residuo del numero es cero
        print (i) 
        contador += 1                        #contador suma 1
  

print (f"los numeros pares son : {contador}")#se muestra el resultado