# problema 7/20
"""
Registro de temperaturas extremas y promedios: Registra las temperaturas máximas
de cada día del mes (30 días). Determina cuál fue la temperatura más alta
registrada, la más baja y calcula el promedio mensual de temperatura.
"""
media = 0 #inicia el acumulador en cero
#estos dos serviran para iniciar el valor en cero y con este comparar a los demas 
mayor = 0
menor = 0

#inicia el ciclo que se va repetir treinta veces 
for i in range (1,31,1):
    temperatura = float(input(f"cual es la temperatura en el dia {i} ")) #pregunta la temperatura del dia mediante un input
    #si i es igual a 1 ambas variables son menor al mismo tiempo de aqui inician para despues irse comparando ya ctualizando
    if i == 1:
        menor = temperatura
        mayor = temperatura
    #si la temperatura ingresada es menor que la variable menor, el valor de esa temperatura se guarda en menor
    if temperatura < menor:
        menor = temperatura
    #si la temperatura es mayor que la variable mayor, el valor de esa temperatura se guarda en mayor
    if temperatura > mayor:
        mayor = temperatura
    #todas las temperaturas ingresadas se acumulan es media 
    media += temperatura

#calculo para temperatura promedio
tempm= media/30

#se imprimen todos los resultados
print (f"la temperatura mas alta registrada es: {mayor}")
print (f"la temperatura mas baja registrada es: { menor}")
print (f"la temperatura media del mes es: {tempm} ")
