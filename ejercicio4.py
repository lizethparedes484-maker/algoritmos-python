#La compañía de autobuses “La curva loca” requiere determinar el costo que tendrá el boleto de un viaje sencillo, esto basado en los kilómetros por recorrer y en el costo por kilómetro.
#guardamos el costo en una variable
km = 80

#le preguntamos al usuario cuantos kilometros va a recorrer
km_recorridos = int(input("¿cuantos kilometros va a recorrer?"))

# Sacamos la cuenta multiplicando los kilómetros por la tarifa
costo_total = km_recorridos* km

#mostramos el total
print (f"su total a pagar es: ${costo_total}")
