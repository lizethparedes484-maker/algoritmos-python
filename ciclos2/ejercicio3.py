#problema 3/20
"""
Inversión con interés compuesto anual: Un inversionista inicia con un capital inicial de $2,000 y recibe un rendimiento del 8% anual acumulado durante N años. Genera
un reporte que muestre el capital ganado en cada uno de los años y el saldo final acumulado al terminar el periodo.
"""
capital = 2000   #capital inicial
total = 0        #inicia el acumulador para el total
N = int(input("¿Cuantos son los años?: "))   #pregunta la cantidad de años con un input

#se inician los ciclos
for i in range(N):

    #se acumula el incremento sobre el capital actual
    capital += capital*0.08
    #acumulamos lo anterior dentro de total
    total += capital
    #se imprime como va el monto en cada año actual 
    print(f"El sueldo ganado en el año {i + 1} es: {capital}")
#se imprime la suma acumulada de todos los años 
print("El salario al cabo del total de años es", total)
