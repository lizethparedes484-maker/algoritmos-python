#problema 19 ciclos
#Un profesor tiene un salario inicial de $1500, y recibe un incremento de 10 % anual durante 6 años. ¿Cuál es su salario al cabo de 6 años? ¿Qué salario ha recibido en cada uno de los 6 años? Realice el algoritmo

salary = 1500 # se define el sueldo inicial
    
salario = 0   #el contador comienza en cero
acumulador = 0  #este tambien inicia en cero
for i in range (1, 7):   # el ciclo se va repetir del 1 al 6
    salary += salary * 0.10  #se calcula el 10% sobre el salario de cada año
    
    salario += 1        # salario suma 1
    acumulador += salary  # acumulador suma el salario fijo
    
    print(f"el salario en {i} es {salary}")  # se imprime el salrio del año correspondiente
print (f"el salrio acumulado al cabo de 6 años es {acumulador}")   #se imprime el resultado
