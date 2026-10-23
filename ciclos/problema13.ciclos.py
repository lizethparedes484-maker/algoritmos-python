#problema 13 ciclos
#Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes.

ahorro = 0 #inicia el contador 
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"] #se declara la lista de meses

for i in range (12 ): #ciclo que se repite 12 veces(meses de la lista)
    deposito_mes = float(input(f"cuanto depositaras en {meses[i]}:  "))  #pide la cantidad que se va a depositar 
    ahorro += deposito_mes  #la cantidad se va acumulandoen en ahorro
    print(f"el ahorro acumulado es {ahorro} ")  #se imprime lo acumulado hasta el momento
print (f"el ahorro total en el año es {ahorro}")  # se imprime el resultado total