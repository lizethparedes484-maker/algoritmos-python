#La política de la compañía telefónica “chimefón” es: “Chismea + x -”. Cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan $1.00 peso c/u, los siguientes tres, 80¢ centavos de peso c/u, los siguientes dos minutos, 70¢ centavos de peso c/u, y a partir deldécimo minuto, 50¢ centavos de peso c/u.a (MXN). Determinar cuánto debe pagar por cada concepto una persona que realiza una llamada en moneda nacional mexicana (MXN).
# Pedimos la duración de la llamada en minutos
duracion = int(input("cuanto duro la llamada:"))

# Evaluamos la duración para calcular la tarifa acumulada:
# duracion 1: Primeros 5 minutos, costo de $1.00 por minuto
if duracion <= 5:
if duracion <= 5:
    precio = 1
    kl  = precio*duracion

# duracion 2: De 6 a 8 minutos, $0.80 por cada minuto extra + $1.00 base 
elif duracion > 5 and duracion <= 8:
    precio = 0.80 
    kl = (precio*duracion + 1) 

# duracion3: De 9 a 10 minutos, $0.70 por cada minuto extra + $1.80 base 
elif duracion >  8 and duracion <= 10:
    precio = 0.70  
    kl = (precio*duracion + 1.8) 

# duracion 4: Más de 10 minutos, $0.50 por cada minuto extra a partir del minuto 11 + $3.80 
else :
    precio = 0.50
    kl = (precio*duracion + 3.8) 
#mostramos el resultado final
print (f"el precio de la llamada es:$" ,kl)
