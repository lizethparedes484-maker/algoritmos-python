#Se requiere determinar el costo que tendrá realizar una llamada telefónica con base en el tiempo que dura la llamada y en el costo por minuto. costo por minuto: $3.00 mxn
# Le pedimos al usuario que ingrese la duración de la llamada en minutos 
minuto = int(input("ingrese los minutos de llamada"))

# Guardamos el costo de cada minuto
costo_minuto = 3

# Multiplicamos la cantidad de minutos por el costo para sacar el total
costo_llamada = minuto* costo_minuto

#mostramos el resultado
print(f"su total a pagar es:, {costo_llamada}$")
