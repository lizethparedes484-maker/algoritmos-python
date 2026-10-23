#problema 3 ciclos
#Pide al usuario que ingrese 5 números enteros uno por uno. Al finalizar la lectura, muestra la suma total de todos los números ingresados.
suma = 0       # suma va a servir como contador por eso se declara en cero
for i in range (5):  # i se va a repetir 5 veces
    numero = int(input(" ingrese un numero "))   #le pide al usuario ingresar un numero 
    suma += numero   #en suma se va a sumar cada numero ingresado
    
print (f" la suma de los 5 numeros es: {suma}")   #se imprime el resultado de la suma total