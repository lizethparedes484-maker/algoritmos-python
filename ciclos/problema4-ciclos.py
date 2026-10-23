#problema 4 ciclos
#Pide al usuario que ingrese N números enteros enteros uno por uno. Al finalizar la lectura, muestra la suma total de todos los números ingresados
n = int(input(" cuantos numeros desea ingresar:"))   #le pide al usuario la cantidad de numeros a sumar 
suma = 0         # suma va a servir como contador por eso se declara en cero
for i in range (1,n+1,1):    #i va a comenzar en uno, hasta el numero ingresado, de uno a uno
    numero = int(input(f" ingrese el numero {i} ")) #el texto "ingrese numero" se va a repetir la cantida de veces de n
    suma += numero          #se suma cada numero ingresado y los acumula
    
print (f" la suma de los numeros es: {suma}")       #imprime el resultado