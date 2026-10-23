#problema 12 ciclos
#Realizar un algoritmo que pida N números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

#estos tres son solo contadores que inician en cero
mmo = 0
numimayor = 0
numermenorig = 0
numero = int(input("cuantos numeros desea ingresar"))  #fuera del rango se pide lo numeros ingresar

#se repite el ciclo segun la cantidad de numeros ingresada anteriormente
for i in range (numero) :   
    mmo = float(input("cual es el numero: "))  
    if mmo <= 0:  #si el numero es menor o igual a cero
        numermenorig += 1  #este contador suma 1
    else:         # si la primera condicion no se cumple
        numimayor += 1     #este otro contador es el que suma

#se imprimen los resultados
print("cantidades iguales o menores que cero ,", numermenorig)
print("cantidades mayores ,", numimayor)