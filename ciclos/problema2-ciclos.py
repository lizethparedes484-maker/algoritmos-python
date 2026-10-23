#problema 2 ciclos
#Mostrar la tabla de multiplicar de un n numero ingresado por teclado
numero = int(input(" ingrese un numero para saber su tabla de multiplicar"))  #pide a usuario un numero cualsea
for i in range (1, 11, 1):    # i va a empezar desde el 1 hasta el 10 de uno en uno
    tabla = (i*numero)        #la variable tabla va a guardar el resultado de la multiplicacion
    print (f" {numero} por {i} es: {tabla}")   # se imprime el resultado(tabla de multiplicar)