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