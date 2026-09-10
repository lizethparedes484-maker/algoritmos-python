#La política de la compañía telefónica “chimefón” es: “Chismea + x -”. Cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan $1.00 peso c/u, los siguientes tres, 80¢ centavos de peso c/u, los siguientes dos minutos, 70¢ centavos de peso c/u, y a partir deldécimo minuto, 50¢ centavos de peso c/u.a (MXN). Determinar cuánto debe pagar por cada concepto una persona que realiza una llamada en moneda nacional mexicana (MXN).

duracion = int(input("cuanto duro la llamada:"))
if duracion <= 5:
    precio = 1
    kl  = precio*duracion
elif duracion > 5 and duracion <= 8:
    precio = 0.80 
    kl = (precio*duracion + 1) 
elif duracion >  8 and duracion <= 10:
    precio = 0.70  
    kl = (precio*duracion + 1.8) 
else :
    precio = 0.50
    kl = (precio*duracion + 3.8) 
print (f"el precio de la llamada es:$" ,kl)
