#problema 7 ciclos
#Un sensor en la puerta de una discoteca registra la edad de 8 personas que intentan entrar. Usa un contador para determinar cuántas personas son menores de edad (menores a 18 años).

contador = 0   #inicia el contador en cero
for i in range(8):    #se repite 8 veces 
    edades  = int(input("cual es tu edad ")) #pregunta la edad(8 veces)
    if(edades < 18):  #si edades es menor a 18
        contador += 1 #el contador suma 1
print("las personas que no pueden pasar son ", contador) #se imprime el resultado
